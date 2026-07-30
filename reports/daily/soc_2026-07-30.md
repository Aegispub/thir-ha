# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-30 |
| **Generated At** | 2026-07-30T23:12:18Z |
| **Shift Time** | 23:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **165** |
| Confirmed Threats | **147** |
| False Positives Filtered | **18** (10.9%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **24** |
| High Severity Cases | **56** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **109** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **77** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **11** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **65** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `default` | 14 |
| `guest` | 12 |
| `support` | 11 |
| `supervisor` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin123` | 5 |
| `123123123` | 5 |
| `default4` | 4 |
| `LeitboGi0ro` | 4 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `guest` | `123123123` | 5 |
| `guest` | `admin123` | 4 |
| `default` | `default4` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Password1` | `80.94.92.55` | 2026-07-30T20:56:58 |
| `guest` | `admin123` | `220.189.209.18` | 2026-07-30T20:57:14 |
| `default` | `default4` | `61.2.228.177` | 2026-07-30T20:59:43 |
| `root` | `admin` | `80.94.92.55` | 2026-07-30T20:59:46 |
| `default` | `default4` | `49.124.154.163` | 2026-07-30T20:59:52 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-30T21:00:36 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-30T21:00:37 |
| `root` | `admin123` | `80.94.92.55` | 2026-07-30T21:01:51 |
| `root` | `default` | `80.94.92.55` | 2026-07-30T21:04:32 |
| `guest` | `1qaz2wsx` | `10.0.0.73` | 2026-07-30T21:06:24 |
| `root` | `letmein` | `80.94.92.55` | 2026-07-30T21:06:26 |
| `default` | `default4` | `106.13.181.87` | 2026-07-30T21:07:34 |
| `default` | `default4` | `74.208.177.56` | 2026-07-30T21:07:48 |
| `default` | `default12345` | `117.248.201.39` | 2026-07-30T21:08:29 |
| `root` | `passw0rd` | `80.94.92.55` | 2026-07-30T21:09:10 |
| `guest` | `admin123` | `10.0.0.73` | 2026-07-30T21:09:11 |
| `root` | `password` | `80.94.92.55` | 2026-07-30T21:11:02 |
| `root` | `qwerty` | `80.94.92.55` | 2026-07-30T21:12:50 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-30T21:14:43 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-30T21:14:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.132.248` | 2026-07-30T21:15:21 |
| `root` | `system` | `80.94.92.55` | 2026-07-30T21:16:25 |
| `support` | `support` | `176.53.159.196` | 2026-07-30T21:16:52 |
| `default` | `default12345` | `182.151.45.136` | 2026-07-30T21:25:11 |
| `guest` | `1qaz2wsx` | `182.156.35.238` | 2026-07-30T21:25:36 |
| `guest` | `admin123` | `65.20.161.126` | 2026-07-30T21:27:02 |
| `guest` | `123123123` | `10.0.0.73` | 2026-07-30T21:27:57 |
| `default` | `default7` | `1.212.225.99` | 2026-07-30T21:32:17 |
| `default` | `default7` | `115.46.88.68` | 2026-07-30T21:32:31 |
| `guest` | `123123123` | `93.42.222.164` | 2026-07-30T21:33:17 |
| `operator` | `qwerty1` | `10.0.0.73` | 2026-07-30T21:41:11 |
| `guest` | `123123123` | `222.75.225.206` | 2026-07-30T21:41:12 |
| `guest` | `123123123` | `61.184.128.210` | 2026-07-30T21:41:21 |
| `debian` | `debian2` | `10.0.0.73` | 2026-07-30T21:41:39 |
| `root` | `Lg!123456` | `20.255.152.112` | 2026-07-30T21:42:10 |
| `345gs5662d34` | `345gs5662d34` | `20.255.152.112` | 2026-07-30T21:42:13 |
| `root` | `3245gs5662d34` | `20.255.152.112` | 2026-07-30T21:42:15 |
| `default` | `default7` | `10.0.0.73` | 2026-07-30T21:44:14 |
| `mati` | `mati` | `2.26.50.151` | 2026-07-30T21:45:40 |
| `345gs5662d34` | `345gs5662d34` | `2.26.50.151` | 2026-07-30T21:45:42 |
| `mati` | `3245gs5662d34` | `2.26.50.151` | 2026-07-30T21:45:43 |
| `support` | `support` | `10.0.0.73` | 2026-07-30T21:48:30 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-30T21:57:27 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-30T21:57:27 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-30T21:57:35 |
| `operator` | `qwerty1` | `27.128.162.146` | 2026-07-30T21:59:47 |
| `debian` | `debian2` | `117.216.33.31` | 2026-07-30T21:59:50 |
| `supervisor` | `webadmin` | `196.190.180.18` | 2026-07-30T22:07:01 |
| `supervisor` | `webadmin` | `117.250.250.2` | 2026-07-30T22:07:10 |
| `support` | `password@123` | `10.0.0.73` | 2026-07-30T22:15:34 |
| `support` | `5555555` | `10.0.0.73` | 2026-07-30T22:16:15 |
| `supervisor` | `webadmin` | `10.0.0.73` | 2026-07-30T22:18:58 |
| `root` | `Js123456` | `101.47.159.50` | 2026-07-30T22:33:06 |
| `345gs5662d34` | `345gs5662d34` | `101.47.159.50` | 2026-07-30T22:33:10 |
| `root` | `3245gs5662d34` | `101.47.159.50` | 2026-07-30T22:33:12 |
| `support` | `password@123` | `116.114.84.246` | 2026-07-30T22:34:32 |
| `support` | `5555555` | `217.150.37.249` | 2026-07-30T22:34:41 |
| `support` | `password@123` | `213.55.79.195` | 2026-07-30T22:34:44 |
| `default` | `default44` | `178.178.222.53` | 2026-07-30T22:40:19 |
| `default` | `default44` | `178.178.194.136` | 2026-07-30T22:40:27 |
| `root` | `2wsx#EDC` | `218.4.156.254` | 2026-07-30T22:42:04 |
| `default` | `default44` | `111.171.127.190` | 2026-07-30T22:48:22 |
| `default` | `default44` | `111.70.32.51` | 2026-07-30T22:48:32 |
| `centos` | `centos33` | `10.0.0.73` | 2026-07-30T22:50:45 |
| `supervisor` | `logon` | `10.0.0.73` | 2026-07-30T22:51:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **165** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 26 |
| libssh | 15 |
| Go SSH scanner | 12 |
| Paramiko (Python) | 9 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 26 | 26 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 26 | 26 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 9 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `80.94.92.55`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.255.152.112`, `101.47.159.50`, `2.26.50.151`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **46** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS396982` | Google LLC | 6 | LOW |
| `AS9829` | National Internet Backbone | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (55)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aa3c3702ecb2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 20:56 |
| **Last Seen** | 2026-07-30 20:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 20:56:50` | `cowrie.session.connect` |
| `2026-07-30 20:56:52` | `cowrie.client.version` |
| `2026-07-30 20:56:52` | `cowrie.client.kex` |
| `2026-07-30 20:56:58` | `cowrie.login.success` |
| `2026-07-30 20:57:01` | `cowrie.session.params` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.success` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:01` | `cowrie.command.input` |
| `2026-07-30 20:57:02` | `cowrie.log.closed` |
| `2026-07-30 20:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22db65fccdc9

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-07-30 20:57 |
| **Last Seen** | 2026-07-30 20:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 20:57:11` | `cowrie.session.connect` |
| `2026-07-30 20:57:12` | `cowrie.client.version` |
| `2026-07-30 20:57:12` | `cowrie.client.kex` |
| `2026-07-30 20:57:14` | `cowrie.login.success` |
| `2026-07-30 20:57:15` | `cowrie.direct-tcpip.request` |
| `2026-07-30 20:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4d7e4ec398

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-30 20:59 |
| **Last Seen** | 2026-07-30 20:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 20:59:40` | `cowrie.session.connect` |
| `2026-07-30 20:59:41` | `cowrie.client.version` |
| `2026-07-30 20:59:41` | `cowrie.client.kex` |
| `2026-07-30 20:59:43` | `cowrie.login.success` |
| `2026-07-30 20:59:44` | `cowrie.direct-tcpip.request` |
| `2026-07-30 20:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4150d19bf43e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 20:59 |
| **Last Seen** | 2026-07-30 20:59 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 20:59:40` | `cowrie.session.connect` |
| `2026-07-30 20:59:41` | `cowrie.client.version` |
| `2026-07-30 20:59:41` | `cowrie.client.kex` |
| `2026-07-30 20:59:46` | `cowrie.login.success` |
| `2026-07-30 20:59:50` | `cowrie.session.params` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.success` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:50` | `cowrie.command.input` |
| `2026-07-30 20:59:52` | `cowrie.log.closed` |
| `2026-07-30 20:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28699492003a

| Field | Detail |
|---|---|
| **Source IP** | `49.124.154[.]163` |
| **First Seen** | 2026-07-30 20:59 |
| **Last Seen** | 2026-07-30 20:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 20:59:49` | `cowrie.session.connect` |
| `2026-07-30 20:59:49` | `cowrie.client.version` |
| `2026-07-30 20:59:49` | `cowrie.client.kex` |
| `2026-07-30 20:59:52` | `cowrie.login.success` |
| `2026-07-30 20:59:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 20:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.154[.]163` to AbuseIPDB if not already reported
- [ ] Block `49.124.154[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41459523436

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 21:00 |
| **Last Seen** | 2026-07-30 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:00:35` | `cowrie.session.connect` |
| `2026-07-30 21:00:35` | `cowrie.client.version` |
| `2026-07-30 21:00:35` | `cowrie.client.kex` |
| `2026-07-30 21:00:36` | `cowrie.login.success` |
| `2026-07-30 21:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10c2063f1db0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 21:00 |
| **Last Seen** | 2026-07-30 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:00:36` | `cowrie.session.connect` |
| `2026-07-30 21:00:36` | `cowrie.client.version` |
| `2026-07-30 21:00:36` | `cowrie.client.kex` |
| `2026-07-30 21:00:37` | `cowrie.login.success` |
| `2026-07-30 21:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3492ac1babb7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:01 |
| **Last Seen** | 2026-07-30 21:01 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:01:44` | `cowrie.session.connect` |
| `2026-07-30 21:01:45` | `cowrie.client.version` |
| `2026-07-30 21:01:45` | `cowrie.client.kex` |
| `2026-07-30 21:01:51` | `cowrie.login.success` |
| `2026-07-30 21:01:55` | `cowrie.session.params` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.success` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:55` | `cowrie.command.input` |
| `2026-07-30 21:01:56` | `cowrie.log.closed` |
| `2026-07-30 21:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92f35b64fe9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:04 |
| **Last Seen** | 2026-07-30 21:04 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:04:21` | `cowrie.session.connect` |
| `2026-07-30 21:04:23` | `cowrie.client.version` |
| `2026-07-30 21:04:23` | `cowrie.client.kex` |
| `2026-07-30 21:04:32` | `cowrie.login.success` |
| `2026-07-30 21:04:37` | `cowrie.session.params` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.success` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:37` | `cowrie.command.input` |
| `2026-07-30 21:04:38` | `cowrie.log.closed` |
| `2026-07-30 21:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1e77d9eacf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:06 |
| **Last Seen** | 2026-07-30 21:06 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:06:16` | `cowrie.session.connect` |
| `2026-07-30 21:06:18` | `cowrie.client.version` |
| `2026-07-30 21:06:18` | `cowrie.client.kex` |
| `2026-07-30 21:06:26` | `cowrie.login.success` |
| `2026-07-30 21:06:31` | `cowrie.session.params` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.success` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:31` | `cowrie.command.input` |
| `2026-07-30 21:06:34` | `cowrie.log.closed` |
| `2026-07-30 21:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ee2ed650c2

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]87` |
| **First Seen** | 2026-07-30 21:07 |
| **Last Seen** | 2026-07-30 21:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:07:29` | `cowrie.session.connect` |
| `2026-07-30 21:07:30` | `cowrie.client.version` |
| `2026-07-30 21:07:30` | `cowrie.client.kex` |
| `2026-07-30 21:07:34` | `cowrie.login.success` |
| `2026-07-30 21:07:35` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]87` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a2e8782d95

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-07-30 21:07 |
| **Last Seen** | 2026-07-30 21:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:07:46` | `cowrie.session.connect` |
| `2026-07-30 21:07:47` | `cowrie.client.version` |
| `2026-07-30 21:07:47` | `cowrie.client.kex` |
| `2026-07-30 21:07:48` | `cowrie.login.success` |
| `2026-07-30 21:07:48` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6d7d6b3eb9

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-07-30 21:08 |
| **Last Seen** | 2026-07-30 21:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:08:26` | `cowrie.session.connect` |
| `2026-07-30 21:08:27` | `cowrie.client.version` |
| `2026-07-30 21:08:27` | `cowrie.client.kex` |
| `2026-07-30 21:08:29` | `cowrie.login.success` |
| `2026-07-30 21:08:29` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4adaedd5bf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:08 |
| **Last Seen** | 2026-07-30 21:09 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:08:53` | `cowrie.session.connect` |
| `2026-07-30 21:08:56` | `cowrie.client.version` |
| `2026-07-30 21:08:56` | `cowrie.client.kex` |
| `2026-07-30 21:09:10` | `cowrie.login.success` |
| `2026-07-30 21:09:15` | `cowrie.session.params` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.success` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:15` | `cowrie.command.input` |
| `2026-07-30 21:09:17` | `cowrie.log.closed` |
| `2026-07-30 21:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db64dc08dad

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:10 |
| **Last Seen** | 2026-07-30 21:11 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:10:45` | `cowrie.session.connect` |
| `2026-07-30 21:10:49` | `cowrie.client.version` |
| `2026-07-30 21:10:49` | `cowrie.client.kex` |
| `2026-07-30 21:11:02` | `cowrie.login.success` |
| `2026-07-30 21:11:08` | `cowrie.session.params` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.success` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:08` | `cowrie.command.input` |
| `2026-07-30 21:11:11` | `cowrie.log.closed` |
| `2026-07-30 21:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7443e4b5773

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:12 |
| **Last Seen** | 2026-07-30 21:13 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:12:34` | `cowrie.session.connect` |
| `2026-07-30 21:12:37` | `cowrie.client.version` |
| `2026-07-30 21:12:37` | `cowrie.client.kex` |
| `2026-07-30 21:12:50` | `cowrie.login.success` |
| `2026-07-30 21:12:57` | `cowrie.session.params` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.success` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:57` | `cowrie.command.input` |
| `2026-07-30 21:12:59` | `cowrie.log.closed` |
| `2026-07-30 21:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf56c53cd2e3

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-30 21:14 |
| **Last Seen** | 2026-07-30 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:14:42` | `cowrie.session.connect` |
| `2026-07-30 21:14:42` | `cowrie.client.version` |
| `2026-07-30 21:14:43` | `cowrie.client.kex` |
| `2026-07-30 21:14:43` | `cowrie.login.success` |
| `2026-07-30 21:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d034419dcf

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-30 21:14 |
| **Last Seen** | 2026-07-30 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:14:43` | `cowrie.session.connect` |
| `2026-07-30 21:14:43` | `cowrie.client.version` |
| `2026-07-30 21:14:44` | `cowrie.client.kex` |
| `2026-07-30 21:14:44` | `cowrie.login.success` |
| `2026-07-30 21:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d288298ecc5

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-30 21:15 |
| **Last Seen** | 2026-07-30 21:17 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:15:01` | `cowrie.session.connect` |
| `2026-07-30 21:15:01` | `cowrie.client.version` |
| `2026-07-30 21:15:02` | `cowrie.client.kex` |
| `2026-07-30 21:15:02` | `cowrie.login.success` |
| `2026-07-30 21:15:04` | `cowrie.session.file_upload` |
| `2026-07-30 21:15:05` | `cowrie.session.params` |
| `2026-07-30 21:15:05` | `cowrie.command.input` |
| `2026-07-30 21:15:05` | `cowrie.command.input` |
| `2026-07-30 21:15:05` | `cowrie.command.input` |
| `2026-07-30 21:15:05` | `cowrie.command.failed` |
| `2026-07-30 21:15:06` | `cowrie.log.closed` |
| `2026-07-30 21:15:07` | `cowrie.session.params` |
| `2026-07-30 21:15:07` | `cowrie.command.input` |
| `2026-07-30 21:15:07` | `cowrie.log.closed` |
| `2026-07-30 21:15:08` | `cowrie.session.params` |
| `2026-07-30 21:15:08` | `cowrie.command.input` |
| `2026-07-30 21:15:08` | `cowrie.log.closed` |
| `2026-07-30 21:15:09` | `cowrie.session.params` |
| `2026-07-30 21:15:09` | `cowrie.command.input` |
| `2026-07-30 21:15:09` | `cowrie.command.failed` |
| `2026-07-30 21:15:09` | `cowrie.command.failed` |
| `2026-07-30 21:16:10` | `cowrie.session.params` |
| `2026-07-30 21:16:10` | `cowrie.command.input` |
| `2026-07-30 21:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abceac02f4c0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-30 21:16 |
| **Last Seen** | 2026-07-30 21:16 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:16:13` | `cowrie.session.connect` |
| `2026-07-30 21:16:15` | `cowrie.client.version` |
| `2026-07-30 21:16:15` | `cowrie.client.kex` |
| `2026-07-30 21:16:25` | `cowrie.login.success` |
| `2026-07-30 21:16:31` | `cowrie.session.params` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.success` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:31` | `cowrie.command.input` |
| `2026-07-30 21:16:33` | `cowrie.log.closed` |
| `2026-07-30 21:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f971514f69b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 21:16 |
| **Last Seen** | 2026-07-30 21:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:16:52` | `cowrie.session.connect` |
| `2026-07-30 21:16:52` | `cowrie.client.version` |
| `2026-07-30 21:16:52` | `cowrie.client.kex` |
| `2026-07-30 21:16:52` | `cowrie.login.success` |
| `2026-07-30 21:16:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:16:53` | `cowrie.direct-tcpip.data` |
| `2026-07-30 21:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac4346513849

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-30 21:25 |
| **Last Seen** | 2026-07-30 21:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:25:09` | `cowrie.session.connect` |
| `2026-07-30 21:25:09` | `cowrie.client.version` |
| `2026-07-30 21:25:09` | `cowrie.client.kex` |
| `2026-07-30 21:25:11` | `cowrie.login.success` |
| `2026-07-30 21:25:12` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b50c6a3401

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-30 21:25 |
| **Last Seen** | 2026-07-30 21:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:25:33` | `cowrie.session.connect` |
| `2026-07-30 21:25:34` | `cowrie.client.version` |
| `2026-07-30 21:25:34` | `cowrie.client.kex` |
| `2026-07-30 21:25:36` | `cowrie.login.success` |
| `2026-07-30 21:25:36` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f651936d3c5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-07-30 21:27 |
| **Last Seen** | 2026-07-30 21:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:27:01` | `cowrie.session.connect` |
| `2026-07-30 21:27:01` | `cowrie.client.version` |
| `2026-07-30 21:27:01` | `cowrie.client.kex` |
| `2026-07-30 21:27:02` | `cowrie.login.success` |
| `2026-07-30 21:27:03` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e529c6b09050

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-30 21:32 |
| **Last Seen** | 2026-07-30 21:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:32:14` | `cowrie.session.connect` |
| `2026-07-30 21:32:15` | `cowrie.client.version` |
| `2026-07-30 21:32:15` | `cowrie.client.kex` |
| `2026-07-30 21:32:17` | `cowrie.login.success` |
| `2026-07-30 21:32:18` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85bd916f41e

| Field | Detail |
|---|---|
| **Source IP** | `115.46.88[.]68` |
| **First Seen** | 2026-07-30 21:32 |
| **Last Seen** | 2026-07-30 21:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:32:28` | `cowrie.session.connect` |
| `2026-07-30 21:32:28` | `cowrie.client.version` |
| `2026-07-30 21:32:28` | `cowrie.client.kex` |
| `2026-07-30 21:32:31` | `cowrie.login.success` |
| `2026-07-30 21:32:31` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.46.88[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.46.88[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c9022c9d13

| Field | Detail |
|---|---|
| **Source IP** | `93.42.222[.]164` |
| **First Seen** | 2026-07-30 21:33 |
| **Last Seen** | 2026-07-30 21:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:33:16` | `cowrie.session.connect` |
| `2026-07-30 21:33:16` | `cowrie.client.version` |
| `2026-07-30 21:33:16` | `cowrie.client.kex` |
| `2026-07-30 21:33:17` | `cowrie.login.success` |
| `2026-07-30 21:33:17` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.42.222[.]164` to AbuseIPDB if not already reported
- [ ] Block `93.42.222[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0777e1315e1

| Field | Detail |
|---|---|
| **Source IP** | `222.75.225[.]206` |
| **First Seen** | 2026-07-30 21:41 |
| **Last Seen** | 2026-07-30 21:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:41:09` | `cowrie.session.connect` |
| `2026-07-30 21:41:09` | `cowrie.client.version` |
| `2026-07-30 21:41:09` | `cowrie.client.kex` |
| `2026-07-30 21:41:12` | `cowrie.login.success` |
| `2026-07-30 21:41:12` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.75.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `222.75.225[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09fda76c638

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-07-30 21:41 |
| **Last Seen** | 2026-07-30 21:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:41:18` | `cowrie.session.connect` |
| `2026-07-30 21:41:18` | `cowrie.client.version` |
| `2026-07-30 21:41:18` | `cowrie.client.kex` |
| `2026-07-30 21:41:21` | `cowrie.login.success` |
| `2026-07-30 21:41:21` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407b02d7a587

| Field | Detail |
|---|---|
| **Source IP** | `20.255.152[.]112` |
| **First Seen** | 2026-07-30 21:42 |
| **Last Seen** | 2026-07-30 21:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:42:09` | `cowrie.session.connect` |
| `2026-07-30 21:42:09` | `cowrie.client.version` |
| `2026-07-30 21:42:09` | `cowrie.client.kex` |
| `2026-07-30 21:42:10` | `cowrie.login.success` |
| `2026-07-30 21:42:11` | `cowrie.session.params` |
| `2026-07-30 21:42:11` | `cowrie.command.input` |
| `2026-07-30 21:42:11` | `cowrie.command.failed` |
| `2026-07-30 21:42:11` | `cowrie.log.closed` |
| `2026-07-30 21:42:12` | `cowrie.session.params` |
| `2026-07-30 21:42:12` | `cowrie.command.input` |
| `2026-07-30 21:42:12` | `cowrie.session.file_download` |
| `2026-07-30 21:42:12` | `cowrie.log.closed` |
| `2026-07-30 21:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.152[.]112` to AbuseIPDB if not already reported
- [ ] Block `20.255.152[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2b3b70982e

| Field | Detail |
|---|---|
| **Source IP** | `20.255.152[.]112` |
| **First Seen** | 2026-07-30 21:42 |
| **Last Seen** | 2026-07-30 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:42:12` | `cowrie.session.connect` |
| `2026-07-30 21:42:12` | `cowrie.client.version` |
| `2026-07-30 21:42:13` | `cowrie.client.kex` |
| `2026-07-30 21:42:13` | `cowrie.login.success` |
| `2026-07-30 21:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.152[.]112` to AbuseIPDB if not already reported
- [ ] Block `20.255.152[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b417edcb25e

| Field | Detail |
|---|---|
| **Source IP** | `20.255.152[.]112` |
| **First Seen** | 2026-07-30 21:42 |
| **Last Seen** | 2026-07-30 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:42:14` | `cowrie.session.connect` |
| `2026-07-30 21:42:14` | `cowrie.client.version` |
| `2026-07-30 21:42:14` | `cowrie.client.kex` |
| `2026-07-30 21:42:15` | `cowrie.login.success` |
| `2026-07-30 21:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.152[.]112` to AbuseIPDB if not already reported
- [ ] Block `20.255.152[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0248ffdcca5

| Field | Detail |
|---|---|
| **Source IP** | `2.26.50[.]151` |
| **First Seen** | 2026-07-30 21:45 |
| **Last Seen** | 2026-07-30 21:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:45:39` | `cowrie.session.connect` |
| `2026-07-30 21:45:39` | `cowrie.client.version` |
| `2026-07-30 21:45:39` | `cowrie.client.kex` |
| `2026-07-30 21:45:40` | `cowrie.login.success` |
| `2026-07-30 21:45:40` | `cowrie.session.params` |
| `2026-07-30 21:45:40` | `cowrie.command.input` |
| `2026-07-30 21:45:40` | `cowrie.command.failed` |
| `2026-07-30 21:45:41` | `cowrie.log.closed` |
| `2026-07-30 21:45:41` | `cowrie.session.params` |
| `2026-07-30 21:45:41` | `cowrie.command.input` |
| `2026-07-30 21:45:41` | `cowrie.session.file_download` |
| `2026-07-30 21:45:41` | `cowrie.log.closed` |
| `2026-07-30 21:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.50[.]151` to AbuseIPDB if not already reported
- [ ] Block `2.26.50[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9ff1235707

| Field | Detail |
|---|---|
| **Source IP** | `2.26.50[.]151` |
| **First Seen** | 2026-07-30 21:45 |
| **Last Seen** | 2026-07-30 21:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:45:42` | `cowrie.session.connect` |
| `2026-07-30 21:45:42` | `cowrie.client.version` |
| `2026-07-30 21:45:42` | `cowrie.client.kex` |
| `2026-07-30 21:45:42` | `cowrie.login.success` |
| `2026-07-30 21:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.50[.]151` to AbuseIPDB if not already reported
- [ ] Block `2.26.50[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccfe6d7d3b29

| Field | Detail |
|---|---|
| **Source IP** | `2.26.50[.]151` |
| **First Seen** | 2026-07-30 21:45 |
| **Last Seen** | 2026-07-30 21:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:45:42` | `cowrie.session.connect` |
| `2026-07-30 21:45:42` | `cowrie.client.version` |
| `2026-07-30 21:45:42` | `cowrie.client.kex` |
| `2026-07-30 21:45:43` | `cowrie.login.success` |
| `2026-07-30 21:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.50[.]151` to AbuseIPDB if not already reported
- [ ] Block `2.26.50[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552773edd750

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 21:57 |
| **Last Seen** | 2026-07-30 21:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:57:26` | `cowrie.session.connect` |
| `2026-07-30 21:57:26` | `cowrie.client.version` |
| `2026-07-30 21:57:26` | `cowrie.client.kex` |
| `2026-07-30 21:57:27` | `cowrie.login.success` |
| `2026-07-30 21:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406421701c55

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 21:57 |
| **Last Seen** | 2026-07-30 21:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:57:27` | `cowrie.session.connect` |
| `2026-07-30 21:57:27` | `cowrie.client.version` |
| `2026-07-30 21:57:27` | `cowrie.client.kex` |
| `2026-07-30 21:57:27` | `cowrie.login.success` |
| `2026-07-30 21:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bbfdf237353

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 21:57 |
| **Last Seen** | 2026-07-30 21:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:57:35` | `cowrie.session.connect` |
| `2026-07-30 21:57:35` | `cowrie.client.version` |
| `2026-07-30 21:57:35` | `cowrie.client.kex` |
| `2026-07-30 21:57:35` | `cowrie.login.success` |
| `2026-07-30 21:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf9ddc09715

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 21:57 |
| **Last Seen** | 2026-07-30 21:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:57:35` | `cowrie.session.connect` |
| `2026-07-30 21:57:35` | `cowrie.client.version` |
| `2026-07-30 21:57:35` | `cowrie.client.kex` |
| `2026-07-30 21:57:35` | `cowrie.login.success` |
| `2026-07-30 21:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ba452c97dd

| Field | Detail |
|---|---|
| **Source IP** | `27.128.162[.]146` |
| **First Seen** | 2026-07-30 21:59 |
| **Last Seen** | 2026-07-30 21:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:59:45` | `cowrie.session.connect` |
| `2026-07-30 21:59:45` | `cowrie.client.version` |
| `2026-07-30 21:59:45` | `cowrie.client.kex` |
| `2026-07-30 21:59:47` | `cowrie.login.success` |
| `2026-07-30 21:59:48` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `27.128.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f02d3398a60

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-07-30 21:59 |
| **Last Seen** | 2026-07-30 21:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 21:59:47` | `cowrie.session.connect` |
| `2026-07-30 21:59:48` | `cowrie.client.version` |
| `2026-07-30 21:59:48` | `cowrie.client.kex` |
| `2026-07-30 21:59:50` | `cowrie.login.success` |
| `2026-07-30 21:59:51` | `cowrie.direct-tcpip.request` |
| `2026-07-30 21:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82b68bcdc3b

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-30 22:07 |
| **Last Seen** | 2026-07-30 22:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:07:00` | `cowrie.session.connect` |
| `2026-07-30 22:07:00` | `cowrie.client.version` |
| `2026-07-30 22:07:00` | `cowrie.client.kex` |
| `2026-07-30 22:07:01` | `cowrie.login.success` |
| `2026-07-30 22:07:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7cdf2b34560

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-07-30 22:07 |
| **Last Seen** | 2026-07-30 22:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:07:07` | `cowrie.session.connect` |
| `2026-07-30 22:07:08` | `cowrie.client.version` |
| `2026-07-30 22:07:08` | `cowrie.client.kex` |
| `2026-07-30 22:07:10` | `cowrie.login.success` |
| `2026-07-30 22:07:10` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c3bf520d4d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 22:30 |
| **Last Seen** | 2026-07-30 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:30:13` | `cowrie.session.connect` |
| `2026-07-30 22:30:13` | `cowrie.client.version` |
| `2026-07-30 22:30:13` | `cowrie.client.kex` |
| `2026-07-30 22:30:14` | `cowrie.login.success` |
| `2026-07-30 22:30:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:30:14` | `cowrie.direct-tcpip.data` |
| `2026-07-30 22:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d134ba8ffe43

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-07-30 22:33 |
| **Last Seen** | 2026-07-30 22:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:33:05` | `cowrie.session.connect` |
| `2026-07-30 22:33:05` | `cowrie.client.version` |
| `2026-07-30 22:33:05` | `cowrie.client.kex` |
| `2026-07-30 22:33:06` | `cowrie.login.success` |
| `2026-07-30 22:33:07` | `cowrie.session.params` |
| `2026-07-30 22:33:07` | `cowrie.command.input` |
| `2026-07-30 22:33:07` | `cowrie.command.failed` |
| `2026-07-30 22:33:08` | `cowrie.log.closed` |
| `2026-07-30 22:33:08` | `cowrie.session.params` |
| `2026-07-30 22:33:08` | `cowrie.command.input` |
| `2026-07-30 22:33:09` | `cowrie.session.file_download` |
| `2026-07-30 22:33:09` | `cowrie.log.closed` |
| `2026-07-30 22:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2af7edfafe

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-07-30 22:33 |
| **Last Seen** | 2026-07-30 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:33:09` | `cowrie.session.connect` |
| `2026-07-30 22:33:09` | `cowrie.client.version` |
| `2026-07-30 22:33:09` | `cowrie.client.kex` |
| `2026-07-30 22:33:10` | `cowrie.login.success` |
| `2026-07-30 22:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0892607469

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-07-30 22:33 |
| **Last Seen** | 2026-07-30 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:33:11` | `cowrie.session.connect` |
| `2026-07-30 22:33:11` | `cowrie.client.version` |
| `2026-07-30 22:33:11` | `cowrie.client.kex` |
| `2026-07-30 22:33:12` | `cowrie.login.success` |
| `2026-07-30 22:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21699377608f

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-07-30 22:34 |
| **Last Seen** | 2026-07-30 22:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:34:29` | `cowrie.session.connect` |
| `2026-07-30 22:34:30` | `cowrie.client.version` |
| `2026-07-30 22:34:30` | `cowrie.client.kex` |
| `2026-07-30 22:34:32` | `cowrie.login.success` |
| `2026-07-30 22:34:32` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554e8b7b45c6

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-30 22:34 |
| **Last Seen** | 2026-07-30 22:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:34:39` | `cowrie.session.connect` |
| `2026-07-30 22:34:39` | `cowrie.client.version` |
| `2026-07-30 22:34:39` | `cowrie.client.kex` |
| `2026-07-30 22:34:41` | `cowrie.login.success` |
| `2026-07-30 22:34:41` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2140a926e1d

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-07-30 22:34 |
| **Last Seen** | 2026-07-30 22:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:34:42` | `cowrie.session.connect` |
| `2026-07-30 22:34:43` | `cowrie.client.version` |
| `2026-07-30 22:34:43` | `cowrie.client.kex` |
| `2026-07-30 22:34:44` | `cowrie.login.success` |
| `2026-07-30 22:34:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1960c48c1f36

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-07-30 22:40 |
| **Last Seen** | 2026-07-30 22:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:40:17` | `cowrie.session.connect` |
| `2026-07-30 22:40:17` | `cowrie.client.version` |
| `2026-07-30 22:40:17` | `cowrie.client.kex` |
| `2026-07-30 22:40:19` | `cowrie.login.success` |
| `2026-07-30 22:40:20` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aac93330d8f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]136` |
| **First Seen** | 2026-07-30 22:40 |
| **Last Seen** | 2026-07-30 22:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:40:25` | `cowrie.session.connect` |
| `2026-07-30 22:40:25` | `cowrie.client.version` |
| `2026-07-30 22:40:25` | `cowrie.client.kex` |
| `2026-07-30 22:40:27` | `cowrie.login.success` |
| `2026-07-30 22:40:27` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]136` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85b19f45247

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-30 22:42 |
| **Last Seen** | 2026-07-30 22:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:42:01` | `cowrie.session.connect` |
| `2026-07-30 22:42:02` | `cowrie.client.version` |
| `2026-07-30 22:42:02` | `cowrie.client.kex` |
| `2026-07-30 22:42:04` | `cowrie.login.success` |
| `2026-07-30 22:42:05` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8eb0ce84f0d

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-30 22:48 |
| **Last Seen** | 2026-07-30 22:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:48:19` | `cowrie.session.connect` |
| `2026-07-30 22:48:20` | `cowrie.client.version` |
| `2026-07-30 22:48:20` | `cowrie.client.kex` |
| `2026-07-30 22:48:22` | `cowrie.login.success` |
| `2026-07-30 22:48:23` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4170da8d154c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-07-30 22:48 |
| **Last Seen** | 2026-07-30 22:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 22:48:29` | `cowrie.session.connect` |
| `2026-07-30 22:48:30` | `cowrie.client.version` |
| `2026-07-30 22:48:30` | `cowrie.client.kex` |
| `2026-07-30 22:48:32` | `cowrie.login.success` |
| `2026-07-30 22:48:33` | `cowrie.direct-tcpip.request` |
| `2026-07-30 22:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **50** | 2026-07-30 20:56 | 2026-07-30 22:53 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `194.165.16[.]165` | **6** | 2026-07-30 21:07 | 2026-07-30 21:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **6** | 2026-07-30 22:23 | 2026-07-30 22:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-30 20:57 | 2026-07-30 22:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]168` | **3** | 2026-07-30 21:11 | 2026-07-30 21:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-07-30 20:56 | 2026-07-30 21:18 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]100` | **2** | 2026-07-30 20:55 | 2026-07-30 20:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-07-30 21:14 | 2026-07-30 21:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.214[.]209` | 1 | 2026-07-30 21:47 | 2026-07-30 21:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-07-30 21:59 | 2026-07-30 22:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-07-30 21:33 | 2026-07-30 21:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-07-30 22:34 | 2026-07-30 22:36 | 105s | 0 | `T1592` | 🟢 LOW |
| `193.24.126[.]135` | 1 | 2026-07-30 21:25 | 2026-07-30 21:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.46.255[.]142` | 1 | 2026-07-30 22:22 | 2026-07-30 22:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.59.235[.]170` | 1 | 2026-07-30 22:34 | 2026-07-30 22:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.178.246[.]43` | 1 | 2026-07-30 22:03 | 2026-07-30 22:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.105.212[.]205` | 1 | 2026-07-30 21:19 | 2026-07-30 21:19 | 23s | 0 | `T1592` | 🟢 LOW |
| `39.106.21[.]251` | 1 | 2026-07-30 22:17 | 2026-07-30 22:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-30 22:11 | 2026-07-30 22:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]26` | 1 | 2026-07-30 22:18 | 2026-07-30 22:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-30 21:12 | 2026-07-30 21:13 | 54s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-07-30 21:48 | 2026-07-30 21:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-30 21:38 | 2026-07-30 21:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-07-30 21:08 | 2026-07-30 21:10 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | **1/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `193.46.255[.]142` | RO | UNMANAGED LTD | **100** ⚠️ | 8 |
| `111.70.32[.]51` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `220.178.246[.]43` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `1.212.225[.]99` | KR | LG Uplus | **100** ⚠️ | 50 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `182.156.35[.]238` | IN | D 26/2 TTC INDUSTRIAL AREA MIDC SANPADA | **100** ⚠️ | 5 |
| `218.59.235[.]170` | CN | Zaozhuang-Tengzhou Dawushishang Internet Bar | **100** ⚠️ | 50 |
| `27.128.162[.]146` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `117.250.250[.]2` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 35 |
| `61.184.128[.]210` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 56 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 10 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 165 cases |
| Tool 34  | Credential Extractor        | ✅ 77 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 55 priority case(s) shown individually · 24 recon entry/entries in table (8 group(s) consolidating 76 session(s)).

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
_Report time: 2026-07-30T23:12:18Z_

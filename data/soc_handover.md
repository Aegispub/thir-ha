# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T08:34:59Z |
| **Shift Time** | 08:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4964** |
| Confirmed Threats | **4941** |
| False Positives Filtered | **23** (0.5%) |
| Unique Attacker IPs | **91** |
| Countries of Origin | **30** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4877** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **106** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **24** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **96** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `dspace` | 9 |
| `root` | 9 |
| `support` | 9 |
| `www` | 9 |
| `default` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 10 |
| `user11` | 6 |
| `nobody12345` | 6 |
| `passwd` | 6 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `user11` | 6 |
| `nobody` | `nobody12345` | 6 |
| `config` | `passwd` | 6 |
| `default` | `123` | 5 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin1` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T04:55:50 |
| `admin1` | `pass123` | `193.32.162.15` | 2026-08-16T04:57:01 |
| `admin1` | `123abc` | `193.32.162.15` | 2026-08-16T04:58:08 |
| `dspace` | `1234567890` | `193.32.162.15` | 2026-08-16T04:59:15 |
| `dspace` | `password1` | `193.32.162.15` | 2026-08-16T05:00:26 |
| `user` | `user11` | `10.0.0.73` | 2026-08-16T05:01:06 |
| `dspace` | `admin123` | `193.32.162.15` | 2026-08-16T05:01:36 |
| `dspace` | `1234` | `193.32.162.15` | 2026-08-16T05:02:45 |
| `user` | `user11` | `42.248.129.234` | 2026-08-16T05:02:47 |
| `user` | `user11` | `23.30.11.253` | 2026-08-16T05:02:54 |
| `dspace` | `123` | `193.32.162.15` | 2026-08-16T05:03:50 |
| `dspace` | `qwerty123` | `193.32.162.15` | 2026-08-16T05:04:54 |
| `admin` | `insecure` | `211.22.222.251` | 2026-08-16T05:05:24 |
| `admin` | `insecure` | `92.255.196.185` | 2026-08-16T05:05:32 |
| `dspace` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T05:05:58 |
| `root` | `Password@123` | `45.142.193.164` | 2026-08-16T05:06:40 |
| `minecraft` | `password` | `217.165.22.192` | 2026-08-16T05:06:54 |
| `dspace` | `pass123` | `193.32.162.15` | 2026-08-16T05:07:01 |
| `dspace` | `123abc` | `193.32.162.15` | 2026-08-16T05:08:05 |
| `support` | `123` | `111.70.42.37` | 2026-08-16T05:08:05 |
| `support` | `123` | `122.160.142.194` | 2026-08-16T05:08:15 |
| `support` | `123` | `112.30.127.9` | 2026-08-16T05:08:28 |
| `root` | `` | `94.154.43.210` | 2026-08-16T05:08:41 |
| `www` | `1234567890` | `193.32.162.15` | 2026-08-16T05:09:09 |
| `www` | `password1` | `193.32.162.15` | 2026-08-16T05:10:13 |
| `www` | `admin123` | `193.32.162.15` | 2026-08-16T05:11:19 |
| `www` | `1234` | `193.32.162.15` | 2026-08-16T05:12:26 |
| `www` | `123` | `193.32.162.15` | 2026-08-16T05:13:36 |
| `user` | `123!@#qweQWE` | `103.114.147.217` | 2026-08-16T05:14:14 |
| `345gs5662d34` | `345gs5662d34` | `103.114.147.217` | 2026-08-16T05:14:19 |
| `user` | `3245gs5662d34` | `103.114.147.217` | 2026-08-16T05:14:21 |
| `www` | `qwerty123` | `193.32.162.15` | 2026-08-16T05:14:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.198.2` | 2026-08-16T05:15:07 |
| `*1` | `$4` | `34.38.198.2` | 2026-08-16T05:15:15 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2808` | `34.38.198.2` | 2026-08-16T05:15:17 |
| `www` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T05:15:56 |
| `www` | `pass123` | `193.32.162.15` | 2026-08-16T05:17:08 |
| `www` | `123abc` | `193.32.162.15` | 2026-08-16T05:18:17 |
| `user` | `user11` | `196.190.180.18` | 2026-08-16T05:18:39 |
| `user` | `user11` | `5.11.162.163` | 2026-08-16T05:18:50 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T05:21:55 |
| `default` | `123` | `10.0.0.73` | 2026-08-16T05:23:38 |
| `radio` | `radio` | `217.165.22.192` | 2026-08-16T05:26:01 |
| `root` | `Aa112211@` | `45.142.193.164` | 2026-08-16T05:28:23 |
| `admin` | `insecure` | `207.254.22.207` | 2026-08-16T05:33:53 |
| `debian` | `ubuntu` | `65.20.138.46` | 2026-08-16T05:36:34 |
| `debian` | `ubuntu` | `218.95.73.31` | 2026-08-16T05:36:43 |
| `hunter` | `hunter` | `14.33.96.3` | 2026-08-16T05:39:32 |
| `default` | `123` | `117.191.83.250` | 2026-08-16T05:41:54 |
| `default` | `123` | `103.29.185.162` | 2026-08-16T05:42:03 |
| `default` | `123` | `120.234.232.184` | 2026-08-16T05:42:06 |
| `root` | `public` | `10.0.0.73` | 2026-08-16T05:44:57 |
| `minecraft` | `123456` | `217.165.22.192` | 2026-08-16T05:45:08 |
| `root` | `1qaz2wsx` | `45.142.193.164` | 2026-08-16T05:46:45 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T05:46:55 |
| `hunter` | `hunter` | `10.0.0.73` | 2026-08-16T05:50:46 |
| `debian` | `ubuntu` | `62.182.132.94` | 2026-08-16T05:52:40 |
| `debian` | `ubuntu` | `85.152.57.60` | 2026-08-16T05:52:46 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.97.37` | 2026-08-16T05:53:17 |
| `*1` | `$4` | `34.156.97.37` | 2026-08-16T05:53:30 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5805` | `34.156.97.37` | 2026-08-16T05:53:32 |
| `unknown` | `unknown6` | `118.123.116.93` | 2026-08-16T05:55:27 |
| `unknown` | `unknown6` | `179.184.85.167` | 2026-08-16T05:55:37 |
| `nobody` | `nobody12345` | `10.0.0.73` | 2026-08-16T05:57:14 |
| `test` | `1` | `217.165.22.192` | 2026-08-16T06:04:16 |
| `root` | `Abc123456` | `45.142.193.164` | 2026-08-16T06:05:04 |
| `hunter` | `hunter` | `111.46.77.2` | 2026-08-16T06:07:55 |
| `config` | `passwd` | `10.0.0.73` | 2026-08-16T06:08:41 |
| `config` | `passwd` | `187.8.120.90` | 2026-08-16T06:10:20 |
| `config` | `passwd` | `182.73.164.228` | 2026-08-16T06:10:30 |
| `blank` | `p@ssword` | `175.206.113.91` | 2026-08-16T06:13:09 |
| `blank` | `p@ssword` | `220.180.166.214` | 2026-08-16T06:13:21 |
| `nobody` | `nobody12345` | `183.63.220.210` | 2026-08-16T06:15:45 |
| `nobody` | `nobody12345` | `182.75.227.178` | 2026-08-16T06:15:55 |
| `nobody` | `nobody12345` | `103.147.248.23` | 2026-08-16T06:15:59 |
| `nobody` | `nobody12345` | `31.41.84.98` | 2026-08-16T06:16:08 |
| `support` | `0` | `10.0.0.73` | 2026-08-16T06:20:56 |
| `minecraft` | `minecraft` | `217.165.22.192` | 2026-08-16T06:23:23 |
| `config` | `passwd` | `178.178.194.137` | 2026-08-16T06:26:40 |
| `config` | `passwd` | `14.153.230.167` | 2026-08-16T06:26:50 |
| `b'Tw\x0c,=\xc8\x01\x04tU\x1aj\xbe\xc7\x0b\xa1\xc1\xfe\xb9\t,\xc56\xacA\x02x~\x0e\x9f\x00\x86\xbb\xc9fkl.2\x10\x92\x9cj\xe6'` | `b'\xd2;O\x9c$\xd7\xb6\xdc\xeb\xd6\x14,\x12\xa6\xd59\xe6\x15c\x06\x9dS\xeb|\x1c\xf4=\xd5\x8d\x8f5\x9bdh\xdc\x84\xe5\xfb3\xc5\xf3\xb7JF\xf0\xccc\x1c7p\xbd\xce53\x80\xa4\x06y^z\x84\xb2\xbb\x9e'` | `181.191.148.177` | 2026-08-16T06:29:53 |
| `default` | `12345` | `10.0.0.73` | 2026-08-16T06:31:06 |
| `ubuntu` | `admin1234` | `185.74.59.14` | 2026-08-16T06:38:52 |
| `blank` | `p@ssword` | `59.46.182.10` | 2026-08-16T06:41:53 |
| `ubuntu` | `1` | `217.165.22.192` | 2026-08-16T06:42:31 |
| `config` | `123123` | `10.0.0.73` | 2026-08-16T06:42:42 |
| `config` | `123123` | `197.155.225.93` | 2026-08-16T06:44:21 |
| `config` | `123123` | `90.228.229.182` | 2026-08-16T06:44:30 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.85.137` | 2026-08-16T06:45:05 |
| `*1` | `$4` | `34.62.85.137` | 2026-08-16T06:45:18 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2536` | `34.62.85.137` | 2026-08-16T06:45:20 |
| `centos` | `qwerty12345` | `171.217.70.151` | 2026-08-16T06:46:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-16T06:46:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-16T06:46:59 |
| `default` | `12345` | `178.178.222.61` | 2026-08-16T06:49:31 |
| `default` | `12345` | `27.71.60.22` | 2026-08-16T06:49:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4964** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 38 |
| Go SSH scanner | 37 |
| libssh | 8 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 38 | 38 |
| `2ec37a7cc8da...` | Mirai/variant | 21 | 1 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 5 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 38 | 38 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 21 | 1 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 5 | 2 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 21 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `193.32.162.15`

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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.114.147.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **91** |
| Unique ASNs | **68** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 9 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS1257` | Tele2 Sverige AB | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (87)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cf6ae533aa0f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:55 |
| **Last Seen** | 2026-08-16 04:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:55:49` | `cowrie.session.connect` |
| `2026-08-16 04:55:49` | `cowrie.client.version` |
| `2026-08-16 04:55:49` | `cowrie.client.kex` |
| `2026-08-16 04:55:50` | `cowrie.login.success` |
| `2026-08-16 04:55:51` | `cowrie.session.params` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.success` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.command.input` |
| `2026-08-16 04:55:51` | `cowrie.log.closed` |
| `2026-08-16 04:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af555335258

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:57 |
| **Last Seen** | 2026-08-16 04:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:57:00` | `cowrie.session.connect` |
| `2026-08-16 04:57:00` | `cowrie.client.version` |
| `2026-08-16 04:57:00` | `cowrie.client.kex` |
| `2026-08-16 04:57:01` | `cowrie.login.success` |
| `2026-08-16 04:57:02` | `cowrie.session.params` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.success` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:02` | `cowrie.command.input` |
| `2026-08-16 04:57:03` | `cowrie.log.closed` |
| `2026-08-16 04:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4107187ec73

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:58 |
| **Last Seen** | 2026-08-16 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:58:07` | `cowrie.session.connect` |
| `2026-08-16 04:58:07` | `cowrie.client.version` |
| `2026-08-16 04:58:08` | `cowrie.client.kex` |
| `2026-08-16 04:58:08` | `cowrie.login.success` |
| `2026-08-16 04:58:10` | `cowrie.session.params` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.success` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.command.input` |
| `2026-08-16 04:58:10` | `cowrie.log.closed` |
| `2026-08-16 04:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c436e280a03c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:59 |
| **Last Seen** | 2026-08-16 04:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:59:14` | `cowrie.session.connect` |
| `2026-08-16 04:59:14` | `cowrie.client.version` |
| `2026-08-16 04:59:15` | `cowrie.client.kex` |
| `2026-08-16 04:59:15` | `cowrie.login.success` |
| `2026-08-16 04:59:16` | `cowrie.session.params` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.success` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:16` | `cowrie.command.input` |
| `2026-08-16 04:59:17` | `cowrie.log.closed` |
| `2026-08-16 04:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9e66585f62

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:00 |
| **Last Seen** | 2026-08-16 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:00:25` | `cowrie.session.connect` |
| `2026-08-16 05:00:25` | `cowrie.client.version` |
| `2026-08-16 05:00:25` | `cowrie.client.kex` |
| `2026-08-16 05:00:26` | `cowrie.login.success` |
| `2026-08-16 05:00:27` | `cowrie.session.params` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.success` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.command.input` |
| `2026-08-16 05:00:27` | `cowrie.log.closed` |
| `2026-08-16 05:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba18732f94ca

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:01 |
| **Last Seen** | 2026-08-16 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:01:35` | `cowrie.session.connect` |
| `2026-08-16 05:01:35` | `cowrie.client.version` |
| `2026-08-16 05:01:35` | `cowrie.client.kex` |
| `2026-08-16 05:01:36` | `cowrie.login.success` |
| `2026-08-16 05:01:37` | `cowrie.session.params` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:37` | `cowrie.command.success` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:37` | `cowrie.command.input` |
| `2026-08-16 05:01:38` | `cowrie.command.input` |
| `2026-08-16 05:01:38` | `cowrie.command.input` |
| `2026-08-16 05:01:38` | `cowrie.log.closed` |
| `2026-08-16 05:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d75335d6d41c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:02 |
| **Last Seen** | 2026-08-16 05:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:02:43` | `cowrie.session.connect` |
| `2026-08-16 05:02:43` | `cowrie.client.version` |
| `2026-08-16 05:02:43` | `cowrie.client.kex` |
| `2026-08-16 05:02:45` | `cowrie.login.success` |
| `2026-08-16 05:02:46` | `cowrie.session.params` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.success` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.command.input` |
| `2026-08-16 05:02:46` | `cowrie.log.closed` |
| `2026-08-16 05:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87aa79edfb30

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-08-16 05:02 |
| **Last Seen** | 2026-08-16 05:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:02:44` | `cowrie.session.connect` |
| `2026-08-16 05:02:44` | `cowrie.client.version` |
| `2026-08-16 05:02:44` | `cowrie.client.kex` |
| `2026-08-16 05:02:47` | `cowrie.login.success` |
| `2026-08-16 05:02:47` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4815576de114

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-08-16 05:02 |
| **Last Seen** | 2026-08-16 05:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:02:52` | `cowrie.session.connect` |
| `2026-08-16 05:02:53` | `cowrie.client.version` |
| `2026-08-16 05:02:53` | `cowrie.client.kex` |
| `2026-08-16 05:02:54` | `cowrie.login.success` |
| `2026-08-16 05:02:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe94161c8e2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:03 |
| **Last Seen** | 2026-08-16 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:03:49` | `cowrie.session.connect` |
| `2026-08-16 05:03:49` | `cowrie.client.version` |
| `2026-08-16 05:03:49` | `cowrie.client.kex` |
| `2026-08-16 05:03:50` | `cowrie.login.success` |
| `2026-08-16 05:03:51` | `cowrie.session.params` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.success` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.command.input` |
| `2026-08-16 05:03:51` | `cowrie.log.closed` |
| `2026-08-16 05:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e21f1935da9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:04 |
| **Last Seen** | 2026-08-16 05:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:04:53` | `cowrie.session.connect` |
| `2026-08-16 05:04:53` | `cowrie.client.version` |
| `2026-08-16 05:04:53` | `cowrie.client.kex` |
| `2026-08-16 05:04:54` | `cowrie.login.success` |
| `2026-08-16 05:04:56` | `cowrie.session.params` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.success` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.command.input` |
| `2026-08-16 05:04:56` | `cowrie.log.closed` |
| `2026-08-16 05:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94b7ed3c664

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-08-16 05:05 |
| **Last Seen** | 2026-08-16 05:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:05:20` | `cowrie.session.connect` |
| `2026-08-16 05:05:21` | `cowrie.client.version` |
| `2026-08-16 05:05:21` | `cowrie.client.kex` |
| `2026-08-16 05:05:24` | `cowrie.login.success` |
| `2026-08-16 05:05:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab04260c2f6

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-16 05:05 |
| **Last Seen** | 2026-08-16 05:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:05:30` | `cowrie.session.connect` |
| `2026-08-16 05:05:30` | `cowrie.client.version` |
| `2026-08-16 05:05:30` | `cowrie.client.kex` |
| `2026-08-16 05:05:32` | `cowrie.login.success` |
| `2026-08-16 05:05:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe0dc024430

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:05 |
| **Last Seen** | 2026-08-16 05:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:05:57` | `cowrie.session.connect` |
| `2026-08-16 05:05:57` | `cowrie.client.version` |
| `2026-08-16 05:05:57` | `cowrie.client.kex` |
| `2026-08-16 05:05:58` | `cowrie.login.success` |
| `2026-08-16 05:05:59` | `cowrie.session.params` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.success` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.command.input` |
| `2026-08-16 05:05:59` | `cowrie.log.closed` |
| `2026-08-16 05:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd391254031

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 05:06 |
| **Last Seen** | 2026-08-16 05:06 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:06:11` | `cowrie.session.connect` |
| `2026-08-16 05:06:18` | `cowrie.client.version` |
| `2026-08-16 05:06:18` | `cowrie.client.kex` |
| `2026-08-16 05:06:40` | `cowrie.login.success` |
| `2026-08-16 05:06:53` | `cowrie.session.params` |
| `2026-08-16 05:06:53` | `cowrie.command.input` |
| `2026-08-16 05:06:58` | `cowrie.log.closed` |
| `2026-08-16 05:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce3a4466f16

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 05:06 |
| **Last Seen** | 2026-08-16 05:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:06:53` | `cowrie.session.connect` |
| `2026-08-16 05:06:53` | `cowrie.client.version` |
| `2026-08-16 05:06:53` | `cowrie.client.kex` |
| `2026-08-16 05:06:54` | `cowrie.login.success` |
| `2026-08-16 05:06:55` | `cowrie.session.params` |
| `2026-08-16 05:06:55` | `cowrie.command.input` |
| `2026-08-16 05:06:55` | `cowrie.log.closed` |
| `2026-08-16 05:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df2ca7f712d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:07 |
| **Last Seen** | 2026-08-16 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:07:00` | `cowrie.session.connect` |
| `2026-08-16 05:07:00` | `cowrie.client.version` |
| `2026-08-16 05:07:00` | `cowrie.client.kex` |
| `2026-08-16 05:07:01` | `cowrie.login.success` |
| `2026-08-16 05:07:02` | `cowrie.session.params` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.success` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.command.input` |
| `2026-08-16 05:07:02` | `cowrie.log.closed` |
| `2026-08-16 05:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5643c4a458c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.42[.]37` |
| **First Seen** | 2026-08-16 05:08 |
| **Last Seen** | 2026-08-16 05:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:08:02` | `cowrie.session.connect` |
| `2026-08-16 05:08:02` | `cowrie.client.version` |
| `2026-08-16 05:08:02` | `cowrie.client.kex` |
| `2026-08-16 05:08:05` | `cowrie.login.success` |
| `2026-08-16 05:08:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.42[.]37` to AbuseIPDB if not already reported
- [ ] Block `111.70.42[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b9e576936d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:08 |
| **Last Seen** | 2026-08-16 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:08:04` | `cowrie.session.connect` |
| `2026-08-16 05:08:04` | `cowrie.client.version` |
| `2026-08-16 05:08:04` | `cowrie.client.kex` |
| `2026-08-16 05:08:05` | `cowrie.login.success` |
| `2026-08-16 05:08:06` | `cowrie.session.params` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.success` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.command.input` |
| `2026-08-16 05:08:06` | `cowrie.log.closed` |
| `2026-08-16 05:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb30fb0c0c8

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-08-16 05:08 |
| **Last Seen** | 2026-08-16 05:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:08:12` | `cowrie.session.connect` |
| `2026-08-16 05:08:13` | `cowrie.client.version` |
| `2026-08-16 05:08:13` | `cowrie.client.kex` |
| `2026-08-16 05:08:15` | `cowrie.login.success` |
| `2026-08-16 05:08:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817d589d4954

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-08-16 05:08 |
| **Last Seen** | 2026-08-16 05:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:08:25` | `cowrie.session.connect` |
| `2026-08-16 05:08:26` | `cowrie.client.version` |
| `2026-08-16 05:08:26` | `cowrie.client.kex` |
| `2026-08-16 05:08:28` | `cowrie.login.success` |
| `2026-08-16 05:08:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2357ea1332f7

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-16 05:08 |
| **Last Seen** | 2026-08-16 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:08:40` | `cowrie.session.connect` |
| `2026-08-16 05:08:41` | `cowrie.login.success` |
| `2026-08-16 05:08:41` | `cowrie.session.params` |
| `2026-08-16 05:08:42` | `cowrie.command.input` |
| `2026-08-16 05:08:42` | `cowrie.command.input` |
| `2026-08-16 05:08:43` | `cowrie.command.input` |
| `2026-08-16 05:08:43` | `cowrie.command.input` |
| `2026-08-16 05:08:43` | `cowrie.command.failed` |
| `2026-08-16 05:08:44` | `cowrie.log.closed` |
| `2026-08-16 05:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9ce9e8cc0b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:09 |
| **Last Seen** | 2026-08-16 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:09:08` | `cowrie.session.connect` |
| `2026-08-16 05:09:08` | `cowrie.client.version` |
| `2026-08-16 05:09:08` | `cowrie.client.kex` |
| `2026-08-16 05:09:09` | `cowrie.login.success` |
| `2026-08-16 05:09:10` | `cowrie.session.params` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.success` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.command.input` |
| `2026-08-16 05:09:10` | `cowrie.log.closed` |
| `2026-08-16 05:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c01bcc6c8e7e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:10 |
| **Last Seen** | 2026-08-16 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:10:12` | `cowrie.session.connect` |
| `2026-08-16 05:10:12` | `cowrie.client.version` |
| `2026-08-16 05:10:12` | `cowrie.client.kex` |
| `2026-08-16 05:10:13` | `cowrie.login.success` |
| `2026-08-16 05:10:14` | `cowrie.session.params` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.success` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.command.input` |
| `2026-08-16 05:10:14` | `cowrie.log.closed` |
| `2026-08-16 05:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b55e1e878f7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:11 |
| **Last Seen** | 2026-08-16 05:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:11:18` | `cowrie.session.connect` |
| `2026-08-16 05:11:18` | `cowrie.client.version` |
| `2026-08-16 05:11:18` | `cowrie.client.kex` |
| `2026-08-16 05:11:19` | `cowrie.login.success` |
| `2026-08-16 05:11:20` | `cowrie.session.params` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.success` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.command.input` |
| `2026-08-16 05:11:20` | `cowrie.log.closed` |
| `2026-08-16 05:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b25bc9fc84

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:12 |
| **Last Seen** | 2026-08-16 05:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:12:24` | `cowrie.session.connect` |
| `2026-08-16 05:12:24` | `cowrie.client.version` |
| `2026-08-16 05:12:25` | `cowrie.client.kex` |
| `2026-08-16 05:12:26` | `cowrie.login.success` |
| `2026-08-16 05:12:27` | `cowrie.session.params` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.success` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.command.input` |
| `2026-08-16 05:12:27` | `cowrie.log.closed` |
| `2026-08-16 05:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6993b9e15683

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:13 |
| **Last Seen** | 2026-08-16 05:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:13:36` | `cowrie.session.connect` |
| `2026-08-16 05:13:36` | `cowrie.client.version` |
| `2026-08-16 05:13:36` | `cowrie.client.kex` |
| `2026-08-16 05:13:36` | `cowrie.login.success` |
| `2026-08-16 05:13:37` | `cowrie.session.params` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.success` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:37` | `cowrie.command.input` |
| `2026-08-16 05:13:38` | `cowrie.log.closed` |
| `2026-08-16 05:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0217b56299ef

| Field | Detail |
|---|---|
| **Source IP** | `103.114.147[.]217` |
| **First Seen** | 2026-08-16 05:14 |
| **Last Seen** | 2026-08-16 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:14:13` | `cowrie.session.connect` |
| `2026-08-16 05:14:13` | `cowrie.client.version` |
| `2026-08-16 05:14:13` | `cowrie.client.kex` |
| `2026-08-16 05:14:14` | `cowrie.login.success` |
| `2026-08-16 05:14:16` | `cowrie.session.params` |
| `2026-08-16 05:14:16` | `cowrie.command.input` |
| `2026-08-16 05:14:16` | `cowrie.command.failed` |
| `2026-08-16 05:14:16` | `cowrie.log.closed` |
| `2026-08-16 05:14:17` | `cowrie.session.params` |
| `2026-08-16 05:14:17` | `cowrie.command.input` |
| `2026-08-16 05:14:17` | `cowrie.session.file_download` |
| `2026-08-16 05:14:17` | `cowrie.log.closed` |
| `2026-08-16 05:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.114.147[.]217` to AbuseIPDB if not already reported
- [ ] Block `103.114.147[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc49e922eabb

| Field | Detail |
|---|---|
| **Source IP** | `103.114.147[.]217` |
| **First Seen** | 2026-08-16 05:14 |
| **Last Seen** | 2026-08-16 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:14:18` | `cowrie.session.connect` |
| `2026-08-16 05:14:18` | `cowrie.client.version` |
| `2026-08-16 05:14:18` | `cowrie.client.kex` |
| `2026-08-16 05:14:19` | `cowrie.login.success` |
| `2026-08-16 05:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.114.147[.]217` to AbuseIPDB if not already reported
- [ ] Block `103.114.147[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee9efc3e718

| Field | Detail |
|---|---|
| **Source IP** | `103.114.147[.]217` |
| **First Seen** | 2026-08-16 05:14 |
| **Last Seen** | 2026-08-16 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:14:19` | `cowrie.session.connect` |
| `2026-08-16 05:14:19` | `cowrie.client.version` |
| `2026-08-16 05:14:20` | `cowrie.client.kex` |
| `2026-08-16 05:14:21` | `cowrie.login.success` |
| `2026-08-16 05:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.114.147[.]217` to AbuseIPDB if not already reported
- [ ] Block `103.114.147[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827f697b045b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:14 |
| **Last Seen** | 2026-08-16 05:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:14:46` | `cowrie.session.connect` |
| `2026-08-16 05:14:46` | `cowrie.client.version` |
| `2026-08-16 05:14:46` | `cowrie.client.kex` |
| `2026-08-16 05:14:47` | `cowrie.login.success` |
| `2026-08-16 05:14:47` | `cowrie.session.params` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.success` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:47` | `cowrie.command.input` |
| `2026-08-16 05:14:48` | `cowrie.log.closed` |
| `2026-08-16 05:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4fabd250daa

| Field | Detail |
|---|---|
| **Source IP** | `34.38.198[.]2` |
| **First Seen** | 2026-08-16 05:15 |
| **Last Seen** | 2026-08-16 05:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:15:07` | `cowrie.session.connect` |
| `2026-08-16 05:15:07` | `cowrie.login.success` |
| `2026-08-16 05:15:08` | `cowrie.session.params` |
| `2026-08-16 05:15:08` | `cowrie.command.input` |
| `2026-08-16 05:15:08` | `cowrie.command.input` |
| `2026-08-16 05:15:08` | `cowrie.command.failed` |
| `2026-08-16 05:15:08` | `cowrie.command.input` |
| `2026-08-16 05:15:08` | `cowrie.log.closed` |
| `2026-08-16 05:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.198[.]2` to AbuseIPDB if not already reported
- [ ] Block `34.38.198[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dedfc392c02

| Field | Detail |
|---|---|
| **Source IP** | `34.38.198[.]2` |
| **First Seen** | 2026-08-16 05:15 |
| **Last Seen** | 2026-08-16 05:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:15:15` | `cowrie.session.connect` |
| `2026-08-16 05:15:15` | `cowrie.login.success` |
| `2026-08-16 05:15:16` | `cowrie.session.params` |
| `2026-08-16 05:15:16` | `cowrie.command.input` |
| `2026-08-16 05:15:16` | `cowrie.command.failed` |
| `2026-08-16 05:15:28` | `cowrie.log.closed` |
| `2026-08-16 05:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.198[.]2` to AbuseIPDB if not already reported
- [ ] Block `34.38.198[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51288807539e

| Field | Detail |
|---|---|
| **Source IP** | `34.38.198[.]2` |
| **First Seen** | 2026-08-16 05:15 |
| **Last Seen** | 2026-08-16 05:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:15:17` | `cowrie.session.connect` |
| `2026-08-16 05:15:17` | `cowrie.login.success` |
| `2026-08-16 05:15:18` | `cowrie.session.params` |
| `2026-08-16 05:15:18` | `cowrie.command.input` |
| `2026-08-16 05:15:28` | `cowrie.log.closed` |
| `2026-08-16 05:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.198[.]2` to AbuseIPDB if not already reported
- [ ] Block `34.38.198[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2060bad736

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:15 |
| **Last Seen** | 2026-08-16 05:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:15:55` | `cowrie.session.connect` |
| `2026-08-16 05:15:55` | `cowrie.client.version` |
| `2026-08-16 05:15:55` | `cowrie.client.kex` |
| `2026-08-16 05:15:56` | `cowrie.login.success` |
| `2026-08-16 05:15:57` | `cowrie.session.params` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.success` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:57` | `cowrie.command.input` |
| `2026-08-16 05:15:58` | `cowrie.log.closed` |
| `2026-08-16 05:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c28f10641b0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:17 |
| **Last Seen** | 2026-08-16 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:17:06` | `cowrie.session.connect` |
| `2026-08-16 05:17:07` | `cowrie.client.version` |
| `2026-08-16 05:17:07` | `cowrie.client.kex` |
| `2026-08-16 05:17:08` | `cowrie.login.success` |
| `2026-08-16 05:17:08` | `cowrie.session.params` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.success` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:08` | `cowrie.command.input` |
| `2026-08-16 05:17:09` | `cowrie.log.closed` |
| `2026-08-16 05:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006242319dd0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 05:18 |
| **Last Seen** | 2026-08-16 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:18:16` | `cowrie.session.connect` |
| `2026-08-16 05:18:16` | `cowrie.client.version` |
| `2026-08-16 05:18:16` | `cowrie.client.kex` |
| `2026-08-16 05:18:17` | `cowrie.login.success` |
| `2026-08-16 05:18:18` | `cowrie.session.params` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.success` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.command.input` |
| `2026-08-16 05:18:18` | `cowrie.log.closed` |
| `2026-08-16 05:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c561e6ac4db9

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-16 05:18 |
| **Last Seen** | 2026-08-16 05:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:18:37` | `cowrie.session.connect` |
| `2026-08-16 05:18:38` | `cowrie.client.version` |
| `2026-08-16 05:18:38` | `cowrie.client.kex` |
| `2026-08-16 05:18:39` | `cowrie.login.success` |
| `2026-08-16 05:18:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c3f9efd48f

| Field | Detail |
|---|---|
| **Source IP** | `5.11.162[.]163` |
| **First Seen** | 2026-08-16 05:18 |
| **Last Seen** | 2026-08-16 05:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:18:45` | `cowrie.session.connect` |
| `2026-08-16 05:18:46` | `cowrie.client.version` |
| `2026-08-16 05:18:46` | `cowrie.client.kex` |
| `2026-08-16 05:18:50` | `cowrie.login.success` |
| `2026-08-16 05:18:52` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.11.162[.]163` to AbuseIPDB if not already reported
- [ ] Block `5.11.162[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8957b48e5058

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 05:21 |
| **Last Seen** | 2026-08-16 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:21:55` | `cowrie.session.connect` |
| `2026-08-16 05:21:55` | `cowrie.client.version` |
| `2026-08-16 05:21:55` | `cowrie.client.kex` |
| `2026-08-16 05:21:55` | `cowrie.login.success` |
| `2026-08-16 05:21:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:21:56` | `cowrie.direct-tcpip.data` |
| `2026-08-16 05:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a65e36b61a0

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 05:26 |
| **Last Seen** | 2026-08-16 05:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:26:00` | `cowrie.session.connect` |
| `2026-08-16 05:26:00` | `cowrie.client.version` |
| `2026-08-16 05:26:00` | `cowrie.client.kex` |
| `2026-08-16 05:26:01` | `cowrie.login.success` |
| `2026-08-16 05:26:02` | `cowrie.session.params` |
| `2026-08-16 05:26:02` | `cowrie.command.input` |
| `2026-08-16 05:26:02` | `cowrie.log.closed` |
| `2026-08-16 05:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e98022b74c5e

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 05:27 |
| **Last Seen** | 2026-08-16 05:28 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:27:49` | `cowrie.session.connect` |
| `2026-08-16 05:27:55` | `cowrie.client.version` |
| `2026-08-16 05:27:55` | `cowrie.client.kex` |
| `2026-08-16 05:28:23` | `cowrie.login.success` |
| `2026-08-16 05:28:36` | `cowrie.session.params` |
| `2026-08-16 05:28:36` | `cowrie.command.input` |
| `2026-08-16 05:28:43` | `cowrie.log.closed` |
| `2026-08-16 05:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4897c13cc810

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-08-16 05:33 |
| **Last Seen** | 2026-08-16 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:33:52` | `cowrie.session.connect` |
| `2026-08-16 05:33:52` | `cowrie.client.version` |
| `2026-08-16 05:33:52` | `cowrie.client.kex` |
| `2026-08-16 05:33:53` | `cowrie.login.success` |
| `2026-08-16 05:33:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560ee00fa917

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-08-16 05:36 |
| **Last Seen** | 2026-08-16 05:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:36:32` | `cowrie.session.connect` |
| `2026-08-16 05:36:33` | `cowrie.client.version` |
| `2026-08-16 05:36:33` | `cowrie.client.kex` |
| `2026-08-16 05:36:34` | `cowrie.login.success` |
| `2026-08-16 05:36:34` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beec8764d0f3

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-16 05:36 |
| **Last Seen** | 2026-08-16 05:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:36:39` | `cowrie.session.connect` |
| `2026-08-16 05:36:41` | `cowrie.client.version` |
| `2026-08-16 05:36:41` | `cowrie.client.kex` |
| `2026-08-16 05:36:43` | `cowrie.login.success` |
| `2026-08-16 05:36:44` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e450ea2a28c

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-08-16 05:39 |
| **Last Seen** | 2026-08-16 05:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:39:29` | `cowrie.session.connect` |
| `2026-08-16 05:39:30` | `cowrie.client.version` |
| `2026-08-16 05:39:30` | `cowrie.client.kex` |
| `2026-08-16 05:39:32` | `cowrie.login.success` |
| `2026-08-16 05:39:33` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5535bcc88aa

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-08-16 05:41 |
| **Last Seen** | 2026-08-16 05:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:41:50` | `cowrie.session.connect` |
| `2026-08-16 05:41:51` | `cowrie.client.version` |
| `2026-08-16 05:41:51` | `cowrie.client.kex` |
| `2026-08-16 05:41:54` | `cowrie.login.success` |
| `2026-08-16 05:41:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c710efa35ffb

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-16 05:42 |
| **Last Seen** | 2026-08-16 05:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:42:01` | `cowrie.session.connect` |
| `2026-08-16 05:42:01` | `cowrie.client.version` |
| `2026-08-16 05:42:01` | `cowrie.client.kex` |
| `2026-08-16 05:42:03` | `cowrie.login.success` |
| `2026-08-16 05:42:04` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0eb62b40a68

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-08-16 05:42 |
| **Last Seen** | 2026-08-16 05:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:42:03` | `cowrie.session.connect` |
| `2026-08-16 05:42:04` | `cowrie.client.version` |
| `2026-08-16 05:42:04` | `cowrie.client.kex` |
| `2026-08-16 05:42:06` | `cowrie.login.success` |
| `2026-08-16 05:42:07` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe13cedf7b1

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 05:45 |
| **Last Seen** | 2026-08-16 05:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:45:08` | `cowrie.session.connect` |
| `2026-08-16 05:45:08` | `cowrie.client.version` |
| `2026-08-16 05:45:08` | `cowrie.client.kex` |
| `2026-08-16 05:45:08` | `cowrie.login.success` |
| `2026-08-16 05:45:09` | `cowrie.session.params` |
| `2026-08-16 05:45:09` | `cowrie.command.input` |
| `2026-08-16 05:45:10` | `cowrie.log.closed` |
| `2026-08-16 05:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ada187a0e9d

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 05:46 |
| **Last Seen** | 2026-08-16 05:47 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:46:16` | `cowrie.session.connect` |
| `2026-08-16 05:46:21` | `cowrie.client.version` |
| `2026-08-16 05:46:21` | `cowrie.client.kex` |
| `2026-08-16 05:46:45` | `cowrie.login.success` |
| `2026-08-16 05:47:00` | `cowrie.session.params` |
| `2026-08-16 05:47:00` | `cowrie.command.input` |
| `2026-08-16 05:47:06` | `cowrie.log.closed` |
| `2026-08-16 05:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e02b3493b50

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-08-16 05:52 |
| **Last Seen** | 2026-08-16 05:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:52:38` | `cowrie.session.connect` |
| `2026-08-16 05:52:39` | `cowrie.client.version` |
| `2026-08-16 05:52:39` | `cowrie.client.kex` |
| `2026-08-16 05:52:40` | `cowrie.login.success` |
| `2026-08-16 05:52:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d06e67d98a9

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-16 05:52 |
| **Last Seen** | 2026-08-16 05:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:52:45` | `cowrie.session.connect` |
| `2026-08-16 05:52:45` | `cowrie.client.version` |
| `2026-08-16 05:52:46` | `cowrie.client.kex` |
| `2026-08-16 05:52:46` | `cowrie.login.success` |
| `2026-08-16 05:52:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960ac64a012d

| Field | Detail |
|---|---|
| **Source IP** | `34.156.97[.]37` |
| **First Seen** | 2026-08-16 05:53 |
| **Last Seen** | 2026-08-16 05:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:53:17` | `cowrie.session.connect` |
| `2026-08-16 05:53:17` | `cowrie.login.success` |
| `2026-08-16 05:53:17` | `cowrie.session.params` |
| `2026-08-16 05:53:17` | `cowrie.command.input` |
| `2026-08-16 05:53:17` | `cowrie.command.input` |
| `2026-08-16 05:53:17` | `cowrie.command.failed` |
| `2026-08-16 05:53:17` | `cowrie.command.input` |
| `2026-08-16 05:53:17` | `cowrie.log.closed` |
| `2026-08-16 05:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.97[.]37` to AbuseIPDB if not already reported
- [ ] Block `34.156.97[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c3a8eb2b03

| Field | Detail |
|---|---|
| **Source IP** | `34.156.97[.]37` |
| **First Seen** | 2026-08-16 05:53 |
| **Last Seen** | 2026-08-16 05:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:53:30` | `cowrie.session.connect` |
| `2026-08-16 05:53:30` | `cowrie.login.success` |
| `2026-08-16 05:53:31` | `cowrie.session.params` |
| `2026-08-16 05:53:31` | `cowrie.command.input` |
| `2026-08-16 05:53:31` | `cowrie.command.failed` |
| `2026-08-16 05:53:43` | `cowrie.log.closed` |
| `2026-08-16 05:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.97[.]37` to AbuseIPDB if not already reported
- [ ] Block `34.156.97[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d3a0f4fff4

| Field | Detail |
|---|---|
| **Source IP** | `34.156.97[.]37` |
| **First Seen** | 2026-08-16 05:53 |
| **Last Seen** | 2026-08-16 05:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:53:32` | `cowrie.session.connect` |
| `2026-08-16 05:53:32` | `cowrie.login.success` |
| `2026-08-16 05:53:33` | `cowrie.session.params` |
| `2026-08-16 05:53:33` | `cowrie.command.input` |
| `2026-08-16 05:53:43` | `cowrie.log.closed` |
| `2026-08-16 05:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.97[.]37` to AbuseIPDB if not already reported
- [ ] Block `34.156.97[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fd90d46bf0

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-08-16 05:55 |
| **Last Seen** | 2026-08-16 05:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:55:21` | `cowrie.session.connect` |
| `2026-08-16 05:55:22` | `cowrie.client.version` |
| `2026-08-16 05:55:22` | `cowrie.client.kex` |
| `2026-08-16 05:55:27` | `cowrie.login.success` |
| `2026-08-16 05:55:28` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2134ed9cb6

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-16 05:55 |
| **Last Seen** | 2026-08-16 05:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 05:55:34` | `cowrie.session.connect` |
| `2026-08-16 05:55:35` | `cowrie.client.version` |
| `2026-08-16 05:55:35` | `cowrie.client.kex` |
| `2026-08-16 05:55:37` | `cowrie.login.success` |
| `2026-08-16 05:55:38` | `cowrie.direct-tcpip.request` |
| `2026-08-16 05:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf53a80b54e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 06:04 |
| **Last Seen** | 2026-08-16 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:04:15` | `cowrie.session.connect` |
| `2026-08-16 06:04:15` | `cowrie.client.version` |
| `2026-08-16 06:04:15` | `cowrie.client.kex` |
| `2026-08-16 06:04:16` | `cowrie.login.success` |
| `2026-08-16 06:04:17` | `cowrie.session.params` |
| `2026-08-16 06:04:17` | `cowrie.command.input` |
| `2026-08-16 06:04:17` | `cowrie.log.closed` |
| `2026-08-16 06:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d5bec16c88

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 06:04 |
| **Last Seen** | 2026-08-16 06:05 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:04:33` | `cowrie.session.connect` |
| `2026-08-16 06:04:37` | `cowrie.client.version` |
| `2026-08-16 06:04:37` | `cowrie.client.kex` |
| `2026-08-16 06:05:04` | `cowrie.login.success` |
| `2026-08-16 06:05:18` | `cowrie.session.params` |
| `2026-08-16 06:05:18` | `cowrie.command.input` |
| `2026-08-16 06:05:23` | `cowrie.log.closed` |
| `2026-08-16 06:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f62f8f89f4

| Field | Detail |
|---|---|
| **Source IP** | `111.46.77[.]2` |
| **First Seen** | 2026-08-16 06:07 |
| **Last Seen** | 2026-08-16 06:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:07:51` | `cowrie.session.connect` |
| `2026-08-16 06:07:52` | `cowrie.client.version` |
| `2026-08-16 06:07:52` | `cowrie.client.kex` |
| `2026-08-16 06:07:55` | `cowrie.login.success` |
| `2026-08-16 06:07:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.46.77[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.46.77[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e25769a2d1

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-16 06:10 |
| **Last Seen** | 2026-08-16 06:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:10:17` | `cowrie.session.connect` |
| `2026-08-16 06:10:18` | `cowrie.client.version` |
| `2026-08-16 06:10:18` | `cowrie.client.kex` |
| `2026-08-16 06:10:20` | `cowrie.login.success` |
| `2026-08-16 06:10:21` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dedcb34dadd

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-08-16 06:10 |
| **Last Seen** | 2026-08-16 06:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:10:27` | `cowrie.session.connect` |
| `2026-08-16 06:10:28` | `cowrie.client.version` |
| `2026-08-16 06:10:28` | `cowrie.client.kex` |
| `2026-08-16 06:10:30` | `cowrie.login.success` |
| `2026-08-16 06:10:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f72f852594c

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-08-16 06:13 |
| **Last Seen** | 2026-08-16 06:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:13:05` | `cowrie.session.connect` |
| `2026-08-16 06:13:06` | `cowrie.client.version` |
| `2026-08-16 06:13:06` | `cowrie.client.kex` |
| `2026-08-16 06:13:09` | `cowrie.login.success` |
| `2026-08-16 06:13:11` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96fab11b59f0

| Field | Detail |
|---|---|
| **Source IP** | `220.180.166[.]214` |
| **First Seen** | 2026-08-16 06:13 |
| **Last Seen** | 2026-08-16 06:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:13:17` | `cowrie.session.connect` |
| `2026-08-16 06:13:18` | `cowrie.client.version` |
| `2026-08-16 06:13:18` | `cowrie.client.kex` |
| `2026-08-16 06:13:21` | `cowrie.login.success` |
| `2026-08-16 06:13:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.166[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.180.166[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a554dc5632

| Field | Detail |
|---|---|
| **Source IP** | `183.63.220[.]210` |
| **First Seen** | 2026-08-16 06:15 |
| **Last Seen** | 2026-08-16 06:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:15:41` | `cowrie.session.connect` |
| `2026-08-16 06:15:42` | `cowrie.client.version` |
| `2026-08-16 06:15:42` | `cowrie.client.kex` |
| `2026-08-16 06:15:45` | `cowrie.login.success` |
| `2026-08-16 06:15:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.63.220[.]210` to AbuseIPDB if not already reported
- [ ] Block `183.63.220[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b79e30755a

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-08-16 06:15 |
| **Last Seen** | 2026-08-16 06:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:15:52` | `cowrie.session.connect` |
| `2026-08-16 06:15:53` | `cowrie.client.version` |
| `2026-08-16 06:15:53` | `cowrie.client.kex` |
| `2026-08-16 06:15:55` | `cowrie.login.success` |
| `2026-08-16 06:15:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3932b878351a

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-08-16 06:15 |
| **Last Seen** | 2026-08-16 06:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:15:56` | `cowrie.session.connect` |
| `2026-08-16 06:15:57` | `cowrie.client.version` |
| `2026-08-16 06:15:57` | `cowrie.client.kex` |
| `2026-08-16 06:15:59` | `cowrie.login.success` |
| `2026-08-16 06:16:00` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20a47796504

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-08-16 06:16 |
| **Last Seen** | 2026-08-16 06:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:16:06` | `cowrie.session.connect` |
| `2026-08-16 06:16:07` | `cowrie.client.version` |
| `2026-08-16 06:16:07` | `cowrie.client.kex` |
| `2026-08-16 06:16:08` | `cowrie.login.success` |
| `2026-08-16 06:16:09` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bbdc4f6cb87

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 06:23 |
| **Last Seen** | 2026-08-16 06:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:23:23` | `cowrie.session.connect` |
| `2026-08-16 06:23:23` | `cowrie.client.version` |
| `2026-08-16 06:23:23` | `cowrie.client.kex` |
| `2026-08-16 06:23:23` | `cowrie.login.success` |
| `2026-08-16 06:23:24` | `cowrie.session.params` |
| `2026-08-16 06:23:24` | `cowrie.command.input` |
| `2026-08-16 06:23:25` | `cowrie.log.closed` |
| `2026-08-16 06:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8b23593ecb

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-16 06:26 |
| **Last Seen** | 2026-08-16 06:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:26:38` | `cowrie.session.connect` |
| `2026-08-16 06:26:38` | `cowrie.client.version` |
| `2026-08-16 06:26:38` | `cowrie.client.kex` |
| `2026-08-16 06:26:40` | `cowrie.login.success` |
| `2026-08-16 06:26:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ef86886df3

| Field | Detail |
|---|---|
| **Source IP** | `14.153.230[.]167` |
| **First Seen** | 2026-08-16 06:26 |
| **Last Seen** | 2026-08-16 06:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:26:47` | `cowrie.session.connect` |
| `2026-08-16 06:26:48` | `cowrie.client.version` |
| `2026-08-16 06:26:48` | `cowrie.client.kex` |
| `2026-08-16 06:26:50` | `cowrie.login.success` |
| `2026-08-16 06:26:51` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.230[.]167` to AbuseIPDB if not already reported
- [ ] Block `14.153.230[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ddbd38c152

| Field | Detail |
|---|---|
| **Source IP** | `181.191.148[.]177` |
| **First Seen** | 2026-08-16 06:29 |
| **Last Seen** | 2026-08-16 06:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:29:51` | `cowrie.session.connect` |
| `2026-08-16 06:29:53` | `cowrie.login.success` |
| `2026-08-16 06:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.148[.]177` to AbuseIPDB if not already reported
- [ ] Block `181.191.148[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae090169613

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 06:38 |
| **Last Seen** | 2026-08-16 06:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:38:49` | `cowrie.session.connect` |
| `2026-08-16 06:38:49` | `cowrie.client.version` |
| `2026-08-16 06:38:52` | `cowrie.client.kex` |
| `2026-08-16 06:38:52` | `cowrie.login.success` |
| `2026-08-16 06:38:53` | `cowrie.session.params` |
| `2026-08-16 06:38:53` | `cowrie.command.input` |
| `2026-08-16 06:38:53` | `cowrie.log.closed` |
| `2026-08-16 06:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e03e1031b82

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-16 06:41 |
| **Last Seen** | 2026-08-16 06:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:41:48` | `cowrie.session.connect` |
| `2026-08-16 06:41:49` | `cowrie.client.version` |
| `2026-08-16 06:41:49` | `cowrie.client.kex` |
| `2026-08-16 06:41:53` | `cowrie.login.success` |
| `2026-08-16 06:41:54` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ead3eff19ea

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 06:42 |
| **Last Seen** | 2026-08-16 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:42:30` | `cowrie.session.connect` |
| `2026-08-16 06:42:30` | `cowrie.client.version` |
| `2026-08-16 06:42:30` | `cowrie.client.kex` |
| `2026-08-16 06:42:31` | `cowrie.login.success` |
| `2026-08-16 06:42:32` | `cowrie.session.params` |
| `2026-08-16 06:42:32` | `cowrie.command.input` |
| `2026-08-16 06:42:32` | `cowrie.log.closed` |
| `2026-08-16 06:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d1e4d4cf8c

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-08-16 06:44 |
| **Last Seen** | 2026-08-16 06:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:44:18` | `cowrie.session.connect` |
| `2026-08-16 06:44:19` | `cowrie.client.version` |
| `2026-08-16 06:44:19` | `cowrie.client.kex` |
| `2026-08-16 06:44:21` | `cowrie.login.success` |
| `2026-08-16 06:44:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa75caf4c1a1

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-08-16 06:44 |
| **Last Seen** | 2026-08-16 06:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:44:28` | `cowrie.session.connect` |
| `2026-08-16 06:44:28` | `cowrie.client.version` |
| `2026-08-16 06:44:28` | `cowrie.client.kex` |
| `2026-08-16 06:44:30` | `cowrie.login.success` |
| `2026-08-16 06:44:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3176d4573c

| Field | Detail |
|---|---|
| **Source IP** | `34.62.85[.]137` |
| **First Seen** | 2026-08-16 06:45 |
| **Last Seen** | 2026-08-16 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:45:05` | `cowrie.session.connect` |
| `2026-08-16 06:45:05` | `cowrie.login.success` |
| `2026-08-16 06:45:05` | `cowrie.session.params` |
| `2026-08-16 06:45:05` | `cowrie.command.input` |
| `2026-08-16 06:45:05` | `cowrie.command.input` |
| `2026-08-16 06:45:05` | `cowrie.command.failed` |
| `2026-08-16 06:45:05` | `cowrie.command.input` |
| `2026-08-16 06:45:05` | `cowrie.log.closed` |
| `2026-08-16 06:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.85[.]137` to AbuseIPDB if not already reported
- [ ] Block `34.62.85[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e62361704a

| Field | Detail |
|---|---|
| **Source IP** | `34.62.85[.]137` |
| **First Seen** | 2026-08-16 06:45 |
| **Last Seen** | 2026-08-16 06:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:45:18` | `cowrie.session.connect` |
| `2026-08-16 06:45:18` | `cowrie.login.success` |
| `2026-08-16 06:45:19` | `cowrie.session.params` |
| `2026-08-16 06:45:19` | `cowrie.command.input` |
| `2026-08-16 06:45:19` | `cowrie.command.failed` |
| `2026-08-16 06:45:29` | `cowrie.log.closed` |
| `2026-08-16 06:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.85[.]137` to AbuseIPDB if not already reported
- [ ] Block `34.62.85[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38f9660e1bd

| Field | Detail |
|---|---|
| **Source IP** | `34.62.85[.]137` |
| **First Seen** | 2026-08-16 06:45 |
| **Last Seen** | 2026-08-16 06:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:45:20` | `cowrie.session.connect` |
| `2026-08-16 06:45:20` | `cowrie.login.success` |
| `2026-08-16 06:45:21` | `cowrie.session.params` |
| `2026-08-16 06:45:21` | `cowrie.command.input` |
| `2026-08-16 06:45:29` | `cowrie.log.closed` |
| `2026-08-16 06:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.85[.]137` to AbuseIPDB if not already reported
- [ ] Block `34.62.85[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d9d06bd318

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-16 06:46 |
| **Last Seen** | 2026-08-16 06:51 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:46:49` | `cowrie.session.connect` |
| `2026-08-16 06:46:50` | `cowrie.client.version` |
| `2026-08-16 06:46:50` | `cowrie.client.kex` |
| `2026-08-16 06:46:53` | `cowrie.login.success` |
| `2026-08-16 06:46:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f393263bb1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 06:46 |
| **Last Seen** | 2026-08-16 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:46:57` | `cowrie.session.connect` |
| `2026-08-16 06:46:57` | `cowrie.client.version` |
| `2026-08-16 06:46:57` | `cowrie.client.kex` |
| `2026-08-16 06:46:58` | `cowrie.login.success` |
| `2026-08-16 06:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656e0bbefd35

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 06:46 |
| **Last Seen** | 2026-08-16 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:46:58` | `cowrie.session.connect` |
| `2026-08-16 06:46:58` | `cowrie.client.version` |
| `2026-08-16 06:46:58` | `cowrie.client.kex` |
| `2026-08-16 06:46:59` | `cowrie.login.success` |
| `2026-08-16 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba642fb8961

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 06:47 |
| **Last Seen** | 2026-08-16 06:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:47:32` | `cowrie.session.connect` |
| `2026-08-16 06:47:32` | `cowrie.client.version` |
| `2026-08-16 06:47:32` | `cowrie.client.kex` |
| `2026-08-16 06:47:32` | `cowrie.login.success` |
| `2026-08-16 06:47:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:47:32` | `cowrie.direct-tcpip.data` |
| `2026-08-16 06:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7de535081a

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]61` |
| **First Seen** | 2026-08-16 06:49 |
| **Last Seen** | 2026-08-16 06:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:49:29` | `cowrie.session.connect` |
| `2026-08-16 06:49:29` | `cowrie.client.version` |
| `2026-08-16 06:49:29` | `cowrie.client.kex` |
| `2026-08-16 06:49:31` | `cowrie.login.success` |
| `2026-08-16 06:49:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]61` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207fca1146b2

| Field | Detail |
|---|---|
| **Source IP** | `27.71.60[.]22` |
| **First Seen** | 2026-08-16 06:49 |
| **Last Seen** | 2026-08-16 06:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:49:37` | `cowrie.session.connect` |
| `2026-08-16 06:49:38` | `cowrie.client.version` |
| `2026-08-16 06:49:38` | `cowrie.client.kex` |
| `2026-08-16 06:49:40` | `cowrie.login.success` |
| `2026-08-16 06:49:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 06:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.71.60[.]22` to AbuseIPDB if not already reported
- [ ] Block `27.71.60[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4688** | 2026-08-16 04:55 | 2026-08-16 06:55 | 5578m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **36** | 2026-08-16 04:57 | 2026-08-16 06:48 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.97[.]37` | **30** | 2026-08-16 05:52 | 2026-08-16 05:53 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.198[.]2` | **30** | 2026-08-16 05:14 | 2026-08-16 05:15 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.85[.]137` | **30** | 2026-08-16 06:44 | 2026-08-16 06:45 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-16 04:55 | 2026-08-16 06:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **3** | 2026-08-16 05:25 | 2026-08-16 06:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-16 05:40 | 2026-08-16 06:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.51.239[.]46` | **2** | 2026-08-16 04:55 | 2026-08-16 04:57 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.142.193[.]164` | **2** | 2026-08-16 06:22 | 2026-08-16 06:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `50.194.57[.]209` | **2** | 2026-08-16 06:33 | 2026-08-16 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-16 05:03 | 2026-08-16 05:04 | 43s | 0 | `T1592` | 🟢 LOW |
| `110.25.105[.]161` | 1 | 2026-08-16 06:42 | 2026-08-16 06:42 | 54s | 0 | `T1592` | 🟢 LOW |
| `115.160.67[.]73` | 1 | 2026-08-16 06:19 | 2026-08-16 06:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.190.243[.]73` | 1 | 2026-08-16 05:17 | 2026-08-16 05:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.99.255[.]13` | 1 | 2026-08-16 05:29 | 2026-08-16 05:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `124.152.90[.]68` | 1 | 2026-08-16 05:03 | 2026-08-16 05:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.239.129[.]2` | 1 | 2026-08-16 05:42 | 2026-08-16 05:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-16 06:34 | 2026-08-16 06:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]61` | 1 | 2026-08-16 06:07 | 2026-08-16 06:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]51` | 1 | 2026-08-16 06:08 | 2026-08-16 06:08 | 11s | 0 | `T1592` | 🟢 LOW |
| `183.243.126[.]46` | 1 | 2026-08-16 06:40 | 2026-08-16 06:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.154.212[.]113` | 1 | 2026-08-16 05:35 | 2026-08-16 05:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `201.97.213[.]235` | 1 | 2026-08-16 06:26 | 2026-08-16 06:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `60.163.139[.]198` | 1 | 2026-08-16 06:11 | 2026-08-16 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.251.40[.]153` | 1 | 2026-08-16 05:27 | 2026-08-16 05:28 | 11s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]34` | 1 | 2026-08-16 05:06 | 2026-08-16 05:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.31.230[.]91` | 1 | 2026-08-16 06:43 | 2026-08-16 06:44 | 11s | 0 | `T1592` | 🟢 LOW |
| `82.224.163[.]144` | 1 | 2026-08-16 05:42 | 2026-08-16 05:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-16 05:08 | 2026-08-16 05:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-16 05:33 | 2026-08-16 05:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.129.165[.]39` | 1 | 2026-08-16 05:01 | 2026-08-16 05:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `93.177.157[.]179` | 1 | 2026-08-16 05:39 | 2026-08-16 05:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-08-16 05:08 | 2026-08-16 05:08 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `14.153.230[.]167` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `83.191.176[.]93` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 45 |
| `31.41.84[.]98` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `88.129.165[.]39` | SE | Bredband2 AB | **100** ⚠️ | 11 |
| `181.225.32[.]51` | VE | IFX Networks Venezuela C.A. | **100** ⚠️ | 5 |
| `112.30.127[.]9` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `27.71.60[.]22` | VN | Viettel Group | **100** ⚠️ | 50 |
| `171.217.70[.]151` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `136.116.129[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `85.152.57[.]60` | ES | TeleCable | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 22 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 21 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 21 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4964 cases |
| Tool 34  | Credential Extractor        | ✅ 106 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 91 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 68 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 87 priority case(s) shown individually · 34 recon entry/entries in table (11 group(s) consolidating 4831 session(s)).

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
_Report time: 2026-08-16T08:34:59Z_

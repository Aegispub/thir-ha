# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-22 |
| **Generated At** | 2026-07-22T19:27:19Z |
| **Shift Time** | 19:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **127** |
| Confirmed Threats | **115** |
| False Positives Filtered | **12** (9.4%) |
| Unique Attacker IPs | **69** |
| Countries of Origin | **24** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **33** |
| Malware Samples Analyzed | **2** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **126** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **17** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **108** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 50 |
| `support` | 13 |
| `ubnt` | 11 |
| `admin` | 11 |
| `unknown` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `9999` | 6 |
| `999` | 6 |
| `99999` | 5 |
| `support` | 4 |
| `p@ssw0rd` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `9999` | 6 |
| `admin` | `999` | 6 |
| `ubnt` | `99999` | 5 |
| `support` | `support` | 4 |
| `root` | `LeitboGi0ro` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `92.118.39.71` | 2026-07-22T16:56:35 |
| `support` | `support2019` | `65.181.79.60` | 2026-07-22T16:56:47 |
| `support` | `support2019` | `10.0.0.73` | 2026-07-22T16:57:03 |
| `root` | `1234567890` | `92.118.39.71` | 2026-07-22T16:58:48 |
| `ubnt` | `9999` | `121.202.138.181` | 2026-07-22T17:00:27 |
| `ubnt` | `9999` | `211.53.58.10` | 2026-07-22T17:00:38 |
| `root` | `123qwe` | `92.118.39.71` | 2026-07-22T17:01:09 |
| `support` | `support` | `176.53.159.196` | 2026-07-22T17:02:01 |
| `support` | `2222222` | `183.167.234.154` | 2026-07-22T17:03:05 |
| `support` | `2222222` | `10.0.0.73` | 2026-07-22T17:03:16 |
| `support` | `support` | `10.0.0.73` | 2026-07-22T17:03:19 |
| `root` | `123qwerty` | `92.118.39.71` | 2026-07-22T17:03:24 |
| `ubnt` | `9999` | `96.1.40.151` | 2026-07-22T17:03:46 |
| `ubnt` | `9999` | `36.154.134.146` | 2026-07-22T17:04:01 |
| `ubnt` | `9999` | `10.0.0.73` | 2026-07-22T17:04:06 |
| `root` | `21` | `92.118.39.71` | 2026-07-22T17:05:39 |
| `root` | `321` | `92.118.39.71` | 2026-07-22T17:08:10 |
| `Ubnt` | `p@ssw0rd` | `179.185.1.97` | 2026-07-22T17:09:03 |
| `root` | `4321` | `92.118.39.71` | 2026-07-22T17:10:37 |
| `root` | `P455W0RD` | `10.0.0.73` | 2026-07-22T17:12:08 |
| `Ubnt` | `p@ssw0rd` | `220.80.223.144` | 2026-07-22T17:12:19 |
| `Ubnt` | `p@ssw0rd` | `187.8.120.90` | 2026-07-22T17:12:32 |
| `root` | `54321` | `92.118.39.71` | 2026-07-22T17:12:52 |
| `root` | `P455W0RD` | `185.242.3.195` | 2026-07-22T17:13:30 |
| `root` | `654321` | `92.118.39.71` | 2026-07-22T17:15:03 |
| `default` | `default2021` | `113.160.140.138` | 2026-07-22T17:16:56 |
| `root` | `P4ssw0rd` | `92.118.39.71` | 2026-07-22T17:17:16 |
| `a` | `a` | `165.232.61.133` | 2026-07-22T17:18:36 |
| `root` | `P4ssword` | `92.118.39.71` | 2026-07-22T17:19:41 |
| `default` | `default2021` | `10.0.0.73` | 2026-07-22T17:20:22 |
| `root` | `Pass@word12` | `185.242.3.195` | 2026-07-22T17:21:08 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-07-22T17:22:18 |
| `root` | `ubuntu` | `61.240.17.66` | 2026-07-22T17:24:27 |
| `root` | `Passw0rd` | `92.118.39.71` | 2026-07-22T17:24:40 |
| `config` | `333333` | `210.206.24.237` | 2026-07-22T17:25:07 |
| `config` | `333333` | `211.238.237.254` | 2026-07-22T17:25:16 |
| `root` | `p4ssword` | `92.118.39.71` | 2026-07-22T17:26:57 |
| `blank` | `blank777` | `146.190.215.195` | 2026-07-22T17:27:47 |
| `blank` | `blank777` | `196.190.41.137` | 2026-07-22T17:27:58 |
| `blank` | `blank777` | `10.0.0.73` | 2026-07-22T17:28:11 |
| `config` | `333333` | `51.116.117.203` | 2026-07-22T17:28:35 |
| `root` | `p@ssw0rd` | `92.118.39.71` | 2026-07-22T17:29:13 |
| `ubnt` | `99999` | `113.108.88.121` | 2026-07-22T17:33:42 |
| `ubnt` | `99999` | `46.210.94.61` | 2026-07-22T17:33:55 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-22T17:35:10 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-22T17:35:11 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-22T17:35:20 |
| `ubnt` | `99999` | `186.235.193.170` | 2026-07-22T17:37:12 |
| `ubnt` | `99999` | `10.0.0.73` | 2026-07-22T17:37:35 |
| `admin` | `admin2021` | `191.36.154.175` | 2026-07-22T17:43:25 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-22T17:44:40 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-22T17:44:40 |
| `unknown` | `2222` | `10.0.0.73` | 2026-07-22T17:53:34 |
| `admin` | `admin` | `8.208.44.152` | 2026-07-22T18:01:35 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-22T18:01:35 |
| `user` | `user444` | `85.105.2.51` | 2026-07-22T18:01:42 |
| `user` | `user444` | `10.0.0.73` | 2026-07-22T18:02:04 |
| `root` | `Pass@word12` | `10.0.0.73` | 2026-07-22T18:05:21 |
| `nobody` | `nobody12345` | `91.241.150.246` | 2026-07-22T18:06:38 |
| `nobody` | `nobody12345` | `10.0.0.73` | 2026-07-22T18:06:59 |
| `nobody` | `nobody555` | `178.178.194.128` | 2026-07-22T18:13:40 |
| `root` | `1g2w3e4r` | `185.242.3.195` | 2026-07-22T18:14:05 |
| `root` | `000000` | `92.118.39.49` | 2026-07-22T18:14:10 |
| `root` | `111111` | `92.118.39.49` | 2026-07-22T18:16:16 |
| `test` | `0` | `10.0.0.73` | 2026-07-22T18:18:07 |
| `root` | `123` | `92.118.39.49` | 2026-07-22T18:18:20 |
| `root` | `123123` | `92.118.39.49` | 2026-07-22T18:20:21 |
| `root` | `1234` | `92.118.39.49` | 2026-07-22T18:22:21 |
| `sammy` | `Test123` | `8.217.235.231` | 2026-07-22T18:23:20 |
| `345gs5662d34` | `345gs5662d34` | `8.217.235.231` | 2026-07-22T18:23:24 |
| `sammy` | `3245gs5662d34` | `8.217.235.231` | 2026-07-22T18:23:25 |
| `root` | `12345` | `92.118.39.49` | 2026-07-22T18:24:16 |
| `123` | `123456` | `103.88.76.27` | 2026-07-22T18:25:56 |
| `345gs5662d34` | `345gs5662d34` | `103.88.76.27` | 2026-07-22T18:26:01 |
| `123` | `3245gs5662d34` | `103.88.76.27` | 2026-07-22T18:26:03 |
| `unknown` | `000` | `103.67.152.201` | 2026-07-22T18:26:16 |
| `test` | `test2022` | `93.177.157.179` | 2026-07-22T18:26:29 |
| `unknown` | `000` | `220.246.46.144` | 2026-07-22T18:26:29 |
| `test` | `test2022` | `49.206.194.29` | 2026-07-22T18:26:37 |
| `unknown` | `000` | `10.0.0.73` | 2026-07-22T18:26:41 |
| `root` | `12345678` | `92.118.39.49` | 2026-07-22T18:27:56 |
| `test` | `test2022` | `102.211.7.162` | 2026-07-22T18:29:30 |
| `root` | `123456789` | `92.118.39.49` | 2026-07-22T18:29:41 |
| `test` | `test2022` | `10.0.0.73` | 2026-07-22T18:29:56 |
| `root` | `1q2w3e4r` | `92.118.39.49` | 2026-07-22T18:31:28 |
| `root` | `654321` | `92.118.39.49` | 2026-07-22T18:33:19 |
| `root` | `P@ssw0rd` | `92.118.39.49` | 2026-07-22T18:35:09 |
| `root` | `admin` | `92.118.39.49` | 2026-07-22T18:36:59 |
| `root` | `admin123` | `92.118.39.49` | 2026-07-22T18:38:49 |
| `admin` | `999` | `196.188.93.169` | 2026-07-22T18:38:56 |
| `admin` | `999` | `92.84.21.186` | 2026-07-22T18:39:02 |
| `root` | `passw0rd` | `92.118.39.49` | 2026-07-22T18:40:40 |
| `support` | `444` | `59.48.39.222` | 2026-07-22T18:41:45 |
| `support` | `444` | `10.0.0.73` | 2026-07-22T18:42:04 |
| `admin` | `999` | `117.250.19.91` | 2026-07-22T18:42:16 |
| `root` | `password` | `92.118.39.49` | 2026-07-22T18:42:27 |
| `admin` | `999` | `49.124.150.250` | 2026-07-22T18:42:32 |
| `admin` | `999` | `10.0.0.73` | 2026-07-22T18:42:34 |
| `root` | `password1` | `92.118.39.49` | 2026-07-22T18:44:18 |
| `root` | `qwerty` | `92.118.39.49` | 2026-07-22T18:46:04 |
| `root` | `root123` | `92.118.39.49` | 2026-07-22T18:47:50 |
| `root` | `toor` | `92.118.39.49` | 2026-07-22T18:49:38 |
| `User` | `1234567` | `122.160.15.31` | 2026-07-22T18:50:53 |
| `User` | `1234567` | `10.0.0.73` | 2026-07-22T18:51:22 |
| `admin` | `000000` | `92.118.39.49` | 2026-07-22T18:51:31 |
| `blank` | `blank2000` | `95.165.142.8` | 2026-07-22T18:52:42 |
| `blank` | `blank2000` | `10.0.0.73` | 2026-07-22T18:53:06 |
| `admin` | `111111` | `92.118.39.49` | 2026-07-22T18:53:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **127** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 47 |
| OpenSSH | 38 |
| libssh | 13 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 37 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 37 | 37 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 37 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 37 | 37 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 36 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.49`, `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `8.217.235.231`, `103.88.76.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **69** |
| Unique ASNs | **47** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS3786` | LG DACOM Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-49df1a145903

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 16:56 |
| **Last Seen** | 2026-07-22 16:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 16:56:33` | `cowrie.session.connect` |
| `2026-07-22 16:56:34` | `cowrie.client.version` |
| `2026-07-22 16:56:34` | `cowrie.client.kex` |
| `2026-07-22 16:56:35` | `cowrie.login.success` |
| `2026-07-22 16:56:36` | `cowrie.session.params` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.success` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:36` | `cowrie.command.input` |
| `2026-07-22 16:56:37` | `cowrie.log.closed` |
| `2026-07-22 16:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36306b2f305

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-07-22 16:56 |
| **Last Seen** | 2026-07-22 16:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 16:56:44` | `cowrie.session.connect` |
| `2026-07-22 16:56:45` | `cowrie.client.version` |
| `2026-07-22 16:56:45` | `cowrie.client.kex` |
| `2026-07-22 16:56:47` | `cowrie.login.success` |
| `2026-07-22 16:56:47` | `cowrie.direct-tcpip.request` |
| `2026-07-22 16:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e0ac5dba3f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 16:58 |
| **Last Seen** | 2026-07-22 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 16:58:46` | `cowrie.session.connect` |
| `2026-07-22 16:58:46` | `cowrie.client.version` |
| `2026-07-22 16:58:46` | `cowrie.client.kex` |
| `2026-07-22 16:58:48` | `cowrie.login.success` |
| `2026-07-22 16:58:49` | `cowrie.session.params` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.success` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:49` | `cowrie.command.input` |
| `2026-07-22 16:58:50` | `cowrie.log.closed` |
| `2026-07-22 16:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c575ad089046

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-07-22 17:00 |
| **Last Seen** | 2026-07-22 17:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:00:23` | `cowrie.session.connect` |
| `2026-07-22 17:00:24` | `cowrie.client.version` |
| `2026-07-22 17:00:24` | `cowrie.client.kex` |
| `2026-07-22 17:00:27` | `cowrie.login.success` |
| `2026-07-22 17:00:28` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170b0ab99e74

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-07-22 17:00 |
| **Last Seen** | 2026-07-22 17:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:00:33` | `cowrie.session.connect` |
| `2026-07-22 17:00:35` | `cowrie.client.version` |
| `2026-07-22 17:00:35` | `cowrie.client.kex` |
| `2026-07-22 17:00:38` | `cowrie.login.success` |
| `2026-07-22 17:00:39` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f315699df7f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:01 |
| **Last Seen** | 2026-07-22 17:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:01:07` | `cowrie.session.connect` |
| `2026-07-22 17:01:07` | `cowrie.client.version` |
| `2026-07-22 17:01:07` | `cowrie.client.kex` |
| `2026-07-22 17:01:09` | `cowrie.login.success` |
| `2026-07-22 17:01:10` | `cowrie.session.params` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.success` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.command.input` |
| `2026-07-22 17:01:10` | `cowrie.log.closed` |
| `2026-07-22 17:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16df9236d29e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 17:02 |
| **Last Seen** | 2026-07-22 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:02:00` | `cowrie.session.connect` |
| `2026-07-22 17:02:00` | `cowrie.client.version` |
| `2026-07-22 17:02:00` | `cowrie.client.kex` |
| `2026-07-22 17:02:01` | `cowrie.login.success` |
| `2026-07-22 17:02:01` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:02:01` | `cowrie.direct-tcpip.data` |
| `2026-07-22 17:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f687f1301c7f

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-07-22 17:02 |
| **Last Seen** | 2026-07-22 17:03 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:02:56` | `cowrie.session.connect` |
| `2026-07-22 17:02:57` | `cowrie.client.version` |
| `2026-07-22 17:02:57` | `cowrie.client.kex` |
| `2026-07-22 17:03:05` | `cowrie.login.success` |
| `2026-07-22 17:03:07` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3142d8f56bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:03 |
| **Last Seen** | 2026-07-22 17:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:03:22` | `cowrie.session.connect` |
| `2026-07-22 17:03:22` | `cowrie.client.version` |
| `2026-07-22 17:03:23` | `cowrie.client.kex` |
| `2026-07-22 17:03:24` | `cowrie.login.success` |
| `2026-07-22 17:03:25` | `cowrie.session.params` |
| `2026-07-22 17:03:25` | `cowrie.command.input` |
| `2026-07-22 17:03:25` | `cowrie.command.input` |
| `2026-07-22 17:03:25` | `cowrie.command.input` |
| `2026-07-22 17:03:25` | `cowrie.command.input` |
| `2026-07-22 17:03:25` | `cowrie.command.input` |
| `2026-07-22 17:03:26` | `cowrie.command.success` |
| `2026-07-22 17:03:26` | `cowrie.command.input` |
| `2026-07-22 17:03:26` | `cowrie.command.input` |
| `2026-07-22 17:03:26` | `cowrie.command.input` |
| `2026-07-22 17:03:26` | `cowrie.command.input` |
| `2026-07-22 17:03:26` | `cowrie.log.closed` |
| `2026-07-22 17:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7263fb4338

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-22 17:03 |
| **Last Seen** | 2026-07-22 17:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:03:45` | `cowrie.session.connect` |
| `2026-07-22 17:03:45` | `cowrie.client.version` |
| `2026-07-22 17:03:45` | `cowrie.client.kex` |
| `2026-07-22 17:03:46` | `cowrie.login.success` |
| `2026-07-22 17:03:46` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6017604e1778

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-07-22 17:03 |
| **Last Seen** | 2026-07-22 17:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:03:56` | `cowrie.session.connect` |
| `2026-07-22 17:03:57` | `cowrie.client.version` |
| `2026-07-22 17:03:57` | `cowrie.client.kex` |
| `2026-07-22 17:04:01` | `cowrie.login.success` |
| `2026-07-22 17:04:01` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3426686daf5f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:05 |
| **Last Seen** | 2026-07-22 17:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:05:37` | `cowrie.session.connect` |
| `2026-07-22 17:05:38` | `cowrie.client.version` |
| `2026-07-22 17:05:38` | `cowrie.client.kex` |
| `2026-07-22 17:05:39` | `cowrie.login.success` |
| `2026-07-22 17:05:40` | `cowrie.session.params` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.success` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:40` | `cowrie.command.input` |
| `2026-07-22 17:05:42` | `cowrie.log.closed` |
| `2026-07-22 17:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8226f90617f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:08 |
| **Last Seen** | 2026-07-22 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:08:09` | `cowrie.session.connect` |
| `2026-07-22 17:08:09` | `cowrie.client.version` |
| `2026-07-22 17:08:09` | `cowrie.client.kex` |
| `2026-07-22 17:08:10` | `cowrie.login.success` |
| `2026-07-22 17:08:11` | `cowrie.session.params` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.success` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.command.input` |
| `2026-07-22 17:08:11` | `cowrie.log.closed` |
| `2026-07-22 17:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c399d4803f

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-22 17:09 |
| **Last Seen** | 2026-07-22 17:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:09:01` | `cowrie.session.connect` |
| `2026-07-22 17:09:01` | `cowrie.client.version` |
| `2026-07-22 17:09:01` | `cowrie.client.kex` |
| `2026-07-22 17:09:03` | `cowrie.login.success` |
| `2026-07-22 17:09:03` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78353209c6fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:10 |
| **Last Seen** | 2026-07-22 17:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:10:35` | `cowrie.session.connect` |
| `2026-07-22 17:10:36` | `cowrie.client.version` |
| `2026-07-22 17:10:36` | `cowrie.client.kex` |
| `2026-07-22 17:10:37` | `cowrie.login.success` |
| `2026-07-22 17:10:38` | `cowrie.session.params` |
| `2026-07-22 17:10:38` | `cowrie.command.input` |
| `2026-07-22 17:10:38` | `cowrie.command.input` |
| `2026-07-22 17:10:38` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.command.success` |
| `2026-07-22 17:10:39` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.command.input` |
| `2026-07-22 17:10:39` | `cowrie.log.closed` |
| `2026-07-22 17:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6540cd4d12c

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-22 17:12 |
| **Last Seen** | 2026-07-22 17:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:12:15` | `cowrie.session.connect` |
| `2026-07-22 17:12:16` | `cowrie.client.version` |
| `2026-07-22 17:12:16` | `cowrie.client.kex` |
| `2026-07-22 17:12:19` | `cowrie.login.success` |
| `2026-07-22 17:12:20` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5421358946cb

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-22 17:12 |
| **Last Seen** | 2026-07-22 17:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:12:29` | `cowrie.session.connect` |
| `2026-07-22 17:12:30` | `cowrie.client.version` |
| `2026-07-22 17:12:30` | `cowrie.client.kex` |
| `2026-07-22 17:12:32` | `cowrie.login.success` |
| `2026-07-22 17:12:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c62e453ad2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:12 |
| **Last Seen** | 2026-07-22 17:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:12:50` | `cowrie.session.connect` |
| `2026-07-22 17:12:50` | `cowrie.client.version` |
| `2026-07-22 17:12:50` | `cowrie.client.kex` |
| `2026-07-22 17:12:52` | `cowrie.login.success` |
| `2026-07-22 17:12:53` | `cowrie.session.params` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.success` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.command.input` |
| `2026-07-22 17:12:53` | `cowrie.log.closed` |
| `2026-07-22 17:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f73041286bd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 17:13 |
| **Last Seen** | 2026-07-22 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:13:30` | `cowrie.session.connect` |
| `2026-07-22 17:13:30` | `cowrie.client.version` |
| `2026-07-22 17:13:30` | `cowrie.client.kex` |
| `2026-07-22 17:13:30` | `cowrie.login.success` |
| `2026-07-22 17:13:31` | `cowrie.session.params` |
| `2026-07-22 17:13:31` | `cowrie.command.input` |
| `2026-07-22 17:13:31` | `cowrie.log.closed` |
| `2026-07-22 17:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5111917218

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:15 |
| **Last Seen** | 2026-07-22 17:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:15:01` | `cowrie.session.connect` |
| `2026-07-22 17:15:01` | `cowrie.client.version` |
| `2026-07-22 17:15:01` | `cowrie.client.kex` |
| `2026-07-22 17:15:03` | `cowrie.login.success` |
| `2026-07-22 17:15:04` | `cowrie.session.params` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.success` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.command.input` |
| `2026-07-22 17:15:04` | `cowrie.log.closed` |
| `2026-07-22 17:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23962ab8fd8f

| Field | Detail |
|---|---|
| **Source IP** | `113.160.140[.]138` |
| **First Seen** | 2026-07-22 17:16 |
| **Last Seen** | 2026-07-22 17:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:16:53` | `cowrie.session.connect` |
| `2026-07-22 17:16:54` | `cowrie.client.version` |
| `2026-07-22 17:16:54` | `cowrie.client.kex` |
| `2026-07-22 17:16:56` | `cowrie.login.success` |
| `2026-07-22 17:16:57` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.160.140[.]138` to AbuseIPDB if not already reported
- [ ] Block `113.160.140[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db40af35b575

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:17 |
| **Last Seen** | 2026-07-22 17:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:17:14` | `cowrie.session.connect` |
| `2026-07-22 17:17:14` | `cowrie.client.version` |
| `2026-07-22 17:17:14` | `cowrie.client.kex` |
| `2026-07-22 17:17:16` | `cowrie.login.success` |
| `2026-07-22 17:17:17` | `cowrie.session.params` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.success` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.command.input` |
| `2026-07-22 17:17:17` | `cowrie.log.closed` |
| `2026-07-22 17:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f19dc44021c

| Field | Detail |
|---|---|
| **Source IP** | `165.232.61[.]133` |
| **First Seen** | 2026-07-22 17:18 |
| **Last Seen** | 2026-07-22 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:18:36` | `cowrie.session.connect` |
| `2026-07-22 17:18:36` | `cowrie.client.version` |
| `2026-07-22 17:18:36` | `cowrie.client.kex` |
| `2026-07-22 17:18:36` | `cowrie.login.success` |
| `2026-07-22 17:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.61[.]133` to AbuseIPDB if not already reported
- [ ] Block `165.232.61[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f920d64cfba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:19 |
| **Last Seen** | 2026-07-22 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:19:40` | `cowrie.session.connect` |
| `2026-07-22 17:19:40` | `cowrie.client.version` |
| `2026-07-22 17:19:40` | `cowrie.client.kex` |
| `2026-07-22 17:19:41` | `cowrie.login.success` |
| `2026-07-22 17:19:42` | `cowrie.session.params` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.success` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.command.input` |
| `2026-07-22 17:19:42` | `cowrie.log.closed` |
| `2026-07-22 17:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9737c44c7b6b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 17:21 |
| **Last Seen** | 2026-07-22 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:21:08` | `cowrie.session.connect` |
| `2026-07-22 17:21:08` | `cowrie.client.version` |
| `2026-07-22 17:21:08` | `cowrie.client.kex` |
| `2026-07-22 17:21:08` | `cowrie.login.success` |
| `2026-07-22 17:21:09` | `cowrie.session.params` |
| `2026-07-22 17:21:09` | `cowrie.command.input` |
| `2026-07-22 17:21:09` | `cowrie.log.closed` |
| `2026-07-22 17:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68dcd719dfe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:22 |
| **Last Seen** | 2026-07-22 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:22:17` | `cowrie.session.connect` |
| `2026-07-22 17:22:17` | `cowrie.client.version` |
| `2026-07-22 17:22:17` | `cowrie.client.kex` |
| `2026-07-22 17:22:18` | `cowrie.login.success` |
| `2026-07-22 17:22:19` | `cowrie.session.params` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.success` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.command.input` |
| `2026-07-22 17:22:19` | `cowrie.log.closed` |
| `2026-07-22 17:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d94905ea23f

| Field | Detail |
|---|---|
| **Source IP** | `61.240.17[.]66` |
| **First Seen** | 2026-07-22 17:24 |
| **Last Seen** | 2026-07-22 17:29 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:24:26` | `cowrie.session.connect` |
| `2026-07-22 17:24:26` | `cowrie.client.version` |
| `2026-07-22 17:24:26` | `cowrie.client.kex` |
| `2026-07-22 17:24:27` | `cowrie.login.success` |
| `2026-07-22 17:29:27` | `cowrie.session.file_upload` |
| `2026-07-22 17:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.17[.]66` to AbuseIPDB if not already reported
- [ ] Block `61.240.17[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8623aa31200c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:24 |
| **Last Seen** | 2026-07-22 17:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:24:39` | `cowrie.session.connect` |
| `2026-07-22 17:24:39` | `cowrie.client.version` |
| `2026-07-22 17:24:39` | `cowrie.client.kex` |
| `2026-07-22 17:24:40` | `cowrie.login.success` |
| `2026-07-22 17:24:41` | `cowrie.session.params` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.success` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:41` | `cowrie.command.input` |
| `2026-07-22 17:24:42` | `cowrie.log.closed` |
| `2026-07-22 17:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67021b8a0530

| Field | Detail |
|---|---|
| **Source IP** | `210.206.24[.]237` |
| **First Seen** | 2026-07-22 17:25 |
| **Last Seen** | 2026-07-22 17:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:25:05` | `cowrie.session.connect` |
| `2026-07-22 17:25:06` | `cowrie.client.version` |
| `2026-07-22 17:25:06` | `cowrie.client.kex` |
| `2026-07-22 17:25:07` | `cowrie.login.success` |
| `2026-07-22 17:25:08` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.206.24[.]237` to AbuseIPDB if not already reported
- [ ] Block `210.206.24[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f702257261a5

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-22 17:25 |
| **Last Seen** | 2026-07-22 17:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:25:13` | `cowrie.session.connect` |
| `2026-07-22 17:25:14` | `cowrie.client.version` |
| `2026-07-22 17:25:14` | `cowrie.client.kex` |
| `2026-07-22 17:25:16` | `cowrie.login.success` |
| `2026-07-22 17:25:17` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d251e08f320b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:26 |
| **Last Seen** | 2026-07-22 17:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:26:56` | `cowrie.session.connect` |
| `2026-07-22 17:26:56` | `cowrie.client.version` |
| `2026-07-22 17:26:56` | `cowrie.client.kex` |
| `2026-07-22 17:26:57` | `cowrie.login.success` |
| `2026-07-22 17:26:59` | `cowrie.session.params` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.success` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.command.input` |
| `2026-07-22 17:26:59` | `cowrie.log.closed` |
| `2026-07-22 17:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8144609cca7e

| Field | Detail |
|---|---|
| **Source IP** | `146.190.215[.]195` |
| **First Seen** | 2026-07-22 17:27 |
| **Last Seen** | 2026-07-22 17:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:27:46` | `cowrie.session.connect` |
| `2026-07-22 17:27:46` | `cowrie.client.version` |
| `2026-07-22 17:27:46` | `cowrie.client.kex` |
| `2026-07-22 17:27:47` | `cowrie.login.success` |
| `2026-07-22 17:27:47` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.215[.]195` to AbuseIPDB if not already reported
- [ ] Block `146.190.215[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a223a15e3c

| Field | Detail |
|---|---|
| **Source IP** | `196.190.41[.]137` |
| **First Seen** | 2026-07-22 17:27 |
| **Last Seen** | 2026-07-22 17:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:27:56` | `cowrie.session.connect` |
| `2026-07-22 17:27:57` | `cowrie.client.version` |
| `2026-07-22 17:27:57` | `cowrie.client.kex` |
| `2026-07-22 17:27:58` | `cowrie.login.success` |
| `2026-07-22 17:27:59` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.41[.]137` to AbuseIPDB if not already reported
- [ ] Block `196.190.41[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062803c7ac81

| Field | Detail |
|---|---|
| **Source IP** | `51.116.117[.]203` |
| **First Seen** | 2026-07-22 17:28 |
| **Last Seen** | 2026-07-22 17:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:28:34` | `cowrie.session.connect` |
| `2026-07-22 17:28:34` | `cowrie.client.version` |
| `2026-07-22 17:28:34` | `cowrie.client.kex` |
| `2026-07-22 17:28:35` | `cowrie.login.success` |
| `2026-07-22 17:28:35` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.116.117[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.116.117[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02f2e290189

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 17:29 |
| **Last Seen** | 2026-07-22 17:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:29:11` | `cowrie.session.connect` |
| `2026-07-22 17:29:11` | `cowrie.client.version` |
| `2026-07-22 17:29:11` | `cowrie.client.kex` |
| `2026-07-22 17:29:13` | `cowrie.login.success` |
| `2026-07-22 17:29:15` | `cowrie.session.params` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.success` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.command.input` |
| `2026-07-22 17:29:15` | `cowrie.log.closed` |
| `2026-07-22 17:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da67663d957b

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-07-22 17:33 |
| **Last Seen** | 2026-07-22 17:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:33:40` | `cowrie.session.connect` |
| `2026-07-22 17:33:40` | `cowrie.client.version` |
| `2026-07-22 17:33:40` | `cowrie.client.kex` |
| `2026-07-22 17:33:42` | `cowrie.login.success` |
| `2026-07-22 17:33:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada46192bd75

| Field | Detail |
|---|---|
| **Source IP** | `46.210.94[.]61` |
| **First Seen** | 2026-07-22 17:33 |
| **Last Seen** | 2026-07-22 17:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:33:53` | `cowrie.session.connect` |
| `2026-07-22 17:33:53` | `cowrie.client.version` |
| `2026-07-22 17:33:53` | `cowrie.client.kex` |
| `2026-07-22 17:33:55` | `cowrie.login.success` |
| `2026-07-22 17:33:56` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.210.94[.]61` to AbuseIPDB if not already reported
- [ ] Block `46.210.94[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47cababaf14

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 17:35 |
| **Last Seen** | 2026-07-22 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:35:10` | `cowrie.session.connect` |
| `2026-07-22 17:35:10` | `cowrie.client.version` |
| `2026-07-22 17:35:10` | `cowrie.client.kex` |
| `2026-07-22 17:35:10` | `cowrie.login.success` |
| `2026-07-22 17:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d80a18ee8f95

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 17:35 |
| **Last Seen** | 2026-07-22 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:35:11` | `cowrie.session.connect` |
| `2026-07-22 17:35:11` | `cowrie.client.version` |
| `2026-07-22 17:35:11` | `cowrie.client.kex` |
| `2026-07-22 17:35:11` | `cowrie.login.success` |
| `2026-07-22 17:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605a0b26cc99

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 17:35 |
| **Last Seen** | 2026-07-22 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:35:20` | `cowrie.session.connect` |
| `2026-07-22 17:35:20` | `cowrie.client.version` |
| `2026-07-22 17:35:20` | `cowrie.client.kex` |
| `2026-07-22 17:35:20` | `cowrie.login.success` |
| `2026-07-22 17:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeae8703e165

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 17:35 |
| **Last Seen** | 2026-07-22 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:35:20` | `cowrie.session.connect` |
| `2026-07-22 17:35:20` | `cowrie.client.version` |
| `2026-07-22 17:35:20` | `cowrie.client.kex` |
| `2026-07-22 17:35:20` | `cowrie.login.success` |
| `2026-07-22 17:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267db16d1ab7

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-07-22 17:37 |
| **Last Seen** | 2026-07-22 17:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:37:10` | `cowrie.session.connect` |
| `2026-07-22 17:37:11` | `cowrie.client.version` |
| `2026-07-22 17:37:11` | `cowrie.client.kex` |
| `2026-07-22 17:37:12` | `cowrie.login.success` |
| `2026-07-22 17:37:13` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc18065477e1

| Field | Detail |
|---|---|
| **Source IP** | `191.36.154[.]175` |
| **First Seen** | 2026-07-22 17:43 |
| **Last Seen** | 2026-07-22 17:48 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:43:22` | `cowrie.session.connect` |
| `2026-07-22 17:43:23` | `cowrie.client.version` |
| `2026-07-22 17:43:23` | `cowrie.client.kex` |
| `2026-07-22 17:43:25` | `cowrie.login.success` |
| `2026-07-22 17:43:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 17:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.154[.]175` to AbuseIPDB if not already reported
- [ ] Block `191.36.154[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75b4513a305

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-22 17:44 |
| **Last Seen** | 2026-07-22 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:44:39` | `cowrie.session.connect` |
| `2026-07-22 17:44:39` | `cowrie.client.version` |
| `2026-07-22 17:44:39` | `cowrie.client.kex` |
| `2026-07-22 17:44:40` | `cowrie.login.success` |
| `2026-07-22 17:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721ec2b469f3

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-22 17:44 |
| **Last Seen** | 2026-07-22 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:44:39` | `cowrie.session.connect` |
| `2026-07-22 17:44:39` | `cowrie.client.version` |
| `2026-07-22 17:44:39` | `cowrie.client.kex` |
| `2026-07-22 17:44:40` | `cowrie.login.success` |
| `2026-07-22 17:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3985f7a6c72d

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-22 17:45 |
| **Last Seen** | 2026-07-22 17:47 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:45:02` | `cowrie.session.connect` |
| `2026-07-22 17:45:02` | `cowrie.client.version` |
| `2026-07-22 17:45:02` | `cowrie.client.kex` |
| `2026-07-22 17:45:03` | `cowrie.login.success` |
| `2026-07-22 17:45:05` | `cowrie.session.file_upload` |
| `2026-07-22 17:45:06` | `cowrie.session.params` |
| `2026-07-22 17:45:06` | `cowrie.command.input` |
| `2026-07-22 17:45:06` | `cowrie.command.input` |
| `2026-07-22 17:45:06` | `cowrie.command.input` |
| `2026-07-22 17:45:06` | `cowrie.command.failed` |
| `2026-07-22 17:45:06` | `cowrie.log.closed` |
| `2026-07-22 17:45:07` | `cowrie.session.params` |
| `2026-07-22 17:45:07` | `cowrie.command.input` |
| `2026-07-22 17:45:07` | `cowrie.log.closed` |
| `2026-07-22 17:45:08` | `cowrie.session.params` |
| `2026-07-22 17:45:08` | `cowrie.command.input` |
| `2026-07-22 17:45:08` | `cowrie.log.closed` |
| `2026-07-22 17:45:09` | `cowrie.session.params` |
| `2026-07-22 17:45:09` | `cowrie.command.input` |
| `2026-07-22 17:45:09` | `cowrie.command.failed` |
| `2026-07-22 17:45:09` | `cowrie.command.failed` |
| `2026-07-22 17:46:10` | `cowrie.session.params` |
| `2026-07-22 17:46:10` | `cowrie.command.input` |
| `2026-07-22 17:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df97a691bb2c

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-22 17:47 |
| **Last Seen** | 2026-07-22 17:49 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 17:47:27` | `cowrie.session.connect` |
| `2026-07-22 17:47:27` | `cowrie.client.version` |
| `2026-07-22 17:47:27` | `cowrie.client.kex` |
| `2026-07-22 17:47:28` | `cowrie.login.success` |
| `2026-07-22 17:47:30` | `cowrie.session.file_upload` |
| `2026-07-22 17:47:31` | `cowrie.session.params` |
| `2026-07-22 17:47:31` | `cowrie.command.input` |
| `2026-07-22 17:47:31` | `cowrie.command.input` |
| `2026-07-22 17:47:31` | `cowrie.command.input` |
| `2026-07-22 17:47:31` | `cowrie.command.failed` |
| `2026-07-22 17:47:31` | `cowrie.log.closed` |
| `2026-07-22 17:47:32` | `cowrie.session.params` |
| `2026-07-22 17:47:32` | `cowrie.command.input` |
| `2026-07-22 17:47:32` | `cowrie.log.closed` |
| `2026-07-22 17:47:33` | `cowrie.session.params` |
| `2026-07-22 17:47:33` | `cowrie.command.input` |
| `2026-07-22 17:47:34` | `cowrie.log.closed` |
| `2026-07-22 17:47:35` | `cowrie.session.params` |
| `2026-07-22 17:47:35` | `cowrie.command.input` |
| `2026-07-22 17:47:35` | `cowrie.command.failed` |
| `2026-07-22 17:47:35` | `cowrie.command.failed` |
| `2026-07-22 17:48:36` | `cowrie.session.params` |
| `2026-07-22 17:48:36` | `cowrie.command.input` |
| `2026-07-22 17:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7d3dc89398

| Field | Detail |
|---|---|
| **Source IP** | `8.208.44[.]152` |
| **First Seen** | 2026-07-22 18:01 |
| **Last Seen** | 2026-07-22 18:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:01:34` | `cowrie.session.connect` |
| `2026-07-22 18:01:34` | `cowrie.client.version` |
| `2026-07-22 18:01:34` | `cowrie.client.kex` |
| `2026-07-22 18:01:35` | `cowrie.login.success` |
| `2026-07-22 18:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.208.44[.]152` to AbuseIPDB if not already reported
- [ ] Block `8.208.44[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb0c44ee5358

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-22 18:01 |
| **Last Seen** | 2026-07-22 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:01:35` | `cowrie.session.connect` |
| `2026-07-22 18:01:35` | `cowrie.client.version` |
| `2026-07-22 18:01:35` | `cowrie.client.kex` |
| `2026-07-22 18:01:35` | `cowrie.login.success` |
| `2026-07-22 18:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269347d1c32e

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-07-22 18:01 |
| **Last Seen** | 2026-07-22 18:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:01:41` | `cowrie.session.connect` |
| `2026-07-22 18:01:41` | `cowrie.client.version` |
| `2026-07-22 18:01:41` | `cowrie.client.kex` |
| `2026-07-22 18:01:42` | `cowrie.login.success` |
| `2026-07-22 18:01:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919744bd9142

| Field | Detail |
|---|---|
| **Source IP** | `91.241.150[.]246` |
| **First Seen** | 2026-07-22 18:06 |
| **Last Seen** | 2026-07-22 18:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:06:36` | `cowrie.session.connect` |
| `2026-07-22 18:06:37` | `cowrie.client.version` |
| `2026-07-22 18:06:37` | `cowrie.client.kex` |
| `2026-07-22 18:06:38` | `cowrie.login.success` |
| `2026-07-22 18:06:39` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.241.150[.]246` to AbuseIPDB if not already reported
- [ ] Block `91.241.150[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536cce47ccff

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 18:06 |
| **Last Seen** | 2026-07-22 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:06:41` | `cowrie.session.connect` |
| `2026-07-22 18:06:41` | `cowrie.client.version` |
| `2026-07-22 18:06:41` | `cowrie.client.kex` |
| `2026-07-22 18:06:41` | `cowrie.login.success` |
| `2026-07-22 18:06:42` | `cowrie.session.params` |
| `2026-07-22 18:06:42` | `cowrie.command.input` |
| `2026-07-22 18:06:42` | `cowrie.log.closed` |
| `2026-07-22 18:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23dd00142fa

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-07-22 18:13 |
| **Last Seen** | 2026-07-22 18:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:13:38` | `cowrie.session.connect` |
| `2026-07-22 18:13:39` | `cowrie.client.version` |
| `2026-07-22 18:13:39` | `cowrie.client.kex` |
| `2026-07-22 18:13:40` | `cowrie.login.success` |
| `2026-07-22 18:13:40` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-291041427d68

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 18:14 |
| **Last Seen** | 2026-07-22 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:14:04` | `cowrie.session.connect` |
| `2026-07-22 18:14:04` | `cowrie.client.version` |
| `2026-07-22 18:14:05` | `cowrie.client.kex` |
| `2026-07-22 18:14:05` | `cowrie.login.success` |
| `2026-07-22 18:14:06` | `cowrie.session.params` |
| `2026-07-22 18:14:06` | `cowrie.command.input` |
| `2026-07-22 18:14:06` | `cowrie.log.closed` |
| `2026-07-22 18:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b03ff3c4bdf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:14 |
| **Last Seen** | 2026-07-22 18:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:14:07` | `cowrie.session.connect` |
| `2026-07-22 18:14:07` | `cowrie.client.version` |
| `2026-07-22 18:14:07` | `cowrie.client.kex` |
| `2026-07-22 18:14:10` | `cowrie.login.success` |
| `2026-07-22 18:14:12` | `cowrie.session.params` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.success` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:12` | `cowrie.command.input` |
| `2026-07-22 18:14:13` | `cowrie.log.closed` |
| `2026-07-22 18:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5161211e762d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:16 |
| **Last Seen** | 2026-07-22 18:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:16:13` | `cowrie.session.connect` |
| `2026-07-22 18:16:13` | `cowrie.client.version` |
| `2026-07-22 18:16:13` | `cowrie.client.kex` |
| `2026-07-22 18:16:16` | `cowrie.login.success` |
| `2026-07-22 18:16:17` | `cowrie.session.params` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.success` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:17` | `cowrie.command.input` |
| `2026-07-22 18:16:18` | `cowrie.log.closed` |
| `2026-07-22 18:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2839e2925bab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:18 |
| **Last Seen** | 2026-07-22 18:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:18:17` | `cowrie.session.connect` |
| `2026-07-22 18:18:17` | `cowrie.client.version` |
| `2026-07-22 18:18:17` | `cowrie.client.kex` |
| `2026-07-22 18:18:20` | `cowrie.login.success` |
| `2026-07-22 18:18:22` | `cowrie.session.params` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.success` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:22` | `cowrie.command.input` |
| `2026-07-22 18:18:23` | `cowrie.log.closed` |
| `2026-07-22 18:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a309ba2d017

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:20 |
| **Last Seen** | 2026-07-22 18:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:20:18` | `cowrie.session.connect` |
| `2026-07-22 18:20:18` | `cowrie.client.version` |
| `2026-07-22 18:20:18` | `cowrie.client.kex` |
| `2026-07-22 18:20:21` | `cowrie.login.success` |
| `2026-07-22 18:20:22` | `cowrie.session.params` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.success` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:22` | `cowrie.command.input` |
| `2026-07-22 18:20:23` | `cowrie.log.closed` |
| `2026-07-22 18:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3620d185b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:22 |
| **Last Seen** | 2026-07-22 18:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:22:18` | `cowrie.session.connect` |
| `2026-07-22 18:22:19` | `cowrie.client.version` |
| `2026-07-22 18:22:19` | `cowrie.client.kex` |
| `2026-07-22 18:22:21` | `cowrie.login.success` |
| `2026-07-22 18:22:23` | `cowrie.session.params` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.success` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.command.input` |
| `2026-07-22 18:22:23` | `cowrie.log.closed` |
| `2026-07-22 18:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597696c5f8df

| Field | Detail |
|---|---|
| **Source IP** | `8.217.235[.]231` |
| **First Seen** | 2026-07-22 18:23 |
| **Last Seen** | 2026-07-22 18:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:23:19` | `cowrie.session.connect` |
| `2026-07-22 18:23:19` | `cowrie.client.version` |
| `2026-07-22 18:23:19` | `cowrie.client.kex` |
| `2026-07-22 18:23:20` | `cowrie.login.success` |
| `2026-07-22 18:23:21` | `cowrie.session.params` |
| `2026-07-22 18:23:21` | `cowrie.command.input` |
| `2026-07-22 18:23:21` | `cowrie.command.failed` |
| `2026-07-22 18:23:22` | `cowrie.log.closed` |
| `2026-07-22 18:23:22` | `cowrie.session.params` |
| `2026-07-22 18:23:22` | `cowrie.command.input` |
| `2026-07-22 18:23:22` | `cowrie.session.file_download` |
| `2026-07-22 18:23:22` | `cowrie.log.closed` |
| `2026-07-22 18:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.235[.]231` to AbuseIPDB if not already reported
- [ ] Block `8.217.235[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91c2d0d4fe5

| Field | Detail |
|---|---|
| **Source IP** | `8.217.235[.]231` |
| **First Seen** | 2026-07-22 18:23 |
| **Last Seen** | 2026-07-22 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:23:23` | `cowrie.session.connect` |
| `2026-07-22 18:23:23` | `cowrie.client.version` |
| `2026-07-22 18:23:23` | `cowrie.client.kex` |
| `2026-07-22 18:23:24` | `cowrie.login.success` |
| `2026-07-22 18:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.235[.]231` to AbuseIPDB if not already reported
- [ ] Block `8.217.235[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89262a95d40

| Field | Detail |
|---|---|
| **Source IP** | `8.217.235[.]231` |
| **First Seen** | 2026-07-22 18:23 |
| **Last Seen** | 2026-07-22 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:23:24` | `cowrie.session.connect` |
| `2026-07-22 18:23:24` | `cowrie.client.version` |
| `2026-07-22 18:23:24` | `cowrie.client.kex` |
| `2026-07-22 18:23:25` | `cowrie.login.success` |
| `2026-07-22 18:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.235[.]231` to AbuseIPDB if not already reported
- [ ] Block `8.217.235[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba99489f8c32

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:24 |
| **Last Seen** | 2026-07-22 18:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:24:14` | `cowrie.session.connect` |
| `2026-07-22 18:24:14` | `cowrie.client.version` |
| `2026-07-22 18:24:14` | `cowrie.client.kex` |
| `2026-07-22 18:24:16` | `cowrie.login.success` |
| `2026-07-22 18:24:18` | `cowrie.session.params` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.success` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.command.input` |
| `2026-07-22 18:24:18` | `cowrie.log.closed` |
| `2026-07-22 18:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4bfcc91765

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 18:25 |
| **Last Seen** | 2026-07-22 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:25:27` | `cowrie.session.connect` |
| `2026-07-22 18:25:27` | `cowrie.client.version` |
| `2026-07-22 18:25:27` | `cowrie.client.kex` |
| `2026-07-22 18:25:27` | `cowrie.login.success` |
| `2026-07-22 18:25:27` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:25:28` | `cowrie.direct-tcpip.data` |
| `2026-07-22 18:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ab6f377d7b

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-07-22 18:25 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:25:55` | `cowrie.session.connect` |
| `2026-07-22 18:25:55` | `cowrie.client.version` |
| `2026-07-22 18:25:55` | `cowrie.client.kex` |
| `2026-07-22 18:25:56` | `cowrie.login.success` |
| `2026-07-22 18:25:57` | `cowrie.session.params` |
| `2026-07-22 18:25:57` | `cowrie.command.input` |
| `2026-07-22 18:25:57` | `cowrie.command.failed` |
| `2026-07-22 18:25:58` | `cowrie.log.closed` |
| `2026-07-22 18:25:59` | `cowrie.session.params` |
| `2026-07-22 18:25:59` | `cowrie.command.input` |
| `2026-07-22 18:25:59` | `cowrie.session.file_download` |
| `2026-07-22 18:25:59` | `cowrie.log.closed` |
| `2026-07-22 18:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-887101828ce2

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-07-22 18:25 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:25:59` | `cowrie.session.connect` |
| `2026-07-22 18:25:59` | `cowrie.client.version` |
| `2026-07-22 18:25:59` | `cowrie.client.kex` |
| `2026-07-22 18:26:01` | `cowrie.login.success` |
| `2026-07-22 18:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2354db79865

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-07-22 18:26 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:26:01` | `cowrie.session.connect` |
| `2026-07-22 18:26:01` | `cowrie.client.version` |
| `2026-07-22 18:26:02` | `cowrie.client.kex` |
| `2026-07-22 18:26:03` | `cowrie.login.success` |
| `2026-07-22 18:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ddc8cb6dd5

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-22 18:26 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:26:13` | `cowrie.session.connect` |
| `2026-07-22 18:26:14` | `cowrie.client.version` |
| `2026-07-22 18:26:14` | `cowrie.client.kex` |
| `2026-07-22 18:26:16` | `cowrie.login.success` |
| `2026-07-22 18:26:17` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042b39d82b7b

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-07-22 18:26 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:26:27` | `cowrie.session.connect` |
| `2026-07-22 18:26:27` | `cowrie.client.version` |
| `2026-07-22 18:26:27` | `cowrie.client.kex` |
| `2026-07-22 18:26:29` | `cowrie.login.success` |
| `2026-07-22 18:26:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ebd5af3c0c0

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-22 18:26 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:26:28` | `cowrie.session.connect` |
| `2026-07-22 18:26:28` | `cowrie.client.version` |
| `2026-07-22 18:26:28` | `cowrie.client.kex` |
| `2026-07-22 18:26:29` | `cowrie.login.success` |
| `2026-07-22 18:26:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ff681e57ee

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-22 18:26 |
| **Last Seen** | 2026-07-22 18:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:26:35` | `cowrie.session.connect` |
| `2026-07-22 18:26:35` | `cowrie.client.version` |
| `2026-07-22 18:26:35` | `cowrie.client.kex` |
| `2026-07-22 18:26:37` | `cowrie.login.success` |
| `2026-07-22 18:26:38` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d112c725dd0d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:27 |
| **Last Seen** | 2026-07-22 18:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:27:54` | `cowrie.session.connect` |
| `2026-07-22 18:27:54` | `cowrie.client.version` |
| `2026-07-22 18:27:54` | `cowrie.client.kex` |
| `2026-07-22 18:27:56` | `cowrie.login.success` |
| `2026-07-22 18:27:57` | `cowrie.session.params` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.success` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:57` | `cowrie.command.input` |
| `2026-07-22 18:27:58` | `cowrie.log.closed` |
| `2026-07-22 18:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e440e107f11

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-07-22 18:29 |
| **Last Seen** | 2026-07-22 18:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:29:29` | `cowrie.session.connect` |
| `2026-07-22 18:29:29` | `cowrie.client.version` |
| `2026-07-22 18:29:29` | `cowrie.client.kex` |
| `2026-07-22 18:29:30` | `cowrie.login.success` |
| `2026-07-22 18:29:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98053bb278fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:29 |
| **Last Seen** | 2026-07-22 18:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:29:39` | `cowrie.session.connect` |
| `2026-07-22 18:29:39` | `cowrie.client.version` |
| `2026-07-22 18:29:39` | `cowrie.client.kex` |
| `2026-07-22 18:29:41` | `cowrie.login.success` |
| `2026-07-22 18:29:43` | `cowrie.session.params` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.success` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.command.input` |
| `2026-07-22 18:29:43` | `cowrie.log.closed` |
| `2026-07-22 18:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa50bf4c021

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:31 |
| **Last Seen** | 2026-07-22 18:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:31:26` | `cowrie.session.connect` |
| `2026-07-22 18:31:27` | `cowrie.client.version` |
| `2026-07-22 18:31:27` | `cowrie.client.kex` |
| `2026-07-22 18:31:28` | `cowrie.login.success` |
| `2026-07-22 18:31:30` | `cowrie.session.params` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.success` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.command.input` |
| `2026-07-22 18:31:30` | `cowrie.log.closed` |
| `2026-07-22 18:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0310fd8c3011

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:33 |
| **Last Seen** | 2026-07-22 18:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:33:17` | `cowrie.session.connect` |
| `2026-07-22 18:33:17` | `cowrie.client.version` |
| `2026-07-22 18:33:17` | `cowrie.client.kex` |
| `2026-07-22 18:33:19` | `cowrie.login.success` |
| `2026-07-22 18:33:21` | `cowrie.session.params` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.success` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.command.input` |
| `2026-07-22 18:33:21` | `cowrie.log.closed` |
| `2026-07-22 18:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc33980afe68

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:35 |
| **Last Seen** | 2026-07-22 18:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:35:07` | `cowrie.session.connect` |
| `2026-07-22 18:35:07` | `cowrie.client.version` |
| `2026-07-22 18:35:07` | `cowrie.client.kex` |
| `2026-07-22 18:35:09` | `cowrie.login.success` |
| `2026-07-22 18:35:10` | `cowrie.session.params` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.success` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:10` | `cowrie.command.input` |
| `2026-07-22 18:35:11` | `cowrie.log.closed` |
| `2026-07-22 18:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd7ac4d59e6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:36 |
| **Last Seen** | 2026-07-22 18:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:36:57` | `cowrie.session.connect` |
| `2026-07-22 18:36:57` | `cowrie.client.version` |
| `2026-07-22 18:36:57` | `cowrie.client.kex` |
| `2026-07-22 18:36:59` | `cowrie.login.success` |
| `2026-07-22 18:37:00` | `cowrie.session.params` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.success` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:00` | `cowrie.command.input` |
| `2026-07-22 18:37:01` | `cowrie.log.closed` |
| `2026-07-22 18:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c342f4a5cbf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:38 |
| **Last Seen** | 2026-07-22 18:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:38:47` | `cowrie.session.connect` |
| `2026-07-22 18:38:47` | `cowrie.client.version` |
| `2026-07-22 18:38:47` | `cowrie.client.kex` |
| `2026-07-22 18:38:49` | `cowrie.login.success` |
| `2026-07-22 18:38:50` | `cowrie.session.params` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.success` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:50` | `cowrie.command.input` |
| `2026-07-22 18:38:51` | `cowrie.log.closed` |
| `2026-07-22 18:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4712f6ead875

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-22 18:38 |
| **Last Seen** | 2026-07-22 18:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:38:54` | `cowrie.session.connect` |
| `2026-07-22 18:38:55` | `cowrie.client.version` |
| `2026-07-22 18:38:55` | `cowrie.client.kex` |
| `2026-07-22 18:38:56` | `cowrie.login.success` |
| `2026-07-22 18:38:56` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ffd7d9c1f5

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-22 18:39 |
| **Last Seen** | 2026-07-22 18:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:39:01` | `cowrie.session.connect` |
| `2026-07-22 18:39:01` | `cowrie.client.version` |
| `2026-07-22 18:39:01` | `cowrie.client.kex` |
| `2026-07-22 18:39:02` | `cowrie.login.success` |
| `2026-07-22 18:39:03` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef30610cf065

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:40 |
| **Last Seen** | 2026-07-22 18:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:40:38` | `cowrie.session.connect` |
| `2026-07-22 18:40:38` | `cowrie.client.version` |
| `2026-07-22 18:40:38` | `cowrie.client.kex` |
| `2026-07-22 18:40:40` | `cowrie.login.success` |
| `2026-07-22 18:40:41` | `cowrie.session.params` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.success` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:41` | `cowrie.command.input` |
| `2026-07-22 18:40:42` | `cowrie.log.closed` |
| `2026-07-22 18:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db015088370

| Field | Detail |
|---|---|
| **Source IP** | `59.48.39[.]222` |
| **First Seen** | 2026-07-22 18:41 |
| **Last Seen** | 2026-07-22 18:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:41:42` | `cowrie.session.connect` |
| `2026-07-22 18:41:44` | `cowrie.client.version` |
| `2026-07-22 18:41:44` | `cowrie.client.kex` |
| `2026-07-22 18:41:45` | `cowrie.login.success` |
| `2026-07-22 18:41:46` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.39[.]222` to AbuseIPDB if not already reported
- [ ] Block `59.48.39[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd2e3373dc6

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-07-22 18:42 |
| **Last Seen** | 2026-07-22 18:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:42:10` | `cowrie.session.connect` |
| `2026-07-22 18:42:12` | `cowrie.client.version` |
| `2026-07-22 18:42:12` | `cowrie.client.kex` |
| `2026-07-22 18:42:16` | `cowrie.login.success` |
| `2026-07-22 18:42:18` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1cf55b7406

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:42 |
| **Last Seen** | 2026-07-22 18:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:42:25` | `cowrie.session.connect` |
| `2026-07-22 18:42:25` | `cowrie.client.version` |
| `2026-07-22 18:42:25` | `cowrie.client.kex` |
| `2026-07-22 18:42:27` | `cowrie.login.success` |
| `2026-07-22 18:42:29` | `cowrie.session.params` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.success` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.command.input` |
| `2026-07-22 18:42:29` | `cowrie.log.closed` |
| `2026-07-22 18:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d331d4c09f7a

| Field | Detail |
|---|---|
| **Source IP** | `49.124.150[.]250` |
| **First Seen** | 2026-07-22 18:42 |
| **Last Seen** | 2026-07-22 18:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:42:29` | `cowrie.session.connect` |
| `2026-07-22 18:42:29` | `cowrie.client.version` |
| `2026-07-22 18:42:29` | `cowrie.client.kex` |
| `2026-07-22 18:42:32` | `cowrie.login.success` |
| `2026-07-22 18:42:33` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `49.124.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b6a4cf0bc8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:44 |
| **Last Seen** | 2026-07-22 18:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:44:16` | `cowrie.session.connect` |
| `2026-07-22 18:44:16` | `cowrie.client.version` |
| `2026-07-22 18:44:16` | `cowrie.client.kex` |
| `2026-07-22 18:44:18` | `cowrie.login.success` |
| `2026-07-22 18:44:19` | `cowrie.session.params` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.success` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:19` | `cowrie.command.input` |
| `2026-07-22 18:44:20` | `cowrie.log.closed` |
| `2026-07-22 18:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5c31d58254

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:46 |
| **Last Seen** | 2026-07-22 18:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:46:02` | `cowrie.session.connect` |
| `2026-07-22 18:46:02` | `cowrie.client.version` |
| `2026-07-22 18:46:02` | `cowrie.client.kex` |
| `2026-07-22 18:46:04` | `cowrie.login.success` |
| `2026-07-22 18:46:05` | `cowrie.session.params` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.success` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:05` | `cowrie.command.input` |
| `2026-07-22 18:46:06` | `cowrie.log.closed` |
| `2026-07-22 18:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb2326af307

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:47 |
| **Last Seen** | 2026-07-22 18:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:47:48` | `cowrie.session.connect` |
| `2026-07-22 18:47:49` | `cowrie.client.version` |
| `2026-07-22 18:47:49` | `cowrie.client.kex` |
| `2026-07-22 18:47:50` | `cowrie.login.success` |
| `2026-07-22 18:47:52` | `cowrie.session.params` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.success` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:52` | `cowrie.command.input` |
| `2026-07-22 18:47:53` | `cowrie.log.closed` |
| `2026-07-22 18:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37e888d1295

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:49 |
| **Last Seen** | 2026-07-22 18:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:49:37` | `cowrie.session.connect` |
| `2026-07-22 18:49:37` | `cowrie.client.version` |
| `2026-07-22 18:49:37` | `cowrie.client.kex` |
| `2026-07-22 18:49:38` | `cowrie.login.success` |
| `2026-07-22 18:49:40` | `cowrie.session.params` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.success` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.command.input` |
| `2026-07-22 18:49:40` | `cowrie.log.closed` |
| `2026-07-22 18:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94ea2a13f5f

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-07-22 18:50 |
| **Last Seen** | 2026-07-22 18:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:50:50` | `cowrie.session.connect` |
| `2026-07-22 18:50:51` | `cowrie.client.version` |
| `2026-07-22 18:50:51` | `cowrie.client.kex` |
| `2026-07-22 18:50:53` | `cowrie.login.success` |
| `2026-07-22 18:50:54` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a33c08e38c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:51 |
| **Last Seen** | 2026-07-22 18:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:51:30` | `cowrie.session.connect` |
| `2026-07-22 18:51:30` | `cowrie.client.version` |
| `2026-07-22 18:51:30` | `cowrie.client.kex` |
| `2026-07-22 18:51:31` | `cowrie.login.success` |
| `2026-07-22 18:51:32` | `cowrie.session.params` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.success` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.command.input` |
| `2026-07-22 18:51:32` | `cowrie.log.closed` |
| `2026-07-22 18:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ad435adf74

| Field | Detail |
|---|---|
| **Source IP** | `95.165.142[.]8` |
| **First Seen** | 2026-07-22 18:52 |
| **Last Seen** | 2026-07-22 18:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:52:41` | `cowrie.session.connect` |
| `2026-07-22 18:52:41` | `cowrie.client.version` |
| `2026-07-22 18:52:41` | `cowrie.client.kex` |
| `2026-07-22 18:52:42` | `cowrie.login.success` |
| `2026-07-22 18:52:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 18:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.142[.]8` to AbuseIPDB if not already reported
- [ ] Block `95.165.142[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b62e46ac2d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:53 |
| **Last Seen** | 2026-07-22 18:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:53:23` | `cowrie.session.connect` |
| `2026-07-22 18:53:23` | `cowrie.client.version` |
| `2026-07-22 18:53:23` | `cowrie.client.kex` |
| `2026-07-22 18:53:24` | `cowrie.login.success` |
| `2026-07-22 18:53:26` | `cowrie.session.params` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.success` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.command.input` |
| `2026-07-22 18:53:26` | `cowrie.log.closed` |
| `2026-07-22 18:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-22 17:10 | 2026-07-22 18:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-22 16:58 | 2026-07-22 16:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.180.246[.]242` | **2** | 2026-07-22 17:41 | 2026-07-22 17:44 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-07-22 17:08 | 2026-07-22 17:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-07-22 18:04 | 2026-07-22 18:26 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-07-22 18:19 | 2026-07-22 18:20 | 53s | 0 | `T1592` | 🟢 LOW |
| `113.161.32[.]14` | 1 | 2026-07-22 18:03 | 2026-07-22 18:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `190.12.109[.]162` | 1 | 2026-07-22 17:02 | 2026-07-22 17:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `200.105.141[.]172` | 1 | 2026-07-22 17:49 | 2026-07-22 17:49 | 5s | 0 | `T1592` | 🟢 LOW |
| `36.137.38[.]119` | 1 | 2026-07-22 18:13 | 2026-07-22 18:14 | 7s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-22 17:56 | 2026-07-22 17:56 | 7s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-22 17:53 | 2026-07-22 17:55 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 49/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |

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
| `210.206.24[.]237` | KR | LG Uplus | **100** ⚠️ | 4 |
| `51.116.117[.]203` | DE | Microsoft Limited | **100** ⚠️ | 22 |
| `117.250.19[.]91` | IN | L malini devi high garden resort kailashpuri udaipur | **100** ⚠️ | 37 |
| `36.137.38[.]119` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `196.190.41[.]137` | ET | REFUGEE_COUNCIL | **100** ⚠️ | 50 |
| `36.154.134[.]146` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `95.165.142[.]8` | RU | Moscow Local Telephone Network (PJSC MGTS) | **100** ⚠️ | 50 |
| `103.67.152[.]201` | IN | Netfirre Communications Pvt Ltd | **100** ⚠️ | 50 |
| `59.48.39[.]222` | CN | CHINANET Shanxi province network | **100** ⚠️ | 50 |
| `96.1.40[.]151` | CA | TELUS Mobility-Ontario | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 107 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 94 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 38 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 36 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 36 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 127 cases |
| Tool 34  | Credential Extractor        | ✅ 126 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 69 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 12 recon entry/entries in table (5 group(s) consolidating 14 session(s)).

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
_Report time: 2026-07-22T19:27:19Z_

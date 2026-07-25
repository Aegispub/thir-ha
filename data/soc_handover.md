# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-25 |
| **Generated At** | 2026-07-25T15:08:02Z |
| **Shift Time** | 15:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **118** |
| Confirmed Threats | **108** |
| False Positives Filtered | **10** (8.5%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **26** |
| High Severity Cases | **57** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **81** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **17** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **59** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `support` | 18 |
| `unknown` | 6 |
| `mysql` | 6 |
| `default` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 18 |
| `root66` | 5 |
| `77` | 5 |
| `66` | 5 |
| `666666` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 18 |
| `root` | `root66` | 5 |
| `default` | `77` | 5 |
| `unknown` | `66` | 5 |
| `config` | `666666` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `5` | `65.20.202.4` | 2026-07-25T13:02:28 |
| `root` | `root66` | `180.76.52.146` | 2026-07-25T13:09:34 |
| `root` | `root66` | `46.77.69.201` | 2026-07-25T13:09:42 |
| `ubuntu` | `1qaz2wsx` | `10.0.0.73` | 2026-07-25T13:11:43 |
| `root` | `root66` | `81.22.51.64` | 2026-07-25T13:13:02 |
| `root` | `root66` | `10.0.0.73` | 2026-07-25T13:13:27 |
| `support` | `support` | `176.53.159.196` | 2026-07-25T13:13:53 |
| `support` | `support` | `10.0.0.73` | 2026-07-25T13:14:09 |
| `Nobody` | `P@ssword` | `183.104.220.84` | 2026-07-25T13:23:50 |
| `Nobody` | `P@ssword` | `122.187.234.54` | 2026-07-25T13:27:10 |
| `config` | `666666` | `185.112.148.66` | 2026-07-25T13:32:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `156.225.1.44` | 2026-07-25T13:33:55 |
| `config` | `666666` | `222.76.248.54` | 2026-07-25T13:35:53 |
| `config` | `666666` | `10.0.0.73` | 2026-07-25T13:36:18 |
| `blank` | `7777` | `122.187.230.183` | 2026-07-25T13:37:43 |
| `blank` | `7777` | `112.26.101.76` | 2026-07-25T13:37:58 |
| `blank` | `7777` | `10.0.0.73` | 2026-07-25T13:38:06 |
| `root` | `---fuck_you----` | `120.26.200.188` | 2026-07-25T13:42:03 |
| `user` | `33` | `118.91.176.243` | 2026-07-25T13:48:32 |
| `user` | `33` | `10.0.0.73` | 2026-07-25T13:52:14 |
| `operator` | `operator2005` | `187.115.144.103` | 2026-07-25T13:57:23 |
| `default` | `77` | `61.145.181.7` | 2026-07-25T13:59:10 |
| `default` | `77` | `41.220.3.101` | 2026-07-25T13:59:18 |
| `operator` | `operator2005` | `10.0.0.73` | 2026-07-25T14:01:08 |
| `default` | `77` | `65.20.202.4` | 2026-07-25T14:02:33 |
| `default` | `77` | `10.0.0.73` | 2026-07-25T14:02:58 |
| `root` | `Qwe123asd` | `223.197.186.7` | 2026-07-25T14:05:35 |
| `345gs5662d34` | `345gs5662d34` | `223.197.186.7` | 2026-07-25T14:05:39 |
| `root` | `3245gs5662d34` | `223.197.186.7` | 2026-07-25T14:05:40 |
| `test` | `222222` | `196.190.180.18` | 2026-07-25T14:13:12 |
| `root` | `adidas` | `120.52.92.8` | 2026-07-25T14:16:22 |
| `test` | `222222` | `10.0.0.73` | 2026-07-25T14:17:07 |
| `mysql` | `raspberry` | `101.13.1.58` | 2026-07-25T14:22:10 |
| `mysql` | `raspberry` | `31.173.2.182` | 2026-07-25T14:22:22 |
| `unknown` | `66` | `183.6.118.248` | 2026-07-25T14:24:03 |
| `root` | `1234567890` | `193.32.162.42` | 2026-07-25T14:24:55 |
| `mysql` | `raspberry` | `111.70.29.158` | 2026-07-25T14:25:23 |
| `mysql` | `raspberry` | `110.136.122.230` | 2026-07-25T14:25:33 |
| `unknown` | `66` | `196.188.93.169` | 2026-07-25T14:27:11 |
| `unknown` | `66` | `24.207.66.154` | 2026-07-25T14:27:18 |
| `root` | `password1` | `193.32.162.42` | 2026-07-25T14:27:22 |
| `unknown` | `66` | `10.0.0.73` | 2026-07-25T14:27:36 |
| `root` | `admin123` | `193.32.162.42` | 2026-07-25T14:28:47 |
| `root` | `1234` | `193.32.162.42` | 2026-07-25T14:30:20 |
| `root` | `123` | `193.32.162.42` | 2026-07-25T14:31:56 |
| `root` | `qwerty123` | `193.32.162.42` | 2026-07-25T14:33:31 |
| `root` | `1q2w3e4r` | `193.32.162.42` | 2026-07-25T14:34:46 |
| `root` | `pass123` | `193.32.162.42` | 2026-07-25T14:36:01 |
| `root` | `123abc` | `193.32.162.42` | 2026-07-25T14:37:15 |
| `admin` | `1234567890` | `193.32.162.42` | 2026-07-25T14:38:27 |
| `admin` | `password1` | `193.32.162.42` | 2026-07-25T14:39:41 |
| `admin` | `admin123` | `193.32.162.42` | 2026-07-25T14:40:56 |
| `debian` | `0` | `223.25.108.2` | 2026-07-25T14:41:37 |
| `admin` | `1234` | `193.32.162.42` | 2026-07-25T14:42:11 |
| `mal` | `mal` | `85.206.68.80` | 2026-07-25T14:44:39 |
| `345gs5662d34` | `345gs5662d34` | `85.206.68.80` | 2026-07-25T14:44:42 |
| `mal` | `3245gs5662d34` | `85.206.68.80` | 2026-07-25T14:44:43 |
| `mysql` | `admin123` | `197.242.170.10` | 2026-07-25T14:52:08 |
| `mysql` | `admin123` | `10.0.0.73` | 2026-07-25T14:52:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **118** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 28 |
| OpenSSH | 26 |
| libssh | 19 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 26 | 25 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |
| `f555226df196...` | Mirai/variant | 7 | 3 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 26 | 25 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 7 | 3 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 14 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `193.32.162.42`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `223.197.186.7`, `85.206.68.80`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **45** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (57)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a25685941ce

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-25 13:02 |
| **Last Seen** | 2026-07-25 13:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:02:26` | `cowrie.session.connect` |
| `2026-07-25 13:02:27` | `cowrie.client.version` |
| `2026-07-25 13:02:27` | `cowrie.client.kex` |
| `2026-07-25 13:02:28` | `cowrie.login.success` |
| `2026-07-25 13:02:28` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36d1ec645a6

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-07-25 13:09 |
| **Last Seen** | 2026-07-25 13:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:09:30` | `cowrie.session.connect` |
| `2026-07-25 13:09:31` | `cowrie.client.version` |
| `2026-07-25 13:09:31` | `cowrie.client.kex` |
| `2026-07-25 13:09:34` | `cowrie.login.success` |
| `2026-07-25 13:09:35` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609ce037062b

| Field | Detail |
|---|---|
| **Source IP** | `46.77.69[.]201` |
| **First Seen** | 2026-07-25 13:09 |
| **Last Seen** | 2026-07-25 13:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:09:40` | `cowrie.session.connect` |
| `2026-07-25 13:09:40` | `cowrie.client.version` |
| `2026-07-25 13:09:40` | `cowrie.client.kex` |
| `2026-07-25 13:09:42` | `cowrie.login.success` |
| `2026-07-25 13:09:42` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.77.69[.]201` to AbuseIPDB if not already reported
- [ ] Block `46.77.69[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403ce2855514

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-07-25 13:13 |
| **Last Seen** | 2026-07-25 13:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:13:00` | `cowrie.session.connect` |
| `2026-07-25 13:13:01` | `cowrie.client.version` |
| `2026-07-25 13:13:01` | `cowrie.client.kex` |
| `2026-07-25 13:13:02` | `cowrie.login.success` |
| `2026-07-25 13:13:02` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109b7a3a990f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 13:13 |
| **Last Seen** | 2026-07-25 13:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:13:53` | `cowrie.session.connect` |
| `2026-07-25 13:13:53` | `cowrie.client.version` |
| `2026-07-25 13:13:53` | `cowrie.client.kex` |
| `2026-07-25 13:13:53` | `cowrie.login.success` |
| `2026-07-25 13:13:53` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:13:54` | `cowrie.direct-tcpip.data` |
| `2026-07-25 13:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42c1f9274a8

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-07-25 13:23 |
| **Last Seen** | 2026-07-25 13:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:23:47` | `cowrie.session.connect` |
| `2026-07-25 13:23:48` | `cowrie.client.version` |
| `2026-07-25 13:23:48` | `cowrie.client.kex` |
| `2026-07-25 13:23:50` | `cowrie.login.success` |
| `2026-07-25 13:23:50` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fc2ac0e5c1

| Field | Detail |
|---|---|
| **Source IP** | `122.187.234[.]54` |
| **First Seen** | 2026-07-25 13:27 |
| **Last Seen** | 2026-07-25 13:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:27:07` | `cowrie.session.connect` |
| `2026-07-25 13:27:08` | `cowrie.client.version` |
| `2026-07-25 13:27:08` | `cowrie.client.kex` |
| `2026-07-25 13:27:10` | `cowrie.login.success` |
| `2026-07-25 13:27:11` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.234[.]54` to AbuseIPDB if not already reported
- [ ] Block `122.187.234[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac43e8be1dc

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-25 13:32 |
| **Last Seen** | 2026-07-25 13:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:32:33` | `cowrie.session.connect` |
| `2026-07-25 13:32:33` | `cowrie.client.version` |
| `2026-07-25 13:32:33` | `cowrie.client.kex` |
| `2026-07-25 13:32:35` | `cowrie.login.success` |
| `2026-07-25 13:32:36` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82c3d449e87

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 13:33 |
| **Last Seen** | 2026-07-25 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:33:28` | `cowrie.session.connect` |
| `2026-07-25 13:33:28` | `cowrie.client.version` |
| `2026-07-25 13:33:28` | `cowrie.client.kex` |
| `2026-07-25 13:33:28` | `cowrie.login.success` |
| `2026-07-25 13:33:28` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:33:28` | `cowrie.direct-tcpip.data` |
| `2026-07-25 13:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d341b066048

| Field | Detail |
|---|---|
| **Source IP** | `156.225.1[.]44` |
| **First Seen** | 2026-07-25 13:33 |
| **Last Seen** | 2026-07-25 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:33:55` | `cowrie.session.connect` |
| `2026-07-25 13:33:55` | `cowrie.login.success` |
| `2026-07-25 13:33:56` | `cowrie.session.params` |
| `2026-07-25 13:33:56` | `cowrie.command.input` |
| `2026-07-25 13:33:56` | `cowrie.command.failed` |
| `2026-07-25 13:33:56` | `cowrie.command.input` |
| `2026-07-25 13:33:56` | `cowrie.log.closed` |
| `2026-07-25 13:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.1[.]44` to AbuseIPDB if not already reported
- [ ] Block `156.225.1[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbab11fc776e

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-07-25 13:35 |
| **Last Seen** | 2026-07-25 13:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:35:49` | `cowrie.session.connect` |
| `2026-07-25 13:35:50` | `cowrie.client.version` |
| `2026-07-25 13:35:50` | `cowrie.client.kex` |
| `2026-07-25 13:35:53` | `cowrie.login.success` |
| `2026-07-25 13:35:54` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdade96b3d8d

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]183` |
| **First Seen** | 2026-07-25 13:37 |
| **Last Seen** | 2026-07-25 13:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:37:40` | `cowrie.session.connect` |
| `2026-07-25 13:37:41` | `cowrie.client.version` |
| `2026-07-25 13:37:41` | `cowrie.client.kex` |
| `2026-07-25 13:37:43` | `cowrie.login.success` |
| `2026-07-25 13:37:44` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]183` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98476b3b39b

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-25 13:37 |
| **Last Seen** | 2026-07-25 13:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:37:54` | `cowrie.session.connect` |
| `2026-07-25 13:37:55` | `cowrie.client.version` |
| `2026-07-25 13:37:55` | `cowrie.client.kex` |
| `2026-07-25 13:37:58` | `cowrie.login.success` |
| `2026-07-25 13:38:00` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df186b5265ae

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 13:40 |
| **Last Seen** | 2026-07-25 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:40:30` | `cowrie.session.connect` |
| `2026-07-25 13:40:30` | `cowrie.client.version` |
| `2026-07-25 13:40:30` | `cowrie.client.kex` |
| `2026-07-25 13:40:31` | `cowrie.login.success` |
| `2026-07-25 13:40:31` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:40:31` | `cowrie.direct-tcpip.data` |
| `2026-07-25 13:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b90b8971070

| Field | Detail |
|---|---|
| **Source IP** | `120.26.200[.]188` |
| **First Seen** | 2026-07-25 13:41 |
| **Last Seen** | 2026-07-25 13:42 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:41:55` | `cowrie.session.connect` |
| `2026-07-25 13:41:57` | `cowrie.client.version` |
| `2026-07-25 13:41:57` | `cowrie.client.kex` |
| `2026-07-25 13:42:03` | `cowrie.login.success` |
| `2026-07-25 13:42:07` | `cowrie.session.params` |
| `2026-07-25 13:42:07` | `cowrie.command.input` |
| `2026-07-25 13:42:09` | `cowrie.log.closed` |
| `2026-07-25 13:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.200[.]188` to AbuseIPDB if not already reported
- [ ] Block `120.26.200[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66b2102b595

| Field | Detail |
|---|---|
| **Source IP** | `118.91.176[.]243` |
| **First Seen** | 2026-07-25 13:48 |
| **Last Seen** | 2026-07-25 13:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:48:29` | `cowrie.session.connect` |
| `2026-07-25 13:48:30` | `cowrie.client.version` |
| `2026-07-25 13:48:30` | `cowrie.client.kex` |
| `2026-07-25 13:48:32` | `cowrie.login.success` |
| `2026-07-25 13:48:32` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.91.176[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.91.176[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b948268f81f

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-25 13:57 |
| **Last Seen** | 2026-07-25 13:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:57:21` | `cowrie.session.connect` |
| `2026-07-25 13:57:21` | `cowrie.client.version` |
| `2026-07-25 13:57:21` | `cowrie.client.kex` |
| `2026-07-25 13:57:23` | `cowrie.login.success` |
| `2026-07-25 13:57:24` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2554eb91d1d7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 13:57 |
| **Last Seen** | 2026-07-25 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:57:35` | `cowrie.session.connect` |
| `2026-07-25 13:57:35` | `cowrie.client.version` |
| `2026-07-25 13:57:35` | `cowrie.client.kex` |
| `2026-07-25 13:57:35` | `cowrie.login.success` |
| `2026-07-25 13:57:35` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:57:36` | `cowrie.direct-tcpip.data` |
| `2026-07-25 13:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd0cc398d7d

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-07-25 13:59 |
| **Last Seen** | 2026-07-25 13:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:59:06` | `cowrie.session.connect` |
| `2026-07-25 13:59:07` | `cowrie.client.version` |
| `2026-07-25 13:59:07` | `cowrie.client.kex` |
| `2026-07-25 13:59:10` | `cowrie.login.success` |
| `2026-07-25 13:59:11` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f042facf1782

| Field | Detail |
|---|---|
| **Source IP** | `41.220.3[.]101` |
| **First Seen** | 2026-07-25 13:59 |
| **Last Seen** | 2026-07-25 13:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 13:59:16` | `cowrie.session.connect` |
| `2026-07-25 13:59:16` | `cowrie.client.version` |
| `2026-07-25 13:59:16` | `cowrie.client.kex` |
| `2026-07-25 13:59:18` | `cowrie.login.success` |
| `2026-07-25 13:59:19` | `cowrie.direct-tcpip.request` |
| `2026-07-25 13:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.220.3[.]101` to AbuseIPDB if not already reported
- [ ] Block `41.220.3[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a97dbdf9ea

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-25 14:02 |
| **Last Seen** | 2026-07-25 14:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:02:31` | `cowrie.session.connect` |
| `2026-07-25 14:02:32` | `cowrie.client.version` |
| `2026-07-25 14:02:32` | `cowrie.client.kex` |
| `2026-07-25 14:02:33` | `cowrie.login.success` |
| `2026-07-25 14:02:33` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9dbd72c863

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 14:05 |
| **Last Seen** | 2026-07-25 14:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:05:29` | `cowrie.session.connect` |
| `2026-07-25 14:05:29` | `cowrie.client.version` |
| `2026-07-25 14:05:29` | `cowrie.client.kex` |
| `2026-07-25 14:05:29` | `cowrie.login.success` |
| `2026-07-25 14:05:29` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:05:29` | `cowrie.direct-tcpip.data` |
| `2026-07-25 14:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5916747034b7

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-07-25 14:05 |
| **Last Seen** | 2026-07-25 14:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:05:34` | `cowrie.session.connect` |
| `2026-07-25 14:05:34` | `cowrie.client.version` |
| `2026-07-25 14:05:34` | `cowrie.client.kex` |
| `2026-07-25 14:05:35` | `cowrie.login.success` |
| `2026-07-25 14:05:36` | `cowrie.session.params` |
| `2026-07-25 14:05:36` | `cowrie.command.input` |
| `2026-07-25 14:05:36` | `cowrie.command.failed` |
| `2026-07-25 14:05:36` | `cowrie.log.closed` |
| `2026-07-25 14:05:37` | `cowrie.session.params` |
| `2026-07-25 14:05:37` | `cowrie.command.input` |
| `2026-07-25 14:05:37` | `cowrie.session.file_download` |
| `2026-07-25 14:05:37` | `cowrie.log.closed` |
| `2026-07-25 14:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce90be31dd83

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-07-25 14:05 |
| **Last Seen** | 2026-07-25 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:05:37` | `cowrie.session.connect` |
| `2026-07-25 14:05:37` | `cowrie.client.version` |
| `2026-07-25 14:05:38` | `cowrie.client.kex` |
| `2026-07-25 14:05:39` | `cowrie.login.success` |
| `2026-07-25 14:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c26b9bc495a

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-07-25 14:05 |
| **Last Seen** | 2026-07-25 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:05:39` | `cowrie.session.connect` |
| `2026-07-25 14:05:39` | `cowrie.client.version` |
| `2026-07-25 14:05:39` | `cowrie.client.kex` |
| `2026-07-25 14:05:40` | `cowrie.login.success` |
| `2026-07-25 14:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b6a922ec5d

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-25 14:13 |
| **Last Seen** | 2026-07-25 14:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:13:10` | `cowrie.session.connect` |
| `2026-07-25 14:13:11` | `cowrie.client.version` |
| `2026-07-25 14:13:11` | `cowrie.client.kex` |
| `2026-07-25 14:13:12` | `cowrie.login.success` |
| `2026-07-25 14:13:12` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e453ef1f83

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 14:14 |
| **Last Seen** | 2026-07-25 14:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:14:06` | `cowrie.session.connect` |
| `2026-07-25 14:14:06` | `cowrie.client.version` |
| `2026-07-25 14:14:06` | `cowrie.client.kex` |
| `2026-07-25 14:14:07` | `cowrie.login.success` |
| `2026-07-25 14:14:07` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:14:07` | `cowrie.direct-tcpip.data` |
| `2026-07-25 14:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6863c66225c

| Field | Detail |
|---|---|
| **Source IP** | `120.52.92[.]8` |
| **First Seen** | 2026-07-25 14:16 |
| **Last Seen** | 2026-07-25 14:21 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:16:20` | `cowrie.session.connect` |
| `2026-07-25 14:16:22` | `cowrie.client.version` |
| `2026-07-25 14:16:22` | `cowrie.client.kex` |
| `2026-07-25 14:16:22` | `cowrie.login.success` |
| `2026-07-25 14:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.92[.]8` to AbuseIPDB if not already reported
- [ ] Block `120.52.92[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51e1875eac2

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-25 14:22 |
| **Last Seen** | 2026-07-25 14:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:22:07` | `cowrie.session.connect` |
| `2026-07-25 14:22:08` | `cowrie.client.version` |
| `2026-07-25 14:22:08` | `cowrie.client.kex` |
| `2026-07-25 14:22:10` | `cowrie.login.success` |
| `2026-07-25 14:22:11` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa51b5f089f9

| Field | Detail |
|---|---|
| **Source IP** | `31.173.2[.]182` |
| **First Seen** | 2026-07-25 14:22 |
| **Last Seen** | 2026-07-25 14:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:22:21` | `cowrie.session.connect` |
| `2026-07-25 14:22:21` | `cowrie.client.version` |
| `2026-07-25 14:22:21` | `cowrie.client.kex` |
| `2026-07-25 14:22:22` | `cowrie.login.success` |
| `2026-07-25 14:22:23` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.2[.]182` to AbuseIPDB if not already reported
- [ ] Block `31.173.2[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d914c25b88

| Field | Detail |
|---|---|
| **Source IP** | `183.6.118[.]248` |
| **First Seen** | 2026-07-25 14:23 |
| **Last Seen** | 2026-07-25 14:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:23:59` | `cowrie.session.connect` |
| `2026-07-25 14:24:00` | `cowrie.client.version` |
| `2026-07-25 14:24:00` | `cowrie.client.kex` |
| `2026-07-25 14:24:03` | `cowrie.login.success` |
| `2026-07-25 14:24:04` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.6.118[.]248` to AbuseIPDB if not already reported
- [ ] Block `183.6.118[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73dc428d1b4f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:24 |
| **Last Seen** | 2026-07-25 14:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:24:51` | `cowrie.session.connect` |
| `2026-07-25 14:24:51` | `cowrie.client.version` |
| `2026-07-25 14:24:51` | `cowrie.client.kex` |
| `2026-07-25 14:24:55` | `cowrie.login.success` |
| `2026-07-25 14:24:57` | `cowrie.session.params` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.success` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:57` | `cowrie.command.input` |
| `2026-07-25 14:24:58` | `cowrie.log.closed` |
| `2026-07-25 14:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6e1e785106

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-07-25 14:25 |
| **Last Seen** | 2026-07-25 14:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:25:20` | `cowrie.session.connect` |
| `2026-07-25 14:25:21` | `cowrie.client.version` |
| `2026-07-25 14:25:21` | `cowrie.client.kex` |
| `2026-07-25 14:25:23` | `cowrie.login.success` |
| `2026-07-25 14:25:23` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c7a6bcb6f1

| Field | Detail |
|---|---|
| **Source IP** | `110.136.122[.]230` |
| **First Seen** | 2026-07-25 14:25 |
| **Last Seen** | 2026-07-25 14:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:25:29` | `cowrie.session.connect` |
| `2026-07-25 14:25:30` | `cowrie.client.version` |
| `2026-07-25 14:25:30` | `cowrie.client.kex` |
| `2026-07-25 14:25:33` | `cowrie.login.success` |
| `2026-07-25 14:25:35` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.136.122[.]230` to AbuseIPDB if not already reported
- [ ] Block `110.136.122[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1c2f296ff0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:25 |
| **Last Seen** | 2026-07-25 14:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:25:54` | `cowrie.session.connect` |
| `2026-07-25 14:25:55` | `cowrie.client.version` |
| `2026-07-25 14:25:55` | `cowrie.client.kex` |
| `2026-07-25 14:25:58` | `cowrie.login.success` |
| `2026-07-25 14:26:01` | `cowrie.session.params` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.success` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:01` | `cowrie.command.input` |
| `2026-07-25 14:26:02` | `cowrie.log.closed` |
| `2026-07-25 14:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9fd27ec793e

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-25 14:27 |
| **Last Seen** | 2026-07-25 14:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:27:10` | `cowrie.session.connect` |
| `2026-07-25 14:27:10` | `cowrie.client.version` |
| `2026-07-25 14:27:10` | `cowrie.client.kex` |
| `2026-07-25 14:27:11` | `cowrie.login.success` |
| `2026-07-25 14:27:12` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad55c512dfb2

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-07-25 14:27 |
| **Last Seen** | 2026-07-25 14:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:27:17` | `cowrie.session.connect` |
| `2026-07-25 14:27:17` | `cowrie.client.version` |
| `2026-07-25 14:27:17` | `cowrie.client.kex` |
| `2026-07-25 14:27:18` | `cowrie.login.success` |
| `2026-07-25 14:27:18` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f933c097cd1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:27 |
| **Last Seen** | 2026-07-25 14:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:27:18` | `cowrie.session.connect` |
| `2026-07-25 14:27:19` | `cowrie.client.version` |
| `2026-07-25 14:27:19` | `cowrie.client.kex` |
| `2026-07-25 14:27:22` | `cowrie.login.success` |
| `2026-07-25 14:27:25` | `cowrie.session.params` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.success` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.command.input` |
| `2026-07-25 14:27:25` | `cowrie.log.closed` |
| `2026-07-25 14:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde0f36f045c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 14:27 |
| **Last Seen** | 2026-07-25 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:27:55` | `cowrie.session.connect` |
| `2026-07-25 14:27:55` | `cowrie.client.version` |
| `2026-07-25 14:27:55` | `cowrie.client.kex` |
| `2026-07-25 14:27:56` | `cowrie.login.success` |
| `2026-07-25 14:27:56` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:27:56` | `cowrie.direct-tcpip.data` |
| `2026-07-25 14:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88000ba85b5f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:28 |
| **Last Seen** | 2026-07-25 14:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:28:43` | `cowrie.session.connect` |
| `2026-07-25 14:28:43` | `cowrie.client.version` |
| `2026-07-25 14:28:43` | `cowrie.client.kex` |
| `2026-07-25 14:28:47` | `cowrie.login.success` |
| `2026-07-25 14:28:49` | `cowrie.session.params` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.success` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:49` | `cowrie.command.input` |
| `2026-07-25 14:28:50` | `cowrie.log.closed` |
| `2026-07-25 14:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1df101d873b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:30 |
| **Last Seen** | 2026-07-25 14:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:30:14` | `cowrie.session.connect` |
| `2026-07-25 14:30:15` | `cowrie.client.version` |
| `2026-07-25 14:30:15` | `cowrie.client.kex` |
| `2026-07-25 14:30:20` | `cowrie.login.success` |
| `2026-07-25 14:30:22` | `cowrie.session.params` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.success` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:22` | `cowrie.command.input` |
| `2026-07-25 14:30:23` | `cowrie.log.closed` |
| `2026-07-25 14:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572d2799570d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:31 |
| **Last Seen** | 2026-07-25 14:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:31:50` | `cowrie.session.connect` |
| `2026-07-25 14:31:51` | `cowrie.client.version` |
| `2026-07-25 14:31:51` | `cowrie.client.kex` |
| `2026-07-25 14:31:56` | `cowrie.login.success` |
| `2026-07-25 14:32:00` | `cowrie.session.params` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.success` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:00` | `cowrie.command.input` |
| `2026-07-25 14:32:01` | `cowrie.log.closed` |
| `2026-07-25 14:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5be66f754a8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:33 |
| **Last Seen** | 2026-07-25 14:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:33:28` | `cowrie.session.connect` |
| `2026-07-25 14:33:28` | `cowrie.client.version` |
| `2026-07-25 14:33:28` | `cowrie.client.kex` |
| `2026-07-25 14:33:31` | `cowrie.login.success` |
| `2026-07-25 14:33:33` | `cowrie.session.params` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.success` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:33` | `cowrie.command.input` |
| `2026-07-25 14:33:34` | `cowrie.log.closed` |
| `2026-07-25 14:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2718c28fde

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:34 |
| **Last Seen** | 2026-07-25 14:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:34:43` | `cowrie.session.connect` |
| `2026-07-25 14:34:43` | `cowrie.client.version` |
| `2026-07-25 14:34:43` | `cowrie.client.kex` |
| `2026-07-25 14:34:46` | `cowrie.login.success` |
| `2026-07-25 14:34:48` | `cowrie.session.params` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.success` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:48` | `cowrie.command.input` |
| `2026-07-25 14:34:49` | `cowrie.log.closed` |
| `2026-07-25 14:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a76823bcc1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:35 |
| **Last Seen** | 2026-07-25 14:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:35:58` | `cowrie.session.connect` |
| `2026-07-25 14:35:59` | `cowrie.client.version` |
| `2026-07-25 14:35:59` | `cowrie.client.kex` |
| `2026-07-25 14:36:01` | `cowrie.login.success` |
| `2026-07-25 14:36:03` | `cowrie.session.params` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.success` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:03` | `cowrie.command.input` |
| `2026-07-25 14:36:04` | `cowrie.log.closed` |
| `2026-07-25 14:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53de1c95dfd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:37 |
| **Last Seen** | 2026-07-25 14:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:37:12` | `cowrie.session.connect` |
| `2026-07-25 14:37:12` | `cowrie.client.version` |
| `2026-07-25 14:37:12` | `cowrie.client.kex` |
| `2026-07-25 14:37:15` | `cowrie.login.success` |
| `2026-07-25 14:37:16` | `cowrie.session.params` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.success` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:16` | `cowrie.command.input` |
| `2026-07-25 14:37:17` | `cowrie.log.closed` |
| `2026-07-25 14:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502446479495

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:38 |
| **Last Seen** | 2026-07-25 14:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:38:24` | `cowrie.session.connect` |
| `2026-07-25 14:38:25` | `cowrie.client.version` |
| `2026-07-25 14:38:25` | `cowrie.client.kex` |
| `2026-07-25 14:38:27` | `cowrie.login.success` |
| `2026-07-25 14:38:29` | `cowrie.session.params` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.success` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.command.input` |
| `2026-07-25 14:38:29` | `cowrie.log.closed` |
| `2026-07-25 14:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fe436eb348

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 14:39 |
| **Last Seen** | 2026-07-25 14:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:39:03` | `cowrie.session.connect` |
| `2026-07-25 14:39:03` | `cowrie.client.version` |
| `2026-07-25 14:39:03` | `cowrie.client.kex` |
| `2026-07-25 14:39:04` | `cowrie.login.success` |
| `2026-07-25 14:39:04` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:39:04` | `cowrie.direct-tcpip.data` |
| `2026-07-25 14:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814008cb6c5b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:39 |
| **Last Seen** | 2026-07-25 14:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:39:38` | `cowrie.session.connect` |
| `2026-07-25 14:39:39` | `cowrie.client.version` |
| `2026-07-25 14:39:39` | `cowrie.client.kex` |
| `2026-07-25 14:39:41` | `cowrie.login.success` |
| `2026-07-25 14:39:42` | `cowrie.session.params` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.success` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:42` | `cowrie.command.input` |
| `2026-07-25 14:39:43` | `cowrie.log.closed` |
| `2026-07-25 14:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016b51b46e88

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:40 |
| **Last Seen** | 2026-07-25 14:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:40:53` | `cowrie.session.connect` |
| `2026-07-25 14:40:54` | `cowrie.client.version` |
| `2026-07-25 14:40:54` | `cowrie.client.kex` |
| `2026-07-25 14:40:56` | `cowrie.login.success` |
| `2026-07-25 14:40:57` | `cowrie.session.params` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.success` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:57` | `cowrie.command.input` |
| `2026-07-25 14:40:58` | `cowrie.log.closed` |
| `2026-07-25 14:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7354e3e74866

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-07-25 14:41 |
| **Last Seen** | 2026-07-25 14:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:41:33` | `cowrie.session.connect` |
| `2026-07-25 14:41:34` | `cowrie.client.version` |
| `2026-07-25 14:41:34` | `cowrie.client.kex` |
| `2026-07-25 14:41:37` | `cowrie.login.success` |
| `2026-07-25 14:41:38` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e7e829cefe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-25 14:42 |
| **Last Seen** | 2026-07-25 14:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:42:08` | `cowrie.session.connect` |
| `2026-07-25 14:42:08` | `cowrie.client.version` |
| `2026-07-25 14:42:08` | `cowrie.client.kex` |
| `2026-07-25 14:42:11` | `cowrie.login.success` |
| `2026-07-25 14:42:12` | `cowrie.session.params` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.success` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:12` | `cowrie.command.input` |
| `2026-07-25 14:42:13` | `cowrie.log.closed` |
| `2026-07-25 14:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390f939b8bb9

| Field | Detail |
|---|---|
| **Source IP** | `85.206.68[.]80` |
| **First Seen** | 2026-07-25 14:44 |
| **Last Seen** | 2026-07-25 14:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:44:38` | `cowrie.session.connect` |
| `2026-07-25 14:44:38` | `cowrie.client.version` |
| `2026-07-25 14:44:39` | `cowrie.client.kex` |
| `2026-07-25 14:44:39` | `cowrie.login.success` |
| `2026-07-25 14:44:40` | `cowrie.session.params` |
| `2026-07-25 14:44:40` | `cowrie.command.input` |
| `2026-07-25 14:44:40` | `cowrie.command.failed` |
| `2026-07-25 14:44:40` | `cowrie.log.closed` |
| `2026-07-25 14:44:41` | `cowrie.session.params` |
| `2026-07-25 14:44:41` | `cowrie.command.input` |
| `2026-07-25 14:44:41` | `cowrie.session.file_download` |
| `2026-07-25 14:44:41` | `cowrie.log.closed` |
| `2026-07-25 14:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.206.68[.]80` to AbuseIPDB if not already reported
- [ ] Block `85.206.68[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349cd2df973b

| Field | Detail |
|---|---|
| **Source IP** | `85.206.68[.]80` |
| **First Seen** | 2026-07-25 14:44 |
| **Last Seen** | 2026-07-25 14:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:44:41` | `cowrie.session.connect` |
| `2026-07-25 14:44:41` | `cowrie.client.version` |
| `2026-07-25 14:44:41` | `cowrie.client.kex` |
| `2026-07-25 14:44:42` | `cowrie.login.success` |
| `2026-07-25 14:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.206.68[.]80` to AbuseIPDB if not already reported
- [ ] Block `85.206.68[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526ed63c5342

| Field | Detail |
|---|---|
| **Source IP** | `85.206.68[.]80` |
| **First Seen** | 2026-07-25 14:44 |
| **Last Seen** | 2026-07-25 14:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:44:42` | `cowrie.session.connect` |
| `2026-07-25 14:44:42` | `cowrie.client.version` |
| `2026-07-25 14:44:42` | `cowrie.client.kex` |
| `2026-07-25 14:44:43` | `cowrie.login.success` |
| `2026-07-25 14:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.206.68[.]80` to AbuseIPDB if not already reported
- [ ] Block `85.206.68[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964a39408727

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 14:50 |
| **Last Seen** | 2026-07-25 14:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:50:25` | `cowrie.session.connect` |
| `2026-07-25 14:50:25` | `cowrie.client.version` |
| `2026-07-25 14:50:25` | `cowrie.client.kex` |
| `2026-07-25 14:50:25` | `cowrie.login.success` |
| `2026-07-25 14:50:25` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:50:25` | `cowrie.direct-tcpip.data` |
| `2026-07-25 14:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0822c58c1b6f

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-07-25 14:52 |
| **Last Seen** | 2026-07-25 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 14:52:05` | `cowrie.session.connect` |
| `2026-07-25 14:52:05` | `cowrie.client.version` |
| `2026-07-25 14:52:05` | `cowrie.client.kex` |
| `2026-07-25 14:52:08` | `cowrie.login.success` |
| `2026-07-25 14:52:08` | `cowrie.direct-tcpip.request` |
| `2026-07-25 14:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `156.225.1[.]44` | **8** | 2026-07-25 13:33 | 2026-07-25 13:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-25 12:55 | 2026-07-25 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **4** | 2026-07-25 13:07 | 2026-07-25 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | **3** | 2026-07-25 14:38 | 2026-07-25 14:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-25 14:34 | 2026-07-25 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-25 13:21 | 2026-07-25 13:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-25 13:47 | 2026-07-25 13:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]203` | **2** | 2026-07-25 14:29 | 2026-07-25 14:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-07-25 14:03 | 2026-07-25 14:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.213.214[.]233` | 1 | 2026-07-25 14:37 | 2026-07-25 14:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-07-25 14:44 | 2026-07-25 14:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.26.200[.]188` | 1 | 2026-07-25 13:41 | 2026-07-25 13:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `124.133.10[.]66` | 1 | 2026-07-25 14:01 | 2026-07-25 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]35` | 1 | 2026-07-25 14:14 | 2026-07-25 14:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-07-25 14:52 | 2026-07-25 14:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]42` | 1 | 2026-07-25 14:19 | 2026-07-25 14:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-07-25 13:48 | 2026-07-25 13:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-07-25 13:23 | 2026-07-25 13:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.64.33[.]82` | 1 | 2026-07-25 14:41 | 2026-07-25 14:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-25 13:06 | 2026-07-25 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-25 14:38 | 2026-07-25 14:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-25 13:37 | 2026-07-25 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-07-25 13:36 | 2026-07-25 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]250` | 1 | 2026-07-25 13:13 | 2026-07-25 13:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]56` | 1 | 2026-07-25 14:22 | 2026-07-25 14:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-25 13:51 | 2026-07-25 13:53 | 88s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-07-25 13:32 | 2026-07-25 13:32 | 16s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |

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
| `156.225.1[.]44` | HK | AGOTOZ PTE. LTD | **100** ⚠️ | 3 |
| `185.112.148[.]66` | IR | Sefroyek Pardaz Engineering PJSC | **100** ⚠️ | 10 |
| `213.66.197[.]199` | SE | Telia Network services | **100** ⚠️ | 42 |
| `142.93.218[.]50` | IN | DigitalOcean, LLC | **100** ⚠️ | 30 |
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `172.235.40[.]131` | US | Linode | **100** ⚠️ | 50 |
| `187.115.144[.]103` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |
| `88.214.25[.]123` | DE | VDS&VPN services | **100** ⚠️ | 50 |
| `196.190.180[.]18` | ET | Ethio Telecom | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 57 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 14 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 14 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 118 cases |
| Tool 34  | Credential Extractor        | ✅ 81 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (8.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 57 priority case(s) shown individually · 27 recon entry/entries in table (9 group(s) consolidating 33 session(s)).

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
_Report time: 2026-07-25T15:08:02Z_

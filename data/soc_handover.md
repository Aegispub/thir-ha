# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-30 |
| **Generated At** | 2026-07-30T14:11:08Z |
| **Shift Time** | 14:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **281** |
| Confirmed Threats | **240** |
| False Positives Filtered | **41** (14.6%) |
| Unique Attacker IPs | **136** |
| Countries of Origin | **33** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **194** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **118** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **18** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **91** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `supervisor` | 15 |
| `admin` | 12 |
| `unknown` | 10 |
| `support` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 8 |
| `admin` | 6 |
| `centos13` | 6 |
| `admin1` | 5 |
| `123qwe` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `centos` | `centos13` | 6 |
| `admin` | `admin` | 5 |
| `admin` | `admin1` | 5 |
| `supervisor` | `123qwe` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `unknown12345678` | `49.124.151.65` | 2026-07-30T09:05:02 |
| `admin` | `admin` | `47.88.0.49` | 2026-07-30T09:06:37 |
| `supervisor` | `supervisor00` | `203.92.36.109` | 2026-07-30T09:08:24 |
| `supervisor` | `supervisor00` | `220.122.115.9` | 2026-07-30T09:08:33 |
| `supervisor` | `supervisor00` | `122.170.98.139` | 2026-07-30T09:08:38 |
| `operator` | `admin123` | `203.129.217.70` | 2026-07-30T09:10:08 |
| `operator` | `admin123` | `103.93.37.178` | 2026-07-30T09:10:20 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-30T09:12:12 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-30T09:12:13 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-30T09:12:15 |
| `guest` | `guest8` | `196.188.93.169` | 2026-07-30T09:13:15 |
| `guest` | `guest8` | `183.82.108.109` | 2026-07-30T09:13:23 |
| `supervisor` | `default` | `10.0.0.73` | 2026-07-30T09:21:39 |
| `admin` | `admin` | `147.139.136.75` | 2026-07-30T09:27:06 |
| `default` | `passwd` | `10.0.0.73` | 2026-07-30T09:27:47 |
| `support` | `support` | `176.53.159.196` | 2026-07-30T09:27:56 |
| `guest` | `guest4` | `185.2.228.48` | 2026-07-30T09:43:46 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-30T09:47:06 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-30T09:47:06 |
| `support` | `support` | `200.232.114.71` | 2026-07-30T09:47:10 |
| `admin` | `admin1` | `49.124.151.21` | 2026-07-30T09:50:51 |
| `admin` | `admin1` | `220.246.43.109` | 2026-07-30T09:51:05 |
| `support` | `support` | `10.0.0.73` | 2026-07-30T09:52:04 |
| `unknown` | `unknown2` | `10.0.0.73` | 2026-07-30T09:56:51 |
| `unknown` | `999` | `10.0.0.73` | 2026-07-30T09:59:26 |
| `admin` | `admin1` | `10.0.0.73` | 2026-07-30T10:02:47 |
| `supervisor` | `123qwe` | `10.0.0.73` | 2026-07-30T10:15:10 |
| `unknown` | `unknown2` | `111.70.29.158` | 2026-07-30T10:15:12 |
| `admin` | `admin` | `104.251.181.37` | 2026-07-30T10:18:44 |
| `admin` | `admin1` | `90.230.168.26` | 2026-07-30T10:20:26 |
| `supervisor` | `123qwe` | `95.79.57.221` | 2026-07-30T10:20:44 |
| `supervisor` | `123qwe` | `93.42.222.164` | 2026-07-30T10:20:51 |
| `root` | `` | `94.154.43.144` | 2026-07-30T10:22:24 |
| `supervisor` | `123qwe` | `2.54.85.220` | 2026-07-30T10:28:44 |
| `supervisor` | `123qwe` | `111.171.125.94` | 2026-07-30T10:28:53 |
| `guest` | `uploader` | `10.0.0.73` | 2026-07-30T10:31:55 |
| `guest` | `uploader` | `14.29.204.161` | 2026-07-30T10:33:38 |
| `guest` | `uploader` | `220.93.167.144` | 2026-07-30T10:33:47 |
| `supervisor` | `qwerty12345` | `10.0.0.73` | 2026-07-30T10:34:42 |
| `root` | `123!@#qwe` | `10.0.0.73` | 2026-07-30T10:49:00 |
| `supervisor` | `qwerty12345` | `24.207.66.154` | 2026-07-30T10:53:45 |
| `supervisor` | `qwerty12345` | `103.103.53.44` | 2026-07-30T10:53:54 |
| `supervisor` | `qwerty12345` | `178.178.194.151` | 2026-07-30T10:53:58 |
| `root` | `123!@#qwe` | `102.211.7.162` | 2026-07-30T10:54:07 |
| `root` | `123!@#qwe` | `103.68.52.210` | 2026-07-30T10:54:15 |
| `support` | `1961` | `117.211.15.106` | 2026-07-30T10:55:30 |
| `support` | `1961` | `203.124.60.46` | 2026-07-30T10:55:40 |
| `blank` | `swiadmin` | `49.124.153.58` | 2026-07-30T11:00:54 |
| `operator` | `P@ssword` | `112.27.38.203` | 2026-07-30T11:08:50 |
| `unknown` | `unknown1234567890` | `10.0.0.73` | 2026-07-30T11:09:38 |
| `config` | `config5` | `10.0.0.73` | 2026-07-30T11:22:20 |
| `operator` | `P@ssword` | `14.49.131.77` | 2026-07-30T11:25:28 |
| `unknown` | `unknown1234567890` | `178.178.222.55` | 2026-07-30T11:28:52 |
| `unknown` | `unknown1234567890` | `182.76.36.62` | 2026-07-30T11:29:01 |
| `unknown` | `unknown1234567890` | `62.91.108.146` | 2026-07-30T11:29:07 |
| `root` | `admin` | `192.42.116.17` | 2026-07-30T11:30:07 |
| `blank` | `swiadmin` | `60.18.139.82` | 2026-07-30T11:30:42 |
| `config` | `config5` | `41.178.230.115` | 2026-07-30T11:35:45 |
| `blank` | `blank1` | `114.30.223.119` | 2026-07-30T11:44:00 |
| `test1` | `test1` | `2.57.122.168` | 2026-07-30T11:45:03 |
| `blank` | `blank8` | `10.0.0.73` | 2026-07-30T11:45:03 |
| `test2` | `test2` | `2.57.122.168` | 2026-07-30T11:46:59 |
| `root` | `---fuck_you----` | `152.32.230.238` | 2026-07-30T11:47:05 |
| `user` | `102030` | `10.0.0.73` | 2026-07-30T11:48:07 |
| `test3` | `test3` | `2.57.122.168` | 2026-07-30T11:48:53 |
| `ubuntu` | `password2025!` | `91.232.247.229` | 2026-07-30T11:49:01 |
| `345gs5662d34` | `345gs5662d34` | `91.232.247.229` | 2026-07-30T11:49:03 |
| `ubuntu` | `3245gs5662d34` | `91.232.247.229` | 2026-07-30T11:49:04 |
| `root` | `root123` | `2.57.122.168` | 2026-07-30T11:50:46 |
| `blank` | `blank1` | `183.247.171.186` | 2026-07-30T12:00:45 |
| `admin` | `admin66` | `111.70.13.240` | 2026-07-30T12:01:22 |
| `admin` | `admin66` | `118.113.164.137` | 2026-07-30T12:01:31 |
| `blank` | `blank8` | `111.17.213.162` | 2026-07-30T12:04:23 |
| `default` | `maintenance` | `117.34.210.196` | 2026-07-30T12:19:21 |
| `default` | `maintenance` | `186.215.107.189` | 2026-07-30T12:19:33 |
| `operator` | `operator` | `10.0.0.73` | 2026-07-30T12:23:18 |
| `ubuntu` | `a12345678` | `118.145.246.44` | 2026-07-30T12:27:48 |
| `ubuntu` | `3245gs5662d34` | `118.145.246.44` | 2026-07-30T12:28:07 |
| `centos` | `centos13` | `10.0.0.73` | 2026-07-30T12:30:10 |
| `centos` | `centos13` | `1.247.245.61` | 2026-07-30T12:35:31 |
| `centos` | `centos13` | `116.228.195.251` | 2026-07-30T12:35:45 |
| `default` | `maintenance` | `223.107.146.186` | 2026-07-30T12:36:20 |
| `guest` | `guest1234567890` | `49.124.147.109` | 2026-07-30T12:39:34 |
| `guest` | `guest1234567890` | `202.111.183.30` | 2026-07-30T12:39:47 |
| `centos` | `centos13` | `220.246.46.144` | 2026-07-30T12:43:25 |
| `centos` | `centos13` | `117.158.166.73` | 2026-07-30T12:43:35 |
| `operator` | `test` | `115.241.228.34` | 2026-07-30T12:46:44 |
| `operator` | `test` | `121.179.93.147` | 2026-07-30T12:46:53 |
| `ssh` | `ssh` | `10.0.0.73` | 2026-07-30T12:53:07 |
| `ssh` | `ssh` | `136.56.34.147` | 2026-07-30T12:54:51 |
| `ssh` | `ssh` | `62.201.228.210` | 2026-07-30T12:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **281** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 56 |
| libssh | 20 |
| Go SSH scanner | 16 |
| Paramiko (Python) | 12 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 55 | 54 |
| `a2de0f306611...` | Mirai/variant | 12 | 2 |
| `f555226df196...` | Mirai/variant | 5 | 2 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 55 | 54 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 6 | — |
| `a2de0f306611...` | Paramiko (Python) | 12 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 5 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 4 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.168`

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
Source IPs: `94.154.43.144`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.145.246.44`, `91.232.247.229`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **136** |
| Unique ASNs | **82** |
| High-Risk ASNs | **67** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 12 | MEDIUM |
| `AS46562` | Performive LLC | 9 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS4766` | Korea Telecom | 7 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 4 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (87)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dd9b35ea96c9

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]65` |
| **First Seen** | 2026-07-30 09:04 |
| **Last Seen** | 2026-07-30 09:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:04:59` | `cowrie.session.connect` |
| `2026-07-30 09:05:00` | `cowrie.client.version` |
| `2026-07-30 09:05:00` | `cowrie.client.kex` |
| `2026-07-30 09:05:02` | `cowrie.login.success` |
| `2026-07-30 09:05:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]65` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc4bf5b9a54

| Field | Detail |
|---|---|
| **Source IP** | `47.88.0[.]49` |
| **First Seen** | 2026-07-30 09:06 |
| **Last Seen** | 2026-07-30 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:06:37` | `cowrie.session.connect` |
| `2026-07-30 09:06:37` | `cowrie.telnet.option` |
| `2026-07-30 09:06:37` | `cowrie.telnet.option` |
| `2026-07-30 09:06:37` | `cowrie.login.success` |
| `2026-07-30 09:06:37` | `cowrie.session.params` |
| `2026-07-30 09:06:38` | `cowrie.log.closed` |
| `2026-07-30 09:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.0[.]49` to AbuseIPDB if not already reported
- [ ] Block `47.88.0[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2477fbceee2d

| Field | Detail |
|---|---|
| **Source IP** | `47.88.0[.]49` |
| **First Seen** | 2026-07-30 09:06 |
| **Last Seen** | 2026-07-30 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:06:45` | `cowrie.session.connect` |
| `2026-07-30 09:06:45` | `cowrie.telnet.option` |
| `2026-07-30 09:06:45` | `cowrie.telnet.option` |
| `2026-07-30 09:06:45` | `cowrie.login.success` |
| `2026-07-30 09:06:46` | `cowrie.session.params` |
| `2026-07-30 09:06:46` | `cowrie.telnet.option` |
| `2026-07-30 09:06:46` | `cowrie.telnet.option` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.failed` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.failed` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.failed` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.command.input` |
| `2026-07-30 09:06:46` | `cowrie.log.closed` |
| `2026-07-30 09:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.0[.]49` to AbuseIPDB if not already reported
- [ ] Block `47.88.0[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d56f2404a4d

| Field | Detail |
|---|---|
| **Source IP** | `47.88.0[.]49` |
| **First Seen** | 2026-07-30 09:07 |
| **Last Seen** | 2026-07-30 09:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:07:03` | `cowrie.session.connect` |
| `2026-07-30 09:07:03` | `cowrie.telnet.option` |
| `2026-07-30 09:07:03` | `cowrie.telnet.option` |
| `2026-07-30 09:07:03` | `cowrie.login.success` |
| `2026-07-30 09:07:04` | `cowrie.session.params` |
| `2026-07-30 09:07:04` | `cowrie.log.closed` |
| `2026-07-30 09:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.0[.]49` to AbuseIPDB if not already reported
- [ ] Block `47.88.0[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f2913890df

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-30 09:08 |
| **Last Seen** | 2026-07-30 09:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:08:22` | `cowrie.session.connect` |
| `2026-07-30 09:08:22` | `cowrie.client.version` |
| `2026-07-30 09:08:22` | `cowrie.client.kex` |
| `2026-07-30 09:08:24` | `cowrie.login.success` |
| `2026-07-30 09:08:25` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3be43a33322d

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-30 09:08 |
| **Last Seen** | 2026-07-30 09:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:08:30` | `cowrie.session.connect` |
| `2026-07-30 09:08:31` | `cowrie.client.version` |
| `2026-07-30 09:08:31` | `cowrie.client.kex` |
| `2026-07-30 09:08:33` | `cowrie.login.success` |
| `2026-07-30 09:08:33` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3047c59488f3

| Field | Detail |
|---|---|
| **Source IP** | `122.170.98[.]139` |
| **First Seen** | 2026-07-30 09:08 |
| **Last Seen** | 2026-07-30 09:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:08:35` | `cowrie.session.connect` |
| `2026-07-30 09:08:36` | `cowrie.client.version` |
| `2026-07-30 09:08:36` | `cowrie.client.kex` |
| `2026-07-30 09:08:38` | `cowrie.login.success` |
| `2026-07-30 09:08:38` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.98[.]139` to AbuseIPDB if not already reported
- [ ] Block `122.170.98[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68be8939d6ae

| Field | Detail |
|---|---|
| **Source IP** | `203.129.217[.]70` |
| **First Seen** | 2026-07-30 09:10 |
| **Last Seen** | 2026-07-30 09:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:10:05` | `cowrie.session.connect` |
| `2026-07-30 09:10:06` | `cowrie.client.version` |
| `2026-07-30 09:10:06` | `cowrie.client.kex` |
| `2026-07-30 09:10:08` | `cowrie.login.success` |
| `2026-07-30 09:10:08` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.217[.]70` to AbuseIPDB if not already reported
- [ ] Block `203.129.217[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1984227614a5

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-30 09:10 |
| **Last Seen** | 2026-07-30 09:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:10:15` | `cowrie.session.connect` |
| `2026-07-30 09:10:16` | `cowrie.client.version` |
| `2026-07-30 09:10:16` | `cowrie.client.kex` |
| `2026-07-30 09:10:20` | `cowrie.login.success` |
| `2026-07-30 09:10:20` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb733823acbb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 09:12 |
| **Last Seen** | 2026-07-30 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:12:12` | `cowrie.session.connect` |
| `2026-07-30 09:12:12` | `cowrie.client.version` |
| `2026-07-30 09:12:12` | `cowrie.client.kex` |
| `2026-07-30 09:12:12` | `cowrie.login.success` |
| `2026-07-30 09:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef8a74e46b0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 09:12 |
| **Last Seen** | 2026-07-30 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:12:13` | `cowrie.session.connect` |
| `2026-07-30 09:12:13` | `cowrie.client.version` |
| `2026-07-30 09:12:13` | `cowrie.client.kex` |
| `2026-07-30 09:12:13` | `cowrie.login.success` |
| `2026-07-30 09:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2711df9a89

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 09:12 |
| **Last Seen** | 2026-07-30 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:12:15` | `cowrie.session.connect` |
| `2026-07-30 09:12:15` | `cowrie.client.version` |
| `2026-07-30 09:12:15` | `cowrie.client.kex` |
| `2026-07-30 09:12:15` | `cowrie.login.success` |
| `2026-07-30 09:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385ccf4aaa8a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 09:12 |
| **Last Seen** | 2026-07-30 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:12:15` | `cowrie.session.connect` |
| `2026-07-30 09:12:15` | `cowrie.client.version` |
| `2026-07-30 09:12:15` | `cowrie.client.kex` |
| `2026-07-30 09:12:15` | `cowrie.login.success` |
| `2026-07-30 09:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a60bf45cc2

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-30 09:13 |
| **Last Seen** | 2026-07-30 09:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:13:13` | `cowrie.session.connect` |
| `2026-07-30 09:13:14` | `cowrie.client.version` |
| `2026-07-30 09:13:14` | `cowrie.client.kex` |
| `2026-07-30 09:13:15` | `cowrie.login.success` |
| `2026-07-30 09:13:15` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6682a8ce3397

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-07-30 09:13 |
| **Last Seen** | 2026-07-30 09:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:13:21` | `cowrie.session.connect` |
| `2026-07-30 09:13:21` | `cowrie.client.version` |
| `2026-07-30 09:13:21` | `cowrie.client.kex` |
| `2026-07-30 09:13:23` | `cowrie.login.success` |
| `2026-07-30 09:13:24` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233db927c59e

| Field | Detail |
|---|---|
| **Source IP** | `147.139.136[.]75` |
| **First Seen** | 2026-07-30 09:25 |
| **Last Seen** | 2026-07-30 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:25:30` | `cowrie.session.connect` |
| `2026-07-30 09:25:43` | `cowrie.telnet.option` |
| `2026-07-30 09:26:06` | `cowrie.telnet.option` |
| `2026-07-30 09:27:06` | `cowrie.login.success` |
| `2026-07-30 09:27:06` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `147.139.136[.]75` to AbuseIPDB if not already reported
- [ ] Block `147.139.136[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-decbe643260a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 09:27 |
| **Last Seen** | 2026-07-30 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:27:55` | `cowrie.session.connect` |
| `2026-07-30 09:27:55` | `cowrie.client.version` |
| `2026-07-30 09:27:55` | `cowrie.client.kex` |
| `2026-07-30 09:27:56` | `cowrie.login.success` |
| `2026-07-30 09:27:56` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:27:56` | `cowrie.direct-tcpip.data` |
| `2026-07-30 09:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a32053b88ac

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-30 09:43 |
| **Last Seen** | 2026-07-30 09:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:43:44` | `cowrie.session.connect` |
| `2026-07-30 09:43:45` | `cowrie.client.version` |
| `2026-07-30 09:43:45` | `cowrie.client.kex` |
| `2026-07-30 09:43:46` | `cowrie.login.success` |
| `2026-07-30 09:43:46` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adc41082c8d

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-30 09:43 |
| **Last Seen** | 2026-07-30 09:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:43:51` | `cowrie.session.connect` |
| `2026-07-30 09:43:51` | `cowrie.client.version` |
| `2026-07-30 09:43:51` | `cowrie.client.kex` |
| `2026-07-30 09:43:53` | `cowrie.login.success` |
| `2026-07-30 09:43:53` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6aab54071f3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 09:47 |
| **Last Seen** | 2026-07-30 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:47:05` | `cowrie.session.connect` |
| `2026-07-30 09:47:05` | `cowrie.client.version` |
| `2026-07-30 09:47:05` | `cowrie.client.kex` |
| `2026-07-30 09:47:06` | `cowrie.login.success` |
| `2026-07-30 09:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33bb6378bf4b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 09:47 |
| **Last Seen** | 2026-07-30 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:47:05` | `cowrie.session.connect` |
| `2026-07-30 09:47:05` | `cowrie.client.version` |
| `2026-07-30 09:47:05` | `cowrie.client.kex` |
| `2026-07-30 09:47:06` | `cowrie.login.success` |
| `2026-07-30 09:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99f4814ca1c

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-30 09:47 |
| **Last Seen** | 2026-07-30 09:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:47:07` | `cowrie.session.connect` |
| `2026-07-30 09:47:08` | `cowrie.client.version` |
| `2026-07-30 09:47:08` | `cowrie.client.kex` |
| `2026-07-30 09:47:10` | `cowrie.login.success` |
| `2026-07-30 09:47:10` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0513dcc615

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]21` |
| **First Seen** | 2026-07-30 09:50 |
| **Last Seen** | 2026-07-30 09:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:50:48` | `cowrie.session.connect` |
| `2026-07-30 09:50:49` | `cowrie.client.version` |
| `2026-07-30 09:50:49` | `cowrie.client.kex` |
| `2026-07-30 09:50:51` | `cowrie.login.success` |
| `2026-07-30 09:50:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]21` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8666aaccad9a

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-07-30 09:51 |
| **Last Seen** | 2026-07-30 09:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 09:51:02` | `cowrie.session.connect` |
| `2026-07-30 09:51:03` | `cowrie.client.version` |
| `2026-07-30 09:51:03` | `cowrie.client.kex` |
| `2026-07-30 09:51:05` | `cowrie.login.success` |
| `2026-07-30 09:51:05` | `cowrie.direct-tcpip.request` |
| `2026-07-30 09:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3609a73b58

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-07-30 10:15 |
| **Last Seen** | 2026-07-30 10:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:15:09` | `cowrie.session.connect` |
| `2026-07-30 10:15:10` | `cowrie.client.version` |
| `2026-07-30 10:15:10` | `cowrie.client.kex` |
| `2026-07-30 10:15:12` | `cowrie.login.success` |
| `2026-07-30 10:15:12` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3e2af68879

| Field | Detail |
|---|---|
| **Source IP** | `104.251.181[.]37` |
| **First Seen** | 2026-07-30 10:16 |
| **Last Seen** | 2026-07-30 10:19 |
| **Session Duration** | 174s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo PlAQcH9vvO && cd /tmp; echo wMgijaRSYH > hQcVxKDycl && sleep 274 &` |
| **Download Attempts** | 7720c34f05c646b0c8c69e97d4c9dedb839ee048bc6eee9d064216cbab2649d7 |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:16:51` | `cowrie.session.connect` |
| `2026-07-30 10:17:11` | `cowrie.client.version` |
| `2026-07-30 10:17:11` | `cowrie.client.kex` |
| `2026-07-30 10:18:44` | `cowrie.login.success` |
| `2026-07-30 10:19:25` | `cowrie.session.params` |
| `2026-07-30 10:19:25` | `cowrie.command.input` |
| `2026-07-30 10:19:45` | `cowrie.session.file_download` |
| `2026-07-30 10:19:45` | `cowrie.log.closed` |
| `2026-07-30 10:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.251.181[.]37` to AbuseIPDB if not already reported
- [ ] Block `104.251.181[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b06ddfaa6bd

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-07-30 10:20 |
| **Last Seen** | 2026-07-30 10:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:20:24` | `cowrie.session.connect` |
| `2026-07-30 10:20:25` | `cowrie.client.version` |
| `2026-07-30 10:20:25` | `cowrie.client.kex` |
| `2026-07-30 10:20:26` | `cowrie.login.success` |
| `2026-07-30 10:20:26` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea66a232624f

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-30 10:20 |
| **Last Seen** | 2026-07-30 10:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:20:43` | `cowrie.session.connect` |
| `2026-07-30 10:20:43` | `cowrie.client.version` |
| `2026-07-30 10:20:43` | `cowrie.client.kex` |
| `2026-07-30 10:20:44` | `cowrie.login.success` |
| `2026-07-30 10:20:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8095a3dc46

| Field | Detail |
|---|---|
| **Source IP** | `93.42.222[.]164` |
| **First Seen** | 2026-07-30 10:20 |
| **Last Seen** | 2026-07-30 10:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:20:50` | `cowrie.session.connect` |
| `2026-07-30 10:20:50` | `cowrie.client.version` |
| `2026-07-30 10:20:50` | `cowrie.client.kex` |
| `2026-07-30 10:20:51` | `cowrie.login.success` |
| `2026-07-30 10:20:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.42.222[.]164` to AbuseIPDB if not already reported
- [ ] Block `93.42.222[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80253d228efd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]144` |
| **First Seen** | 2026-07-30 10:22 |
| **Last Seen** | 2026-07-30 10:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:22:24` | `cowrie.session.connect` |
| `2026-07-30 10:22:24` | `cowrie.login.success` |
| `2026-07-30 10:22:25` | `cowrie.session.params` |
| `2026-07-30 10:22:25` | `cowrie.command.input` |
| `2026-07-30 10:22:26` | `cowrie.command.input` |
| `2026-07-30 10:22:27` | `cowrie.command.input` |
| `2026-07-30 10:22:27` | `cowrie.command.input` |
| `2026-07-30 10:22:27` | `cowrie.command.failed` |
| `2026-07-30 10:22:28` | `cowrie.log.closed` |
| `2026-07-30 10:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]144` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fb6b44b8e3

| Field | Detail |
|---|---|
| **Source IP** | `2.54.85[.]220` |
| **First Seen** | 2026-07-30 10:28 |
| **Last Seen** | 2026-07-30 10:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:28:42` | `cowrie.session.connect` |
| `2026-07-30 10:28:43` | `cowrie.client.version` |
| `2026-07-30 10:28:43` | `cowrie.client.kex` |
| `2026-07-30 10:28:44` | `cowrie.login.success` |
| `2026-07-30 10:28:44` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.54.85[.]220` to AbuseIPDB if not already reported
- [ ] Block `2.54.85[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e853216f925

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-30 10:28 |
| **Last Seen** | 2026-07-30 10:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:28:49` | `cowrie.session.connect` |
| `2026-07-30 10:28:50` | `cowrie.client.version` |
| `2026-07-30 10:28:50` | `cowrie.client.kex` |
| `2026-07-30 10:28:53` | `cowrie.login.success` |
| `2026-07-30 10:28:53` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36143f3aace

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-07-30 10:33 |
| **Last Seen** | 2026-07-30 10:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:33:34` | `cowrie.session.connect` |
| `2026-07-30 10:33:35` | `cowrie.client.version` |
| `2026-07-30 10:33:35` | `cowrie.client.kex` |
| `2026-07-30 10:33:38` | `cowrie.login.success` |
| `2026-07-30 10:33:38` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70770cafeda8

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-07-30 10:33 |
| **Last Seen** | 2026-07-30 10:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:33:44` | `cowrie.session.connect` |
| `2026-07-30 10:33:44` | `cowrie.client.version` |
| `2026-07-30 10:33:44` | `cowrie.client.kex` |
| `2026-07-30 10:33:47` | `cowrie.login.success` |
| `2026-07-30 10:33:48` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7243fcdef7c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 10:51 |
| **Last Seen** | 2026-07-30 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:51:01` | `cowrie.session.connect` |
| `2026-07-30 10:51:01` | `cowrie.client.version` |
| `2026-07-30 10:51:01` | `cowrie.client.kex` |
| `2026-07-30 10:51:02` | `cowrie.login.success` |
| `2026-07-30 10:51:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:51:02` | `cowrie.direct-tcpip.data` |
| `2026-07-30 10:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31fb145473ce

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-07-30 10:53 |
| **Last Seen** | 2026-07-30 10:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:53:43` | `cowrie.session.connect` |
| `2026-07-30 10:53:44` | `cowrie.client.version` |
| `2026-07-30 10:53:44` | `cowrie.client.kex` |
| `2026-07-30 10:53:45` | `cowrie.login.success` |
| `2026-07-30 10:53:46` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a94eeb33c4

| Field | Detail |
|---|---|
| **Source IP** | `103.103.53[.]44` |
| **First Seen** | 2026-07-30 10:53 |
| **Last Seen** | 2026-07-30 10:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:53:51` | `cowrie.session.connect` |
| `2026-07-30 10:53:52` | `cowrie.client.version` |
| `2026-07-30 10:53:52` | `cowrie.client.kex` |
| `2026-07-30 10:53:54` | `cowrie.login.success` |
| `2026-07-30 10:53:55` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.53[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.103.53[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab27aeb57411

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-07-30 10:53 |
| **Last Seen** | 2026-07-30 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:53:56` | `cowrie.session.connect` |
| `2026-07-30 10:53:56` | `cowrie.client.version` |
| `2026-07-30 10:53:56` | `cowrie.client.kex` |
| `2026-07-30 10:53:58` | `cowrie.login.success` |
| `2026-07-30 10:53:58` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f322d9baf279

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-07-30 10:54 |
| **Last Seen** | 2026-07-30 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:54:05` | `cowrie.session.connect` |
| `2026-07-30 10:54:05` | `cowrie.client.version` |
| `2026-07-30 10:54:05` | `cowrie.client.kex` |
| `2026-07-30 10:54:07` | `cowrie.login.success` |
| `2026-07-30 10:54:07` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273726bafede

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-30 10:54 |
| **Last Seen** | 2026-07-30 10:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:54:12` | `cowrie.session.connect` |
| `2026-07-30 10:54:13` | `cowrie.client.version` |
| `2026-07-30 10:54:13` | `cowrie.client.kex` |
| `2026-07-30 10:54:15` | `cowrie.login.success` |
| `2026-07-30 10:54:16` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71713173cf8

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-30 10:55 |
| **Last Seen** | 2026-07-30 10:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:55:27` | `cowrie.session.connect` |
| `2026-07-30 10:55:28` | `cowrie.client.version` |
| `2026-07-30 10:55:28` | `cowrie.client.kex` |
| `2026-07-30 10:55:30` | `cowrie.login.success` |
| `2026-07-30 10:55:31` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3963d0d1372a

| Field | Detail |
|---|---|
| **Source IP** | `203.124.60[.]46` |
| **First Seen** | 2026-07-30 10:55 |
| **Last Seen** | 2026-07-30 10:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 10:55:36` | `cowrie.session.connect` |
| `2026-07-30 10:55:37` | `cowrie.client.version` |
| `2026-07-30 10:55:37` | `cowrie.client.kex` |
| `2026-07-30 10:55:40` | `cowrie.login.success` |
| `2026-07-30 10:55:41` | `cowrie.direct-tcpip.request` |
| `2026-07-30 10:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.124.60[.]46` to AbuseIPDB if not already reported
- [ ] Block `203.124.60[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30963821f91f

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]58` |
| **First Seen** | 2026-07-30 11:00 |
| **Last Seen** | 2026-07-30 11:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:00:50` | `cowrie.session.connect` |
| `2026-07-30 11:00:51` | `cowrie.client.version` |
| `2026-07-30 11:00:51` | `cowrie.client.kex` |
| `2026-07-30 11:00:54` | `cowrie.login.success` |
| `2026-07-30 11:00:55` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]58` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a183622fcc7

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-07-30 11:08 |
| **Last Seen** | 2026-07-30 11:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:08:45` | `cowrie.session.connect` |
| `2026-07-30 11:08:46` | `cowrie.client.version` |
| `2026-07-30 11:08:46` | `cowrie.client.kex` |
| `2026-07-30 11:08:50` | `cowrie.login.success` |
| `2026-07-30 11:08:51` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06de845ca7dc

| Field | Detail |
|---|---|
| **Source IP** | `14.49.131[.]77` |
| **First Seen** | 2026-07-30 11:25 |
| **Last Seen** | 2026-07-30 11:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:25:25` | `cowrie.session.connect` |
| `2026-07-30 11:25:26` | `cowrie.client.version` |
| `2026-07-30 11:25:26` | `cowrie.client.kex` |
| `2026-07-30 11:25:28` | `cowrie.login.success` |
| `2026-07-30 11:25:28` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.49.131[.]77` to AbuseIPDB if not already reported
- [ ] Block `14.49.131[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565323dab006

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-30 11:28 |
| **Last Seen** | 2026-07-30 11:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:28:48` | `cowrie.session.connect` |
| `2026-07-30 11:28:48` | `cowrie.client.version` |
| `2026-07-30 11:28:48` | `cowrie.client.kex` |
| `2026-07-30 11:28:52` | `cowrie.login.success` |
| `2026-07-30 11:28:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae108abfc278

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-30 11:28 |
| **Last Seen** | 2026-07-30 11:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:28:58` | `cowrie.session.connect` |
| `2026-07-30 11:28:59` | `cowrie.client.version` |
| `2026-07-30 11:28:59` | `cowrie.client.kex` |
| `2026-07-30 11:29:01` | `cowrie.login.success` |
| `2026-07-30 11:29:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b33c22f4bb6

| Field | Detail |
|---|---|
| **Source IP** | `62.91.108[.]146` |
| **First Seen** | 2026-07-30 11:29 |
| **Last Seen** | 2026-07-30 11:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:29:06` | `cowrie.session.connect` |
| `2026-07-30 11:29:06` | `cowrie.client.version` |
| `2026-07-30 11:29:06` | `cowrie.client.kex` |
| `2026-07-30 11:29:07` | `cowrie.login.success` |
| `2026-07-30 11:29:07` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.91.108[.]146` to AbuseIPDB if not already reported
- [ ] Block `62.91.108[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d2199db3ea4

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]17` |
| **First Seen** | 2026-07-30 11:30 |
| **Last Seen** | 2026-07-30 11:30 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:30:06` | `cowrie.session.connect` |
| `2026-07-30 11:30:07` | `cowrie.client.version` |
| `2026-07-30 11:30:07` | `cowrie.client.kex` |
| `2026-07-30 11:30:07` | `cowrie.client.fingerprint` |
| `2026-07-30 11:30:07` | `cowrie.login.failed` |
| `2026-07-30 11:30:07` | `cowrie.login.success` |
| `2026-07-30 11:30:26` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:30:26` | `cowrie.direct-tcpip.ja4` |
| `2026-07-30 11:30:26` | `cowrie.direct-tcpip.data` |
| `2026-07-30 11:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]17` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a8228120f4

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-07-30 11:30 |
| **Last Seen** | 2026-07-30 11:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:30:39` | `cowrie.session.connect` |
| `2026-07-30 11:30:40` | `cowrie.client.version` |
| `2026-07-30 11:30:40` | `cowrie.client.kex` |
| `2026-07-30 11:30:42` | `cowrie.login.success` |
| `2026-07-30 11:30:42` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0d5f59f050

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-07-30 11:35 |
| **Last Seen** | 2026-07-30 11:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:35:39` | `cowrie.session.connect` |
| `2026-07-30 11:35:43` | `cowrie.client.version` |
| `2026-07-30 11:35:43` | `cowrie.client.kex` |
| `2026-07-30 11:35:45` | `cowrie.login.success` |
| `2026-07-30 11:35:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d8ea5817cf

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-07-30 11:43 |
| **Last Seen** | 2026-07-30 11:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:43:57` | `cowrie.session.connect` |
| `2026-07-30 11:43:58` | `cowrie.client.version` |
| `2026-07-30 11:43:58` | `cowrie.client.kex` |
| `2026-07-30 11:44:00` | `cowrie.login.success` |
| `2026-07-30 11:44:01` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccb99e4430fc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-30 11:44 |
| **Last Seen** | 2026-07-30 11:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:44:58` | `cowrie.session.connect` |
| `2026-07-30 11:44:59` | `cowrie.client.version` |
| `2026-07-30 11:44:59` | `cowrie.client.kex` |
| `2026-07-30 11:45:03` | `cowrie.login.success` |
| `2026-07-30 11:45:05` | `cowrie.session.params` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.success` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:05` | `cowrie.command.input` |
| `2026-07-30 11:45:06` | `cowrie.log.closed` |
| `2026-07-30 11:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9af3a60999

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-30 11:46 |
| **Last Seen** | 2026-07-30 11:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:46:55` | `cowrie.session.connect` |
| `2026-07-30 11:46:56` | `cowrie.client.version` |
| `2026-07-30 11:46:56` | `cowrie.client.kex` |
| `2026-07-30 11:46:59` | `cowrie.login.success` |
| `2026-07-30 11:47:01` | `cowrie.session.params` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.success` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:01` | `cowrie.command.input` |
| `2026-07-30 11:47:02` | `cowrie.log.closed` |
| `2026-07-30 11:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79559b3e2630

| Field | Detail |
|---|---|
| **Source IP** | `152.32.230[.]238` |
| **First Seen** | 2026-07-30 11:46 |
| **Last Seen** | 2026-07-30 11:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:46:59` | `cowrie.session.connect` |
| `2026-07-30 11:46:59` | `cowrie.client.version` |
| `2026-07-30 11:47:05` | `cowrie.client.kex` |
| `2026-07-30 11:47:05` | `cowrie.login.success` |
| `2026-07-30 11:47:06` | `cowrie.session.params` |
| `2026-07-30 11:47:06` | `cowrie.command.input` |
| `2026-07-30 11:47:06` | `cowrie.log.closed` |
| `2026-07-30 11:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.230[.]238` to AbuseIPDB if not already reported
- [ ] Block `152.32.230[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f221a79aa3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-30 11:48 |
| **Last Seen** | 2026-07-30 11:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:48:49` | `cowrie.session.connect` |
| `2026-07-30 11:48:50` | `cowrie.client.version` |
| `2026-07-30 11:48:50` | `cowrie.client.kex` |
| `2026-07-30 11:48:53` | `cowrie.login.success` |
| `2026-07-30 11:48:55` | `cowrie.session.params` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.success` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:55` | `cowrie.command.input` |
| `2026-07-30 11:48:56` | `cowrie.log.closed` |
| `2026-07-30 11:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625418820d8b

| Field | Detail |
|---|---|
| **Source IP** | `91.232.247[.]229` |
| **First Seen** | 2026-07-30 11:49 |
| **Last Seen** | 2026-07-30 11:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:49:00` | `cowrie.session.connect` |
| `2026-07-30 11:49:00` | `cowrie.client.version` |
| `2026-07-30 11:49:00` | `cowrie.client.kex` |
| `2026-07-30 11:49:01` | `cowrie.login.success` |
| `2026-07-30 11:49:01` | `cowrie.session.params` |
| `2026-07-30 11:49:01` | `cowrie.command.input` |
| `2026-07-30 11:49:01` | `cowrie.command.failed` |
| `2026-07-30 11:49:02` | `cowrie.log.closed` |
| `2026-07-30 11:49:02` | `cowrie.session.params` |
| `2026-07-30 11:49:02` | `cowrie.command.input` |
| `2026-07-30 11:49:02` | `cowrie.session.file_download` |
| `2026-07-30 11:49:02` | `cowrie.log.closed` |
| `2026-07-30 11:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.232.247[.]229` to AbuseIPDB if not already reported
- [ ] Block `91.232.247[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab941538b21

| Field | Detail |
|---|---|
| **Source IP** | `91.232.247[.]229` |
| **First Seen** | 2026-07-30 11:49 |
| **Last Seen** | 2026-07-30 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:49:03` | `cowrie.session.connect` |
| `2026-07-30 11:49:03` | `cowrie.client.version` |
| `2026-07-30 11:49:03` | `cowrie.client.kex` |
| `2026-07-30 11:49:03` | `cowrie.login.success` |
| `2026-07-30 11:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.232.247[.]229` to AbuseIPDB if not already reported
- [ ] Block `91.232.247[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b38a81973f

| Field | Detail |
|---|---|
| **Source IP** | `91.232.247[.]229` |
| **First Seen** | 2026-07-30 11:49 |
| **Last Seen** | 2026-07-30 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:49:03` | `cowrie.session.connect` |
| `2026-07-30 11:49:03` | `cowrie.client.version` |
| `2026-07-30 11:49:03` | `cowrie.client.kex` |
| `2026-07-30 11:49:04` | `cowrie.login.success` |
| `2026-07-30 11:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.232.247[.]229` to AbuseIPDB if not already reported
- [ ] Block `91.232.247[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae7bfc6f139

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-30 11:50 |
| **Last Seen** | 2026-07-30 11:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:50:44` | `cowrie.session.connect` |
| `2026-07-30 11:50:44` | `cowrie.client.version` |
| `2026-07-30 11:50:44` | `cowrie.client.kex` |
| `2026-07-30 11:50:46` | `cowrie.login.success` |
| `2026-07-30 11:50:48` | `cowrie.session.params` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.success` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.command.input` |
| `2026-07-30 11:50:48` | `cowrie.log.closed` |
| `2026-07-30 11:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130467de2717

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 11:57 |
| **Last Seen** | 2026-07-30 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 11:57:26` | `cowrie.session.connect` |
| `2026-07-30 11:57:26` | `cowrie.client.version` |
| `2026-07-30 11:57:27` | `cowrie.client.kex` |
| `2026-07-30 11:57:27` | `cowrie.login.success` |
| `2026-07-30 11:57:27` | `cowrie.direct-tcpip.request` |
| `2026-07-30 11:57:27` | `cowrie.direct-tcpip.data` |
| `2026-07-30 11:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46bc1f40abfb

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-07-30 12:00 |
| **Last Seen** | 2026-07-30 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:00:40` | `cowrie.session.connect` |
| `2026-07-30 12:00:40` | `cowrie.client.version` |
| `2026-07-30 12:00:40` | `cowrie.client.kex` |
| `2026-07-30 12:00:45` | `cowrie.login.success` |
| `2026-07-30 12:00:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1041229872a2

| Field | Detail |
|---|---|
| **Source IP** | `111.70.13[.]240` |
| **First Seen** | 2026-07-30 12:01 |
| **Last Seen** | 2026-07-30 12:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:01:19` | `cowrie.session.connect` |
| `2026-07-30 12:01:20` | `cowrie.client.version` |
| `2026-07-30 12:01:20` | `cowrie.client.kex` |
| `2026-07-30 12:01:22` | `cowrie.login.success` |
| `2026-07-30 12:01:22` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.13[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.13[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806117f52429

| Field | Detail |
|---|---|
| **Source IP** | `118.113.164[.]137` |
| **First Seen** | 2026-07-30 12:01 |
| **Last Seen** | 2026-07-30 12:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:01:28` | `cowrie.session.connect` |
| `2026-07-30 12:01:29` | `cowrie.client.version` |
| `2026-07-30 12:01:29` | `cowrie.client.kex` |
| `2026-07-30 12:01:31` | `cowrie.login.success` |
| `2026-07-30 12:01:31` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.113.164[.]137` to AbuseIPDB if not already reported
- [ ] Block `118.113.164[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5337a54a1d00

| Field | Detail |
|---|---|
| **Source IP** | `111.17.213[.]162` |
| **First Seen** | 2026-07-30 12:04 |
| **Last Seen** | 2026-07-30 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:04:21` | `cowrie.session.connect` |
| `2026-07-30 12:04:21` | `cowrie.client.version` |
| `2026-07-30 12:04:21` | `cowrie.client.kex` |
| `2026-07-30 12:04:23` | `cowrie.login.success` |
| `2026-07-30 12:04:26` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.213[.]162` to AbuseIPDB if not already reported
- [ ] Block `111.17.213[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b528da337ff

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 12:13 |
| **Last Seen** | 2026-07-30 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:13:02` | `cowrie.session.connect` |
| `2026-07-30 12:13:02` | `cowrie.client.version` |
| `2026-07-30 12:13:02` | `cowrie.client.kex` |
| `2026-07-30 12:13:02` | `cowrie.login.success` |
| `2026-07-30 12:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd56b9f8edc4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 12:13 |
| **Last Seen** | 2026-07-30 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:13:02` | `cowrie.session.connect` |
| `2026-07-30 12:13:02` | `cowrie.client.version` |
| `2026-07-30 12:13:02` | `cowrie.client.kex` |
| `2026-07-30 12:13:02` | `cowrie.login.success` |
| `2026-07-30 12:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4813abba7f73

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 12:13 |
| **Last Seen** | 2026-07-30 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:13:07` | `cowrie.session.connect` |
| `2026-07-30 12:13:07` | `cowrie.client.version` |
| `2026-07-30 12:13:07` | `cowrie.client.kex` |
| `2026-07-30 12:13:07` | `cowrie.login.success` |
| `2026-07-30 12:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0eea13a331

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 12:13 |
| **Last Seen** | 2026-07-30 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:13:07` | `cowrie.session.connect` |
| `2026-07-30 12:13:07` | `cowrie.client.version` |
| `2026-07-30 12:13:07` | `cowrie.client.kex` |
| `2026-07-30 12:13:07` | `cowrie.login.success` |
| `2026-07-30 12:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea8cca987d2

| Field | Detail |
|---|---|
| **Source IP** | `117.34.210[.]196` |
| **First Seen** | 2026-07-30 12:19 |
| **Last Seen** | 2026-07-30 12:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:19:17` | `cowrie.session.connect` |
| `2026-07-30 12:19:18` | `cowrie.client.version` |
| `2026-07-30 12:19:18` | `cowrie.client.kex` |
| `2026-07-30 12:19:21` | `cowrie.login.success` |
| `2026-07-30 12:19:22` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.210[.]196` to AbuseIPDB if not already reported
- [ ] Block `117.34.210[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c70d1877af4

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-30 12:19 |
| **Last Seen** | 2026-07-30 12:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:19:31` | `cowrie.session.connect` |
| `2026-07-30 12:19:32` | `cowrie.client.version` |
| `2026-07-30 12:19:32` | `cowrie.client.kex` |
| `2026-07-30 12:19:33` | `cowrie.login.success` |
| `2026-07-30 12:19:34` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4c6c104c5f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 12:23 |
| **Last Seen** | 2026-07-30 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:23:59` | `cowrie.session.connect` |
| `2026-07-30 12:23:59` | `cowrie.client.version` |
| `2026-07-30 12:23:59` | `cowrie.client.kex` |
| `2026-07-30 12:24:00` | `cowrie.login.success` |
| `2026-07-30 12:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533fab2ae5da

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 12:23 |
| **Last Seen** | 2026-07-30 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:23:59` | `cowrie.session.connect` |
| `2026-07-30 12:23:59` | `cowrie.client.version` |
| `2026-07-30 12:23:59` | `cowrie.client.kex` |
| `2026-07-30 12:24:00` | `cowrie.login.success` |
| `2026-07-30 12:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62b9e4fd13a

| Field | Detail |
|---|---|
| **Source IP** | `118.145.246[.]44` |
| **First Seen** | 2026-07-30 12:27 |
| **Last Seen** | 2026-07-30 12:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:27:46` | `cowrie.session.connect` |
| `2026-07-30 12:27:47` | `cowrie.client.version` |
| `2026-07-30 12:27:47` | `cowrie.client.kex` |
| `2026-07-30 12:27:48` | `cowrie.login.success` |
| `2026-07-30 12:27:49` | `cowrie.session.params` |
| `2026-07-30 12:27:49` | `cowrie.command.input` |
| `2026-07-30 12:27:49` | `cowrie.command.failed` |
| `2026-07-30 12:27:50` | `cowrie.log.closed` |
| `2026-07-30 12:27:51` | `cowrie.session.params` |
| `2026-07-30 12:27:51` | `cowrie.command.input` |
| `2026-07-30 12:27:51` | `cowrie.session.file_download` |
| `2026-07-30 12:27:51` | `cowrie.log.closed` |
| `2026-07-30 12:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.246[.]44` to AbuseIPDB if not already reported
- [ ] Block `118.145.246[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-268dd1afcd92

| Field | Detail |
|---|---|
| **Source IP** | `118.145.246[.]44` |
| **First Seen** | 2026-07-30 12:28 |
| **Last Seen** | 2026-07-30 12:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:28:05` | `cowrie.session.connect` |
| `2026-07-30 12:28:07` | `cowrie.client.version` |
| `2026-07-30 12:28:07` | `cowrie.client.kex` |
| `2026-07-30 12:28:07` | `cowrie.login.success` |
| `2026-07-30 12:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.246[.]44` to AbuseIPDB if not already reported
- [ ] Block `118.145.246[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e07c9b78c8

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-07-30 12:35 |
| **Last Seen** | 2026-07-30 12:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:35:27` | `cowrie.session.connect` |
| `2026-07-30 12:35:28` | `cowrie.client.version` |
| `2026-07-30 12:35:28` | `cowrie.client.kex` |
| `2026-07-30 12:35:31` | `cowrie.login.success` |
| `2026-07-30 12:35:32` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0255e3744a65

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-30 12:35 |
| **Last Seen** | 2026-07-30 12:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:35:42` | `cowrie.session.connect` |
| `2026-07-30 12:35:42` | `cowrie.client.version` |
| `2026-07-30 12:35:42` | `cowrie.client.kex` |
| `2026-07-30 12:35:45` | `cowrie.login.success` |
| `2026-07-30 12:35:46` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52cd479f7b65

| Field | Detail |
|---|---|
| **Source IP** | `223.107.146[.]186` |
| **First Seen** | 2026-07-30 12:36 |
| **Last Seen** | 2026-07-30 12:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:36:17` | `cowrie.session.connect` |
| `2026-07-30 12:36:17` | `cowrie.client.version` |
| `2026-07-30 12:36:17` | `cowrie.client.kex` |
| `2026-07-30 12:36:20` | `cowrie.login.success` |
| `2026-07-30 12:36:21` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.146[.]186` to AbuseIPDB if not already reported
- [ ] Block `223.107.146[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f90ce187af

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]109` |
| **First Seen** | 2026-07-30 12:39 |
| **Last Seen** | 2026-07-30 12:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:39:32` | `cowrie.session.connect` |
| `2026-07-30 12:39:32` | `cowrie.client.version` |
| `2026-07-30 12:39:32` | `cowrie.client.kex` |
| `2026-07-30 12:39:34` | `cowrie.login.success` |
| `2026-07-30 12:39:35` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]109` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6659a135d384

| Field | Detail |
|---|---|
| **Source IP** | `202.111.183[.]30` |
| **First Seen** | 2026-07-30 12:39 |
| **Last Seen** | 2026-07-30 12:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:39:44` | `cowrie.session.connect` |
| `2026-07-30 12:39:45` | `cowrie.client.version` |
| `2026-07-30 12:39:45` | `cowrie.client.kex` |
| `2026-07-30 12:39:47` | `cowrie.login.success` |
| `2026-07-30 12:39:48` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.111.183[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.111.183[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9950253282

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 12:42 |
| **Last Seen** | 2026-07-30 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:42:46` | `cowrie.session.connect` |
| `2026-07-30 12:42:46` | `cowrie.client.version` |
| `2026-07-30 12:42:46` | `cowrie.client.kex` |
| `2026-07-30 12:42:47` | `cowrie.login.success` |
| `2026-07-30 12:42:47` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:42:47` | `cowrie.direct-tcpip.data` |
| `2026-07-30 12:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4ea89b2ac2

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-07-30 12:43 |
| **Last Seen** | 2026-07-30 12:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:43:22` | `cowrie.session.connect` |
| `2026-07-30 12:43:23` | `cowrie.client.version` |
| `2026-07-30 12:43:23` | `cowrie.client.kex` |
| `2026-07-30 12:43:25` | `cowrie.login.success` |
| `2026-07-30 12:43:26` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85639fc4e34

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-07-30 12:43 |
| **Last Seen** | 2026-07-30 12:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:43:31` | `cowrie.session.connect` |
| `2026-07-30 12:43:32` | `cowrie.client.version` |
| `2026-07-30 12:43:32` | `cowrie.client.kex` |
| `2026-07-30 12:43:35` | `cowrie.login.success` |
| `2026-07-30 12:43:37` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b0c22c37b1

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-30 12:46 |
| **Last Seen** | 2026-07-30 12:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:46:40` | `cowrie.session.connect` |
| `2026-07-30 12:46:41` | `cowrie.client.version` |
| `2026-07-30 12:46:41` | `cowrie.client.kex` |
| `2026-07-30 12:46:44` | `cowrie.login.success` |
| `2026-07-30 12:46:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28826d6737b

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-30 12:46 |
| **Last Seen** | 2026-07-30 12:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:46:50` | `cowrie.session.connect` |
| `2026-07-30 12:46:51` | `cowrie.client.version` |
| `2026-07-30 12:46:51` | `cowrie.client.kex` |
| `2026-07-30 12:46:53` | `cowrie.login.success` |
| `2026-07-30 12:46:54` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a28e3c53951

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-30 12:54 |
| **Last Seen** | 2026-07-30 12:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:54:50` | `cowrie.session.connect` |
| `2026-07-30 12:54:50` | `cowrie.client.version` |
| `2026-07-30 12:54:50` | `cowrie.client.kex` |
| `2026-07-30 12:54:51` | `cowrie.login.success` |
| `2026-07-30 12:54:51` | `cowrie.direct-tcpip.request` |
| `2026-07-30 12:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae974dcfe97d

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-30 12:55 |
| **Last Seen** | 2026-07-30 12:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:55:00` | `cowrie.session.connect` |
| `2026-07-30 12:55:01` | `cowrie.client.version` |
| `2026-07-30 12:55:01` | `cowrie.client.kex` |
| `2026-07-30 12:55:02` | `cowrie.login.success` |
| `2026-07-30 12:55:02` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **61** | 2026-07-30 08:55 | 2026-07-30 12:54 | 59m | 0 | `T1592` | 🟠 MEDIUM |
| `104.251.181[.]37` | **17** | 2026-07-30 10:08 | 2026-07-30 10:16 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.30[.]167` | **11** | 2026-07-30 09:43 | 2026-07-30 11:55 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-30 09:13 | 2026-07-30 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **6** | 2026-07-30 09:43 | 2026-07-30 11:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **4** | 2026-07-30 11:30 | 2026-07-30 12:52 | 4m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-30 12:35 | 2026-07-30 12:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-30 10:04 | 2026-07-30 10:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | **3** | 2026-07-30 09:38 | 2026-07-30 09:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-30 11:32 | 2026-07-30 11:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.72.56[.]31` | **2** | 2026-07-30 11:42 | 2026-07-30 11:44 | 2m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-07-30 12:19 | 2026-07-30 12:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.84.166[.]43` | **2** | 2026-07-30 11:56 | 2026-07-30 11:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-30 11:56 | 2026-07-30 11:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-07-30 11:35 | 2026-07-30 11:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `118.145.246[.]44` | 1 | 2026-07-30 12:27 | 2026-07-30 12:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-07-30 12:35 | 2026-07-30 12:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `14.45.131[.]108` | 1 | 2026-07-30 11:15 | 2026-07-30 11:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `144.123.15[.]82` | 1 | 2026-07-30 09:27 | 2026-07-30 09:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.212.92[.]43` | 1 | 2026-07-30 09:00 | 2026-07-30 09:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-07-30 08:55 | 2026-07-30 08:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `184.168.31[.]238` | 1 | 2026-07-30 11:49 | 2026-07-30 11:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `185.94.219[.]88` | 1 | 2026-07-30 12:48 | 2026-07-30 12:48 | 14s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-07-30 11:30 | 2026-07-30 11:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.93[.]17` | 1 | 2026-07-30 11:45 | 2026-07-30 11:46 | 14s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-07-30 09:58 | 2026-07-30 10:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]111` | 1 | 2026-07-30 11:53 | 2026-07-30 11:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-07-30 09:50 | 2026-07-30 09:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.76.28[.]231` | 1 | 2026-07-30 09:39 | 2026-07-30 09:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-07-30 09:15 | 2026-07-30 09:16 | 40s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-07-30 11:25 | 2026-07-30 11:26 | 40s | 0 | `T1592` | 🟢 LOW |
| `42.51.44[.]110` | 1 | 2026-07-30 12:25 | 2026-07-30 12:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-30 09:37 | 2026-07-30 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-30 12:36 | 2026-07-30 12:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-30 10:35 | 2026-07-30 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-30 12:36 | 2026-07-30 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.88.0[.]49` | 1 | 2026-07-30 09:06 | 2026-07-30 09:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-07-30 11:33 | 2026-07-30 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]144` | 1 | 2026-07-30 10:22 | 2026-07-30 10:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.181.232[.]51` | 1 | 2026-07-30 08:56 | 2026-07-30 08:56 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | **1/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **22/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

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
| `194.165.16[.]123` | LT | Flyservers S.A. | **100** ⚠️ | 5 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `62.201.228[.]210` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `95.181.232[.]51` | MA | M247 LTD, Morocco Infrastructure | **100** ⚠️ | 16 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `114.30.223[.]119` | KR | HVHonam | **100** ⚠️ | 50 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |
| `20.84.166[.]43` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `185.2.228[.]48` | LT | Tele2 Lithuania | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 106 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 6 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (41 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 36 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 281 cases |
| Tool 34  | Credential Extractor        | ✅ 118 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 136 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 41 filtered (14.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 82 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 87 priority case(s) shown individually · 40 recon entry/entries in table (13 group(s) consolidating 126 session(s)).

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
_Report time: 2026-07-30T14:11:08Z_

